#!/usr/bin/python

import smtplib

# aux.  send email
def send_email(recv, sub, content):
    s= smtplib.SMTP('localhost')
    msg="""Subject: """+sub+"""
    """
    s.sendmail("illumina_archive_script@xxx.com", recv, msg)
    s.quit()

