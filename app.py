from flask import Flask, request, render_template
from funciones import SubPalindroma

app= Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    
    respuesta=''
    if request.method == 'POST':
        respuesta = SubPalindroma(request.form['cadena'])
        
    return render_template("index.html", respuesta={'cadena':respuesta})

if __name__ == "__main__": 
    app.run(debug= True)
