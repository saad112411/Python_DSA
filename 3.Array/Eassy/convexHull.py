import math
def convex_hull(points):
    if len(points) < 3:
        return []
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - \
              (q[0] - p[0]) * (r[1] - q[1])
        if val == 0: return 0 
        return 1 if val > 0 else 2 

    start_point = min(points, key=lambda p: (p[1], p[0]))

    sorted_points = sorted(
        points,
        key=lambda p: (
            math.atan2(p[1] - start_point[1], p[0] - start_point[0]),
            (p[0] - start_point[0])**2 + (p[1] - start_point[1])**2
        )
    )
    hull = []
    for point in sorted_points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) != 2:
            hull.pop()
        hull.append(point)
    return hull
if __name__ == '__main__':
    points = [(0, 3), (1, 1), (2, 2), (4, 4),
              (0, 0), (1, 2), (3, 1), (3, 3)]
    hull_points = convex_hull(points)
    print("Original Points:", points)
    print("Convex Hull Points:", hull_points)