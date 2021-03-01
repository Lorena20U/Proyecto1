from flask import Flask, jsonify, request
usuarios = ["Hola", "Lorena"]
contras = ["1", "2"]
Roles = ["Vendedor", "Comprador"]
objetos = ["telefono", "cama"]
costo = ["5", "3"]
enviar = False
pagado = False
solicitud = False
Compr="""
<html>
<body>
<h1>Bienvenido al sistema de intercambios!!!!!</h1>
<h2>Rol: Comprador </h2>
<h3>Elija una opcion: </h3>
<form action="/menucompr/" method="get">
<p><input type = "checkbox" name = "opcion" value = "1"> 1. Realizar intercambio </p>
<p><input type = "checkbox" name = "opcion" value = "2"> 2. Confirmar pago </p>
<p><input type = "checkbox" name = "opcion" value = "3"> 3. Pagar multa </p>
<p><input type = "checkbox" name = "opcion" value = "4"> 4. Cerrar sesion </p>
<p><input type="submit" value="submit"> </p>
</form>
</body>
</html>"""
Vend="""
<html>
<body>
<h1>Bienvenido al sistema de intercambios!!!!!</h1>
<h2>Rol: Vendedor </h2>
<h3>Elija una opcion: </h3>
<form action="/menuvend/" method="get">
<p><input type = "checkbox" name = "opcion" value = "1"> 1. Registrar producto </p>
<p><input type = "checkbox" name = "opcion" value = "2"> 2. Confirmar envio </p>
<p><input type = "checkbox" name = "opcion" value = "3"> 3. Pagar multa </p>
<p><input type = "checkbox" name = "opcion" value = "4"> 4. Cerrar sesion </p>
<p></p>
<p><input type = "checkbox" name = "opcion" value = "5"> 5. Historial de usuarios </p>
<p><input type="submit" value="submit"> </p>
</form>
</body>
</html>"""
Fallo="""
<html>
<body>
<h1>Error vuelva a intentar!<h1>
<form action="/">
<button>Reintentar</button>
</form>"""
FalloRegistro="""
<html>
<body>
<h1>Este usuario ya existe!<h1>
<form action="/">
<button>Vuelva a intentar</button>
</form>"""
Inicio="""<html>
<body>
<h1> Bienvenido! </h1>
<form action="/register">
<button>Registrarse</button>
</form>
<form action="/login">
<button>Loguearse</button>
</form>"""
Registro="""<html>
<body>
<h1>
Registrate 
</h1>
<form action="/Registro/" method="get">
<p>
<input type="text" name="nombre" value=""> </p>
<p><input type="password" name="passw" value=""> </p>
<p><input type = "checkbox" name = "Rol" value = "Vendedor"> Vendedor
    <input type = "checkbox" name = "Rol" value = "Comprador"> Comprador</p>
<p><input type="submit" value="submit"> </p>
</form>
</body>
</html>"""
Pag="""<html>
<body>
<h1>
Confirmar pago
</h1>
<h3>Elija una opcion: </h3>
<form action="/pago/" method="get">
<p><input type = "checkbox" name = "opcion" value = "Si"> 1. Ya realice el pago</p>
<p><input type = "checkbox" name = "opcion" value = "No"> 2. Sin confirmar </p>
<p><input type="submit" value="submit"> </p>
</form>
</body>
</html>"""
Enviado="""<html>
<body>
<h1>
Confirmar envio
</h1>
<h3>Elija una opcion: </h3>
<form action="/envio/" method="get">
<p><input type = "checkbox" name = "opcion" value = "Si"> 1. Ya envie el paquete</p>
<p><input type = "checkbox" name = "opcion" value = "No"> 2. Sin confirmar </p>
<p><input type="submit" value="submit"> </p>
</form>
</body>
</html>"""
Completado="""
<html>
<body>
<h4>Accion realizada con exito</h4>
<form action="/redireccionando">
<button>Continuar</button>
</form>
</body>
</html>"""
CompletadoV="""
<html>
<body>
<h4>Accion realizada con exito</h4>
<form action="/redireccionandov">
<button>Continuar</button>
</form>
</body>
</html>"""
Loguearse="""<html>
<body>
<h1>
Inicia Sesion
</h1>
<form action="/Logueado/" method="get">
<p>
<input type="text" name="nombre" value=""></p>
<p><input type="password" name="passw" value=""> </p>
<p><input type="submit" value="submit"> </p>
</form>
</body>
</html>"""
producto="""
<html>
<body>
<h1> Nuevo producto </h1>
<form action="/productoregistrado/" method="get">
<h5> Inserte el nombre del producto </h5>
<p><input type="text" name="producto" value=""></p>
<h5> Inserte el precio del producto </h5>
<p><input type="text" name="precio" value=""></p>
<p><input type="submit" value="submit"> </p>
</form>
</body>
</html>"""
productoReg="""
<html>
<body>
<h3> Producto registrado correctamente</h3>
<h2> Desea agregar otro producto</h2>
<form action="/otroproducto/" method="get">
<p>
<p><input type = "checkbox" name = "decision" value = "Si"> Si
    <input type = "checkbox" name = "decision" value = "No"> No</p>
<p><input type="submit" value="submit"> </p>
</form>
</body>
</html>"""
Inter = """
<html>
<body>
<h1>Iniciar un intercambio: </h1>
<h3>Elija el usuario con el que desea realizar un intercambio: </h3>
<form action="/intercambio/" method="get">"""
if objetos:
    for i in range(len(usuarios)):
        Inter += f"""<p><input type = "checkbox" name = "opcion" value = "{i+1}"> {i+1}. {usuarios[i]}</p>"""
    Inter += """<p><input type="submit" value="submit"></p></form></body></html>"""
else:
    Inter += """<p>No se ha registrado ningun vendedor.</p>
<p><input type="submit" value="submit"></p></form></body></html>"""

app = Flask(__name__)
@app.route("/")
def opcion():
    return Inicio

@app.route("/register")
def despedida():
    return Registro

@app.route("/login")
def logue():
    return Loguearse  

@app.route("/completado")
def lcompl():
    return Completado

@app.route("/redireccionando")
def com():
    return Compr

@app.route("/redireccionandov")
def ven():
    return Vend

@app.route("/Registro/", methods=['GET'])
def getvalue():
    name = [request.args['nombre']]
    passw = [request.args['passw']]
    rol = [request.args['Rol']]
    rol2 = request.args['Rol']
    for i in range(len(usuarios)):
        if name == usuarios[i]:
            return FalloRegistro
    usuarios[len(usuarios):] = name
    contras[len(contras):] = passw
    Roles[len(Roles):] = rol
    print(usuarios, contras, Roles)
    if name == "":
        return "Ningun campo a sido rellenado.\nVuelva a intentarlo"
    else: 
        if rol2 == "Vendedor":
            return Vend
        if rol2 == "Comprador":
            return Compr

@app.route("/Logueado/", methods=['GET'])
def check():
    name = request.args['nombre']
    passw = request.args['passw']
    if name == "":
        return "Ningun campo a sido rellenado.\nVuelva a intentarlo."
    if usuarios:
        for i in range(len(usuarios)):
            if name == usuarios[i]:
                if passw == contras[i]:
                    if Roles[i] == "Vendedor":
                        return Vend
                    if Roles[i] == "Comprador":
                        return Compr
        return Fallo
    else:
        return Fallo

@app.route("/productoregistrado/", methods=['GET'])
def product_reg():
    product = [request.args['producto']]
    precio = [request.args['precio']]
    objetos[len(objetos):] = product
    costo[len(costo):] = precio
    return productoReg

@app.route("/otroproducto/", methods=['GET'])
def otro_product():
    decision = request.args['decision']
    if decision == "":
        return "Ningun campo a sido rellenado. \nVuelva a intentarlo."
    if decision == "Si":
        return producto
    if decision == "No":
        return Vend

@app.route("/menuvend/", methods=['GET'])
def inicio_vend():
    opcion = request.args['opcion']
    if opcion == "1":
        return producto
    if opcion == "2":
        return Enviado
    if opcion == "3":
        return "Pagar multa"
    if opcion == "4":
        return Inicio
    if opcion == "5":
        return historial()

@app.route("/menucompr/", methods=['GET'])
def inicio_compr():
    opcion = request.args['opcion']
    if opcion == "1":
        return Inter
    if opcion == "2":
        return Pag
    if opcion == "3":
        return "Pagar multa"
    if opcion == "4":
        return Inicio

@app.route("/intercambio/", methods=['GET'])
def intercambio():
    opcion = request.args['opcion']
    Listado = """
    <html>
    <body>
    <h1>Producto</h1>
    <form action="/completado" method="get">"""
    Listado += f"""<h2>Solicitando a: {usuarios[int(opcion)-1]}</h2>
    <h3>Elija el producto que desea comprarle: </h3>"""
    if objetos:
        for x in range(len(objetos)):
            Listado += f"""<p><input type = "checkbox" name = "opcion" value = "{x+1}"> {x+1}. {objetos[x]} <p>Precio: {costo[x]}</p></p>"""
        Listado += """<p><input type="submit" value="submit"></p></form></body></html>"""
        solicitud = True
    else:
        Listado += """<p>No se ha registrado ningun producto.</p>
        <p><input type="submit" value="submit"></p></form></body></html>"""
    return Listado, solicitud

@app.route("/pago/", methods=['GET'])
def pago():
    pago = request.args['opcion']
    if pago == "Si":
        pagado = True
    else:
        pagado = False
    return Completado, pagado

@app.route("/envio/", methods=['GET'])
def envioP():
    envio = request.args['opcion']
    if envio == "Si":
        enviar = True
    else:
        enviar = False
    return CompletadoV, enviar

@app.route("/historial/", methods=['GET'])
def historial():
    h = """
    <html>
    <body>
    <h1>Historial</h1>
    <form action="/completado" method="get">
    <table class="default">
    <tr>
        <td>Usuarios</td>
        <td>Contrasena</td>
    </tr>"""
    for i in range(len(usuarios)):
        h+=f"""
        <tr>
            <td>{usuarios[i]}</td>
            <td>{contras[i]}</td>
        </tr>"""
    h += """</table></body></html>"""
    return h

if __name__ == '__main__':
    app.run(debug = True)