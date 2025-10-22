def letter(a):
    b=['!','@','#','$','%','^','&','*']
    if 0==len(a):
        print("Password is not strong")
    else:
        for i in a:
            if i  in b and len(a)==8 :
                return("Password is strong")
            else:
                return("Password is not strong")
            
       
   #     if 8==len(a) and a in b:
#         print("Password is strong")
#     else:
#         print("Password is not strong")
letter("python123")
letter("my@password")
    