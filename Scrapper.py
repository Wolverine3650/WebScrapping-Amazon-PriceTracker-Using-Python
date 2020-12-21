import requests
from bs4 import BeautifulSoup
import smtplib
URL= 'https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?crid=1Z2O35B19RTGZ&dchild=1&keywords=sony+alpha+7+iii&qid=1599071065&sprefix=sony+alpha%2Caps%2C295&sr=8-1'

header={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=header)
    
    soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    price=price.replace("₹","")
    price=price.replace(",","")
    converted_price=float(price[0:7])
    if(converted_price<150000):
        send_mail()
    print(title.strip())
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('SecondaryEmailID','yourPassword')

    subject='price fell down!'
    body='Check the Amazon Link: https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?crid=1Z2O35B19RTGZ&dchild=1&keywords=sony+alpha+7+iii&qid=1599071065&sprefix=sony+alpha%2Caps%2C295&sr=8-1'
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'secondary mailID',
        'mailID on which you want notification',
        msg
    )
    print('Hey email has been sent')
    server.quit()

check_price()
