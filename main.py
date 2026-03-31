from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class habilidade:

    def __init__(self, master, nome, ganho, tempoEspera):
        """
        tempoEspera: tempo em décimos de segundo para a duração da barra da habilidade
        """

        self.nome = nome
        self.master = master
        self.ganho = ganho
        self.tempoEspera = tempoEspera

        self.frameHabilidade = ttk.Frame(master, padding = 15, width= 100)
        self.frameHabilidade.pack()
        
        self.barra = ttk.Progressbar(self.frameHabilidade, orient= "horizontal", length= 300, mode = "determinate", maximum= tempoEspera)
        self.barra.pack(side='right')

        self.botao = Button(self.frameHabilidade, text= self.nome, command= self.iniciar_progresso, width= "15", font= ("Arial", 12))
        self.botao.pack(padx= 5, side='left')
    
    def iniciar_progresso(self):
        self.barra["value"] = 0
        self.incrementar()

    def incrementar(self):
        if self.barra["value"] < self.barra["maximum"]:
            self.barra["value"] += 1
            self.master.after(50, self.incrementar)
        else:
            self.barra["value"] = 0
            self.comando_final()

    def comando_final(self):
        global aura
        aura.set(aura.get() + self.ganho)



root = Tk()
root.title("simulador de farmar aura")
root.geometry("500x500")

aura = IntVar(root, value = 0)

# Header
frame1 = ttk.Frame(root,width=500, height=100, relief="solid")
frame1.pack(pady=20, padx=20, fill="both", expand=False)

contadorAura = ttk.Label(frame1, text="0", font=("Comic Sans MS", 20))
contadorAura.place(relx=1.0, rely=0, anchor='ne')

def AtualizarLabelAura(name, index, mode):
    global aura
    contadorAura["text"] = aura.get()

aura.trace_add("write", AtualizarLabelAura)

# frame das habilidades
frame2 = ttk.Frame(root, padding = 20, relief="solid", width=500)
frame2.pack()

habilidade1 = habilidade(master= frame2, nome="moggar 1 beta", ganho= 1, tempoEspera= 30)
habilidade2 = habilidade(master= frame2, nome= "tocar phonk \nem publico", ganho= 3, tempoEspera= 50)

root.mainloop()