from Binomial.BinomialALO import BinomialALO
from Binomial.BinomialAMO import BinomialAMO
from Binomial.BinomialAMK import BinomialAMK

from cnf.CNF import CNF

def main():
    n = 10
    k = 5
    variable_list = list(range(1, n + 1))

    binomial_amk = BinomialAMK(n, k, variable_list, n)

    print(binomial_amk)

    cnf = CNF(n, binomial_amk.clause_count, binomial_amk.cnf)

    cnf.write_to_file("../cnf/binomial_amk.cnf")


if __name__ == '__main__':
    main()