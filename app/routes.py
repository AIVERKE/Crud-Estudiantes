from flask import Blueprint, render_template, request, redirect, url_for
from .models import Estudiante
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    estudiantes = Estudiante.query.all()
    return render_template('index.html', estudiantes=estudiantes)

@main.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        carrera = request.form['carrera']

        nuevo = Estudiante(nombre=nombre, edad=int(edad) if edad else None, carrera=carrera)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_student.html')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    estudiante = Estudiante.query.get_or_404(id)
    if request.method == 'POST':
        estudiante.nombre = request.form['nombre']
        edad = request.form['edad']
        estudiante.edad = int(edad) if edad else None
        estudiante.carrera = request.form['carrera']
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('edit_student.html', estudiante=estudiante)

@main.route('/delete/<int:id>')
def delete_student(id):
    estudiante = Estudiante.query.get_or_404(id)
    db.session.delete(estudiante)
    db.session.commit()
    return redirect(url_for('main.index'))
