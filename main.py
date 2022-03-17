import string
import re
import subprocess
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

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

                responseP = palabra(entry[apuntador])

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
                responseP = palabra(entry[apuntador])
                
                apuntador += 1
                response2 = direccion(entry)
                apuntadorC = 0
                
                apuntador += 1
                responseP2 = palabra(entry[apuntador])
                

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
            responseP = palabra(entry[apuntador])

       

            if responseD is None and responseP == 'Correcto':
                return 'Correcto'
            else: 
                return 'Error'

        elif entry[apuntador] == CREARA:
            
            apuntador += 1
            responseD = direccion(entry)
            apuntador += 1
            responseP = palabra(entry[apuntador])

            

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
                        
                        responseD = palabra(entry[apuntador])
                        
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
                return palabra(entry[apuntador])

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
        
            if palabra(''.join(t)) == 'Error':
                return 'Error'

            if nextStr[apuntadorC] == DIAGONAL:
                if complementoM(entry) != 'Error':
                    complementoM(entry)
                else:
                    return 'Error'
            else:
                return 'Error'
    
        
    elif string.ascii_letters.__contains__(nextStr[apuntadorC]):
        
        return palabra(nextStr)

    elif nextStr[apuntadorC] == '.' and len(nextStr)==1:
        return 'Error'
        
    elif nextStr[apuntadorC] == '.' and nextStr[apuntadorC+1] == '.':
        return 'Correcto'
    else:
        return 'Error'

def direccion(entry):
    global apuntadorC
    nextStr = entry[apuntador]  
    print('Entro a direccion')

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
        
            if palabra(''.join(t)) == 'Error':
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

def palabra(palabra):
    p = re.compile('(\w|_|-)+')

    if p.fullmatch(palabra) is None: 
        return 'Error'
    else:
        return 'Correcto'

class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.comprobacion)
    
    def comprobacion(self):
        global apuntador
        global apuntadorC
        entry = self.ui.lineEdit.text().strip(' ').split()
        response = comando(entry = entry)

        self.ui.message.setText(response)

        if response == 'Correcto':
            print('Ejecutar comando')
            print(entry)
            
            

            # for palabra in entry:

                
            for i in range(len(entry)):
                palabra = entry[i]
                
                if isDirection(palabra):
                    l = list(palabra)
                    l.pop(len(l)-1)
                    l.append('"')
                    l.insert(0,'"')
                    print(l)

                    palabra = ''.join(l)
                    palabra = palabra.replace('/','\\')
                    print(f'Palabra: {palabra}')

                    entry[i]= palabra
            
            print('entry')
# 

            entry = ' '.join(entry)

            print(entry)
            v = r'ls "C:\Users\gugod\Downloads"'
            print(v)
            pipe = subprocess.Popen(v,  stdout=subprocess.PIPE).stdout

            # output = pipe.read()

            # texto = output.str()
            
            print(pipe.read())
            
        

        apuntador = 0
        apuntadorC = 0
        

def isDirection (sDirec):
    if sDirec[len(sDirec)-1] == '/' and sDirec[0] == '/':
        return True
    else:
        return False

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())

    # print(direccion('a'))
    # entry = input('Escribe el comando de linux: ').strip(' ').split()

    # comando(entry=entry)
    # print('Termino bien')

    # print(string.ascii_letters.__contains__('a'))

