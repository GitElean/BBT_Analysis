class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    #Diccionario height para los nodos
    height = {}

    #Encontramos la altura de cada nodo
    def computeHeight(node):
        if node is None:
            return 0
        left_height = height.get(node.left, computeHeight(node.left))
        right_height = height.get(node.right, computeHeight(node.right))
        node_height = max(left_height, right_height) + 1
        height[node] = node_height
        return node_height

    computeHeight(root)

    #Chequeamos que este balanceado
    def check_balanced(node):
        if node is None:
            return True
        left_height = height.get(node.left, 0)
        right_height = height.get(node.right, 0)
        return abs(left_height - right_height) <= 1 and check_balanced(node.left) and check_balanced(node.right)

    return check_balanced(root)
