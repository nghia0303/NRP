from Binomial.BinomialALO import BinomialALO
from Binomial.BinomialAMO import BinomialAMO

from cnf.CNF import CNF

def main():
    n = 20
    k = 5
    variable_list = list(range(1, n + 1))

    encoding = BinomialAMO(
        n, variable_list, n
    )

    cnf = CNF(
        encoding.current_variable_count,
        encoding.clause_count,
        encoding.cnf
    )

    print(cnf)
    print("added variable", encoding.current_variable_count)
    print("added clauses", encoding.clause_count)
    cnf.write_to_file("../cnf/BinomialAMO.cnf")

if __name__ == '__main__':
    main()