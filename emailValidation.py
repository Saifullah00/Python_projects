import re

email_conditions= "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_input = input("Enter your Email : ")

if re.search(email_conditions, user_input):
    print("      Great!! right email id 😎\n")
else :
    print("      Oops!! wrong email id 🙄\n")