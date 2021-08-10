class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# f1 = Node(5)
# f1.left = Node(3)
# f1.right = Node(7)
# f1.left.left = Node(1)
# f1.left.right = Node(4)
#
# print(f1.val)
# print(f1.left.val, f1.right.val)
# print(f1.left.left.val, f1.left.right.val)


def insert_to_node(root, val):
    if not root:
        return Node(val)
    elif root.val <= val:
        root = insert_to_node(root.right, val)
    else:
        root = insert_to_node(root.left, val)
    return root

root = None
for i in [2, 5, 7, 10, 4, 5, 6, 7]:
    root = insert_to_node(root, i)
