from typing import List

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from tabulate import tabulate

from truss.Link import Link2D
from truss.Node import Node2D


class Truss2D:

    def __init__(self, name: str):
        self._name = name
        self._nodes: List[Node2D] = []
        self._links: List[Link2D] = []

    def create_node(self, x: float, y: float, support="None") -> int:
        """Creates a node in the truss.

        Args:
            x (float): x-coordinate of the node
            y (float): y-coordinate of the node
            support (str, optional): the support on the node. Defaults to
                "None".

        Returns:
            int: index of the node in internal list
        """
        new_node = Node2D(x, y, support=support)
        if new_node in self._nodes:
            raise Exception(f"Duplicate node in truss {self._name}")

        # Add the new node into the truss
        new_node.index = len(self._nodes)
        self._nodes.append(new_node)
        return new_node.index

    def create_link(self, node1: int, node2: int) -> int:
        """Creates a link in the truss.

        Args:
            node1 (int): index of the node1 in internal list
            node2 (int): index of the node2 in internal list

        Returns:
            int: index of the link in internal list
        """
        new_link = Link2D(self._nodes[node1], self._nodes[node2])
        if new_link in self._links:
            raise Exception(f"Duplicate link in truss {self._name}")
        self._links.append(new_link)
        return len(self._links) - 1

    def set_external_force(self, node_index, Fx, Fy):
        self._nodes[node_index].Fx = Fx
        self._nodes[node_index].Fy = Fy

    def simulate_stress(self):
        """
        Simulates the bridge under external forces.
        """
        n_nodes = len(self._nodes)
        n_links = len(self._links)

        # Initializes the matrix and the vectors used in FEM
        K_matrix = np.zeros(shape=(n_nodes * 2, n_nodes * 2))
        u_vector = np.zeros(n_nodes*2)
        F_vector = np.zeros(n_nodes*2)

        # Fill K-matrix of each truss into the overall K-matrix
        for i in range(n_links):
            link = self._links[i]
            K_i = link.get_K_matrix()

            i1 = link.node1.index * 2
            i2 = link.node2.index * 2

            K_matrix[i1:i1+2, i1:i1+2] += K_i
            K_matrix[i2:i2+2, i1:i1+2] -= K_i
            K_matrix[i1:i1+2, i2:i2+2] -= K_i
            K_matrix[i2:i2+2, i2:i2+2] += K_i

        free_indices = []
        for i in range(len(self._nodes)):
            node = self._nodes[i]

            F_vector[2*i] = node.Fx
            F_vector[2*i+1] = node.Fy

            (x_free, y_free) = node.freedom

            if x_free:
                free_indices.append(2*i)
            if y_free:
                free_indices.append(2*i+1)

        # Calculates deformations of the free nodes
        temp_K = K_matrix[free_indices, :][:, free_indices]
        temp_F = np.zeros(len(free_indices))
        for i in range(len(free_indices)):
            force = F_vector[free_indices[i]]
            temp_F[i] = force
        temp_u = np.linalg.solve(temp_K, temp_F)

        # Updates the deformations calculated in the u_vector
        for i in range(len(free_indices)):
            u_vector[free_indices[i]] = temp_u[i]

        # Multiply K_matrix and U_vector to get F_vector
        F_vector = K_matrix @ u_vector

        # Updates the deformations and forces of each truss and joint
        for i in range(len(self._nodes)):
            node = self._nodes[i]
            node.Fx = F_vector[2*i]
            node.Fy = F_vector[2*i+1]
            node.ux = u_vector[2*i]
            node.uy = u_vector[2*i+1]

    def show_truss(self):
        """
        docstring
        """
        lines = []
        for link in self._links:
            coord1 = (link.node1.x, link.node1.y)
            coord2 = (link.node2.x, link.node2.y)
            lines.append([coord1, coord2])

        lc = LineCollection(lines)
        fig = plt.figure()

        ax1 = fig.add_subplot(1, 1, 1)
        ax1.add_collection(lc)
        ax1.autoscale()

        plt.show()

    def print_summary(self):
        """
        docstring
        """
        print("Node Summary:")
        node_summary = []
        for node in self._nodes:
            row = [node.index, node.x, node.y, node.support, node.Fx, node.Fy]
            node_summary.append(row)
        print(tabulate(node_summary, headers=[
              "Index", "X", "Y", "Support", "Fx", "Fy"]))
        print('\n\n')

        print("Link Summary:")
        link_summary = []
        for link in self._links:
            row = [(link.node1.index, link.node2.index),
                   link.length, link.force]
            link_summary.append(row)
        print(tabulate(sorted(link_summary),
                       headers=["Nodes", "Length", "Force"]))
        print('\n\n')
