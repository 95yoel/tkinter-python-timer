import tkinter as tk
import time

class ContadorTiempo:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Tiempo")
        self.root.geometry("300x150")  # Cambia las dimensiones de la ventana

        # Cambiar el fondo de la ventana principal a negro
        self.root.configure(bg="black")

        self.tiempo_restante = 0
        self.iniciado = False
        self.tiempo_inicial = None  # Almacena el tiempo inicial cuando se inicia

        self.etiqueta_tiempo = tk.Label(root, text="00:00.000", font=("Helvetica", 24), bg="black", fg="white")
        self.etiqueta_tiempo.pack(pady=10)

        self.frame_botones = tk.Frame(root, bg="black")  # Fondo negro alrededor de los botones
        self.frame_botones.pack()

        self.boton_iniciar = tk.Button(self.frame_botones, text="Iniciar", command=self.toggle_contador, bg="gray", fg="white", highlightbackground="white")
        self.boton_reiniciar = tk.Button(self.frame_botones, text="Reiniciar", command=self.reiniciar_contador, bg="gray", fg="white", highlightbackground="white")

        self.boton_iniciar.pack(side="left", padx=5, pady=10)
        self.boton_reiniciar.pack(side="left", padx=5, pady=10)

        # Agregar un enlace de tecla de espacio
        self.root.bind("<space>", self.toggle_contador)

    def toggle_contador(self, event=None):
        if not self.iniciado:
            if self.tiempo_inicial is None:
                self.tiempo_inicial = time.time()
            else:
                self.tiempo_inicial += time.time() - self.tiempo_detenido
            self.iniciado = True
            self.actualizar_tiempo()
            self.boton_iniciar.config(text="Detener")
        else:
            self.iniciado = False
            self.tiempo_detenido = time.time()
            self.boton_iniciar.config(text="Continuar")

    def reiniciar_contador(self):
        self.iniciado = False
        self.tiempo_inicial = None
        self.tiempo_restante = 0
        self.etiqueta_tiempo.config(text="00:00.000")
        self.boton_iniciar.config(text="Iniciar")

    def actualizar_tiempo(self):
        if self.iniciado:
            tiempo_transcurrido = time.time() - self.tiempo_inicial + self.tiempo_restante
            minutos, segundos = divmod(int(tiempo_transcurrido), 60)
            milisegundos = int((tiempo_transcurrido % 1) * 1000)
            self.etiqueta_tiempo.config(text=f"{minutos:02}:{segundos:02}.{milisegundos:03}")
            self.root.after(1, self.actualizar_tiempo)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorTiempo(root)
    root.mainloop()
