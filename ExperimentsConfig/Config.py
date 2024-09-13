from Binomial.BinomialAMO import BinomialAMO
from Binomial.BinomialALO import BinomialALO

from staircaseAtLeastOne.StairCaseALO import StairCaseALO

from cnf.CNF import CNF


class Config:
    def __init__(self, n, k, variable_list, current_variable_count):
        self.n = n
        self.k = k
        self.variable_list = variable_list
        self.current_variable_count = current_variable_count
        self.cnf = []
        self.clause_count = 0

    def __str__(self):
        cnf = CNF(self.n, self.clause_count, self.cnf)
        return cnf.__str__()

    def cnf_file_export(self, file_name):
        cnf = CNF(self.n, self.clause_count, self.cnf)
        cnf.write_to_file(file_name)


# Binomial AMO + Binomial Staircase ALO
class Config1(Config):

    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)
        self.staircase_amo()
        self.staircase_alo()

    def staircase_amo(self):
        for i in range(self.n - self.k + 1):

            temp_variable_list = self.variable_list[i:i + self.k]
            binomial_amo = BinomialAMO(self.k, temp_variable_list, self.current_variable_count)
            self.cnf += binomial_amo.cnf
            self.clause_count += binomial_amo.clause_count
            print("AMO, ", temp_variable_list)
            print(binomial_amo.cnf)

    def staircase_alo(self):
        for i in range(self.n - self.k + 1):
            temp_variable_list = self.variable_list[i: i + self.k]
            binomial_alo = BinomialALO(self.k, temp_variable_list, self.current_variable_count)
            self.cnf += binomial_alo.cnf
            self.clause_count += binomial_alo.clause_count
            print("ALO, ", temp_variable_list)
            print(binomial_alo.cnf)


class Config2(Config):
    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)
        # self.staircase_amo()
        self.staircase_alo()

    def staircase_amo(self):
        for i in range(self.n - self.k + 1):
            temp_variable_list = self.variable_list[i:i + self.k]
            binomial_amo = BinomialAMO(self.k, temp_variable_list, self.current_variable_count)
            self.cnf += binomial_amo.cnf
            self.clause_count += binomial_amo.clause_count
            print("AMO, ", temp_variable_list)
            print(binomial_amo.cnf)


    def staircase_alo(self):

        my_staircase_alo = StairCaseALO(self.n, self.k, self.variable_list, self.current_variable_count)
        self.cnf += my_staircase_alo.cnf
        self.clause_count += my_staircase_alo.clause_count
        self.current_variable_count = my_staircase_alo.current_variable_count
        print("ALO, ", self.variable_list)
        print(my_staircase_alo.cnf)





def main():
    n = 20
    k = 5
    variable_list = list(range(1, n + 1))

    print("Config1")
    config1 = Config1(n, k, variable_list, n)
    # print(config1)
    config1.cnf_file_export("Results/config1.cnf")
    print("--------------------------------------------------------------------------")

    print("Config2")
    config2 = Config2(n, k, variable_list, n)
    config2.cnf_file_export("Results/config2.cnf")
    # print(config2)
    print("--------------------------------------------------------------------------")


if __name__ == '__main__':
    main()



