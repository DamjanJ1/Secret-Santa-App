import smtplib
# UI
import tkinter as tk
import random
from tkinter.constants import COMMAND


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 400)
canvas1.pack()



label2 = tk.Label(root, text='Enter all the names using a space inbetween')
label2.config(font=('helvetica', 14))
canvas1.create_window(300, 100, window = label2)

entry2 = tk.Entry (root)
canvas1.create_window(300, 125, window = entry2 )


label3 = tk.Label(root, text='Enter all the emails im order using a space inbetween')
label3.config(font=('helvetica', 14))
canvas1.create_window(300, 200, window=label3)


entry3 = tk.Entry (root)
canvas1.create_window(300, 225, window = entry3 )










def main():




    namess = entry2.get()
    n1 = namess.split(" ")



    emailss = entry3.get()
    e1 = emailss.split(" ")




    n2 =random.sample( n1, len(n1))
    i=0
    for word in n2:
        if word == n1[i]:
            label10 = tk.Label(root, text= "( Click again! )")
            canvas1.create_window(300, 250, window=label10)
            return
        
        i = i +1 
    
    

# Ova e za prakjanje mail





    # se vnesuva nekokoj nov acc koj ima vkluceno trust other apps
    
    gmail_user = '************'
    gmail_password = '*********'


    for i in range(0 , len(n1)):

        sent_from = gmail_user
        to = e1[i]
        subject = 'Your Secret Santa friend is:'
        body = n2[i] 
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            print ("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….",ex)




button1 = tk.Button(text='Create Christmas magic', command=main)
canvas1.create_window(300, 300, window=button1)
root.mainloop()


