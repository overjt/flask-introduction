from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#
# Parametros de configuracion a la base de datos
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#
# A continuacion se crea un modelo o esquema para la base de datos
#
class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #
    # Funcion que devuelve una cadena cada vez que se crea un nuevo elemento
    # Devuelve el 'id' de la tarea recien creada
    #
    def __repr__(self): 
        return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index(): 
    if request.method == 'POST': 
        if request.json and 'content' in request.json:
            task_content = request.json.get('content',"")
        else: 
            task_content = request.form.get('content',"") # Obtiene el contenido de la tarea, si no hay nada, devuelve una cadena vacia
        
        if not task_content: # Si no hay contenido, no se crea la tarea
            return "task content is required", 400
        # 
        # Se crea un objeto conforme al modelo declarado 
        # 
        new_task = Todo(content = task_content) 
        try: 
            db.session.add(new_task) 
            db.session.commit() 
            if request.json:
                return "Recorded!"
            else: 
                return redirect('/') 
        except: 
            return 'There was an issue adding your task' 
    else: 
        tasks = Todo.query.order_by(Todo.date_created).all() 
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id): 
    task_to_delete = Todo.query.get_or_404(id) 
    try: 
        db.session.delete(task_to_delete) 
        db.session.commit() 
        if request.json:
            return "Deleted!"
        else: 
            return redirect('/')
    except: 
        return "There was a problem deleting that task"

@app.route('/delete', methods=['POST'])
def delete_post():
    if request.json and 'id' in request.json:
        task_id = request.json.get('id', "")
    else: 
        task_id = request.form.get('id', "")
    if not task_id:
        return "task id is required", 400
    return delete(task_id)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id) 
    if request.method == 'POST': 
        task.content = request.form['content'] 
        try: 
            db.session.commit() 
            return redirect('/') 
        except: 
            return 'There was an issue updating your task' 
    else: 
        return render_template('update.html', task=task)


if __name__ == "__main__": 
    app.run(host='0.0.0.0',debug=True)
