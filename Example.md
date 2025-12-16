## Example: Parametric Force Sweep Using Shared Geometry Parameters

This example performs a parametric force sweep by translating a permanent magnet through a C-shaped steel guide.  

---

### Example

```python
from temp import Model

# Model Setup
mod1 = Model(radius=20, symetric=False)

# Materials
steel = mod1.loadMaterial("1010 Steel")
N52 = mod1.loadMaterial("N52")


# Shared Geometry Parameters
magWidth = 1
magHeight = 10

airGap = 0.1
vGap = 10
yThickness = 1

magCenterY = 0.0

# C-Shaped Steel Geometry
polyCoords = [
    magWidth/2 + airGap, 0,
    magWidth/2 + airGap + yThickness, 0,
    magWidth/2 + airGap + yThickness, vGap + yThickness,
    -magWidth/2 - airGap - yThickness, vGap + yThickness,
    -magWidth/2 - airGap - yThickness, 0,
    -magWidth/2 - airGap, 0,
    -magWidth/2 - airGap, vGap,
    magWidth/2 + airGap, vGap,
    magWidth/2 + airGap, 0
]

cShape = mod1.addBlock(steel)
cShape.setCoords(polyCoords)

magnet = mod1.addBlock(N52, 90)

def setMagnetPosition(center_y):
    half_h = magHeight / 2
    half_w = magWidth / 2

    magnet.setCoords([
        -half_w, center_y - half_h,
         half_w, center_y - half_h,
         half_w, center_y + half_h,
        -half_w, center_y + half_h
    ])

y_positions = [i * 0.5 for i in range(-10, 11)]
force_data = {}

for y in y_positions:
    magCenterY = y
    setMagnetPosition(magCenterY)

    # Redraw geometry and compute force
    mod1.drawAll()
    force = magnet.getForce()
    force_data[magCenterY] = force

# force_data now contains:
# { magnet_center_y : force_vector }
