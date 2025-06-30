from . import db  # Importa la instancia de SQLAlchemy

class Estudiante(db.Model):
    __tablename__ = 'estudiante'  # Opcional, pero recomendable

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer)
    carrera = db.Column(db.String(100))

    def __repr__(self):
        return f'<Estudiante {self.nombre}>'
