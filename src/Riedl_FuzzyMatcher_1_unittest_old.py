import unittest
from src.Riedl_FuzzyMatcher_1 import fuzzymatch_csv

class TestFuzzyMatcher_1_1(unittest.TestCase):
    matched_results = fuzzymatch_csv (input_file_master = '..\\data\\raw\\hospital_account_info.csv',
                                  input_file_to_match_with_master = '..\\data\\raw\\hospital_reimbursement.csv',
                                  list_columns_to_match_of_master_file = ["Facility Name", "Address", "City", "State"],
                                  list_columns_to_match_with_master_file = ["Provider Name", "Provider Street Address", "Provider City",   "Provider State"],
                                  left_id_col='Account_Num',
                                  right_id_col='Provider_Num'
                                 )

    test_pairs = [
                (224294,[0.7916676326592663]),
                (289643,[-1.0418092409677926, 1.164888307994805, -2.2682313785772212]),
                (610668,[-0.4914047624519645, 2.1560437732726587, 0.002013991959749867]),
                (571561,[-0.702083260270369, 0.9998428499474692]),
                (342693,[-0.646561727520119, 1.5002566983035555]),
                (112908,[3.0909307222809534])
                ]
	
    #def test_one(self):
    #    expected_result = [0.7916676326592663]
    #    result= list(self.matched_results.query("__id_right == 224294")["best_match_score"])
    #    self.assertEqual(result,expected_result)

    def test_0(self):
        result= list(self.matched_results.query(f"__id_right == {self.test_pairs[0][0]}")["best_match_score"]).sort()
        expected_result = [self.test_pairs[0][1]].sort()
        self.assertEqual(result,expected_result)

    def test_1(self):
        result= list(self.matched_results.query(f"__id_right == {self.test_pairs[1][0]}")["best_match_score"]).sort()
        expected_result = [self.test_pairs[1][1]].sort()
        self.assertEqual(result,expected_result)
    
    def test_2(self):
        result= list(self.matched_results.query(f"__id_right == {self.test_pairs[2][0]}")["best_match_score"]).sort()
        expected_result = [self.test_pairs[2][1]].sort()
        self.assertEqual(result,expected_result)

    def test_3(self):
        result= list(self.matched_results.query(f"__id_right == {self.test_pairs[3][0]}")["best_match_score"]).sort()
        expected_result = [self.test_pairs[3][1]].sort()
        self.assertEqual(result,expected_result)
	
        
if __name__ == "__main__":
    unittest.main()
