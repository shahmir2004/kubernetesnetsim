import tkinter as tk
from tkinter import messagebox
import requests


class ProgramRunner:
    def __init__(self, ping_server_url, tracert_server_url):
        self.ping_server_url = ping_server_url
        self.tracert_server_url = tracert_server_url

    def run_ping(self, flag=None):
        try:
            if flag:
                response = requests.get(f"{self.ping_server_url}?n={flag}")
            else:
                response = requests.get(self.ping_server_url)

            if response.status_code == 200:
                return response.text
            else:
                return f"Error: Server returned status code {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def run_tracert(self):
        try:
            response = requests.get(self.tracert_server_url)
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: Server returned status code {response.status_code}"
        except Exception as e:
            return f"Error: {e}"


def run_ping_with_flag():
    flag_value = flag_entry.get().strip()
    if not flag_value.isdigit():
        show_output("Please enter a valid number for the flag.")
        return

    output = program_runner.run_ping(flag=flag_value)
    show_output(output)


def run_ping_without_flag():
    output = program_runner.run_ping()
    show_output(output)


def run_tracert():
    output = program_runner.run_tracert()
    show_output(output)


def show_output(output):
    messagebox.showinfo("Output", output)


# URLs for the NGINX load balancer
PING_SERVER_URL = "http://localhost:8080/ping"
TRACERT_SERVER_URL = "http://localhost:8080/tracert"

# Initialize the ProgramRunner
program_runner = ProgramRunner(PING_SERVER_URL, TRACERT_SERVER_URL)

# Create GUI
root = tk.Tk()
root.title("Network Simulation GUI")
root.geometry("600x300")

label = tk.Label(root, text="Enter the number of pings:")
label.pack(pady=10)

flag_entry = tk.Entry(root)
flag_entry.pack()

button_with_flag = tk.Button(root, text="Run Ping (n times)", command=run_ping_with_flag, height=2, width=30)
button_with_flag.pack(pady=10)

button_without_flag = tk.Button(root, text="Run Ping (default)", command=run_ping_without_flag, height=2, width=30)
button_without_flag.pack(pady=10)

button_tracert = tk.Button(root, text="Run Tracert", command=run_tracert, height=2, width=30)
button_tracert.pack(pady=10)

root.mainloop()
