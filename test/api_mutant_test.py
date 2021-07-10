from wsgi import server
import unittest
from flask import json
class ApiMutantTestCase(unittest.TestCase):

    def test_is_mutant_horizontal(self):
        tester = server.test_client(self)
        info = {"dna":["AAAAGA", "CAGTGC", "TTCTAT", "AGAAGG", "CCCCTA", "TCACTG"]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_is_mutant_vertical(self):
        tester = server.test_client(self)
        info = {"dna":["ACTGAG", "GGAGTT", "ATTACC", "AGCACA", "AATGCC", "ACTACT"]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_is_mutant_diag1(self):
        tester = server.test_client(self)
        info = {"dna":["ACTCGA", "GATAGC", "GTATCT", "ACTAAG", "TACTCG", "CAGATT"]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_is_mutant_diag2(self):
        tester = server.test_client(self)
        info = {"dna":["ACTAGA", "CTGGTT", "CTGTAG", "AGTTCC", "TTGCCA", "ATGCAT"]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)                

    def test_is_in_db(self):
        tester = server.test_client(self)
        info = {"dna":["AAAAGA", "CAGTGC", "TTCTAT", "AGAAGG", "CCCCTA", "TCACTG"]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)        

    def test_is_no_mutant(self):
        tester = server.test_client(self)
        info = {"dna":["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 403)

    def test_dna_exception_char(self):
        tester = server.test_client(self)
        info = {"dna":["ACTGGT", "GGCACT", "CATRTA", "TTATCG", "CATCAA", "AGGATC"]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_dna_exception_matrix_invalid(self):
        tester = server.test_client(self)
        info = {"dna":["ATCT", "GATTT", "ACGA", "AATC"]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)  

    def test_is_dna_exception_matrix_empty(self):
        tester = server.test_client(self)
        info = {"dna":[]}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400) 

    def test_is_dna_exception_empty_parmeter(self):
        tester = server.test_client(self)
        info = {}
        response = tester.post('/mutant', data = json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)         

    def test_stats_service_response_code(self):
        tester = server.test_client(self)
        response = tester.get('/stats')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()