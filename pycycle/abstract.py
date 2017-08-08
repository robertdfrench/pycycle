from collections import namedtuple


Edge = namedtuple("Edge", "parent child")


class GraphWalker(object):
    def __init__(self, root):
        self.stack = [root]

    @property
    def edges(self):
        for parent in self.stack:
            for child in parent.children:
                yield Edge(parent=parent, child=child)

    def walk(self, action):
        for edge in self.edges:
            self.soft_append(edge, action)

    def soft_append(self, edge, action):
        if action(edge.parent, edge.child):
            self.stack.append(edge.child)


class NodeSet(object):
    def __init__(self):
        self.items = {}

    def add(self, element):
        self.items[element.name] = element

    def contains(self, element):
        return element.name in self.items

    def contains_name(self, name):
        return name in self.items

    def remove_arbitrary_element(self):
        if len(self.items) > 0:
            (name, element) = self.items.popitem()
            return element

    def __len__(self):
        return len(self.items)


def walk(graph, action):
    gw = GraphWalker(graph)
    gw.walk(action)


def membership(digraph):
    members = NodeSet()
    def collect_nodes(parent, child):
        if not members.contains(parent) or not members.contains(child):
            members.add(parent)
            members.add(child)
            return True
    walk(digraph, collect_nodes)
    return members


def find_cycles(digraph):
    gray = NodeSet()
    black = NodeSet()
    white = membership(digraph)

    next_element = white.remove_arbitrary_element()

    while next_element:
        if next_element not in black:
            gray.add(element)

    return []
