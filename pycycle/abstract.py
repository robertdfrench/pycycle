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


class DripCounter(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.total_items = len(source)

    @property
    def all_items_have_been_moved(self):
        return self.source_is_empty and self.dest_is_full

    @property
    def source_is_empty(self):
        return len(self.source) == 0

    @property
    def dest_is_full(self):
        return len(self.dest) == self.total_items


def find_cycles(digraph):
    actively_visiting = NodeSet()
    totally_visited = NodeSet()
    not_visited = membership(digraph)

    next_element = not_visited.remove_arbitrary_element()
    actively_visiting.add(next_element)

    search_stack = [next_element]

    cycle_found = False
    drip_counter = DripCounter(not_visited, totally_visited)

    while not cycle_found and not drip_counter.all_items_have_been_moved:
        cycle_found = True

    return []
