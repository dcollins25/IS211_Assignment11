from flask import Flask, request, redirect, render_template

app = Flask(__name__)

todo_list = []

@app.route('/', methods=['GET'])
def index():
    error_msg = request.args.get('error')
    return render_template('index.html', todo_list=todo_list, error=error_msg)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    # Validation
    if not task:
        error_msg = 'Task cannot be empty.'
        return redirect('/?error=' + error_msg)
    elif not email:
        error_msg = 'Email cannot be empty.'
        return redirect('/?error=' + error_msg)
    elif priority not in ['Low', 'Medium', 'High']:
        error_msg = 'Priority must be either Low, Medium, or High.'
        return redirect('/?error=' + error_msg)
    else:
        todo_list.append({'task': task, 'email': email, 'priority': priority})
        return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
