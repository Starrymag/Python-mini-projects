import tkinter as tk

WIDTH, HEIGHT = 605, 605
SIZE_WINDOW = "1010x610"
# SIZE_CANVAS = "600x600"
GRID = WIDTH // 3
OFFSET = 40
STROKE_WIDTH = 8
CIRCLE_RADIUS = 60

class Game:
    def __init__(self):
        self.field = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.window = tk.Tk()
        self.window.geometry(SIZE_WINDOW)
        self.window.title("TIC TAC TOE")
        
        self.canvas = tk.Canvas(self.window, bg="white", width=WIDTH, height=HEIGHT) 
        self.canvas.pack(side="left")


    def click_handler(self, event):
        x = event.x
        y = event.y
        x_coord = x // GRID
        y_coord = y // GRID        
        self.field[y_coord][x_coord] = "0"
        # [print(x) for x in self.field]


    def input_motion(self):
        self.window.bind("<Button-1>", self.click_handler)


    def proccesing(self):
        pass


    def draw(self):
        # draw field
        for i in range(2, WIDTH+4, WIDTH//3):
            self.canvas.create_line(i, 0, i, WIDTH, width=4)

        for i in range(2, HEIGHT+4, HEIGHT//3):
            self.canvas.create_line(0, i, HEIGHT, i, width=4)
            
        # draw items
        for y_i in range(len(self.field)):
            for x_i in range(len(self.field[y_i])):
                if self.field[y_i][x_i] == "X":
                    self.canvas.create_line(x_i*GRID + OFFSET, y_i*GRID + OFFSET, x_i*GRID + GRID - OFFSET, y_i*GRID + GRID - OFFSET, width=STROKE_WIDTH)
                    self.canvas.create_line(x_i*GRID + GRID - OFFSET, y_i*GRID + OFFSET, x_i*GRID + OFFSET, y_i*GRID + GRID - OFFSET, width=STROKE_WIDTH)
                if self.field[y_i][x_i] == "0":
                    self.canvas.create_oval(x_i*GRID + OFFSET, y_i*GRID + OFFSET, x_i*GRID + GRID - OFFSET, y_i*GRID + GRID - OFFSET, width=STROKE_WIDTH)


    def start_game(self):
        while True:
            self.input_motion()
            self.draw()
            self.window.update_idletasks()
            self.window.update()



if __name__ == "__main__":
    game = Game()
    game.start_game()
