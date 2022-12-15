import sqlite3
from time import strftime
from datetime import datetime
import logging
from queries import obtener_datos_aforo
URI = "/home/pi/Urban_Urbano/db/asignacion.db"

# Creando una tabla llamada chofer
# operacion ASIGNACION: (ASIGNACION), folio_asignacion, id_operador, id_ruta, fecha_de_asignacion, hora_de_inicio [2da geocerca]
tabla_actualizacion = '''CREATE TABLE IF NOT EXISTS actualizacion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operacion VARCHAR(100),
        fecha DATE,
        folio INTEGER,
        estado VARCHAR(100)
)'''

tabla_asignacion = '''CREATE TABLE IF NOT EXISTS asignacion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folio_asignacio INTEGER,
        id_operador INTEGER,
        id_ruta INTEGER,
        fecha_de_asignacion DATE,
        hora_de_inicio TIME,
        estado VARCHAR(100) default 'por_hacer'
)'''

tabla_auto_asignacion = '''CREATE TABLE IF NOT EXISTS auto_asignacion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folio INTEGER,
        csn_chofer VARCHAR(100),
        servicio_pension VARCHAR(100),
        fecha DATE,
        hora_inicio TIME,
        folio_de_viaje VARCHAR(100) default 'por_aniadir',
        check_servidor VARCHAR(100) default 'NO'
)'''

tabla_estado_del_viaje = '''CREATE TABLE IF NOT EXISTS estado_del_viaje (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        csn_chofer VARCHAR(100),
        servicio_pension VARCHAR(100),
        fecha DATE,
        hora_inicio TIME,
        total_de_folio_aforo_efectivo INTEGER,
        total_de_folio_aforo_tarjeta INTEGER,
        folio_de_viaje VARCHAR(100) default 'por_aniadir',
        check_servidor VARCHAR(100) default 'NO'
)'''

def crear_tabla_asignacion():
    try:
        con = sqlite3.connect(URI,check_same_thread=False)
        cur = con.cursor()
        cur.execute(tabla_asignacion)
    except Exception as e:
        print(e)
        logging.info(e)


def crear_tabla_actualizacion():
    try:
        con = sqlite3.connect(URI,check_same_thread=False)
        cur = con.cursor()
        cur.execute(tabla_actualizacion)
    except Exception as e:
        print(e)
        logging.info(e)

def crear_tabla_auto_asignacion():
    try:
        con = sqlite3.connect(URI,check_same_thread=False)
        cur = con.cursor()
        cur.execute(tabla_auto_asignacion)
    except Exception as e:
        print(e)
        logging.info(e)

def crear_tabla_estado_del_viaje():
    try:
        con = sqlite3.connect(URI,check_same_thread=False)
        cur = con.cursor()
        cur.execute(tabla_estado_del_viaje)
    except Exception as e:
        print(e)
        logging.info(e)

def guardar_asignacion(folio_asignacion, id_operador, id_ruta, fecha_de_asignacion, hora_de_inicio):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO asignacion (folio_asignacio, id_operador, id_ruta, fecha_de_asignacion, hora_de_inicio) VALUES (?, ?, ?, ?, ?)",(folio_asignacion, id_operador, id_ruta, fecha_de_asignacion, hora_de_inicio))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)


def obtener_asignaciones_de_hoy():
    try:
        con = sqlite3.connect(URI,check_same_thread=False)
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM asignacion WHERE fecha_de_asignacion = ? and estado = 'por_hacer' and hora_de_inicio > ? ORDER BY hora_de_inicio  ASC", (strftime("%Y-%m-%d"), strftime("%H:%M:%S")))
        return cur.fetchall()
    except Exception as e:
        print(e)
        logging.info(e)


def marcar_asignacion_como_cancelada(id):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE asignacion SET estado = 'cancelada' WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)


def marcar_asignacion_como_realizada(id):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE asignacion SET estado = 'realizada' WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)


def obtener_asignaciones_por_fecha(fecha):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM asignacion WHERE fecha_de_asignacion = ? and estado = 'por_hacer'", (fecha,))
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)


def guardar_auto_asignacion(id_chofer, servicio_pension, fecha, hora_inicio):
    try:
        folio = obtener_ultimo_folio_auto_asignacion()['folio']
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO auto_asignacion (folio, csn_chofer, servicio_pension, fecha, hora_inicio) VALUES (?, ?, ?, ?, ?)", (folio, id_chofer, servicio_pension, fecha, hora_inicio))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)

def aniadir_folio_de_viaje_a_auto_asignacion(folio, folio_de_viaje):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute("UPDATE auto_asignacion SET folio_de_viaje = ? WHERE folio = ?", (folio_de_viaje, folio))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)

def guardar_actualizacion(operacion, fecha, folio):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO actualizacion (operacion, fecha, folio) VALUES (?, ?, ?)", (operacion, fecha, folio))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)


def obtener_actualizacion_por_operacion_y_fecha(operacion, fecha):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM actualizacion WHERE LIKE operacion = ? AND fecha = ?", (operacion, fecha))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)

def compare_two_dates(date1, date2):
    try:
        d1 = datetime.strptime(date1, "%d/%m/%Y")
        d2 = datetime.strptime(date2, "%d/%m/%Y")
        delta = d2 - d1
        if delta.days == 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        logging.info(e)

def obtener_ultima_asignacion():
    try:
        con = sqlite3.connect(URI,check_same_thread=False)
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM auto_asignacion ORDER BY id DESC LIMIT 1")
        return cur.fetchone()
    except Exception as e:
        print(e)
        logging.info(e)
        
def obtener_primer_asignacion():
    try:
        con = sqlite3.connect(URI,check_same_thread=False)
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM auto_asignacion ORDER BY id ASC LIMIT 1")
        return cur.fetchone()
    except Exception as e:
        print(e)
        logging.info(e)
        
def obtener_primer_fin_viaje():
    try:
        con = sqlite3.connect(URI,check_same_thread=False)
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM estado_del_viaje ORDER BY id ASC LIMIT 1")
        return cur.fetchone()
    except Exception as e:
        print(e)
        logging.info(e)
        
def eliminar_auto_asignacion_por_folio(folio):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM auto_asignacion WHERE folio = ?", (folio,))
        conexion.commit()
        conexion.close()
    except Exception as e:
        print(e)
        logging.info(e)
        
def seleccionar_auto_asignaciones_antiguas():
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(f"SELECT id, fecha FROM auto_asignacion")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)
        return False
        
def eliminar_auto_asignaciones_antiguas(id):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM auto_asignacion WHERE id == {id}")
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)
        return False
    
def seleccionar_fin_de_viaje_antiguos():
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(f"SELECT id, fecha FROM estado_del_viaje")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)
        return False
        
def eliminar_fin_de_viaje_antiguos(id):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM estado_del_viaje WHERE id == {id}")
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)
        return False

def obtener_ultimo_folio_asignaciones():
    try:
        asignacion = obtener_ultima_asignacion()
        if asignacion is None:
            return {
                'folio': 1
            }
        folio = asignacion[1]
        fecha_db = asignacion[5]
        fecha_actual = strftime("%d/%m/%Y")

        if compare_two_dates(fecha_actual, fecha_db):
            return {
                'folio': folio + 1
            }
        else:
            return {
                'folio': 1
            }
    except Exception as e:
        print(e)
        logging.info(e)

def obtener_ultimo_folio_auto_asignacion():
    try:
        asignacion = obtener_ultima_asignacion()
        inicio_folio = obtener_datos_aforo()[6]
        if asignacion is None:
            return {
                'folio': f"{inicio_folio}"
            }
        folio = asignacion[1]
        fecha_db = asignacion[4].replace("-", "/")
        fecha_actual = strftime("%d/%m/%Y")

        if compare_two_dates(fecha_actual, fecha_db):
            folio = folio + 1
            return {
                'folio': folio
            }
        else:
            return {
                'folio': f"{inicio_folio}"
            }
    except Exception as e:
        print(e)
        logging.info(e)


def obtener_asignaciones_no_enviadas():
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM auto_asignacion WHERE check_servidor = 'NO' AND folio_de_viaje IS NOT 'por_aniadir' LIMIT 1")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)
        
def obtener_asignacion_por_folio_de_viaje(folio_de_viaje):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM auto_asignacion WHERE folio_de_viaje = ? LIMIT 1", (folio_de_viaje,))
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)
        
def obtener_todas_las_asignaciones_no_enviadas():
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM auto_asignacion WHERE check_servidor = 'NO' LIMIT 1")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)
        
def obtener_todass_las_asignaciones_no_enviadas():
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM auto_asignacion WHERE check_servidor = 'NO'")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)


def actualizar_asignacion_check_servidor(id):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE auto_asignacion SET check_servidor = 'OK' WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)

def guardar_estado_del_viaje(csn_chofer, servicio_pension, fecha, hora_inicio, total_de_folio_aforo_efectivo, total_de_folio_aforo_tarjeta, folio_de_viaje):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO estado_del_viaje (csn_chofer, servicio_pension, fecha, hora_inicio, total_de_folio_aforo_efectivo, total_de_folio_aforo_tarjeta, folio_de_viaje) VALUES (?, ?, ?, ?, ?, ?, ?)", (csn_chofer, servicio_pension, fecha, hora_inicio, total_de_folio_aforo_efectivo, total_de_folio_aforo_tarjeta, folio_de_viaje))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)

def actualizar_estado_del_viaje_check_servidor(id):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE estado_del_viaje SET check_servidor = 'OK' WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(e)
        logging.info(e)

def obtener_estado_de_viajes_no_enviados():
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM estado_del_viaje WHERE check_servidor = 'NO' LIMIT 1")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)
        
def obtener_fin_de_viaje_por_folio_de_viaje(folio_de_viaje):
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM estado_del_viaje WHERE folio_de_viaje = ? LIMIT 1", (folio_de_viaje,))
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)
        
def obtener_estado_de_todos_los_viajes_no_enviados():
    try:
        conexion = sqlite3.connect(URI,check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM estado_del_viaje WHERE check_servidor = 'NO'")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except Exception as e:
        print(e)
        logging.info(e)

# sql like example: SELECT * FROM actualizacion WHERE operacion LIKE '%actualizacion%'
crear_tabla_actualizacion()
crear_tabla_auto_asignacion()
crear_tabla_asignacion()
crear_tabla_estado_del_viaje()