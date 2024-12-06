class Simulator(object): 

    def __init__(self):
        self.symbols = {0: 'do nothing',
                        1 : 'move alone',
                        2 : 'move with wolf',
                        3 : 'move with goat',
                        4 : 'move with cabbage'}
        self.reset()

    def reset(self):
        self.state = {'wolf': True, 'goat': True, 'cabbage': True, 'farmer' : True}
        self.fit = 0
        self.need_to_move = 0

    def count_need_to_move(self):
        self.need_to_move = 0
        for need_to_move in self.state.values():
            if need_to_move:
                self.need_to_move += 1

    def simulate(self, steps):
        self.reset()
        for step in steps:
            if int(step) == 1:
                self.state['farmer'] = not self.state['farmer']
            if int(step) == 2:
                if self.state['farmer'] == self.state['wolf']:
                    self.state['farmer'] = not self.state['farmer']
                    self.state['wolf'] = not self.state['wolf']
                else:
                    self.fit += len(self.state) + 1
            if int(step) == 3:
                if self.state['farmer'] == self.state['goat']:
                    self.state['farmer'] = not self.state['farmer']
                    self.state['goat'] = not self.state['goat']
                else:
                    self.fit += len(self.state) + 1
            if int(step) == 4:
                if self.state['farmer'] == self.state['cabbage']:
                    self.state['farmer'] = not self.state['farmer']
                    self.state['cabbage'] = not self.state['cabbage']
                else:
                    self.fit += len(self.state) + 1
            self.count_need_to_move()
            if (self.state['goat'] == self.state['wolf']) and (self.state['farmer'] != self.state['goat']):
                self.fit += len(self.state) + 1
            if (self.state['goat'] == self.state['cabbage']) and (self.state['farmer'] != self.state['goat']):
                self.fit += len(self.state) + 1
            if int(step) == 0:
                self.fit += self.need_to_move
            else:
                self.fit += 1
        return self.fit

    def print(self, steps):
        for step in steps:
            if int(step) in self.symbols.keys():
                print(self.symbols[int(step)])
            else:
                print('invalid move')
