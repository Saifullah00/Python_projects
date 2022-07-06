import qrcode as qr

print("\nMake your Website, Profile, Resume etc...\nAS a Qr CODE\n")
user_input = input("Enter your link address : ")
# img = qr.make("https://www.linkedin.com/in/saifullah-b83a25205/")
img = qr.make(user_input)
img.save("qr.png" )
