# 1. Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the
# origin.
def check_coordinates(x, y):
    if x == 0 and y == 0:
        return "The point is at the origin."
    elif y == 0:
        return "The point lies on the X-axis."
    elif x == 0:
        return 'The point lies on the Y-axis.'
    else:
        return "The point does not lie on the X-axis, Y-axis, or at the origin."

print(check_coordinates(0, 0))  # Output: "The point is at the origin."
print(check_coordinates(5, 0))  # Output: "The point lies on the X-axis."
print(check_coordinates(0, 3))  # Output: "The point lies on the Y-axis."