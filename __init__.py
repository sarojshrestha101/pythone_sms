import time
import os

def get_allsms():
    getsms = os.system("sudo gammu getallsms").read()
    print(getsms)

def send_sms():
    os.system("clear")
    sms_text = input("Enter message\n")
    sms_no = int(input("Enter Phone no\n"))

    os.system("echo {} | gammu sendsms TEXT {}".format(sms_text, sms_no))

def main():
        print("main function")
        # get_allsms()
        send_sms()


if __name__ == '__main__':
    main()
