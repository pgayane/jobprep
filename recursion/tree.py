class Node:

    def __init__(self, value, l=None, r=None):
        self.value = value
        self.left = l
        self.right = r


def sum_of_tree(root):

    if root is None:
        return 0

    return root.value + sum_of_tree(root.left) + sum_of_tree(root.right)

if __name__ == '__main__':
    tree = Node(3, 
                    Node(1,Node(2),Node(4)),
                    Node(10,Node(5),Node(6))
                )
    print sum_of_tree(tree)
