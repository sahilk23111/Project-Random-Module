import numpy as np
import random
from functools import lru_cache

class OptimizedRandomModule:
    def __init__(self):
        # Seed for reproducibility (optional)
        np.random.seed(42)
        random.seed(42)

    @lru_cache(maxsize=None)
    def get_single_random_number(self, lower=0, upper=100):
        """
        Generate a single random number between lower and upper limits.
        Caches results to improve performance for repeated calls.
        """
        return random.randint(lower, upper)

    def get_multiple_random_numbers(self, count, lower=0, upper=100):
        """
        Generate multiple random numbers using numpy for faster performance.
        """
        return np.random.randint(lower, upper, size=count)

    def get_random_float(self, lower=0.0, upper=1.0):
        """
        Generate a single random float between lower and upper limits.
        """
        return random.uniform(lower, upper)

    def get_multiple_random_floats(self, count, lower=0.0, upper=1.0):
        """
        Generate multiple random floats using numpy for faster performance.
        """
        return np.random.uniform(lower, upper, size=count)

# Example usage
if __name__ == "__main__":
    rand_module = OptimizedRandomModule()
    
    # Generate a single random integer
    print(f"Single random number: {rand_module.get_single_random_number(1, 100)}")
    
    # Generate multiple random integers (size=10)
    print(f"Multiple random numbers: {rand_module.get_multiple_random_numbers(10, 1, 100)}")
    
    # Generate a single random float
    print(f"Single random float: {rand_module.get_random_float(0.0, 1.0)}")
    
    # Generate multiple random floats (size=5)
    print(f"Multiple random floats: {rand_module.get_multiple_random_floats(5, 0.0, 1.0)}")
