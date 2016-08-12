"""
Find shortest unique prefix to represent each word in the list.

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}

where we can see that
  zebra = z
  dog = dog
  duck = du
  dove = dov

Approach: Build a trie from the words first.

       root
      /    \
     zebra  d
    /      /  \
          uck   o
             /   \
            ve    g
"""


def insert(node, word):
    if len(word) == 0:
        return

    for child in node.children:
        if child.char[0] == word[0]:
            insert(child, word[1:])
            return

    if len(node.char) > 1:
        replacement_node = TrieNode(node.char[1:])
        node.children.append(replacement_node)
        node.char = node.char[0]
        insert(node, word)
        return

    new_node = TrieNode(word)
    node.children.append(new_node)


def find_prefix(node, prefix, word):
    for child in node.children:
        if child.char == word:
            return prefix + [node.char, child.char[0]]

        if child.char[0] == word[0]:
            return find_prefix(child, prefix + [node.char], word[1:])

    return []


class TrieNode():
    def __init__(self, c):
        self.char = c
        self.children = []

    def __repr__(self):
        return '<TrieNode {}>'.format(self.char)


def create_trie(words):
    root = TrieNode('')
    for word in words:
        insert(root, word)
    return root


def shortest_unique_prefix(words):
    trie = create_trie(words)
    return [''.join(find_prefix(trie, prefix=[], word=w)) for w in words]


def test_shortest_unique_prefix_no_words():
    assert shortest_unique_prefix([]) == []


def test_shortest_unique_prefix_one_word():
    assert shortest_unique_prefix(['zebra']) == ['z']


def test_shortest_unique_prefix():
    words = ['zebra', 'dog', 'duck', 'dove']
    assert shortest_unique_prefix(words) == ['z', 'dog', 'du', 'dov']


def test_shortest_unique_prefix_same_start():
    words = ['bearcat', 'bert']
    assert shortest_unique_prefix(words) == ['bea', 'ber']


def test_create_trie_same_start():
    words = ['bearcat', 'bert']
    trie = create_trie(words)

    assert len(trie.children) == 1
    assert trie.children[0].char == 'b'
    assert trie.children[0].children[0].char == 'e'
    assert trie.children[0].children[0].children[0].char == 'arcat'
    assert trie.children[0].children[0].children[1].char == 'rt'


def test_create_trie():
    words = ['zebra', 'dog', 'duck', 'dove']
    trie = create_trie(words)

    assert len(trie.children) == 2
    assert trie.children[0].char == 'zebra'
    assert trie.children[1].char == 'd'

    assert len(trie.children[0].children) == 0
    assert len(trie.children[1].children) == 2

    assert trie.children[1].children[0].char == 'o'
    assert trie.children[1].children[1].char == 'uck'

    assert trie.children[1].children[0].children[0].char == 'g'
    assert trie.children[1].children[0].children[1].char == 've'
