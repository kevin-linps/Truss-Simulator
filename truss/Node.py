from typing import Tuple

TOL = 1e-9


class Node2D(object):

    def __init__(self, X: float, Y: float, support: str) -> None:
        """Constructor of the class.

        Args:
            X (float): x-coordinate of the node
            Y (float): y-coordinate of the node
            support (str): the support on the node
        """
        super().__init__()
        self.x = X
        self.y = Y
        self.support = support

        self.index = 0
        self.Fx = 0
        self.Fy = 0
        self.ux = 0
        self.uy = 0

    def __eq__(self, node: "Node2D") -> bool:
        return self.x == node.x and self.y == node.y

    @property
    def freedom(self) -> Tuple[bool, bool]:
        if self.support == "pin":
            return (False, False)
        if self.support == "h_roller":
            return (True, False)
        if self.support == "v_roller":
            return (False, True)
        return (True, True)

    @property
    def Fx(self):
        return self._Fx

    @Fx.setter
    def Fx(self, force: float):
        if abs(force) < TOL:
            self._Fx = 0
        else:
            self._Fx = force

    @property
    def Fy(self):
        return self._Fy

    @Fy.setter
    def Fy(self, force: float):
        if abs(force) < TOL:
            self._Fy = 0
        else:
            self._Fy = force
