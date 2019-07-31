from fixture.application import Application


def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_delete_project(app):
    app.session.login(username="administrator", password="root")
    app.return_to_ptoject_page()
    app.get_project_list()
    app.delete_first_project()
