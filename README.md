# Truss Simulator

The Truss Simulator uses direct stiffness method to analyze forces in a truss structure. Unlike other solvers that uses method of joints, this simulator is capable of solving both statically determinate and indeterminate trusses. 

To use the library, simply follow the procedure below:

1. Build the truss by calling initializing <code> Truss2D </code>.
2. Add nodes to the truss. Define its coordinate and supports.
3. Link two nodes in the truss to form a link.
4. Set external forces to the nodes.
5. Preview the bridge to see if the shape is as expected.
6. Solve for forces within links and at supports.
7. Output the result in the console.

## Example
### Code
```python
from truss import Truss2D

# Step 1: Build the truss by calling initializing Truss2D.
t = Truss2D("T1")

# Step 2: Add nodes to the truss. Define its coordinate and supports.
n0 = t.create_node(-7, 7, support="pin")
n1 = t.create_node(7, 7, support="h_roller")
n2 = t.create_node(0, 0)

# Step 3: Add nodes to the truss. Define its coordinate and supports.
m0 = t.create_link(n0, n1)
m1 = t.create_link(n1, n2)
m2 = t.create_link(n2, n0)

# Step 4: Set external forces to the nodes.
t.set_external_force(n2, 0, -30)

# Step 5: Preview the bridge to see if the shape is as expected.
t.show_truss()

# Step 6: Solve for forces within links and at supports.
t.simulate_stress()

# Step 7: Output the result in the console.
t.print_summary()
```
### Output
```
Node Summary:
  Index    X    Y  Support      Fx    Fy
-------  ---  ---  ---------  ----  ----
      0   -7    7  pin           0    15
      1    7    7  h_roller      0    15
      2    0    0  None          0   -30



Link Summary:
Nodes      Length     Force
-------  --------  --------
(0, 1)   14        -15
(0, 2)    9.89949   21.2132
(1, 2)    9.89949   21.2132


```