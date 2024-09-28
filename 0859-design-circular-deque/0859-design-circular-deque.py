class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        self.space = k
        self.left = Node(-1, None, None)
        self.right = Node(-1, None, None)
        self.left.next = self.right
        self.right.prev = self.left

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value, self.left, self.left.next)
        self.left.next.prev = new_node
        self.left.next = new_node
        self.space -= 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value, self.right.prev, self.right)
        self.right.prev.next = new_node
        self.right.prev = new_node
        self.space -= 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.left.next == self.right:
            self.left.next = self.right
            self.right.prev = self.left
        else:
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
        self.space += 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.right.prev == self.left:
            self.right.prev = self.left
            self.left.next = self.right
        else:
            self.right.prev = self.right.prev.prev
            self.right.prev.next = self.right
        self.space += 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.left.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0