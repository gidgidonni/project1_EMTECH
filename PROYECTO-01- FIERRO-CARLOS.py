# Importamos librería con los datos a analizar
from lifestore_file import *
import copy

# Lista de usuarios admitidos
usuarios = ["MegaSaurio","BrontoSaurio","SaltaSaurio"]
# Contraseñas de cada usuario
passcode = ["Pass123","Pass456","Pass789"]
# Datos de super usuario (Todos los usuarios pueden generar reportes pero el super usuario puede crear
# nuevos usuarios en el sistema)
super_usuario = usuarios[0]
contrasena_super_usuario = passcode[0]

# Creamos Login
print("Bienvenido al sistema de reportes")
print("---------------------------------")
usuario = input("Ingrese su usuario: ")
# Definimos contador de intentos y variable de control de acceso
h = 3
while h > 0:
    # Corroboramos que el usuario esté en la lista
    if usuario in usuarios:
        passco = input("Ingrese su contraseña: ")
        # Corroboramos que sea la contraseña indicada
        if passco in passcode:
            print("---------------------------------")
            print("---------------------------------")
            print("Bienvenido "+usuario)
            h = -1
            entrada = True
        else:
            h -= 1
            print("Contraseña incorrecta, le quedan "+str(h)+" intentos.")
            if h == 0:
                print("--------------------------")
                print("El programa se ha cerrado.")
    else:
        print("-------------------------------------------------------------")
        print("El nombre de usuario no se encuentra en la lista de usuarios.")
        respuesta = input("¿Desea agregar uno nuevo? (si/no): ")
        if respuesta == "si":
            print("--------------------------------------------")
            print("Ingrese datos de superusuario para continuar")
            sup = input("Usuario: ")
            contrasena_sup = input("Contraseña: ")
            if sup == super_usuario and contrasena_sup == contrasena_super_usuario:
                nuevo_usuario = input("Ingrese nuevo nombre de usuario: ")
                usuarios.append(nuevo_usuario)
                nueva_contrasena = input("Ingrese contraseña para nuevo usuario: ")
                passcode.append(nueva_contrasena)
                print("---------------------------------")
                print("Bienvenido al sistema de reportes")
                print("---------------------------------")
                usuario = input("Ingrese su usuario: ")
            else:
                print("Datos incorrectos, el programa se ha cerrado.")
                h = 0
        else:
            print("---------------------------------")
            print("Bienvenido al sistema de reportes")
            print("---------------------------------")
            usuario = input("Ingrese su usuario: ")
            
# Corremos el siguiente código para conocer cuanto se vendió de cada producto
resultado_ventas = []
# No contamos como venta el primer producto si se devolvió
if lifestore_sales[0][4] == 0:
    contador = 1
else:
    contador = 0
for i in range(len(lifestore_sales)-1):
    prod_id = lifestore_sales[i][1]
    if lifestore_sales[i][1] == lifestore_sales[i+1][1]:
        contador += 1
        # Nótese que no contamos a un producto como vendido si se devolvió
        if lifestore_sales[i+1][4] == 1:
            contador -= 1
    else:
        if contador > 0:
            contador_vec = [prod_id]
            contador_vec.append(contador)
            resultado_ventas.append(contador_vec)
        if lifestore_sales[i+1][4] == 0:
            contador = 1
        else:
            contador = 0
# Tratamos de manera especial el final de la lista
if lifestore_sales[-1][1] == lifestore_sales[-2][1]:
    contador_vec = [prod_id]
    contador_vec.append(contador)
    resultado_ventas.append(contador_vec)
else:
    if lifestore_sales[-1][4] == 0:
        contador_vec = [lifestore_sales[-1][1]]
        contador_vec.append(1)
        resultado_ventas.append(contador_vec)
# Ordenaremos los productos contados por número de ventas
resultado_ventas_ordenado = []
# Primero creamos copia de resultado_ventas
copia_resultado_ventas = resultado_ventas.copy()
# Procedemos a realizar el algoritmo de ordenamiento por medio de una comparación de los dos últimos
# elementos
for i in range(len(copia_resultado_ventas)):
    while len(resultado_ventas) > 1:
        # Comparamos los dos últimos elementos y vamos retirando el más pequeño
        if resultado_ventas[len(resultado_ventas)-2][1] >= resultado_ventas[len(resultado_ventas)-1][1]:
            resultado_ventas.remove(resultado_ventas[len(resultado_ventas)-1])
        else:
            resultado_ventas.remove(resultado_ventas[len(resultado_ventas)-2])
    # Guardamos el valor más alto de todos
    resultado_ventas_ordenado.append(resultado_ventas[0])
    resultado_ventas = copia_resultado_ventas.copy()
    # Quitamos valores que ya ganaron
    for h in range(len(resultado_ventas_ordenado)):
        resultado_ventas.remove(resultado_ventas_ordenado[h])

# Realizamos el mismo procedimiento para las búsquedas
# Corremos el siguiente código para conocer cuanto se buscó de cada producto
resultado_busqueda = []
contador = 1
for i in range(len(lifestore_searches)-1):
    prod_id = lifestore_searches[i][1]
    if lifestore_searches[i][1] == lifestore_searches[i+1][1]:
        contador += 1
    else:
        contador_vec = [prod_id]
        contador_vec.append(contador)
        resultado_busqueda.append(contador_vec)
        contador = 1
# Tratamos de manera especial el final de la lista
if lifestore_searches[-1][1] == lifestore_searches[-2][1]:
    contador_vec = [prod_id]
    contador_vec.append(contador)
    resultado_busqueda.append(contador_vec)
else:
    contador_vec = [lifestore_searches[-1][1]]
    contador_vec.append(1)
    resultado_busqueda.append(contador_vec)
# Ordenamos por número de búsquedas
resultado_busqueda_ordenado = []
# Primero creamos copia de resultado_busqueda
copia_resultado_busqueda = resultado_busqueda.copy()
# Procedemos a realizar el algoritmo de ordenamiento por medio de una comparación de los dos últimos
# elementos
for i in range(len(copia_resultado_busqueda)):
    while len(resultado_busqueda) > 1:
        # Comparamos los dos últimos elementos y vamos retirando el más pequeño
        if resultado_busqueda[len(resultado_busqueda)-2][1] >= resultado_busqueda[len(resultado_busqueda)-1][1]:
            resultado_busqueda.remove(resultado_busqueda[len(resultado_busqueda)-1])
        else:
            resultado_busqueda.remove(resultado_busqueda[len(resultado_busqueda)-2])
    # Guardamos el valor más alto de todos
    resultado_busqueda_ordenado.append(resultado_busqueda[0])
    resultado_busqueda = copia_resultado_busqueda.copy()
    # Quitamos valores que ya ganaron
    for h in range(len(resultado_busqueda_ordenado)):
        resultado_busqueda.remove(resultado_busqueda_ordenado[h])

# Ahora calcularemos el promedio de reseña para los productos vendidos
prom_resenas = []
contador1 = lifestore_sales[0][2]
contador2 = 1
for i in range(len(lifestore_sales)-1):
    prod_id = lifestore_sales[i][1]
    if lifestore_sales[i][1] == lifestore_sales[i+1][1]:
        contador1 += lifestore_sales[i+1][2]
        contador2 += 1
    else:
        prom = contador1/contador2
        contador_vec = [prod_id]
        contador_vec.append(prom)
        prom_resenas.append(contador_vec)
        contador1 = lifestore_sales[i+1][2]
        contador2 = 1
# Tratamos de manera especial el final de la lista
if lifestore_sales[-1][1] == lifestore_sales[-2][1]:
    prom = contador1/contador2
    contador_vec = [prod_id]
    contador_vec.append(prom)
    prom_resenas.append(contador_vec)
else:
    contador_vec = [lifestore_sales[-1][1]]
    contador_vec.append(lifestore_sales[-1][2])
    prom_resenas.append(contador_vec)
# Ordenaremos los productos por su reseña
prom_resenas_ordenado = []
# Primero creamos copia de prom_resenas
copia_prom_resenas = prom_resenas.copy()
# Procedemos a realizar el algoritmo de ordenamiento por medio de una comparación de los dos últimos
# elementos
for i in range(len(copia_prom_resenas)):
    while len(prom_resenas) > 1:
        # Comparamos los dos últimos elementos y vamos retirando el más pequeño
        if prom_resenas[len(prom_resenas)-2][1] >= prom_resenas[len(prom_resenas)-1][1]:
            prom_resenas.remove(prom_resenas[len(prom_resenas)-1])
        else:
            prom_resenas.remove(prom_resenas[len(prom_resenas)-2])
    # Guardamos el valor más alto de todos
    prom_resenas_ordenado.append(prom_resenas[0])
    prom_resenas = copia_prom_resenas.copy()
    # Quitamos valores que ya ganaron
    for h in range(len(prom_resenas_ordenado)):
        prom_resenas.remove(prom_resenas_ordenado[h])
        
# Calculamos 

# Si el login fue exitoso, se arranca el siguiente código
while entrada == True:
    print("---------------------------------")
    print("¿Qué reporte desea generar?")
    print("1) Productos más vendidos y productos rezagados.")
    print("2) Productos por reseña en el servicio.")
    print("3) Total anual de ingresos y ventas promedio mensuales, con meses con más ventas al año.")
    print("-----------------------------------------------")
    print("4) Salir")
    print("-----------------------------------------------")
    solicitud = input("Ingrese número de acción deseada: ")
    if solicitud == str(1):
        print("-----------------------------------------------------------------------------------")
        print("A continuación se presentan los 50 productos de mayores ventas en orden descendente")
        print("-----------------------------------------------------------------------------------")
        print("# | ID | Nombre                                         | Ventas totales")
        for i in range(50):
            if i < len(resultado_ventas_ordenado):
                print(str(i+1)+" | "+str(resultado_ventas_ordenado[i][0])+" | "+str(lifestore_products[resultado_ventas_ordenado[i][0]-1][1][:35])+"           | "+str(resultado_ventas_ordenado[i][1]))
        print("----------------------------------------------------------------------------------------")
        print("A continuación se presentan los 100 productos con mayores búsquedas en orden descendente")
        print("----------------------------------------------------------------------------------------")
        print("# | ID | Nombre                                         | Búsquedas totales")
        for i in range(100):
            if i < len(resultado_busqueda_ordenado):
                print(str(i+1)+" | "+str(resultado_busqueda_ordenado[i][0])+" | "+str(lifestore_products[resultado_busqueda_ordenado[i][0]-1][1][:35])+"           | "+str(resultado_busqueda_ordenado[i][1]))
        print("-----------------------------------------------------------------------------------")
        print("A continuación se presentan los 50 productos con menores ventas en orden ascendente")
        print("-----------------------------------------------------------------------------------")
        print("# | ID | Nombre                                         | Ventas totales")
        for i in range(50):
            resultado_ventas_inverso = resultado_ventas_ordenado[::-1]
            if i < len(resultado_ventas_inverso):
                print(str(50-i)+" | "+str(resultado_ventas_inverso[i][0])+" | "+str(lifestore_products[resultado_ventas_inverso[i][0]-1][1][:35])+"           | "+str(resultado_ventas_inverso[i][1]))
        print("---------------------------------------------------------------------------------------")
        print("A continuación se presentan los 100 productos con menores búsquedas en orden ascendente")
        print("---------------------------------------------------------------------------------------")
        print("# | ID | Nombre                                         | Búsquedas totales")
        for i in range(100):
            resultado_busqueda_inverso = resultado_busqueda_ordenado[::-1]
            if i < len(resultado_busqueda_inverso):
                print(str(100-i)+" | "+str(resultado_busqueda_inverso[i][0])+" | "+str(lifestore_products[resultado_busqueda_inverso[i][0]-1][1][:35])+"           | "+str(resultado_busqueda_inverso[i][1]))
        print("---------------------------------")
    if solicitud == str(2):
        print("-------------------------------------------------------------------------------------")
        print("A continuación se presentan los 20 productos con mejores reseñas en orden descendente")
        print("-------------------------------------------------------------------------------------")
        print("# | ID | Nombre                                        | Promedio de reseñas")
        for i in range(20):
            if i < len(prom_resenas_ordenado):
                print(str(i+1)+" | "+str(prom_resenas_ordenado[i][0])+" | "+str(lifestore_products[prom_resenas_ordenado[i][0]-1][1][:35])+"           | "+str(prom_resenas_ordenado[i][1])[0:4])
        print("-----------------------------------------------------------------------------------")
        print("A continuación se presentan los 20 productos con peores reseñas en orden ascendente")
        print("-----------------------------------------------------------------------------------")
        print("# | ID | Nombre                                        | Promedio de reseñas")
        for i in range(20):
            prom_resenas_inverso = prom_resenas_ordenado[::-1]
            if i < len(prom_resenas_inverso):
                print(str(i+1)+" | "+str(prom_resenas_inverso[i][0])+" | "+str(lifestore_products[prom_resenas_inverso[i][0]-1][1][:35])+"           | "+str(prom_resenas_inverso[i][1])[0:4])

    if solicitud == str(4):
        print("---------------------------------------")
        print("---------------------------------------")
        print("Se ha cerrado exitosamente el programa.")
        break
