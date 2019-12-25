'''1～100以内能被3整除，但不能被5整除的数'''
a=0
b=0
while a<100:
    a += 1
    if a%3==0 and a%5!=0 :
        print(a,end= ' ')
        b+=1
        if b%5==0:
            print( )
print('\n能被3整除，但不能被5整除的数有%d个'%b)

