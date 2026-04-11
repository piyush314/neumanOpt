import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neumann_kernels.io import load_certified_kernel

class BoundsSmokeTest(unittest.TestCase):
    def test_certified_data_present(self):
        data = load_certified_kernel("radix24", root=ROOT)
        self.assertGreater(data["safe_radii"]["q_certified"], 0.984)

if __name__ == "__main__":
    unittest.main()
