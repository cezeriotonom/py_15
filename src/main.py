import tkinter as tk

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Hello World App")

    # Create a label with the message
    label = tk.Label(window, text="Hello, World!", padx=40, pady=20)
    label.pack()

    # Start the GUI event loop
    window.mainloop()

if __name__ == "__main__":
    main()
