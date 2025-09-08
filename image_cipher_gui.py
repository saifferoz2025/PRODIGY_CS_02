import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    result_array = img_array ^ key
    result_img = Image.fromarray(result_array.astype('uint8'))
    result_img.save(output_path)

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    entry_input.delete(0, tk.END)
    entry_input.insert(0, file_path)

def process_image(action):
    input_file = entry_input.get()
    key = entry_key.get()

    if not input_file:
        messagebox.showerror("Error", "Please select an image file")
        return
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be an integer (0-255)")
        return

    key = int(key)
    output_file = "encrypted.png" if action == "encrypt" else "decrypted.png"

    try:
        encrypt_decrypt_image(input_file, output_file, key)
        messagebox.showinfo("Success", f"{action.capitalize()}ed image saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("🖼 Pixel Manipulation Image Cipher")
root.geometry("450x250")
root.config(bg="#1e1e2e")

tk.Label(root, text="Pixel Manipulation Image Cipher", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2e").pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=5)

tk.Label(frame, text="Input Image:", fg="white", bg="#1e1e2e").grid(row=0, column=0, padx=5, pady=5)
entry_input = tk.Entry(frame, width=30)
entry_input.grid(row=0, column=1, padx=5)
btn_browse = tk.Button(frame, text="Browse", command=choose_file, bg="#4CAF50", fg="white")
btn_browse.grid(row=0, column=2, padx=5)

tk.Label(frame, text="Key (0-255):", fg="white", bg="#1e1e2e").grid(row=1, column=0, padx=5, pady=5)
entry_key = tk.Entry(frame, width=10)
entry_key.grid(row=1, column=1, padx=5, pady=5)

frame_btns = tk.Frame(root, bg="#1e1e2e")
frame_btns.pack(pady=15)

btn_encrypt = tk.Button(frame_btns, text="Encrypt", command=lambda: process_image("encrypt"), bg="#2196F3", fg="white", width=10)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_btns, text="Decrypt", command=lambda: process_image("decrypt"), bg="#f44336", fg="white", width=10)
btn_decrypt.grid(row=0, column=1, padx=10)

root.mainloop()