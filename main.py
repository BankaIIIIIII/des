import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from cryptography.fernet import Fernet

class AESApp:
    def __init__(self, master):
        self.master = master
        self.master.title("AES Encryption / Decryption")
        self.master.geometry("400x400")
        self.master.configure(bg='white')

        # إنشاء المفتاح وكائن خوارزمية AES
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        # إنشاء واجهة المستخدم
        self.label = tk.Label(
            self.master, text="Choose an option:", font=("Helvetica", 14), pady=10
        )
        self.label.pack()

        self.option_var = tk.StringVar()
        self.option_var.set("Encryption")

        self.option_radio_encrypt = tk.Radiobutton(
            self.master,
            text="Encryption",
            variable=self.option_var,
            value="Encryption",
            font=("Helvetica", 12),
            padx=10,
            pady=5
        )
        self.option_radio_encrypt.pack()

        self.option_radio_decrypt = tk.Radiobutton(
            self.master,
            text="Decryption",
            variable=self.option_var,
            value="Decryption",
            font=("Helvetica", 12),
            padx=10,
            pady=5
        )
        self.option_radio_decrypt.pack()

        self.text_label = tk.Label(
            self.master,
            text="Enter Text:",
            font=("Helvetica", 12),
            pady=10
        )
        self.text_label.pack()

        self.text_input = tk.Text(
            self.master,
            height=5,
            width=30,
            font=("Helvetica", 12)
        )
        self.text_input.pack()

        self.run_button = tk.Button(
            self.master,
            text="Run",
            font=("Helvetica", 12),
            padx=10,
            pady=5,
            command=self.run_action
        )
        self.run_button.pack()

        self.output_label = tk.Label(
            self.master,
            text="Output:",
            font=("Helvetica", 14),
            pady=10,
        )
        self.output_label.pack()

        self.output_text = tk.Text(
            self.master,
            height=5,
            width=30,
            font=("Helvetica", 12)
        )
        self.output_text.pack()

    def run_action(self):
        option = self.option_var.get()
        text = self.text_input.get("1.0", tk.END).strip().encode()

        if option == "Encryption":
            encrypted_text = self.cipher_suite.encrypt(text)
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, encrypted_text.decode())
        else:
            decrypted_text = self.cipher_suite.decrypt(text)
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, decrypted_text.decode())


root = tk.Tk()
app = AESApp(root)
root.mainloop()