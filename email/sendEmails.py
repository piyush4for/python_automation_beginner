import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()   #started connection
conn.starttls()  # used tls encryption
conn.ehlo()

conn.login('jaanakshitij@gmail.com','*************')
#Limit 100 msg per day
conn.sendmail('jaanakshitij@gmail.com','jaanakshitij@gmail.com','Subject: So long... \n\nDear Piyush,\nThis message is send by smtp.\n\n-piyush')
conn.quit()