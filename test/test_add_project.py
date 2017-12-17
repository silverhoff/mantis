from generator import project as generator
from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_projects = app.project.get_project_list()
    project = Project(name=generator.random_string("name",10), description=generator.random_string("description",10))
    app.project.add_project(project)
    app.project.open_project_page()
    old_projects.append(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)



