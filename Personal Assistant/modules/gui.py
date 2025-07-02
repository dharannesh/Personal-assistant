import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
from modules.listener import listen
from modules.commands import handle_command
from modules.speaker import speak

class PDA_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Digital Assistant")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f4f8")

        title = tk.Label(root, text="Personal Digital Assistant", font=("Segoe UI", 20, "bold"), bg="#f0f4f8", fg="#333")
        title.pack(pady=15)

        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=65, height=15, font=("Segoe UI", 11))
        self.output_area.pack(padx=20, pady=10)
        self.output_area.config(borderwidth=2, relief="solid")

        button_frame = tk.Frame(root, bg="#f0f4f8")
        button_frame.pack(pady=10)

        listen_btn = tk.Button(button_frame, text="Start Listening", font=("Segoe UI", 12), command=self.run_in_thread, bg="#4caf50", fg="white", padx=15, pady=5)
        listen_btn.grid(row=0, column=0, padx=10)


        speak_btn = tk.Button(button_frame, text="Speak Text", font=("Segoe UI", 12), command=self.speak_custom_text, bg="#ff9800", fg="white", padx=15, pady=5)
        speak_btn.grid(row=0, column=2, padx=10)

    def run_in_thread(self):
        threading.Thread(target=self.listen_and_respond, daemon=True).start()

    def listen_and_respond(self):
        speak("Listening for your command.")
        command = listen().strip()

        if command.lower() in [
            "no speech detected.",
            "sorry, i didn't catch that.",
            "sorry, network error."
        ]:
            self.output_area.insert(tk.END, f"You: {command}\n")
            self.output_area.insert(tk.END, f"PDA: I didn’t catch that. Please try again.\n\n")
            self.output_area.see(tk.END)
            return

        self.output_area.insert(tk.END, f"You: {command}\n")
        response = handle_command(command)
        self.output_area.insert(tk.END, f"PDA: {response}\n\n")
        self.output_area.see(tk.END)


    def speak_custom_text(self):
        text = self.output_area.get("1.0", tk.END).strip()
        if text:
            speak(text)
        else:
            speak("Please enter some text to speak.")
