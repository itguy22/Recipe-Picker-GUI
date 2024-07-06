import tkinter as tk
from PIL import ImageTk

# initialize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

# place app in the center of the screen
x = root.winfo_screenwidth() // 2

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg="#3d6466")
frame1.grid(row=0, column=0)

#frame1 widgets
logo_img = ImageTk.PhotoImage(file="starter_files/assets/RRecipe_logo.png")
logo_widget = tk.Label(frame1, image=logo_img)
logo_widget.image = logo_img
logo_widget.pack()


# run app
root.mainloop()