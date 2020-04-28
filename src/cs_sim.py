import numpy as np

def calculate(vec_a, vec_b):
  return np.dot(vec_a, vec_b) / \
    (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))


