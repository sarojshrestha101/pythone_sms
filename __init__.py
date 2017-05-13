import time
import os

def get_allsms():
    getsms = os.system("gammu getallsms")
    print(getsms)

def send_sms():
    os.system("clear")
    sms_text = input("Enter message\n")
    sms_no = int(input("Enter Phone no\n"))

    output = os.system("echo {} | gammu sendsms TEXT {}".format(sms_text, sms_no))
    print(output)

def main():
        os.system("clear")
        get_allsms()
        # send_sms()


if __name__ == '__main__':
    main()
