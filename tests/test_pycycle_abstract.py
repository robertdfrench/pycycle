from pycycle import abstract
from collections import namedtuple
import pytest


Node = namedtuple("Node", "children name")


def empty_node(name):
    return Node(children=[], name=name)


@pytest.fixture
def dag():
    a = empty_node("a")
    b = empty_node("b")
    c = empty_node("c")
    d = empty_node("d")
    a.children.append(b)
    b.children.append(c)
    b.children.append(d)
    return a


def test_no_cycle(dag):
    assert not abstract.find_cycles(dag)


@pytest.fixture
def dcg():
    a = empty_node("a")
    b = empty_node("b")
    c = empty_node("c")
    d = empty_node("d")
    a.children.append(b)
    b.children.append(c)
    b.children.append(d)
    d.children.append(a)
    return a


def test_has_cycles(dcg):
    assert ["a","b","d"] in abstract.find_cycles(dcg)


def test_graph_walker(dag):
    gw = abstract.GraphWalker(dag)
    edges = []
    def append_once(parent, child):
        edge = [parent.name, child.name]
        if edge not in edges:
            edges.append(edge)
            return True
    gw.walk(append_once)
    assert ["a","b"] in edges
    assert ["b","d"] in edges


def test_whiteset(dag):
    white = abstract.membership(dag)
    assert white.contains_name("a")
    assert white.contains_name("b")
    assert white.contains_name("c")
    assert white.contains_name("d")
