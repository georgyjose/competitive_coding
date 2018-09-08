import smtplib
import csv

fromaddr = 'thewinger96@gmail.com'

with open('at.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        toaddrs  = row[1]		#Enter recepient address here
        name = row[0]
        msg ="""Subject: Test Mail
        
Hello There, {},
    This is just a test Mail
    Regards
    Geo
        """.format(name).encode('utf-8').strip()
        try:
            username = fromaddr
            password = 'BOSS in COC'					#Enter your password here
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
            print("Mail sent to: ",toaddrs)
        except:
            print("Error at id " + toaddrs)