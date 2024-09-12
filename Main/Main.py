from Binomial.BinomialALO import BinomialALO
from Binomial.BinomialAMO import BinomialAMO
from Binomial.BinomialAMK import BinomialAMK

from SC.SCAMO import SCAMO
from SC.SCAMK import SCAMK


from cnf.CNF import CNF

def main():
    n = 10
    k = 5
    variable_list = list(range(1, n + 1))

    scamk = SCAMK(
        n, k, variable_list, n
    )

    cnf = CNF(
        scamk.current_variable_count, scamk.clause_count, scamk.cnf
    )

    cnf.write_to_file("../cnf/SCAMK.cnf")


if __name__ == '__main__':
    main()