#=================================Imported Modules========================================================================================================
from bs4 import BeautifulSoup
import requests
import smtplib

#======================================================================variable=====================================================================================
my_email = 'carlosmark894@gmail.com'
pswd = 'oftc srpl tiho jhyi '
subject = "Price has changed"
body = "check the jumia link https://www.jumia.com.ng/generic-p9-wireless-bluetooth-headset-headphone-black-257913135.html"
URL = 'https://www.jumia.com.ng/apple-iphone-14-pro-max-6.7-512gb-nano-sim-deep-purple-259217751.html'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64;rv:122.0) Gecko/20100101 Firefox/122.0"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#=================================GUI========================================================================================================
def check_price():
    title = soup.find(class_="-fs20 -pts -pbxs").getText()
    price = soup.find(class_ = "-b -ubpt -tal -fs24 -prxs").get_text()
    conv_price = price.split(',')
    convert_price = conv_price[0] + conv_price[1] + conv_price[2]
    converted_price = int(convert_price[1:])
    print (converted_price)

    if converted_price > 2200000 or converted_price < 2200000:
        send_mail()

def send_mail():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(my_email, pswd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ukwedjedimeji@gmail.com",
            msg = f"Subject: {subject}\n\n{body}")
        connection.close()

if __name__ == "__main__":
    check_price()