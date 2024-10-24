import socket
import tkinter as tk
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 65432

def send_message():
    message = entry.get()
    if not message:
        messagebox.showwarning("Warning", "Please enter a message")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            messagebox.showinfo("Server response:", f"{data.decode()}")
    except ConnectionRefusedError:
        messagebox.showerror("Error")

root = tk.Tk()
root.title("TCP Client")

label = tk.Label(root, text="Order ticket (Event_name, user_name, ticket_count):")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

root.mainloop()
