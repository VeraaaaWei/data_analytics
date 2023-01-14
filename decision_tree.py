import numpy as np


class Node():
    def __init__(self, return_value=None, split_value=None, attribute_name=None, attribute_index=None, branches=[]):
        """
        This class implements a tree structure with multiple branches at each node.

        If this is a leaf node, return_value must hold the predicted class.
            In a leaf node, branches is an empty list, and all of
            attribute_name, attribute_index, and split_value should be None.

        If this is not a leaf node, return_value should be None.
            In non-leaf node, branches should be a list of Node objections,
            and all of attribute_name, attribute_index, and split_value
            should have non-None values.

        Arguments:
            branches (list): List of Node classes. Used to traverse the tree. In a
                binary decision tree, the length of this list is either 2 (for
                non-leaf nodes) or 0 (at a leaf node).
            attribute_name (str): If not a leaf, contains name of attribute
                that the tree splits the data on. Used for visualization (see
                `DecisionTree.visualize`).
            attribute_index (float): If not a leaf, contains the  index of the
                feature vector for the given attribute. Should correspond to
                self.attribute_name.
            split_value (int or float): If not a leaf, contains the value that
                data should be compared to along the given attri bute.

            return_value (int): If this is a leaf, the value that this node
                should return.
        """

        self.branches = [] if branches is None else branches
        self.attribute_name = attribute_name
        self.attribute_index = attribute_index
        self.split_value = split_value
        self.return_value = return_value


class DecisionTree():
    def __init__(self, attribute_names):
        """
        This class implements a binary decision tree learner for examples with
        categorical attributes. Use the ID3 algorithm for implementing the Decision
        Tree: https://en.wikipedia.org/wiki/ID3_algorithm

        A decision tree is a machine learning model that fits data with a tree
        structure. Each branching point along the tree marks a decision (e.g.
        today is sunny or today is not sunny). Data is filtered by the value of
        each attribute to the next level of the tree. At the next level, the process
        starts again with the remaining attributes, recursing on the filtered data.

        Which attributes to split on at each point in the tree are decided by the
        information gain of a specific attribute.

        Here, you will implement a binary decision tree that uses the ID3 algorithm.
        Your decision tree will be contained in `self.tree`, which consists of
        nested Node classes (see above).

        Args:
            attribute_names (list): list of strings containing the attribute names for
                each feature (e.g. chocolatey, good_grades, etc.)

        """
        self.attribute_names = attribute_names
        self.tree = None

    def _check_input(self, features):
        if features.shape[1] != len(self.attribute_names):
            raise ValueError(
                "Number of features and number of attribute names must match!"
            )

    def visualize(self, branch=None, level=0):
        """
        Visualization of a decision tree. Implemented for you to check your work and to
        use as an example of how to use the given classes to implement your decision
        tree.
        """
        if branch is None:
            branch = self.tree
        self._visualize_helper(branch, level)

        if branch.branches is not None and len(branch.branches) > 0:
            left, right = branch.branches
            if left is not None:
                self.visualize(left, level + 1)

            if left is not None and right is not None:
                tab_level = "  " * level
                print(f"{level}: {tab_level} else:")

            if right is not None:
                self.visualize(right, level + 1)

    def _visualize_helper(self, tree, level):
        """
        Helper function for visualize a decision tree at a given level of recursion.
        """
        tab_level = "  " * level
        if len(tree.branches) == 0:
            print(f"{level}: {tab_level} Predict {tree.return_value:d}")
        elif len(tree.branches) == 2:
            print(f"{level}: {tab_level} if {tree.attribute_name} <= {tree.split_value:.1f}:")

    def fit(self, features, targets):
        """
        Takes in the features as a numpy array and fits a decision tree to the targets.
        You shouldn't need to edit this function, but you need to implement the
        self._create_tree function that is called.

        Args:
            features (np.array): numpy array of size NxF containing features, where N is
                number of examples and F is number of features.
            targets (np.array): numpy array containing class labels for each of the N
                examples.
        Returns:
            None: It should update self.tree with a built decision tree.
        """
        self._check_input(features)

        self.tree = self._create_tree(
            features=features,
            targets=targets,
            used_attributes=[],
             default=0,
        )

    def _create_tree(self, features, targets, used_attributes, default):
        '''
        Create a decision tree recursively.
        1. If no data remains, return a leaf node with return_value `default`
            (e.g., if features and targets are both empty)

        2. If all targets are the same, return a leaf node with
            that target as the return_value

        3. For each attribute, compute the information gain from splitting on it

        3.1. If that is in `used_attributes`, instead set information gain to -1
            to prevent us from reusing it
        3.2. If all attributes are used, return a leaf node with the mode class

        3.3.1 If at least one attribute, has a non-negative information gain,
            select `best_attribute` with the largest information gain;
        3.3.2 Split data (feature & target) according to attribute values,
            where: `attribute_values = features[:, best_attribute]`;
        3.3.3 If that attribute's values are binary, split on 0.5;
            Otherwise, split on the median of the attribute values;

        3.4 Create a non-leaf node with the specified attribute_name,
              attribute_index, and split_value, and then RECURSIVELY
              set build its branches using self._create_tree.
              After recursing, return the node.
        '''
        #1. If no data remains, return a leaf node with return_value `default`
        if len(features) == 0 and len(targets) == 0:
            return Node(default)
        #2. If all targets are the same, return a leaf node with
        #    that target as the return_value
        all_the_same = True
        for i in range(1, len(targets)):
            if targets[i] != targets[i-1]:
                all_the_same = False
                break
        if all_the_same:
            return Node(targets[0])
        #3. For each attribute, compute the information gain from splitting on it
        max_IG = -1
        target_attribute = -1
        for i in range(len(features[0])):
            #3.1 if it is in used_attributes, set IG = -1
            if i in used_attributes:
                IG = -1
            else:
                IG = information_gain(features, i, targets)
                if max_IG < IG:
                    max_IG, target_attribute = IG, i
        #3.2 if all of them are used, return the most common class
        if len(used_attributes) == len(features[0]):
            vals, counts = np.unique(targets, return_counts=True)
            return Node(vals[np.argmax(counts)])
        attr_val = np.array(features)[:, target_attribute]
        #split data based on the val type
        if attr_val[0] == 1 or attr_val[0] == 0:  # binary
            threshold = 0.5
        else:
            threshold = np.median(attr_val)
        l_x, l_y, r_x, r_y = [], [], [], []
        for i, val in enumerate(attr_val):
            if val < threshold:
                l_x.append(features[i])
                l_y.append(targets[i])
            elif val > threshold:
                r_x.append(features[i])
                r_y.append(targets[i])
        l_x, l_y, r_x, r_y = np.array(l_x), np.array(l_y), np.array(r_x), np.array(r_y)
        return Node(attribute_name=self.attribute_names[target_attribute], attribute_index=target_attribute,
                        split_value=threshold,
                        branches=[self._create_tree(l_x, l_y, used_attributes + [target_attribute], default),
                                  self._create_tree(r_x, r_y, used_attributes + [target_attribute], default)])


    def predict(self, features):
        """
        Predicts label for each example in features using the trained model.

        Args:
            features (np.array): numpy array of shape (n, d)
                where n is number of examples and d is number of features.
        Returns:
            predictions (np.array): numpy array of size N array which has the predicitons
                for the input data.
        """
        self._check_input(features)
        Y = []
        for sample in features:
            cur_node = self.tree
            while cur_node is not None:
                if cur_node.return_value is not None:
                    Y.append(cur_node.return_value)
                    break
                if sample[cur_node.attribute_index] <= cur_node.split_value:
                    cur_node = cur_node.branches[0]
                else:
                    cur_node = cur_node.branches[1]
        return np.array(Y).reshape(len(Y), 1)


        # self.branches = [] if branches is None else branches
        # self.attribute_name = attribute_name
        # self.attribute_index = attribute_index
        # self.split_value = split_value
        # self.return_value = return_value



def entropy(targets):
    """
    Helper function: compute Shannon entropy given targets
    See: https://en.wikipedia.org/wiki/Entropy_(information_theory)

    Note that if a target appears 0 times, it does not
    factor into the entropy computation. This is equivalent
    to defining `0 * log(0) = 0`.
    """
    _, counts = np.unique(targets, return_counts=True)
    H_S = 0.0
    for c in counts:
        p_c = c / np.sum(counts)
        H_S -= p_c * np.log2(p_c)

    return H_S


def information_gain(features, attribute_index, targets):
    """
    Information gain is how a decision tree makes decisions on how to create
    split points in the tree. Information gain is measured in terms of entropy.
    The goal of a decision tree is to decrease entropy at each split point as
    much as possible. This function should work perfectly or your decision tree
    will not work properly.

    Information gain is a central concept in many machine learning algorithms.
    In decision trees, it captures how effective splitting the tree on a
    specific attribute will be for the goal of classifying the training data
    correctly.  Consider data points S and an attribute A; we'll split S into
    two data points.

    For binary A: S(A == 0) and S(A == 1)
    For continuous A: S(A < m) and S(A >= m), where m is the median of A in S.

    Together, the two subsets make up S. If the attribute A were perfectly correlated with
    the class of each data point in S, then all points in a given subset will have the
    same class. Clearly, in this case, we want something that captures that A is a good
    attribute to use in the decision tree. This something is information gain. Formally:

        IG(S,A) = H(S) - H(S|A)

    where H is information entropy. Recall that entropy captures how orderly or chaotic
    a system is. A system that is very chaotic will evenly distribute probabilities to
    all outcomes (e.g. 50% chance of class 0, 50% chance of class 1). Machine learning
    algorithms work to decrease entropy, so as to make predictions that are
    accurate on testing data. Formally, H is defined as:

        H(S) = sum_{c in (groups in S)} -p(c) * log_2 p(c)

    To elaborate: for each group c in S, you compute the probability (or weight) of c:

        p(c) = (# of elements of group c in S) / (total # of elements in S)

    Then you compute the term for this group:

        -p(c) * log_2 p(c)

    Note: if p(c) is 0, we define `-p(c) * log_2 p(c)` as 0. You can see how
        we handle in the `entropy` helper function, to avoid how numpy
        defines `0 * log(0) = 0 * -inf = nan`.

    Then compute the sum across all groups: either classes 0 and 1 for binary data, or
    for the above-median and below-median classes for continuous data. The final number
    is the entropy. To gain more intution about entropy, consider the following - what
    does H(S) = 0 tell you about S?

    Information gain is an extension of entropy. The equation for information gain
    involves comparing the entropy of the set and the entropy of the set when conditioned
    on selecting for a single attribute (e.g. S(A == 0)).

    For more details: https://en.wikipedia.org/wiki/ID3_algorithm#The_ID3_metrics

    Args:
        features (np.array): numpy array containing features for each example.
        attribute_index (int): which column of features to take when computing the
            information gain
        targets (np.array): numpy array containing labels corresponding to each example.

    Returns:
        information_gain (float): information gain if the features were split on the
            attribute_index.
    """
    feature_m = features[:, attribute_index]
    sz = len(feature_m)
    Counter = {}
    for i, v in enumerate(feature_m):
        if v in Counter :
            Counter[v].append(targets[i])
        else:
            Counter[v] = [targets[i]]
    HS, HSA = entropy(targets), 0
    for c in Counter:
        num_val = len(Counter[c])
        _, cnt = np.unique(Counter[c], return_counts=True)
        temp = 0
        for c in cnt:
            temp += (c / num_val * np.log2(c / num_val))
        HSA -= temp * (num_val / sz)
    return HS - HSA



if __name__ == '__main__':
    # construct a fake tree
    attribute_names = ['Outlook', 'Temp', 'Wind']
    decision_tree = DecisionTree(attribute_names=attribute_names)
    root = Node(
        attribute_name="Outlook", attribute_index=0,
        split_value=0.5, branches=[])

    left = Node(
        attribute_name="Temp", attribute_index=1,
        split_value=0.5, branches=[])

    left_left = Node(
        attribute_name=None, attribute_index=None,
        return_value=1, branches=None)

    left_right = Node(
        attribute_name=None, attribute_index=None,
        return_value=0, branches=None)

    right = Node(
        attribute_name=None, attribute_index=None,
        return_value=1, branches=None)

    # left.branches = [left_left, left_right]
    # root.branches = [left, right]
    # decision_tree.tree = root.fit()
    # decision_tree.visualize()
    # This call should output:
    # 0:  if Outlook <= 0.5:
    # 1:    if Temp <= 0.5:
    # 2:      Predict 1
    # 1:    else:
    # 2:      Predict 0
    # 0:  else:
    # 1:    Predict 1
