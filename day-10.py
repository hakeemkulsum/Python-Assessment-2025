#buble sort
# arr=[8,5,4,9,2,1,3,6]
# n=len(arr)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

#selection sort
# arr=[8,5,4,9,2,1,3,6]
# n=len(arr)
# for i in range(n):
#     min=i
#     for j in range(i+1,n):
#         if arr[min]>arr[j]:
#             min=j 
#     arr[i],arr[min]=arr[min],arr[i]
# print(arr)

#insertion sort
# arr=[5,2,9,1]
# n=len(arr)
# for i in range(1,n):
#     key=arr[i]
#     j=i-1
#     while j>=0 and arr[j]>key:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key
# print(arr)

#quick sort
# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot=arr[0]
#     left=[x for x in arr[1:]if x<= pivot]
#     right=[x for x in arr[1:] if x> pivot]
#     return quick_sort(left)+[pivot]+quick_sort(right)
# arr=[5,3,8,4,2,7,1,10]
# print(quick_sort(arr))

#merge sort
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=merge_sort(arr[:mid])
#     right=merge_sort(arr[mid:])
#     return merge(left,right)
# def merge(left,right):
#     result=[]
#     i=j=0
#     while i<len(left)and j<len(right):
#         if left[i]<right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# arr=[5,2,9,1,6,3]
# print(merge_sort(arr))

#linked list
# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.next=None
# class SLL:
#     def __init__(self):
#         self.head=None
#     def traversal(self):
#         if self.head is None:
#             print("Linked list is empty.")
#         else:
#             temp=self.head
#             while temp!=None:
#                 print(temp.data, end="->")
#                 temp=temp.next

#     def insert_at_beg(self,data):
#         print()
#         new = Node(data)
#         if self.head is None:
#             self.head=new
#         else:
#             new.next=self.head
#             self.head=new
#     def insert_at_end(self, data):
#         print()
#         new1=Node(data)
#         if self.head is None:
#             self.head=new1
#         else:
#             temp=self.head
#             while temp.next!=None:
#                 temp=temp.next
#             temp.next=new1
#     def insert_at_specific(self,data,pos):
#         print()
#         new2=Node(data)
#         temp=self.head
#         for i in range(1,pos-1):
#             temp=temp.next
#         new2.next=temp.next
#         temp.next=new2
#     def del_beg(self):
#         print()
#         temp=self.head
#         self.head=temp.next
#         temp.next=None
#     def del_end(self):
#         print()
#         prev=self.head
#         temp=self.head.next
#         while temp.next!=None:
#             temp=temp.next
#             prev=prev.next
#         prev.next=None
#     def del_particular(self,pos):
#         print()
#         prev=self.head
#         temp=self.head.next
#         for i in range(1,pos-1):
#             temp=temp.next
#             prev=prev.next
#         prev.next=temp.next
#         temp.next=None
#     def sum_all(self):

#        s=0
#        temp=self.head
#     while temp!=None:
#         s=s+temp.data
#         temp=temp.next
#     print(s)
#     def count_all(self):
#       c=0
#       temp=self.head
#     while temp!=None:
#         c=c+1
#         temp=temp.next
#     print(c)
#     def sum_even(self):
#       t=self.head
#     s=0
#     while(t!=None):
#         if(t.data%2==0):
#             s=s+t.data
#         t=t.next
#     print(s)
# def sum_even_nodes(self):
#     t=self.head
#     s=0
#     pos=1
#     while(t!=None):
#         if(pos%2==0):
#             s=s+t.data
#         t=t.next
#         pos=pos+1
#     print(s)

    
# n1=Node(5)
# sll=SLL()
# sll.head=n1
# n2=Node(10)
# n1.next=n2
# n3=Node(15)
# n2.next=n3
# sll.traversal()
# sll.insert_at_beg(2)
# sll.traversal()
# sll.insert_at_end(20)
# sll.traversal()
# sll.insert_at_specific(8,3)
# sll.traversal()  
# sll.sum_all()
# sll.count_all()
# sll.sum_even()
# sum_even_nodes()

