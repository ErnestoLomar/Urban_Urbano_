# Urban_Urbano
Software de validador para camiones de transporte urbano para la empresa Urban de Tampico.

**Autor: Ernesto Lomar**

Linea cronológica:
- v1.20:
  - Solucionando problema d la lectura de tickets de la base de datos.
- v1.19:
  - Agregando la eliminación de datos antiguos que sobrepasan los 15 días.
- v1.18:
  - Agregando inicio de sesión del GPS cuando no se obtienen coordenadas.
- v1.17:
  - Añadiendo la opción de poder hacer la actualización de software mediante 2 servidores con FTP.
  - Haciendo que cuando comience el software se enciende el GPS con *AT+QGPS=1*.
  - Corrigiendo bug de cuando no se hace ninguna venta.
- v1.16:
  - Agregando candado de seguridad en el CSN al crear la trama 2.
  - Quitando enters.
  - Quitando caracteres de tarjetas leídas.
  - Agregando candado de seguridad al crear trama 4.
  - Nueva comunicación con servidor de Azure.
- v1.15:
  - Modificando estructura de la función *handle_ok* cuando se inicia un viaje.
  - Añadiendo candado de seguridad del conteo de boletos registrados en la base de datos, los que se llevan en conteo y del folio de la ultima venta realizada.
  - Quitando botón de apagar raspberry de la ventana de chofer.
  - Quitando valor por defecto en la selección de pensión.
  - Añadiendo candado de verificación de si hay un fin de viaje por enviar al servidor antes de enviar un comienzo de viaje.
  - Agregando candados de seguridad al obtener el CSN.
  - Agregando candados de seguridad del CSN al crear trama 2.
  - Agregando candado de seguridad en la creación del folio de viaje.
  - Mejorando el envío de datos cronológicamente.
  - Cambiando nombres de variables para evitar la concatenación de datos.
  - Actualizando funciones del letrero de la ventana principal de *datos pendientes por enviar*
- v1.14:
  - Modificando la comparación de vigencias de tarjeta y actual a solo fechas.
- v1.13:
  - Agregando la detección de vigencia de las tarjetas al software.
  - Cambiando el inicio de folio a 60.
  - Poniendo el label del socket de la ventana principal en la cintilla.
  - Añadiendo nueva opción de *"Fuera de vigencia"* a las ventanas emergentes.
- v1.12:
  - Agregando opción en la base de datos para que se pueda iniciar el viaje desde un folio especifico.
  - Agregando nuevas bases de datos de matrices tarifarías y servicios.
  - Agregando nuevo letrero en la ventana principal de camiones que se mostrara por si llegara a faltar enviar un dato al servidor.
  - Quitando variable "en_viaje".
  - Modificando diseño de las ventanas inicio y enviar vuelta.
  - Quitando la opción de que no dejaba cerrar turno hasta que se enviaran todos los datos al servidor.
  - Añadiendo en la ventana principal el número de socket.
  - Corrigiendo error de *"por_aniadir"*.
- v1.11:
  - Corrección de diseño de *enviar_vuelta*.
  - Arreglando glitch de cuando se cierra la ventana de chofer al no encontrar un servicio no se puede volver a meter a la misma.
- v1.10:
  - Agregando nuevas bases de datos, con nuevas matrices tarifarías, servicios, etc.
  - Nueva base de datos operadores.py.
  - Modificando diseño de ventana *enviar_vuelta*.
  - Añadiendo nombre y numero de empleado de operador en ticket de liquidación.
  - Solucionando espacio vació del UID.
  - Agregando parche para que no se dupliquen folios de ventas y no se sobrescriban en el servidor.
- v1.9:
  - Cambiando el numero de versión a variables globales.
  - Modificando query de la consulta de ventas de la petición "D".
  - Modificando las acciones de las peticiones del servidor.
  - Modificando estructura de la lectura de QR.
  - Modificando diseño de ventanas.
  - Añadiendo folio de viaje, folio de liquidación y versión del software a ticket de liquidación.
  - Modificando software para que no deje cerrar turno del operador hasta que se envíen todos los datos al servidor.
  - Arreglando bug de que el hilo de "enviar_vuelta" no se restablece al volver al restablecer la raspberry después de haber sido apagada.
  - Añadiendo nueva variable "en_viaje".
- v1.8:
  - Haciendo modificaciones en puertoSocket e idUnidad.
  - Modificando scrips de bases de datos.
  - Arreglando bug de que se truena el programa al darle doble click en el botón de terminar vuelta.
  - Agregando opción para que no se abran ventanas innecesarias.
- v1.7:
  - Mejorando la detección de la hora por SIM y GPS.
  - Modificando scripts de bases de datos.
  - Haciendo modificaciones en puertoSocket e idUnidad.
  - Agregando nuevas bases de datos
- v1.6:
  - Añadiendo verificación del tamaño del archivo que llega por FTP.
  - Añadiendo nuevo archivo "verificar_carpeta" para la detección de Urban_Urbano.
  - Mejorando la auto-actualización por FTP.
  - Modificando la lectura de transbordos.
  - Cambiando distancia minima de 0.004 a 0.003.
  - Creando nueva base de datos para los tickets usados.
  - Optimizando lectura en bases de datos.
  - Creando nuevo archivo "impresora.py" donde se concentra toda la impresión de tickets.
  - Modificando los archivos donde se imprimen tickets para que utilicen el archivo *impresora.py*
  - Añadiendo nueva base de datos.
  - Modificando el tamaño de las ventanas para que abarquen todo el espacio de la pantalla.
- v1.5:
  - Cambiando los tipo de hilos de la detección de geocercas y validación de datos de *threading* a *QThread*.
  - Corrigiendo la impresión de tickets de transbordo.
  - Haciendo más robusto el envío de datos por TCP/IP al servidor.
  - Añadiendo respuestas de las peticiones del servidor para el reenvió de datos.
  - Modificando trama 3 (envío de GNSS) para cuando no haya un viaje iniciado, se mande un 99 en el contador de folio de viaje, para así no perder coordenadas GNSS de una unidad a pesar de que no tenga folio de viaje asociado.
  - Añadiendo más información de retroalimentación al log.
  - Cambiando la reconexión al servidor cuando falla el envío de datos para que ahora solo al intento fallido 4 cierre y abra el socket y al intento 6 reinicie el módem Quectel.
  - Modificaciones del FrontEnd
- v1.4:
  - Haciendo que suene el zumbador al momento de que suceda cualquier error.
  - Priorizando el reinicio del Quectel al acumular muchos intentos fallidos de envíos de datos al servidor.
  - Cambiando diseño.
  - Mejorando condicional de conteo de datos enviados en la interfaz enviar_vuelta.
- v1.3:
  - Mejorando restablecimiento de la conexión del QR.
  - Añadiendo nuevo campo a la base de datos aforo.db donde se guardara el puerto del socket y así sera mas accesible para cambiarlo.
  - Mejorando el diseño de la ventana enviar_vuelta.
  - Optimizando el envió de datos a pesar de no contar con coordenadas GPS.
  - Optimizando la conexión de la impresora para la impresión de tickets.
- v1.2:
    - Mejorando la restauración de ventanas y datos por si llegara a ocurrir que el sistema se detenga de la nada cuando no debe.
- v1.1:
    - Mejorando la detección de geocercas.
    - Añadiendo lectura de códigos QR.
    - Optimizando código para una mayor eficiencia.
    - Añadiendo más opciones de ventanas emergentes.
    - Arreglando bugs y glitches generales que podrían afectar en lo proximo.
- v1.0:
    Sistema funcional para la venta de pasajes en transporte urbano, impresión de tickets con/sin QR, envió de datos mediante TCP/IP, auto actualizable mediante FTP y detección de geocercas.