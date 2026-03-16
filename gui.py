import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import subprocess
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct relative paths to the script files
detector_path = os.path.join(script_dir, 'detector.py')
dataset_creator_path = os.path.join(script_dir, 'dataset_creator.py')
trainer_path = os.path.join(script_dir, 'trainer.py')

# Function to verify login credentials
def login(entry_username, entry_password, root):
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('face_recognition.db')
    c = conn.cursor()

    # Check if the table exists
    c.execute('''CREATE TABLE IF NOT EXISTS account (
                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT UNIQUE, 
                 password TEXT)''')

    c.execute("SELECT * FROM account WHERE username=? AND password=?", (username, password))
    result = c.fetchone()

    if result:
        root.destroy()  # Close the window on successful login
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

    conn.close()

# Function to create a new account
def create_account(entry_username, entry_password, root):
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('face_recognition.db')
    c = conn.cursor()

    # Check if the table exists
    c.execute('''CREATE TABLE IF NOT EXISTS account (
                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT UNIQUE, 
                 password TEXT)''')

    try:
        c.execute("INSERT INTO account (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        root.destroy()  # Close the window after account creation
        open_dashboard()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    finally:
        conn.close()

# Function to open the dashboard
def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")

    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TButton', font=('Helvetica', 12))

    main_frame = ttk.Frame(dashboard, padding="20")
    main_frame.pack(expand=True)

    label_title = ttk.Label(main_frame, text="Dashboard", font=('Helvetica', 16))
    label_title.pack(pady=10)

    live_feed_button = ttk.Button(main_frame, text="Live Feed", command=open_live_feed)
    live_feed_button.pack(pady=10)

    face_registration_button = ttk.Button(main_frame, text="Face Registration", command=open_face_registration)
    face_registration_button.pack(pady=10)

    dashboard.mainloop()

# Function to open the live feed
def open_live_feed():
    try:
        print(f"Opening live feed from: {detector_path}")  # Debugging line
        subprocess.Popen(['python', detector_path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open live feed: {e}")

# Function to open face registration
def open_face_registration():
    try:
        print(f"Opening dataset creator from: {dataset_creator_path}")  # Debugging line
        print(f"Opening trainer from: {trainer_path}")  # Debugging line
        subprocess.Popen(['python', dataset_creator_path])
        # subprocess.Popen(['python', trainer_path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open face registration: {e}")

# GUI for login and account creation
def run_gui():
    root = tk.Tk()
    root.title("Login / Create Account")
    root.geometry("400x300")

    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TEntry', font=('Helvetica', 12))
    style.configure('TButton', font=('Helvetica', 12))

    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(expand=True)

    label_username = ttk.Label(main_frame, text="Username")
    label_username.pack(pady=5)
    entry_username = ttk.Entry(main_frame)
    entry_username.pack(pady=5)

    label_password = ttk.Label(main_frame, text="Password")
    label_password.pack(pady=5)
    entry_password = ttk.Entry(main_frame, show="*")
    entry_password.pack(pady=5)

    login_button = ttk.Button(main_frame, text="Login", command=lambda: login(entry_username, entry_password, root))
    login_button.pack(pady=10)

    create_account_button = ttk.Button(main_frame, text="Create Account", command=lambda: create_account(entry_username, entry_password, root))
    create_account_button.pack(pady=10)

    root.mainloop()

def main():
    run_gui()

'''
if __name__ == "__main__":
    main()
'''