import unittest as ut
import unittest.mock as m

from context import *


class TestORCA(ut.TestCase):
    def setUp(self):
        self.seq = "AGCATGCTAGTAGCTCGTCGTAGTACGATGCATGTCAGCTGATCGTACGATCGATAGATGACTACATGCACCACACGTACTACGATGATGATAGCTCA"
        self.gene_locs = [('dnaA', 0, 10), ('dnaN', 20, 30)]
        # remove later


    def test___make_1(self):
        ...

    
    def test_from_string_1(self):
        orca = ORCA.from_string(sequence=self.seq, gene_locations=self.gene_locs, accession="Test")

        exp_gene_locs = [("dnaA", Peak.from_calc_middle(0, 10, len(self.seq), 0)), ("dnaN", Peak.from_calc_middle(20, 30, len(self.seq), 0))]

        self.assertIsInstance(orca, ORCA)
        self.assertEqual(orca.accession, "Test")
        self.assertEqual(orca.seq, self.seq)
        self.assertEqual(orca.gene_locations, exp_gene_locs)
        self.assertEqual(orca.seq_len, len(self.seq))
        self.assertEqual(orca.version, 0)


    def test_from_string_2(self):
        orca = ORCA.from_string(sequence=self.seq)

        self.assertIsInstance(orca, ORCA)
        self.assertEqual(orca.accession, "Custom")
        self.assertEqual(orca.seq, self.seq)
        self.assertEqual(orca.gene_locations, [])
        self.assertEqual(orca.seq_len, len(self.seq))
        self.assertEqual(orca.version, 0)


    def test_from_gbk(self):
        ...


    def test_from_pkl(self):
        ...


    def test_from_accession(self):
        ...


    def test_setup_variables(self):
        ...


    def test_get_dnaa_boxes_with_mismatches(self):
        ...


    def test_calculate_disparity_curves(self):
        ...


    def test_analyse_disparity_curves(self):
        ...


    def test_calculate_Z_scores(self):
        ...


    def test_calculate_D_scores(self):
        ...


    def test_calculate_G_scores(self):
        ...


    def find_oriCs(self):
        ...


if __name__ == "__main__":
    ut.main()