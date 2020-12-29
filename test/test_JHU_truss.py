from truss import Truss2D

import pytest

# JHU simulator calculates value to 3 decimal places
TOL = 1e-3


def approx(value: float):
    return pytest.approx(value, abs=TOL)


def test_JHU_truss1():
    t = Truss2D("T1")

    n0 = t.create_node(-7, 7, support="pin")
    n1 = t.create_node(7, 7, support="h_roller")
    n2 = t.create_node(0, 0)

    m0 = t.create_link(n0, n1)
    m1 = t.create_link(n1, n2)
    m2 = t.create_link(n2, n0)

    t.set_external_force(n2, 0, -30)

    t.simulate_stress()

    assert t._links[m0].force == approx(-15)
    assert t._links[m1].force == approx(21.213)
    assert t._links[m2].force == approx(21.213)


def test_JHU_truss2():
    t = Truss2D("T2")

    n0 = t.create_node(0, 0)
    n1 = t.create_node(6, 6, support="h_roller")
    n2 = t.create_node(-6, 6, support="pin")
    n3 = t.create_node(-6, -6)
    n4 = t.create_node(6, -6)

    m0 = t.create_link(n0, n1)
    m1 = t.create_link(n0, n2)
    m2 = t.create_link(n0, n3)
    m3 = t.create_link(n0, n4)
    m4 = t.create_link(n1, n2)
    m5 = t.create_link(n2, n3)
    m6 = t.create_link(n3, n4)

    t.set_external_force(n4, 0, -12)

    t.simulate_stress()

    assert t._links[m0].force == approx(16.971)
    assert t._links[m1].force == approx(16.971)
    assert t._links[m2].force == approx(16.971)
    assert t._links[m3].force == approx(16.971)
    assert t._links[m4].force == approx(-12)
    assert t._links[m5].force == approx(-12)
    assert t._links[m6].force == approx(-12)


def test_JHU_truss3():
    t = Truss2D("T3")

    n0 = t.create_node(-4, 0, support="pin")
    n1 = t.create_node(-2, 0)
    n2 = t.create_node(0, 0)
    n3 = t.create_node(2, 0)
    n4 = t.create_node(4, 0, support="h_roller")
    n5 = t.create_node(3, 3)
    n6 = t.create_node(1, 3)
    n7 = t.create_node(-1, 3)
    n8 = t.create_node(-3, 3)

    m0 = t.create_link(n0, n1)
    m1 = t.create_link(n1, n2)
    m2 = t.create_link(n2, n3)
    m3 = t.create_link(n3, n4)
    m4 = t.create_link(n4, n5)
    m5 = t.create_link(n5, n6)
    m6 = t.create_link(n6, n7)
    m7 = t.create_link(n7, n8)
    m8 = t.create_link(n0, n8)
    m9 = t.create_link(n1, n8)
    m10 = t.create_link(n1, n7)
    m11 = t.create_link(n2, n7)
    m12 = t.create_link(n2, n6)
    m13 = t.create_link(n3, n6)
    m14 = t.create_link(n3, n5)

    t.set_external_force(n1, 0, -10)
    t.set_external_force(n2, 0, -20)
    t.set_external_force(n3, 0, -10)

    t.simulate_stress()

    assert t._links[m0].force == approx(6.667)
    assert t._links[m1].force == approx(16.667)
    assert t._links[m2].force == approx(16.667)
    assert t._links[m3].force == approx(6.667)
    assert t._links[m4].force == approx(-21.082)
    assert t._links[m5].force == approx(-13.333)
    assert t._links[m6].force == approx(-20.000)
    assert t._links[m7].force == approx(-13.333)
    assert t._links[m8].force == approx(-21.082)
    assert t._links[m9].force == approx(21.082)
    assert t._links[m10].force == approx(-10.541)
    assert t._links[m11].force == approx(10.541)
    assert t._links[m12].force == approx(10.541)
    assert t._links[m13].force == approx(-10.541)
    assert t._links[m14].force == approx(21.082)


def test_JHU_truss4():
    t = Truss2D("T4")

    n0 = t.create_node(0, 0)
    n1 = t.create_node(25, 0, support="h_roller")
    n2 = t.create_node(-25, 0, support="pin")
    n3 = t.create_node(6, 14)
    n4 = t.create_node(-6, 14)
    n5 = t.create_node(-15, 11)
    n6 = t.create_node(-21, 7)
    n7 = t.create_node(21, 7)
    n8 = t.create_node(15, 11)

    m0 = t.create_link(n2, n0)
    m1 = t.create_link(n0, n1)
    m2 = t.create_link(n1, n7)
    m3 = t.create_link(n7, n8)
    m4 = t.create_link(n8, n3)
    m5 = t.create_link(n3, n4)
    m6 = t.create_link(n4, n5)
    m7 = t.create_link(n5, n6)
    m8 = t.create_link(n6, n2)
    m9 = t.create_link(n6, n0)
    m10 = t.create_link(n0, n5)
    m11 = t.create_link(n0, n4)
    m12 = t.create_link(n0, n8)
    m13 = t.create_link(n0, n7)
    m14 = t.create_link(n0, n3)

    t.set_external_force(n0, 0, -20)

    t.simulate_stress()

    assert t._links[m0].force == approx(5.714)
    assert t._links[m1].force == approx(5.714)
    assert t._links[m2].force == approx(-11.518)
    assert t._links[m3].force == approx(-14.308)
    assert t._links[m4].force == approx(-16.47)
    assert t._links[m5].force == approx(-17.857)
    assert t._links[m6].force == approx(-16.47)
    assert t._links[m7].force == approx(-14.308)
    assert t._links[m8].force == approx(-11.518)
    assert t._links[m9].force == approx(6.525)
    assert t._links[m10].force == approx(4.613)
    assert t._links[m11].force == approx(5.666)
    assert t._links[m12].force == approx(4.613)
    assert t._links[m13].force == approx(6.525)
    assert t._links[m14].force == approx(5.666)
