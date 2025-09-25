#googly number
#def is_googly(number):
   ## sum_of_squares = sum(int(digit)**2 for digit in str(number))
    #return sum_of_squares % 7 == 0


#num = int(input("Enter a number: "))

#if is_googly(num):
    #print(f"{num} is a Googly number!")
#else:
 #   print(f"{num} is NOT a Googly number.")

#for i in range(5):
 #       if i<3:
      #      break
     #   print(i)

#finding magic number
#num=int(input("enter the number"))

#while num>9:
    #sum=0
    #while num>0:
     #   d=num%10
      #  sum+=d
       # num//=10
    #num=sum
#if num==1:
 #   print("magic number")
#else:
 #   print("not a magic number")

#finding neon number
#num=int(input("enter the number"))
#sqr=num*num
#while sqr:
    #d1=sqr//10
    #d2=sqr%10
#if d1+d2==num:
    #print("neon")
#else:
    #print("not neon")

 #finding niven number
#n = int(input("Enter a number: "))
#digit_sum = sum(int(d) for d in str(n))

#if n % digit_sum == 0:
    #print("Niven number")
#else:
   # print("Not a Niven number")
  

#finding strong number
#import math

#n = int(input("Enter a number: "))
#sum_fact = sum(math.factorial(int(d)) for d in str(n))

#if sum_fact == n:
 #   print("Strong number")
#else:
   # print("Not a Strong number")


#merge a list
#L1=int(input("enter the L1"))
#L2=int(input("enter the L2"))
#merge_list=L1+L2
#print(merge_list)

#removing dublicates
#unique_list = list(dict.fromkeys([1, 2, 2, 3, 4, 1]))
#print(unique_list)

#returns elems which r repeated odd number of times
#nums = [1,3,5,2,4,3,1,5,2]
#result = [x for x in set(nums) if nums.count(x) % 2 == 1]
#print(result)

#sum of three minimum elems in a list
#num = [8,9,1,2,3,4,5,0]
#total = sum(sorted(num)[:3])
#print(total)

#l=[8,5,6,9,10,5,3,11,2,11,12,4]
#even=[]
#odd=[]
  #for in l:
 #  if i%2==0:
     #  even.append(i)
  #    odd.append(i)
   #odd.sort()
 #res=even+odd
  #print(res)

#l=[3,5,1,2,8,6,4,7]
#l1=[]
##
# if i%2==0:
       
      # l1.insert(0,i)
    #else:
        #l1.append(i)
#print(l1)

#for i in range(5):
 #       if i<3:
      #      break
     #   print(i)

