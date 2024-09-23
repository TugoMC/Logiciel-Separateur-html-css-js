import customtkinter as ctk
from tkinter import filedialog, messagebox
import re
import os

# Fonction pour séparer les sections HTML, CSS et JS
def split_html_css_js(content):
    css = ''.join(re.findall(r'<style.*?>(.*?)</style>', content, re.DOTALL))
    js = ''.join(re.findall(r'<script.*?>(.*?)</script>', content, re.DOTALL))
    html = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
    html = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)
    
    return html, css, js

# Fonction pour sauvegarder les fichiers
def save_files(html, css, js, save_path):
    with open(os.path.join(save_path, "index.html"), 'w', encoding='utf-8') as html_file:
        html_file.write(html)
    
    with open(os.path.join(save_path, "style.css"), 'w', encoding='utf-8') as css_file:
        css_file.write(css)
    
    with open(os.path.join(save_path, "script.js"), 'w', encoding='utf-8') as js_file:
        js_file.write(js)
    
    messagebox.showinfo("Succès", "Les fichiers ont été générés avec succès!")

# Fonction appelée lors de l'importation d'un fichier
def import_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        html, css, js = split_html_css_js(content)
        
        save_path = filedialog.askdirectory()
        if save_path:
            save_files(html, css, js, save_path)

# Interface CustomTkinter
app = ctk.CTk()
app.title("Séparateur HTML/CSS/JS")
app.geometry("400x200")

label = ctk.CTkLabel(app, text="Importer un fichier HTML:")
label.pack(pady=20)

import_button = ctk.CTkButton(app, text="Importer", command=import_file)
import_button.pack(pady=10)

app.mainloop()
