import tkinter as tk
from modules.listener import listen
from modules.commands import handle_command
from modules.speaker import speak
from modules.gui import PDA_GUI

def main():
    speak("How can I help you?")
    while True:
        command = listen()
        handle_command(command)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDA_GUI(root)
    root.mainloop()
