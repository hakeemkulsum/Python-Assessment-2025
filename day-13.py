#bingo online lottery game
# def encrypt_char(ch, k):
#     if 'a' <= ch <= 'z':  
#         base = ord('a')
#     elif 'A' <= ch <= 'Z':  
#         base = ord('A')
#     else:
#         return ch  
#     encrypted = chr((ord(ch) - base + k) % 26 + base)
#     return encrypted
# ch, k = input("Enter character and key: ").split()
# k = int(k)
# print(encrypt_char(ch, k))

#
# ch='h'
# k=3
# lower='abcdefghijklmnopqrstuvwxyz'
# upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# if  ch in lower:
#     idx=lower.index(ch)
#     out=lower[(idx+k)%26]
# elif ch in upper:
#     idx=upper.index(ch)
#     out=upper[(idx+k)%26]
# else:
#     out=ch
# print(out)


# pooled cab service:
# a,b=30,50
# l=[29,38,12,48,39,55]
# for i in l:
#     if a<=i and b>=i:
#         print(i,end=" ")

# kth shortest processing queue:
# n,a=7,4
# l=[9 ,-3, 8, -6, -7, 18, 10]
# l.sort()
# print(l[a])
# print(l)

# #converting graph input into adjacency list
# from collections import defaultdict
# edges=[['A','B'],['B','D'],['A','C'],['C','E'],['E','F']]
# adj_list=defaultdict(list)
# for u,v in edges:


#bfs traversal
# def BFS(graph,start):
#     visited=set()
#     q=[start]
#     while q:
#         n=q.pop(0)
#         if n not in visited:
#             print(n,end=" ")
#             visited.add(n)
#             q.extend(graph[n])
# graph={
#     'A':['B','C'],
#     'B':['A','D','E'],
#     'C':['A','F'],
#     'D':['B'],
#     'E':['B','F'],
#     'F':['C','E']
# }
# BFS(graph,'A')

#DFS Traversal
# def DFS(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     if start not in visited:
#         print(start, end=" ")
#         visited.add(start)
#         for neighbour in graph[start]:
#             DFS(graph, neighbour, visited)
# graph = {
#     'A': ['B','C'],
#     'B': ['A','D','E'],
#     'C': ['A','F'],
#     'D': ['B'],
#     'E': ['B','F'],
#     'F': ['C','E']
# }
#  DFS(graph, 'A')

# 997. Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
# Example 1:
# Input: n = 2, trust = [[1,2]]
# Output: 2






