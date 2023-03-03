
import datetime
import random
DateTime = datetime.datetime.now()


def passwordencryption(encryptpass):
    first = encryptpass[0]
    last = encryptpass[-1]
    encryptpass = last + encryptpass[1:-1] + first
    epass = encryptpass
    epass = epass.replace('i', '!')
    epass = epass.replace('a', '@')
    epass = epass.replace('S', '$')
    epass = epass.replace('J', '?')
    return epass


def signin():
    print('Enter Username')
    sign_in_user = input()
    userfile = open('users.txt', 'r')
    if sign_in_user in userfile.read():
        print("please enter password")
        userpass = input()
        print("re-enter password")
        userpassc = input()
        if userpass == userpassc:
            userpasscheck = passwordencryption(userpass)
            with open('users.txt') as f:
                for line in f:
                    if userpasscheck in line:
                        print("Welcome! have a nice day")
                        status = 'OK'
                        logfile = open("log.txt", 'a')
                        logfile.write("[%s]::[%s]::[%s]" % (sign_in_user, DateTime, status) + '\n')
                        logfile.close()
        elif userpass != userpassc:
            print("There was an error goodbye")
            status = 'BAD PASS'
            logfile = open("log.txt", 'a')
            logfile.write("[%s]::[%s]::[%s]" % (sign_in_user, DateTime, status) + '\n')
            logfile.close()


def passwordcreate(userpass):
    passconstraint = '!', '@', '$', ':', '?'
    while len(userpass) < 7:
        print("Enter a password that is atleast 7 characters")
        userpass = input()
    while any(ve in userpass for ve in passconstraint):
        print("Password must not contain !@$:?, enter password again")
        userpass = input()
    print("Re-Enter password")
    passwordcheck = input()
    if userpass == passwordcheck:
        encryptedpassword = passwordencryption(userpass)
    return encryptedpassword


def usercreate():
    print("Enter First name")
    firstname = input()
    print("Enter Last name")
    newusernumber = random.randint(1000, 9999)
    lastname = input()
    newusername = firstname[:1]+lastname
    newusername = ("%s%d" % (newusername, newusernumber))
    print(newusername)
    print("Enter a password")
    NewPassword = input()
    encryptedpassword = passwordcreate(NewPassword)
    userfile = open('users.txt', 'a')
    userfile.write("Username:[%s]::Password:[%s]" % (newusername, encryptedpassword)+'\n')
    userfile.close()
    status = 'New'
    logfile = open("log.txt", 'a')
    logfile.write("[%s]::[%s]::[%s]" % (newusername, DateTime, status)+'\n')
    logfile.close()
    print("Account created")
    print("Your user name is:", newusername)

def main():
    print("Welcome please enter sign in or create new user")
    Choice = input()

    if Choice == "sign in":
       signin()
    elif Choice == "create new user":
        usercreate()

main()
