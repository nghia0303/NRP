from SC import SequentialCounterEncoding

class SCAMO(SequentialCounterEncoding.SCEncoding):

    def __init__(self, n, variable_list, current_variable_count):
        super().__init__(n, 0, variable_list, current_variable_count)
        self.add_s_map()
        self.at_most_one()

    def add_s_map(self):
        for i in range(1, self.n):
            self.current_variable_count += 1
            self.variable_count += 1
            self.s_map[i] = self.current_variable_count

    def at_most_one(self):

        # -x1 + s1
        cnf_line = [-self.x_map[1], self.s_map[1]]
        self.cnf.append(cnf_line)
        self.clause_count += 1
        print("-X", 1, " ", "S", 1, " ", cnf_line)

        # -xn + -sn-1
        cnf_line = [-self.x_map[self.n], -self.s_map[self.n-1]]
        self.cnf.append(cnf_line)
        self.clause_count += 1
        print("-X", self.n, " ", "-S", self.n-1, " ", cnf_line)

        for i in range(2, self.n):
            # -xi + si
            cnf_line = [-self.x_map[i], self.s_map[i]]
            self.cnf.append(cnf_line)
            self.clause_count += 1
            print("-X", i, " ", "S", i, " ", cnf_line)

            # -si-1 + si
            cnf_line = [-self.s_map[i-1], self.s_map[i]]
            self.cnf.append(cnf_line)
            self.clause_count += 1
            print("-S", i-1, " ", "S", i, " ", cnf_line)

            #-Xi + -Si-1
            cnf_line = [-self.x_map[i], -self.s_map[i-1]]
            self.cnf.append(cnf_line)
            self.clause_count += 1
            print("-X", i, " ", "-S", i-1, " ", cnf_line)
