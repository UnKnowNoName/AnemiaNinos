import tkinter as tk
from Conexion import *
from Historial import *
from Nino import *


class Principal:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Registro")
        self.master.geometry("500x400")
        self.master.resizable(0, 0)
        self.master.config(bg="skyblue")
        self.frame = tk.Frame(self.master, bg="skyblue")
        self.label = tk.Label(self.frame, text="Bienvenido al sistema de Registro", bg="skyblue", fg="darkgreen",
                              font=("Times New Roman", 15, "bold italic")).pack()
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.butnew("Registrar Paciente", Registrador)
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.butnew("Registrar Hemoglobina", Registrador_hemoglobina)
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.butnew("Reporte Paciente", Reporte_Paciente)
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.butnew("Reporte General", General)
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.butnew("Reporte Suministros", Suministro)
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.butnew("Registro Usuarios", Registrador_usuarios)
        self.label = tk.Label(self.frame, text="", bg="skyblue").pack()
        self.frame.pack()

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, width=25, command=lambda: self.new_window(_class)).pack()

    def new_window(self, _class):
        self.newWindow = tk.Toplevel(self.master)
        _class(self.newWindow)


class Registrador:

    def __init__(self, master):

        self.master = master
        self.master.title("Registra Paciente")

        global name, last, age, estado, histclin
        name = tk.StringVar(self.master, "", "name_register")
        last = tk.StringVar(self.master, "", "last_register")
        age = tk.IntVar(self.master, "", "age_register")
        estado = tk.StringVar(self.master, "", "Estado_register")
        histclin = tk.IntVar(self.master, "", "histclin_register")
        self.master.geometry("400x420")
        self.master.config(bd=2, bg="lightblue")
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(master, text="Registrar Paciente", bg="lightblue", fg="darkgreen",
                              font=("Times New Roman", 15, "bold italic")).pack()
        self.label_nombre = tk.Label(self.master, text="Nombre", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=name).pack()
        tk.Label(self.master, text="Apellido", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=last).pack()
        tk.Label(self.master, text="Edad (Meses)", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=age).pack()
        tk.Label(self.master, text="", bg="lightblue").pack()
        tk.Label(self.master, text="\nEstado", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=estado, state="disabled",
                 width=38).pack()
        tk.Label(self.master, text="\nHistoria Clinica N°", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=histclin, state="disabled",
                 width=38).pack()
        tk.Label(self.master, text="\n", bg="lightblue").pack()
        self.butnew("Registrar ", self.register)
        self.butnew("Limpiar", self.errase)
        self.butnew("Cancelar", self.close_windows)
        self.frame.pack()

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, width=25, command=_class).pack()

    def register(self):
        try:
            if (name.get() != ""):
                if (last.get() != ""):
                    if (age.get() >= 1):
                        paciente = Niño(name.get(), last.get(), age.get())
                        Pacientes(name.get(), last.get(), age.get())
                        estado.set("Se ha registrado correctamente al paciente")
                        histclin.set(paciente.getId())
                        self.errase()
                    else:
                        print("Ingrese una edad válida")
                else:
                    print("Ingrese un apellido válido")
            else:
                print("Ingrese un nombre válido")
        except:
            print("Porfavor ingresa valores válidos")

    def errase(self):
        name.set("")
        last.set("")
        age.set("")

    def close_windows(self):
        self.master.destroy()


class Registrador_hemoglobina:

    def __init__(self, master):
        self.master_registrador = master
        self.master_registrador.title("Registra Hemoglobina")

        global registrador_estado, registrador_histclin, registrador_hemoglobina
        registrador_estado = tk.StringVar(self.master_registrador, "", "Estado_RegistradorHemoglobina")
        registrador_histclin = tk.IntVar(self.master_registrador, "", "Historia Clinica_RegistradorHemoglobina")
        registrador_hemoglobina = tk.DoubleVar(self.master_registrador, "", "Hemoglobina_RegistradorHemoglobina")
        self.master_registrador.geometry("400x420")
        self.master_registrador.config(bd=2, bg="lightblue")
        self.frame = tk.Frame(self.master_registrador)

        self.label = tk.Label(self.master_registrador, text="Registrar Hemoglobina", bg="lightblue", fg="darkgreen",
                              font=("Times New Roman", 15, "bold italic")).pack()

        tk.Label(self.master_registrador, text="N° Historia Clinica", bg="lightblue").pack()
        tk.Entry(self.master_registrador, justify="center", textvariable=registrador_histclin).pack()
        tk.Label(self.master_registrador, text="Nivel de Hemoglobina", bg="lightblue").pack()
        tk.Entry(self.master_registrador, justify="center", textvariable=registrador_hemoglobina).pack()
        tk.Label(self.master_registrador, text="", bg="lightblue").pack()

        tk.Label(self.master_registrador, text="\nEstado", bg="lightblue").pack()
        tk.Entry(self.master_registrador, justify="center", textvariable=registrador_estado, state="disabled",
                 width=38).pack()
        tk.Label(self.master_registrador, text="\n", bg="lightblue").pack()

        self.butnew("Registrar ", self.register)
        self.butnew("Limpiar", self.errase)
        self.butnew("Cancelar", self.close_windows)
        self.frame.pack()

    def register(self):
        try:
            hclin = registrador_histclin.get()
            hemo = registrador_hemoglobina.get()
            if hclin > 0:
                if hemo > 0:
                    if Pacientes.consulta(hclin) is not None:
                        Registro(hclin, hemo)
                        registrador_estado.set("Guardado Correctamente")
                        self.errase()
                    else:
                        registrador_estado.set("El paciente no está registrado")

                else:
                    registrador_estado.set("Ingrese un nivel de hemoglobina válido")
            else:
                registrador_estado.set("Ingrese un numero de historia clinica válido")
        except:
            registrador_estado.set("Porfavor ingresa valores válidos")

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, width=25, command=_class).pack()

    def errase(self):
        registrador_histclin.set("")
        registrador_hemoglobina.set("")

    def close_windows(self):
        self.master_registrador.destroy()


class Reporte_Paciente:

    def __init__(self, master):
        self.master_reporte = master
        self.master_reporte.title("Reporte Paciente")

        global reporte_name, reporte_last, reporte_age, reporte_hemoglobina, reporte_histclin, \
            reporte_reporte, reporte_tratamiento, reporte_nivel_riesgo, reporte_estado
        reporte_name = tk.StringVar(self.master_reporte, "", "name_ReportePaciente")
        reporte_last = tk.StringVar(self.master_reporte, "", "last_ReportePaciente")
        reporte_age = tk.IntVar(self.master_reporte, "", "age_ReportePaciente")
        reporte_reporte = tk.StringVar(self.master_reporte, "", "Reporte por Paciente_ReportePaciente")
        reporte_histclin = tk.IntVar(self.master_reporte, "", "Historia Clinica_ReportePaciente")
        reporte_hemoglobina = tk.IntVar(self.master_reporte, "", "Hemoglobina_ReportePaciente")
        reporte_tratamiento = tk.StringVar(self.master_reporte, "", "Tratamiento_ReportePaciente")
        reporte_nivel_riesgo = tk.StringVar(self.master_reporte, "", "Nivel de Riesgo_ReportePaciente")
        reporte_estado = tk.StringVar(self.master_reporte, "", "Reporte_Estado")
        self.master_reporte.geometry("400x680")
        self.master_reporte.config(bd=2, bg="lightblue")
        self.frame = tk.Frame(self.master_reporte)
        tk.Label(self.master_reporte, text="\n", bg="lightblue").pack()
        self.label = tk.Label(self.master_reporte, text="Reporte por Paciente", bg="lightblue", fg="darkgreen",
                              font=("Times New Roman", 15, "bold italic")).pack()
        tk.Label(self.master_reporte, text="N° Historia Clinica", bg="lightblue").pack()
        tk.Entry(self.master_reporte, justify="center", textvariable=reporte_histclin).pack()
        tk.Label(self.master_reporte, text="\nReporte", bg="lightblue", fg="darkgreen",
                 font=("Times New Roman", 15, "bold italic")).pack()
        tk.Label(self.master_reporte, text="", bg="lightblue").pack()
        tk.Label(self.master_reporte, text="Nombre", bg="lightblue").pack()
        tk.Entry(self.master_reporte, justify="center", textvariable=reporte_name, state="disable").pack()
        tk.Label(self.master_reporte, text="Apellido", bg="lightblue").pack()
        tk.Entry(self.master_reporte, justify="center", textvariable=reporte_last, state="disable").pack()
        tk.Label(self.master_reporte, text="Edad (Meses)", bg="lightblue").pack()
        tk.Entry(self.master_reporte, justify="center", textvariable=reporte_age, state="disable").pack()
        tk.Label(self.master_reporte, text="Nivel de Riesgo", bg="lightblue").pack()
        tk.Entry(self.master_reporte, justify="center", textvariable=reporte_nivel_riesgo, state="disable").pack()
        tk.Label(self.master_reporte, text="Hemoglobina", bg="lightblue").pack()
        tk.Entry(self.master_reporte, justify="center", textvariable=reporte_hemoglobina, state="disable").pack()
        tk.Label(self.master_reporte, text="Tratamiento", bg="lightblue").pack()
        tk.Entry(self.master_reporte, justify="center", textvariable=reporte_tratamiento, state="disable").pack()
        tk.Label(self.master_reporte, text="\n", bg="lightblue").pack()

        tk.Label(self.master_reporte, text="\nEstado", bg="lightblue").pack()
        tk.Entry(self.master_reporte, justify="center", textvariable=reporte_estado, state="disabled",
                 width=38).pack()
        tk.Label(self.master_reporte, text="\n", bg="lightblue").pack()

        self.butnew("Consultar ", self.reporte)
        self.butnew("Limpiar", self.errase)
        self.butnew("Cancelar", self.close_windows)
        self.frame.pack()

    def reporte(self):
        try:
            k = reporte_histclin.get()
            paciente = Pacientes.consulta(k)
            if paciente is not None:
                niño = Niño(paciente[1], paciente[2], paciente[3])
                registro = Registro.consulta(k)
                t = Historial(niño)
                for r in registro:
                    t.registraHemoglobina(r[2])

                reporte_histclin.set("")
                reporte_name.set(paciente[1])
                reporte_last.set(paciente[2])
                reporte_age.set(paciente[3])
                reporte_nivel_riesgo.set(t.getNivelRiesgo())
                reporte_hemoglobina.set(t.getHemoglobina())
                reporte_tratamiento.set(t.getTratamiento())
                reporte_estado.set("")
            else:
                self.errase()
                reporte_estado.set('El paciente no se encuentra registrado')

        except Exception as e:
            print(f"Porfavor ingresa valores válidos. \n\tInformación:\n\t - {e}")

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, width=25, command=_class).pack()

    def errase(self):
        reporte_histclin.set("")
        reporte_name.set("")
        reporte_last.set("")
        reporte_age.set("")
        reporte_nivel_riesgo.set("")
        reporte_hemoglobina.set("")
        reporte_tratamiento.set("")

    def close_windows(self):
        self.master_reporte.destroy()


class General:
    def __init__(self, master):
        self.master_general = master
        self.master_general.title("Reporte General")
        global general_reporte
        general_reporte = tk.StringVar(self.master_general, "", "Reporte General")
        self.cuadroReporte = ""
        self.master_general.geometry("1360x780")
        self.master_general.config(bd=2, bg="lightblue")

        self.frame = tk.Frame(self.master_general)

        try:
            cuadro = General.reporte()
            self.cuadroReporte = f'ID{cuadro.to_string()[2:]}'
        except Exception as e:
            print('Error:\n', e)
            self.cuadroReporte = """[ERROR]
    Parece que algo falló
    - Debes registrar almenos un paciente
    - Debes haber registrado la hemoglobina almenos una vez de cada paciente registrado"""

        self.label = tk.Label(self.master_general, text="Reporte General", bg="lightblue", fg="darkgreen",
                              font=("Times New Roman", 15, "bold italic")).pack()

        self.table = tk.Text(self.master_general, height=40, width=150, bd=4)
        self.table.insert(tk.INSERT, self.cuadroReporte)
        self.table.pack()

        tk.Label(self.master_general, text="\n", bg="lightblue").pack()

        self.butnew("Cerrar", self.close_windows)
        self.frame.pack()

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, width=25, command=_class).pack()

    def close_windows(self):
        self.master_general.destroy()

    def reporte():
        try:
            data = []
            pacientes = Pacientes.consulta_todos()
            for paciente in pacientes:
                #registro = Registro.consulta(paciente[0])
                #print(registro)
                if Registro.consulta(paciente[0]) != []:
                    registro = Registro.consulta(paciente[0])
                    niño = Niño(paciente[1], paciente[2], paciente[3])
                    t = Historial(niño)
                    for r in registro:
                        t.registraHemoglobina(r[2])
                    info = (
                        paciente[0],
                        paciente[1],
                        paciente[2],
                        paciente[3],
                        t.getNivelRiesgo(),
                        t.getHemoglobina()[-1],
                        t.getTratamiento()
                    )
                    data.append(info)
                else:
                    info = (
                        paciente[0],
                        paciente[1],
                        paciente[2],
                        paciente[3],
                        '-',
                        '-',
                        '-'
                    )
                    data.append(info)

            # DATAFRAME
            id = []
            nombres = []
            apellidos = []
            edades = []
            nriesgo = []
            hemog = []
            tratamiento = []

            for d in data:
                id.append(d[0])
                nombres.append(d[1])
                apellidos.append(d[2])
                edades.append(d[3])
                nriesgo.append(d[4])
                hemog.append(d[5])
                tratamiento.append(d[6])

            reporte = {
                "Nombre": nombres,
                "Apellido": apellidos,
                "Edad (Meses)": edades,
                "Nivel Riesgo": nriesgo,
                "Reg. Hemoglobina": hemog,
                "Tratamiento": tratamiento
            }
            cuadro = pd.DataFrame(reporte, index=id)
            return cuadro
        except Exception as e:
            print('Error:\n', e)


class Suministro:
    def __init__(self, master):
        self.master_suministro = master
        self.master_suministro.title("Reporte Suministro")

        global cuadro_suministro_reporte
        cuadro_suministro_reporte = tk.StringVar(self.master_suministro, "", "Reporte Suministro")
        self.cuadro_suministro_Reporte = ""
        self.master_suministro.geometry("450x360")
        self.master_suministro.config(bd=2, bg="lightblue")

        self.frame = tk.Frame(self.master_suministro)

        try:
            cuadro = Suministro.reporte()
            self.cuadro_suministro_Reporte = cuadro.to_string()
        except:
            self.cuadro_suministro_Reporte = """[ERROR]
Parece que algo falló
- Debes registrar almenos un paciente
- Debes haber registrado la hemoglobina almenos una vez de cada paciente\nregistrado"""

        self.label = tk.Label(self.master_suministro, text="Reporte Suministros", bg="lightblue", fg="darkgreen",
                              font=("Times New Roman", 15, "bold italic")).pack()

        self.table = tk.Text(self.master_suministro, height=10, width=40, bd=4)
        self.table.insert(tk.INSERT, self.cuadro_suministro_Reporte)
        self.table.pack()

        tk.Label(self.master_suministro, text="\n", bg="lightblue").pack()

        self.butnew("Cerrar", self.close_windows)
        self.frame.pack()

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, width=25, command=_class).pack()

    def close_windows(self):
        self.master_suministro.destroy()

    def reporte():
        try:
            tratamientoSevero = 0
            tratamientoModerado = 0
            tratamientoLeve = 0
            noRequiere = 0
            hemoglobinas = []
            pacientes = Pacientes.consulta_todos()
            for paciente in pacientes:
                if Registro.consulta(paciente[0]) != []:
                    registro = Registro.consulta(paciente[0])
                    niño = Niño(paciente[1], paciente[2], paciente[3])
                    t = Historial(niño)

                    for r in registro:
                        t.registraHemoglobina(r[2])
                    hemoglobinas.append(t.getHemoglobina()[-1])

                else:
                    noRequiere+=1

            for hemoglobina in hemoglobinas:
                if (hemoglobina < 7.0):
                    tratamientoSevero += 1
                elif (hemoglobina < 10.0):
                    tratamientoModerado += 1
                elif (hemoglobina < 11.0):
                    tratamientoLeve += 1
                else:
                    noRequiere += 1

            medic = ["Sulfato ferroso", "Micronutrientes en polvo", "Hierro polimaltosado"]
            cantidad = [tratamientoSevero, tratamientoModerado, tratamientoLeve]
            reporte = pd.DataFrame({"Total": cantidad}, index=medic)
            cuadro = pd.DataFrame(reporte)
            return cuadro
        except Exception as e:
            print(f'Error: {e}')

class Registrador_usuarios:

    def __init__(self, master):

        self.master = master
        self.master.title("Registra Usuarios")

        global usuario, contrasena, grupo, estado
        usuario = tk.StringVar(self.master, "", "usuario")
        contrasena = tk.StringVar(self.master, "", "contrasena")
        grupo = tk.StringVar(self.master, "", "grupo")
        estado= tk.StringVar(self.master,"","estado_registradorUsuarios")
        self.master.geometry("400x420")
        self.master.config(bd=2, bg="lightblue")
        self.frame = tk.Frame(self.master)
        #self.label = \
        tk.Label(master, text="Registrar Usuario", bg="lightblue", fg="darkgreen",
                 font=("Times New Roman", 15, "bold italic")).pack()
        #self.label_nombre = \
        tk.Label(self.master, text="Usuario", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=usuario).pack()
        tk.Label(self.master, text="Contrasena", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=contrasena, show="*").pack()
        tk.Label(self.master, text="Grupo", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=grupo).pack()
        tk.Label(self.master, text="", bg="lightblue").pack()

        tk.Label(self.master, text="\nEstado", bg="lightblue").pack()
        tk.Entry(self.master, justify="center", textvariable=estado, state="disabled",
                 width=38).pack()
        tk.Label(self.master, text="\n", bg="lightblue").pack()
        self.butnew("Registrar ", self.register)
        self.butnew("Limpiar", self.errase)
        self.butnew("Cancelar", self.close_windows)
        self.frame.pack()

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, width=25, command=_class).pack()

    def register(self):
        try:
            if (usuario.get() != ""):
                if (contrasena.get() != ""):
                    if (grupo.get() !=""):
                        Usuarios(usuario.get(), contrasena.get(), grupo.get())
                        estado.set("Se ha registrado correctamente al usuario")
                        self.errase()
                    else:
                        estado.set("Ingrese un grupo válida")
                else:
                    estado.set("Ingrese una contraseña válido")
            else:
                estado.set("Ingrese un usuario válido")
        except Exception as e:
            estado.set(f"Porfavor ingresa valores válidos {e}")

    def errase(self):
        usuario.set("")
        contrasena.set("")
        grupo.set("")

    def close_windows(self):
        self.master.destroy()


class Login:
    i = 5

    def __init__(self, master):
        self.master_login = master
        global user_login, password_login, state_login
        user_login = tk.StringVar(self.master_login, "", "Usuario_Login")
        password_login = tk.StringVar(self.master_login, "", "Password_Login")
        state_login = tk.StringVar(self.master_login, "5", "Estado_Login")
        self.master_login.title("Sistema de Registro")
        self.master_login.geometry("500x370")
        self.master_login.resizable(0, 0)
        self.master_login.config(bg="skyblue")

        self.frame = tk.Frame(self.master_login, bg="skyblue")
        tk.Label(self.frame, text="", bg="skyblue").pack()
        tk.Label(self.frame, text="Bienvenido al sistema de Registro", bg="skyblue", fg="darkgreen",
                 font=("Times New Roman", 25, "bold italic")).pack()
        tk.Label(self.frame, text="", bg="skyblue").pack()
        tk.Label(self.frame, text="", bg="skyblue").pack()

        tk.Label(self.frame, text="Usuario", bg="skyblue").pack()
        tk.Entry(self.frame, justify="center", textvariable=user_login).pack()
        tk.Label(self.frame, text="Contraseña", bg="skyblue").pack()
        tk.Entry(self.frame, justify="center", textvariable=password_login, show="*").pack()
        tk.Label(self.frame, text="", bg="skyblue").pack()
        tk.Label(self.frame, text="Intentos", bg="skyblue").pack()
        tk.Entry(self.frame, justify="center", textvariable=state_login, state="disable").pack()
        tk.Label(self.frame, text="", bg="skyblue").pack()
        self.butnew("Ingrese", self.access)
        tk.Label(self.frame, text="", bg="skyblue").pack()

        tk.Button(self.frame, text="Salir", width=25, command=self.close_windows).pack()
        self.frame.pack()

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, width=25, command=lambda: self.access(Principal)).pack()

    def new_window(self, _class):
        self.newWindow = tk.Toplevel(self.master_login)
        _class(self.newWindow)

    def access(self, _class):

        try:
            u = user_login.get().upper()
            p = password_login.get().upper()
            usr = Usuarios.consulta(u)
            if self.i >= 1:
                if u == usr[1] and p == usr[2]:
                    self.new_window(_class)
                    CargaInformacion.cargar()
                    Login.errase()
                else:
                    state_login.set(self.i - 1)
                    self.i -= 1
            else:
                self.close_windows()

        except Exception as e:
            state_login.set(self.i - 1)
            self.i -= 1
            if self.i < 1: self.close_windows()
            print(e)

    def errase():
        user_login.set("")
        password_login.set("")

    def close_windows(self):
        self.master_login.destroy()
