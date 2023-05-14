# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
from timeit import timeit


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        # iterative method
        curNode = self
        while True:
            if value < curNode.value:
                if curNode.left is None:
                    curNode.left = BST(value)
                    break
                else:
                    curNode = curNode.left
            else:
                if curNode.right is None:
                    curNode.right = BST(value)
                    break
                else:
                    curNode = curNode.right
        return self

        # Recursive method
        # if value < self.value:
        #     if self.left:
        #         self.left.insert(value)
        #     else:
        #         self.left = BST(value)
        # else:
        #     if self.right:
        #         self.right.insert(value)
        #     else:
        #         self.right = BST(value)
        # return self

    def contains(self, value):
        # Write your code here.
        # Iterative method
        curNode = self
        while curNode:
            if value < curNode.value:
                curNode = curNode.left
            elif value > curNode.value:
                curNode = curNode.right
            else:
                return True
        return False

        # Recursive method
        # if value == self.value:
        #     return self
        # elif value < self.value and self.left:
        #     return self.left.contains(value)
        # elif value > self.value and self.right:
        #     return self.right.contains(value)
        # else:
        #     return None

    def remove(self, value, parentNode=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        # Iterative method
        curNode = self
        while curNode:
            # first we search for the node
            if value < curNode.value:
                parentNode = curNode
                curNode = curNode.left
            elif value > curNode.value:
                parentNode = curNode
                curNode = curNode.right
            # when we found the node
            else:
                # it might be several cases
                # 1 - has both child nodes
                if (curNode.left is not None and curNode.right is not None):
                    curNode.value = curNode.right.getMinValue()
                    curNode.right.remove(curNode.value, curNode)
                # 2 - parent node doesn't exist aka it's a root
                elif parentNode is None:
                    if curNode.left is not None:
                        curNode.value = curNode.left.value
                        curNode.left = curNode.left.left
                        curNode.right = curNode.left.right
                    elif curNode.right is not None:
                        curNode.value = curNode.right.value
                        curNode.left = curNode.right.left
                        curNode.right = curNode.right.right
                    else:
                        # single node tree, do nothing
                        curNode.value = None
                # 3 - is parent left node
                elif parentNode.left == curNode:
                    parentNode.left = (curNode.left
                                       if curNode.left is not None
                                       else curNode.right)
                # 3 - is parent right node
                elif parentNode.right == curNode:
                    parentNode.right = (curNode.right
                                        if curNode.right is not None
                                        else curNode.left)
                break
        # when node doesn't
        return self

    def getMinValue(self):
        curNode = self
        while curNode.left is not None:
            curNode = curNode.left
        return curNode.value

    def __str__(self) -> str:
        return str(self.value)

    def print_tree_top_left(self):
        # recursive method
        print(str(self.value))
        if self.left:
            self.left.print_tree_top_left()
        if self.right:
            self.right.print_tree_top_left()

    def print_tree_left_top(self):
        if self.left:
            self.left.print_tree_top_left()
        if self.right:
            self.right.print_tree_top_left()
        print(str(self.value))


def evaluateExpressionTree_short(tree):
    # Write your code here.
    if tree.value > 0:
        return tree.value

    leftExpresstion = evaluateExpressionTree(tree.left)
    rightExpression = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftExpresstion + rightExpression
    if tree.value == -2:
        return leftExpresstion - rightExpression
    if tree.value == -3:
        return int(leftExpresstion / rightExpression)
    if tree.value == -4:
        return leftExpresstion * rightExpression


def evaluateExpressionTree(tree):
    # Write your code here.
    return calculateNode(tree, tree.value)


def calculateNode(curNode, operation):
    if operation == -1:
        return (calculateNode(curNode.left, curNode.left.value) +
                calculateNode(curNode.right, curNode.right.value))
    elif operation == -2:
        return (calculateNode(curNode.left, curNode.left.value) -
                calculateNode(curNode.right, curNode.right.value))
    elif operation == -3:
        return int(calculateNode(curNode.left, curNode.left.value) /
                   calculateNode(curNode.right, curNode.right.value))
    elif operation == -4:
        return (calculateNode(curNode.left, curNode.left.value) *
                calculateNode(curNode.right, curNode.right.value))
    else:
        return curNode.value


tree = BST(-1)
nodeL = BST(2)
nodeR = BST(-2)
node3 = BST(4)
node4 = BST(5)
nodeR.left = node3
nodeR.right = node4
tree.left = nodeL
tree.right = nodeR

tree.print_tree_top_left()
print(evaluateExpressionTree_short(tree))
# print(nodeDepth_iter(tree))
# print(nodeDepths_rec(tree))


itr = 1_000_000

for foo in [evaluateExpressionTree, evaluateExpressionTree_short]:
    t = timeit(stmt="foo(tree)", number=itr, globals=globals())
    print(f"{foo.__name__} runed in {t:.6f} seconds")
