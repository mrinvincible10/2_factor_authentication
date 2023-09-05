import tkinter as tk
import qrcode as qr
import pyotp
from PIL import Image
import time


def one_time() :
    key = "NeuralNineMySuperSecretKey"
    totp = pyotp.TOTP(key)
    print(totp.now())

    print("Enter the OTP.")
    print("Remeber the OTP is only valid for 30 seconds.")
    x=input()
    while totp.verify(x) is False:
        if totp.verify(x) is False:
           print("The code does not match.Try again.")

        print("Enter the OTP.")
        print("Remeber the OTP is only valid for 30 seconds.")
        x = input()
        if totp.verify(x) is True:
            print("You have successfully cleared 2-Factor Authentication.")
def scannercode():
    key = "NeuralNineMySuperSecretKey"
    totp = pyotp.totp.TOTP(key).provisioning_uri(name="excel",issuer_name='NeuralNine App')
    totp_z =pyotp.TOTP(key)
    qr.make(totp).save("qr1.png")
    z= Image.open("qr1.png")
    z.show()

    print("Enter the OTP.")
    print("Remeber the OTP is only valid for 30 seconds.")
    x = input()
    while totp_z.verify(x) is False:
        if totp_z.verify(x) is False:
            print("The code does not match.Try again.")

        print("Enter the OTP.")
        print("Remeber the OTP is only valid for 30 seconds.")
        x = input()
        if totp_z.verify(x) is True:
            print("You have successfully cleared 2-Factor Authentication.")


username=input("Enter username:")
password=input("Enter password:")

print("Now going through 2 factor authentication.")
check1=input("Enter username:")
check2=input("Enter password:")
if check1==username and check2==password:
    root = tk.Tk()
    tk.Label(text='Choose one of the following:')
    i = tk.IntVar()
    v1 = tk.Radiobutton(text='OTP',value=1,command='otp',variable=i).pack()
    v2 = tk.Radiobutton(text='QR Code',value=2,command='qrcod',variable=i).pack()
    tk.Button(root,text='Submit',command=root.destroy).pack()

    root.mainloop()

    if i.get()==1:
        one_time()

    if i.get()==2:
        scannercode()

else:
    print("Credentials do not match")