import tkinter as tk
import sched, time
import pygame


#making it into a website
from flask import Flask, render_template, request
app = Flask(__name__)
# make the list of users
users = []
# Function to add users
def add_user(class_amount):
    while len(users) < class_amount:
        username = request.form.get(f'user_{len(users)+1}')
        if username:
            users.append(username)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        class_amount = int(request.form['class_amount'])
        add_user(class_amount)
    return render_template('index.html', users=users)
if __name__ == '__main__':
    app.run(debug=True)


#GRID

display_width = 600
display_height = 700


def grid_click(row, col):
  print ("Clicked on cell at coordinates:", (row, col))
root = tk.Tk()
root.title("Player List: " + ", ".join(users))

for i in range(7):
    for j in range(7):
        btn = tk.Button(root, width=4, height=2, command=lambda row=i, col=j: grid_click(row, col))
        btn.grid(row=i, column=j)

root.mainloop()

#BUTTONS

class DraggableButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.bind("<Button-1>", self.on_button_press)
        self.bind("<B1-Motion>", self.on_move)
        self.bind("<ButtonRelease-1>", self.on_button_release)
        self.start_x = 0
        self.start_y = 0

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_move(self, event):
        x, y = (event.x - self.start_x + self.winfo_x()), (event.y - self.start_y + self.winfo_y())
        self.place(x=x, y=y)

    def on_button_release(self, event):
        pass

root = tk.Tk()
root.geometry("400x400")

button = DraggableButton(root, text="Drag me!")
button.place(x=50, y=50)

root.mainloop()

def button_click():
    print("Button clicked")

# Create the main application window
root = tk.Tk()
root.title("Button Example")

# Define and pack the button
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()


