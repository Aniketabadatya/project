# Email Validation Using PYTHON
# EX:a@g.com/in
# 1stch is alphabet,counts of @ is 1,postion of [.] is 3rd/4th from right side,and no extra " ",",","@",".","_" and others spl ch

email = input( "Enter your Email Id: ")

k,d = 0,0
if len(email) >= 6:
    if email[0].isalpha():
        if (("@" in email) and (email.count("@") == 1)):
            if ((".") in email) and (email.count(".") == 1):
                if ((email[-4] == ".") ^ (email[-3] == ".")):
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            #if i = i.uppercase():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if k == 1  or d == 1:
                        print("invalid email")
                    else:
                        print("valid email")
                else:
                    print("invaild email")
            else:
                print("invalid email")
        else:
            print("Invalid email")
    else:
        print("invalid email")
else:
    print("invalid email")
                        
                
            

