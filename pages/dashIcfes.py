# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:00:12 2023

@author: cob91
"""

import dash
from dash import dcc, html, callback
from pgmpy.inference import VariableElimination
from pgmpy.readwrite import XMLBIFReader
from dash.dependencies import Input, Output, State
#reader = XMLBIFReader("C:/Users/cob91/Desktop/p3 analitica/modeloK2.xml")
#reader = XMLBIFReader("Analitica computacional/Proyecto 3 Prueba Saber/modelok2.xml")
reader = XMLBIFReader("modelok2.xml")
model = reader.get_model()

# Retrieve the states for each variable
variable_states = {}
for variable in model.nodes:
    cpd = model.get_cpds(variable)
    states = cpd.state_names[variable]
    variable_states[variable] = states

# Print the states for each variable
for variable, states in variable_states.items():
    print(f"Variable: {variable}, States: {states}")





listaPrueba=['URBANO', 'N', 'A', 'ACAD_MICO', 'FEMENINO', 'SABATINA', 'NO_OFICIAL', 'F', 'Uno', 'Educaci_n_profesional_completa', 'Educaci_n_profesional_completa', 'Estrato_1', 'Una', 'Si', 'Si', 'Si', 'Si', 'RURAL', 'S', 'B', 'T_CNICO', 'MASCULINO', 'SABATINA', 'OFICIAL', 'M', 'Dos', 'Educaci_n_profesional_incompleta', 'Educaci_n_profesional_incompleta', 'Estrato_2', 'Dos', 'No', 'No', 'No', 'No']
listaPrueba2=['URBANO', 'S', 'B', 'ACAD_MICO', 'MASCULINO', 'MA_ANA', 'NO_OFICIAL', 'M', 'Tres', 'Educaci_n_profesional_completa', 'Educaci_n_profesional_completa', 'Estrato_4', 'Dos', 'Si', 'Si', 'Si', 'Si']
infer = VariableElimination(model)

def calcularProbabilidad(selected_values_list):
    probabilidadEstimada=infer.query(["global"], evidence={"cole_area_ubicacion": selected_values_list[0], "cole_bilingue":selected_values_list[1], "cole_calendario": selected_values_list[2], "cole_caracter": selected_values_list[3], "cole_genero": selected_values_list[4], "cole_jornada":selected_values_list[5] , "cole_naturaleza":selected_values_list[6] , "estu_genero":selected_values_list[7], "fami_cuartoshogar":selected_values_list[8] , "fami_educacionmadre":selected_values_list[9] , "fami_educacionpadre":selected_values_list[10],"fami_estratovivienda":selected_values_list[11],"fami_personashogar":selected_values_list[12],"fami_tieneautomovil":selected_values_list[13],"fami_tienecomputador":selected_values_list[14],"fami_tieneinternet":selected_values_list[15],"fami_tienelavadora":selected_values_list[16]})
    return probabilidadEstimada



print(calcularProbabilidad(listaPrueba2))



dash.register_page(__name__, name='Predicción')

layout = html.Div([
    html.H1('Ingrese sus datos'),
    html.Label('Área de ubicación del colegio:'),
    dcc.Dropdown(
        id='dropdown-1',
        options=[
            {'label': 'Rural', 'value': 'RURAL'},
            {'label': 'Urbano', 'value': 'URBANO'}
        ],
        value=''
    ),
    html.Label('¿su colegio es bilingüe?:'),
    dcc.Dropdown(
        id='dropdown-2',
        options=[
            {'label': 'No', 'value': 'N'},
            {'label': 'Si', 'value': 'S'}
        ],
        value=''
    ),
    html.Label('Calendario del colegio:'),
    dcc.Dropdown(
        id='dropdown-3',
        options=[
            {'label': 'A', 'value': 'A'},
            {'label': 'B', 'value': 'B'},
            {'label': 'OTRO', 'value': 'OTRO'}
        ],
        value=''
    ),
    html.Label('Caracter del colegio:'),
    dcc.Dropdown(
        id='dropdown-4',
        options=[
            {'label': 'ACADÉMICO', 'value': 'ACAD_MICO'},
            {'label': 'TÉCNICO', 'value': 'T_CNICO'},
            {'label': 'TÉCNICO/ACADÉMICO', 'value': 'T_CNICO/ACAD_MICO'},
            {'label': 'NO APLICA', 'value': 'NO_APLICA'}
        ],
        value=''
    ),
    html.Label('Género del colegio:'),
    dcc.Dropdown(
        id='dropdown-5',
        options=[
            {'label': 'FEMENINO', 'value': 'FEMENINO'},
            {'label': 'MASCULINO', 'value': 'MASCULINO'},
            {'label': 'MIXTO', 'value': 'MIXTO'}
        ],
        value=''
    ),
    html.Label('Jornada del colegio:'),
    dcc.Dropdown(
        id='dropdown-6',
        options=[
            {'label': 'MAÑANA', 'value': 'MA_ANA'},
            {'label': 'NOCHE', 'value': 'NOCHE'},
            {'label': 'SABATINA', 'value': 'SABATINA'},
            {'label': 'TARDE', 'value': 'TARDE'},
            {'label': 'ÚNICA', 'value': 'UNICA'}
        ],
        value=''
    ),
    
    html.Label('Naturaleza del colegio:'),
    dcc.Dropdown(
        id='dropdown-7',
        options=[
            {'label': 'NO OFICIAL', 'value': 'NO_OFICIAL'},
            {'label': 'OFICIAL', 'value': 'OFICIAL'}
        ],
        value=''
    ),
    html.Label('Género:'),
    dcc.Dropdown(
        id='dropdown-8',
        options=[
            {'label': 'FEMENINO', 'value': 'F'},
            {'label': 'MASCULINO', 'value': 'M'}
        ],
        value=''
    ),
    html.Label('Número de cuartos en su hogar:'),
    dcc.Dropdown(
        id='dropdown-9',
        options=[
            {'label': '1', 'value': 'Uno'},
            {'label': '2', 'value': 'Dos'},
            {'label': '3', 'value': 'Tres'},
            {'label': '4', 'value': 'Cuatro'},
            {'label': '5', 'value': 'Cinco'},
            {'label': '6', 'value': 'Seis'},
            {'label': '7', 'value': 'Siete'},
            {'label': '8', 'value': 'Ocho'},
            {'label': '9', 'value': 'Nueve'},
            {'label': '10 o más', 'value': 'Diez_o_m_s'}
        ],
        value=''
    ),
    html.Label('Educación madre:'),
    dcc.Dropdown(
        id='dropdown-10',
        options=[
            {'label': 'Educación profesional completa', 'value': 'Educaci_n_profesional_completa'},
            {'label': 'Educación profesional incompleta', 'value': 'Educaci_n_profesional_incompleta'},
            {'label': 'Ninguno', 'value': 'Ninguno'},
            {'label': 'No sabe', 'value': 'No_sabe'},
            {'label': 'Postgrado', 'value': 'Postgrado'},
            {'label': 'Primaria completa', 'value': 'Primaria_completa'},
            {'label': 'Primaria incompleta', 'value': 'Primaria_incompleta'},
            {'label': 'Secundaria (Bachillerato) completa', 'value': 'Secundaria_Bachillerato_completa'},
            {'label': 'Secundaria (Bachillerato) incompleta', 'value': 'Secundaria_Bachillerato_incompleta'},
            {'label': 'Técnica o tecnológica completa', 'value': 'T_cnica_o_tecnol_gica_completa'},
            {'label': 'Técnica o tecnológica incompleta', 'value': 'T_cnica_o_tecnol_gica_incompleta'}
        ],
        value=''
    ),
    html.Label('Educación padre:'),
    dcc.Dropdown(
        id='dropdown-11',
        options=[
            {'label': 'Educación profesional completa', 'value': 'Educaci_n_profesional_completa'},
            {'label': 'Educación profesional incompleta', 'value': 'Educaci_n_profesional_incompleta'},
            {'label': 'Ninguno', 'value': 'Ninguno'},
            {'label': 'No sabe', 'value': 'No_sabe'},
            {'label': 'Postgrado', 'value': 'Postgrado'},
            {'label': 'Primaria completa', 'value': 'Primaria_completa'},
            {'label': 'Primaria incompleta', 'value': 'Primaria_incompleta'},
            {'label': 'Secundaria (Bachillerato) completa', 'value': 'Secundaria_Bachillerato_completa'},
            {'label': 'Secundaria (Bachillerato) incompleta', 'value': 'Secundaria_Bachillerato_incompleta'},
            {'label': 'Técnica o tecnológica completa', 'value': 'T_cnica_o_tecnol_gica_completa'},
            {'label': 'Técnica o tecnológica incompleta', 'value': 'T_cnica_o_tecnol_gica_incompleta'}
        ],
        value=''
    ),
    
    html.Label('Estrato vivienda:'),
    dcc.Dropdown(
        id='dropdown-12',
        options=[
            {'label': 'Estrato 1', 'value': 'Estrato_1'},
            {'label': 'Estrato 2', 'value': 'Estrato_2'},
            {'label': 'Estrato 3', 'value': 'Estrato_3'},
            {'label': 'Estrato 4', 'value': 'Estrato_4'},
            {'label': 'Estrato 5', 'value': 'Estrato_5'},
            {'label': 'Estrato 6', 'value': 'Estrato_6'},
            {'label': 'Sin Estrato', 'value': 'Sin_Estrato'}
           
        ],
        value=''
    ),
    
    html.Label('Cantidad de personas que viven en su hogar:'),
    dcc.Dropdown(
        id='dropdown-13',
        options=[
            {'label': '1', 'value': 'Una'},
            {'label': '2', 'value': 'Dos'},
            {'label': '3', 'value': 'Tres'},
            {'label': '4', 'value': 'Cuatro'},
            {'label': '5', 'value': 'Cinco'},
            {'label': '6', 'value': 'Seis'},
            {'label': '7', 'value': 'Siete'},
            {'label': '8', 'value': 'Ocho'},
            {'label': '9', 'value': 'Nueve'},
            {'label': '10', 'value': 'Diez'}
           
        ],
        value=''
    ),
    html.Label('¿Tiene automovil?'),
    dcc.Dropdown(
        id='dropdown-14',
        options=[
            {'label': 'Si', 'value': 'Si'},
            {'label': 'No', 'value': 'No'}
           
        ],
        value=''
    ),
    html.Label('¿Tiene computador?'),
    dcc.Dropdown(
        id='dropdown-15',
        options=[
            {'label': 'Si', 'value': 'Si'},
            {'label': 'No', 'value': 'No'}
           
        ],
        value=''
    ),
    html.Label('¿Tiene Internet?'),
    dcc.Dropdown(
        id='dropdown-16',
        options=[
            {'label': 'Si', 'value': 'Si'},
            {'label': 'No', 'value': 'No'}
           
        ],
        value=''
    ),
    html.Label('¿Tiene Lavadora?'),
    dcc.Dropdown(
        id='dropdown-17',
        options=[
            {'label': 'Si', 'value': 'Si'},
            {'label': 'No', 'value': 'No'}
           
        ],
        value=''
    ),
    
    
    
    html.Button('Dar Resultado', id='store-button', n_clicks=0),
    html.Div(id='output-div')
])

selected_options = []

@callback(
    Output('output-div', 'children'),
    Input('store-button', 'n_clicks'),
    State('dropdown-1', 'value'),
    State('dropdown-2', 'value'),
    State('dropdown-3', 'value'),
    State('dropdown-4', 'value'),
    State('dropdown-5', 'value'),
    State('dropdown-6', 'value'),
    State('dropdown-7', 'value'),
    State('dropdown-8', 'value'),
    State('dropdown-9', 'value'),
    State('dropdown-10', 'value'),
    State('dropdown-11', 'value'),
    State('dropdown-12', 'value'),
    State('dropdown-13', 'value'),
    State('dropdown-14', 'value'),
    State('dropdown-15', 'value'),
    State('dropdown-16', 'value'),
    State('dropdown-17', 'value')
)
def store_selection(n_clicks, option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, option11, option12, option13, option14, option15, option16, option17):
    global selected_options
    if n_clicks > 0:
        selected_options.append(option1)
        selected_options.append(option2)
        selected_options.append(option3)
        selected_options.append(option4)
        selected_options.append(option5)
        selected_options.append(option6)
        selected_options.append(option7)
        selected_options.append(option8)
        selected_options.append(option9)
        selected_options.append(option10)
        selected_options.append(option11)
        selected_options.append(option12)
        selected_options.append(option13)
        selected_options.append(option14)
        selected_options.append(option15)
        selected_options.append(option16)
        selected_options.append(option17)
        print("Lista Guardada")
        print(selected_options)
        print("lista de lo que se selecciono en el dash")
        print( calcularProbabilidad(selected_options).values)
        print("Resultados")
        print( calcularProbabilidad(selected_options))
        resul= calcularProbabilidad(selected_options)
        selected_options.clear()
    
        
        return html.Div([
            html.H3('Probabilidades:'),
            #html.Ul(print(selected_options)),
            html.Ul("0 a 25%: " + str(   round(resul.values[0],2))),
            html.Br(),
            html.Ul("25 a 50%: " +str(round(resul.values[1],2))),
            html.Br(),
            html.Ul("50 a 75%: " +str(round(resul.values[2],2))),
            html.Br(),
            html.Ul("75 a 100%: " +str(round(resul.values[3],2)))
            #html.Ul(html_string)
        ])