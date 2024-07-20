def main():
    while True:
        print('1.add')
        print('2.subt')
        print('3.multi')
        print('4.divi')
        print('5.exit')
        ch=int(input("enter your choice"))
        if ch==5:
               print('exit prgrm')
               break
    a=int(input("enter first num"))
    b=int(input("enter second num"))
    if ch==1:
         print(add(a,b))
    elif ch==2:
        print(sub(a,b))
    elif ch==3:
        print(mul(a,b))
    elif ch==4:
        print(div(a,b))
    elif ch==5:
         break
