import re 

with open("input.txt","r") as file:
    text=file.read()
    
emails=re.findall(r'[\w.-]+@[\w.-]+\.\w+',text)

with open("emails.txt","w") as file:
    for email in emails:
        file.write(email+"\n")
        
print("Email addresses extracted successfully!")
print("Total emails found:",len(emails))