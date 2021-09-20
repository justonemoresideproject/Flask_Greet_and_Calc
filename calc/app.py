from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_form():
    return """
    <h1>Add two numbers together</h1>
    <form method="POST">
        <h3>A</h3>
        <input type="number" placeholder=0 name='a'/>
        <h3>B</h3>
        <input type="number" placeholder=0 name='b'/>
        <br>
        <button>Submit</button>
    </form>
    """

@app.route('/add', methods=["POST"])
def add_answer():
    a = request.form['a']
    b = request.form['b']
    return f"""
        <h1>{a} + {b} = {int(a) + int(b)}</h1>
        <a href='/add'>Reset</a>
    """

@app.route('/add/<int:a>/<int:b>')
def add_route(a, b):
    return f"""
        <h1>{a} + {b} = {a + b}</h1>
    """

@app.route('/sub')
def sub_form():
    return """
    <h1>Subtract a from b</h1>
    <form method="POST">
        <h3>A</h3>
        <input type="number" placeholder=0 name='a'/>
        <h3>B</h3>
        <input type="number" placeholder=0 name='b'/>
        <br>
        <button>Submit</button>
    </form>
    """

@app.route('/sub', methods=["POST"])
def sub_answer():
    a = request.form['a']
    b = request.form['b']
    return f"""
        <h1>{a} - {b} = {int(a) - int(b)}</h1>
        <a href='/sub'>Reset</a>
    """

@app.route('/sub/<int:a>/<int:b>')
def sub_route(a, b):
    return f"""
        <h1>{a} - {b} = {a - b}</h1>
    """

@app.route('/mult')
def mult_form():
    return """
    <h1>Multiply a times b</h1>
    <form method="POST">
        <h3>A</h3>
        <input type="number" placeholder=0 name='a'/>
        <h3>B</h3>
        <input type="number" placeholder=0 name='b'/>
        <br>
        <button>Submit</button>
    </form>
    """

@app.route('/mult', methods=["POST"])
def mult_answer():
    a = request.form['a']
    b = request.form['b']
    return f"""
        <h1>{a} * {b} = {int(a) * int(b)}</h1>
        <a href='/mult'>Reset</a>
    """

@app.route('/mult/<int:a>/<int:b>')
def mult_route(a, b):
    return f"""
        <h1>{a} * {b} = {a * b}</h1>
    """

@app.route('/div')
def div_form():
    return """
    <h1>Divide a by b</h1>
    <form method="POST">
        <h3>A</h3>
        <input type="number" placeholder=0 name='a'/>
        <h3>B</h3>
        <input type="number" placeholder=0 name='b'/>
        <br>
        <button>Submit</button>
    </form>
    """

@app.route('/div', methods=["POST"])
def div_answer():
    a = request.form['a']
    b = request.form['b']
    return f"""
        <h1>{a} / {b} = {int(a) / int(b)}</h1>
        <a href='/div'>Reset</a>
    """

@app.route('/div/<int:a>/<int:b>')
def div_route(a, b):
    return f"""
        <h1>{a} / {b} = {a / b}</h1>
    """

OPERATIONS = {
    'add': '+',
    'sub': '-',
    'mult': '*',
    'div': '/'
}

@app.route('/math/<operation>/<int:a>/<int:b>')
def operation_route(operation, a, b):
    op = OPERATIONS[operation]
    return f"""
        <h1>{op(a, b)}</h1>
    """