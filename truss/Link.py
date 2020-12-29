from math import sqrt

import numpy as np

from truss.Node import Node2D


class Link2D(object):

    def __init__(self, node1: Node2D, node2: Node2D) -> None:
        super().__init__()

        if node1.index < node2.index:
            self.node1 = node1
            self.node2 = node2
        else:
            self.node1 = node2
            self.node2 = node1

        self.length = sqrt(pow(node1.x - node2.x, 2) +
                           pow(node1.y - node2.y, 2))

    def __eq__(self, link: "Link2D") -> bool:
        return self.node1 == link.node1 and self.node2 == link.node2

    @property
    def force(self) -> float:
        """
        Calculates the force within the link. Tensile forces are positive
        and compressive forces are negative.

        Returns:
            float: the force within the link
        """
        delta_ux = self.node1.ux - self.node2.ux
        delta_uy = self.node1.uy - self.node2.uy

        cos = (self.node1.x - self.node2.x) / self.length
        sin = (self.node1.y - self.node2.y) / self.length

        return (delta_ux * cos + delta_uy * sin) / self.length

    def get_K_matrix(self) -> np.ndarray:
        c = (self.node1.x - self.node2.x) / self.length
        s = (self.node1.y - self.node2.y) / self.length

        # Creates a 2x2 matrix and populates it
        matrix = np.zeros((2, 2))
        matrix[0, 0] = c * c
        matrix[0, 1] = c * s
        matrix[1, 0] = c * s
        matrix[1, 1] = s * s

        return matrix / self.length
