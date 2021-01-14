import unittest
import Segundaentrega
print("\nUnit testing con los numeros 10, 8, 3 respectivamente: ")
class TestSegundaentrega(unittest.TestCase):
    def test_sumador(self):
        self.assertEqual(Segundaentrega.sumador(10), 55)
        self.assertEqual(Segundaentrega.sumador(8), 36)
        self.assertEqual(Segundaentrega.sumador(3), 6)

if __name__ == '__main__':
    unittest.main()

