# -*- coding: utf-8 -*-


def test_add_project(app, json_project):
    project = json_project
    app.session.login(username="administrator", password="root")
    old_list=app.project.get_project_list()
    app.project.create_project(project)
    app.project.return_to_ptoject_page()
    # new_list=old_list.append(Project(name="Test 8", status='stable', view_state="private", description="Description 7"))
    # assert len(old_list)+1 == len(new_list)
    app.session.logout()





