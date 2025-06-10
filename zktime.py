# lib de conexion con zktime - hullero
from zk import ZK, const
# lib que permite la conexion con la base de datos
import pymysql
# data config hullero
IP = '192.168.100.138'
PORT = 8080
PASSWORD = 111111  # contraseña de comunicacion del hullero en este caso es 111111
 
def conexion_hullero():
    zk = ZK(IP, port=PORT, timeout=10, password=PASSWORD)
    try:
        conn = zk.connect()
        print("Conectado al hullero manito")
        conn.disable_device()
        registros = conn.get_attendance()
        usuarios = conn.get_users()
        nombres = {u.user_id: u.name for u in usuarios}

        # muestra los registros con len en numero
        print(f"Se encontraron {len(registros)} registros:\n")
        print("--------------------------------------------------------")
        # muestra la data encontrada
        # for r in registros:
        #     print(f"Usuario: {r.user_id} - Fecha y Hora: {r.timestamp} - Estado: {r.status} - Punch: {r.punch}")
        conn.enable_device()
        conn.disconnect()
        return [(r, nombres.get(r.user_id, "Desconocido")) for r in registros]
    
    except Exception as e:
        print("Error manito:", e)

# funcion para insertar data en la bd
def insertar_registros(data):
    if data == None:
        return print("No hay data para insertar")
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', database='zk_attendance')
        cursor = conn.cursor()

        sql = """
            INSERT IGNORE INTO attendance_logs (userid, username, checktime, checktype, verifycode)
             VALUES (%s, %s, %s, %s, %s)
        """

        for r, nombre in data:
         cursor.execute(sql, (r.user_id, nombre, r.timestamp, r.status, r.punch))


        conn.commit()
        print("Registro insertado en la base de datos MANITO")

    except Exception as e:
        print("Error al insertar en la base de datos:", e)
    finally:
        cursor.close()
        conn.close()

def main():
    registros = conexion_hullero()   
    insertar_registros(registros)

if __name__ == "__main__":
    main()
