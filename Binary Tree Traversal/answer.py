class Node:
    def __init__(self, n, L=None, R=None):
        self.left = L
        self.right = R
        self.data = n


def pre_order(node):
    """D"""
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

def in_order(node):
    """D"""
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)
def post_order(node):
    """D"""
    if node is None:
        return []
    return  post_order(node.left) + post_order(node.right) + [node.data]
if __name__ == '__main__':
    a = Node(5)
    b = Node(10)
    c = Node(2)
    d = Node("leaf")
    a.left = b
    a.right = c
    c.left = d
    assert pre_order(a) == [a.data, b.data, c.data, d.data]
    assert pre_order(b) == [b.data]
    assert pre_order(c) == [c.data, d.data]
    print(pre_order(a))
    print(in_order(a))
    assert in_order(a) == [b.data, a.data, d.data, c.data]
    assert in_order(b) == [b.data]
    assert in_order(c) == [d.data, c.data]
    