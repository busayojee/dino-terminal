
import random

class Game:
    dinoHeight = 11
    def __init__(self, stdscr, _screen_dimension, dino):
        self.stdscr = stdscr
        self.dino = dino
        self.screen_height, self.screen_width = _screen_dimension
        self.LineBuffer = []
        self.gen = True
        self.__num= 0
        self.linBr = 0
        self.score = 0
        self.frame_time = 0.1

    @property
    def _num(self):
        return self.__num 

    def draw_dino(self, y_pos, x_pos):
        for i, row in enumerate(self.dino):
            for j, char in enumerate(row):
                part_height = Game.dinoHeight - i + y_pos
                self.stdscr.addstr(self.screen_height - part_height, j + x_pos, char)
                


    def first_line(self, lenght):
        len = int(lenght/32)
        len += lenght%32 
        for i in range(int(len)):
            for j in range(30):
                self.LineBuffer.append('_')
            self.LineBuffer.append('-')
            self.LineBuffer.append('-')

    

    def draw_line_buffer(self):
        for i in range(self.screen_width):
            if self.LineBuffer[i] == '-':
                self.stdscr.addstr(self.screen_height - 2, i, self.LineBuffer[i])
            else:
                self.stdscr.addstr(self.screen_height - 2, i, self.LineBuffer[i])

    def move_line_buffer(self):
        for i in range(self.screen_width-1):
            self.LineBuffer[i] = self.LineBuffer[i+1]

    def generate_obstacle(self):
        num = random.randint(20, 35)
        return num
    def draw_obstacle(self):
        if self.gen:
            self.__num = self.generate_obstacle()
            self.gen = False
        if(self.linBr >self._num):
            self.LineBuffer[self.screen_width-1] = '-'
            if(self.linBr>self._num+1):  
                self.LineBuffer[self.screen_width-1] = '-'
                self.linBr = 0    
                self.gen=True
        else:
            self.LineBuffer[self.screen_width-1] = '_'

    def increment_score(self):
        self.score += 1

    def display_score(self):
        score_str = f"Score: {self.score}"
        self.stdscr.addstr(0, self.screen_width - len(score_str), score_str)

