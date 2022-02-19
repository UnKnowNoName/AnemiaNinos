import psycopg2
import pandas as pd
from Nino import *
from Historial import *

class Pacientes:
    def __init__(self,nombret,apellidot,edadt):
        conexion = psycopg2.connect(user='postgres',
                                    password='ntMN5IgdFyk1AAa1',
                                    host='35.238.179.213',
                                    port='5432',
                                    database='app_db'
                                    )
        try:

            valores=[nombret,apellidot,edadt]
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia =f'INSERT INTO "Pacientes"(nombre, apellido, edad) VALUES(%s,%s,%s)'
                    cursor.execute(sentencia,valores)
        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            conexion.close()

    def consulta_todos():
        conexion = psycopg2.connect(user='postgres',
                                    password='ntMN5IgdFyk1AAa1',
                                    host='35.238.179.213',
                                    port='5432',
                                    database='app_db'
                                    )
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'SELECT * FROM "Pacientes"'
                    cursor.execute(sentencia)
                    registros=cursor.fetchall()
                    return registros

        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            conexion.close()

    def consulta(idt):
            conexion = psycopg2.connect(user='postgres',
                                        password='ntMN5IgdFyk1AAa1',
                                        host='35.238.179.213',
                                        port='5432',
                                        database='app_db'
                                        )
            try:
                with conexion:
                    with conexion.cursor() as cursor:
                        sentencia = 'SELECT * FROM "Pacientes" WHERE id = %s'
                        cursor.execute(sentencia,(idt,))
                        registro=cursor.fetchone()
                        return registro

            except Exception as e:
                print(f'Ocurrió un error: {e}')

            finally:
                conexion.close()

class Registro:

    def __init__(self,idp,hemo):
        conexion = psycopg2.connect(user='postgres',
                                    password='ntMN5IgdFyk1AAa1',
                                    host='35.238.179.213',
                                    port='5432',
                                    database='app_db'
                                    )
        try:
            valores=[idp,hemo]
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia =f'INSERT INTO "Registros"(id_paciente, hemoglobina) VALUES(%s,%s)'
                    cursor.execute(sentencia,valores)
        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            conexion.close()

    def consulta_todos():
        conexion = psycopg2.connect(user='postgres',
                                    password='ntMN5IgdFyk1AAa1',
                                    host='35.238.179.213',
                                    port='5432',
                                    database='app_db'
                                    )
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'SELECT * FROM "Registros"'
                    cursor.execute(sentencia)
                    registros=cursor.fetchall()
                    '''for registro in registros:
                        print(registro)'''
                    return registros

        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            conexion.close()

    def consulta(idt):
        conexion = psycopg2.connect(user='postgres',
                                    password='ntMN5IgdFyk1AAa1',
                                    host='35.238.179.213',
                                    port='5432',
                                    database='app_db'
                                    )
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'SELECT * FROM "Registros" WHERE id_paciente = %s'
                    cursor.execute(sentencia,(idt,))
                    registro=cursor.fetchall()
                    return registro

        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            conexion.close()

class Reportes:
    def id_hemoglobina():
        reg = Registro.consulta_todos()
        pacientes = range(len(Pacientes.consulta_todos())+1)
        i = []
        p = []
        h = []

        for registro in reg:
            for paciente in pacientes:
                if registro[1] == paciente:
                    i.append(registro[0])
                    p.append(registro[1])
                    h.append(registro[2])

        indices = ['id_paciente', 'hemoglobina']
        df = pd.DataFrame([p, h], index=indices, columns=i).transpose()
        grp = df.groupby('id_paciente')
        l=[]
        for key, item in grp:
            k = 'ID ' + key.__str__()
            cadena= f'{k.center(29, "*")}\n{grp.get_group(key)}\n'
            l.append(cadena)
        return l

class Usuarios:
    def __init__(self, usr, psw, gp):
        conexion = psycopg2.connect(user='postgres',
                                    password='ntMN5IgdFyk1AAa1',
                                    host='35.238.179.213',
                                    port='5432',
                                    database='app_db'
                                    )
        try:
            valores = [usr, psw, gp]
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'INSERT INTO "Usuarios"(usuario, contrasena, grupo) VALUES(%s,%s,%s)'
                    cursor.execute(sentencia, valores)
        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            conexion.close()

    def consulta_todos():
        conexion = psycopg2.connect(user='postgres',
                                    password='ntMN5IgdFyk1AAa1',
                                    host='35.238.179.213',
                                    port='5432',
                                    database='app_db'
                                    )
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'SELECT * FROM "Usuarios"'
                    cursor.execute(sentencia)
                    registros=cursor.fetchall()
                    '''for registro in registros:
                        print(registro)'''
                    return registros

        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            conexion.close()


    def consulta(usr):
        conexion = psycopg2.connect(user='postgres',
                                    password='ntMN5IgdFyk1AAa1',
                                    host='35.238.179.213',
                                    port='5432',
                                    database='app_db'
                                    )
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'SELECT * FROM "Usuarios" WHERE usuario = %s'
                    cursor.execute(sentencia,(usr,))
                    registro=cursor.fetchone()
                    #print(registro)
                    return registro

        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            conexion.close()

class CargaInformacion:
    def cargar():
        pacientes = Pacientes.consulta_todos()
        registros = Registro.consulta_todos()
        try:
            for paciente in pacientes:
                niño = Niño(paciente[1],paciente[2],paciente[3])
                historial = Historial(niño)
                for registro in registros:
                    if registro[1]== niño.getId():
                        historial.registraHemoglobina(registro[2])
            print('Finalizó correctamente la carga de información')
        except Exception as e:
            print(f'Ocurrió un error: {e}')