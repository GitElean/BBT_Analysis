import BBT_dac as dac

    # Create a sample binary tree
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
root = dac.TreeNode(1)
root.left = dac.TreeNode(2)
root.right = dac.TreeNode(3)
root.left.left = dac.TreeNode(4)
root.left.right = dac.TreeNode(5)

#Verfica si el árbol esta balanceado
if dac.is_balanced(root):
    print("The binary tree is balanced.")
else:
    print("The binary tree is not balanced.")