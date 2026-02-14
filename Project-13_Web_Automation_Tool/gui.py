import tkinter as tk
from tkinter import messagebox
from main import WebAutomation


class App:
    """
    Tkinter GUI Application Class.

    Responsible for:
    - Rendering UI components
    - Capturing user input
    - Calling automation backend
    """

    def __init__(self, root):
        """
        Initialize the GUI layout and automation backend.
        """

        self.root = root
        self.root.title("Web Automation GUI")
        self.root.geometry("450x350")

        # Initialize browser automation only once
        # This prevents multiple Chrome windows from opening
        self.webautomation = WebAutomation()

        # ==============================
        # Login Frame
        # ==============================
        self.login_frame = tk.LabelFrame(self.root, text="Login Details")
        self.login_frame.pack(fill="x", padx=10, pady=5)

        # Username
        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Password
        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Allow column resizing
        self.login_frame.columnconfigure(1, weight=1)

        # ==============================
        # Form Frame
        # ==============================
        self.form_frame = tk.LabelFrame(self.root, text="Form Details")
        self.form_frame.pack(fill="x", padx=10, pady=5)

        # Full Name
        tk.Label(self.form_frame, text="Full Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_fullname = tk.Entry(self.form_frame)
        self.entry_fullname.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Email
        tk.Label(self.form_frame, text="Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Current Address
        tk.Label(self.form_frame, text="Current Address:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_current_address = tk.Entry(self.form_frame)
        self.entry_current_address.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Permanent Address
        tk.Label(self.form_frame, text="Permanent Address:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_permanent_address = tk.Entry(self.form_frame)
        self.entry_permanent_address.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.form_frame.columnconfigure(1, weight=1)

        # ==============================
        # Buttons Frame
        # ==============================
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=15)

        tk.Button(
            self.button_frame,
            text="Submit",
            width=15,
            command=self.submit_data
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            self.button_frame,
            text="Close Browser",
            width=15,
            command=self.close_browser
        ).grid(row=0, column=1, padx=10)

    # ==========================================================
    # Submit Data Function
    # ==========================================================
    def submit_data(self):
        """
        Collect user input from GUI fields,
        validate input, and trigger Selenium automation.
        """

        # Retrieve user inputs
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        fullname = self.entry_fullname.get().strip()
        email = self.entry_email.get().strip()
        current_address = self.entry_current_address.get().strip()
        permanent_address = self.entry_permanent_address.get().strip()

        # Basic validation to prevent empty submission
        if not username or not password:
            messagebox.showerror("Input Error", "Username and Password are required.")
            return

        if not fullname or not email:
            messagebox.showerror("Input Error", "Full Name and Email are required.")
            return

        try:
            # Call backend automation functions
            self.webautomation.login(username, password)
            self.webautomation.fill_form(
                fullname,
                email,
                current_address,
                permanent_address
            )

            messagebox.showinfo("Success", "Data submitted successfully!")

        except Exception as e:
            # Catch and display automation errors
            messagebox.showerror("Automation Error", f"An error occurred:\n{e}")

    # ==========================================================
    # Close Browser Function
    # ==========================================================
    def close_browser(self):
        """
        Safely close the Selenium browser session.
        """
        try:
            self.webautomation.close()
            messagebox.showinfo("Closed", "Browser closed successfully.")
        except Exception:
            messagebox.showwarning("Warning", "Browser is already closed.")


# ==============================================================
# Application Entry Point
# ==============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
