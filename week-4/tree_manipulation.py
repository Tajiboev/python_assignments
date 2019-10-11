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


def findLCA(T, n1, n2):
    """
    This function returns the lowest common ancestor of two positions in a tree n1 and n2.
    The LCA is the lowest position in T that has both n1 and n2 as descendants.
    :param T: the binary tree
    :param n1: position 1 in T
    :param n2: position 2 in tree
    :return: the LCA of n1 and n2
    """
    root = T._root
    if not root:
	    return root

	# findLCA.n1 and findLCA.n2 are boolean variables to verify nodes exists in tree.
	# Current node Match n1
    if root._element == n1:
	    findLCA.n1 = True

	# Current node Match n2
    if root._element == n2:
	    findLCA.n2 = True

	# Both have been Matched no need to go any further.
	# This condition is added for scenario where both nodes are found no need to
	# further down the tree.
    if findLCA.n1 and findLCA.n2:
        return root

    # if lca_left not null atleast one of the nodes is present in left sub tree
    lca_left = findLCA(root._left, n1, n2)

    # Both have been Matched no need to go any further
    if findLCA.n1 and findLCA.n2:
        return lca_left

    # if lca_right not null at least one of the nodes is present in right sub tree
    lca_right = findLCA(root._right, n1, n2)

    # This condition is added for scenario where one of the requested node is LCA
    # Here we will override the child result received from parent node
    if root._data == n1 or root._data == n2:
        return root

    # if one node is present in left subtree and other in right subtree.
    # this will be your lowest common ancestor
    if lca_left and lca_right:
        return root

    # return if any of the subtree returned a result
    return lca_right if lca_right else lca_left


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

    """ some code showing how to find positions in a binary tree"""
    root = tree.root()
    p_engineering = tree.left(root)
    p_business = tree.right(root)
    print(p_engineering.element())
    print(p_business.element())
    p_man_eng = tree.left(p_engineering)
    print(p_man_eng.element())