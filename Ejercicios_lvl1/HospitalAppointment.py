# Por Felipe (ZenTial)

# 3.The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this
# application with the following features: It must have a login and validate the data; after the third failed
# attempt, it should be locked. The user can schedule an appointment for: General Medicine, Emergency Care,
# Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine. There are
# 3 doctors for each specialty. The user can only book one appointment per specialist. An error message should be
# displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer,
# you can choose the doctors' names. The maximum limit for appointments, in general, is 3. Upon selecting a
# specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a
# developer, you can choose the hours. Display available specialists. The user can choose their preferred specialist.
# The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.
from os import system
from random import randint

# Declaración de variables
medicina_general = ['Dr.Chander', 'Dra.Veronica', 'Dr.Pablo']
cuidado_emergencia = ['Dr.Felipe', 'Dr.Luis', 'Dra.Maria']
analisis_clinico = ['Dr.Fernando', 'Dra.Natalia', 'Dra.Carolina']
cardiologia = ['Dr.Benjamín', 'Dr.Gregor', 'Dra.Cristina']
neurologia = ['Dra.Patricia', 'Dra.Lily', 'Dr.Shepherd']
nutricion = ['Dra.Susan', 'Dra.Alicia', 'Dr.Frederick']
kinesiologia = ['Dra.Eva', 'Dra.Jeniffer', 'Dr.William']
traumatologia = ['Dr.Jean', 'Dra.Anna', 'Dr.Alfred']
medicina_clinica = ['Dr.James', 'Dr.Harvey', 'Dr.Gerardo']
lista_especialidades = [medicina_general, cuidado_emergencia, analisis_clinico, cardiologia,
                        neurologia, nutricion, kinesiologia, traumatologia, medicina_clinica]
especialidades = ['medicina general', 'cuidado emergencia', 'análisis clínico', 'cardiología', 'neurología',
                  'nutrición', 'kinesiología', 'traumatología', 'medicina clínica']
citas_agendadas = 0
dict_agendadas = {'medicina general': 0, 'cuidado emergencia': 0, 'análisis clínico': 0,
                  'cardiología': 0, 'neurología': 0, 'nutrición': 0,
                  'kinesiología': 0, 'traumatología': 0, 'medicina clínica': 0}


# Función de inicio de sesión
def inicio_sesion():
    usuario = 'admin'
    password = 'python'
    intentos = 0
    while True:
        try:
            usuario_input = input('Ingrese un usuario: ')
            contrasena_input = input('Ingrese una contraseña: ')
            [usuario].index(usuario_input)
            [password].index(contrasena_input)

        except ValueError:
            intentos += 1
            system('cls')
            print('Ingresa las credenciales correctas.')

        else:
            system('cls')
            return True

        finally:
            if intentos == 3:
                system('cls')
                print('El sistema ha sido bloqueado debido a que ha hecho muchos intentos')
                return False


# Función del menu
def menu():
    while True:
        print('*' * 50)
        for especialidad in especialidades:
            print(especialidad.capitalize())
        print('[F] Finalizar programa')
        try:
            opcion = input('Escriba la especialidad a la que desea agendar una hora: ').lower()
            ['medicina general', 'cuidado emergencia', 'análisis clínico', 'cardiología', 'neurología',
             'nutrición', 'kinesiología', 'traumatología', 'medicina clínica', 'f'].index(opcion)
        except ValueError:
            system('cls')
            print('Error, elige una especialidad valida')
        else:
            if opcion != 'f':
                if dict_agendadas[opcion] == 1:
                    system('cls')
                    print('Esta especialidad no acepta más agendación de horas')
                    input('Presione cualquier tecla para volver al menú')
                    return
                else:
                    dict_agendadas[opcion] = 1
                    return opcion
            else:
                return opcion


# Función para elegir especialista
def elegir_especialista(especialidad):
    while True:
        indice = especialidades.index(especialidad)
        lista_doctores = lista_especialidades[indice]
        print('*' * 50)
        print('Elige un doctor con el que agendar su hora: ')
        for doctor in lista_doctores:
            print(doctor)
        try:
            doctor_elegido = input('')
            lista_doctores.index(doctor_elegido)
        except ValueError:
            system('cls')
            print('Error, escriba un Dr. que exista')
        else:
            return


# Función para escoger horario
def hora():
    while True:
        global citas_agendadas
        print('*' * 50)
        print('Escoga en que horas desea su cita:\nMañana\nTarde')
        try:
            horario_elegido = input('').lower()
            ['mañana', 'tarde'].index(horario_elegido)
        except ValueError:
            system('cls')
            print('Error, escoga un horario valido')
        else:
            if horario_elegido == 'mañana':
                system('cls')
                citas_agendadas += 1
                print(f'Su hora ha sido agendada exitosamente para las 0{randint(8, 11)}:00')
                input('Presione cualquier tecla para volver al menú')
                return
            else:
                system('cls')
                citas_agendadas += 1
                print(f'Su hora ha sido agendada exitosamente para las {randint(12, 17)}:00')
                input('Presione cualquier tecla para volver al menú')
                return


# Función main del programa
def main():
    while True:
        system('cls')
        especialidad = menu()
        if especialidad is None:
            continue
        elif especialidad == 'f':
            system('cls')
            print('El programa ha sido finalizado')
            return
        else:
            system('cls')
            elegir_especialista(especialidad)
            if citas_agendadas == 3:
                system('cls')
                print('Ya has llegado al maximo de citas agendadas')
                input('Presiona cualquier tecla para volver al menú')
                continue
            else:
                system('cls')
                hora()


if __name__ == '__main__':
    main()
