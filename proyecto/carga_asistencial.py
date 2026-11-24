import json

usuarios=("/home/camper/Documentos/proyecto/acme_clinic.json")

consultas_doctor1=0
consultas_doctor2=0

pacientes_distintos=[]

def leer_consultas():
    with open(usuarios,"r",encoding="utf-8")as archivo:
        for i in archivo:
           if i=="consultas"["nombre_completo":"Juan Médico"]:
            consultas_doctor1+=1
           elif i=="consultas"["nombre_completo":"juan mantilla"]:
              consultas_doctor2+=1
        maximo=max(consultas_doctor1,consultas_doctor2)
        return maximo

print (leer_consultas())

def diferenciar_pacientes():
   with open(usuarios,"r",encoding="utf-8")as archivo:
      pass