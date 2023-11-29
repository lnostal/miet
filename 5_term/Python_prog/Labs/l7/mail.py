


from smtplib import SMTP
from imaplib import IMAP4
import re

email = 'b8677961-20ca-4ba2-8c77-8bd4961b3af4@mailslurp.mx'
email_to = 'e2065923-fb6a-4e6b-a3e4-fb2c06b22866@mailslurp.mx'

#SMTP
smtp_host ='mailslurp.mx'
smtp_port = 2587
smtp_u = 'FQbYu4JvbFYMROGRTfzpwrdaafGiBCun'
smtp_p = 'T6aWDATSxv3tvwhaZmYOuY9w96NiJodZ'

#IMAP
imap_host ='mailslurp.click'
imap_port = 1143
imap_u = '10FqWyi8lYwrtb58gLhRfh5Kr0Mwx9Kz'
imap_p = '1ma9pIRM6mXCrASEjruI40i5acLNtoDx'


def send_message(message):
    msg = 'Subject: {}\n\n{}'.format('Lab 7', message)

    with SMTP("{}:{}".format(smtp_host, smtp_port)) as smtp:
        smtp.starttls()
        smtp.login(smtp_u, smtp_p)
        smtp.sendmail(
            email,
            email_to,
            msg)



def get_message():
    with IMAP4(imap_host, imap_port) as IMAP:
        IMAP.login(imap_u,imap_p)
        l = IMAP.select(email) # кол-во писем в ящике
        _, msgnums = IMAP.search(None, 'FROM', '"mail"')

        l = msgnums[0].split()
        _, d = IMAP.fetch(l[-1], '(RFC822)')
        print("Subject: ", getValue("Subject: ", d[0][1]))
        print("Text: ", getValue("Content-Transfer-Encoding: 7bit\\r\\n\\r\\n", d[0][1]))


def header(text):
    return str.encode("(?<={})(([A-Za-z0-9]+( |)+)+)(?=\\r)".format(text))

def getValue(find, text):
    regex = header(find)
    r = re.findall(regex, text)
    if len(r) > 0:
        return r[0][0]
    return ""

def valid(email):
    r = re.fullmatch("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)
    if r == None:
        return False
    return True
