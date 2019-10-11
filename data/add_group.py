from model.group import Group
import random
import string

constant_data = [Group(name="ABC", header="ABC", footer="ABC"),
                 Group(name="", header="", footer="")]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(5)]
