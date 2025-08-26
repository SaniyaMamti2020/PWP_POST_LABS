import tkinter as tk

def increment():
    global count
    count += 1
    label.config(text=f"Count: {count}")

# main window
root = tk.Tk()
root.title("Counter App")
root.geometry("250x150")

count = 0
label = tk.Label(root, text=f"Count: {count}", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Increment", command=increment, font=("Arial", 14))
button.pack()

root.mainloop()
print("\n 3EK3_16_Saniya_Mamti")