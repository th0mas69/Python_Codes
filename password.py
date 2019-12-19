import re
password = input("enter the password:")
flag = 0
while True:
    if (len(password)<6):
        flag = -1
        break
    elif not re.search('[0-9]',password):
        flag = -1
        break
    elif not re.search('[!@#$%^&*_+]',password):
        flag = -1
        break
    elif re.search('[/s]',password):
        flag = -1
        break
    else:
        flag = 1
        print("Its Valid Password")
        break
if flag == -1:
    print("Not a Valid Password, try again")
    
