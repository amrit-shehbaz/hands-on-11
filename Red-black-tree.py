class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = "red"

    def __str__(self):
        return f"Key: {self.key}, Color: {self.color}, [Left: {self.left.key if self.left is not None else None} | Right: {self.right.key if self.right is not None else None}]"

class RedBlackTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def add(self, key, value):
        if self.isEmpty():
            self.root = Node(key, value)
            self.root.color = "black"
        else:
            self.root = self._add(self.root, key, value)
            self.root.color = "black"

    def _add(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:
            node.value = value
        return self.balance(node)



    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.key = self._min(node.right).key
                node.value = self._min(node.right).value
                node.right = self._delete(node.right, node.key)
        return self.balance(node)

    def balance(self, node):
        if node.color == "red" and node.left is not None and node.left.color == "red":
            if node.right is not None and node.right.color == "red":
                node.color = "red"
                node.left.color = "black"
                node.right.color = "black"
        return node


    def query(self, key):
        return self._query(self.root, key)

    def _query(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._query(node.left, key)
        else:
            return self._query(node.right, key)

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def __str__(self):
        return "======== {RBT} ==========\n" + self._print(self.root) + "========================="

    def _print(self, node):
        if node is None:
            return ""
        return self._print(node.left) + str(node) + "\n" + self._print(node.right)


if __name__=='__main__':
    rbt = RedBlackTree()
    rbt.add(10, "Ten")
    rbt.add(20, "Twenty")
    rbt.add(30, "Thirty")
    rbt.add(40, "Forty")
    print(rbt)
    print("{Root}: ", rbt.root)
    print("{Root Left}: ", rbt.root.left)
    print("{Root Right}: ", rbt.root.right)
    print("Deleting 20 and 30...")
    rbt.delete(20)
    rbt.delete(30)
    print("{Root Left}: ", rbt.root.left)
    print("{Root Right}: ", rbt.root.right)
    print("{Query 10}: ", rbt.query(10))
    print("{Query 40}: ", rbt.query(40))
    print("{Query 30}: ", rbt.query(30))
    print(rbt)
