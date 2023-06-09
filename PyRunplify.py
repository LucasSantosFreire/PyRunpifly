import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

host_gmail = "smtp.gmail.com"
host_outlook = "smtp.office365.com"
port = "587"

def send_mail(host, port, email, passw, new_name, error_handler, attach_handler):
		server = smtplib.SMTP(host, port)
		server.starttls()        
		server.login(email, passw)
		if(error_handler == False):
			body = 'Your code has finished running, your results have been saved in the ' + new_name + ' archive.'
			subject = 'Your code has finished running!'
			msg = MIMEMultipart()
			msg['From'] = email
			msg['To'] = email
			msg['Subject'] = subject
			msg.attach(MIMEText(body, 'plain'))
			if(attach_handler == True):
				arq_path = new_name+".ipynb"
				arq_bin = open(arq_path, 'rb')           
				attach_core = MIMEBase('application', 'octet-stream')
				attach_core.set_payload(arq_bin.read())
				encoders.encode_base64(attach_core)              
				attach_core.add_header('Content-Disposition', 'attachment', filename=new_name+'.ipynb')
				arq_bin.close()
				msg.attach(attach_core)
			server.sendmail(msg['To'], msg['From'], msg.as_string())
		elif(error_handler == True):
			body = 'Your code has finished running with some erros, check your results  in the ' + new_name + ' archive.'
			subject = 'Your code has finished running with some errors!'
			msg = MIMEMultipart()
			msg['From'] = email
			msg['To'] = email
			msg['Subject'] = subject
			msg.attach(MIMEText(body, 'plain'))
			if(attach_handler == True):
				arq_path = new_name+".ipynb"
				arq_bin = open(arq_path, 'rb')           
				attach_core = MIMEBase('application', 'octet-stream')
				attach_core.set_payload(arq_bin.read())
				encoders.encode_base64(attach_core)              
				attach_core.add_header('Content-Disposition', 'attachment', filename=new_name+'.ipynb')
				arq_bin.close()
				msg.attach(attach_core)
			server.sendmail(msg['To'], msg['From'], msg.as_string())                     
		server.quit()
        
def init_worker(path, new_name='executed_notebook', email=None, passw=None, flag=None, attach_handler=False):
	error_handler = False
	with open(path) as f:
		nb = nbformat.read(f, as_version=4)    
		ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
		try:
			out = ep.preprocess(nb)
		except CellExecutionError:
			out = None
			error_handler = True
		finally:            
			with open(new_name + '.ipynb', 'w', encoding='utf-8') as f:
				nbformat.write(nb, f)                
        #Notification for gmail users
	if(flag=="gmail"):
		send_mail(host_gmail, port, email, passw, new_name, error_handler, attach_handler) 
		print("Finished")
        #Notification for outlook users
	elif(flag=="outlook"):
		send_mail(host_outlook, port, email, passw, new_name, error_handler, attach_handler)
		print("Finished")
	else:
		print("Finished")
    

    
