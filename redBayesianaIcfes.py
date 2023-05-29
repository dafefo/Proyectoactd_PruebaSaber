# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:06:22 2023

@author: baka
"""

import numpy as np 
import pandas as pd
import plotly.express as px
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
##################CARGA Y MANIPULACION DE DATOS#####################################################
#Apertura de los datos Daniel
#data_cardiaca = pd.read_csv("Analitica computacional/Proyecto1 Enfermedades cardiacas/cleveland_data.csv")

#Apertura datos Christer
#data_cardiaca = pd.read_csv("C:/Users/baka/Desktop/analitica/Proyectos/Proyecto_prediccion_enfermedades_cardiacas__actd/cleveland_data.csv")
#datos_icfes = pd.read_csv("C:/Users/cob91/Desktop/p3 analitica/Datos_PruebaSaber.csv")
datos_icfes = pd.read_csv("C:/Users/dafef/OneDrive - Universidad de los Andes/Decimo Semestre/Analitica computacional/Proyecto 3 Pruebas Saber 11/Datos_modelo.csv")
datos_icfes = datos_icfes.dropna()
print(len(datos_icfes))

#datos_icfes = datos_icfes.drop('cole_area_ubicacion', axis=1)
#datos_icfes = datos_icfes.drop('cole_cod_depto_ubicacion', axis=1)
#datos_icfes = datos_icfes.drop('cole_cod_mcpio_ubicacion', axis=1)
#datos_icfes = datos_icfes.drop('fami_cuartoshogar', axis=1)
#datos_icfes = datos_icfes.drop('fami_educacionpadre', axis=1)
#datos_icfes = datos_icfes.drop('fami_personashogar', axis=1)
#datos_icfes = datos_icfes.drop('estu_depto_reside', axis=1)


#datos_icfes = datos_icfes.drop('cole_bilingue', axis=1)
#datos_icfes = datos_icfes.drop('cole_jornada', axis=1)
#datos_icfes = datos_icfes.drop('fami_tienelavadora', axis=1)
#datos_icfes = datos_icfes.drop('fami_tieneautomovil', axis=1)
#datos_icfes = datos_icfes.drop('fami_tienecomputador', axis=1)

estadisticas = datos_icfes.describe()

#Discretizar las variables
#print(np.quantile(datos_icfes["punt_global"],0.25))
conditions = [
    datos_icfes['punt_global'] < 219,
    (datos_icfes['punt_global'] >= 219) & (datos_icfes['punt_global'] < 253),
    (datos_icfes['punt_global'] >= 253) & (datos_icfes['punt_global'] < 290),
    datos_icfes['punt_global'] >= 290
]
values = ['0%-25%', '25%-50%', '50%-75%','75%-100%']

# Use np.select to create the new "global" column
datos_icfes['global'] = np.select(conditions, values)

datos_icfes = datos_icfes.drop('punt_global', axis=1)
nombreColumnas= datos_icfes.columns
tipoColumnas= datos_icfes.dtypes

icfes_prueba= datos_icfes.tail(1000)
datos_icfes.drop(datos_icfes.tail(1000).index,inplace=True)
#Crear la lista negra para el modelo
bl=[]
causas =nombreColumnas[:-1]
#Quitar relaciones de que global permite saber informacion previa
for i in causas:
    bl.append(('global',i))

#Quitar relacion de que cualquier variable da informacion del genero
for i in causas:
    bl.append((i,'estu_genero'))
#Quitar relaciones de que el colegio va a dar informacion sobre la familia
colegio = nombreColumnas[0:7]
familia = nombreColumnas[8:17]
for i in familia:
    for j in colegio:
        bl.append((j,i))
#Quitar informacion de que la familia da informacion sobre el colegio
for i in familia:
    for j in colegio:
        bl.append((i,j))

arcos=[]

for i in causas:
    arcos.append((i,"global"))

#arcos.remove(('estu_depto_reside', 'global'))

#########RED BAYESIANA################################################
#Se crea el modelo Bayesiano
'''model = BayesianNetwork(arcos)
emv = MaximumLikelihoodEstimator(model=model, data= datos_icfes)

#Esto esta fallando por memoria
model.fit(data=datos_icfes, estimator = MaximumLikelihoodEstimator) 

print(model.nodes())

for i in model.nodes():
    print(model.get_cpds(i))
    
model.check_model()
print(model)
print(model.nodes())
print(model.edges())

scoring_method = K2Score(data=datos_icfes)
print(scoring_method.score(model))

infer = VariableElimination(model)
#posterior_p = infer.query(["global"], evidence={"cole_bilingue": "N", "cole_calendario":"A", "cole_caracter": "ACADÉMICO", "cole_genero": "MIXTO", "cole_jornada": "TARDE", "cole_naturaleza": "OFICIAL", "estu_genero": "F", "cole_jornada": "TARDE", "fami_educacionmadre": "Ninguno", "fami_estratovivienda": "Estrato 1", "fami_tieneautomovil": "No", "fami_tienecomputador": "No", "fami_tieneinternet": "No", "fami_tienelavadora": "No"})
posterior_p = infer.query(["global"], evidence={ "cole_calendario":"A", "cole_caracter": "ACADÉMICO", "cole_genero": "MIXTO",  "cole_naturaleza": "OFICIAL", "estu_genero": "F", "fami_educacionmadre": "Ninguno", "fami_estratovivienda": "Estrato 1", "fami_tieneinternet": "No"})
print(posterior_p)
#prob de verdadero
print(posterior_p.values)'''
#####K2##########################

from pgmpy.estimators import HillClimbSearch
from pgmpy.estimators import K2Score

scoring_method = K2Score(data=datos_icfes)
esth = HillClimbSearch(data=datos_icfes)
estimated_modelh = esth.estimate(
    scoring_method=scoring_method, max_indegree=3, max_iter=int(500), black_list=(bl)
)
modeloK2p=estimated_modelh
print(estimated_modelh)
print(estimated_modelh.nodes())
print(estimated_modelh.edges())

print(scoring_method.score(estimated_modelh))

#calcular las probabilidades condicionales
estimated_modelh=BayesianNetwork(estimated_modelh)
estimated_modelh.fit(data=datos_icfes, estimator = MaximumLikelihoodEstimator)     
estimated_modelh.check_model()

##############Serializacion############
from pgmpy.readwrite import BIFWriter
writer = BIFWriter(estimated_modelh)
writer.write_bif(filename='modeloK2.bif')

from pgmpy.readwrite import XMLBIFWriter
# write model to an XML BIF file 
writer = XMLBIFWriter(estimated_modelh)
writer.write_xmlbif('modeloK2.xml')

##Validación modelo
datos_icfes_vali = pd.read_csv("C:/Users/dafef/OneDrive - Universidad de los Andes/Decimo Semestre/Analitica computacional/Proyecto 3 Pruebas Saber 11/Datos_Validacion.csv")
datos_icfes_vali = datos_icfes_vali.dropna()
print(len(datos_icfes_vali))
conditions = [
    datos_icfes_vali['punt_global'] < 219,
    (datos_icfes_vali['punt_global'] >= 219) & (datos_icfes_vali['punt_global'] < 253),
    (datos_icfes_vali['punt_global'] >= 253) & (datos_icfes_vali['punt_global'] < 290),
    datos_icfes_vali['punt_global'] >= 290
]
values = ['0%-25%', '25%-50%', '50%-75%','75%-100%']

# Use np.select to create the new "global" column
datos_icfes_vali['global'] = np.select(conditions, values)

datos_icfes_vali = datos_icfes_vali.drop('punt_global', axis=1)

def process_data(datosPrueba, pModelo):
    inferencia = VariableElimination(pModelo)
    V1=0
    V2=0
    V3=0
    V4=0
    F=0
    
    for index, row in datosPrueba.iterrows():
        #Obtener el valor de las varaibles
        col_ubicacion=row['cole_area_ubicacion']
        col_bilingue = row['cole_bilingue']
        col_cale = row['cole_calendario']
        col_carac = row['cole_caracter']
        col_genero = row['cole_genero']
        col_jor = row['cole_jornada']
        col_nat = row['cole_naturaleza']
        est_genero = row["estu_genero"]
        fcuartos = row["fami_cuartoshogar"]
        fedumadre = row["fami_educacionmadre"]
        fedupadre = row["fami_educacionpadre"]
        festrato = row["fami_estratovivienda"]
        fpersonas = row["fami_personashogar"]
        fauto = row["fami_tieneautomovil"]
        fcompu = row["fami_tienecomputador"]
        finternet = row["fami_tieneinternet"]
        flavadora = row["fami_tienelavadora"]
        pglobal = row["global"]
        
        pp = inferencia.query(["global"], evidence={"cole_area_ubicacion": col_ubicacion, "cole_bilingue":col_bilingue, "cole_calendario": col_cale, "cole_caracter": col_carac, "cole_genero": col_genero, "cole_jornada": col_jor, "cole_naturaleza": col_nat, "estu_genero": est_genero, "fami_cuartoshogar": fcuartos, "fami_educacionmadre": fedumadre, "fami_educacionpadre": fedupadre, "fami_estratovivienda": festrato, "fami_personashogar":fpersonas, "fami_tieneautomovil": fauto, "fami_tienecomputador":fcompu, "fami_tieneinternet":finternet,"fami_tienelavadora":flavadora})
        pmax = np.argmax(pp.values)
        estadomax = pp.state_names['global'][pmax]
        
        #Verdaderos Positivos
        if (pglobal== "0%-25%" and estadomax == "0%-25%"):
            V= V+1
        elif (pglobal== "25%-50%" and estadomax == "25%-50%"):
            V= V+1
        elif (pglobal== "50%-75%" and estadomax == "50%-75%"):
            V= V+1
        elif (pglobal== "75%-100%" and estadomax == "75%-100%"):
            V= V+1
        
        #Falos
        else:
            F = F+1
    return V,F

ResultadoK2 = process_data(icfes_prueba,estimated_modelh)

a = 1











