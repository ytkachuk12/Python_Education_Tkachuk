actor = {"name": "John Cleese", "rank": "awesome"}


def get_last_name():
    if actor["name"].split() == -1:
        raise NameError
    else:
        return actor["name"].split()[1]


get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())