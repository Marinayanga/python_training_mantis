# -*- coding: utf-8 -*-
import operator

def test_add_project(app, fix_login, json_project,db):
    project = json_project
    #old_list=db.get_project_list()
    old_list = app.soap.get_projects()
    app.project.create_project(project)
    app.project.return_to_ptoject_page()
    #new_list = db.get_project_list()
    new_list = app.soap.get_projects()
    old_list.append(project)
    assert sorted(old_list, key=operator.attrgetter('name')) == sorted(new_list, key=operator.attrgetter('name'))





