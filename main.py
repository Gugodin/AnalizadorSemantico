import string
import re
import subprocess, shlex
import sys
from tabnanny import check
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from matplotlib.pyplot import text
import os
 

from view.mainView import Ui_MainWindow

CREAR = 'mkdir'
MOVER = 'cd'
MOSTRAR = 'ls'
EDITAR = 'mv'
REMOVER = 'rm'
CREARA = 'touch'
DIAGONAL = '/'

apuntador = 0
apuntadorC = 0

def comando(entry):

    global apuntador
    global apuntadorC

    if len(entry)!=1:

        if entry[apuntador] == CREAR:
            if len(entry) == 2:
                apuntador += 1

                responseP = isPalabra(entry[apuntador])
                if entry[apuntador] == '..':
                    return 'Error'
                if responseP =='Correcto':
                    return 'Correcto'
                else:
                    return 'Error'
            else: 
                return 'Error'

        elif entry[apuntador] == MOVER:
            if len(entry) == 2:
                apuntador += 1

                if complementoM(entry) == 'Error':
                    
                    return 'Error'
                else:
                    return 'Correcto'
            else: 
                return 'Error'
            
        elif entry[apuntador] == EDITAR:
            if len(entry) == 5:
                apuntador += 1
                # verificar

                response1 = direccion(entry)
                apuntador += 1
                
                apuntadorC = 0
                responseP = isPalabra(entry[apuntador])
                
                apuntador += 1
                response2 = direccion(entry)
                apuntadorC = 0
                
                apuntador += 1
                responseP2 = isPalabra(entry[apuntador])
                

                if response1 is None and response2 is None and responseP =='Correcto' and responseP2 =='Correcto':
                    return 'Correcto'
                else:
                    return 'Error'
            else:
                return 'Error'

        elif entry[apuntador] == REMOVER:
    
            #error index out of range
            apuntador += 1
            responseD = direccion(entry) 
            apuntador += 1
            responseP = isPalabra(entry[apuntador])

       

            if responseD is None and responseP == 'Correcto':
                return 'Correcto'
            else: 
                return 'Error'

        elif entry[apuntador] == CREARA:
            
            apuntador += 1
            responseD = direccion(entry)
            apuntador += 1
            responseP = isPalabra(entry[apuntador])

            print(f'responseP {responseP}')

            if responseD is None and responseP == 'Correcto':
                return 'Correcto'
            else: 
                return 'Error'
        
        elif entry[apuntador] == MOSTRAR:
            
            apuntador += 1    
            #ls -l PERO
            if entry[apuntador] == '-l': 
                apuntador += 1
                
                if  apuntador == len(entry):
                    return 'Correcto'
                
                elif apuntador < len(entry):
                    
                    responseD = ''

                    if entry[apuntador].count('/') == 0:
                        
                        responseD = isPalabra(entry[apuntador])
                        
                    else:
                        
                        responseD = direccion(entry)

                    if responseD is None or responseD == 'Correcto':
                        return 'Correcto'
                    else:
                        return 'Error'
            elif entry[apuntador][0] == DIAGONAL:
                
                responseD = direccion(entry)
                if responseD is None:
                    return 'Correcto'
                else:
                    return 'Error'
            elif string.ascii_letters.__contains__(entry[apuntador][0]):
                return isPalabra(entry[apuntador])

            else:
                return 'Error'

        else:
            return 'Error'
    else:
        
        if entry[apuntador] == MOSTRAR:
            
            apuntador += 1
            #Ls
            if apuntador == len(entry):
               return 'Correcto'
        else:       
        
            return 'Error'

def complementoM(entry):

    global apuntadorC
    nextStr = entry[apuntador]



    if (nextStr[len(nextStr)-1] != DIAGONAL or nextStr[0] != DIAGONAL) and nextStr.count('/') != 0:
        
        return 'Error'
        
    if nextStr[apuntadorC] == DIAGONAL:

        if apuntadorC+1 < len(nextStr):

            apuntadorC += 1
            t = []
            while nextStr[apuntadorC] != DIAGONAL:
                if apuntadorC+1 < len(nextStr):
                    t.append(nextStr[apuntadorC])
                    apuntadorC += 1
                else:
                    return 'Error'
        
            if isPalabra(''.join(t)) == 'Error':
                return 'Error'

            if nextStr[apuntadorC] == DIAGONAL:
                if complementoM(entry) != 'Error':
                    complementoM(entry)
                else:
                    return 'Error'
            else:
                return 'Error'
    
        
    elif string.ascii_letters.__contains__(nextStr[apuntadorC]):
        
        return isPalabra(nextStr)

    elif nextStr[apuntadorC] == '.' and len(nextStr)==1:
        return 'Error'
        
    elif nextStr[apuntadorC] == '.' and nextStr[apuntadorC+1] == '.':
        return 'Correcto'
    else:
        return 'Error'

def direccion(entry):
    global apuntadorC
    nextStr = entry[apuntador]  

    if (nextStr[len(nextStr)-1] != DIAGONAL or nextStr[0] != DIAGONAL)  and nextStr.count('/') != 0:

        return 'Error'

    if nextStr[apuntadorC] == DIAGONAL:
        if apuntadorC+1 < len(nextStr):
            apuntadorC += 1
            t = []
            while nextStr[apuntadorC] != DIAGONAL:
                
                if apuntadorC+1 < len(nextStr):
                    t.append(nextStr[apuntadorC])
                    apuntadorC += 1
                else:
                    return 'Error'
        
            if isPalabra(''.join(t)) == 'Error':
                return 'Error'
               
            if nextStr[apuntadorC] == DIAGONAL:
                if direccion(entry) != 'Error':
                    direccion(entry)
                else:
                    return 'Error'
            else:
                return 'Error'
    else: 
        return 'Error'

def isPalabra(palabra):
    p = re.compile('([a-z]|[A-B]|_|.|-)+')

    if p.fullmatch(palabra) is None: 
        return 'Error'
    else:
        return 'Correcto'

class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tokens= [
        ['crear','mkdir'],
        ['mover','cd'],
        ['mostrar','ls'],
        ['editar','mv'],
        ['remover','rm'],
        ['crearA','touch'],
        ['diagonal','/'],
        ['guion','-'],
        ['guionB','_'],
        ['punto','.'],
        ['numero',list(string.digits)],
        ['letra',list(string.ascii_letters)]
        ]
        self.ui.pushButton.clicked.connect(self.comprobacion)

    def getTockens(self):
        
        command = self.ui.lineEdit.text().strip(' ').split()
        print(f'Comando: {command}')
        listTokens = []
        error = ''
        for i in range(len(command)):
            band = False
            palabra = command[i]

            # print(f'Bandera antes del if {band}')
            for e in range(len(self.tokens)):
                if palabra == self.tokens[e][1]:
                    print(f'Token: {self.tokens[e][0]}')
                    listTokens.append(self.tokens[e][0])
                    band = True
                    break
               

            if band == False:       
                for z in range(len(palabra)):
                    charFinded = False

                    char = palabra[z]

                    # print(char)
                   
                    for e in range(len(self.tokens)):

                        # print(self.tokens[e])

                        if self.tokens[e][0] == 'numero' or self.tokens[e][0] == 'letra':

                            if self.tokens[e][1].count(char) > 0:
                                
                                print(f'Token: {self.tokens[e][0]}')
                                listTokens.append(self.tokens[e][0])
                                band = True
                                charFinded = True
                                break
                        
                        elif char == self.tokens[e][1]:
                            print(f'Token: {self.tokens[e][0]}')
                            listTokens.append(self.tokens[e][0])
                            band = True
                            charFinded = True
                            break

                    if charFinded == False:
                        band = False
                        return f'Cadena invalida\nEl carater siguiente no existe dentro de nuestros tokens {char}'
                                                
            if band == False:
                listTokens.clear()
                if error == '':
                    listTokens.append(f'Cadena invalida\nEl carater siguiente no existe dentro de nuestros tokens {command[i]}')
                else:
                    listTokens.append(error)
                break
        cadenaT = ''

        for i in range(len(listTokens)):
            cadenaT = cadenaT + listTokens[i] + ' '
    
    def comprobacion(self):
        global apuntador
        global apuntadorC

        errorTo = self.getTockens()

        print(errorTo)
        
        if errorTo == None:
            entry = self.ui.lineEdit.text().strip(' ').split()
            response = comando(entry = entry)
            
            self.ui.message.setText(response+' sintacticamente')

            if response == 'Correcto':
            

                # PRIMERO VERIFICAMOS QUE LAS RUTAS SEAN EXISTENTES EN EL COMANDO EXISTAN
                error = verifyRoutesAndArchives(entry)

                print(error) 
                
                prueba = []
                for i in range(len(entry)):
                    palabra = entry[i]
                    
                    if isDirection(palabra):
                        l = list(palabra)
                        if entry[0] =='ls':
                            l.pop(len(l)-1)
                        l.append('"')
                        l.insert(0,'C:')
                        l.insert(0,'"')
                        if entry[0] != 'ls':
                            l.insert(len(l)-1,entry[i+1])
                        # print(l)
                        palabra = ''.join(l)
                        palabra = palabra.replace('/','\\')
                        print(f'Palabra: {palabra}')
                        prueba.append(palabra)

                        entry[i]= palabra
                        
                        # entry.pop()
                        # entry.insert(len(entry), palabra)
                        # print(prueba)


                
                if error == False:

                    # subprocess.call(shlex.split(' mv "C:\\Users\\humbe\\Desktop\\prueba\\c.txt" "C:\\Users\\humbe\\Desktop\\prueba\\a.txt"'))    
                    if entry[0] != 'ls':
                        prueba.insert(0,entry[0])
                        entry = prueba
                        
                    print(entry)
                    if entry[0] == 'ls' or entry[0] == 'mkdir':
                        entry = ' '.join(entry)
                        print(entry)
                        pipe = subprocess.Popen(entry,  stdout=subprocess.PIPE).stdout
                    
                        output = pipe.read()

                        texto = list(output.__str__())
                        # texto[0] = ''
                        texto[0] = ''
                        texto=''.join(texto)
                        texto = texto.replace('\'','')
                        # print(texto)
                        texto = texto.split('\\n')
                        texto = '\n'.join(texto)
                        # print(texto)
                        # texto = texto.replace('\'','')
                        
                        self.ui.consola.setText(texto)
                    elif entry[0]=='rm':
                        entry = ' '.join(entry)
                        subprocess.call(shlex.split(entry))
                        self.ui.consola.setText('Archivo eliminado')
                    elif entry[0]=='mv':
                        entry = ' '.join(entry)
                        print(f'mv entry {entry}')
                        subprocess.call(shlex.split(entry))
                        self.ui.consola.setText('Archivo editado')
                    elif entry[0]=='touch':
                        entry = ' '.join(entry)
                        subprocess.call(shlex.split(entry))
                        self.ui.consola.setText('Archivo creado')




            
                elif error=='Error de ruta':
                    self.ui.consola.setText('Ruta no existente')
                
                elif error=='Error de archivo':
                    self.ui.consola.setText('Archivo no existente')
                
            
            # self.ui.consola.setText('')
            apuntador = 0
            apuntadorC = 0
        else:
            self.ui.consola.setText(errorTo)
        
def verifyRoutesAndArchives(entry):

    
    #EN ESTE METODO VERIFICAMOS PRIMERO QUE COMANDO ES YA QUE CADA EN UNOS CASOS NO SE DEBE DE VERIFICAR SI EL ARCHIVO EXISTE
    

    rutas = []
    archivos = []

    if entry[0] == 'mkdir' or entry[0] == 'touch':
        return False
    elif entry[0] == 'cd':
        #EL CD SOLAMENTE SE VERIFICARA SI TRAE UN ARCHIVO O RUTA SI NO LO REGRESAMOS AUTOMATICAMENTE
        if entry[1] == '..':
            return False
        else:
            #VERIFICAMOS SI ES UNA RUTA O UNA CARPETA LO QUE TRAE
            if entry[1].count('/') > 0:
                rutas.append(entry[1])
            else: 
                archivos.append(entry[1])
    elif entry[0] == 'ls':
        if len(entry) == 1:
            return False
        if len(entry) == 2:
            if entry[1] == '-l':
                return False
            else:
                if entry[1].count('/') > 0:
                    rutas.append(entry[1])
                else: 
                    archivos.append(entry[1])
        else:
            if entry[2].count('/') > 0:
                rutas.append(entry[2])
            else: 
                archivos.append(entry[2])
    elif entry[0] == 'mv':
        rutas.append(entry[1])  
        archivos.append(entry[2]) 
        rutas.append(entry[3])  
        archivos.append(entry[4]) 
    elif entry[0] == 'rm':
        rutas.append(entry[1])  
        archivos.append(entry[2]) 
    elif entry[0] == 'touch':
        rutas.append(entry[1])  
        archivos.append(entry[2]) 



    print(f'Rutas existentes: {rutas}')
    print(f'Archivos existentes: {archivos}')


    for i in range(len(rutas)):
         if os.path.exists(rutas[i]) == False:
             return 'Error de ruta'

    # for i in range(len(archivos)):
    
    if len(archivos) >0 :
        if os.path.exists(rutas[0]+archivos[0]) == False:
            return 'Error de archivo'

    return False

def isDirection (sDirec):
    if sDirec[len(sDirec)-1] == '/' and sDirec[0] == '/':
        return True
    else:
        return False

if __name__ == '__main__':
    # subprocess.call(shlex.split('cd ..'))
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())
