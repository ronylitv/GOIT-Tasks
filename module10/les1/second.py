class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = Node(1)
# root.left = Node(7)
# root.right = Node(5)
# root.left.left = Node(3)
#
# print(root.val)
# print(root.left.val, root.right.val)


def insert_to_node(root, val):
    if not root:
        return Node(val)
    elif root.val <= val:
        root.right = insert_to_node(root.right, val)
    else:
        root.left = insert_to_node(root.left, val)
    return root


values = [8, 3, 6, 10, 1, 14, 13, 4, 7]
root = None
for i in values:
    root = insert_to_node(root, i)

print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.right.right.val)
