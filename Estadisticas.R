library(readr)
library(dplyr)
Resultados <- read_csv("ResultadosQuery.csv")
rm(ResultadosQuery)

Resultados1 <- na.omit(Resultados)
rm(Resultados)

unique(Resultados1$cole_area_ubicacion)
#SOlo hay Urbajo y Rural
unique(Resultados1$cole_bilingue)
#Solo hay N y S
unique(Resultados1$cole_calendario)
#Solo hay A, Otro, B

unique(Resultados1$cole_caracter)
#Hay tecnico/Academico, Academico, Tecnico, No aplica

unique(Resultados1$cole_cod_depto_ubicacion)
#Solo estan los 33 departamentos

unique(Resultados1$cole_genero)
#Solo hay Mixto, Femenino y Masculino

unique(Resultados1$cole_jornada)
#Hay "MAÑANA"   "UNICA"    "COMPLETA" "TARDE"    "SABATINA" "NOCHE" 

unique(Resultados1$cole_naturaleza)
#Hay "OFICIAL"    "NO OFICIAL"

unique(Resultados1$estu_estudiante)
Resultados1 <- Resultados1[-11]
#Solo hay uno Hay que eliminar esta variable

unique(Resultados1$estu_genero)
#Hay M y F

unique(Resultados1$fami_cuartoshogar)
#"Tres" "Dos" "Seis o mas""Uno""Cuatro" "Cinco" "Ocho" "Siete" "Seis" "Diez o más" "Nueve"  
Resultados1 <- Resultados1%>%filter(fami_cuartoshogar!="Seis o mas")

unique(Resultados1$fami_educacionpadre)

unique(Resultados1$fami_personashogar)
Resultados2 <- Resultados1%>%filter(fami_personashogar!="Cuatro")

unique(Resultados1$fami_tieneautomovil)

unique(Resultados1$fami_tienecomputador)

unique(Resultados1$fami_tieneinternet)

unique(Resultados1$fami_tienelavadora)

modelo_ANOVA <- aov(punt_global~cole_area_ubicacion + cole_bilingue + cole_calendario+cole_caracter + cole_genero+cole_jornada + cole_naturaleza + estu_genero + fami_cuartoshogar + fami_educacionmadre + fami_educacionpadre + fami_estratovivienda + fami_personashogar + fami_tieneautomovil + fami_tienecomputador + fami_tieneinternet + fami_tienelavadora, data = Resultados1)

summary(modelo_ANOVA)

#Revisar supuestos
#Normalidad
library(nortest)
ad.test(sqrt(Resultados1$punt_global))
hist(sqrt(Resultados1$punt_global))

kruskal.test(Resultados1$punt_global, Resultados1$cole_caracter)

quantile(Resultados1$punt_global)
