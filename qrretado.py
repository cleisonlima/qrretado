# ==========================================================
# QRretado! - Gerador de QR Code
# Autor: Cleison Lima
# Direitos autorais © 2025 Cleison Lima
# Todos os direitos reservados.
# ==========================================================

import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

def gerar_qr():
    texto = entrada.get()
    if not texto.strip():
        messagebox.showwarning("Aviso", "Digite um texto ou link para gerar o QR Code!")
        return
    
    # Gerando QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(texto)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Mostrando no app
    img.save("qrretado.png")
    img_tk = ImageTk.PhotoImage(img.resize((200, 200)))
    label_img.config(image=img_tk)
    label_img.image = img_tk

    messagebox.showinfo("QRretado!", "QR Code gerado com sucesso e salvo como 'qrretado.png'")

def salvar_qr():
    texto = entrada.get()
    if not texto.strip():
        messagebox.showwarning("Aviso", "Digite algo para gerar o QR Code primeiro!")
        return
    
    # Gerando novamente para salvar
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(texto)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    caminho = filedialog.asksaveasfilename(defaultextension=".png",
                                           filetypes=[("PNG files", "*.png")],
                                           title="Salvar QR Code")
    if caminho:
        img.save(caminho)
        messagebox.showinfo("QRretado!", f"QR Code salvo em:\n{caminho}")

# ================== Interface Tkinter ==================
root = tk.Tk()
root.title("QRretado!")
root.geometry("400x500")
root.configure(bg="#fefefe")

titulo = tk.Label(root, text="QRretado!", font=("Arial", 20, "bold"), fg="#c0392b", bg="#fefefe")
titulo.pack(pady=10)

subtitulo = tk.Label(root, text="Digite um texto ou link e gere seu QR Code!", font=("Arial", 10), bg="#fefefe")
subtitulo.pack()

entrada = tk.Entry(root, width=40, font=("Arial", 12))
entrada.pack(pady=10)

btn_gerar = tk.Button(root, text="Gerar QR Code", command=gerar_qr, bg="#27ae60", fg="white", font=("Arial", 12, "bold"))
btn_gerar.pack(pady=5)

btn_salvar = tk.Button(root, text="Salvar QR Code", command=salvar_qr, bg="#2980b9", fg="white", font=("Arial", 12, "bold"))
btn_salvar.pack(pady=5)

label_img = tk.Label(root, bg="#fefefe")
label_img.pack(pady=20)

# Rodapé com direito autoral
rodape = tk.Label(
    root, 
    text="© 2025 Cleison Lima", 
    font=("Arial", 9, "italic"), 
    bg="#fefefe", 
    fg="#7f8c8d"
)
rodape.pack(side="bottom", pady=5)

root.mainloop()
