class TrieNode:
    def __init__(self, char, parent=None):
        self._char = char
        self._parent = parent
        self._children = []

    @property
    def is_root(self):
        return self._parent is None

    @property
    def is_leaf(self):
        return len(self._children) == 0

    @property
    def char(self):
        return self._char

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent


class Trie:
    def __init__(self):
        self._root = TrieNode('#')

    def is_empty(self):
        return self._root is None

    def depth(self, node):
        d = 0
        current_node = node
        while current_node.parent is not None:
            d += 1
            current_node = current_node.parent
        return d

    def preorder(self, func):
        self._preorder(self._root, func)

    def _preorder(self, node, func):
        func(node)
        for child in node.children:
            self._preorder(child, func)

    def postorder(self, func: TrieNode) -> None:
        self._postorder(self._root, func)

    def _postorder(self, node, func):
        for child in node.children:
            self._postorder(child, func)
        func(node)

    def print_node(self, node: TrieNode) -> None:
        print(node.char)

    def print_trie(self):
        func = self.print_node
        self.preorder(func)

    def add_word(self, string):
        current_node = self._root
        for char in string:
            add_to_node = True
            for child in current_node.children:
                if child.char == char:
                    current_node = child
                    add_to_node = False
                    break
            if add_to_node:
                new_node = TrieNode(char, current_node)
                current_node.children.append(new_node)
                current_node = new_node
