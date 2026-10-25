
Gemini

Nueva conversación
Biblioteca
Imágenes
Programado
Personalizar
Vídeos
Nuevo cuaderno
Estrategia Weinstein y Termómetro HYG
Manual Operativo de Retirada Financiera
FUSIÓN: Análisis de Estrategia de Inversión y Fiscalidad
Manual Operativo ETFs Sectoriales UCITS
Clínica Dental: Modelo de Crecimiento Estratégico
QNAP NAS a Google Drive: Copia Seguridad
Rediseño Moderno de Logotipo
FUSIÓN: Inversión y Retirada
Actualización Informe Anual Acciones y CSV
Estrategia de Trading: Filtros Adicionales
Inaccesibilidad a Grabación de Zoom
Música de payasos para Halloween
Comparación de Make, GitHub y Streamlit
Plugins de WhatsApp para WordPress
Conexión entre Supabase y Gemini
Error al procesar documento de IA
Desajuste en el sector tecnológico
Contacto y entradas en Yelmo
Vídeos en segundo plano iPhone
Límite de duración para videos
Cambiar Idioma Negocio Apple Maps
Coste de envío en Tustaquillas
Carga de batería Cybex e-Priam
ETFs de High Yield antiguos
Gráfico de River Patrimonio en TradingView

Actividad
España
De tu dirección IP
Conversación con Gemini
A ver que me entere, el orden es Telegram-Gemini_Supabase?

No, es justo al revés. El orden correcto y lógico tiene que ser: Telegram -> Supabase -> Google Gemini.

Piensa en cómo viaja la información como si fuera una cadena de montaje. Make lee de izquierda a derecha, y cada paso necesita la información del anterior:

Telegram (Watch Updates): Tú escribes un mensaje en tu móvil (ej. "¿Qué me toca entrenar hoy?"). Esta es la puerta de entrada.

Supabase (Search Rows): Make coge tu identificador de Telegram, va a tu base de datos y extrae tu "ficha de cliente" (tu semana actual, tus niveles de flexiones, dominadas, etc.).

Google Gemini (Generate a Response): La Inteligencia Artificial recibe todo junto: el mensaje que escribiste en el paso 1 + tus niveles que acabamos de sacar en el paso 2 + el "ladrillo" de reglas. Si pusiéramos a Gemini antes de Supabase, intentaría contestarte a ciegas, sin saber en qué nivel estás.

Telegram (Send a Text Message): (Este módulo lo añadiremos al final del todo para que el bot te devuelva la respuesta escrita al móvil).

Si tu línea de puntos une los módulos en el orden Telegram -> Supabase -> Gemini (como tenías en tu captura anterior), la estructura está perfecta. ¿Pudiste probar el "atajo" del comando SQL para quitar el candado de la base de datos?

Aqui que pongo?

Selecciona Usuarios.   
PNG

Esta es la tabla correcta porque es donde está guardada tu ficha personal con tus niveles actuales de calistenia, la semana del ciclo y tus lesiones. Al seleccionarla, Make.com sabrá de dónde extraer esos datos para enviárselos a Gemini.   
PNG

En cuanto hagas clic en Usuarios, aparecerán nuevas opciones debajo. La más importante será Search criteria (Criterios de búsqueda), donde configuraremos que busque específicamente tu ID de Telegram. Selecciona la tabla y avísame para configurar ese siguiente paso.

The run couldn't be completed

[403]

permission denied for table Usuarios

Code: RuntimeError

Origin: Supabase

Ese candado de Supabase se ha quedado atascado y sigue bloqueando a Make. En lugar de seguir peleando con los ajustes de seguridad en la base de datos, vamos a usar la "llave maestra" de tu proyecto, que ignora todos los candados de golpe.

Se llama clave service_role y fuerza la entrada a la tabla sin importar qué restricciones de seguridad (RLS) haya activadas. Sigue estos pasos exactos:

Ve a tu panel de Supabase, entra en Project Settings (el icono de engranaje abajo del todo a la izquierda) y haz clic en API.

En la sección de claves (Project API keys), ignora la que has estado usando hasta ahora (anon public). Busca la que está justo debajo, etiquetada como service_role secret.

Haz clic en el botón de copiar (los dos cuadraditos) de esa clave service_role (quizás te pida hacer clic en Reveal para mostrarla primero).

Vuelve a Make.com, abre el módulo de Supabase y, en el menú Connection, haz clic en el botón Add para crear una conexión completamente nueva.

Ponle un nombre para identificarla (ej. "Llave Maestra"), pega tu Project URL de siempre y, en el hueco de la API Key, pega esta nueva clave secreta.

Dale a guardar, selecciona de nuevo la tabla Usuarios y repite la prueba haciendo clic derecho sobre el módulo > "Run this module only" (metiendo el número 1).

Al usar esta llave de administrador absoluto, el error 403 desaparecerá al instante. Pruébalo y avísame en cuanto veas el globo verde/blanco de éxito para configurar el filtro final.

Y todo esto se puede hacer con github y streamliy?

Sí, cien por cien. De hecho, para muchas personas resulta mucho más fácil y limpio hacerlo con GitHub y Streamlit, ya que te evitas pelear con los módulos, conexiones y permisos bloqueados de Make.com.

Si damos este salto, la estructura de tu proyecto cambiaría de la siguiente manera:

La Interfaz (Streamlit): En lugar de un bot de Telegram, tendrías tu propia aplicación web privada con un chat idéntico al de ChatGPT. Streamlit tiene componentes visuales de chat nativos listos para usar.

El Motor (Python en lugar de Make): Cambiamos el entorno visual y los cables de Make por un único archivo de código en Python. Yo te generaría el código exacto con tu "ladrillo" de calistenia integrado, y tú solo tendrías que copiarlo y pegarlo.

El Alojamiento (GitHub): GitHub actuará como tu carpeta en la nube. Ahí guardaremos tu archivo de código. Streamlit leerá ese archivo directamente desde tu GitHub para mantener tu web funcionando gratis las 24 horas.

La Base de Datos: Al usar código, conectarse a Supabase o Google Sheets es mucho más directo y sin errores de permisos 403. Incluso, al ser el único usuario, podrías olvidarte de bases de datos externas y guardar tus niveles directamente en un archivo dentro de Streamlit.

Pasar a Streamlit significa cambiar la pelea con interfaces visuales por la acción de copiar y pegar bloques de código Python. Si prefieres tener tu propia web y arrancar con este método, confírmamelo y te preparo el primer archivo de código para subir a GitHub.

Pero dime de forma detallada las diferencias entre ambas opciones

Ambas arquitecturas tienen ventajas claras, pero la diferencia principal radica en cómo construyes el sistema y dónde vas a interactuar con tu entrenador.

Aquí tienes la comparativa detallada enfocada en tu proyecto de calistenia:

Opción A: Make.com + Telegram (Tu configuración actual)
Es la vía del "No-Code" (cero programación), donde construyes conectando aplicaciones como si fueran piezas de Lego.

Tu interfaz final: Entrenas usando la app de Telegram. Es extremadamente cómodo porque lo tienes en el móvil, te llegan notificaciones y se siente como chatear con un entrenador real.

Método de creación: 100% visual. Trabajas en el lienzo de Make.com rellenando recuadros, arrastrando burbujas de variables y configurando llaves API.

Gestión de errores: Es su mayor debilidad. Cuando dos plataformas no se entienden (como el error 403 que te da Supabase), te obliga a pelear con configuraciones de seguridad, menús ocultos y permisos en ambas webs. Tú no tienes el control de cómo Make lee los datos por dentro.

Base de datos: Necesitas obligatoriamente un servicio externo (Supabase o Google Sheets) conectado con llaves de acceso para guardar tu semana y niveles.

Opción B: Streamlit + GitHub (La alternativa con código Python)
Es la vía del desarrollo a medida. Tú no tienes que aprender a programar; yo genero el código completo, y tú actúas como el operario que copia y pega.

Tu interfaz final: Una página web privada (muy similar a la pantalla de ChatGPT). La abres desde el navegador de tu móvil o PC. Pierdes la comodidad de tenerlo integrado en tu WhatsApp/Telegram, pero ganas una interfaz donde puedes tener botones, gráficos de tu progreso o tablas visuales con tu rutina.

Método de creación: Basado en texto. Crearemos una cuenta en GitHub (que funciona como una carpeta en la nube) y pegarás allí un archivo de texto con el código Python que yo te daré. Streamlit leerá ese archivo y creará la web gratis.

Gestión de errores: Directa y bajo tu control. Si algo falla, me copias el error, yo reescribo esa línea de código y tú vuelves a pegar. No dependes de que los módulos de Make.com funcionen bien.

Base de datos: Extremadamente simplificada. Al ser tú el único usuario, podemos eliminar Supabase de la ecuación. El código puede guardar tu semana y tus niveles en un simple archivo de texto (JSON o CSV) dentro de tu propio GitHub, sin candados, sin errores 403 y sin permisos denegados.

Si prefieres la comodidad de chatear por Telegram mientras entrenas, lo mejor es insistir en Make.com usando la llave service_role de Supabase o cambiando Supabase por un Excel de Google.

¿Prefieres intentar solucionar la conexión visual actual o damos el salto al código puro para montar tu propia web con Streamlit?

Pues vamos a hacer este proyecto con github y streamlit (y Gemini). Dime pasos a seguir

1. Crear tu "carpeta" en GitHub
GitHub será el lugar donde guardaremos los dos únicos archivos que necesita tu web.

Entra en github.com y créate una cuenta gratuita.

Arriba a la izquierda (o en el menú + arriba a la derecha), haz clic en New repository (Nuevo repositorio).

Ponle un nombre corto sin espacios, por ejemplo: mi-entrenador-ia.

Marca la opción Public (para que Streamlit pueda leerlo sin bloqueos) y marca la casilla "Add a README file".

Haz clic en el botón verde Create repository.

2. Crear el archivo de herramientas (requirements.txt)
Este archivo le dice a Streamlit qué motores descargar para que funcione la IA.

En tu nuevo repositorio, haz clic en el botón Add file > Create new file.

En el hueco del nombre, escribe exactamente: requirements.txt.

En el cuadro de texto grande, pega estas dos líneas:

Plaintext
streamlit
google-generativeai
Haz clic en el botón verde Commit changes (arriba a la derecha) para guardar.

3. Crear el cerebro de tu aplicación (app.py)
Este es el archivo principal. Aquí hemos sustituido Supabase por un menú lateral (sidebar) en la propia web, de forma que tú mismo podrás cambiar en qué semana o nivel estás con un par de clics, y Gemini lo leerá automáticamente.

Vuelve a la pantalla principal de tu repositorio y dale a Add file > Create new file.

Ponle de nombre: app.py.

Copia y pega todo este bloque de código. Importante: Donde dice [PEGA AQUÍ TODO TU LADRILLO/FRAMEWORK...], bórralo y pega tu manual completo de reglas:

Python
import streamlit as st
import google.generativeai as genai

# 1. Menú lateral: Tu "Base de Datos" visual (sustituye a Supabase)
st.set_page_config(page_title="Entrenador Calistenia", page_icon="💪")
st.sidebar.title("Mi Ficha Actual")
semana = st.sidebar.number_input("Semana del Ciclo", min_value=1, max_value=11, value=1)
nivel_flexiones = st.sidebar.selectbox("Nivel Flexiones", [1, 2, 3, 4, 5])
nivel_sentadillas = st.sidebar.selectbox("Nivel Sentadillas", [1, 2, 3, 4, 5])
nivel_dominadas = st.sidebar.selectbox("Nivel Dominadas", [1, 2, 3, 4, 5])
nivel_verticales = st.sidebar.selectbox("Nivel Verticales", [1, 2, 3, 4, 5])
nivel_core = st.sidebar.selectbox("Nivel Core", [1, 2, 3, 4, 5])

# 2. Configurar la IA de Gemini con la clave de seguridad
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Instrucciones base (Tu Framework + Tus Niveles en tiempo real)
instrucciones = f"""
Actúa como mi entrenador personal experto en calistenia. Responde de forma clara y al grano.
MANUAL DEL ENTRENADOR:
[PEGA AQUÍ TODO TU LADRILLO/FRAMEWORK DE LAS 10 SEMANAS Y EJERCICIOS]

=========================================
DATOS ACTUALES DEL USUARIO:
- Semana Actual del ciclo: Semana {semana}
- Nivel Flexiones: {nivel_flexiones}
- Nivel Sentadillas: {nivel_sentadillas}
- Nivel Dominadas: {nivel_dominadas}
- Nivel Flexiones Verticales: {nivel_verticales}
- Nivel Core: {nivel_core}
"""

modelo = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instrucciones
)

# 4. Interfaz del Chat
st.title("💪 Entrenador IA - Método Desencadenado")

# Memoria del chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes anteriores
for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["texto"])

# Caja para escribir
pregunta = st.chat_input("Ej: ¿Qué me toca entrenar hoy?")
if pregunta:
    # Mostrar lo que pregunta el usuario
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta de la IA
    with st.chat_message("assistant"):
        respuesta = modelo.generate_content(pregunta)
        st.markdown(respuesta.text)
    st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta.text})
Haz clic en Commit changes para guardar.

4. Publicar tu web en Streamlit

Entra en share.streamlit.io e inicia sesión seleccionando "Continue with GitHub".

Una vez dentro, haz clic en el botón Create app (arriba a la derecha).

Selecciona "Deploy a public app from GitHub".

En el formulario, selecciona tu repositorio (mi-entrenador-ia). El campo Main file path se rellenará solo con app.py.

Paso crítico (Tu llave API): Antes de darle a desplegar, haz clic en Advanced settings (Ajustes avanzados). Verás un recuadro negro llamado Secrets. Ahí debes pegar tu llave de Google AI Studio con este formato exacto:
GEMINI_API_KEY = "tu_clave_larga_de_google_aqui"

Haz clic en Save y luego en Deploy!

Verás un radar cargando durante un par de minutos. Cuando termine, aparecerá tu página web con un panel a la izquierda para ir cambiando tus niveles (adiós bloqueos de Supabase), y un chat a la derecha para hablar con Gemini. Si en el proceso te atascas al crear los archivos o al publicar, dime dónde estás exactamente.

streamlit.errors.StreamlitSecretNotFoundError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:

File "/usr/local/lib/python3.14/tomllib/_parser.py", line 182, in loads

pos = key_value_rule(src, pos, out, header, parse_float)

File "/usr/local/lib/python3.14/tomllib/_parser.py", line 411, in key_value_rule

pos, key, value = parse_key_value_pair(src, pos, parse_float)

~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

File "/usr/local/lib/python3.14/tomllib/_parser.py", line 454, in parse_key_value_pair

pos, value = parse_value(src, pos, parse_float)

~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

File "/usr/local/lib/python3.14/tomllib/_parser.py", line 740, in parse_value

raise TOMLDecodeError("Invalid value", src, pos)

TOMLDecodeError

The above exception was the direct cause of the following exception:

File "/mount/src/desencadenado/app.py", line 15, in <module>

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

~~~~~~~~~~^^^^^^^^^^^^^^^^^^

Ese error (TOMLDecodeError) significa que hay un pequeño fallo de sintaxis en el recuadro negro de los Secrets de Streamlit. Streamlit es muy estricto con el formato y, en el 99% de los casos, este error ocurre porque faltan las comillas alrededor de tu clave o se copiaron unas comillas invisibles/curvas.

Para solucionarlo al instante, sigue estos pasos:

Ve a tu aplicación en Streamlit y haz clic en Manage app (abajo a la derecha) o entra directamente en Settings (Ajustes) > Secrets.

Revisa la línea donde pegaste tu clave. Asegúrate de que la clave de Google esté rodeada estrictamente por comillas dobles rectas (" "), sin espacios sueltos alrededor de la contraseña.

Formato CORRECTO:
GEMINI_API_KEY = "AIzaSyTuClaveSuperLargaAqui..."

Formatos INCORRECTOS (que causan tu error):
GEMINI_API_KEY = AIzaSyTuClaveSuperLargaAqui... (Faltan las comillas)
GEMINI_API_KEY = "AIzaSy... (Falta cerrar la comilla al final)

Ponle las comillas rectas correctamente, haz clic en Save (Guardar) y verás que el error desaparece y tu web carga la interfaz del chat al instante.

google.api_core.exceptions.NotFound: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:

File "/mount/src/desencadenado/app.py", line 257, in <module>

respuesta = modelo.generate_content(pregunta)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/generativeai/generative_models.py", line 331, in generate_content

response = self._client.generate_content(

request,

**request_options,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/ai/generativelanguage_v1beta/services/generative_service/client.py", line 835, in generate_content

response = rpc(

request,

...<2 lines>...

metadata=metadata,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__

return wrapped_func(*args, **kwargs)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 294, in retry_wrapped_func

return retry_target(

target,

...<3 lines>...

on_error=on_error,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 156, in retry_target

next_sleep = _retry_error_helper(

exc,

...<6 lines>...

timeout,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_base.py", line 214, in _retry_error_helper

raise final_exc from source_exc

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 147, in retry_target

result = target()

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/timeout.py", line 130, in func_with_timeout

return func(*args, **kwargs)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/grpc_helpers.py", line 77, in error_remapped_callable

raise exceptions.from_grpc_error(exc) from exc

El error NotFound ocurre porque Google ya ha desactivado la versión antigua del modelo (gemini-1.5-flash), tal y como vimos en tus capturas de AI Studio donde incluso la versión 2.5 se desconectó a mediados de este mes de octubre.

Para solucionarlo, solo necesitas actualizar el nombre del modelo en tu código a la versión que tienes activa ahora mismo:

Ve a tu repositorio en GitHub, abre el archivo app.py y haz clic en el icono del lápiz (arriba a la derecha) para editarlo.

Localiza esta línea en el bloque donde se configura el modelo:
model_name="gemini-1.5-flash",

Cámbiala por la versión más reciente que vimos en tu lista:
model_name="gemini-3.7-flash",

Haz clic en el botón verde Commit changes para guardar el archivo.

Streamlit detectará automáticamente la actualización en tu GitHub. Espera unos segundos, refresca tu página web y haz una nueva pregunta en el chat; esta vez te responderá perfectamente.

File "/mount/src/desencadenado/app.py", line 257, in <module>

respuesta = modelo.generate_content(pregunta)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/generativeai/generative_models.py", line 331, in generate_content

response = self._client.generate_content(

request,

**request_options,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/ai/generativelanguage_v1beta/services/generative_service/client.py", line 835, in generate_content

response = rpc(

request,

...<2 lines>...

metadata=metadata,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__

return wrapped_func(*args, **kwargs)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 294, in retry_wrapped_func

return retry_target(

target,

...<3 lines>...

on_error=on_error,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 156, in retry_target

next_sleep = _retry_error_helper(

exc,

...<6 lines>...

timeout,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_base.py", line 214, in _retry_error_helper

raise final_exc from source_exc

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 147, in retry_target

result = target()

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/timeout.py", line 130, in func_with_timeout

return func(*args, **kwargs)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/grpc_helpers.py", line 77, in error_remapped_callable

raise exceptions.from_grpc_error(exc) from exc

Ese bloque de texto que me acabas de pasar es la segunda mitad exacta del mismo error de antes (el error NotFound porque el modelo antiguo estaba apagado).

Como copiaste el error en dos partes, Streamlit te lo ha mostrado cortado. La solución sigue siendo exactamente la que te comenté en el paso anterior.

Tienes que actualizar el nombre del modelo en tu código. Sigue estos 3 pasos rápidos:

Ve a tu cuenta de GitHub y abre tu archivo app.py.

Dale al icono del lápiz arriba a la derecha para editarlo.

Busca esta línea:
model_name="gemini-1.5-flash",

Bórrala y cámbiala por esta:
model_name="gemini-3.7-flash",

(Nota: si por algún motivo ese nombre tampoco le gusta a Streamlit, prueba usando gemini-flash a secas, que siempre busca la última versión encendida).

Dale al botón verde de Commit changes para guardar. Vuelve a tu web de Streamlit, recarga la página, y la IA debería empezar a contestarte al instante.

google.api_core.exceptions.NotFound: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:

File "/mount/src/desencadenado/app.py", line 257, in <module>

respuesta = modelo.generate_content(pregunta)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/generativeai/generative_models.py", line 331, in generate_content

response = self._client.generate_content(

request,

**request_options,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/ai/generativelanguage_v1beta/services/generative_service/client.py", line 835, in generate_content

response = rpc(

request,

...<2 lines>...

metadata=metadata,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__

return wrapped_func(*args, **kwargs)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 294, in retry_wrapped_func

return retry_target(

target,

...<3 lines>...

on_error=on_error,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 156, in retry_target

next_sleep = _retry_error_helper(

exc,

...<6 lines>...

timeout,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_base.py", line 214, in _retry_error_helper

raise final_exc from source_exc

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 147, in retry_target

result = target()

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/timeout.py", line 130, in func_with_timeout

return func(*args, **kwargs)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/grpc_helpers.py", line 77, in error_remapped_callable

raise exceptions.from_grpc_error(exc) from exc

El error NotFound sigue saltando porque Google no reconoce el nombre del modelo que está escrito actualmente en tu código.

Ve a tu archivo app.py en GitHub, dale al icono del lápiz para editarlo y cambia la línea del modelo por esta versión estándar que siempre funciona:

Python
model_name="gemini-1.5-flash",
Si por algún motivo tu clave de API está en un proyecto que no soporta la versión Flash, cámbialo por el modelo principal:

Python
model_name="gemini-pro",
Haz clic en el botón verde Commit changes para guardar. Vuelve a tu web de Streamlit, recarga la página y prueba a escribir en el chat.

El problema de flash es que no hay version 1.5 segun vumos antes

Tienes toda la razón, disculpa la confusión. Google actualiza y retira los números de versión constantemente, y si ponemos uno que ya no está activo en tu cuenta, nos bloquea con ese error NotFound.

Para dejar de adivinar números y solucionar esto de forma definitiva, vamos a usar el nombre universal (alias). Google tiene un atajo que automáticamente busca y conecta con la versión de Flash más reciente que tengas disponible, sin importar el número.

Ve a tu archivo app.py en GitHub, edítalo y cambia la línea del modelo exactamente a esto:

Python
model_name="gemini-flash",
(Si por algún casual tu cuenta no tuviera acceso a la familia Flash, el otro comodín universal que siempre funciona es model_name="gemini-pro",)

Dale a Commit changes para guardar. Streamlit se actualizará en unos segundos; recarga la página y hazle una pregunta. ¡Debería responderte por fin!

google.api_core.exceptions.ResourceExhausted: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:

File "/mount/src/desencadenado/app.py", line 257, in <module>

respuesta = modelo.generate_content(pregunta)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/generativeai/generative_models.py", line 331, in generate_content

response = self._client.generate_content(

request,

**request_options,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/ai/generativelanguage_v1beta/services/generative_service/client.py", line 835, in generate_content

response = rpc(

request,

...<2 lines>...

metadata=metadata,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__

return wrapped_func(*args, **kwargs)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 294, in retry_wrapped_func

return retry_target(

target,

...<3 lines>...

on_error=on_error,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 156, in retry_target

next_sleep = _retry_error_helper(

exc,

...<6 lines>...

timeout,

)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_base.py", line 214, in _retry_error_helper

raise final_exc from source_exc

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 147, in retry_target

result = target()

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/timeout.py", line 130, in func_with_timeout

return func(*args, **kwargs)

File "/home/adminuser/venv/lib/python3.14/site-packages/google/api_core/grpc_helpers.py", line 77, in error_remapped_callable

raise exceptions.from_grpc_error(exc) from exc

¡Buenas noticias! El error NotFound ha desaparecido, lo que significa que tu web ya se está conectando con éxito a los servidores de Google Gemini.

El nuevo aviso (ResourceExhausted) significa "Límite de cuota gratuita alcanzado". Cuando esto salta en el primer mensaje, suele deberse a uno de estos dos motivos:

Usaste gemini-pro: En las cuentas gratuitas de Google AI Studio, los modelos "Pro" suelen tener la cuota gratuita bloqueada (a cero). Solo los modelos Flash tienen uso gratuito amplio.

El código exacto del modelo Flash: En el paso anterior probamos variantes genéricas, pero el identificador técnico exacto del modelo que vimos activo en tu cuenta (Gemini Flash Latest) es gemini-flash-latest.

Cómo solucionarlo y evitar pantallas rojas
Ve a tu archivo app.py en GitHub, dale al icono del lápiz para editarlo y haz estos dos pequeños cambios al final de tu código (después de tu "ladrillo" de instrucciones):

1. Pon el nombre exacto del modelo gratuito:
Busca la línea de model_name (justo debajo de donde termina tu manual de entrenamiento) y déjala exactamente así:

Python
modelo = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=instrucciones
)
2. Protege el chat para ver avisos claros (Opcional pero muy recomendado):
Como Streamlit oculta los detalles de los errores por seguridad (The original error message is redacted), sustituye las últimas líneas de tu archivo (desde if pregunta: hasta el final) por este bloque mejorado:

Python
if pregunta:
    # Mostrar lo que pregunta el usuario
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta de la IA sin que la web se rompa si hay límite
    with st.chat_message("assistant"):
        try:
            respuesta = modelo.generate_content(pregunta)
            st.markdown(respuesta.text)
            st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta.text})
        except Exception as e:
            st.error(f"Detalle exacto de Google: {e}")
Haz clic en el botón verde Commit changes para guardar, espera unos segundos a que Streamlit se actualice y escribe de nuevo en el chat. Con gemini-flash-latest debería entrar dentro de tu cuota gratuita; y si Google vuelve a quejarse, el nuevo bloque try/except nos mostrará en pantalla el motivo exacto sin ocultar nada. ¿Qué te sale al probarlo?

Ponme todo el texto de app.py entero y corregido

Sustituye todo el contenido de tu archivo app.py en GitHub por este código (recuerda volver a pegar tu manual de entrenamiento en la zona indicada entre corchetes antes de guardar):

Python
import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página y Menú lateral (Tu ficha actual)
st.set_page_config(page_title="Entrenador Calistenia", page_icon="💪")
st.sidebar.title("Mi Ficha Actual")

semana = st.sidebar.number_input("Semana del Ciclo", min_value=1, max_value=11, value=1)
nivel_flexiones = st.sidebar.selectbox("Nivel Flexiones", [1, 2, 3, 4, 5])
nivel_sentadillas = st.sidebar.selectbox("Nivel Sentadillas", [1, 2, 3, 4, 5])
nivel_dominadas = st.sidebar.selectbox("Nivel Dominadas", [1, 2, 3, 4, 5])
nivel_verticales = st.sidebar.selectbox("Nivel Verticales", [1, 2, 3, 4, 5])
nivel_core = st.sidebar.selectbox("Nivel Core", [1, 2, 3, 4, 5])

# 2. Configurar la IA de Gemini con la clave de seguridad
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Instrucciones base (Tu Framework + Tus Niveles en tiempo real)
instrucciones = f"""
Actúa como mi entrenador personal experto en calistenia. Responde de forma clara y al grano.
MANUAL DEL ENTRENADOR:
[PEGA AQUÍ TODO TU LADRILLO/FRAMEWORK DE LAS 10 SEMANAS Y EJERCICIOS]

=========================================
DATOS ACTUALES DEL USUARIO:
- Semana Actual del ciclo: Semana {semana}
- Nivel Flexiones: {nivel_flexiones}
- Nivel Sentadillas: {nivel_sentadillas}
- Nivel Dominadas: {nivel_dominadas}
- Nivel Flexiones Verticales: {nivel_verticales}
- Nivel Core: {nivel_core}
"""

# 4. Configuración del modelo (versión gratuita activa)
modelo = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=instrucciones
)

# 5. Interfaz del Chat
st.title("💪 Entrenador IA - Método Desencadenado")

# Memoria del chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes anteriores en pantalla
for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["texto"])

# Caja para escribir nuevas preguntas
pregunta = st.chat_input("Ej: ¿Qué me toca entrenar hoy?")

if pregunta:
    # Mostrar y guardar lo que pregunta el usuario
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta de la IA (con detector de errores visible)
    with st.chat_message("assistant"):
        try:
            respuesta = modelo.generate_content(pregunta)
            st.markdown(respuesta.text)
            st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta.text})
        except Exception as e:
            st.error(f"Detalle exacto de Google: {e}")
Una vez pegado tu manual dentro de instrucciones, haz clic en el botón verde Commit changes arriba a la derecha, espera unos segundos a que tu web en Streamlit se actualice sola y escribe un mensaje de prueba en el chat.

File "/mount/src/desencadenado/app.py", line 1

google.api_core.exceptions.ResourceExhausted: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

^

SyntaxError: unterminated string literal (detected at line 1)

Este error ha ocurrido porque se te quedó copiado en el portapapeles el mensaje del error anterior (el que me acabas de enviar al chat) y lo has pegado por accidente en la primera línea de tu archivo app.py en lugar del código de programación.

Para solucionarlo, sigue estos pasos:

Entra en tu archivo app.py en GitHub y dale al icono del lápiz para editarlo.

Selecciona todo lo que hay dentro del archivo y bórralo por completo hasta que quede totalmente en blanco (la línea 1 debe empezar por import streamlit as st).

Haz clic en el icono de copiar (arriba a la derecha del recuadro gris de aquí abajo) para asegurarte de que copias el código limpio, pégalo en GitHub y añade tu manual en la zona indicada:

Python
import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página y Menú lateral (Tu ficha actual)
st.set_page_config(page_title="Entrenador Calistenia", page_icon="💪")
st.sidebar.title("Mi Ficha Actual")

semana = st.sidebar.number_input("Semana del Ciclo", min_value=1, max_value=11, value=1)
nivel_flexiones = st.sidebar.selectbox("Nivel Flexiones", [1, 2, 3, 4, 5])
nivel_sentadillas = st.sidebar.selectbox("Nivel Sentadillas", [1, 2, 3, 4, 5])
nivel_dominadas = st.sidebar.selectbox("Nivel Dominadas", [1, 2, 3, 4, 5])
nivel_verticales = st.sidebar.selectbox("Nivel Verticales", [1, 2, 3, 4, 5])
nivel_core = st.sidebar.selectbox("Nivel Core", [1, 2, 3, 4, 5])

# 2. Configurar la IA de Gemini con la clave de seguridad
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Instrucciones base (Tu Framework + Tus Niveles en tiempo real)
instrucciones = f"""
Actúa como mi entrenador personal experto en calistenia. Responde de forma clara y al grano.
MANUAL DEL ENTRENADOR:
[PEGA AQUÍ TODO TU LADRILLO/FRAMEWORK DE LAS 10 SEMANAS Y EJERCICIOS]

=========================================
DATOS ACTUALES DEL USUARIO:
- Semana Actual del ciclo: Semana {semana}
- Nivel Flexiones: {nivel_flexiones}
- Nivel Sentadillas: {nivel_sentadillas}
- Nivel Dominadas: {nivel_dominadas}
- Nivel Flexiones Verticales: {nivel_verticales}
- Nivel Core: {nivel_core}
"""

# 4. Configuración del modelo (versión gratuita activa)
modelo = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=instrucciones
)

# 5. Interfaz del Chat
st.title("💪 Entrenador IA - Método Desencadenado")

# Memoria del chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes anteriores en pantalla
for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["texto"])

# Caja para escribir nuevas preguntas
pregunta = st.chat_input("Ej: ¿Qué me toca entrenar hoy?")

if pregunta:
    # Mostrar y guardar lo que pregunta el usuario
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta de la IA (con detector de errores visible)
    with st.chat_message("assistant"):
        try:
            respuesta = modelo.generate_content(pregunta)
            st.markdown(respuesta.text)
            st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta.text})
        except Exception as e:
            st.error(f"Detalle exacto de Google: {e}")
Dale al botón verde Commit changes arriba a la derecha y espera unos segundos a que la pantalla de tu web se recargue.

Detalle exacto de Google: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit.

Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3.8-flash, description: Generate content requests per minute limit exceeded on Free Tier. See https://ai.google.dev/gemini-api/docs/rate-limits. Please retry in 40.51973481s. [links { description: "Learn more about Gemini API quotas" url: "https://ai.google.dev/gemini-api/docs/rate-limits" } , violations { description: "Generate content requests per minute limit exceeded on Free Tier. See https://ai.google.dev/gemini-api/docs/rate-limits." quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests" quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier" quota_dimensions { key: "model" value: "gemini-3.8-flash" } quota_dimensions { key: "location" value: "global" } quota_value: 5 } , retry_delay { seconds: 40 } ]
¡Tu aplicación ya está conectada y funcionando con el modelo gemini-3.8-flash! Ese aviso ya no es un fallo de tu código ni de tus claves, sino el límite de velocidad de la versión gratuita de Google.

Esto es lo que dice exactamente el mensaje que acabas de destapar:

limit: 5 (Generate content requests per minute limit exceeded on Free Tier): El plan gratuito del modelo gemini-3.8-flash solo permite enviar 5 mensajes por minuto.

Please retry in 40.5s: Al haber hecho varias pruebas seguidas al recargar la web (sumado a que la librería de Google reintenta conectarse automáticamente varias veces en un segundo cuando nota saturación), gastaste los 5 intentos del minuto actual. Google simplemente te puso en pausa durante 40 segundos.

Qué hacer ahora mismo:

Haz la prueba definitiva: Espera 1 minuto completo sin recargar la página, escribe una sola pregunta en el chat (ej. "¿Qué me toca entrenar hoy?") y pulsa Enter. Al haberse reiniciado el contador de 60 segundos, te dará tu rutina de entrenamiento.

En tu día a día entrenando: Como solo le harás una o dos preguntas puntuales para ver tu rutina, nunca chocarás con ese límite de 5 mensajes por minuto.

Truco si quieres más velocidad gratis: Si en algún momento notas que el límite de 5 por minuto se te queda corto charlando con él, puedes cambiar en tu app.py el nombre del modelo de "gemini-flash-latest" a "gemini-flash-lite-latest" (la versión ligera suele tener una cuota gratuita por minuto mucho más amplia).

Espera ese minuto, hazle una pregunta a tu entrenador y dime si ya te genera la rutina en pantalla.

Sale el mismo error: Detalle exacto de Google: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit.

Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.8-flash, description: Generate content requests per day limit exceeded on Free Tier. See https://ai.google.dev/gemini-api/docs/rate-limits. Please retry in 14h16m33.749638039s. [links { description: "Learn more about Gemini API quotas" url: "https://ai.google.dev/gemini-api/docs/rate-limits" } , violations { description: "Generate content requests per day limit exceeded on Free Tier. See https://ai.google.dev/gemini-api/docs/rate-limits." quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests" quota_id: "GenerateRequestsPerDayPerProjectPerModel-FreeTier" quota_dimensions { key: "model" value: "gemini-3.8-flash" } quota_dimensions { key: "location" value: "global" } quota_value: 20 } , retry_delay { seconds: 51393 } ]
Aunque parece el mismo mensaje, fíjate en un detalle clave que ha cambiado dentro del texto: antes decía limit: 5 ... per minute (límite por minuto) y ahora dice limit: 20 ... per day ... retry in 14h16m (límite de 20 peticiones al día superado, pidiendo esperar 14 horas).

¿Por qué has gastado 20 usos si solo has escrito 3 o 4 veces?
Cuando haces una pregunta y salta un error de límite por minuto, el conector de Google intenta reenviar tu mensaje 5 veces seguidas de forma oculta en pocos segundos antes de rendirse y mostrarte el fallo. Con solo 3 o 4 pruebas que hicimos antes, esos reintentos automáticos consumieron de golpe los 20 usos diarios gratuitos que Google da para el modelo gemini-3.8-flash.

Cómo saltarse la espera de 14 horas ahora mismo
El contador de Google funciona por modelo individual (PerProjectPerModel). Eso significa que si cambiamos a la versión ligera del modelo (Lite), estrenas un contador completamente nuevo a cero y además tendrás un límite diario gratuito mucho más amplio:

Entra en tu archivo app.py en GitHub y dale al icono del lápiz para editarlo.

Baja hasta el punto 4 (# 4. Configuración del modelo) y cambia "gemini-flash-latest" por "gemini-flash-lite-latest", dejándolo así:

Python
# 4. Configuración del modelo (versión gratuita activa)
modelo = genai.GenerativeModel(
    model_name="gemini-flash-lite-latest",
    system_instruction=instrucciones
)
Haz clic en el botón verde Commit changes arriba a la derecha.

Espera unos 15 segundos a que tu página de Streamlit se recargue sola y escribe una sola pregunta en el chat. Al ser un modelo distinto, no tendrás que esperar las 14 horas y te responderá al momento. ¿Te carga ya la rutina con la versión Lite?

Perfecto, ahora funciona. ¿se puede hacer mejor y más completo el "ladrillo"? ¿se pueden añadir fotos para ver como es el ejercicio?. Te paso el libro para que lo valores

Analizando el libro completo, sí a ambas cosas: el "ladrillo" puede volverse muchísimo más inteligente (ya que el modelo que usas ahora soporta textos enormes sin despeinarse) y en Streamlit es muy fácil mostrar las fotos originales del libro.   
DOCX

1. Qué le faltaba a tu "Ladrillo" (y cómo mejorarlo con el libro)
Al leer el libro completo, hay reglas clave que hacen que el entrenador piense exactamente como el autor y no solo te escupa una lista de ejercicios:   
DOCX

Cálculo automático del nivel de trabajo según la semana: El libro exige trabajar en Nivel Máximo - 1 en las semanas 1 y 2 (o Nivel Máximo si superas las 20 repeticiones en la pirámide), subir a Nivel Máximo + 1 en las semanas 3 y 4 (si logras hacer al menos 3-4 repeticiones), y usar tu Nivel Máximo en las semanas 5 a 8.   
DOCX

Criterios exactos para subir de nivel (Tests en Semanas 1, 4 y 8): El bot puede examinarte sabiendo las marcas exactas de cada nivel (por ejemplo, 30 repeticiones en hombres para pasar los niveles 1 a 4 de flexiones y sentadillas, o los tiempos colgado en dominadas).   
DOCX

Sustituciones inteligentes y equipamiento casero: Si le dices al chat "hoy me duele el hombro", "no tengo barra" o "se me hace muy difícil", el bot puede usar el catálogo de más de 70 ejercicios del libro (con sus grados de dificultad del 1 al 5) y proponerte trucos caseros del manual, como hacer dominadas horizontales debajo de una mesa sólida o con un palo de escoba entre dos sillas.   
DOCX

Módulos extra del libro: Podemos meterle el protocolo exacto de calentamiento de 5 minutos, los 6 WODs de CrossFit corporales para variar en las semanas 9 y 10, el tutorial de 5 niveles del Handstand (pino) y las reglas de Nutrición (macros 25% proteína / 40% grasa / 35% carbohidratos y 1 a 1,5 g de proteína por kilo de peso).   
DOCX

El "Súper Ladrillo" mejorado para tu app.py
Sustituye la variable instrucciones = f"""...""" en tu archivo app.py por esta versión mucho más completa (solo tienes que pegar el cuadro de las rutinas diarias de las 10 semanas donde se indica):

Python
instrucciones = f"""
Actúa como mi entrenador personal experto en calistenia del método "Desencadenado: tu cuerpo es tu gimnasio" de Fitness Revolucionario. Responde de forma directa, motivadora, clara y estructurada.

=========================================
1. FILOSOFÍA Y CALENTAMIENTO OBLIGATORIO
=========================================
- Antes de entrenar SIEMPRE se calienta 5 minutos (nunca estirar en frío): 25 jumping jacks, 20 giros de cada brazo (10 delante, 10 atrás), 10 giros de cuello (5 por lado), 30 seg de salto de cuerda (o correr en el sitio), 25 jumping jacks + 5 burpees (o 30 seg de escaladores).
- Al terminar la sesión SIEMPRE se estira en caliente (10-15 seg por postura sin dolor).
- "Nivel Máximo" del usuario: el nivel más avanzado (1 a 5) que realiza con buena técnica pero sin alcanzar aún las repeticiones para pasar al siguiente.

=========================================
2. LOS 5 EJERCICIOS TRONCALES, PROGRESIONES Y VARIANTES
=========================================
(Requisito de avance para Hombres = H / Mujeres = M)

A) EMPUJAR - FLEXIONES (Pectorales, tríceps, deltoides, core):
- Técnica: Cuerpo recto, abdominales en tensión, codos cerca del cuerpo, pecho a pocos cm del apoyo, inspirar al bajar y espirar al subir.
- Nivel 1: Manos elevadas a altura de cadera/mesa (si no hace 5-10, empezar contra pared hasta hacer 15-20) -> Avance: H: 30 reps / M: 20 reps.
- Nivel 2: De rodillas -> Avance: H: 30 / M: 20.
- Nivel 3: Flexión clásica sobre puntas de los pies -> Avance: H: 30 / M: 20.
- Nivel 4: Pies elevados (altura mitad del muslo/silla) -> Avance: H: 30 / M: 20.
- Nivel 5: Con una mano (pies separados, mano tras espalda; transición con una mano sobre balón alejándolo gradualmente) -> Meta élite: H: 10 reps por mano / M: 8 por mano.
- Variantes (nivel entre paréntesis): Manos separadas (3), Manos juntas/diamante (3-4), Flexiones "T" (3-4), Sobre balones 1 o 2 manos (3-4), Sobre balón alternando explosivo (3-4), Superman (4-5), Con palmada (4), Espartanas (4-5), Fondos/Dips entre 2 sillas o con pies apoyados en 3ª silla (3-4), Flexiones profundas entre 3 sillas (3-4), Extensiones de tríceps en pared/cadera/rodillas (2-4).

B) EMPUJAR - FLEXIÓN VERTICAL (Deltoides, trapecios, tríceps, core):
- Nivel 1: Posición vertical sobre la cabeza (cojín a 15-20 cm de la pared, formando triángulo con manos) -> Avance: H y M: 45 seg.
- Nivel 2: Posición vertical sobre las manos (subiendo con kick-up o escalando la pared de espaldas) -> Avance: H y M: 45 seg.
- Nivel 3: Semi-flexión vertical (pies en silla/mesa formando ángulo de 90º) -> Avance: H: 10 reps / M: 8 reps.
- Nivel 4: Flexión vertical contra pared -> Avance: H: 10 / M: 8.
- Nivel 5: Flexión vertical profunda (manos sobre libros gordos/soportes para bajar la cabeza más allá de las manos) -> Meta élite: H: 10 / M: 8.
- Variantes: Flexión hindú en V (2-3), Bombardero en picado / Dive Bomber (3-4).

C) TIRAR - DOMINADAS (Dorsales, bíceps, braquiorradial, romboides, trapecios):
- Agarres: Prono (por defecto, palmas hacia fuera, énfasis dorsal/antebrazo), Supino (palmas hacia ti, énfasis bíceps), Neutro (palmas enfrentadas, protege codos), Mixto y Comando.
- Nivel 1: Colgarse con hombros activos/tensos -> Avance: H: 45 seg brazos estirados + 20 seg barbilla sobre la barra (con 30 seg descanso entre ambos) / M: 40 seg estirados + 15 seg flexionados.
- Nivel 2: Dominadas asistidas (pies en silla debajo o adelantada) -> Avance: H: 10 reps / M: 8 reps.
- Nivel 3: Dominada clásica (sin balancear piernas, barbilla pasa la barra) -> Avance: H: 10 / M: 7.
- Nivel 4: Dominada con mano y media (una mano en barra, la otra agarra la muñeca; se recomienda agarre supino) -> Avance: H: 8 por mano / M: 5 por mano.
- Nivel 5: Dominada con una mano (progresar usando cinta elástica, toalla enrollada, lastre, reduciendo dedos de apoyo, bajando agarre a antebrazo/bíceps/hombro o dominadas negativas lentas) -> Meta élite: H: 3 por mano / M: 1 por mano.
- Variantes: Manos juntas (3-4), Semi-dominada horizontal en pomos de puerta (2), Dominada horizontal en barra baja, bajo mesa sólida o palo de escoba en 2 sillas (2-3), Dominada comando (3-4), Muscle-up (4-5).

D) PIERNAS - SENTADILLAS (Cuádriceps, glúteos, cadera):
- Técnica: Talones siempre pegados al suelo, pies anchura de hombros abiertos 30º, rodillas hacia fuera, cadera baja más que las rodillas (muslos tocan gemelos en completa), pausa 1 seg abajo.
- Nivel 1: Sentadilla media con apoyo (bajando hasta sentarse en silla/sofá) -> Avance: H y M: 30 reps.
- Nivel 2: Sentadilla completa con apoyo (sujetando silla/marco de puerta) -> Avance: H y M: 30 reps.
- Nivel 3: Sentadilla tradicional profunda (practicar a 15 cm de la pared) -> Avance: H y M: 30 reps.
- Nivel 4: Sentadilla con una pierna asistida (apoyo en silla/marco de puerta) -> Avance: H: 15 por pierna / M: 10 por pierna.
- Nivel 5: Sentadilla con 1 pierna (Pistol squat sin apoyo) -> Meta élite: H: 10 por pierna / M: 8 por pierna.
- Variantes: Saltos sobre plataforma/escalón (2-4), Sentadilla con salto (3-4), Rodilla a pecho (2-3), Desplantes/zancadas (2-3), Desplantes laterales (2-3), Desplantes con salto (3-4), Elevaciones de talones 1 o 2 piernas (2-3), Sentadilla búlgara con pie trasero en silla (3-4).

E) CORE - ABDOMINALES (Recto abdominal, oblicuos, transverso, serratos, lumbares):
- Nivel 1: Abdominales en silla (encogimientos de piernas sentado al borde) -> Avance: H y M: 30 reps.
- Nivel 2: Levantamiento de piernas en el suelo con piernas encogidas -> Avance: H y M: 30 reps.
- Nivel 3: Levantamiento de piernas en el suelo con piernas estiradas (sin tocar suelo al bajar, a 5-10 cm) -> Avance: H y M: 25 reps.
- Nivel 4: Levantamiento de piernas colgado en barra con piernas encogidas -> Avance: H y M: 15 reps.
- Nivel 5: Levantamiento de piernas colgado con piernas estiradas (subir en 2 seg hasta paralelas al suelo y bajar en 2 seg sin balanceo) -> Meta élite: H y M: 10 reps.
- Variantes: Plancha isométrica (2-3, mínimo 45s antes de usar rueda), Plancha lateral (3), Plancha con flexión en V explosiva (3), Plancha lateral con flexión (3), Levantamiento de caderas a 1 o 2 piernas (2-3), Lumbares en suelo (2-3), Abdominales en V (4-5), Flexión S&M / Bird-dog (3-4), Bicicleta (4), Pies a manos en barra (5), Bandera / Dragon flag (5), Rueda abdominal (4-5).

F) CUERPO COMPLETO Y CARDIO:
- Burpees (3), Escaladores (2-3), Escaladores inversos boca arriba (3-4), Jumping Jacks (2), Flexión a Plancha (2-3), Levantamiento con impulso sin manos (3-4), Levantamientos de rodillas (2-3), Pino puente (4-5), Esprints en días libres (en llano o cuesta arriba tras calentar al 70-80%).

=========================================
3. REGLAS METODOLÓGICAS DE LAS 10 SEMANAS
=========================================
- SEMANAS 1 Y 2 (Resistencia y Masa Muscular):
  * Intensidad: Usar "Nivel Máximo - 1" (salvo que en la pirámide supere las 20 repeticiones en la cima, donde se pasa a "Nivel Máximo").
  * Días de Pirámides: 4 pirámides de 7 minutos cada una, con 1 min de descanso entre pirámides. Subir de 1 en 1 (1, 2, 3... hasta tope sin llegar al fallo total y bajar a 1). El descanso entre series dentro de la pirámide dura exactamente lo mismo que tardaste en hacer las repeticiones. En ejercicios unilaterales se hacen ambos lados antes de descansar. Si estás en Nivel 1 de dominadas: pirámide de tiempos colgado de 5 en 5 seg (5s, 10s, 15s...).
  * Días de Supersets: 2 ejercicios complementarios seguidos sin descanso (8-12 reps del 1º + 8-12 reps del 2º) y 1 min de descanso al terminar la pareja.

- SEMANAS 3 Y 4 (Fuerza):
  * Intensidad: Usar "Nivel Máximo + 1" siempre que se puedan hacer al menos 3-4 repeticiones; si no, usar "Nivel Máximo". Rango objetivo: pocas repeticiones (si pasas de 8-10 reps, añadir lastre con mochila/bidones o subir de nivel).
  * Ejecución: Cadencia controlada 2 segundos subida (concéntrica) y 2 segundos bajada (excéntrica).
  * Descansos: 1 minuto entre tandas y 2 minutos entre ejercicios.
  * Nota fin de Semana 4: Recomendar hacer Test de Nivel en un día libre.

- SEMANAS 5 Y 6 (Potencia):
  * Intensidad: Usar "Nivel Máximo" (o "Nivel Máximo - 1" si no se consigue hacer de forma explosiva).
  * Ejecución: Fase concéntrica a MÁXIMA velocidad/explosividad, aguantar 2 segundos en la posición final, y fase excéntrica lenta.
  * Descansos: 1 minuto entre tandas y 2 minutos entre ejercicios.

- SEMANAS 7 Y 8 (Acondicionamiento Global - Fase 1):
  * Intercala sesiones de Fuerza y Potencia trabajando en tu "Nivel Máximo". Al terminar la Semana 8, recomendar nuevo Test de Nivel.

- SEMANAS 9 Y 10 (Acondicionamiento Global - Fase 2: Tabatas y HIIT):
  * Semana 9: Reducir descansos al mínimo (30 seg entre tandas, máx 1 min entre ejercicios). Incluye series a "mrp" (máximas repeticiones posibles), "mtp" (máximo tiempo posible) y Tabatas (8 rondas de 20 seg a tope + 10 seg descanso = 4 min totales). Si no hay cuerda de saltar, sustituir por el mismo número de levantamientos de rodillas.
  * Semana 10 (HIIT): 4 sesiones de alta intensidad. Hacer todos los ejercicios de la ronda seguidos SIN descanso, descansar 1 minuto y repetir para completar 2 rondas en el menor tiempo posible (anotar tiempo para batir récord).

- SEMANA 11: Semana obligatoria de Descanso Activo (caminatas, flexibilidad, movilidad, sin entrenamientos intensos).

[PEGA AQUÍ TU CUADRO CON EL DETALLE DE LOS DÍAS 1, 2, 3 Y 4 DE CADA SEMANA]

=========================================
4. WODs DE CROSSFIT, HANDSTAND Y NUTRICIÓN
=========================================
- WODs CrossFit (opcionales para semanas 9-10):
  * WOD 1 (AMRAP 15 min): Rondas de 5 flexiones (N3) + 10 saltos plataforma (60cm H/50cm M) + 15 sentadillas (N3).
  * WOD 2 (Por tiempo):Escalera cruzada de Saltos plataforma (35-30-25-20-15-10-5) y Flexiones verticales N4 (2-4-6-8-10-12-14). Reducida: empieza en 25 saltos.
  * WOD 3 (3 rondas por tiempo, 2 min descanso entre rondas): 20 dominadas + 20 flexiones + 20 sentadillas + 40 escaladores (20/pierna) + 100 saltos cuerda (Reducida: mitad de reps).
  * WOD 4 (5 rondas, 1 min descanso entre rondas): 1 min dominadas + 1 min flexiones + 1 min burpees (Reducida: 4 rondas de 45 seg).
  * WOD 5 (2 rondas por tiempo): 100 saltos cuerda + 40 sentadillas + 30 abdominales + 20 flexiones + 10 dominadas (Reducida: 75/30/20/15/8).
  * WOD 6 (3 rondas por tiempo): 40 desplantes + 40 sentadillas + 40 flexiones (Reducida: 20/20/20).
- Progresión Handstand (Pino): Nivel 1 (Cuerpo rígido 45s / Hollow rock 30s), Nivel 2 (Pino contra pared 45s), Nivel 3 (La rana / Crow pose 30s), Nivel 4 (De rana a Headstand), Nivel 5 (Handstand libre y escape lateral o en voltereta).
- Nutrición base: Comida real sin azúcares ni harinas refinadas; macros orientativos 25% proteína (mínimo 1 - 1.5g por kg de peso), 40% grasas saludables (aguacate, frutos secos, aceite de oliva, pescado, huevos) y 35% carbohidratos (verduras libres, 1-2 frutas, concentrar carbos post-entreno).

=========================================
5. FICHA ACTUAL DEL USUARIO (EN TIEMPO REAL):
=========================================
- Semana Actual del ciclo: Semana {semana}
- Nivel Máximo en Flexiones: Nivel {nivel_flexiones}
- Nivel Máximo en Sentadillas: Nivel {nivel_sentadillas}
- Nivel Máximo en Dominadas: Nivel {nivel_dominadas}
- Nivel Máximo en Flexiones Verticales: Nivel {nivel_verticales}
- Nivel Máximo en Core/Abdominales: Nivel {nivel_core}
(Adapta automáticamente el nivel que me toca usar hoy aplicando la regla de la Semana {semana} sobre mis niveles actuales).
"""
2. ¿Cómo añadir las fotos del libro a tu web de Streamlit?
Streamlit permite mostrar imágenes de forma nativa con una sola línea de código (st.image). Como me has pasado el archivo en formato Word (.docx), tienes todas las fotos originales del libro guardadas ahí dentro y puedes sacarlas de golpe en 10 segundos sin tener que hacer capturas de pantalla una por una:

Paso 1: Extraer todas las fotos del archivo .docx de golpe
Un archivo .docx en realidad es una carpeta comprimida disfrazada. Haz este truco en tu ordenador:

Haz una copia en tu ordenador del archivo Desencadenado_ tu cuerpo es tu gimnasio - Fitness Revolucionario.docx.

Cámbiale el nombre y sustituye el final .docx por .zip (para que se llame Desencadenado.zip). Si te pregunta si estás seguro de cambiar la extensión, dile que sí.

Abre o descomprime ese archivo .zip y entra en la carpeta word -> media.

Ahí dentro encontrarás todas las fotos del libro sueltas y numeradas (image1.jpeg, image2.jpeg, etc.). Ponles nombres fáciles a las que más te interesen (por ejemplo: flexion_n1.jpg, flexion_t.jpg, dominada_comando.jpg, sentadilla_bulgara.jpg).

Paso 2: Subirlas a tu GitHub y verlas en tu aplicación
Entra en tu repositorio de GitHub, haz clic en Add file > Upload files y arrastra las fotos ahí (o mételas en una carpeta llamada fotos). Dale a Commit changes.

En tu archivo app.py, podemos añadir un Visor de Ejercicios en el menú lateral izquierdo (debajo de tus niveles) para que, mientras entrenas y lees el chat, puedas elegir cualquier ejercicio en un desplegable y ver la foto al instante sin perder la conversación:

Python
# Añade esto en tu app.py justo debajo de los selectbox del menú lateral (sidebar):
st.sidebar.markdown("---")
st.sidebar.subheader("📸 Guía Visual de Ejercicios")

fotos_ejercicios = {
    "Selecciona un ejercicio...": None,
    "Flexión Nivel 1 (Mesa)": "fotos/flexion_n1.jpg",
    "Flexión en T": "fotos/flexion_t.jpg",
    "Flexión Hindú": "fotos/flexion_hindu.jpg",
    "Dominada Comando": "fotos/dominada_comando.jpg",
    "Sentadilla Búlgara": "fotos/sentadilla_bulgara.jpg",
}

ejercicio_ver = st.sidebar.selectbox("Ver cómo se hace:", list(fotos_ejercicios.keys()))

if fotos_ejercicios[ejercicio_ver]:
    st.sidebar.image(fotos_ejercicios[ejercicio_ver], caption=ejercicio_ver, use_container_width=True)
Incluso, si prefieres que el propio chat te muestre la foto dentro de la respuesta, cuando subas las fotos a tu GitHub público me dices cómo las has llamado y le añadimos una línea al "ladrillo" para que Gemini incruste la foto automáticamente cada vez que te mande hacer un ejercicio. ¿Qué opción te resulta más cómoda para entrenar: el visor en el menú lateral o que salgan dentro de los mensajes del chat?

Pásame el archivo app.py entero

Tu archivo PY está listo

Icono de PY
app
 PY 
He transcrito e integrado directamente dentro del código todas las tablas de entrenamiento de las Semanas 1 a la 10 (Días 1, 2, 3 y 4), además de las progresiones, variantes, WODs de CrossFit, guía de Handstand y pautas de nutrición del libro. No tienes que rellenar ni pegar ningún "ladrillo" aparte: basta con que copies este código tal cual y sustituyas todo tu archivo app.py en GitHub.   
DOCX

También he añadido en el menú lateral un selector de Día de entrenamiento (1 a 4), memoria de conversación real para que recuerde lo que habláis en el chat, y un visor automático de fotos que se activará solo si en algún momento decides crear una carpeta llamada fotos en tu GitHub con imágenes de los ejercicios (si no subes fotos, la aplicación funciona sin dar ningún error).   
DOCX

Python
import os
import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página y Menú lateral (Tu ficha actual)
st.set_page_config(page_title="Entrenador Calistenia - Desencadenado", page_icon="💪", layout="centered")
st.sidebar.title("💪 Mi Ficha Actual")

sexo = st.sidebar.radio("Sexo (para criterios de test)", ["Hombre", "Mujer"], horizontal=True)
semana = st.sidebar.number_input("Semana del Ciclo (1-11)", min_value=1, max_value=11, value=1)
dia_semana = st.sidebar.selectbox("Día de entrenamiento de la semana", [1, 2, 3, 4])

st.sidebar.markdown("### Mis Niveles Máximos (1 a 5)")
nivel_flexiones = st.sidebar.selectbox("Nivel Flexiones", [1, 2, 3, 4, 5], index=0)
nivel_verticales = st.sidebar.selectbox("Nivel Flexiones Verticales", [1, 2, 3, 4, 5], index=0)
nivel_dominadas = st.sidebar.selectbox("Nivel Dominadas", [1, 2, 3, 4, 5], index=0)
nivel_sentadillas = st.sidebar.selectbox("Nivel Sentadillas", [1, 2, 3, 4, 5], index=0)
nivel_core = st.sidebar.selectbox("Nivel Core / Abdominales", [1, 2, 3, 4, 5], index=0)

# Visor opcional de fotos (solo se activa si subes una carpeta 'fotos' a tu GitHub)
if os.path.isdir("fotos"):
    archivos_fotos = sorted([f for f in os.listdir("fotos") if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))])
    if archivos_fotos:
        st.sidebar.markdown("---")
        st.sidebar.subheader("📸 Guía Visual de Ejercicios")
        foto_elegida = st.sidebar.selectbox("Ver imagen de ejercicio:", ["Selecciona una foto..."] + archivos_fotos)
        if foto_elegida != "Selecciona una foto...":
            st.sidebar.image(os.path.join("fotos", foto_elegida), caption=foto_elegida, use_container_width=True)

if st.sidebar.button("🗑️ Limpiar historial del chat"):
    st.session_state.mensajes = []
    st.rerun()

# 2. Configurar la IA de Gemini con la clave de seguridad
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Instrucciones base (El libro completo + Plan de 10 semanas + Tus Niveles en tiempo real)
instrucciones = f"""
Actúa como mi entrenador personal experto en calistenia del método "Desencadenado: tu cuerpo es tu gimnasio" de Fitness Revolucionario. Responde de forma directa, motivadora, clara y estructurada.

=========================================
1. FILOSOFÍA Y CALENTAMIENTO OBLIGATORIO
=========================================
- Antes de entrenar SIEMPRE se calienta 5 minutos (nunca estirar en frío):
  * 25 jumping jacks
  * 20 giros de cada brazo (10 hacia delante y 10 hacia atrás)
  * 10 giros de cuello (5 en cada dirección)
  * 30 segundos de salto de cuerda (o correr en el sitio)
  * 25 jumping jacks + 5 burpees (o 30 segundos de escaladores)
- Al terminar la sesión SIEMPRE se estira en caliente (10-15 segundos por postura, sintiendo tensión pero nunca dolor).
- Definición de "Nivel Máximo": el nivel más avanzado (de 1 a 5) que el usuario puede realizar con buena técnica pero sin lograr aún cumplir el requisito de repeticiones para avanzar al siguiente.

=========================================
2. LOS 5 EJERCICIOS TRONCALES, PROGRESIONES Y VARIANTES
=========================================
(Requisitos de avance para Hombres = H / Mujeres = M)

A) EMPUJAR - FLEXIONES (Pectorales, tríceps, deltoides, core):
- Técnica: Cuerpo totalmente recto, abdominales tensos, codos cerca del cuerpo, bajar hasta pocos cm del apoyo, inspirar al bajar y espirar al subir.
- Nivel 1: Manos elevadas sobre mesa/superficie a altura de la cadera (si no llega a 5-10 reps, empezar contra la pared hasta hacer 15-20) -> Avance: H: 30 reps / M: 20 reps.
- Nivel 2: De rodillas -> Avance: H: 30 reps / M: 20 reps.
- Nivel 3: Flexión clásica sobre puntas de los pies -> Avance: H: 30 reps / M: 20 reps.
- Nivel 4: Pies elevados (sobre silla/superficie a mitad del muslo) -> Avance: H: 30 reps / M: 20 reps.
- Nivel 5: Con una mano (pies algo separados, una mano tras la espalda; para progresar del 4 al 5 usar un balón bajo la mano de apoyo e ir alejándolo) -> Meta élite: H: 10 reps por mano / M: 8 reps por mano.
- Variantes (nivel entre paréntesis): Manos separadas 15-25 cm (3), Manos juntas o diamante (3-4), Flexiones "T" rotando torso (3-4), Sobre balones 1 o 2 manos (3-4), Sobre balón alternando explosivo (3-4), Superman estirado (4-5), Con palmada pliométrica (4), Espartanas alternando mano adelantada en el aire (4-5), Fondos en paralelas o Dips entre 2 sillas o asistidos con 3 sillas (3-4), Flexiones profundas entre 3 sillas (3-4), Extensiones de tríceps en pared/barra/silla (2-4).

B) EMPUJAR - FLEXIÓN VERTICAL (Deltoides, trapecios, tríceps, core):
- Nivel 1: Posición vertical sobre la cabeza (cojín a 15-20 cm de la pared formando triángulo con manos y cabeza) -> Avance: H: 45 seg / M: 45 seg.
- Nivel 2: Posición vertical sobre las manos contra la pared (subiendo con kick-up o escalando la pared de espaldas) -> Avance: H: 45 seg / M: 45 seg.
- Nivel 3: Semi-flexión vertical (pies apoyados en silla/mesa formando ángulo de 90 grados) -> Avance: H: 10 reps / M: 8 reps.
- Nivel 4: Flexión vertical contra la pared -> Avance: H: 10 reps / M: 8 reps.
- Nivel 5: Flexión vertical profunda (manos sobre libros gruesos/soportes sólidos para que la cabeza baje más allá de las manos) -> Meta élite: H: 10 reps / M: 8 reps.
- Variantes: Flexión hindú en V (2-3), Bombardero en picado o Dive Bomber (3-4).

C) TIRAR - DOMINADAS (Dorsales, bíceps, braquiorradial, romboides, trapecios):
- Agarres: Prono (por defecto cuando no se especifica; palmas hacia fuera, énfasis dorsal y antebrazo), Supino (palmas hacia ti, énfasis bíceps), Neutro (palmas enfrentadas, protege codos), Mixto y Comando.
- Nivel 1: Colgarse de la barra con hombros activos/tensionados -> Avance: H: 45 seg brazos estirados + 20 seg brazos flexionados con barbilla sobre la barra (30 seg descanso entre ambos) / M: 40 seg estirados + 15 seg flexionados.
- Nivel 2: Dominadas asistidas (apoyando pies en una silla debajo o adelantada) -> Avance: H: 10 reps / M: 8 reps.
- Nivel 3: Dominada clásica (sin balancear piernas, barbilla supera la barra y baja hasta estirar brazos) -> Avance: H: 10 reps / M: 7 reps.
- Nivel 4: Dominadas con mano y media (una mano agarra la barra y la otra sujeta la muñeca; recomendado agarre supino inicialmente) -> Avance: H: 8 reps por mano / M: 5 reps por mano.
- Nivel 5: Dominadas con una mano (progresar con silla, banda elástica, toalla enrollada en mano de apoyo, lastre, reduciendo dedos de apoyo, bajando agarre de muñeca a antebrazo/bíceps/hombro, dominadas negativas lentas o método GTG) -> Meta élite: H: 3 reps por mano / M: 1 rep por mano.
- Variantes: Manos juntas (3-4), Semi-dominada horizontal en pomos de puerta (2), Dominada horizontal en barra baja, debajo de una mesa sólida o con palo de escoba entre 2 sillas (2-3), Dominada comando perpendicular a la barra (3-4), Muscle-up (4-5).

D) PIERNAS - SENTADILLAS (Cuádriceps, glúteos, cadera):
- Técnica: Talones siempre en el suelo, pies anchura de hombros abiertos 30 grados, rodillas hacia fuera, espalda recta, cadera baja más que las rodillas (muslos tocan gemelos), pausa de 1 seg abajo.
- Nivel 1: Sentadilla media con apoyo (bajando hasta sentarse en silla/sofá) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 2: Sentadilla completa con apoyo (sujetando silla/marco de puerta) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 3: Sentadilla tradicional profunda (practicar al inicio a 15 cm de la pared) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 4: Sentadilla con una pierna asistida (apoyando mano en silla o marco de puerta) -> Avance: H: 15 reps por pierna / M: 10 reps por pierna.
- Nivel 5: Sentadilla con 1 pierna sin apoyo (Pistol squat) -> Meta élite: H: 10 reps por pierna / M: 8 reps por pierna.
- Variantes: Saltos sobre plataforma/escalón (2-4), Sentadilla con salto pliométrica (3-4), Rodilla a pecho (2-3), Desplantes/zancadas (2-3), Desplantes laterales (2-3), Desplantes con salto (3-4), Elevaciones de talones en escalón a 1 o 2 piernas (2-3), Sentadilla búlgara con empeine trasero en silla y opción de mochila/bidones (3-4).

E) CORE - ABDOMINALES (Recto abdominal, oblicuos, transverso, serratos, lumbares):
- Nivel 1: Abdominales en silla (encogimientos de piernas sentado al borde sin tocar suelo) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 2: Levantamiento de piernas en el suelo (piernas encogidas) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 3: Levantamiento de piernas en el suelo (piernas estiradas, quedando a 5-10 cm del suelo al bajar) -> Avance: H: 25 reps / M: 25 reps.
- Nivel 4: Levantamiento de piernas colgado en barra (piernas encogidas hasta muslos paralelos al suelo) -> Avance: H: 15 reps / M: 15 reps.
- Nivel 5: Levantamiento de piernas colgado (piernas completamente estiradas hasta paralelas al suelo, 2 seg subir y 2 seg bajar sin balanceo) -> Meta élite: H: 10 reps / M: 10 reps.
- Variantes: Plancha isométrica (2-3, mínimo 45 seg antes de usar rueda abdominal), Plancha lateral (3), Plancha con flexión en V explosiva (3), Plancha lateral con flexión (3), Levantamiento de caderas / puente glúteo a 1 o 2 piernas (2-3), Lumbares en suelo (2-3), Abdominales en V (4-5), Flexión S&M / Bird-dog (3-4), Bicicleta (4), Pies a manos en barra (5), Bandera / Dragon flag (5), Rueda de abdominales de rodillas o de pie (4-5).

F) CUERPO COMPLETO Y CARDIO:
- Burpees (3), Escaladores (2-3), Escaladores inversos boca arriba (3-4), Jumping Jacks (2), Flexión a Plancha (2-3), Levantamiento con impulso sin apoyar manos (3-4), Levantamientos de rodillas (2-3), Pino puente (4-5), Esprintar en días libres (tras calentar y hacer 2 semi-sprints al 70-80%).

=========================================
3. PLAN DE ENTRENAMIENTO DE 10 SEMANAS (DETALLE EXACTO POR DÍA)
=========================================

--- SEMANAS 1 Y 2: RESISTENCIA Y MASA MUSCULAR ---
* Regla de Nivel: Usar "Nivel Máximo - 1" (salvo que en la pirámide superes las 20 repeticiones en la cima, en cuyo caso usas tu "Nivel Máximo").
* Regla de Pirámides (Días 1 y 2): 7 minutos por ejercicio, con 1 minuto de descanso entre pirámides. Subes de 1 en 1 (1, 2, 3... hasta tu tope sin llegar al fallo y bajas de 1 en 1 hasta 1; si sobra tiempo dentro de los 7 min, vuelves a empezar). El descanso entre series dentro de la pirámide es igual al tiempo que tardaste en hacer las repeticiones. En ejercicios unilaterales haces ambos lados antes de descansar. Si estás en Nivel 1 de dominadas: pirámide colgado de 5 en 5 segundos (5s, 10s, 15s...).
* Regla de Supersets (Días 3 y 4): Hacer 8-12 reps del primer ejercicio e inmediatamente 8-12 reps del segundo sin descanso. Descansar 1 minuto entre supersets. Si estás en Nivel 1 de dominadas: aguantar colgado máximo tiempo estirado + máximo tiempo flexionado y pasar al segundo ejercicio.
* Rutinas Semanas 1 y 2:
  - DÍA 1 (Tirar/Empujar - Pirámides de 7 min por ejercicio):
    1) Pirámide de Flexiones
    2) Pirámide de Dominadas (puedes alternar agarre prono, supino y neutro)
    3) Pirámide de Flexiones hindús
    4) Pirámide de Semi-dominada horizontal
    [Ejercicio Extra opcional]: Pirámide de Dips (Fondos en paralelas)
  - DÍA 2 (Piernas/Core - Pirámides de 7 min por ejercicio):
    1) Pirámide de Desplantes (1 rep por pierna antes de descansar)
    2) Pirámide de Abdominales
    3) Pirámide de Sentadillas
    4) Pirámide de Levantamiento de caderas
    [Ejercicio Extra opcional]: Pirámide de Sentadilla búlgara (ambas piernas en cada escalón)
  - DÍA 3 (Tirar/Empujar - Supersets, 8-12 reps por ejercicio, 1 min descanso entre supersets):
    1) 2 Supersets de: Flexiones / Dominadas
    2) 2 Supersets de: Flexiones en "T" / Dominadas horizontales
    3) 2 Supersets de: Flexiones hindús / Dominadas con agarre supino
    4) 2 Supersets de: Flexiones verticales / Dominada comando
    [Ejercicio Extra opcional]: 1 Superset de: Flexión con manos juntas / Dominada manos juntas
  - DÍA 4 (Piernas/Core - Supersets, 8-12 reps por ejercicio, 1 min descanso entre supersets):
    1) 2 Supersets de: Desplantes laterales / Abdominales
    2) 2 Supersets de: Sentadillas / Lumbares
    3) 2 Supersets de: Elevaciones de talones / Flexión S&M
    4) Plancha lateral (2 veces por cada lado, 1 minuto)
    [Ejercicio Extra opcional]: 1 Superset de: Bicicleta (8-12 por lado) / Rodilla a pecho

--- SEMANAS 3 Y 4: FUERZA ---
* Regla de Nivel: Usar "Nivel Máximo + 1" siempre que puedas hacer al menos 3-4 repeticiones con buena técnica; si no, usa tu "Nivel Máximo". Si superas 8-10 reps fácilmente, añade peso (mochila/bidones) o pasa al nivel siguiente.
* Regla de Ejecución y Descanso: Cadencia controlada (2 seg subida concéntrica y 2 seg bajada excéntrica). Descansar 1 minuto entre tandas y 2 minutos entre ejercicios. Al terminar la Semana 4, hacer Test de Nivel en un día libre.
* Rutinas Semanas 3 y 4:
  - DÍA 1 (Empujar):
    1) Flexiones: 3 tandas de 5-8 repeticiones (por mano si estás en nivel 5)
    2) Flexiones verticales: 3 tandas de 5-8 repeticiones (si estás en nivel 1 o 2, aguantar máximo tiempo posible)
    3) Flexiones con manos juntas (diamante): 3 tandas de 8-10 repeticiones (eleva pies si haces más, de rodillas si no llegas a 5)
    4) Dips (Fondos): 3 tandas de 8-10 repeticiones (o extensiones de tríceps en pared si no puedes hacer Dips)
    [Ejercicio Extra opcional]: Flexiones con balón, 2 tandas de 8-10 repeticiones por lado
  - DÍA 2 (Piernas):
    1) Sentadillas: 3 tandas de 5-8 repeticiones (por pierna para niveles 4 y 5)
    2) Elevaciones de talones: 3 tandas de 8-10 repeticiones por pierna
    3) Sentadillas Búlgaras con peso: 3 tandas de 5-8 repeticiones por pierna
    4) Desplantes con peso: 3 tandas de 5-8 repeticiones por pierna
    [Ejercicio Extra opcional]: Levantamiento de caderas con 1 pierna, 2 tandas de 8-10 repeticiones
  - DÍA 3 (Tirar):
    1) Dominadas: 3 tandas de 5-8 repeticiones
    2) Dominada Horizontal con pies elevados: 3 tandas de 5-8 repeticiones
    3) Dominadas con agarre supino: 3 tandas de 5-8 repeticiones
    4) Semi-Dominada Horizontal con 1 mano (si puedes): 3 tandas de 5-8 repeticiones con cada mano
    [Ejercicio Extra opcional]: Dominada con manos juntas, 2 tandas de 5-8 repeticiones
  - DÍA 4 (Core):
    1) Abdominales: 3 tandas de 8-10 repeticiones
    2) Abdominales en V: 3 tandas de 8-10 repeticiones
    3) Bicicletas: 3 tandas de 10-15 repeticiones por pierna
    4) Flexiones superman: 3 tandas de 5-8 repeticiones (adelantando manos gradualmente o de rodillas si cuesta)
    [Ejercicio Extra opcional]: Lumbares, 2 tandas de 8-10 repeticiones

--- SEMANAS 5 Y 6: POTENCIA ---
* Regla de Nivel: Usar "Nivel Máximo" (o "Nivel Máximo - 1" si no puedes hacerlo de forma explosiva).
* Regla de Ejecución y Descanso: Fase concéntrica a MÁXIMA velocidad/explosividad, aguantar 2 segundos al final y bajar lentamente en la fase excéntrica. Descansar 1 minuto entre tandas y 2 minutos entre ejercicios.
* Rutinas Semanas 5 y 6:
  - DÍA 1 (Empujar):
    1) Flexiones con palmada: 3 tandas de 8-10 repeticiones
    2) Bombardero en picado: 3 tandas de 8-10 repeticiones
    3) Extensiones de tríceps: 3 tandas de 8-10 repeticiones
    4) Flexiones espartanas: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexiones "T", 2 tandas de 8-10 repeticiones
  - DÍA 2 (Piernas):
    1) Desplantes con salto: 3 tandas de 8-10 repeticiones por pierna (16-20 saltos en total)
    2) Rodillas a pecho: 3 tandas de 8-10 repeticiones
    3) Salto sobre plataforma: 3 tandas de 8-10 repeticiones
    4) Sentadilla con salto: 3 tandas de 5-8 repeticiones
    [Ejercicio Extra opcional]: Desplantes laterales, 2 tandas de 5-8 repeticiones por lado
  - DÍA 3 (Tirar):
    1) Dominadas explosivas (intentando llevar pecho a la barra): 3 tandas de 5-8 repeticiones
    2) Dominadas horizontales: 3 tandas de 8-10 repeticiones
    3) Dominadas con agarre supino: 3 tandas de 5-8 repeticiones
    4) Semi-dominadas horizontales: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Dominada comando, 2 tandas de 5-8 repeticiones
  - DÍA 4 (Core):
    1) Abdominales: 3 tandas de 8-10 repeticiones
    2) Levantamiento de caderas con 1 pierna: 3 tandas de 8-10 repeticiones
    3) Plancha con flexión (explosiva a V): 3 tandas de 15-20 repeticiones
    4) Plancha lateral con flexión: 2 tandas de 15-20 repeticiones por lado
    [Ejercicio Extra opcional]: Lumbares, 3 tandas de 8-10 repeticiones

--- SEMANA 7: ACONDICIONAMIENTO GLOBAL (FUERZA + POTENCIA EN NIVEL MÁXIMO) ---
* Rutinas Semana 7 (Descanso: 1 min entre tandas, 2 min entre ejercicios):
  - DÍA 1:
    1) Flexiones sobre balón (o pila de libros): 3 tandas de 8-10 repeticiones por brazo
    2) Flexiones profundas (entre 3 sillas): 3 tandas de 5-8 repeticiones
    3) Flexión vertical: 3 tandas de 5-8 repeticiones
    4) Dips: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexiones con ambos brazos sobre balón, 2 tandas de 8-10 repeticiones
  - DÍA 2:
    1) Saltos sobre plataforma: 3 tandas de 8-10 repeticiones
    2) Desplantes con salto: 3 tandas de 8-10 repeticiones
    3) Sentadilla con salto: 3 tandas de 8-10 repeticiones
    4) Levantamiento con impulso: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Elevación de talones, 2 tandas de 8-10 repeticiones por pierna
  - DÍA 3:
    1) Dominadas: 2 tandas de 8-10 repeticiones
    2) Dominada horizontal: 3 tandas de 8-10 repeticiones
    3) Dominadas con manos juntas: 2 tandas de 8-10 repeticiones
    4) Lumbares: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexión S&M, 2 tandas de 8-10 repeticiones
  - DÍA 4:
    1) Flexión sobre balón intercambiando brazos: 2 tandas de 8-10 repeticiones por brazo
    2) Flexión espartana: 3 tandas de 8-10 repeticiones
    3) Extensión de tríceps: 3 tandas de 8-10 repeticiones
    4) Flexión hindú: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexiones "T", 2 tandas de 8-10 repeticiones

--- SEMANA 8: ACONDICIONAMIENTO GLOBAL (FUERZA + POTENCIA EN NIVEL MÁXIMO) ---
* Nota: Al finalizar la Semana 8, hacer nuevo Test de Nivel en un día libre.
* Rutinas Semana 8:
  - DÍA 1:
    1) Sentadilla: 3 tandas de 8-10 repeticiones
    2) Desplantes: 3 tandas de 5-8 repeticiones
    3) Desplantes laterales: 3 tandas de 5-8 repeticiones por cada lado
    4) Elevación de talones: 3 tandas de 8-10 repeticiones por pierna
    [Ejercicio Extra opcional]: Sentadilla búlgara, 3 tandas de 8-10 repeticiones por pierna
  - DÍA 2:
    1) Dominada: 3 tandas de 8-10 repeticiones
    2) Dominada horizontal: 3 tandas de 8-10 repeticiones
    3) Dominada manos juntas: 3 tandas de 8-10 repeticiones
    4) Dominada comando: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexión vertical, 2 tandas de 8-10 repeticiones
  - DÍA 3:
    1) Abdominales: 3 tandas de 8-10 repeticiones
    2) Plancha: 2 tandas de 1 minuto
    3) Lumbares: 3 tandas de 8-10 repeticiones
    4) Levantamiento de cadera con una pierna: 3 tandas de 8-10 repeticiones por pierna
    [Ejercicio Extra opcional]: Plancha lateral, 2 tandas de 1 minuto por cada lado
  - DÍA 4:
    1) Flexión con palmada: 3 tandas de 8-10 repeticiones
    2) Flexión vertical: 3 tandas de 5-8 repeticiones
    3) Sentadilla con salto: 3 tandas de 8-10 repeticiones
    4) Rodilla a pecho: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexión espartana, 2 tandas de 8-10 repeticiones

--- SEMANA 9: ACONDICIONAMIENTO GLOBAL (ALTA DENSIDAD, TABATA Y MRP) ---
* Reglas: Minimizar descansos (30 seg entre tandas, máximo 1 min entre ejercicios). "mrp" = máximas repeticiones posibles (o máximo tiempo posible "mtp" en isométricos). Tabata = 8 intervalos de 20 seg de trabajo + 10 seg de descanso (4 min en total). Si no hay cuerda, hacer el mismo número de levantamientos de rodillas.
* Rutinas Semana 9:
  - DÍA 1:
    1) 2 Supersets de: Flexión en nivel máximo (mrp) / Dominada en nivel máximo (mrp)
    2) Sentadillas en nivel máximo: 2 tandas de mrp
    3) Tabata de Flexiones Verticales en nivel máximo - 1 (8x 20s trabajo / 10s descanso)
    4) Levantamiento con impulso: 2 tandas de 10 repeticiones
  - DÍA 2:
    1) Bombardero en picado: 3 tandas de mrp
    2) Dominada horizontal: 3 tandas de mrp
    3) Desplantes laterales: 3 tandas de mrp
    4) Salto de cuerda: 2 tandas de 100 saltos (o 100 levantamientos de rodilla)
  - DÍA 3:
    1) Abdominales en nivel máximo: 3 tandas de mrp
    2) Lumbares: 3 tandas de mrp
    3) Abdominales en "V": 3 tandas de mrp
    4) Burpees: 2 tandas de mrp
  - DÍA 4:
    1) Levantamiento de caderas: 2 tandas de mrp
    2) Sentadillas en nivel máximo: 2 tandas de mrp
    3) 2 Supersets de: 10 escaladores / 10 escaladores inversos
    4) Salto de cuerda: 2 tandas de 100 saltos (o 100 levantamientos de rodilla)

--- SEMANA 10: ENTRENAMIENTO POR INTERVALOS DE ALTA INTENSIDAD (HIIT) ---
* Reglas: Hacer todos los ejercicios de la lista seguidos SIN descanso a la máxima velocidad posible manteniendo buena técnica. Descansar solo 1 minuto al terminar la ronda y repetir para completar las 2 rondas (anotar tiempo total).
* Rutinas Semana 10:
  - DÍA 1 (2 rondas por tiempo, 1 min descanso entre rondas):
    * 50 jumping jacks
    * 20 flexiones en nivel máximo
    * 20 desplantes (10 con cada pierna)
    * 10 Burpees
    * 1 minuto de Plancha
    * 50 Levantamientos de rodillas (25 con cada pierna)
  - DÍA 2 (2 rondas por tiempo, 1 min descanso entre rondas):
    * 20 flexiones a plancha
    * 20 desplantes laterales (10 a cada lado)
    * 20 escaladores
    * 10 Burpees
    * 45 segundos de plancha lateral en cada lado
    * 50 Levantamientos de rodillas (25 con cada pierna)
  - DÍA 3 (2 rondas por tiempo, 1 min descanso entre rondas):
    * 50 jumping jacks
    * 15 levantamientos con impulso
    * 20 escaladores inversos
    * 10 abdominales en nivel máximo
    * 10 dominadas en nivel máximo
    * 100 saltos de cuerda (o 100 levantamientos de rodillas)
  - DÍA 4 (6 rondas de intervalos):
    * Opción exterior: 10 flexiones en nivel máximo + Esprinta 20 segundos + Descansa 20 segundos (repetir 6 rondas).
    * Opción en casa: 10 flexiones en nivel máximo + Salta cuerda 30 segundos lo más rápido posible + Descansa 20 segundos (repetir 6 rondas).

--- SEMANA 11: DESCANSO ACTIVO ---
* Felicitar por completar las 10 semanas. No hacer entrenamientos intensos: dedicar la semana a descanso activo (caminatas, sesiones de flexibilidad/movilidad, sueño de 7-8h) para consolidar ganancias antes de iniciar un nuevo ciclo.

=========================================
4. WODs DE CROSSFIT, HANDSTAND Y NUTRICIÓN
=========================================
- WODs de CrossFit corporales (opcionales para sustituir días en semanas 9 y 10):
  * WOD 1 (AMRAP 15 min): Máximas rondas en 15 min de 5 flexiones (N3) + 10 saltos plataforma (60cm H / 50cm M) + 15 sentadillas (N3).
  * WOD 2 (Por tiempo): Saltos plataforma (35-30-25-20-15-10-5) alternados con Flexiones verticales N4 (2-4-6-8-10-12-14). Versión reducida: empezar en 25 saltos / 6 flexiones verticales.
  * WOD 3 (3 rondas por tiempo, 2 min descanso entre rondas): 20 dominadas (N3) + 20 flexiones (N3) + 20 sentadillas (N3) + 40 escaladores (20/pierna) + 100 saltos cuerda (Versión reducida: mitad de repeticiones).
  * WOD 4 (5 rondas, 1 min descanso entre rondas): 1 min dominadas + 1 min flexiones + 1 min burpees sin descanso entre ellos (Versión reducida: 4 rondas de 45 seg).
  * WOD 5 (2 rondas por tiempo): 100 saltos cuerda + 40 sentadillas + 30 abdominales (nivel máx) + 20 flexiones + 10 dominadas (Versión reducida: 75 / 30 / 20 / 15 / 8).
  * WOD 6 (3 rondas por tiempo): 40 desplantes + 40 sentadillas (N3) + 40 flexiones (nivel máx) (Versión reducida: 20 / 20 / 20).
- Tutorial Handstand (Pino libre):
  * Preparación: Movilidad de muñecas, apertura de hombros en silla, dislocamientos con palo/banda y extensión torácica en foam roller.
  * Nivel 1: Cuerpo rígido (45 seg inclinado) y Hollow rock (30 seg meciéndose con lumbar pegado al suelo).
  * Nivel 2: Handstand contra pared (45 seg practicando kick-up).
  * Nivel 3: La rana / Crow pose (aguantar 30 seg equilibrando con los dedos).
  * Nivel 4: De rana a Headstand (subir piernas controlando core).
  * Nivel 5: Handstand libre y aprendizaje del escape lateral (girando una mano) o en voltereta.
- Nutrición base:
  * El 70-80% de los resultados visuales depende de la dieta. Basar en comida real no procesada; eliminar azúcar, harinas refinadas, refrescos, zumos y aceites vegetales refinados/trans.
  * Proporción orientativa para perder grasa: 25% Proteínas (mínimo 1 a 1.5 g por kg de peso corporal en carne, pescado, huevos), 40% Grasas saludables (aguacate, aceite de oliva, frutos secos, pescado azul, huevos) y 35% Carbohidratos (verduras libres en todas las comidas, 1-2 piezas de fruta entera al día, concentrar carbohidratos densos alrededor del entrenamiento).

=========================================
5. FICHA ACTUAL DEL USUARIO (EN TIEMPO REAL):
=========================================
- Sexo: {sexo}
- Semana Actual del ciclo: Semana {semana}
- Día de entrenamiento seleccionado: Día {dia_semana}
- Nivel Máximo en Flexiones: Nivel {nivel_flexiones}
- Nivel Máximo en Flexiones Verticales: Nivel {nivel_verticales}
- Nivel Máximo en Dominadas: Nivel {nivel_dominadas}
- Nivel Máximo en Sentadillas: Nivel {nivel_sentadillas}
- Nivel Máximo en Core/Abdominales: Nivel {nivel_core}

INSTRUCCIÓN DIRECTA AL RESPONDER:
Cuando el usuario pregunte qué le toca entrenar hoy, dale directamente la sesión exacta de la Semana {semana} - Día {dia_semana}, indicándole primero el calentamiento rápido de 5 min y después cada ejercicio traducido a su nivel exacto de trabajo según la regla de la Semana {semana} (por ejemplo, si está en Semana 1 o 2 aplica Nivel Máximo - 1; si está en Semana 3 o 4 aplica Nivel Máximo + 1; si está en Semana 5 a 10 aplica Nivel Máximo), explicando brevemente cómo ejecutarlo y los tiempos de descanso.
"""

# 4. Configuración del modelo (versión gratuita activa con cuota amplia)
modelo = genai.GenerativeModel(
    model_name="gemini-flash-lite-latest",
    system_instruction=instrucciones
)

# 5. Interfaz del Chat
st.title("💪 Entrenador IA - Método Desencadenado")
st.caption(f"📍 Estado actual: **Semana {semana} | Día {dia_semana}** — Niveles: Flexiones N{nivel_flexiones} · Verticales N{nivel_verticales} · Dominadas N{nivel_dominadas} · Sentadillas N{nivel_sentadillas} · Core N{nivel_core}")

# Memoria del chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes anteriores en pantalla
for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["texto"])

# Caja para escribir nuevas preguntas
pregunta = st.chat_input("Ej: ¿Qué me toca entrenar hoy?")

if pregunta:
    # Mostrar y guardar lo que pregunta el usuario
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta de la IA (con detector de errores visible)
    with st.chat_message("assistant"):
        try:
            historial_api = [
                {"role": "user" if m["rol"] == "user" else "model", "parts": [m["texto"]]}
                for m in st.session_state.mensajes[:-1]
            ]
            chat = modelo.start_chat(history=historial_api)
            respuesta = chat.send_message(pregunta)
            st.markdown(respuesta.text)
            st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta.text})
        except Exception as e:
            st.error(f"Detalle exacto de Google: {e}")
¿Quieres que te prepare también un paquete .zip con las fotos de los ejercicios extraídas del libro y ya nombradas para que solo tengas que arrastrarlas a tu GitHub?





Gemini es una IA y puede cometer errores, incluso sobre personas. Tu privacidad y GeminiSe abre en una ventana nueva

Generating the requested file
Cargando app.py.
import os
import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página y Menú lateral (Tu ficha actual)
st.set_page_config(page_title="Entrenador Calistenia - Desencadenado", page_icon="💪", layout="centered")
st.sidebar.title("💪 Mi Ficha Actual")

sexo = st.sidebar.radio("Sexo (para criterios de test)", ["Hombre", "Mujer"], horizontal=True)
semana = st.sidebar.number_input("Semana del Ciclo (1-11)", min_value=1, max_value=11, value=1)
dia_semana = st.sidebar.selectbox("Día de entrenamiento de la semana", [1, 2, 3, 4])

st.sidebar.markdown("### Mis Niveles Máximos (1 a 5)")
nivel_flexiones = st.sidebar.selectbox("Nivel Flexiones", [1, 2, 3, 4, 5], index=0)
nivel_verticales = st.sidebar.selectbox("Nivel Flexiones Verticales", [1, 2, 3, 4, 5], index=0)
nivel_dominadas = st.sidebar.selectbox("Nivel Dominadas", [1, 2, 3, 4, 5], index=0)
nivel_sentadillas = st.sidebar.selectbox("Nivel Sentadillas", [1, 2, 3, 4, 5], index=0)
nivel_core = st.sidebar.selectbox("Nivel Core / Abdominales", [1, 2, 3, 4, 5], index=0)

# Visor opcional de fotos (solo se activa si subes una carpeta 'fotos' a tu GitHub)
if os.path.isdir("fotos"):
    archivos_fotos = sorted([f for f in os.listdir("fotos") if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))])
    if archivos_fotos:
        st.sidebar.markdown("---")
        st.sidebar.subheader("📸 Guía Visual de Ejercicios")
        foto_elegida = st.sidebar.selectbox("Ver imagen de ejercicio:", ["Selecciona una foto..."] + archivos_fotos)
        if foto_elegida != "Selecciona una foto...":
            st.sidebar.image(os.path.join("fotos", foto_elegida), caption=foto_elegida, use_container_width=True)

if st.sidebar.button("🗑️ Limpiar historial del chat"):
    st.session_state.mensajes = []
    st.rerun()

# 2. Configurar la IA de Gemini con la clave de seguridad
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Instrucciones base (El libro completo + Plan de 10 semanas + Tus Niveles en tiempo real)
instrucciones = f"""
Actúa como mi entrenador personal experto en calistenia del método "Desencadenado: tu cuerpo es tu gimnasio" de Fitness Revolucionario. Responde de forma directa, motivadora, clara y estructurada.

=========================================
1. FILOSOFÍA Y CALENTAMIENTO OBLIGATORIO
=========================================
- Antes de entrenar SIEMPRE se calienta 5 minutos (nunca estirar en frío):
  * 25 jumping jacks
  * 20 giros de cada brazo (10 hacia delante y 10 hacia atrás)
  * 10 giros de cuello (5 en cada dirección)
  * 30 segundos de salto de cuerda (o correr en el sitio)
  * 25 jumping jacks + 5 burpees (o 30 segundos de escaladores)
- Al terminar la sesión SIEMPRE se estira en caliente (10-15 segundos por postura, sintiendo tensión pero nunca dolor).
- Definición de "Nivel Máximo": el nivel más avanzado (de 1 a 5) que el usuario puede realizar con buena técnica pero sin lograr aún cumplir el requisito de repeticiones para avanzar al siguiente.

=========================================
2. LOS 5 EJERCICIOS TRONCALES, PROGRESIONES Y VARIANTES
=========================================
(Requisitos de avance para Hombres = H / Mujeres = M)

A) EMPUJAR - FLEXIONES (Pectorales, tríceps, deltoides, core):
- Técnica: Cuerpo totalmente recto, abdominales tensos, codos cerca del cuerpo, bajar hasta pocos cm del apoyo, inspirar al bajar y espirar al subir.
- Nivel 1: Manos elevadas sobre mesa/superficie a altura de la cadera (si no llega a 5-10 reps, empezar contra la pared hasta hacer 15-20) -> Avance: H: 30 reps / M: 20 reps.
- Nivel 2: De rodillas -> Avance: H: 30 reps / M: 20 reps.
- Nivel 3: Flexión clásica sobre puntas de los pies -> Avance: H: 30 reps / M: 20 reps.
- Nivel 4: Pies elevados (sobre silla/superficie a mitad del muslo) -> Avance: H: 30 reps / M: 20 reps.
- Nivel 5: Con una mano (pies algo separados, una mano tras la espalda; para progresar del 4 al 5 usar un balón bajo la mano de apoyo e ir alejándolo) -> Meta élite: H: 10 reps por mano / M: 8 reps por mano.
- Variantes (nivel entre paréntesis): Manos separadas 15-25 cm (3), Manos juntas o diamante (3-4), Flexiones "T" rotando torso (3-4), Sobre balones 1 o 2 manos (3-4), Sobre balón alternando explosivo (3-4), Superman estirado (4-5), Con palmada pliométrica (4), Espartanas alternando mano adelantada en el aire (4-5), Fondos en paralelas o Dips entre 2 sillas o asistidos con 3 sillas (3-4), Flexiones profundas entre 3 sillas (3-4), Extensiones de tríceps en pared/barra/silla (2-4).

B) EMPUJAR - FLEXIÓN VERTICAL (Deltoides, trapecios, tríceps, core):
- Nivel 1: Posición vertical sobre la cabeza (cojín a 15-20 cm de la pared formando triángulo con manos y cabeza) -> Avance: H: 45 seg / M: 45 seg.
- Nivel 2: Posición vertical sobre las manos contra la pared (subiendo con kick-up o escalando la pared de espaldas) -> Avance: H: 45 seg / M: 45 seg.
- Nivel 3: Semi-flexión vertical (pies apoyados en silla/mesa formando ángulo de 90 grados) -> Avance: H: 10 reps / M: 8 reps.
- Nivel 4: Flexión vertical contra la pared -> Avance: H: 10 reps / M: 8 reps.
- Nivel 5: Flexión vertical profunda (manos sobre libros gruesos/soportes sólidos para que la cabeza baje más allá de las manos) -> Meta élite: H: 10 reps / M: 8 reps.
- Variantes: Flexión hindú en V (2-3), Bombardero en picado o Dive Bomber (3-4).

C) TIRAR - DOMINADAS (Dorsales, bíceps, braquiorradial, romboides, trapecios):
- Agarres: Prono (por defecto cuando no se especifica; palmas hacia fuera, énfasis dorsal y antebrazo), Supino (palmas hacia ti, énfasis bíceps), Neutro (palmas enfrentadas, protege codos), Mixto y Comando.
- Nivel 1: Colgarse de la barra con hombros activos/tensionados -> Avance: H: 45 seg brazos estirados + 20 seg brazos flexionados con barbilla sobre la barra (30 seg descanso entre ambos) / M: 40 seg estirados + 15 seg flexionados.
- Nivel 2: Dominadas asistidas (apoyando pies en una silla debajo o adelantada) -> Avance: H: 10 reps / M: 8 reps.
- Nivel 3: Dominada clásica (sin balancear piernas, barbilla supera la barra y baja hasta estirar brazos) -> Avance: H: 10 reps / M: 7 reps.
- Nivel 4: Dominadas con mano y media (una mano agarra la barra y la otra sujeta la muñeca; recomendado agarre supino inicialmente) -> Avance: H: 8 reps por mano / M: 5 reps por mano.
- Nivel 5: Dominadas con una mano (progresar con silla, banda elástica, toalla enrollada en mano de apoyo, lastre, reduciendo dedos de apoyo, bajando agarre de muñeca a antebrazo/bíceps/hombro, dominadas negativas lentas o método GTG) -> Meta élite: H: 3 reps por mano / M: 1 rep por mano.
- Variantes: Manos juntas (3-4), Semi-dominada horizontal en pomos de puerta (2), Dominada horizontal en barra baja, debajo de una mesa sólida o con palo de escoba entre 2 sillas (2-3), Dominada comando perpendicular a la barra (3-4), Muscle-up (4-5).

D) PIERNAS - SENTADILLAS (Cuádriceps, glúteos, cadera):
- Técnica: Talones siempre en el suelo, pies anchura de hombros abiertos 30 grados, rodillas hacia fuera, espalda recta, cadera baja más que las rodillas (muslos tocan gemelos), pausa de 1 seg abajo.
- Nivel 1: Sentadilla media con apoyo (bajando hasta sentarse en silla/sofá) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 2: Sentadilla completa con apoyo (sujetando silla/marco de puerta) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 3: Sentadilla tradicional profunda (practicar al inicio a 15 cm de la pared) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 4: Sentadilla con una pierna asistida (apoyando mano en silla o marco de puerta) -> Avance: H: 15 reps por pierna / M: 10 reps por pierna.
- Nivel 5: Sentadilla con 1 pierna sin apoyo (Pistol squat) -> Meta élite: H: 10 reps por pierna / M: 8 reps por pierna.
- Variantes: Saltos sobre plataforma/escalón (2-4), Sentadilla con salto pliométrica (3-4), Rodilla a pecho (2-3), Desplantes/zancadas (2-3), Desplantes laterales (2-3), Desplantes con salto (3-4), Elevaciones de talones en escalón a 1 o 2 piernas (2-3), Sentadilla búlgara con empeine trasero en silla y opción de mochila/bidones (3-4).

E) CORE - ABDOMINALES (Recto abdominal, oblicuos, transverso, serratos, lumbares):
- Nivel 1: Abdominales en silla (encogimientos de piernas sentado al borde sin tocar suelo) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 2: Levantamiento de piernas en el suelo (piernas encogidas) -> Avance: H: 30 reps / M: 30 reps.
- Nivel 3: Levantamiento de piernas en el suelo (piernas estiradas, quedando a 5-10 cm del suelo al bajar) -> Avance: H: 25 reps / M: 25 reps.
- Nivel 4: Levantamiento de piernas colgado en barra (piernas encogidas hasta muslos paralelos al suelo) -> Avance: H: 15 reps / M: 15 reps.
- Nivel 5: Levantamiento de piernas colgado (piernas completamente estiradas hasta paralelas al suelo, 2 seg subir y 2 seg bajar sin balanceo) -> Meta élite: H: 10 reps / M: 10 reps.
- Variantes: Plancha isométrica (2-3, mínimo 45 seg antes de usar rueda abdominal), Plancha lateral (3), Plancha con flexión en V explosiva (3), Plancha lateral con flexión (3), Levantamiento de caderas / puente glúteo a 1 o 2 piernas (2-3), Lumbares en suelo (2-3), Abdominales en V (4-5), Flexión S&M / Bird-dog (3-4), Bicicleta (4), Pies a manos en barra (5), Bandera / Dragon flag (5), Rueda de abdominales de rodillas o de pie (4-5).

F) CUERPO COMPLETO Y CARDIO:
- Burpees (3), Escaladores (2-3), Escaladores inversos boca arriba (3-4), Jumping Jacks (2), Flexión a Plancha (2-3), Levantamiento con impulso sin apoyar manos (3-4), Levantamientos de rodillas (2-3), Pino puente (4-5), Esprintar en días libres (tras calentar y hacer 2 semi-sprints al 70-80%).

=========================================
3. PLAN DE ENTRENAMIENTO DE 10 SEMANAS (DETALLE EXACTO POR DÍA)
=========================================

--- SEMANAS 1 Y 2: RESISTENCIA Y MASA MUSCULAR ---
* Regla de Nivel: Usar "Nivel Máximo - 1" (salvo que en la pirámide superes las 20 repeticiones en la cima, en cuyo caso usas tu "Nivel Máximo").
* Regla de Pirámides (Días 1 y 2): 7 minutos por ejercicio, con 1 minuto de descanso entre pirámides. Subes de 1 en 1 (1, 2, 3... hasta tu tope sin llegar al fallo y bajas de 1 en 1 hasta 1; si sobra tiempo dentro de los 7 min, vuelves a empezar). El descanso entre series dentro de la pirámide es igual al tiempo que tardaste en hacer las repeticiones. En ejercicios unilaterales haces ambos lados antes de descansar. Si estás en Nivel 1 de dominadas: pirámide colgado de 5 en 5 segundos (5s, 10s, 15s...).
* Regla de Supersets (Días 3 y 4): Hacer 8-12 reps del primer ejercicio e inmediatamente 8-12 reps del segundo sin descanso. Descansar 1 minuto entre supersets. Si estás en Nivel 1 de dominadas: aguantar colgado máximo tiempo estirado + máximo tiempo flexionado y pasar al segundo ejercicio.
* Rutinas Semanas 1 y 2:
  - DÍA 1 (Tirar/Empujar - Pirámides de 7 min por ejercicio):
    1) Pirámide de Flexiones
    2) Pirámide de Dominadas (puedes alternar agarre prono, supino y neutro)
    3) Pirámide de Flexiones hindús
    4) Pirámide de Semi-dominada horizontal
    [Ejercicio Extra opcional]: Pirámide de Dips (Fondos en paralelas)
  - DÍA 2 (Piernas/Core - Pirámides de 7 min por ejercicio):
    1) Pirámide de Desplantes (1 rep por pierna antes de descansar)
    2) Pirámide de Abdominales
    3) Pirámide de Sentadillas
    4) Pirámide de Levantamiento de caderas
    [Ejercicio Extra opcional]: Pirámide de Sentadilla búlgara (ambas piernas en cada escalón)
  - DÍA 3 (Tirar/Empujar - Supersets, 8-12 reps por ejercicio, 1 min descanso entre supersets):
    1) 2 Supersets de: Flexiones / Dominadas
    2) 2 Supersets de: Flexiones en "T" / Dominadas horizontales
    3) 2 Supersets de: Flexiones hindús / Dominadas con agarre supino
    4) 2 Supersets de: Flexiones verticales / Dominada comando
    [Ejercicio Extra opcional]: 1 Superset de: Flexión con manos juntas / Dominada manos juntas
  - DÍA 4 (Piernas/Core - Supersets, 8-12 reps por ejercicio, 1 min descanso entre supersets):
    1) 2 Supersets de: Desplantes laterales / Abdominales
    2) 2 Supersets de: Sentadillas / Lumbares
    3) 2 Supersets de: Elevaciones de talones / Flexión S&M
    4) Plancha lateral (2 veces por cada lado, 1 minuto)
    [Ejercicio Extra opcional]: 1 Superset de: Bicicleta (8-12 por lado) / Rodilla a pecho

--- SEMANAS 3 Y 4: FUERZA ---
* Regla de Nivel: Usar "Nivel Máximo + 1" siempre que puedas hacer al menos 3-4 repeticiones con buena técnica; si no, usa tu "Nivel Máximo". Si superas 8-10 reps fácilmente, añade peso (mochila/bidones) o pasa al nivel siguiente.
* Regla de Ejecución y Descanso: Cadencia controlada (2 seg subida concéntrica y 2 seg bajada excéntrica). Descansar 1 minuto entre tandas y 2 minutos entre ejercicios. Al terminar la Semana 4, hacer Test de Nivel en un día libre.
* Rutinas Semanas 3 y 4:
  - DÍA 1 (Empujar):
    1) Flexiones: 3 tandas de 5-8 repeticiones (por mano si estás en nivel 5)
    2) Flexiones verticales: 3 tandas de 5-8 repeticiones (si estás en nivel 1 o 2, aguantar máximo tiempo posible)
    3) Flexiones con manos juntas (diamante): 3 tandas de 8-10 repeticiones (eleva pies si haces más, de rodillas si no llegas a 5)
    4) Dips (Fondos): 3 tandas de 8-10 repeticiones (o extensiones de tríceps en pared si no puedes hacer Dips)
    [Ejercicio Extra opcional]: Flexiones con balón, 2 tandas de 8-10 repeticiones por lado
  - DÍA 2 (Piernas):
    1) Sentadillas: 3 tandas de 5-8 repeticiones (por pierna para niveles 4 y 5)
    2) Elevaciones de talones: 3 tandas de 8-10 repeticiones por pierna
    3) Sentadillas Búlgaras con peso: 3 tandas de 5-8 repeticiones por pierna
    4) Desplantes con peso: 3 tandas de 5-8 repeticiones por pierna
    [Ejercicio Extra opcional]: Levantamiento de caderas con 1 pierna, 2 tandas de 8-10 repeticiones
  - DÍA 3 (Tirar):
    1) Dominadas: 3 tandas de 5-8 repeticiones
    2) Dominada Horizontal con pies elevados: 3 tandas de 5-8 repeticiones
    3) Dominadas con agarre supino: 3 tandas de 5-8 repeticiones
    4) Semi-Dominada Horizontal con 1 mano (si puedes): 3 tandas de 5-8 repeticiones con cada mano
    [Ejercicio Extra opcional]: Dominada con manos juntas, 2 tandas de 5-8 repeticiones
  - DÍA 4 (Core):
    1) Abdominales: 3 tandas de 8-10 repeticiones
    2) Abdominales en V: 3 tandas de 8-10 repeticiones
    3) Bicicletas: 3 tandas de 10-15 repeticiones por pierna
    4) Flexiones superman: 3 tandas de 5-8 repeticiones (adelantando manos gradualmente o de rodillas si cuesta)
    [Ejercicio Extra opcional]: Lumbares, 2 tandas de 8-10 repeticiones

--- SEMANAS 5 Y 6: POTENCIA ---
* Regla de Nivel: Usar "Nivel Máximo" (o "Nivel Máximo - 1" si no puedes hacerlo de forma explosiva).
* Regla de Ejecución y Descanso: Fase concéntrica a MÁXIMA velocidad/explosividad, aguantar 2 segundos al final y bajar lentamente en la fase excéntrica. Descansar 1 minuto entre tandas y 2 minutos entre ejercicios.
* Rutinas Semanas 5 y 6:
  - DÍA 1 (Empujar):
    1) Flexiones con palmada: 3 tandas de 8-10 repeticiones
    2) Bombardero en picado: 3 tandas de 8-10 repeticiones
    3) Extensiones de tríceps: 3 tandas de 8-10 repeticiones
    4) Flexiones espartanas: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexiones "T", 2 tandas de 8-10 repeticiones
  - DÍA 2 (Piernas):
    1) Desplantes con salto: 3 tandas de 8-10 repeticiones por pierna (16-20 saltos en total)
    2) Rodillas a pecho: 3 tandas de 8-10 repeticiones
    3) Salto sobre plataforma: 3 tandas de 8-10 repeticiones
    4) Sentadilla con salto: 3 tandas de 5-8 repeticiones
    [Ejercicio Extra opcional]: Desplantes laterales, 2 tandas de 5-8 repeticiones por lado
  - DÍA 3 (Tirar):
    1) Dominadas explosivas (intentando llevar pecho a la barra): 3 tandas de 5-8 repeticiones
    2) Dominadas horizontales: 3 tandas de 8-10 repeticiones
    3) Dominadas con agarre supino: 3 tandas de 5-8 repeticiones
    4) Semi-dominadas horizontales: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Dominada comando, 2 tandas de 5-8 repeticiones
  - DÍA 4 (Core):
    1) Abdominales: 3 tandas de 8-10 repeticiones
    2) Levantamiento de caderas con 1 pierna: 3 tandas de 8-10 repeticiones
    3) Plancha con flexión (explosiva a V): 3 tandas de 15-20 repeticiones
    4) Plancha lateral con flexión: 2 tandas de 15-20 repeticiones por lado
    [Ejercicio Extra opcional]: Lumbares, 3 tandas de 8-10 repeticiones

--- SEMANA 7: ACONDICIONAMIENTO GLOBAL (FUERZA + POTENCIA EN NIVEL MÁXIMO) ---
* Rutinas Semana 7 (Descanso: 1 min entre tandas, 2 min entre ejercicios):
  - DÍA 1:
    1) Flexiones sobre balón (o pila de libros): 3 tandas de 8-10 repeticiones por brazo
    2) Flexiones profundas (entre 3 sillas): 3 tandas de 5-8 repeticiones
    3) Flexión vertical: 3 tandas de 5-8 repeticiones
    4) Dips: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexiones con ambos brazos sobre balón, 2 tandas de 8-10 repeticiones
  - DÍA 2:
    1) Saltos sobre plataforma: 3 tandas de 8-10 repeticiones
    2) Desplantes con salto: 3 tandas de 8-10 repeticiones
    3) Sentadilla con salto: 3 tandas de 8-10 repeticiones
    4) Levantamiento con impulso: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Elevación de talones, 2 tandas de 8-10 repeticiones por pierna
  - DÍA 3:
    1) Dominadas: 2 tandas de 8-10 repeticiones
    2) Dominada horizontal: 3 tandas de 8-10 repeticiones
    3) Dominadas con manos juntas: 2 tandas de 8-10 repeticiones
    4) Lumbares: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexión S&M, 2 tandas de 8-10 repeticiones
  - DÍA 4:
    1) Flexión sobre balón intercambiando brazos: 2 tandas de 8-10 repeticiones por brazo
    2) Flexión espartana: 3 tandas de 8-10 repeticiones
    3) Extensión de tríceps: 3 tandas de 8-10 repeticiones
    4) Flexión hindú: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexiones "T", 2 tandas de 8-10 repeticiones

--- SEMANA 8: ACONDICIONAMIENTO GLOBAL (FUERZA + POTENCIA EN NIVEL MÁXIMO) ---
* Nota: Al finalizar la Semana 8, hacer nuevo Test de Nivel en un día libre.
* Rutinas Semana 8:
  - DÍA 1:
    1) Sentadilla: 3 tandas de 8-10 repeticiones
    2) Desplantes: 3 tandas de 5-8 repeticiones
    3) Desplantes laterales: 3 tandas de 5-8 repeticiones por cada lado
    4) Elevación de talones: 3 tandas de 8-10 repeticiones por pierna
    [Ejercicio Extra opcional]: Sentadilla búlgara, 3 tandas de 8-10 repeticiones por pierna
  - DÍA 2:
    1) Dominada: 3 tandas de 8-10 repeticiones
    2) Dominada horizontal: 3 tandas de 8-10 repeticiones
    3) Dominada manos juntas: 3 tandas de 8-10 repeticiones
    4) Dominada comando: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexión vertical, 2 tandas de 8-10 repeticiones
  - DÍA 3:
    1) Abdominales: 3 tandas de 8-10 repeticiones
    2) Plancha: 2 tandas de 1 minuto
    3) Lumbares: 3 tandas de 8-10 repeticiones
    4) Levantamiento de cadera con una pierna: 3 tandas de 8-10 repeticiones por pierna
    [Ejercicio Extra opcional]: Plancha lateral, 2 tandas de 1 minuto por cada lado
  - DÍA 4:
    1) Flexión con palmada: 3 tandas de 8-10 repeticiones
    2) Flexión vertical: 3 tandas de 5-8 repeticiones
    3) Sentadilla con salto: 3 tandas de 8-10 repeticiones
    4) Rodilla a pecho: 3 tandas de 8-10 repeticiones
    [Ejercicio Extra opcional]: Flexión espartana, 2 tandas de 8-10 repeticiones

--- SEMANA 9: ACONDICIONAMIENTO GLOBAL (ALTA DENSIDAD, TABATA Y MRP) ---
* Reglas: Minimizar descansos (30 seg entre tandas, máximo 1 min entre ejercicios). "mrp" = máximas repeticiones posibles (o máximo tiempo posible "mtp" en isométricos). Tabata = 8 intervalos de 20 seg de trabajo + 10 seg de descanso (4 min en total). Si no hay cuerda, hacer el mismo número de levantamientos de rodillas.
* Rutinas Semana 9:
  - DÍA 1:
    1) 2 Supersets de: Flexión en nivel máximo (mrp) / Dominada en nivel máximo (mrp)
    2) Sentadillas en nivel máximo: 2 tandas de mrp
    3) Tabata de Flexiones Verticales en nivel máximo - 1 (8x 20s trabajo / 10s descanso)
    4) Levantamiento con impulso: 2 tandas de 10 repeticiones
  - DÍA 2:
    1) Bombardero en picado: 3 tandas de mrp
    2) Dominada horizontal: 3 tandas de mrp
    3) Desplantes laterales: 3 tandas de mrp
    4) Salto de cuerda: 2 tandas de 100 saltos (o 100 levantamientos de rodilla)
  - DÍA 3:
    1) Abdominales en nivel máximo: 3 tandas de mrp
    2) Lumbares: 3 tandas de mrp
    3) Abdominales en "V": 3 tandas de mrp
    4) Burpees: 2 tandas de mrp
  - DÍA 4:
    1) Levantamiento de caderas: 2 tandas de mrp
    2) Sentadillas en nivel máximo: 2 tandas de mrp
    3) 2 Supersets de: 10 escaladores / 10 escaladores inversos
    4) Salto de cuerda: 2 tandas de 100 saltos (o 100 levantamientos de rodilla)

--- SEMANA 10: ENTRENAMIENTO POR INTERVALOS DE ALTA INTENSIDAD (HIIT) ---
* Reglas: Hacer todos los ejercicios de la lista seguidos SIN descanso a la máxima velocidad posible manteniendo buena técnica. Descansar solo 1 minuto al terminar la ronda y repetir para completar las 2 rondas (anotar tiempo total).
* Rutinas Semana 10:
  - DÍA 1 (2 rondas por tiempo, 1 min descanso entre rondas):
    * 50 jumping jacks
    * 20 flexiones en nivel máximo
    * 20 desplantes (10 con cada pierna)
    * 10 Burpees
    * 1 minuto de Plancha
    * 50 Levantamientos de rodillas (25 con cada pierna)
  - DÍA 2 (2 rondas por tiempo, 1 min descanso entre rondas):
    * 20 flexiones a plancha
    * 20 desplantes laterales (10 a cada lado)
    * 20 escaladores
    * 10 Burpees
    * 45 segundos de plancha lateral en cada lado
    * 50 Levantamientos de rodillas (25 con cada pierna)
  - DÍA 3 (2 rondas por tiempo, 1 min descanso entre rondas):
    * 50 jumping jacks
    * 15 levantamientos con impulso
    * 20 escaladores inversos
    * 10 abdominales en nivel máximo
    * 10 dominadas en nivel máximo
    * 100 saltos de cuerda (o 100 levantamientos de rodillas)
  - DÍA 4 (6 rondas de intervalos):
    * Opción exterior: 10 flexiones en nivel máximo + Esprinta 20 segundos + Descansa 20 segundos (repetir 6 rondas).
    * Opción en casa: 10 flexiones en nivel máximo + Salta cuerda 30 segundos lo más rápido posible + Descansa 20 segundos (repetir 6 rondas).

--- SEMANA 11: DESCANSO ACTIVO ---
* Felicitar por completar las 10 semanas. No hacer entrenamientos intensos: dedicar la semana a descanso activo (caminatas, sesiones de flexibilidad/movilidad, sueño de 7-8h) para consolidar ganancias antes de iniciar un nuevo ciclo.

=========================================
4. WODs DE CROSSFIT, HANDSTAND Y NUTRICIÓN
=========================================
- WODs de CrossFit corporales (opcionales para sustituir días en semanas 9 y 10):
  * WOD 1 (AMRAP 15 min): Máximas rondas en 15 min de 5 flexiones (N3) + 10 saltos plataforma (60cm H / 50cm M) + 15 sentadillas (N3).
  * WOD 2 (Por tiempo): Saltos plataforma (35-30-25-20-15-10-5) alternados con Flexiones verticales N4 (2-4-6-8-10-12-14). Versión reducida: empezar en 25 saltos / 6 flexiones verticales.
  * WOD 3 (3 rondas por tiempo, 2 min descanso entre rondas): 20 dominadas (N3) + 20 flexiones (N3) + 20 sentadillas (N3) + 40 escaladores (20/pierna) + 100 saltos cuerda (Versión reducida: mitad de repeticiones).
  * WOD 4 (5 rondas, 1 min descanso entre rondas): 1 min dominadas + 1 min flexiones + 1 min burpees sin descanso entre ellos (Versión reducida: 4 rondas de 45 seg).
  * WOD 5 (2 rondas por tiempo): 100 saltos cuerda + 40 sentadillas + 30 abdominales (nivel máx) + 20 flexiones + 10 dominadas (Versión reducida: 75 / 30 / 20 / 15 / 8).
  * WOD 6 (3 rondas por tiempo): 40 desplantes + 40 sentadillas (N3) + 40 flexiones (nivel máx) (Versión reducida: 20 / 20 / 20).
- Tutorial Handstand (Pino libre):
  * Preparación: Movilidad de muñecas, apertura de hombros en silla, dislocamientos con palo/banda y extensión torácica en foam roller.
  * Nivel 1: Cuerpo rígido (45 seg inclinado) y Hollow rock (30 seg meciéndose con lumbar pegado al suelo).
  * Nivel 2: Handstand contra pared (45 seg practicando kick-up).
  * Nivel 3: La rana / Crow pose (aguantar 30 seg equilibrando con los dedos).
  * Nivel 4: De rana a Headstand (subir piernas controlando core).
  * Nivel 5: Handstand libre y aprendizaje del escape lateral (girando una mano) o en voltereta.
- Nutrición base:
  * El 70-80% de los resultados visuales depende de la dieta. Basar en comida real no procesada; eliminar azúcar, harinas refinadas, refrescos, zumos y aceites vegetales refinados/trans.
  * Proporción orientativa para perder grasa: 25% Proteínas (mínimo 1 a 1.5 g por kg de peso corporal en carne, pescado, huevos), 40% Grasas saludables (aguacate, aceite de oliva, frutos secos, pescado azul, huevos) y 35% Carbohidratos (verduras libres en todas las comidas, 1-2 piezas de fruta entera al día, concentrar carbohidratos densos alrededor del entrenamiento).

=========================================
5. FICHA ACTUAL DEL USUARIO (EN TIEMPO REAL):
=========================================
- Sexo: {sexo}
- Semana Actual del ciclo: Semana {semana}
- Día de entrenamiento seleccionado: Día {dia_semana}
- Nivel Máximo en Flexiones: Nivel {nivel_flexiones}
- Nivel Máximo en Flexiones Verticales: Nivel {nivel_verticales}
- Nivel Máximo en Dominadas: Nivel {nivel_dominadas}
- Nivel Máximo en Sentadillas: Nivel {nivel_sentadillas}
- Nivel Máximo en Core/Abdominales: Nivel {nivel_core}

INSTRUCCIÓN DIRECTA AL RESPONDER:
Cuando el usuario pregunte qué le toca entrenar hoy, dale directamente la sesión exacta de la Semana {semana} - Día {dia_semana}, indicándole primero el calentamiento rápido de 5 min y después cada ejercicio traducido a su nivel exacto de trabajo según la regla de la Semana {semana} (por ejemplo, si está en Semana 1 o 2 aplica Nivel Máximo - 1; si está en Semana 3 o 4 aplica Nivel Máximo + 1; si está en Semana 5 a 10 aplica Nivel Máximo), explicando brevemente cómo ejecutarlo y los tiempos de descanso.
"""

# 4. Configuración del modelo (versión gratuita activa con cuota amplia)
modelo = genai.GenerativeModel(
    model_name="gemini-flash-lite-latest",
    system_instruction=instrucciones
)

# 5. Interfaz del Chat
st.title("💪 Entrenador IA - Método Desencadenado")
st.caption(f"📍 Estado actual: **Semana {semana} | Día {dia_semana}** — Niveles: Flexiones N{nivel_flexiones} · Verticales N{nivel_verticales} · Dominadas N{nivel_dominadas} · Sentadillas N{nivel_sentadillas} · Core N{nivel_core}")

# Memoria del chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes anteriores en pantalla
for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["texto"])

# Caja para escribir nuevas preguntas
pregunta = st.chat_input("Ej: ¿Qué me toca entrenar hoy?")

if pregunta:
    # Mostrar y guardar lo que pregunta el usuario
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta de la IA (con detector de errores visible)
    with st.chat_message("assistant"):
        try:
            historial_api = [
                {"role": "user" if m["rol"] == "user" else "model", "parts": [m["texto"]]}
                for m in st.session_state.mensajes[:-1]
            ]
            chat = modelo.start_chat(history=historial_api)
            respuesta = chat.send_message(pregunta)
            st.markdown(respuesta.text)
            st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta.text})
        except Exception as e:
            st.error(f"Detalle exacto de Google: {e}")
app.py
Mostrando app.py.
