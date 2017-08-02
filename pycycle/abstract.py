def implements_node_interface(obj):
    return 'children' in _public_methods_of(obj)


def _public_methods_of(obj):
    return [a for a in dir(obj) if not a.startswith('__')]


def add_edge_record(edges, src, dest):
    edges.append(["%s => %s" % (id(src), id(dest))])


def dfs(root):
    history = []
    stack = [root]
    for parent in stack:
        for child in parent.children:
            add_edge_record(history, parent, child)
            stack.append(child)
    return history
