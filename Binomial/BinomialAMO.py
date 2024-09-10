from Binomial import  BinomialEncoding

class BinomialAMO(BinomialEncoding.BinomialEncoding):
    def __init__(self, n, variable_list, current_variable_count):
        super().__init__(n, 1, variable_list, current_variable_count)
        self.at_most_one()

    def at_most_one(self):
        for i in range(self.n):
            for j in range(i):
                cnf_line = [-self.variable_list[j], -self.variable_list[i]]
                self.cnf.append(cnf_line)
                self.clause_count += 1
