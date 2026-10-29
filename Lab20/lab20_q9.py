p=input("enter password")
while True:
    l = list(p)
    e = []
    if len(p)<8:
        e.append("Password is short")
    if p.lower()=="password":
        e.append("password is not allowed")
    if not any ('A' <= char <= 'Z' for char in l):
        e.append("atleast one uppercase letter needed")
    if not any('a' <= char <= 'z' for char in l):
        e.append("atleast one lowercase letter needed")
    if not any('0' <= char <= '9' for char in l):
        e.append("atleast one digit needed")
    if not any(char=='!' or char=='@' or char=='#' or char=='$' or char=='%' or char=='&' or char=='*' for char in l):
        e.append("atleast one special character needed")
    if any(char==' ' for char in l):
        e.append("no space allowed")
    if len(e)>0:
        print(e)
        p=input("enter password")
    else:
        print("password is correct")
        break


