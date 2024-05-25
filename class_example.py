#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:30:39 2024

@author: user
"""
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  @classmethod
  def desde_nombre_y_edad(cls, nombre, edad):
    return cls(nombre, edad)

  @classmethod
  def edad_promedio(cls, lista_de_personas):
    edades = [persona.edad for persona in lista_de_personas]
    promedio = sum(edades) / len(edades)
    return promedio

# Ejemplo de uso general 
persona1 = Persona("Juan", 30)
persona2 = Persona("Maria", 25)

# Ejemplo de uso especifico
persona2 = Persona.desde_nombre_y_edad("Maria", 25)

lista_de_personas = [persona1, persona2]

edad_promedio = Persona.edad_promedio(lista_de_personas)
print(f"La edad promedio es: {edad_promedio:.2f}")

