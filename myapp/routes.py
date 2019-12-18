from myapp import app
from flask import render_template
import csv



@app.route("/")
def index():
    '''
    leer el fichero sales10.csv y transformarlo en un diccionario
    '''
    
    fSales = open('./data/sales10.csv','r')

    csvreader = csv.reader(fSales, delimiter=',')
    registros = []
    for linea in csvreader:
        registros.append(linea)
        print(linea)

    cabecera = registros[0]

    ventas = []
    for datos in registros[1:]:
        d = {}
        for ix, nombre_campo in enumerate(cabecera): 
            d[nombre_campo] = datos[ix]
        ventas.append(d)


    '''
    procesarlo para obtener los totales
    '''
    datos = {}
    for linea in ventas:
        if linea['region'] in datos:
            regAct = datos[linea['region']]
            regAct['ingresos_totales'] += float(linea['ingresos_totales'])
            regAct['beneficios_totales'] += float(linea['beneficio'])
        else:
            datos[linea['region']] = {'ingresos_totales': float(linea['ingresos_totales']), 'beneficios_totales': float(linea['beneficio'])}
    '''
    {'region': 'Australia and Oceania', 'ingresos_totales': 3292856.72, 'beneficios_totales': 1236498.14}
    {'region': ...}
    '''
    resultado = []
    for clave in datos:
        resultado.append((clave, datos[clave]))


    '''
    enviarlo a index.html
    '''

    return render_template('index.html', registros=resultado)

@app.route("/detail")
def detail():
    return render_template('detail.html')