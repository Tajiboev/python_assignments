"""
Your task today is to implement the methods (functions) of the DecisionTree class

A Decision Tree is created using as input a file (listing decisions and outcomes).
Once created, it can be used to interact with a user (asking questions and taking a decision
based on the answers provided by the user through command line)
"""

from linked_binary_tree import LinkedBinaryTree

class DecisionTree(LinkedBinaryTree):
    """
    Note that this class "extends" the LinkedBinaryTree class. That is, a DecisionTree inherits the behaviour of
    the LinkedBinaryTree and adds some additional behaviour (= the functions that you have to implement below)
    """


    def create_decision_tree_from_file(self, file_name):
        """
        This function should build a decision tree using a file containing the questions to be asked.
        In particular, each row the file file (see visa_decision_tree.txt for the example used in the main)
        contains 3 comma separated elements:

        <level>,<side>,<question>
        <level>: is the level in the tree of the <question> (e.g. the root is at level 0, children of the root at
                    level 1 etc.
        <side>: indicates whether the <question> is left or right child of its parent

        IMPORTANT: see the file read_write_file_example.py for a mini tutorial about how to read and write
        from a file in Python

        :param file_name: the name of the file
        """
        read_file = open(file_name, "r")
        for line in read_file.readlines():                                  # read lines in file one by one
            values = line.split(',')                                        
            for value in values:
                value = value.strip()  

            print(values)
            prev = values[0]
            if values[0] == '0':
                self._add_root(values[2]) 
            elif values[0] == '1':
                if values[1] == 'left':
                    self._add_left(self.root(), values[2])
                else:
                    self._add_right(self.root(), values[2])
    

            

        read_file.close()

        print(self._root._element)
        pass


    def use_tree(self):
        """
        Once a decision tree is created (see the code in the main to test this function),
        this function allows the user
        to navigate through the decision tree to reach a final decision.
        Input (answers) are provided by the user through command line.

        Your implemantation should handle the fact that the only allowed answers are YES and NO.
        If the user provides a non expected answer (yes, no, hjhsjhj, whatever), the question should be repeated.
        If the user provides a non expected answer 3 times, the execution will abort
        """
        # Hint:
        # "leaves" of the trees are the final decisions, so...while current position is not a leaf
        # do: ask question, get answer (from console), select next position to visit
        pass

    def preorder_indent(self, p, d):
        """
        This is the function to "pretty" print a tree (already seen in previous sessions)
        """
        print(2 * d * '-' + str(p.element()))
        for c in self.children(p):
            self.preorder_indent(c, d + 1)





if __name__ == '__main__':

    """ ============== test take_decision_from_input """
    # loan_dt = DecisionTree()
    # root = loan_dt._add_root("Is the loan required greater than 20,000,000 KRW?\n")
    # root_left = loan_dt._add_left(root, "Is your criminal record empty?\n")
    # root_right = loan_dt._add_right(root, "Have you been in your current job for less than 1 year?\n")
    # loan_dt._add_left(root_left, "Sorry, we cannot lend you any money!\n")
    # crim_rec_r = loan_dt._add_right(root_left, "Have you been in your current job for less than 5 years?\n")
    # loan_dt._add_left(crim_rec_r, "Loan granted at 6pc interest\n")
    # years_r = loan_dt._add_right(crim_rec_r, "Do you currently have more than 50,000,000 KRW in your bank account?\n")
    # loan_dt._add_left(years_r, "Loan granted at 5pc interest\n")
    # loan_dt._add_right(years_r, "Loan granted at 3,5pc interest\n")
    # money_l = loan_dt._add_left(root_right, "Do you currently have more than 30,000,000 KRW in your bank account?\n")
    # money_r = loan_dt._add_right(root_right, "Do you currently have more than 30,000,000 KRW in your bank account?\n")
    # loan_dt._add_left(money_l, "Loan granted at 10pc interest\n")
    # loan_dt._add_right(money_l, "Loan granted at 8pc interest\n")
    # loan_dt._add_left(money_r, "Loan granted at 7pc interest\n")
    # loan_dt._add_right(money_r, "Loan granted at 6pc interest\n")
    # loan_dt.take_decision_from_user_input()


    """ ==================== test create decision tree from file """

    visa_dt = DecisionTree()
    visa_dt.create_decision_tree_from_file("visa_decision_tree.txt")
    root = visa_dt.root()
    visa_dt.preorder_indent(root, 0)
    # print("\n\n ====== Please answer the following questions...")
    # visa_dt.use_tree()

