# -*- coding: utf-8 -*-
from fixture.application import Application
from model.project import Project
import pytest


# @pytest.fixture
# def app(request):
#     fixture = Application()
#     request.addfinalizer(fixture.destroy)
#     return fixture


def test_add_project(app):
    app.session.login(username="administrator", password="root")
    app.project.create_project(Project(name="Test 7", status='stable', view_state="private", description="Description 7"))
    # app.return_to_ptoject_page()
    # app.click_create_project()
    # app.fill_project_name(Project(name="Test 7", status='stable', view_state="private", description="Description 7"))
    app.project.return_to_ptoject_page()
    app.session.logout()





