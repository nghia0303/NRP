from SC import SequentialCounterEncoding

class SCAMK(SequentialCounterEncoding.SCEncoding):
    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)
        self.add_s_map()
        self.at_most_k()

    def add_s_map(self):
        for i in range(1, self.n):
            for j in range(1, self.k + 1):
                self.current_variable_count += 1
                self.s_map[(i, j)] = self.current_variable_count


    def at_most_k(self):

        # -X1 + S1,1
        cnf_line = [-self.x_map[1], self.s_map[(1, 1)]]
        self.cnf.append(cnf_line)
        self.clause_count += 1
        print("-X", 1, " ", "S", 1, " ", cnf_line)

        # -S1,j (1 < j <=k
        for j in range(2, self.k+1):
            cnf_line = [-self.s_map[(1, j)]]
            self.cnf.append(cnf_line)
            self.clause_count += 1
            print("-S", 1, j, " ", cnf_line)

        # -Xn + -Sn-1,k
        cnf_line = [-self.x_map[self.n], -self.s_map[(self.n-1, self.k)]]
        self.cnf.append(cnf_line)
        self.clause_count += 1
        print("-X", self.n, " ", "-S", self.n-1, self.k, " ", cnf_line)

        for i in range(2, self.n):
            # -Xi + Si,1
            cnf_line = [-self.x_map[i], self.s_map[(i, 1)]]
            self.cnf.append(cnf_line)
            self.clause_count += 1
            print("-X", i, " ", "S", i, 1, " ", cnf_line)

            # -Si-1,1 Si,1
            cnf_line = [-self.s_map[(i-1, 1)], self.s_map[(i, 1)]]
            self.cnf.append(cnf_line)
            self.clause_count += 1
            print("-S", i-1, 1, " ", "S", i, 1, " ", cnf_line)

            for j in range(2, self.k+1):
                # -Xi + -Si-1,j-1 + Si,j
                cnf_line = [-self.x_map[i], -self.s_map[(i-1, j-1)], self.s_map[(i, j)]]
                self.cnf.append(cnf_line)
                self.clause_count += 1
                print("-X", i, " ", "-S", i-1, j-1, " ", "S", i, j, " ", cnf_line)

                # -Si-1,j Si,j
                cnf_line = [-self.s_map[(i-1, j)], self.s_map[(i, j)]]
                self.cnf.append(cnf_line)
                self.clause_count += 1
                print("-S", i-1, j, " ", "S", i, j, " ", cnf_line)

            # -Xi + -Si-1,k
            cnf_line = [-self.x_map[i], -self.s_map[(i-1, self.k)]]
            self.cnf.append(cnf_line)
            self.clause_count += 1
            print("-X", i, " ", "-S", i-1, self.k, " ", cnf_line)

