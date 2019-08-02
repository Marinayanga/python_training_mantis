# -*- coding: utf-8 -*-
import operator

def test_add_project(app, json_project,db):
    project = json_project
    old_list=db.get_project_list()
    app.project.create_project(project)
    app.project.return_to_ptoject_page()
    new_list = db.get_project_list()
    old_list.append(project)
    assert sorted(old_list, key=operator.attrgetter('name')) == sorted(new_list, key=operator.attrgetter('name'))





