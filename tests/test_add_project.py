# -*- coding: utf-8 -*-
import unittest
from fixture.application import Application
from model.project import Project
import pytest


def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_project(app):
    app.session.login(username="administrator", password="root")
    app.return_to_ptoject_page()
    app.click_create_project()
    app.fill_project_name(Project(name="Test 7", status='stable', view_state="private", description="Description 7"))
    app.return_to_ptoject_page()
    app.session.logout()





