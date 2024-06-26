from dataclasses import asdict

from k8s import KubeEnvironment
from models import Node, Link


class GraphState:

    def __init__(self):
        self.nodes: list[Node] = []
        self.links: list[Link] = []

    def update_from_env(self, env: KubeEnvironment):
        self.nodes = [resource.to_node() for resource in env.resources]
        self.links = [relationship.to_link() for relationship in env.relationships]

    def serialize(self):
        return {
            'nodes': [asdict(node) for node in self.nodes],
            'links': [asdict(link) for link in self.links],
            'types': list({i.type for i in self.nodes})
        }
