import random


class MockPh:
    def __init__(self):
        self.ph_safe_min = 6.5
        self.ph_safe_max = 6.7

    def determine_safety(self, ph: float) -> str:
        if ph >= self.ph_safe_min and ph <= self.ph_safe_max:
            return "Aman"
        else:
            return "Tak Aman"

    def generate_random_ph(self):
        ph = round(random.uniform(0, 14), 2)
        return ph
