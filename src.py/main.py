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
# def registro_lectura(): 
    # try:
    #     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # se tiene en cuenta la hora y fecha para el ciclo

    #     with open('registro_UCI.log', 'a', encoding='utf-8') as registro: 
    #         status = "VALIDA" 
    #         if validar_movimiento(paciente['movimiento_actual']):
    #             status = "VALIDA" 
    #         else:
    #             status ="NO VALIDA"
        
    #         registro.write(f"\n{timestamp} | Estado: {status}")
    #         registro.write(f" | Movimiento: {paciente['movimiento_actual']:.2f} G")  
        
    #         if status == "VALIDA":
    #             registro.write(f" | Frecuencia cardiaca: {paciente['ritmo_actual']:.1f} bpm")
    #             print(f"[LECTURA] Frecuencia cardíaca: {paciente['ritmo_actual']:.1f} bpm")
        
    #         if paciente['alertas']:
    #             registro.write(f" | ALERTAS: {', '.join(paciente['alertas'])}")
    #             for alerta in paciente['alertas']:
    #                 print(f"[CRITICO] {alerta}")
    #             paciente['alertas'].clear()
                
    # except Exception as e:
    #     print(f"Error en simulación: {str(e)}")  
    
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
            # registro_lectura(paciente)
            time.sleep(1) 
        
        print('Monitoreo finalizado')
        
    except KeyboardInterrupt:
        print('Interrupcion de emergencia')
        

if __name__ == 'main': #con esto hacemos que el codigo inicie por la funcion main()
    main()
