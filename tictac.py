import tkinter as tk

WIDTH, HEIGHT = 605, 605
SIZE_WINDOW = "1010x610"
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
        self.current_move = True
        self.display = {True: "X", False: "0"}
        self.flag = False
        self.var = tk.IntVar()
        self.button = tk.Button(self.window, text="restart", command=self.restart_handler)
        self.button.pack(side="right", padx=20)


    def click_handler(self, event):
        x = event.x
        y = event.y
        x_coord = x // GRID
        y_coord = y // GRID        
        if self.field[y_coord][x_coord] == " ":
            self.field[y_coord][x_coord] = self.display[self.current_move]
            self.current_move = not(self.current_move)

    
    def restart_handler(self):
        self.var.set(1)
        self.field = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.flag = False
        self.canvas.delete("all") 
        print("NEW GAME")


    def input_motion(self):
        self.window.bind("<Button-1>", self.click_handler)


    def input_restar(self):
        print("waiting...")
        self.button.wait_variable(self.var)


    def proccesing(self):
        # check rows
        for y_i in range(len(self.field)):
            if self.field[y_i] == ["X", "X", "X"] or self.field[y_i] == ["0", "0", "0"]:
                print("END OF THE GAME")
                self.flag = True
         
        # check columns
        for i in range(3):
            tmp_store = []
            for y_i in range(len(self.field)):
                tmp_store.append(self.field[y_i][i])
            if tmp_store == ["X", "X", "X"] or tmp_store == ["0", "0", "0"]:
                print("END OF THE GAME")
                self.flag = True

        # check diagoanl
        tmp_store = []
        for x_i in range(3):
            for y_i in range(3):
                if x_i == y_i:
                    tmp_store.append(self.field[y_i][x_i])
        if tmp_store == ["X", "X", "X"] or tmp_store == ["0", "0", "0"]:
                print("END OF THE GAME")
                self.flag = True

        # check another diagonal
        tmp_store = []
        for x_i in range(3):
            for y_i in range(3):
                if (x_i + y_i) == 2:
                    tmp_store.append(self.field[y_i][x_i])
        if tmp_store == ["X", "X", "X"] or tmp_store == ["0", "0", "0"]:
                print("END OF THE GAME")
                self.flag = True


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
            self.proccesing()
            self.window.update_idletasks()
            self.window.update()
            if self.flag:
                self.input_restar()
                



if __name__ == "__main__":
    game = Game()
    game.start_game()
