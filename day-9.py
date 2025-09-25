#  class bikes
    #  def __init__(self,name,cc,m,cost):
    #     self.name = name
    #      self.cc=cc
    #     self.m=m
    #     self.cost=cost
    # def performance(self):
    #     print("abt bikes:",self.name,self)


# class bikes:
#     def perf(self):
#         print("gt","650cc",15,4)
# gt=bikes()
# duke=bikes()


# class cars:
#     wheels=4
#     def __init__(self,mil,car):
#         self.mil=mil
#         self.car=car
#     def get_mil(self):
#         return c1.mil
#     def set_mil(self):
#         c1.mil=12
#     @staticmethod
#     def info():
#         print(" hi hello")
#     @classmethod 
#     def infor(cls):
#         return cls.wheels
# print(cars.infor())
# c1=cars(10,"BMW")
# c2=cars(15,"audi")
# c1.wheels=9
# print(c1.mil)
# print(c1.wheels)
# print(c2.wheels)
# print(c1.get_mil())
# print(c1.set_mil())
# print(c1.mil)


# class pycharm:
#     def execute(self):
#         print("compiling")
#         print("running")
# class myeditor:
#     def execute(self):
#         print("debugging")
#         print("printing error")
#         print("compiling")
#         print("running")
# class laptop:
#     def code(self,ide):
#         ide.execute()
# ide=pycharm()
# lap1=laptop()
# lap1.code(ide)

# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self,other):
#         s3=student(self.m1,self.m2)
#         return s3
#     def __gt__(self,other):
#         r1=self.m1+self.m2
#         r2=other.m1+other.m2
#         if r1>r2:     
#           return True
#         else:
#             return False
    
# s1=student(59,65)
# s2=student(67,85)
# s3=s1+s2
# print(s3.m1)
# print(s3.m2)
# if s1>s2:
#     print("s1 is having more marks then s2")
# else:
#     print("s2 is having more marks then s1")


# class math:
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
# m=math()
# print(m.add(1,2))
# print(m.add(1,2,3))
# print(m.add())


# class Animal:
#     def sound(self):
#         return "Animals make different sounds"
# class Dog(Animal):
#     def sound(self):
#         return "dog barks"
# d=Dog()
# print(d.sound())

#multiple
# class engine:
#     def engine_info(self):
#         return "This is an Engine"
# class wheels:
#     def wheels_info(self):
#         return "car has 4 wheels"
# class car(engine,wheels):
#         def car_info(self):
#             return "this a car"
# c=car()
# print(c.engine_info())
# print(c.wheels_info())
# print(c.car_info())


# class animal:
#     def species(self):
#         return " this is an animal"
# class mammal(animal):
#     def category(self):
#         return " this is a mammal"
# class human(mammal):
#     def speak(self):
#         return "humans can speak"
# h=human()
# print(h.species())
# print(h.category())
# print(h.speak())

#hierarchial inheritance
# class vehicle:
#     def fuel_type(self):
#         return "vehicles can use petrol,diesel and LPG"
# class car(vehicle):
#     def type(self):
#         return "car is a 4-wheeler"
# class bike(vehicle):
#     def type(self):
#         return "bike is a 2 wheeler"
# c=car()
# b=bike()
# print(c.fuel_type())
# print(c.type())
# print(b.type())



#hybrid inheritence
# class A:
#     def display(self):
#         print("Display from A class.")

# class B(A):
#     def display(self):
#         print("Display from B class.")

# class C:
#     def show(self):
#         print("Hi from C.")

# class D(B, C):
#     def display(self):
#         print("Display from D.")

# d1 = D()
# d1.display()
# d1.show()
# print(D.mro())

# arr=[7,5,1,3,8,9,2,6]
# key=2
# for i in range(len(arr)):
#     if (arr[i]==key):
#         print("EF at index:",i)
#         break

#linear search
# def search(list1,key):
#     for i in range(len(list1)):
#         if key==list[i]:
#             print("key found at iindex:",i)
#             break
#     else:
#         print("key not found")
# list1=[2,4,5,6,1,7,8,9,11]
# key=int(input("enter the key:"))
# search(list1,key)

#binary search 
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2   
#         if arr[mid] == target:
#             return mid   
#         elif arr[mid] < target:
#             low = mid + 1   
#         else:
#             high = mid - 1  
#     return -1

#first occurance of the elem using binary search
# def binary_search(list1,n,target):
#    low=0
#    high=n-1
#    result=-1
#    while(low<=high):
#     mid=(low+high)//2
#     if target==list1[mid]:
#         result=mid
#         high=mid-1
#     elif target<list1[mid]:
#         high=mid-1
#     else:
#         low=mid+1
#    return result
# list1=[1,2,2,4,4,5]
# target=4
# n=len(list1)-1
# print(binary_search(list1,n,target))


# #last occurance of the elem using binary search
# def binary_search(list1,n,target):
#    low=0
#    high=n-1
#    result=-1
#    while(low<=high):
#     mid=(low+high)//2
#     if target==list1[mid]:
#         result=mid
#         low=mid+1
#     elif target<list1[mid]:
#         high=mid-1
#     else:
#         low=mid+1
#    return result
# list1=[1,2,2,4,4,5]
# target=4
# n=len(list1)-1
# print(binary_search(list1,n,target))


#find minimum element from rotated array
# nums=[4,5,6,7,1,2]
# low,high=0,len(nums)-1
# while low<high:
#     mid=(low+high)//2
#     if nums[mid]>nums[high]:
#         low=mid+1
#     else:
#         high=mid
# print(nums[low])

#peak value
# nums=[1,2,3,5,1]
# low,high=0,len(nums)-1
# while low<high:
#     mid=(low+high)//2
#     if nums[mid]<nums[mid+1]:
#         low=mid+1
#     else:
#         high=mid
# print(nums(low))