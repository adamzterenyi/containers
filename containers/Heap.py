from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):

    def __init__(self, xs=None):
        super().__init__()
        self.num_nodes = 0
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        ret = True
        if node.left:
            ret &= node.value <= node.left.value
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= node.value <= node.right.value
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        self.num_nodes += 1
        binary_str = bin(self.num_nodes)[3:]
        if self.root is None:
            self.root = Node(value)
        else:
            Heap._insert(self.root, value, binary_str)

    @staticmethod
    def _insert(node, value, binary_str):
        if binary_str:
            if binary_str[0] == '0':
                if len(binary_str) == 1:
                    node.left = Node(value)
                else:
                    Heap._insert(node.left, value, binary_str[1:])
                if node.value > node.left.value:
                    node.value, node.left.value = node.left.value, node.value
            if binary_str[0] == '1':
                if len(binary_str) == 1:
                    node.right = Node(value)
                else:
                    Heap._insert(node.right, value, binary_str[1:])
                if node.value > node.right.value:
                    node.value, node.right.value = node.right.value, node.value
        else:
            node = Node(value)

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        return self.root.value

    def remove_min(self):
        binary_str = bin(self.num_nodes)[3:]
        self.num_nodes -= 1
        last = Heap._remove_bottom_right(self.root, binary_str)
        self.root.value = last
        Heap._trickle(self.root)

    @staticmethod
    def _remove_bottom_right(node, binary_str):
        if node:
            last = None
            if node.left:
                if binary_str[0] == '0':
                    if len(binary_str) == 1:
                        last = node.left.value
                        node.left = None
                        return last
                    else:
                        last = Heap._remove_bottom_right(node.left,
                                                         binary_str[1:])
                if binary_str[0] == '1':
                    if len(binary_str) == 1:
                        last = node.right.value
                        node.right = None
                        return last
                    else:
                        last = Heap._remove_bottom_right(node.right,
                                                         binary_str[1:])
            return last

    @staticmethod
    def _trickle(node):
        if node:
            if node.right and node.left:
                if node.value > node.right.value < node.left.value:
                    node.value, node.right.value = node.right.value, node.value
                    Heap._trickle(node.right)
                if node.value > node.left.value < node.right.value:
                    node.value, node.left.value = node.left.value, node.value
                    Heap._trickle(node.left)
            if node.left:
                if node.value > node.left.value:
                    node.value, node.left.value = node.left.value, node.value
                    Heap._trickle(node.left)
