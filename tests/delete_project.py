from fixture.db import DbFixture
from  model.project import Project
from random import randrange
import operator


def test_delete_project(app, db):
    app.session.login(username="administrator", password="root")
    if len(db.get_project_list()) == 0:
         app.project.create_project(Project(name="Test 8", status='stable', view_state="private", description="Description 7"))
    old_list = db.get_project_list()
    index = randrange(len(db.get_project_list()))
    app.project.delete_project_by_index(old_list[index].name)
    new_list= db.get_project_list()
    del old_list[index]
    assert sorted(old_list, key=operator.attrgetter('id')) == sorted(new_list, key=operator.attrgetter('id'))
