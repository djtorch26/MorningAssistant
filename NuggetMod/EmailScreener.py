# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:12:33 2020

@author: Dawson
"""

import imaplib as imap
import os
import email
#import FileManager as fmanager
#import html2text

#from email.header import decode_header

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
MAIL_USER = str(os.getenv('MAIL_USER'))
MAIL_PASSWORD = str(os.getenv('MAIL_PASSWORD'))

def readMail():
    try:
        mail = imap.IMAP4_SSL(SMTP_SERVER)
        mail.login(MAIL_USER,MAIL_PASSWORD)
        status, messages = mail.select("INBOX")
        
        status, data = mail.search(None,'ALL')
        mail_ids = []
        
        messages = int(messages[0])
        
        #create new File for specific days emails
        fmanager.openNuggetFile()
        
        for block in data:
            mail_ids += block.split()
        
        for i in mail_ids:
            status, data = mail.fetch(i,'(RFC822)')
            
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    mail_from = message['from']
                    mail_subject = message['subject']
                    
                    if message.is_multipart():
                        mail_content = ''
                        
                        for part in message.get_payload(None,True):
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    
                    else:
                        mail_content = message.get_payload()
                        
                    fmanager.appendNuggetFile(f'From: {mail_from}')
                    fmanager.appendNuggetFile(f'Subject: {mail_subject}')
                    fmanager.appendNuggetFile(f'Content: {mail_content}')
        
        imap.close()
        imap.logout()
    except Exception as e:
        print(e)

        
readMail()


"""

txt = '.txt'
        emailNug = "EmailNugget"
        Nuggets = (emailNug + fmanager.timeNow() + txt)
        
        NugFile = open(os.path.join('C:\\Users\\bamba\\Documents\\Python_Scripts\\MorningAssistant\\MorningNuggets\\' + Nuggets), "a")




for i in range(messages, messages-N, -1):
            res, msg = mail.fetch(str(i), '(RFC822)')
            
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject = decode_header(msg['subject'])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    
                    email_from = msg['from']
                    NugFile.write("From : " + email_from + '\n')
                    NugFile.write("Subject : " + subject + '\n')
                    
                    
                    if msg.is_multipart():
                        #iteration over parts of email
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                body = part.get_payload(decode=True).decode()
                            except:
                                print('exception error, no body')
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                NugFile.write("body : " + body)
                            #elif "attachment" in content_disposition:
                                #pass
                    else: 
                        content_type = msg.get_content_type()
                        body = msg.get_payload(decode=True).decode()
                        if content_type =="text/plain":
                            NugFile.write(body)
                        #if content_type == "text/HTML":
                         #   NugFile.write(body)
                        else:
                            NugFile.write("body : " + body)
"""