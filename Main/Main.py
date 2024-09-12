from Binomial.BinomialALO import BinomialALO
from Binomial.BinomialAMO import BinomialAMO
from Binomial.BinomialAMK import BinomialAMK

from SC.SCAMO import SCAMO

from cnf.CNF import CNF

def main():
    n = 10
    k = 5
    variable_list = list(range(1, n + 1))

    scamo = SCAMO(
        n, k, variable_list, n
    )

    cnf = CNF(
        scamo.current_variable_count, scamo.clause_count, scamo.cnf
    )

    cnf.write_to_file("../cnf/SCAMO.cnf")


if __name__ == '__main__':
    main()