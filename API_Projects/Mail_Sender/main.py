#=================================Imported Modules========================================================================================================
import smtplib
import datetime as dt
import random
#=================================GUI========================================================================================================

my_email = 'carlosmark894@gmail.com'
pswd = 'oftc srpl tiho jhyi '

now=dt.datetime.now()
weekday = now.weekday()
if weekday == 0 or 1 or 2 or 3 or 4 or 5 or 6:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=pswd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ukwedjedimeji@gmail.com", 
            msg=f'Subject:Daily Quotes\n\n{quote}')
        connection.close()
