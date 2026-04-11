import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neumann_kernels.cost_model import asymptotic_coefficient, kernel_catalog, multiply_count


class CostModelTest(unittest.TestCase):
    def test_catalog_contains_expected_kernels(self):
        names = [entry["kernel_id"] for entry in kernel_catalog()]
        self.assertEqual(names, ["radix5", "radix9", "radix15", "radix24"])

    def test_coefficients_match_paper_values(self):
        self.assertAlmostEqual(asymptotic_coefficient(5, 2), 1.723, places=3)
        self.assertAlmostEqual(asymptotic_coefficient(9, 3), 1.577, places=3)
        self.assertAlmostEqual(asymptotic_coefficient(15, 4), 1.536, places=3)
        self.assertAlmostEqual(asymptotic_coefficient(24, 5), 1.527, places=3)

    def test_multiply_count_scales_logarithmically(self):
        direct = 4096 - 1
        rad24 = multiply_count(24, 5, 4096)
        self.assertEqual(rad24, 21)
        self.assertLess(rad24, direct)


if __name__ == "__main__":
    unittest.main()
