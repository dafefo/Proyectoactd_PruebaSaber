import pandas as pd
import numpy as np
import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc


#Apertura de los datos
datos_risaralda = pd.read_csv('Analitica Computacional/Proyecto 3 Pruebas Saber/Datos_Risaralda.csv')
fechas = [20151,20152,20161,20162,20171,20172,20181,20191,20194,20201,20211,20224]
fechas1 = list(map(str, fechas))
dash.register_page(__name__, path='/', name='Análisis Descriptivo') # '/' is home page

# page 1 data
layout = dbc.Container([
    #dbc.Row([
    #    dbc.Col([
    #        html.H1("Prueba Saber 11 Departamento de Risaralda", style={'textAling':'center'})
    #    ], width = 12)
    #]),
    dbc.Row([
        dbc.Col([
            html.H5("Selecciones los años que desea analizar",style={'textAling':'center'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.RangeSlider(min = 0,max = len(fechas)-1, marks={i: fechas1[i] for i in range(len(fechas))}, id = 'range_a')
        ])
    ],justify="center"),
    dbc.Row([
        dbc.Col([
            html.Label("Seleccione la variable que quiere analizar"),
            dcc.Dropdown(options=[
                {'label':'Serie de Tiempo', 'value':'SerieT'},
                {'label':'Educación de la madre','value':'edumad'},
                {'label':'Educación del padre','value':'edupad'},
                {'label':'Estarto de vivienda','value':'estrato'},
                {'label':'Internet','value':'internet'},
                {'label':'Lavadora','value':'lavadora'},
                {'label':'Automovil','value':'auto'},
                {'label':'Computador','value':'compu'},
                {'label':'Genero del estudiante','value':'genero'},
                {'label':'Colegio Bilingue','value':'colebil'},
                {'label':'Calendario Académico','value':'colecalen'},
                {'label':'Genero del Colegio','value':'colegenero'},
            ], value="Serie de Tiempo", id = "dropdown1")
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = "grafica1", figure={})
        ], width=12)
    ])


])

@callback(
    Output(component_id = 'grafica1',component_property='figure'),
    Input(component_id='range_a',component_property= 'value'),
    Input(component_id="dropdown1", component_property='value')
)
def update_graphs(range_fechas,variable):
    fechas_esco = fechas[range_fechas[0]:range_fechas[1]+1]
    df = datos_risaralda[(datos_risaralda["periodo"].isin(fechas_esco))]
    if variable == "SerieT":
        dff = df[['periodo','punt_global']]
        dff = dff.groupby(['periodo']).mean().reset_index()
        fig = px.line(x = dff['periodo'], y=dff['punt_global'])
    elif variable == "edumad":
        dff = df[['fami_educacionmadre','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['fami_educacionmadre']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(x=dff['punt_global'], y=dff['fami_educacionmadre'], orientation='h')
    elif variable == "edupadre":
        dff = df[['fami_educacionpadre','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['fami_educacionpadre']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(x=dff['punt_global'], y=dff['fami_educacionpadre'], orientation='h')
    elif variable == 'estrato':
        dff = df[['fami_estratovivienda','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['fami_estratovivienda']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(x=dff['punt_global'], y=dff['fami_estratovivienda'], orientation='h')
    elif variable == 'internet':
        dff = df[['fami_tieneinternet','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['fami_tieneinternet']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(y=dff['punt_global'], x=dff['fami_tieneinternet'])
    elif variable == 'lavadora':
        dff = df[['fami_tienelavadora','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['fami_tienelavadora']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(y=dff['punt_global'], x=dff['fami_tienelavadora'])
    elif variable == 'auto':
        dff = df[['fami_tieneautomovil','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['fami_tieneautomovil']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(y=dff['punt_global'], x=dff['fami_tieneautomovil'])
    elif variable == 'compu':
        dff = df[['fami_tienecomputador','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['fami_tienecomputador']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(y=dff['punt_global'], x=dff['fami_tienecomputador'])
    elif variable == 'genero':
        dff = df[['estu_genero','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['estu_genero']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(y=dff['punt_global'], x=dff['estu_genero'])
    elif variable == 'colebil':
        dff = df[['cole_bilingue','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['cole_bilingue']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(y=dff['punt_global'], x=dff['cole_bilingue'])
    elif variable == 'colecalen':
        dff = df[['cole_calendario','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['cole_calendario']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(x=dff['punt_global'], y=dff['cole_calendario'], orientation='h')
    elif variable == 'colegenero':
        dff = df[['cole_genero','punt_global']]
        dff = dff.dropna()
        dff = dff.groupby(['cole_genero']).mean().reset_index()
        dff = dff.sort_values(by=['punt_global'], ascending=False)
        fig = px.bar(x=dff['punt_global'], y=dff['cole_genero'], orientation='h')

    return fig
