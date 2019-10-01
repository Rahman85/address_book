import pytest
from model.group import Group
from fixture.application import Application





def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="hfjhgjhghjgj", header="jhgjgghjgj", footer="hjjgjhgj"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

