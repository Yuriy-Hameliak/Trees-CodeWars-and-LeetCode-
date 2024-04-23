from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
def tree_by_levels(node):
    if not node:
        return []
    res = []
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        if node is not None:
            res.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
    return res
if __name__ == '__main__':
    assert tree_by_levels(None) == []
    print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
     
    assert tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)) == [1, 2, 3, 4, 5, 6]