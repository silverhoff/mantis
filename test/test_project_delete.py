from generator import project as generator
from model.project import Project
import random


def test_project_delete(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    if app.project.get_project_list()==0:
        project = Project(name=generator.random_string("name", 10),
                          description=generator.random_string("description", 10))
        app.project.add_project(project)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project.id)
    app.project.open_project_page()
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)