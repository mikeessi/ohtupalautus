import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        dependencies = []
        dev_dependencies = []
        content = request.urlopen(self._url).read().decode("utf-8")
        content_map = toml.loads(content)

        name = content_map['tool']['poetry']['name']
        descr = content_map['tool']['poetry']['description']
        for k in content_map['tool']['poetry']['dev-dependencies']:
            dev_dependencies.append(k)
        for k in content_map['tool']['poetry']['dependencies']:
            dependencies.append(k)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, descr, dependencies, dev_dependencies)
