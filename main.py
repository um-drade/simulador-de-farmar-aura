from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class habilidade:

    def __init__(self, master, nome):
        self.nome = nome
        self.master = master

        self.frameHabilidade = ttk.Frame(master, padding = 15, width= 100)
        self.frameHabilidade.pack()
        
        self.barra = ttk.Progressbar(self.frameHabilidade, orient= "horizontal", length= 300, mode = "determinate", maximum=30)
        self.barra.pack(side='right')

        self.botao = Button(self.frameHabilidade, text= self.nome, command= self.iniciar_progresso, width= "15", font= ("Arial", 12))
        self.botao.pack(padx= 5, side='left')
    
    def iniciar_progresso(self):
        self.barra["value"] = 0
        self.incrementar()

    def incrementar(self):
        if self.barra["value"] < self.barra["maximum"]:
            self.barra["value"] += 1
            # Usamos o self.master (que é o root) para chamar o after
            self.master.after(50, self.incrementar)
        else:
            self.barra["value"] = 0
            self.comando_final()

    def comando_final(self):
        messagebox.showinfo("Fim", "O comando foi executado com sucesso!")

root = Tk()
root.title("simulador de farmar aura")
root.geometry("500x500")

aura = IntVar(root, value = 0)

# Header
frame1 = ttk.Frame(root,width=500, height=100, relief="solid")
frame1.pack(pady=20, padx=20, fill="both", expand=False)

contadorAura = ttk.Label(frame1, text="0", font=("Comic Sans MS", 20))
contadorAura.place(relx=1.0, rely=0, anchor='ne')

# frame das habilidades
frame2 = ttk.Frame(root, padding = 20, relief="solid", width=500)
frame2.pack()

habilidade1 = habilidade(frame2, "tocar phonk \nem publico")
habilidade2 = habilidade(frame2, "moggar 1 beta")

root.mainloop()