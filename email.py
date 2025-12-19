import smtplib
rec_email = "shailendra834973767@gmail.com"
sender_email = "sonuprajapati83497@gmail.com"
password =input(str("Enter your email password : "))

message = "Hello! This is a test email from Python."
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email)
print("Login Success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to", rec_email)