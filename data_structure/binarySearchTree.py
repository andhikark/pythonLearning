from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.min_value()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def BFSTraversal(self):
        result = []
        if self is None:
            return result

        queue = deque([self])

        while queue:
            node = queue.popleft()
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def inorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inorderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorderTraversal()

        return elements

    def preorderTraversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.preorderTraversal()

        if self.right:
            elements += self.right.preorderTraversal()

        return elements

    def postorderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.postorderTraversal()

        if self.right:
            elements += self.right.postorderTraversal()

        elements.append(self.data)

        return elements

    def max_value(self):
        if self.right:
            return self.right.max_value()
        else:
            return self.data

    def min_value(self):
        if self.left:
            return self.left.min_value()
        else:
            return  self.data

    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.height()
        elif self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    def count_leaf(self):
        if self.left is None and self.right is None:
            return 1
        leaf = 0
        if self.left:
            leaf += self.left.count_leaf()
        if self.right:
            leaf += self.right.count_leaf()
        return leaf

    def level_value(self, val, level=0):
        if self is None:
            return -1  # Node not found, return -1
        if self.data == val:
            return level  # Node found at current level
        if self.left:
            left_level = self.left.level_value(val, level + 1)  # Check left subtree
            if left_level != -1:
                return left_level
        if self.right:
            right_level = self.right.level_value(val, level + 1)  # Check right subtree
            return right_level
        return -1  # Node not found


def tree(elements):
    print("Build tree with these elements: ", elements)
    root = Node(elements[0])

    for i in range(1, len(elements)):
        root.insert(elements[i])

    return root


if __name__ == '__main__':
    BStree = tree([17, 4, 1, 20, 9, 23, 18, 34])
    #              17
    #         4          20
    #       1    9    18    23
    #                          34
    print(BStree.inorderTraversal())
    print(BStree.preorderTraversal())
    print(BStree.postorderTraversal())
    print(BStree.search(1))
    print(BStree.search(20))
    print(BStree.search(11))
    print(BStree.max_value())
    BStree.delete(34)
    #              17
    #         4          20
    #       1    9    18    23
    print(BStree.inorderTraversal())
    print(BStree.height())
    print(BStree.count_leaf())
    print(BStree.level_value(17))
    print(BStree.BFSTraversal())







