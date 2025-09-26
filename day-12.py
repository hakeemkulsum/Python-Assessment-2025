# 235. Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# 455. Assign Cookies
# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
# Example 1:
# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.

# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


#sum of adjacent distances
# def sum_of_adjacent_distances(arr):
#     total = 0
#     for i in range(len(arr) - 1):
#         total += abs(arr[i+1] - arr[i])
#     return total
# arr = [1, 3, 6, 2]
# print("Sum of adjacent distances:", sum_of_adjacent_distances(arr))


# security key:
# data=int(input())
# s=str(abs(data))
# from collections import Counter
# cnt=Counter(s)
# print(cnt)
# repeats=sum(1 for v in cnt.values() if v>1)
# if repeats>0:
#     print(repeats)
# else:
#     print(-1)



# encode as number:
# n=int(input())
# m=int(input())
# s=str(n)
# d={}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# res=0
# for i in d:
#     if d[i]==m:
#         res=i
# print(res)



# even odd 
# l=list(map(int,input().split()))
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.append(i)
# for i in l:
#     if i%2!=0:
#         l1.append(i)
# print(l1)



# secret message agency:
# s=input()
# c=0
# for i in s:
#     if i.isalnum():
#         c+=1
# d=len(s)-c
# print(d)



# perfect square:
# areas=[79,77,54,81,48,34,25,16]
# count=0
# for a in areas:
#     i=1
#     while i*i<=a:
#         if i*i==a:
#             count+=1
#             break
#         i+=1
# print(count)