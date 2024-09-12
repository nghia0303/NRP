from SC import SequentialCounterEncoding

class SCAMO(SequentialCounterEncoding):

    def __init__(self, n, k, variable_list, current_variable_count):
        super().__init__(n, k, variable_list, current_variable_count)

        self.add_s_map()

        self.at_most_one()

    def add_s_map(self):
        for i in range(1, self.n):
            self.current_variable_count += 1
            self.s_map[i] = self.current_variable_count

    def at_most_one(self):


        pass