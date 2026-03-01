class SecuenciaADN:
    def __init__(self, id, nombre_secuencia: str, secuencia: str, nivel_riesgo: int):
        self.id = id
        self.nombre_secuencia : str = nombre_secuencia
        self.secuencia: str = secuencia 
        self.nivel_riesgo: int = nivel_riesgo

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





    








        