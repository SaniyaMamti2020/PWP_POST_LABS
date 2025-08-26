import tkinter as tk

def show_text():
    entered = entry.get()
    label.config(text=f"You typed: {entered}")

# main window
root = tk.Tk()
root.title("Text Input App")
root.geometry("300x150")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Show Text", command=show_text, font=("Arial", 12))
button.pack(pady=5)

label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
print("\n 3EK3_16_Saniya_Mamti")