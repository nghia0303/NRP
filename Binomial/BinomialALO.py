from Binomial import  BinomialEncoding

class BinomialALO(BinomialEncoding.BinomialEncoding):
    def __init__(self, n, variable_list, current_variable_count):
        super().__init__(n, 1, variable_list, current_variable_count)
        self.at_least_one()

    def at_least_one(self):
        cnf_line = []
        for i in range(self.n):
            cnf_line.append(self.variable_list[i])
        self.cnf.append(cnf_line)
        self.clause_count += 1