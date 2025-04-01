# Librerías
import time
import random

# Constantes
UMBRAL_MOVIMIENTO = 0.5
FRECUENCIA_CARDIACA_MINIMA = 60
FRECUENCIA_CARDIACA_MAXIMA = 100


# Diccionario para almacenar los datos del paciente
def inicializar_paciente():
    return {"ritmo_actual": None, "movimiento_actual": None, "alertas": []}


# Generación de datos aleatorios
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
    if paciente["movimiento_actual"] is None or paciente["ritmo_actual"] is None:
        return
    if not validar_movimiento(paciente["movimiento_actual"]):
        paciente["alertas"].append("Afectado por movimiento - Lectura invalidada")
        return
    if paciente["ritmo_actual"] < FRECUENCIA_CARDIACA_MINIMA:
        paciente["alertas"].append(
            f"Bradicardia crítica: {paciente['ritmo_actual']:.1f} bpm"
        )
    elif paciente["ritmo_actual"] > FRECUENCIA_CARDIACA_MAXIMA:
        paciente["alertas"].append(
            f"Taquicardia alarmante: {paciente['ritmo_actual']:.1f} bpm"
        )


# Inicializa el archivo de registro .log para almacenar las lecturas
def iniciar_registro():
    try:
        with open("registro_UCI.log", "w", encoding="utf-8") as registro:
            registro.write("Registro de Monitoreo UCI/UCE - Protocolo NCC MERP\n")
    except Exception as e:
        print(f"Error en simulación: {str(e)}")


# Registro de datos en un archivo .log
def registro_lectura(paciente):
    try:
        # Se tiene en cuenta la hora y fecha para el ciclo
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        with open("registro_UCI.log", "a", encoding="utf-8") as registro:
            status = "VALIDA"
            if validar_movimiento(paciente["movimiento_actual"]):
                status = "VALIDA"
            else:
                status = "NO VALIDA"
            registro.write(f"\n{timestamp} | Estado: {status}")
            registro.write(f" | Movimiento: {paciente['movimiento_actual']:.2f} G")
            if status == "VALIDA":
                registro.write(
                    f" | Frecuencia cardiaca: {paciente['ritmo_actual']:.1f} bpm"
                )
                print(
                    f"[LECTURA] Frecuencia cardíaca: {paciente['ritmo_actual']:.1f} bpm"
                )
            if paciente["alertas"]:
                registro.write(f" | ALERTAS: {', '.join(paciente['alertas'])}")
                for alerta in paciente["alertas"]:
                    print(f"[CRITICO] {alerta}")
                paciente["alertas"].clear()
    except Exception as e:
        print(f"Error en simulación: {str(e)}")


# Inicia y ejecuta un monitoreo durante 60 segundos
def main():
    paciente = inicializar_paciente()
    inicio = time.time()
    print("Sistems de monitoreo para UCI/UCE")
    print("Iniciando monitoreo durante 60 segundos")
    try:
        iniciar_registro()
        while (time.time() - inicio) < 60:
            movimiento, ritmo = simular_lecturas()
            paciente["movimiento_actual"] = movimiento
            paciente["ritmo_actual"] = ritmo
            analizar_ritmo(paciente)
            registro_lectura(paciente)
            time.sleep(1)
        print("Monitoreo finalizado")
    except KeyboardInterrupt:
        print("Interrupcion de emergencia")


# Con esto hacemos que el codigo inicie por la funcion main()
if __name__ == "__main__":
    main()
