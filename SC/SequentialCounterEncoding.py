class SCEncoding:
    def __init__(self, n, k, variable_list, current_variable_count):
        self.n = n
        self.k = k
        self.variable_list = variable_list
        self.variable_count = 0
        self.current_variable_count = current_variable_count
        self.clause_count = 0
        self.cnf = []
        self.x_map = {}
        self.add_x_map()

        self.s_map = {}


    def add_x_map(self):
        j = 0
        for i in range(1, self.n + 1):
            self.x_map[i] = self.variable_list[j]
            j += 1


    def __str__(self) -> str:
        res = self.cnf.__str__()
        return res
    
