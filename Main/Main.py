from ExperimentsConfig.Config import Config


from cnf.CNF import CNF

def main():
    n = 10
    k = 5
    variable_list = list(range(1, n + 1))

    config1 = Config(n, k, variable_list, 0)
    cnf = CNF(config1.cnf, config1.clause_count, n)
    print(cnf)




if __name__ == '__main__':
    main()