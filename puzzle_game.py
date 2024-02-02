import turtle
import time
from frame import FrameTurtle
from logicList import LogicList

class ControlTurtle(turtle.Turtle):
    file_path: str = "./Resources/mario.puz"
    cheat_mode: bool = False
    count: int = 0
    max_round: int
    win_list: LogicList = LogicList()
    win: turtle.Screen
    frame_turtle: turtle.Turtle
    ranking: str = f"Leaders:\n\n 3: Keith\n 4: Khaira\n 5: Keith"
    
    function_turtle_list: list = []
    
    file_dict: dict
    
    button_string_list: list = []
    ranking: str

    animation_turtle_dict: dict

    function_location: list = [(30,-200), (140,-200), (250,-200),(90,150),(-400,-250),(270, 400)]
    position_list: list = [(-360,320), (-260, 320), (-160, 320), (-60,320),
                           (-360,220), (-260, 220), (-160, 220), (-60,220),
                           (-360,120), (-260, 120), (-160, 120), (-60,120),
                           (-360,20), (-260, 20), (-160, 20), (-60,20),
                          ]

    def __init__(self):
        '''
        Method:    this is the initial method, create the turtle game frame and set the basic
                   the main purpose is add a listener object which call self.click function 
                   and create a backend_list object which check the win and lose stage
        Parameter: self
        Return   : None
        '''
        self.win = turtle.Screen()
        self.win.setup(width = 1000, height = 1000)
        
        name = turtle.textinput("CS5001 Puzzle Slide", "your name")
        self.max_round = int(turtle.textinput("CS5001 Puzzle Slide", 
                                            "Enter the number of moves you want(5-200)?"))
        
        frame_turtle = FrameTurtle(screen = self.win)

        
        self.set_up_turtle()
        self.win.onclick(self.click)
        turtle.mainloop()

    def set_up_turtle(self):
        '''
        Method:    This is the setting stage method, which call the frame turtle to draw
                   the frame and setup all datastructures
        Parameter: self
        Return   : None
        '''
        button_string_list = ["./Resources/Resources/resetbutton.gif",
                              "./Resources/Resources/loadbutton.gif",
                              "./Resources/Resources/quitbutton.gif"]
            
        for i in range(5):
            self.function_turtle_list.append(turtle.Turtle())
            self.function_turtle_list[i].speed(10)
            self.function_turtle_list[i].penup()
            self.function_turtle_list[i].goto(self.function_location[i])
                
            if i < 3:
                self.win.addshape(button_string_list[i])
                self.function_turtle_list[i].shape(button_string_list[i])
                                   
            if i == 3:
                self.function_turtle_list[i].color("blue")
                self.function_turtle_list[i].write(self.ranking, 
                                          font = ("Verdana", 30, "normal"))
            if i == 4:
                self.function_turtle_list[4].clear()
                self.function_turtle_list[i].write(f"Player Moves: {self.count}", 
                                          font = ("Verdana", 30, "normal"))
        self.reset_turtle()
            
    def reset_turtle(self):
        '''
        Method:    This is the reset method, it is a part of set_up method, however
                   when the game reset, it only run partial, which is this one
        Parameter: self
        Return   : None
        '''
        self.file_dict = self.read_file()
        
        try:
            self.function_turtle_list.append(turtle.Turtle())
            self.function_turtle_list[-1].speed(10)
            self.function_turtle_list[-1].penup()
            self.function_turtle_list[-1].goto(self.function_location[-1])
            self.win.addshape(self.file_dict["thumbnail"])
            self.function_turtle_list[-1].shape(self.file_dict["thumbnail"])
        except AttributeError:
            print("Excetpion catched at line 102")
        except KeyError:
            print("This file doesn't support this dictionary")

        self.turtle_dict = {}
        self.backend_list = LogicList(4)
        
        if self.cheat_mode:
            self.backend_list.master_list[15] = 15 
            self.backend_list.master_list[14] = 16
        else:
        	self.backend_list.shuffle()

        keys = self.backend_list.get_list()
        
        if len(self.file_dict) != 0:
            for i in keys:	
                self.turtle_dict[i] = [i,turtle.Turtle()]
                self.win.addshape(self.file_dict[str(i)])
                self.turtle_dict[i][1].shape(self.file_dict[str(i)])		
                self.turtle_dict[i][1].penup()
		
            for num, key in enumerate(self.turtle_dict):			
                self.turtle_dict[key].append(self.position_list[num])
                self.turtle_dict[key][1].goto(self.turtle_dict[key][2])

    def click(self, x, y):
        '''
        Method:    This is the click function, it holds everything about mouse click
                   and make reaction
                   if y >= -140 holds the animation part, and -260 <y< -140 holds the
                   button part
        Parameter: self, x_coor, y_cood
        Return   : None
        '''
        if y >= -140:
            turtle_number = 0
            for key in self.turtle_dict:
                if abs(x - self.turtle_dict[key][2][0]) < 49\
                and abs(y - self.turtle_dict[key][2][1]) < 49:
                    turtle_number = self.turtle_dict[key][0]
                    break
		
            if turtle_number != 0:
                print(self.backend_list)
                if self.backend_list.is_valid(turtle_number):
                    self.backend_list.swap_backend(turtle_number)
				
                    self.turtle_dict[turtle_number][2], self.turtle_dict[16][2] =\
                    self.turtle_dict[16][2],self.turtle_dict[turtle_number][2]

                    self.turtle_dict[turtle_number][1].goto(self.turtle_dict[turtle_number][2])
                    self.turtle_dict[16][1].goto(self.turtle_dict[16][2])
                    self.count += 1
                    #self.function_turtle_list[-1].goto()
                    self.function_turtle_list[4].clear()
                    self.function_turtle_list[4].write(f"Player Moves: {self.count}",
                                                        font = ("Verdana", 35, "normal"))
                    self.is_game_over()
                    self.is_win()
                else:
                    print("This is not a valid number")
                print(self.backend_list)

        elif -260 < y < -140:
            if -20 < x < 80:
                self.cheat_mode = True
                self.reset_turtle()               
            elif 90 < x < 190:
                for i in self.turtle_dict:
                	self.turtle_dict[i][1].shape("classic")
                self.cheat_mode = False
                self.file_path = turtle.textinput("Please Input the path name", 
                	                    "e.g: ./Resources/mario.puz")
                self.count =0
                self.reset_turtle()
            elif 200 < x < 300:
                exit()

    def is_game_over(self):
        '''
        Method:    This method check if the game is lost
        Parameter: self
        Return   : None
        '''
        if self.count == self.max_round:
            
            self.win.addshape("./Resources/Resources/Lose.gif")
            self.function_turtle_list[4].shape("./Resources/Resources/Lose.gif")
            time.sleep(3)
            print("Game_OVER")
            exit()

    def is_win(self):
        '''
        Method:   This method check if the game is win
        Parameter: self
        Return   : None
        '''
        if self.backend_list == self.win_list:
            
            self.win.addshape("./Resources/Resources/winner.gif")
            self.function_turtle_list[4].shape("./Resources/Resources/winner.gif")
            time.sleep(3)
            print("You win")
            exit()

    def read_file(self):
        '''
        Method:    This method read the file, and convert the file to a python dict
        Parameter: self
        Return   : dict
        '''
        try:
            file = open(self.file_path)
            file_in_dict = {}
            for row in file:
                row = row.strip().split(":")
                file_in_dict[row[0]] = row[1].strip()
            if len(file_in_dict) != 20:
                raise Exception()
            return file_in_dict
        except FileNotFoundError:
            print("Sorry, we didn't find the file with your path")
            write_file = open("5001_puzzle.err","a")
            write_file.write(f"Sorry, we didn't find the file with your path\n")
            self.win.addshape("./Resources/Resources/file_error.gif")
            self.function_turtle_list[4].shape("./Resources/Resources/file_error.gif")
            time.sleep(2)
            self.function_turtle_list[4].shape("classic")
            write_file.close()
            return {}
        except:
            print("Sorry we can't built puzzle with that file")
            write_file = open("5001_puzzle.err","a")
            write_file.write(f"{self.file_path} can not create puzzle\n")
            self.win.addshape("./Resources/Resources/file_error.gif")
            self.function_turtle_list[4].shape("./Resources/Resources/file_error.gif")
            time.sleep(2)
            self.function_turtle_list[4].shape("classic")
            write_file.close()
            return {}

def main():
    rule = ControlTurtle()
if __name__ == '__main__':
	main()
