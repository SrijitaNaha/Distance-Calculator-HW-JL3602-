from tkinter import *
from tkinter import messagebox


def calculate_distance():
    try:
        time = float(time_entry.get())
        speed = float(speed_entry.get())
        distance = time * speed
        result_label.config(text=f"The distance covered is {distance} km")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid time and speed")


root = Tk()
root.geometry("600x600")
root.title("Distance Calculator")

# Display heading
heading = Label(text="DISTANCE CALCULATOR", font=("Arial", 20), fg="grey")
heading.pack()


time_label = Label(root, text="Enter time (in hours):", font=("Arial", 12))
time_label.pack()

time_entry = Entry(root)
time_entry.pack()

speed_label = Label(root, text="Enter speed (in km/h):", font=("Arial", 12))
speed_label.pack()

speed_entry = Entry(root)
speed_entry.pack()

calculate_button = Button(
    root,
    text="Calculate Distance",
    bg="purple",
    fg="white",
    font=("Arial", 13),
    command=calculate_distance
)
calculate_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
