import streamlit as st
import queue
import random
import time

st.title("🚗 Evento de Exhibición de Carros")

class Carro:
    contador = 1

    def __init__(self):
        self.id = Carro.contador
        Carro.contador += 1

        marcas = ["Mustang", "Camaro", "Corvette",
                  "Nissan GTR", "Supra", "Ferrari"]

        colores = ["Rojo", "Azul", "Negro",
                   "Blanco", "Amarillo"]

        self.marca = random.choice(marcas)
        self.color = random.choice(colores)

    def __str__(self):
        return f"Carro {self.id}: {self.marca} {self.color}"

if st.button("Iniciar Evento"):

    cola = queue.Queue()
    registrados = []

    estado = st.empty()

    # Llegan carros
    for i in range(10):
        carro = Carro()
        cola.put(carro)

    # Registro de carros
    while not cola.empty():

        carro = cola.get()

        estado.write(f"📝 Registrando {carro}")
        time.sleep(1)

        registrados.append(carro)

        estado.write(f"✅ Registrado {carro}")
        time.sleep(1)

    st.success("Evento finalizado")

    st.subheader("Autos registrados")

    for carro in registrados:
        st.write(carro)