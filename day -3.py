#police recruit
#l=[1,-1,1,-1,-1,1,1,1]
#p=0
#uns=0
#for i in l:
   # if i==-1:
        #if p>0:
           # p-=1
       # else:
           # uns+=1
   # else:
      #  p+=i
#print(uns)
     
#even or odd 
#num=int(input())
#if num&1==0:
    #print("even")
#else:
    #print("odd")

#swapping of two numbers
#a=10
#b=5
#temp=a
#a=b
#b=temp
#print(a,b)


#def xor_1_to_n(n):
    #if n % 4 == 0:
       # return n
   # elif n % 4 == 1:
        #return 1
    #elif n % 4 == 2:
       # return n + 1
    #else:  
        #return 0

#result = xor_1_to_n(10)
#print(result)


#def XoR(n):
    #if n%4==1:
       # return 1
    #if n%4==2:
       # return n+1
    #if n%4==3:
        #return 0
    #if n%4==0:
        #return n
#l,r=map(int,input().split())
#a=XoR(r)
#b=XoR(l-1)
#print(a^b)