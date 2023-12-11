import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title('Snake Game')
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='black')
        self.canvas.pack()
        self.snake = [(20, 20)]
        self.food = self.create_food()
        self.direction = 'Right'
        self.score = 0
        self.paused = False

        self.draw_snake()
        self.draw_food()

        self.master.bind('<KeyPress>', self.change_direction)
        self.move()

    def draw_snake(self):
        self.canvas.delete('snake')
        for segment in self.snake:
            x, y = segment
            self.canvas.create_oval(x, y, x + 20, y + 20, fill='green', tags='snake')

    def draw_food(self):
        self.canvas.delete('food')
        x, y = self.food
        self.canvas.create_oval(x, y, x + 20, y + 20, fill='red', tags='food')

    def create_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                return x, y

    def move(self):
        if not self.paused:
            head_x, head_y = self.snake[-1]
            if self.direction == 'Right':
                new_head = (head_x + 20, head_y)
            elif self.direction == 'Left':
                new_head = (head_x - 20, head_y)
            elif self.direction == 'Up':
                new_head = (head_x, head_y - 20)
            elif self.direction == 'Down':
                new_head = (head_x, head_y + 20)

            self.snake.append(new_head)

            if new_head == self.food:
                self.food = self.create_food()
                self.score += 1
            else:
                self.snake.pop(0)

            if (new_head[0] < 0 or new_head[0] >= 400 or
                new_head[1] < 0 or new_head[1] >= 400 or
                new_head in self.snake[:-1]):
                self.game_over()
                return

            self.draw_snake()
            self.draw_food()

        self.master.after(100, self.move)

    def change_direction(self, event):
        if event.keysym in ['Left', 'Right', 'Up', 'Down']:
            opposite = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}
            if event.keysym != opposite.get(self.direction):
                self.direction = event.keysym

    def game_over(self):
        self.paused = True
        self.canvas.create_text(200, 200, text=f'Game Over! Score: {self.score}', fill='white', font=('Arial', 20))

def run_game():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == '__main__':
    run_game()
