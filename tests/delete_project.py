
from  model.project import Project


def test_delete_project(app):
    app.session.login(username="administrator", password="root")
    app.project.return_to_ptoject_page()
    if len(app.project.get_project_list()) == 0:
         app.project.create_project(Project(name="Test 7", status='stable', view_state="private", description="Description 7"))
    app.project.delete_first_project()
