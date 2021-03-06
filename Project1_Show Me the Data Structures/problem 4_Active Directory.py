class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        if not user:
            raise ValueError("user must be non-empty")
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True

    if len(group.get_groups()) == 0:
        return False

    for sub_group in group.get_groups():
        found = is_user_in_group(user, sub_group)

        if found:
            return True

    return False


if __name__ == "__main__":

    # test
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent))  # True

    # edge test case 1 (empty user)
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = ""
    try:
        sub_child.add_user(sub_child_user) # must raise exception: "user must be non-empty"
    except ValueError as v:
        print(v)

    # edge case 2 (user not found in the group)
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent)) # False

    # edge case 3 (user does not have parents)
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"

    child.add_group(sub_child)
    print(is_user_in_group(sub_child_user, parent)) # False


