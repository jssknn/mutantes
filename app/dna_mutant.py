import numpy as np
import re

class DNAException(Exception):
    pass

class DNACheck:
    def isValid(matrix=[]):
            #funcion para verificar que las letras ingresadas sean A, T, G o C
            def check_regex(array_string):
                error = 0
                for dna_string in array_string:
                    if not re.match("^([ATGC]*)$",dna_string):
                        error = 1
                    if error:
                        break
                return not error
            #validación de parámetros en json
            if not matrix :
                raise DNAException("Faltan ingresar parámetros")
            #validación de matriz en json
            if not matrix['dna']:
                raise DNAException("Falta ingresar matriz")  

            #validación de matriz NxN
            if not all([len(matrix['dna']) == len(h) for h in matrix['dna']]):
                raise DNAException("La matriz debe tener misma cantidad de filas y columnas")
            #validación de letras ATGC
            if not check_regex(matrix['dna']):
                raise DNAException("Solo se permiten las letras A, T, G y C")
            return True

    def isMutant(matrix=[]):                        
            is_mutant = None
            contador = 0
            matrix_order = len(matrix['dna'])
            dnas_mutant = ['AAAA','CCCC','TTTT','GGGG']
            #Busqueda horizontal
            for dna_word in matrix['dna']:
                contador += sum(dna_word.count(dnas) for dnas in dnas_mutant)
                if contador > 1:
                    is_mutant = True
                    break
            #Busqueda verical    
            if not is_mutant:
                array_string = [[arg for arg in matrix['dna'][i]] for i in range(matrix_order)]
                vertical = np.transpose(array_string).tolist()
                for dna_word in vertical:
                    word = ''.join(dna_word)
                    contador += sum(word.count(dnas) for dnas in dnas_mutant)
                    if contador > 1:
                        is_mutant = True
                        break
            #Busqueda diagonal supizq a infder        
            if not is_mutant:
                diagonal1 = [np.diag(array_string, i).tolist() for i in range(-matrix_order+1,
					matrix_order) if len(np.diag(array_string, i)) > 3]
                for dna_word in diagonal1:
                    word = ''.join(dna_word)
                    contador += sum(word.count(dnas) for dnas in dnas_mutant)
                    if contador > 1:
                        is_mutant = True
                        break
            #Busqueda diagonal supder a infizq         
            if not is_mutant:
                diagonal2 = [np.diag(np.fliplr(array_string), i).tolist() for i in range(-matrix_order+1,
					matrix_order) if len(np.diag(np.fliplr(array_string), i)) > 3]  
                for dna_word in diagonal2:
                    word = ''.join(dna_word)
                    contador += sum(word.count(dnas) for dnas in dnas_mutant)
                    if contador > 1:
                        is_mutant = True
                        break
            if is_mutant == None:
                is_mutant = False        
            return is_mutant