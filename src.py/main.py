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
        paciente["alertas"].append(
            "Afectado por movimiento - Lectura invalidada"
            )
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


# Función principal que ejecuta el monitoreo
def menu():
    print("\n" + "=" * 50)
    print("\t🩺 Sistema de Monitoreo para UCI/UCE")
    print("\t   📋 Protocolo NCC MERP")
    print("=" * 50)
    print("[1] ▶️ Iniciar monitoreo")
    print("[2] ⏳ Seleccionar tiempo de monitoreo manualmente")
    print("[3] ❌ Salir")
    print("=" * 50)
    return input("🔹 Seleccione una opción: ")


# Interacción con el usuario a patir de un menú
def main():
    ejecutando = True
    while ejecutando:
        paciente = inicializar_paciente()
        numero_registros = 60
        print("\n" + "=" * 50)
        print("\t🚀 Iniciando Sistema de Monitoreo...\n")
        print("=" * 50)
        try:
            seleccion = menu()

            if seleccion == '1':
                print(
                    "\n✅ Monitoreo iniciado con configuración por defecto (60 segundos) ✅\n"
                    )

            elif seleccion == '2':
                try:
                    numero_registros = int(input(
                        "⏱️ Ingrese el tiempo de monitoreo en segundos: "
                        ))
                except ValueError:
                    print(
                        "\n⚠️ Entrada inválida. Usando 60 lecturas por defecto. ⚠️\n"
                        )  # Se hace una lectura cada segundo
                if numero_registros <= 0:
                    print(
                        "\n⚠️ Tiempo inválido. Usando 60 lecturas por defecto. ⚠️\n"
                        )
                    numero_registros = 60
                else:
                    print(
                        f"\n⏳ Monitoreo configurado para {numero_registros} segundos. ⏳\n"
                        )

            elif seleccion == '3':
                print("\n👋 Saliendo del sistema... 👋\n")
                ejecutando = False
                break
            else:
                print(
                    "\n⚠️ Opción inválida. Inicializando monitoreo por defecto. ⚠️\n"
                    )
            iniciar_registro()
            print("\n🟢 Iniciando monitoreo... 🟢\n")

            for i in range(numero_registros):
                movimiento, ritmo = simular_lecturas()
                paciente['movimiento_actual'] = movimiento
                paciente['ritmo_actual'] = ritmo
                analizar_ritmo(paciente)
                registro_lectura(paciente)
                # Espera un segundo antes de la siguiente medición
                time.sleep(1)
            print(
                "\n✅ Monitoreo completado: Datos listos para revisión médica ✅\n"
                )
        except KeyboardInterrupt:
            print("\n🛑 Interrupción de emergencia activada 🛑\n")


# Con esto hacemos que el codigo inicie por la función main()
if __name__ == "__main__":
    main()
