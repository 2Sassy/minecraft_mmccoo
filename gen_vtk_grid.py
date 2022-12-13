


points = []
lines = []

xmin = -500
xmax = 1500
ymin = -800
ymax =  500

for x in range(xmin,xmax, 16*4):
    lines.append(f"2 {len(points)} {len(points) + 1}")

    points.extend((f"{x} 0 {ymin}", f"{x} 0 {ymax}"))
for y in range(ymin,ymax, 16*4):
    lines.append(f"2 {len(points)} {len(points) + 1}")

    points.extend((f"{xmin} 0 {y}", f"{xmax} 0 {y}"))
#for y in range(ymin, ymax, 50):



print("# vtk DataFile Version 1.0")
print("3D triangulation data")
print("ASCII")
print("")
print("DATASET POLYDATA")
print(f"POINTS {len(points)} float")

for pt in points:
    print(pt)


print(f"LINES {len(lines)} {len(lines) * 3}")

for line in lines:
    print(line)
