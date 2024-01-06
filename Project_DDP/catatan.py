import tkinter as tk
from tkinter import scrolledtext

def save_note():
    note_content = text_area.get("1.0", tk.END)
    with open("catatan.txt", "w") as file:
        file.write(note_content)
    status_label.config(text="Catatan disimpan!")

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Catatan")

# Text area untuk input catatan
text_area = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_area.pack(padx=10, pady=10)

# Tombol untuk menyimpan catatan
save_button = tk.Button(root, text="Simpan Catatan", command=save_note)
save_button.pack(pady=10)

# Label status
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
