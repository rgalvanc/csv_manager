#
# Esta clase es la encargada de hacer de interfaz con los datos
# y los módulos en python...
#



class Fluid_Data:

    def __init__(self, cas, parent_dir):
        
        #
        #  
        self.parent_dir=parent_dir 
        self.cas=cas

        #
        # Algunas propiedades del fluido para inicializarlas a valores negativos
        # Así sabemos que no se encuentran presentes antes de leerlas y podemos
        # dar algunos errores..
        #
        self.Tc=-1
        self.TTt=-1
        self.Pc=-1
        self.Tb=-1


        #
        # Estas listas de abajo, van desde 0 hasta Número de referencias-1
        #
        self.Ref=[]
        self.Year=[]
        self.DataType=[]
        self.Error=[]
        self.Acp=[]
        self.SType=[]
        self.ESource=[]
        self.label=[]
        self.BibTeX=[]
        self.doi=[]


        #
        # Estas listas de abajo van desde 0 hasta Número de datos-1
        #
        
        self.x=[]
        self.y=[]
        self.ey=[]
        self.take=[]
        self.idRef=[]
        self.Sugden=[]
        

        #
        # Llamamos a las subrutinas de lectura de datos... 
        #
        
        
        self.read_diadem_header()    # Leer cabecera con propiedades del fluido 
        self.read_diadem_data()      # Leer datos de diadem... 
        self.read_detherm()
        self.read_otros()
      

      
     
     



    
    #
    # Leer la cabecera del archivo diadem con los datos generales del fluido.
    #

    def read_diadem_header(self):

       

        has_TTt=0
        has_Tc=0
        has_mw=0
        has_Pc=0
        
        #
        # Listado de tokens a encontrar para procesar..
        #
        tokens=["MW","TC","PC","VC","ZC",
		"MP","TTf","TPP","NBP","LVOL",
		"ACEN","DM","Ajuste","Nombre","Familia",
		"Ref","Calidad","Acp","CASN","TPT",
		"Cal","SubFamilia","SYNL","SYN","RG",
		"SType","SDetail","ESource","Error","DataType",
	        "Formula","SMILES","Structure"];

        filename=self.parent_dir+"ST/"+self.cas+".txt"
     

        try:
            file=open(filename)
        except:
            #
            # Si el archivo de DIPPR no está, entonces es bastante malo ya que no se puede hacer nada
            #
            print("El archivo de DIPPR no puede abrirse.   No puedo seguir.",filename)
        

      
            
        for linea in file:  # Procesamos las líneas del archivo....
            linea=linea.replace('\n','')   # Quitar los retornos de carro
            if len(linea)==0:  # No queremos líneas en blanco... 
                continue
            
            for tks in tokens:               
                needle="#["+tks+"]:"
                rt_val=linea.find(needle)  
                

                
                if rt_val!=-1:   #                 
                    value=linea[len(needle):]
                 
                 
                    
                    match tks:
                        case "CASN":
                            self.casn=value
                            
                        case "Nombre":                            
                            self.name=value
                        case "MW":   # Peso molecular 
                         
                            vec=value.split(";")
                            self.mw=float(vec[0])
                            has_mw=1
                          
                        case "TC":   # Temperatura del punto crítico
                            vec=value.split(";")
                            self.Tc=float(vec[0])
                            has_Tc=1

                        case "TPT":  # Temperatura del punto triple
                            vec=value.split(";")
                            self.TTt=float(vec[0])

                            has_TTt=1

                        case "NBP":   # Temperatura del punto crítico
                            vec=value.split(";")
                            self.Tb=float(vec[0])
                        #
                        # Aquí se pueden poner muchas más cosas....
                        #
        
        

#--------------------------------------------

    def read_diadem_data(self):
        #  -------------------------------------------------------------------------------
        #  
        #                    LEER LOS DATOS CONTENIDOS EN DIADEM
        #
        #  -------------------------------------------------------------------------------


        tokens=["RefID","Ref","Year","SType","SDetail","ESource","Error","Acp","DataType"]
        
        filename=self.parent_dir+"ST/"+self.cas+".txt"
        
        
        try:
            file=open(filename)
        except:
            #
            # Si el archivo de DIPPR no está, entonces es bastante malo ya que no se puede hacer nada
            #
            print("El archivo de DIPPR no puede abrirse.   No puedo seguir.",filename)


      

        for linea in file:  # Procesamos las líneas del archivo....
           
            linea=linea.replace('\n','')    # Quitar los retornos de carro
            if len(linea)==0:
                continue 
            if linea[0]=="#":
                for tks in tokens:               
                    needle="#["+tks+"]:"
                    rt_val=linea.find(needle)
                    
                    if rt_val!=-1:   #                 
                        value=linea[len(needle):]
                        value=value.strip("\n")   # Dichosos \n ..... 
                    
                        match tks:
                            case "RefID":
                                chr="DIPPR-"+str(len(self.Ref)+1)
                                self.label.append(chr)

                                self.BibTeX.append("dippr2022")
                                self.doi.append("")  # No tenemos doi en DIPPR (Lástima) 
                             
                            case "Ref":
                                self.Ref.append(value)
                                is_sugden=0  # Marcar la posibilidad de que el dato sea predicho por el método de Sugden

                                if value.find("Sugden")!=-1:
                                    is_sugden=1
                                    
                            case "Year":
                                self.Year.append(value)
                            case "SType":
                                self.SType.append(value)
                            case "ESource":
                                self.ESource.append(value)
                            case "Error":
                                self.Error.append(value)
                            case "Acp":
                                self.Acp.append(value)
                            case "DataType":
                                DType=0
                                if value.find("Experimental")!=-1:
                                    DType=1
                                if value.find("Smoothed")!=-1:
                                    DType=2
                                if value.find("Predicted")!=-1:
                                    DType=3

                                match DType:
                                    case 0:
                                        self.DataType.append("Unknown")
                                    case 1:
                                        self.DataType.append("Exp")
                                    case 2:
                                        self.DataType.append("Smoothed")
                                    case 3:
                                        self.DataType.append("Predicted")
                                    

            else:
                if len(linea)>1:
                    vec=linea.split(" ")
                    if vec[0][0]=='!':   # Los datos con ! delante no se tienen en cuenta pero se muestran
                        vec[0]=vec[0][1:]
                        self.x.append(float(vec[0]))
                        self.take.append(0)
                    else: 
                        self.x.append(float(vec[0]))
                        self.take.append(1)
                    self.y.append(float(vec[1]))
                    self.Sugden.append(is_sugden)
                    self.ey.append(-1)  # Indicate that no error is assigned...
                    self.idRef.append(len(self.Ref)-1)
                    

# ---------------------------------------------------------------------------------
# 
#       Leer  datos de DETHERM que siguen otra esctructura... 
#
# --------------------------------------------------------------------------------- 

    def read_detherm(self):

        filename=self.parent_dir+"ST-DECH/"+self.cas+".txt"
        
        id_dth=0
        try:
            file=open(filename)
        except:
            #
            # Si el archivo de DIPPR no está, entonces es bastante malo ya que no se puede hacer nada
            #
            print("El archivo de DETERM no existe.",filename)


        prp_line=0   # Señal para ver que hay una línea que empieza por PRP.... 
        for linea in file:
         
            linea=linea.replace('\n','')   # Quitar los retornos de carro
            
            if(len(linea))==0:
                   continue
            
            if linea.find("#id .....:")!=-1:
                id_dth+=1
                chr="DETHERM-"+str(id_dth)
                self.label.append(chr)
                self.BibTeX.append("detherm2019")
                self.DataType.append("Unknown")
                prp_line=0
              

            if linea[0]!="#":  # Tenemos un dato aquí para introducir....
               
                vec=linea.split(" ")
                if vec[0][0]=='!':   # Los datos con ! delante no se tienen en cuenta pero se muestran
                    vec[0]=vec[0][1:]
                    self.x.append(float(vec[0]))
                    self.take.append(0)
                else: 
                    self.x.append(float(vec[0]))
                    self.take.append(1)

                self.y.append(float(vec[1]))
             
                if len(vec)==3:            # Tenemos un error en detherm.... 
                    self.ey.append(float(vec[2]))
                else:
                    self.ey.append(-1)

                self.idRef.append(len(self.Ref)-1)

            if (linea[0]=="#" and prp_line==1): 
                prp_line=0
                self.Ref.append(linea[1:])
                self.Year.append("")

            if(linea.find("#DOI:")!=-1):
                self.doi.append(linea[5:])
                 
            if linea.find("PRP")!=-1:
                prp_line=1

            
#
# Leer el archivo OTROS  que puede tener aún más problema....
#

    def read_otros(self):

        #
        # Se supone que el programa reconoce las siguientes cadenas para ser introducidas
        # en los datos.   El problema es que es muy posible que dichas cadenas no se encuentren
        # en el archivo OTROS por lo que es importante introducir unos valores por defecto
        # en el caso de que no se encuentren...
        #

        def_BibTeX=""
        def_Ref=""
        def_label=""
        def_doi=""
        def_type="Unknown"
        
    
        filename=self.parent_dir+"OTROS/"+self.cas+".txt"


        try:
            file=open(filename)
        except:
            #
            # Si el archivo de DIPPR no está, entonces es bastante malo ya que no se puede hacer nada
            #
            print("El archivo de OTROS no existe.",filename)

        new_source=0

        
        for linea in file:  # Procesamos las líneas del archivo....
                
            linea=linea.replace('\n','')    # Quitar los retornos de carro
            if len(linea)==0:
                continue 
        

            if linea[0]=="@":
                append_data=1
              
                fT=0
                fsrf=1
                
                if linea.find("C")!=0:  # Tenemos la temperatura en C
                    fT=273.1500000
                    
                if linea.find("m")!=0:  # La tensión superficial está en mN/m
                    fsrf=1000


            if ( linea.find("#[BibTeX]:")!=-1  or  linea.find("#[BibTex]:")!=-1):
                def_bibtex=linea[10:]
                
            if linea.find("#[Ref]:")!=-1:
                def_ref=linea[7:]

            if linea.find("#[doi]:")!=-1:
                def_doi=linea[7:]

            if linea.find("#[label]:")!=-1:
                def_label=linea[9:]; 
               
            if linea.find("#[Type]:")!=-1:
                valor=linea[9:]
                if (valor[0]=="U" or valor[0]=="u"):
                    def_type="Unknown"

                if (valor[0]=="E" or valor[0]=="e"):
                    def_type="Exp"

                if (valor[0]=="P" or valor[0]=="p"):
                    def_type="Predicted"

                
                if (valor[0]=="S" or valor[0]=="s"):
                    def_type="Smoothed"
                
           
                
                    
            if (linea[0]!="#" and linea[0]!="@"):  # Tenemos datos por aquí

                if append_data==1:
                    self.BibTeX.append(def_BibTeX)
                    self.label.append(def_label)
                    self.Ref.append(def_Ref)
                    self.doi.append(def_doi)
                    self.DataType.append(def_type)
                    append_data=0

                    
                new_line=(" ".join(linea.split()))  # Agrupar espacios entre columnas por si acaso
                vec=new_line.split(" ")
                
                if vec[0][0]=='!':   # Los datos con ! delante no se tienen en cuenta pero se muestran
                    vec[0]=vec[0][1:]
                    self.x.append(float(vec[0])+fT)
                    self.take.append(0)
                else: 
                    self.x.append(float(vec[0])+fT)
                    self.take.append(1)
                    
                self.y.append(float(vec[1])/fsrf)
                    
                if len(vec)==3:            # Tenemos errores asociados en la fuente
                    self.ey.append(float(vec[2])/fsrf)
                else:
                    self.ey.append(-1)

                self.idRef.append(len(self.Ref)-1)
                
            


                
#
# Simplemente se llama con el cas e introduce los datos...
#

fluido=Fluid_Data("142-29-0","../data/")    # Esto es para testear..... 



#
# Mostrar los datos importantes 
#


        
print(fluido.name)    # Nombre del fluido
print(fluido.casn)    # Cas en la base de datos de DIPPR (debería ser igual al que llamamos)
print(fluido.Tc)      # Temperatura crítica
print(fluido.TTt)     # Temperatura del punto triple
print(fluido.Tb)    # Temperatura del punto de ebullición
#
# Aquí podría añadir un montón más de propiedades del fluido, pero de momento no hace falta..
#


print(fluido.x)   # Todos los datos de temperatura
print(fluido.y)   # Tensión superficial
print(fluido.ey)  # Error de la medida (-1 si no hay.  Esto es lo normal)
print(fluido.take) # 0: Si el dato no se toma en el ajuste 1: si se toma  2: si está repetido....

print(fluido.idRef) # Por cada dato el índice de la referencia de donde esta (las lista de abajo)

print("---------------------- SOLAMENTE HAY UNA ENTRADA POR FUENTE  AQUÍ ABAJO  -----------")
print(fluido.label)     # Etiqueta para mostrar en la gráfica
print(fluido.Ref)       # Referencia bibliográfica
print(fluido.doi)       # Digital Object Identifier (doi) del paper donde se publicó
print(fluido.DataType)  # Tipo de dato:  Unknowhn, Exp, Smoothed, Predicted... 

