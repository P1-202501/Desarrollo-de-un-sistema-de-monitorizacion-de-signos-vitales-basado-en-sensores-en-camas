import time
import random

UMBRAL_MOVIMIENTO = 0.5
FRECUENCIA_CARDIACA_MINIMA = 60
FRECUENCIA_CARDIACA_MAXIMA = 100

def inicializar_paciente():
    pass
def simular_lecturas():
    pass

 # Verifica si el movimiento está dentro del umbral permitido

def validar_movimiento(movimiento):
    return movimiento <= UMBRAL_MOVIMIENTO
 
# Analiza la frecuencia cardíaca y detecta anomalías

def analizar_ritmo(paciente):
    if paciente['movimiento_actual'] is None or paciente['ritmo_actual'] is None:
        return
   
    if not validar_movimiento(paciente['movimiento_actual']):
        paciente['alertas'].append("Afectado por movimiento - Lectura invalidada")
        return
   
    if paciente['ritmo_actual'] < FRECUENCIA_CARDIACA_MINIMA:
        paciente['alertas'].append(f"Bradicardia crítica: {paciente['ritmo_actual']:.1f} bpm")
    elif paciente['ritmo_actual'] > FRECUENCIA_CARDIACA_MAXIMA:
        paciente['alertas'].append(f"Taquicardia alarmante: {paciente['ritmo_actual']:.1f} bpm")


def registro_lectura():
    pass
def main():
    pass

