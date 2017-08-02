def implements_node_interface(obj):
    return 'children' in _public_methods_of(obj)


def _public_methods_of(obj):
    return [a for a in dir(obj) if not a.startswith('__')]
