#spele akmens skeres aparats
import tkinter as tk

#Definejam logu 
window = tk.Tk()

#japievieno elementi
#informacija
lbl_info = tk.Labal(text = "Sveicinats/a!\nSi ir spele akmens,shkeres,papirits!")
#kas jadara 
lbl_darit = tk.label(text = "Izvelies kadu no zemak piedavatajiem variantiem:")
#ko katrs ir izvelejies
lbl_lietizv = tk.labal()
lbl_datoraisv = tk.Labal()
#rezultats
lbl_rezultats = tk.labal()

#Izveles pogas
btn_akmens = tk.Button(text = "akmens")
btn_skeres = tk.Button(text = "skeres")
btn_papirs = tk.Button(text = "papirs")

#Pogu interaktivitate - .bind()
btn_akments.bind("")
btn_skeres.bind
btn_papirs.bind