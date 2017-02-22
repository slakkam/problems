
#  Types for respresenting mobiles:
#
#    mobile ::= branch, branch
#    branch ::= number, structure
#    weight ::= number
#    structure ::= mobile | weight


def make_mobile(left, right):
    return [left, right]

def left_branch(m):
    return m[0]

def right_branch(m):
    return m[1]


def make_branch(length, s):
    return [length, s]

def branch_length(b):
    return b[0]

def branch_structure(b):
    return b[1]


def is_weight(obj):
    return isinstance(obj, (int, float))

def branch_weight(b):
    s = branch_structure(b)
    if is_weight(s):
        return s
    else:
        return total_weight(s)

def total_weight(m):
    return branch_weight(left_branch(m)) + branch_weight(right_branch(m))

def torque(b):
    return branch_weight(b) * branch_length(b)

def is_balanced(s):
    if is_weight(s):
        return True
    else:
        left = left_branch(s)
        right = right_branch(s)
        return torque(left) == torque(right) and \
            is_balanced(branch_structure(left)) and \
            is_balanced(branch_structure(right))

# same structure without rotations

def same_branch(b1, b2):
    return branch_length(b1) == branch_length(b2) and \
        same_structure(branch_structure(b1), branch_structure(b2))

def same_structure(s1, s2):
    if is_weight(s1) and is_weight(s2):
        return s1 == s2
    elif not is_weight(s1) and not is_weight(s2):
        return same_branch(left_branch(s1), left_branch(s2)) and \
            same_branch(right_branch(s1), right_branch(s2))
    else:
        return False

# same structure with rotations

def same_branch_r(b1, b2):
    return branch_length(b1) == branch_length(b2) and \
        same_structure_r(branch_structure(b1), branch_structure(b2))

def same_structure_r(s1, s2):
    if is_weight(s1) and is_weight(s2):
        return s1 == s2
    elif not is_weight(s1) and not is_weight(s2):
        return \
            (same_branch_r(left_branch(s1), left_branch(s2)) and \
                 same_branch_r(right_branch(s1), right_branch(s2))) or \
                 (same_branch_r(left_branch(s1), right_branch(s2)) and \
                      same_branch_r(right_branch(s1), left_branch(s2)))
    else:
        return False

# a few test cases

if __name__ == '__main__':

    m1 = make_mobile(make_branch(4, 6),
                     make_branch(8, make_mobile(make_branch(4, 1),
                                                make_branch(2, 2))))

    m2 = make_mobile(make_branch(6, 2), make_branch(3, 4))

    m3 = make_mobile(make_branch(3, 4), make_branch(6, 2))

    m4 = make_mobile(make_branch(6, make_mobile(make_branch(1, 7),
                                                make_branch(2, 4))),
                     make_branch(3, 2))

    m5 = make_mobile(make_branch(3, 2),
                     make_branch(6, make_mobile(make_branch(2, 4),
                                                make_branch(1, 7))))

    for m in [m1, m2, m3, m4, m5]:
        print(total_weight(m))

    print()

    for m in [m1, m2, m3, m4, m5]:
        print(is_balanced(m))

    print()

    print(same_structure(m1, m1))
    print(same_structure(m1, m2))
    print(same_structure(m4, m5))

    print()

    print(same_structure_r(m1, m1))
    print(same_structure_r(m1, m2))
    print(same_structure_r(m4, m5))

'''
$ python mobile.py
9
6
6
13
13

True
True
True
False
False

True
False
False

True
False
True
'''
