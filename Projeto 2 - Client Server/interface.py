import tkinter as tk
from tkinter.filedialog import askopenfilename

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        self.selectbutton = tk.Button(self, text="Selecionar imagem", fg="black",
                              command=self.selectimage)

        self.selectbutton.pack(side="top")              

        self.sendbutton = tk.Button(self, text="Enviar imagem", fg="black",
                              command=self.sendimage)
        self.sendbutton.pack(side="top")

        self.quit = tk.Button(self, text="Fechar janela", fg="black",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def selectimage(self):
        self.filename = askopenfilename() 
        print("Imagem selecionada")   
        
    def sendimage(self):
        root.destroy()
        print("Mensagem enviada")
 

root = tk.Tk()
app = Application(master=root)
app.mainloop()