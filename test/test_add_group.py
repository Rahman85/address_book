from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="hfjhgjhghjgj", header="jhgjgghjgj", footer="hjjgjhgj"))

def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


