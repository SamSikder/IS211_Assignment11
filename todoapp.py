from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    todo_list.append({'task': task, 'email': email, 'priority': priority})
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
