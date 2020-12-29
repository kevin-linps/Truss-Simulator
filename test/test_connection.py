from itertools import permutations, combinations

import pytest
from truss import Truss2D


def test_duplicate_nodes():

    coords = [(0, 0), (0, 1), (1, 1), (1, 0)]

    t = Truss2D("T1")
    nodes = [t.create_node(x, y) for (x, y) in coords]

    for (x, y) in coords:

        with pytest.raises(Exception) as exception_info:
            n = t.create_node(x, y)

        # Make sure it gives the correct error message
        assert "Duplicate node" in str(exception_info.value)

        # Make sure that the object t has not been modified
        assert len(t._nodes) == len(nodes)
        assert len(t._links) == 0


def test_duplicate_links():

    coords = [(0, 0), (0, 1), (1, 1), (1, 0)]

    t = Truss2D("T2")
    nodes = [t.create_node(x, y) for (x, y) in coords]

    combination = combinations(nodes, 2)
    permutation = permutations(nodes, 2)

    links = [t.create_link(n1, n2) for (n1, n2) in list(combination)]

    for (node1, node2) in list(permutation):

        with pytest.raises(Exception) as exception_info:
            m = t.create_link(node1, node2)

        # Make sure it gives the correct error message
        assert "Duplicate link" in str(exception_info.value)

        # Make sure that the object t has not been modified
        assert len(t._nodes) == len(nodes)
        assert len(t._links) == len(links)
