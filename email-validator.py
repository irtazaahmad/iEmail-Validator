import requests

email_address = input("Enter the email : ")
response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': email_address})

status = response.json()['status']
if status == "valid":
  print("email is valid")
elif status == "invalid":
  print("email is invalid")
else:
  print("email was unknown")