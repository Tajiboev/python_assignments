"""
Your task today is to implement two functions using the LinkedBinaryTree class.
The first function (build_UNIST_tree) simply returns the organisational structure of schools and departments at UNIST
stored in an instance of a linkd binary tree.
The second function (LCA) finds the common ancestor of two positions in a binary tree.

- Implement the first function
- check the main to test your implementation
- Implement the second function
- Complete the main to test your implementation of the second function

Note that a convenient function for pretty print of the content of a tree is provided below
"""

from linked_binary_tree import LinkedBinaryTree


def build_UNIST_tree():
    """
    This function returns a (linked) binary tree that contains (a simplified and fictitious  version of)
    the organisational structure of schools and departments at UNIST.
    In particular, this function should return the following tree:
    
    UNIST
    --Engineering
    ----Management Engineering
    ------Big datastore
    ------Business process management
    ----Materials Engineering
    ------Wood
    ------Plastic
    --Business
    ----Business Administration

    """
    tree = LinkedBinaryTree()
    root = tree._add_root("UNIST")
    p_eng = tree._add_left(root, "Engineering")
    p_business = tree._add_right(root, "Business")
    p_man_eng = tree._add_left(p_eng, "Management Engineering")
    p_big_data = tree._add_left(p_man_eng, "Big datastore")
    p_bpm = tree._add_right(p_man_eng, "Business process management")
    p_mat_eng = tree._add_right(p_eng, "Materials Engineering")
    p_ba = tree._add_left(p_business, "Business Administration")
    return tree


def lca(root, a, b):

    if not root: return None
    if root == a._node or root == b._node: return root._element
    left = lca(root._left, a, b)
    right = lca(root._right, a, b)
    if left and right: 
        # a & b are on both sides
        return root._element
    else: 
        # EITHER a/b is on one side 
        # OR a/b is not in L&R subtrees
        return left if left else right

def preorder_indent(T, p, d):
    """
    This function allows you to print in a "pretty" way the content of a tree.
    Elements of a tree are traversed in the "preorder" way and printed using indentation.
    It is given, you DO NOT have to complete it!

    To print the entire tree from the root use preorder_indent(tree,tree.root(),0)
    Note: you can use this function to print a sub-tree of T rooted an any position p

    Try to understand the code (in particular, note the recursive implementation!)
    """
    print(2 * d * '-' + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d + 1)

if __name__ == '__main__':
    tree = build_UNIST_tree()

    preorder_indent(tree, tree.root(), 0)
    print('\n')
    """ some code showing how to find positions in a binary tree"""
    root = tree.root()
    p_engineering = tree.left(root)
    p_business = tree.right(root)
    p_me = tree.left(p_engineering)
    p_bd = tree.left(p_me)
    p_bpm = tree.right(p_me)


    # print(p_engineering)
    print('found 1: ', lca(tree._root, p_engineering, p_business))
    print('found 2: ', lca(tree._root, p_engineering, p_me))
    print('found 3: ', lca(tree._root, p_bd, p_bpm))
    print('found 4: ', lca(tree._root, p_business, p_me))
    # print(tree._root)