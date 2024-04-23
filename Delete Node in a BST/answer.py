"""s"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self._repr_recursive(self)

    def _repr_recursive(self, node, indent=0):
        result = ""
        if node:
            result += " " * indent + f"TreeNode({node.val})\n"
            result += self._repr_recursive(node.left, indent + 4)
            result += self._repr_recursive(node.right, indent + 4)
        return result


def deleteNode(root, key: int):
    """d"""
    c_n = root
    p_n = None
    if not c_n:
        return root
    while c_n:
        if c_n.val == key:
            break
        if c_n.val < key:
            p_n = c_n
            c_n = c_n.right
        else:
            p_n = c_n
            c_n = c_n.left
    if not c_n:
        return root
    if (c_n.left and not c_n.right) or (not c_n.left and c_n.right):
        if p_n:
            if p_n.left == c_n:
                if c_n.left:
                    p_n.left = c_n.left
                else:
                    p_n.left = c_n.right
            else:
                if c_n.left:
                    p_n.right = c_n.left
                else:
                    p_n.right = c_n.right
        else:
            if c_n.left:
                return c_n.left
            return c_n.right
        return root
    if (c_n.left and c_n.right) or (not c_n.left and not c_n.right):
        if root.val == key:
            root = TreeNode(min_v(c_n), c_n.left,
                            c_n.right) if c_n.left else c_n.left
        else:
            if p_n.left == c_n:
                p_n.left = TreeNode(
                    min_v(c_n), c_n.left, c_n.right) if c_n.right else None
            else:
                p_n.right = TreeNode(
                    min_v(c_n), c_n.left, c_n.right) if c_n.right else None
    else:
        if p_n.left == c_n:
            p_n.left = c_n.left
        else:
            p_n.right = c_n.left
    return root


def min_v(root):
    """f"""
    c_n = root
    p_n = c_n
    c_n = c_n.right
    while c_n.left:
        p_n = c_n
        c_n = c_n.left
    r = c_n.val
    if p_n == root:
        p_n.right = c_n.right
    else:
        if c_n.right:
            p_n.left = c_n.right
        else:
            p_n.left = None
    return r


# tree = TreeNode(5, None, TreeNode(3))
# tree = TreeNode(5, TreeNode(3, None, TreeNode(4)), TreeNode(6))
tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(8)), TreeNode(4)), TreeNode(6, TreeNode(7,None,TreeNode(18)), TreeNode(9)))
print(tree)
print(deleteNode(tree, 5))
