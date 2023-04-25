
def fn(root):
    def leftFun(node, l):
        if not node:
            return l
        return max(leftFun(node.left, 0), rightFun(node.right, l+1))

    def rightFun(node, l):
        if not node:
            return l
        return max(leftFun(node.left, l+1), rightFun(node.right, 0))

    return max(leftFun(root, 0), rightFun(root, 0))

