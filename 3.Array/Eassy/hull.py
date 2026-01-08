import math
import matplotlib.pyplot as plt

def convex_hull(points):
    """
    Computes the convex hull of a set of 2D points using the Graham scan algorithm.
    """
    if len(points) < 3:
        return []

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - \
              (q[0] - p[0]) * (r[1] - q[1])
        if val == 0: return 0  # Collinear
        return 1 if val > 0 else 2  # Clockwise or Counter-clockwise

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

# --- Main part for plotting ---
if __name__ == '__main__':
    # 1. Define the points and compute the hull
    points = [(0, 3), (1, 1), (2, 2), (4, 4),
              (0, 0), (1, 2), (3, 1), (3, 3)]
    
    hull_points = convex_hull(points)
    
    # 2. Prepare data for plotting
    # Extract x and y coordinates of all points
    x_all, y_all = zip(*points)
    
    # To draw a closed polygon, append the first hull point to the end
    hull_closed = hull_points + [hull_points[0]]
    x_hull, y_hull = zip(*hull_closed)

    # 3. Create the plot
    plt.figure(figsize=(8, 6)) # Set the fiimport math
import matplotlib.pyplot as plt

def convex_hull(points):
    """
    Computes the convex hull of a set of 2D points using the Graham scan algorithm.
    """
    if len(points) < 3:
        return []

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - \
              (q[0] - p[0]) * (r[1] - q[1])
        if val == 0: return 0  # Collinear
        return 1 if val > 0 else 2  # Clockwise or Counter-clockwise

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

# --- Main part for plotting ---
if __name__ == '__main__':
    # 1. Define the points and compute the hull
    points = [(0, 3), (1, 1), (2, 2), (4, 4),
              (0, 0), (1, 2), (3, 1), (3, 3)]
    
    hull_points = convex_hull(points)
    
    # 2. Prepare data for plotting
    # Extract x and y coordinates of all points
    x_all, y_all = zip(*points)
    
    # To draw a closed polygon, append the first hull point to the end
    hull_closed = hull_points + [hull_points[0]]
    x_hull, y_hull = zip(*hull_closed)

    # 3. Create the plot
    plt.figure(figsize=(8, 6)) # Set the figure size
    
    # Plot all the points as blue dots ('bo')
    plt.plot(x_all, y_all, 'bo', label='All Points')
    
    # Plot the convex hull as a red line ('r-')
    plt.plot(x_hull, y_hull, 'r-', label='Convex Hull')
    
    # Optional: Fill the hull polygon for better visibility
    plt.fill(x_hull, y_hull, 'r', alpha=0.1)

    # 4. Customize and show the plot
    plt.title('Convex Hull Visualization 📈')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.legend() # Show the labels
    plt.grid(True) # Add a grid
    plt.gca().set_aspect('equal', adjustable='box') # Ensure x and y axes have the same scale
    
    plt.show() # Display the plotgure size
    
    # Plot all the points as blue dots ('bo')
    plt.plot(x_all, y_all, 'bo', label='All Points')
    
    # Plot the convex hull as a red line ('r-')
    plt.plot(x_hull, y_hull, 'r-', label='Convex Hull')
    
    # Optional: Fill the hull polygon for better visibility
    plt.fill(x_hull, y_hull, 'r', alpha=0.1)

    # 4. Customize and show the plot
    plt.title('Convex Hull Visualization 📈')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.legend() # Show the labels
    plt.grid(True) # Add a grid
    plt.gca().set_aspect('equal', adjustable='box') # Ensure x and y axes have the same scale
    
    plt.show() # Display the plot