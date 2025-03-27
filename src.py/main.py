import time
import random

UMBRAL_MOVIMIENTO = 0.5
RITMO_MINIMO = 60
RITMO_MAXIMO = 100

def inicializar_paciente():
    pass
def simular_lecturas():
    pass
def validar_movimiento():
    pass
def analizar_ritmo():
    pass
def iniciar_registro():
    pass
def registro_lectura():
    pass
def main():  
    paciente = inicializar_paciente() 
    inicio = time.time()
    
    print('Sistems de monitoreo para UCI/UCE')
    print('Iniciando monitoreo durante 60 segundos')
   
    try:
        iniciar_registro()
        while (time.time() - inicio) < 60: 
            movimiento, ritmo = simular_lecturas()
            paciente['movimiento_actual'] = movimiento 
            paciente['ritmo_actual'] = ritmo 
            
            analizar_ritmo(paciente)
            registro_lectura(paciente)
            time.sleep(1) 
        
        print('Monitoreo finalizado')
        
    except KeyboardInterrupt:
        print('Interrupcion de emergencia')
        

if __name__ == 'main': #con esto hacemos que el cdigo inicie por la funcion main()
    main
