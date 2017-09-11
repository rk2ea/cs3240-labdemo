import unittest
from graph import Graph
class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph()
        self.g2 = Graph({'A': ['A','B'], 'B': ['A', 'C'], 'C': ['B', 'C', 'D'], 'D':[]})

    def test_get_adjlist_A1(self):
        self.assertEqual(self.g2.get_adjlist('A'), ['A', 'B'])
    def test_get_adjlist_A2(self):
        self.assertIsNone(self.g2.get_adjlist('E'), "Test g1 failed.")
    def test_is_adjacent_B1(self):
        self.assertEqual(self.g2.is_adjacent('A','B'),True)
    def test_is_adjacent_B2(self):
        self.assertEqual(self.g2.is_adjacent('A','F'), False)
    def test_num_nodes_C1(self):
        self.assertEqual(self.g2.num_nodes(),4)
    def test_num_nodes_C2(self):
        self.assertEqual(self.g1.num_nodes(),0)
    def test_contains_D1(self):
        self.assertEqual(self.g2.__contains__('A'), True)
    def test_contains_D2(self):
        self.assertEqual(self.g2.__contains__('G'), False)
    def test_len_E1(self):
        self.assertEqual(self.g2.num_nodes(), 4)
    def test_len_E2(self):
        self.assertEqual(self.g1.num_nodes(), 0)
    def test_add_nodes_F1(self):
        self.assertEqual(self.g2.add_node('Z'),True)
    def test_add_nodes_F2(self):
        self.assertEqual(self.g2.add_node('A'),False)
    def test_link_nodes_G1(self):
        self.assertEqual(self.g2.link_nodes('A','C'),True)
    def test_link_nodes_G2(self):
        self.assertEqual(self.g2.link_nodes('A','H'),False)
    def test_unlink_nodes_H1(self):
        self.assertEqual(self.g2.unlink_nodes('A','B'), True)
    def test_unlink_nodes_H2(self):
        self.assertEqual(self.g2.unlink_nodes('A', 'D'), False)
    def test_del_node_I1(self):
        self.assertEqual(self.g2.del_node('A'), True)
    def test_del_node_I2(self):
        self.assertEqual(self.g2.del_node('N'), False)