from Binomial.BinomialAMO import BinomialAMO
from Binomial.BinomialALO import BinomialALO

from Binomial.BinomialAMK import BinomialAMK

from staircaseAtLeastOne.StairCaseALO import StairCaseALO

from SC.SCAMO import SCAMO
from SC.SCAMK import SCAMK

from cnf.CNF import CNF


class Config:
    def __init__(self, n, k, variable_list, current_variable_count):
        self.n = n
        self.k = k
        self.variable_list = variable_list
        self.current_variable_count = current_variable_count
        self.cnf = []
        self.clause_count = 0
        self.added_variable = 0

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

        self.variable_count_amo = 0
        self.variable_count_alo = 0
        self.clause_count_amo = 0
        self.clause_count_alo = 0

        self.staircase_amo()
        self.staircase_alo()


    def staircase_amo(self):
        for i in range(self.n - self.k + 1):
            temp_variable_list = self.variable_list[i:i + self.k]
            binomial_amo = BinomialAMO(self.k, temp_variable_list, self.current_variable_count)
            self.cnf += binomial_amo.cnf
            self.clause_count += binomial_amo.clause_count
            self.variable_count_amo += binomial_amo.current_variable_count - self.current_variable_count
            self.clause_count_amo += binomial_amo.clause_count

    def staircase_alo(self):
        for i in range(self.n - self.k + 1):
            temp_variable_list = self.variable_list[i: i + self.k]
            binomial_alo = BinomialALO(self.k, temp_variable_list, self.current_variable_count)
            self.cnf += binomial_alo.cnf
            self.clause_count += binomial_alo.clause_count
            self.clause_count_alo += binomial_alo.clause_count

            self.variable_count_alo += binomial_alo.current_variable_count - self.current_variable_count


class Config2(Config):
    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)
        self.variable_count_amo = 0
        self.variable_count_alo = 0
        self.clause_count_amo = 0
        self.clause_count_alo = 0

        self.staircase_amo()
        self.staircase_alo()


    def staircase_amo(self):
        for i in range(self.n - self.k + 1):
            temp_variable_list = self.variable_list[i:i + self.k]
            binomial_amo = BinomialAMO(self.k, temp_variable_list, self.current_variable_count)
            self.cnf += binomial_amo.cnf
            self.clause_count += binomial_amo.clause_count
            self.clause_count_amo += binomial_amo.clause_count
            self.variable_count_amo += binomial_amo.current_variable_count - self.current_variable_count

    def staircase_alo(self):

        my_staircase_alo = StairCaseALO(self.n, self.k, self.variable_list, self.current_variable_count)
        self.cnf += my_staircase_alo.cnf
        self.clause_count += my_staircase_alo.clause_count
        self.clause_count_alo += my_staircase_alo.clause_count
        self.added_variable = my_staircase_alo.current_variable_count - self.current_variable_count
        self.variable_count_alo += my_staircase_alo.current_variable_count - self.current_variable_count
        self.current_variable_count = my_staircase_alo.current_variable_count


class Config21(Config):
    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)
        self.variable_count_amo = 0
        self.variable_count_alo = 0
        self.clause_count_amo = 0
        self.clause_count_alo = 0

        self.staircase_amo()
        self.staircase_alo()

    def staircase_amo(self):
        for i in range(self.n - self.k + 1):
            temp_variable_list = self.variable_list[i:i + self.k]
            binomial_amo = BinomialAMK(self.k, 2, temp_variable_list, self.current_variable_count)
            self.cnf += binomial_amo.cnf
            self.clause_count += binomial_amo.clause_count
            self.clause_count_amo += binomial_amo.clause_count
            self.variable_count_amo += binomial_amo.current_variable_count - self.current_variable_count

    def staircase_alo(self):

        my_staircase_alo = StairCaseALO(self.n, self.k, self.variable_list, self.current_variable_count)
        self.cnf += my_staircase_alo.cnf
        self.clause_count += my_staircase_alo.clause_count
        self.clause_count_alo += my_staircase_alo.clause_count
        self.added_variable = my_staircase_alo.current_variable_count - self.current_variable_count
        self.variable_count_alo += my_staircase_alo.current_variable_count - self.current_variable_count
        self.current_variable_count = my_staircase_alo.current_variable_count

class Config3(Config):
    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)

        self.variable_count_amo = 0
        self.variable_count_alo = 0
        self.clause_count_amo = 0
        self.clause_count_alo = 0

        self.staircase_amo()
        self.staircase_alo()



    def staircase_amo(self):
        for i in range(self.n - self.k + 1):
            temp_variable_list = self.variable_list[i:i + self.k]
            scamo = SCAMO(self.k, temp_variable_list, self.current_variable_count)
            self.cnf += scamo.cnf
            self.clause_count += scamo.clause_count
            self.clause_count_amo += scamo.clause_count
            self.added_variable += scamo.current_variable_count - self.current_variable_count
            self.variable_count_amo = scamo.current_variable_count - self.current_variable_count
            print("added variable: ", scamo.variable_count)
            self.current_variable_count = scamo.current_variable_count


    def staircase_alo(self):
        my_staircase_alo = StairCaseALO(self.n, self.k, self.variable_list, self.current_variable_count)
        self.cnf += my_staircase_alo.cnf
        self.clause_count += my_staircase_alo.clause_count
        self.clause_count_alo += my_staircase_alo.clause_count
        self.added_variable += my_staircase_alo.current_variable_count - self.current_variable_count
        self.variable_count_alo = my_staircase_alo.current_variable_count - self.current_variable_count
        self.current_variable_count = my_staircase_alo.current_variable_count


class Config31(Config):
    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)

        self.variable_count_amo = 0
        self.variable_count_alo = 0
        self.clause_count_amo = 0
        self.clause_count_alo = 0

        self.staircase_amo()
        self.staircase_alo()



    def staircase_amo(self):
        for i in range(self.n - self.k + 1):
            temp_variable_list = self.variable_list[i:i + self.k]
            scamo = SCAMK(self.k, 2, temp_variable_list, self.current_variable_count)
            self.cnf += scamo.cnf
            self.clause_count += scamo.clause_count
            self.clause_count_amo += scamo.clause_count
            self.added_variable += scamo.current_variable_count - self.current_variable_count
            self.variable_count_amo = scamo.current_variable_count - self.current_variable_count
            print("added variable: ", scamo.variable_count)
            self.current_variable_count = scamo.current_variable_count


    def staircase_alo(self):
        my_staircase_alo = StairCaseALO(self.n, self.k, self.variable_list, self.current_variable_count)
        self.cnf += my_staircase_alo.cnf
        self.clause_count += my_staircase_alo.clause_count
        self.clause_count_alo += my_staircase_alo.clause_count
        self.added_variable += my_staircase_alo.current_variable_count - self.current_variable_count
        self.variable_count_alo = my_staircase_alo.current_variable_count - self.current_variable_count
        self.current_variable_count = my_staircase_alo.current_variable_count



def main():
    n = 200
    k = 5
    variable_list = list(range(1, n + 1))

    report_file = open("Results/report.txt", "w")

    print("Config1")
    config1 = Config1(n, k, variable_list, n)
    # print(config1)
    config1.cnf_file_export("Results/config1.cnf")
    report_file.write("Config 1: \n")
    report_file.write("Binomial staircase AMO + Binomial staircase ALO\n")
    report_file.write("added variable: " + str(config1.added_variable) + "\n")
    report_file.write("added clauses: " + str(config1.clause_count) + "\n")
    report_file.write("Variable count AMO: " + str(config1.variable_count_amo) + "\n")
    report_file.write("Variable count ALO: " + str(config1.variable_count_alo) + "\n")
    report_file.write("Clause count AMO: " + str(config1.clause_count_amo) + "\n")
    report_file.write("Clause count ALO: " + str(config1.clause_count_alo) + "\n")
    report_file.write("--------------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------------")

    print("Config2")
    config2 = Config2(n, k, variable_list, n)
    report_file.write("Config 2: \n")
    report_file.write("Binomial staircase AMO + Staircase ALO\n")
    report_file.write("added variable: " + str(config2.added_variable) + "\n")
    report_file.write("added clauses: " + str(config2.clause_count) + "\n")
    report_file.write("Variable count AMO: " + str(config2.variable_count_amo) + "\n")
    report_file.write("Variable count ALO: " + str(config2.variable_count_alo) + "\n")
    report_file.write("Clause count AMO: " + str(config2.clause_count_amo) + "\n")
    report_file.write("Clause count ALO: " + str(config2.clause_count_alo) + "\n")
    report_file.write("--------------------------------------------------------------------------\n")
    config2.cnf_file_export("Results/config2.cnf")
    # print(config2)
    print("--------------------------------------------------------------------------")

    print("Config3")
    config3 = Config3(n, k, variable_list, n)
    config3.cnf_file_export("Results/config3.cnf")
    report_file.write("Config 3: \n")
    report_file.write("Sequential counter staircase AMO + Staircase ALO\n")
    report_file.write("added variable: " + str(config3.added_variable) + "\n")
    report_file.write("added clauses: " + str(config3.clause_count) + "\n")
    report_file.write("Variable count AMO: " + str(config3.variable_count_amo) + "\n")
    report_file.write("Variable count ALO: " + str(config3.variable_count_alo) + "\n")
    report_file.write("Clause count AMO: " + str(config3.clause_count_amo) + "\n")
    report_file.write("Clause count ALO: " + str(config3.clause_count_alo) + "\n")
    report_file.write("--------------------------------------------------------------------------\n")
    # print(config2)
    print("--------------------------------------------------------------------------")

    print("Config21")
    config21 = Config21(n, k, variable_list, n)
    config21.cnf_file_export("Results/config21.cnf")
    report_file.write("Config 21: \n")
    report_file.write("Binomial staircase AM2 + Staircase ALO\n")
    report_file.write("added variable: " + str(config21.added_variable) + "\n")
    report_file.write("added clauses: " + str(config21.clause_count) + "\n")
    report_file.write("Variable count AMO: " + str(config21.variable_count_amo) + "\n")
    report_file.write("Variable count ALO: " + str(config21.variable_count_alo) + "\n")
    report_file.write("Clause count AMO: " + str(config21.clause_count_amo) + "\n")
    report_file.write("Clause count ALO: " + str(config21.clause_count_alo) + "\n")
    report_file.write("--------------------------------------------------------------------------\n")

    print("Config31")
    config31 = Config31(n, k, variable_list, n)
    config31.cnf_file_export("Results/config31.cnf")
    report_file.write("Config 31: \n")
    report_file.write("Sequential counter staircase AM2 + Staircase ALO\n")
    report_file.write("added variable: " + str(config31.added_variable) + "\n")
    report_file.write("added clauses: " + str(config31.clause_count) + "\n")
    report_file.write("Variable count AMO: " + str(config31.variable_count_amo) + "\n")
    report_file.write("Variable count ALO: " + str(config31.variable_count_alo) + "\n")
    report_file.write("Clause count AMO: " + str(config31.clause_count_amo) + "\n")
    report_file.write("Clause count ALO: " + str(config31.clause_count_alo) + "\n")
    report_file.write("--------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()



