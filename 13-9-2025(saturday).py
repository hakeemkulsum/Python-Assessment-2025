n=int(input())
for i in range(1,n+1): #row
    #for j in range(i):
       #print("*",end=" ")
    #print("")
    print(i*"*")


n=int(input())
for i in range(n,0,-1):
    print(i*"  *  ")


n=int(input())
for i in range(n,0,-1):  #row 
    # for j in range(n-i):
    #     print(" ",end=" ")
    # for j in range(i):
    #     print("*",end=" ")
    # print("")
    print((n-i)*" ",end=" ")
    print(i*"  *    ")


n=int(input())
for i in range(n,n+1):
    for j in range(i):
        print(i*("*"))