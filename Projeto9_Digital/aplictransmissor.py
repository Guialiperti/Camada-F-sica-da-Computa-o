import tkinter as tk
from tkinter.filedialog import askopenfilename
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
         
        self.selectbutton = tk.Entry(self, fg="black")

        self.selectbutton.pack(side="top")              

        self.sendbutton = tk.Button(self, text="Enviar texto", fg="black",
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

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
    main(app.filename)