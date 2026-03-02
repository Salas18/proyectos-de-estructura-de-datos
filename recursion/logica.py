class SecuenciaADN:
    def __init__(self, id, nombre_secuencia: str, secuencia: str, nivel_riesgo: int):
        self.id = id
        self.nombre_secuencia : str = nombre_secuencia
        self.secuencia: str = secuencia 
        self.nivel_riesgo: int = nivel_riesgo

    def __repr__(self):
        return f"({self.nombre_secuencia} - {self.secuencia})"

def registrar_secuencias(lista, nuevo_objeto):
        if len(lista) == 0:
            return [nuevo_objeto]
        
        primer_elemento = [lista[0]]
        resto_lista = lista[1:]

        return primer_elemento + registrar_secuencias(resto_lista, nuevo_objeto)

def contar_ocurrencias(patron, secuencia):
    if len(secuencia) < len(patron):
        return 0
    
    p = secuencia[0:len(patron)]
    
    if p == patron:
        coincidencia = 1
    else:
        coincidencia = 0

    return coincidencia + contar_ocurrencias(patron, secuencia[1:])

def riesgo_promedio(lista, acum=0, cant=0):
    if len(lista) == 0:
        if cant == 0:
            return 0
        return acum / cant
        
    riesgo_actual = lista[0].nivel_riesgo
    
    return riesgo_promedio(lista[1:], acum + riesgo_actual, cant + 1)

def secuencia_mas_larga(lista, l):
    if len(lista) == 0:
        return l 
    
    if len(lista[0].secuencia) > len(l.secuencia):
        l = lista[0]

    return secuencia_mas_larga(lista[1:], l)

def generar_subcadenas_de_secuencia(secuencia, corte, lista):
    if corte > len(secuencia):
        return lista 
    fragmento = secuencia[0:corte]
    l = lista + [fragmento]

    return generar_subcadenas_de_secuencia(secuencia, corte + 1, l)

def obtener_todas_secuencias(secuencia, lista_final):
    if len(secuencia) == 0:
        return lista_final
    caja_actualizada = generar_subcadenas_de_secuencia(secuencia, 1 , lista_final)

    return obtener_todas_secuencias(secuencia[1:], caja_actualizada)


def contar_nucleotidos(ADN):
    if len(ADN) == 0:
        return 0
    
    cont = 0
    if ADN[0] == "A":
        cont = 1
    elif ADN[0] == "T":
        cont = -1 
    
    return cont + contar_nucleotidos(ADN[1:])

def mutacion_genetica(secuencia):
    if len(secuencia) == 0:
        return ""
    
    letra_mutada = secuencia[0]

    if letra_mutada == "A":
        letra_mutada = "T"
    elif letra_mutada == "T":
        letra_mutada = "A"
    
    return letra_mutada + mutacion_genetica(secuencia[1:])



seq1 = SecuenciaADN(1, "Prueba", "AGTC", 20)
lista_prueba = [seq1]

print("1. Registrar:", registrar_secuencias(lista_prueba, seq1))
print("2. Ocurrencias de 'AT':", contar_ocurrencias("AT", "ATGCATGCAT"))
print("3. Riesgo promedio:", riesgo_promedio(lista_prueba))
print("4. Secuencia más larga:", secuencia_mas_larga(lista_prueba, seq1).secuencia)
print("5. Subcadenas de 'ATC':", obtener_todas_secuencias("ABC", []))
print("6. ¿Más A que T en 'AGTTGCAT'?:", contar_nucleotidos("AGTTGCAT")> 0)
print("7. Mutar 'AGTC':", mutacion_genetica("AGTC"))








    







        