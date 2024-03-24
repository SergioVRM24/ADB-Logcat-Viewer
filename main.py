import subprocess
import tkinter as tk
from tkinter import ttk
import threading

def close_window():
    root.destroy()

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    for index, line in enumerate(process.stdout):
        if line.lower().count("window") > 0:
            text_widget.insert(tk.END, line)
            text_widget.see(tk.END)  # Scroll to the end of the text
            text_widget.update_idletasks()  # Update the widget to display the new content

def start_command_thread():
    # Example command (replace with your actual command)
    command = ["adb", "logcat"]
    run_command(command)

# Create the main window
root = tk.Tk()
root.title("Command Output Viewer")

# Create a text widget to display the output
text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

# Start the command thread
command_thread = threading.Thread(target = start_command_thread)
command_thread.start()

close_button = tk.Button(root, text="Close Window", command=close_window)
close_button.pack()

root.mainloop()