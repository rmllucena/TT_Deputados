import os
import pyautogui
import time
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from datetime import date
import datetime


#abre arquivo
os.startfile("TT_Deputados.pbix")
time.sleep(15)
#seleciona barra de tarefas
pyautogui.moveTo(900, 1050)
time.sleep(3) 
#seleciona arquivo
pyautogui.moveRel(0, -10)  # move mouse 10 pixels down
time.sleep(5)
#clica na janela aberta
pyautogui.click(900, 1000)  # move mouse 10 pixels down
time.sleep(10) 
#dando enable no pbi
pyautogui.click(1000, 590)
time.sleep(5) 
#atualiza
pyautogui.click(670, 110)
time.sleep(120)
#clica no file
pyautogui.click(50, 50)
time.sleep(5)
#clica no export
pyautogui.click(50, 370)
time.sleep(3)
#clica no export as pdf
pyautogui.click(400, 230)
time.sleep(30)
#clica para fechar o pdf
pyautogui.click(1890, 10)
time.sleep(3)
#clica para fechar o pbi
pyautogui.click(1890, 10)
time.sleep(3)
#clica para salvar o pbi
pyautogui.click(1000, 560)
time.sleep(3)

print("PDF Feito e Salvo")   












   
fromaddr = "autrmllucena@gmail.com"
toaddr = "autrmllucena@gmail.com"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
data_atual = date.today()
minuto = datetime.datetime.now().minute
hora = datetime.datetime.now().hour
print("{} - {}:{}".format(data_atual,hora,minuto))

# storing the subject  
msg['Subject'] = "TT_Deputados-{} - {}:{}".format(data_atual,hora,minuto)
  
# string to store the body of the mail 
body = "Teste"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

import os
output = [dI for dI in os.listdir("C:\\Users\\Romulo\\AppData\\Local\\Temp\\Power BI Desktop\\") 
                                  if os.path.isdir(os.path.join("C:\\Users\\Romulo\\AppData\\Local\\Temp\\Power BI Desktop\\",dI))]

caminho = []
for sub in reversed(output):
    if sub[0:3] == "pri":
        caminho.append(sub)



# open the file to be sent  
filename = "TT_Deputados.pdf"
attachment = open("C:\\Users\\Romulo\\AppData\\Local\\Temp\\Power BI Desktop\\" + caminho[-1] +"\\TT_Deputados.pdf",
                  "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "auto1989") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 





print("PDF enviado")