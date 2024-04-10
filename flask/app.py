from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    nombres=['brayan', 'steven', 'cristian', 'ana', 'sebastian', 'jaider', 'harold', 'david', 'felipe', 'maicol']

    data={
        'titulo':'index',
        'tabla':'tabla',
        'nombres':nombres,
        'numero_nombres':len(nombres)
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)