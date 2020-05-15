class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def bst_sequences(node):
    if node == None:
        return None
    if node.left == None and node.right == None:
        return [[node.val]]

    left_sequences = bst_sequences(node.left)
    right_sequences = bst_sequences(node.right)

    combined = combine(left_sequences, right_sequences)

    for seq in combined:
        seq.insert(0, node.val)

    return combined 

def combine(seqs1, seqs2):
    if not seqs1:
        return seq2
    if not seqs2:
        return seq1

    combined = []
    for seq1 in seqs1:
        for seq2 in seqs2:
            combined.extend(weave(seq1, seq2))
    
    return combined

def weave(seq1, seq2):
    if not seq1:
        return [seq2.copy()]
    if not seq2:
        return [seq1.copy()]

    res1 = weave(seq1[1:], seq2)
    res2 = weave(seq1, seq2[1:])

    for res in res1:
        res.insert(0, seq1[0])
    for res in res2:
        res.insert(0, seq2[0])
    
    res = res1 + res2
    return res.copy()

import math

def minimal_tree(values):
    num_values = len(values)
    if num_values == 0:
        return None
    if num_values == 1:
        return Node(values[0])

    min_height = int(math.ceil(math.log2(num_values + 1)))
    mid = 2 ** (min_height - 1) - 1
    curr = Node(values[mid])
    curr.left = minimal_tree(values[:mid])
    curr.left.parent = curr
    curr.right = minimal_tree(values[mid+1:])
    curr.right.parent = curr
    return curr

n = minimal_tree(range(5))
s = bst_sequences(n)
print(s)