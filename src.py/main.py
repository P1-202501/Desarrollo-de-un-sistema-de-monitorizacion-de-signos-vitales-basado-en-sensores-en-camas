import time
import random

UMBRAL_MOVIMIENTO = 0.5
FRECUENCIA_CARDIACA_MINIMA = 60
FRECUENCIA_CARDIACA_MAXIMA = 100

def inicializar_paciente():
    return {
        'ritmo_actual': None,
        'movimiento_actual': None,
        'alerta': []
    }


def simular_lecturas():
    try:
        movimiento = random.uniform(0, 1)
        frecuencia_cardiaca_base = 70 + random.uniform(-15, 35)
        return movimiento, max(40, min(140, frecuencia_cardiaca_base))
    
    except Exception as e:
        print(f"Error en simulación: {str(e)}")
        return None, None
        

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

