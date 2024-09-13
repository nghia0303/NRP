class BinomialEncoding:
    def __init__(self, n, k, variable_list, current_variable_count):
        self.n = n
        self.k = k
        self.variable_list = variable_list
        self.variable_count = 0
        self.current_variable_count = current_variable_count
        self.clause_count = 0
        self.cnf = []

    def __str__(self) -> str:
        res = self.cnf.__str__()
        return res




