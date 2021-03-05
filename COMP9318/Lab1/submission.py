## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    for n in range(x + 1):
        if n * n == x:
            return n
        elif n * n > x:
            return n - 1


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    current_iter = 1
    while current_iter < MAX_ITER:
        x_new = x_0 - f(x_0) / fprime(x_0)
        if abs(x_0 - x_new) < EPSILON:
            return x_new
        x_0 = x_new
        current_iter += 1
    return x_0


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    num = 0
    t = None
    while num < len(tokens) - 1:
        if tokens[num + 1] == '[':
            tmp_tree, num = need_new_tree(tokens, num)
        else:
            tmp_tree = Tree(tokens[num])
        if t is None:
            t = tmp_tree
        else:
            t.add_child(tmp_tree)

    return t


def need_new_tree(tokens, num):
    new_tree = Tree(tokens[num])
    num = num + 2
    while tokens[num] != ']':
        if tokens[num + 1] == '[':
            temp_tree, num = need_new_tree(tokens, num)
            new_tree.add_child(temp_tree)
        else:
            new_tree.add_child(Tree(tokens[num]))
        num += 1
    return new_tree, num


def max_depth(root):  # do not change the heading of the function
    if root is None:
        return 0

    depth = 1
    max_depth = 1
    vector = [(root, depth)]
    while len(vector) is not 0:
        tmp = vector.pop()
        if len(tmp[0].children) > 0:
            depth = tmp[1] + 1
            max_depth = max(depth, max_depth)
            for child in tmp[0].children:
                vector.append((child, depth))

    return max_depth


