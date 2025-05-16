# 🥼🧠Desarrollo de un sistema de monitorización de signos vitales basado en sensores en camas.🛏️💻

## ✔️INTEGRANTES
#### 👩‍💻 Sara Ramirez Alvarez.
#### 👨‍💻 Sebastián Gutiérrez D'Ruggiero.
#### 👩‍💻 Manuela Zapata Caro.

## ✔️INTRODUCCIÓN
#### El monitoreo de signos vitales en tiempo real es una herramienta clave en la atención médica, ya que permite una supervisión continua del estado de salud de los pacientes. Sin embargo, la interpretación de estos datos puede verse afectada por interferencias y ruido en las señales biomédicas, lo que dificulta su precisión y confiabilidad. 
#### Como estudiantes de ingeniería biomédica buscamos optimizar la monitorización de signos vitales mediante una interfaz digital en tiempo real y técnicas de procesamiento de señales. Esto permitirá reducir el ruido, mejorar la precisión de las mediciones y facilitar el análisis clínico, ofreciendo herramientas más eficaces para el diagnóstico y seguimiento de pacientes.

## ✔️FUNCIONAMIENTO
### 🖥️ Pruebas de escritorio (Simulación y Validación Inicial)
#### Generación de datos simulados: Se crean valores de signos vitales dentro y fuera de los rangos normales.🫀
#### Procesamiento de señales: Se aplican filtros básicos para simular la reducción de ruido en los datos.💡
#### Análisis de signos vitales: Se comparan con umbrales y se generan alertas si es necesario. Solo se almacenan lecturas dentro de los rangos permitidos de un sensor. 📊
#### Registro en log: Se guarda un historial de los datos procesados y alertas generadas en un archivo .log. 📝
#### Interfaz simple en consola: El usuario  interactúa con un menú que le permite selecionar el tiempo de monitoreo. 👥
#### Visualización en tiempo real: Se genera una gráfica con matplotlib que muestra la evolución de los signos vitales válidos.📉

### 🏥 Pasos para ejecutar la solución en un entorno real 
#### 👩‍⚕️👨‍💻 Instruciones para los profesionales de la salud e ingenieros biomédicos:
#### 1️⃣ Encender el sistema de monitoreo.
#### 2️⃣ Seleccionar una opción del menú en consola.
#### 3️⃣ Ingresar el número en segundos que desea ejecutar en el monitoreo. Si se ingresa una letra o carácter inválido, el sistema mostrará un mensaje de error y volverá a pedir el valor.
#### 4️⃣ Observar en pantalla la evolución de los signos vitales válidos. Se mostrará una gráfica en tiempo real.
#### 5️⃣ Revisar el archivo registro_UCI.log para analizar datos históricos y detectar problemas.
#### 6️⃣ Analizar el archivo usando las herramientas del sistema para:

#### - Filtrar lecturas específicas.
#### - Calcular promedios o estadísticas por grupo.
#### -Ordenar, limpiar y transformar datos según necesidad clínica.

#### 7️⃣ Detener el monitoreo desde el menú o cerrando el programa.

## ✔️DEFINICIONES CLAVE
### Concepto📋📚
#### Desarrollar un sistema de monitorización de signos vitales basado en sensores en camas.
### Usuarios
#### 👩‍💻 Ingenieros biomédicos. 
#### 👨‍⚕ Profesionales de la salud. 
### Reto⌛🩺
#### ¿Cómo mejorar la monitorización de signos vitales en entornos hospitalarios mediante sensores en camas, minimizando interferencias causadas por los movimientos de los pacientes?
### Funcionalidades🔧⚙
#### Chequeo, registro y análisis de signos vitales.

## ✔️REFERENCIAS BIBLIOGRÁFICAS 🔍
#### 🐈‍⬛ Recmanik M, Martinek R, Nedoma J, Jaros R, Pelc M, Hajovsky R, Velicka J, Pies M, Sevcakova M, Kawala-Sterniuk A. A Review of Patient Bed Sensors for Monitoring of Vital Signs. Sensors (Basel). 2024 Jul 23;24(15). Tomado de: https://pubmed.ncbi.nlm.nih.gov/39123813/
#### 🐈 M. Raurell-Torredà, E. Regaira-Martínez, R. Ferrer-Roca, JD Martí, E. Blazquez-Martínez. (2021). Algoritmo de movilización temprana para el paciente crítico. Recomendaciones de expertos. Enfermería Intensiva. Tomado de https://www.elsevier.es/es-revista-enfermeria-intensiva-142-articulo-algoritmo-movilizacion-temprana-el-paciente-S1130239921000031
#### 🐈‍⬛ Adobe. (s.f.). ¿Qué es un archivo LOG y cómo abrirlo? Adobe Acrobat. Toamdo de: https://www.adobe.com/es/acrobat/resources/document-files/text-files/log-file.html
#### 🐈Hamilton, R. M., Joglar, J. A., Kim, R. J., Lee, R., Marine, J. E., McLeod, C. J., Oken, K. R., Patton, K. K., Pellegrini, C. N., Selzman, K. A., Thompson, A., & Varosy, P. D. (2019). guideline on the evaluation and management of patients with bradycardia and cardiac conduction delay: A report of the American College of Cardiology/American Heart Association Task Force on Clinical Practice Guidelines and the Heart Rhythm Society. Journal of the American College of Cardiology, 74(7). Tomado de: https://doi.org/10.1016/j.jacc.2018.10.044
#### 🐈‍⬛ Smith, S. C. Jr., Spencer, C. C., Stafford, R. S., Taler, S. J., Thomas, R. J., Williams, K. A. Sr., Williamson, J. D., & Wright, J. T. Jr. (2018).guideline for the prevention, detection, evaluation, and management of high blood pressure in adults: A report of the American College of Cardiology/American Heart Association Task Force on Clinical Practice Guidelines. Journal of the American College of Cardiology, 71(19). Tomado de: https://doi.org/10.1016/j.jacc.2017.11.006
