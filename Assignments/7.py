import numpy as np
from math import sqrt

x1 = np.array([-1, 0])
x2 = np.array([0, 1])
x3 = np.array([1/sqrt(2), 1/sqrt(2)])

w1 = np.array([0, -1])
w2 = np.array([-2/sqrt(5), 1/sqrt(5)])
w3 = np.array([-1/sqrt(5), 2/sqrt(5)])

# sequence of inputs: x1, x2, x3, x1, x2, x3

# w2 is closest to x1
delta_w2 = 0.5 * (x1 - w2)
part1 = w2 + delta_w2
part1 = part1/np.linalg.norm(part1)
print(part1)

# w3 is closer to x2
delta_w3 = 0.5 * (x2 - w3)
part2 = w3 + delta_w3
part2 = part2/np.linalg.norm(part2)
print(part2)

# w3 is closer to x3
delta_w3 = 0.5 * (x3 - w3)
part3 = w3 + delta_w3
part3 = part3/np.linalg.norm(part3)
print(part3)

# w2 is still closest to x1
delta_w2 = 0.5 * (x1 - part1)
part4 = part1 + delta_w2
part4 = part4/np.linalg.norm(part4)
print(part4)

# w3 is still closest to x2
delta_w3 = 0.5 * (x2 - part3)
part5 = part3 + delta_w3
part5 = part5/np.linalg.norm(part5)
print(part5)

# w3 is wtill closest to x3
delta_w3 = 0.5 * (x3 - part5)
part5 = part5 + delta_w3
part5 = part5/np.linalg.norm(part5)
print(part5)
