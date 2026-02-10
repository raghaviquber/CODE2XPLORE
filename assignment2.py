student=input("Student ID: ")
email=input("Email ID: ")
password=input("Password: ")
refcode=input("Referral: ")
if student[0]=="C" and student[1]=="S" and student[2]=="E" and student[3]=="-" and ('0'<=student[4]<="9")  :
    if ('a' <= email[0] <= 'z') or ('A' <= email[0] <= 'Z') or ('0' <= email[0] <= '9') and email.count("@")==1 and email.count(".")>=1  and email.count(" ")==0 and email[-1]=="u" and email[-2]=="d" and email[-3]=="e":
        if len(password)>=8 and ('A'<=password[0]<='Z') and password.count(" ")==0 and any(char.isdigit() for char in password):
            if refcode[0]=="R" and refcode[1]=="E" and refcode[2]=="F" and ('0'<=refcode[3]<='9') and ('0'<=refcode[4]<='9') and refcode[5]=="@":
                print("APPROVED")
            else:
                print("REJECTED")
        else:
            print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")