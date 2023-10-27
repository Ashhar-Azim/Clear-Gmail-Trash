import google.oauth2.credentials
from googleapiclient.discovery import build
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import logging

# Set up logging
logging.basicConfig(filename='gmail_api_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to toggle dark theme
def toggle_dark_theme():
    try:
        current_theme = style.theme_use()
        new_theme = "alt" if current_theme == "vista" else "vista"
        style.theme_use(new_theme)
        print(f"Switched to {new_theme} theme.")
    except tk.TclError as e:
        print(f"An error occurred while changing the theme: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Authenticate using OAuth 2.0 credentials
# Build the Gmail API service
service = build('gmail', 'v1', credentials=google.oauth2.credentials.Credentials.from_authorized_user_file('credentials.json'))

def delete_emails():
    try:
        # Gather input values
        keyword = keyword_entry.get()
        sender = sender_entry.get()
        subject = subject_entry.get()
        has_attachment = attachment_var.get()
        min_size = min_size_entry.get()
        max_size = max_size_entry.get()

        query = ""
        if keyword:
            query += f'"{keyword}" '
        if sender:
            query += f"from:{sender} "
        if subject:
            query += f"subject:{subject} "
        if has_attachment:
            query += "has:attachment "
        if min_size:
            query += f"size:{min_size}-"
        if max_size:
            query += f"-{max_size}"

        # Make the API request
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])

        if not messages:
            messagebox.showinfo("No Emails Found", "No emails found matching the specified criteria.")
            logging.info("No emails found matching the specified criteria.")
            return

        # Ask for confirmation before deleting
        confirmation = messagebox.askquestion("Confirmation", f"Found {len(messages)} email(s) matching the criteria. Delete them?")
        if confirmation == 'yes':
            # Delete the selected emails
            for message in messages:
                service.users().messages().delete(userId='me', id=message['id']).execute()
            messagebox.showinfo("Deletion Complete", f"Deleted {len(messages)} email(s) matching the criteria.")
            logging.info(f"Deleted {len(messages)} email(s) matching the criteria.")
        else:
            messagebox.showinfo("Operation Canceled", "No emails were deleted.")
            logging.info("Operation canceled. No emails were deleted.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        logging.error(f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Gmail API Email Deletion Tool")

# Set up a dark theme style
style = ThemedStyle(window)
style.set_theme("vista")

# GUI elements
frame = ttk.Frame(window, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Entry fields
keyword_label = ttk.Label(frame, text="Enter the keyword you want to filter by:")
keyword_label.grid(row=0, column=0, sticky=tk.W)
keyword_entry = ttk.Entry(frame)
keyword_entry.grid(row=0, column=1)

sender_label = ttk.Label(frame, text="Enter sender email address:")
sender_label.grid(row=1, column=0, sticky=tk.W)
sender_entry = ttk.Entry(frame)
sender_entry.grid(row=1, column=1)

subject_label = ttk.Label(frame, text="Enter email subject:")
subject_label.grid(row=2, column=0, sticky=tk.W)
subject_entry = ttk.Entry(frame)
subject_entry.grid(row=2, column=1)

attachment_var = tk.StringVar()
attachment_var.set("no")
attachment_checkbutton = ttk.Checkbutton(frame, text="Filter by emails with attachments", variable=attachment_var, onvalue="yes", offvalue="no")
attachment_checkbutton.grid(row=3, columnspan=2, sticky=tk.W)

min_size_label = ttk.Label(frame, text="Minimum email size (in bytes):")
min_size_label.grid(row=4, column=0, sticky=tk.W)
min_size_entry = ttk.Entry(frame)
min_size_entry.grid(row=4, column=1)

max_size_label = ttk.Label(frame, text="Maximum email size (in bytes):")
max_size_label.grid(row=5, column=0, sticky=tk.W)
max_size_entry = ttk.Entry(frame)
max_size_entry.grid(row=5, column=1)

# Buttons
delete_button = ttk.Button(frame, text="Delete Emails", command=delete_emails)
delete_button.grid(row=6, column=0, columnspan=2)

theme_toggle_button = ttk.Button(frame, text="Toggle Dark Theme", command=toggle_dark_theme)
theme_toggle_button.grid(row=7, column=0, columnspan=2)

window.mainloop()
