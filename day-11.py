# 876.Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# 206.Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# 160.Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.
# Custom Judge:
# The inputs to the judge are given as follows (your program is not given these inputs):
# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.


# 19.Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# inorder,preorder,postorder
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def inorder(root):
#     if root is None:
#         return
#     inorder(root.left)
#     print(root.data, end=" ")
#     inorder(root.right)
# def preorder(root):
#     if root is None:
#         return
#     print(root.data, end=" ")
#     preorder(root.left)
#     preorder(root.right)
# def postorder(root):
#     if root is None:
#         return
#     postorder(root.left)
#     postorder(root.right)
#     print(root.data, end=" ")
# root = Node(10)
# root.left = Node(5)
# root.right = Node(20)
# root.left.left = Node(2)
# root.left.right = Node(8)
# print("Inorder Traversal:")
# inorder(root)
# print("\nPreorder Traversal:")
# preorder(root)
# print("\nPostorder Traversal:")
# postorder(root)

# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def level_order(root):
#     if not root:
#         return
#     queue = [root]
#     while queue:
#         current = queue.pop(0)
#         print(current.val, end=' ')
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# level_order(root)

#sum of even nodes
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def sum_of_nodes(root):
#     if root is None:   
#         return 0
#     return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)


# # Example usage
# if __name__ == "__main__":
#     root = Node(10)
#     root.left = Node(5)
#     root.right = Node(20)
#     root.left.left = Node(2)
#     root.left.right = Node(8)

# print("Sum of all nodes:", sum_of_nodes(root))

# sum of all even nodes
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def sum_of_even_nodes(root):
#     if root is None:
#         return 0
#     current = root.data if root.data % 2 == 0 else 0
#     return current + sum_of_even_nodes(root.left) + sum_of_even_nodes(root.right)
# root = Node(10)
# root.left = Node(5)
# root.right = Node(20)
# root.left.left = Node(2)
# root.left.right = Node(8)
# print("Sum of all even nodes:", sum_of_even_nodes(root))

#height of the node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def height(node):
#     if node is None:
#         return -1   
#     left_height = height(node.left)
#     right_height = height(node.right)
#     return 1 + max(left_height, right_height)
# root = Node(10)
# root.left = Node(5)
# root.right = Node(20)
# root.left.left = Node(2)
# root.left.right = Node(8)
# print("Height of root:", height(root))    
# print("Height of node 5:", height(root.left)) 
# print("Height of node 2:", height(root.left.left)) 

#top view of a node
# from collections import deque
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def top_view(root):
#     if root is None:
#         return []
#     hd_node = {}
#     queue = deque()
#     queue.append((root, 0))
#     while queue:
#         node, hd = queue.popleft()
#         if hd not in hd_node:
#             hd_node[hd] = node.data
        
#         if node.left:
#             queue.append((node.left, hd - 1))
#         if node.right:
#             queue.append((node.right, hd + 1))
#     return [hd_node[x] for x in sorted(hd_node)]
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.right = Node(4)
# root.left.right.right = Node(5)
# root.left.right.right.right = Node(6)
# print("Top view:", top_view(root))  










    