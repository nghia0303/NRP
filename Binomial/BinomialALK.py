from Binomial import BinomialEncoding
from itertools import combinations

class BinomialAMK(BinomialEncoding.BinomialEncoding):
    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)
        self.at_most_k()

    def at_most_k(self):
        for comb in combinations(self.variable_list, self.n - self.k + 1):
            self.cnf.append(list(comb))
            self.clause_count += 1
