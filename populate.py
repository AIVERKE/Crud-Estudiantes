from app import create_app, db
from app.models import Estudiante

app = create_app()
app.app_context().push()

estudiantes = [
    Estudiante(nombre="Carlos Ruiz", edad=20, carrera="Arquitectura"),
    Estudiante(nombre="María Fernández", edad=23, carrera="Derecho"),
    Estudiante(nombre="Luis Torres", edad=19, carrera="Biología"),
    Estudiante(nombre="Sofía Morales", edad=22, carrera="Ingeniería de Sistemas"),
    Estudiante(nombre="Andrés Gómez", edad=21, carrera="Medicina"),
    Estudiante(nombre="Valentina Pérez", edad=24, carrera="Psicología"),
    Estudiante(nombre="Diego Sánchez", edad=20, carrera="Comunicación"),
    Estudiante(nombre="Lucía Díaz", edad=23, carrera="Economía"),
    Estudiante(nombre="Javier Ortega", edad=22, carrera="Ingeniería Civil"),
    Estudiante(nombre="Paola Castro", edad=21, carrera="Administración de Empresas"),
    Estudiante(nombre="Fernando López", edad=25, carrera="Ingeniería Electrónica"),
    Estudiante(nombre="Camila Rojas", edad=20, carrera="Diseño Gráfico"),
    Estudiante(nombre="Sebastián Vega", edad=23, carrera="Educación"),
    Estudiante(nombre="Natalia Cruz", edad=22, carrera="Farmacia"),
    Estudiante(nombre="Ricardo Mendoza", edad=24, carrera="Derecho"),
]

db.session.bulk_save_objects(estudiantes)
db.session.commit()

print("Datos insertados correctamente.")
