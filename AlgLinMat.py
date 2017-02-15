#En Android me funcionO
#Descargandolo en el directorio Download
#Ejecutando:
#   import sys
#   sys.path.append("/mnt/sdcard/Download")
#   from AlgLinMat import *


import sys
import copy
from fractions import Fraction


    
def sumar_matrices(A,B):
    C=copy.deepcopy(A)
    (m,n)=C.size()
    for i in range(1,m+1):
        for j in range(1,n+1):
          C[i,j]=A[i,j]+B[i,j]      
    return C

def restar_matrices(A,B):
    return sumar_matrices(A,escalar_por_matriz(-1,B))


def multiplicar_matrices(A,B):
    (Am,An)=A.size()
    (Bm,Bn)=B.size()
    C=matriz.de_ceros(Am,Bn,"no_mostrar")
    for i in range(1,Am+1):
        for j in range(1,Bn+1):
            t=0
            for k in range(1,An+1):
                t=t+A[i,k]*B[k,j]
                #print "i "+str(i)+"j "+str(j)+"k "+str(k)+"t "+str(t)
            C[i,j]=t     
    return C

def escalar_por_matriz(k,A):
    C=copy.deepcopy(A)
    (m,n)=C.size()
    for i in range(1,m+1):
        for j in range(1,n+1):
          C[i,j]=k*A[i,j]      
    return C


#latex de columna de lista
#~ def col(list1):
    #~ l=list(list1)
    #~ s="\\begin{bmatrix} " +l.pop(0).latex()
    #~ for a in l:
        #~ s=s+" \\\\ " +a.latex()      
    #~ return s + " \\end{bmatrix}"

#latex de columna de lista
def ren(list1):
    l=list(list1)
    s= l.pop(0).latex()
    for a in l:
        s=s+" & " +a.latex()      
    return s 

def str2num(s):
    if s.find('.')!=-1:
        return float(s)
    elif s.find('/')!=-1:
        return frac(s)
    elif s.strip()=="-":
        return -1
    else:
        return int(s)


class Num:
    def __init__(self,val):
        if type(val) is str:
            self.val=str2num(val)
        elif isinstance(val,Fraction):
            self.val= frac(val)
        else:
            self.val=val
    def latex(self):
        try:
            return self.val.latex()
        except AttributeError:
            return str(self.val)   
    def evalu(self):
        return self.val
    def __str__(self):
        return str(self.val)
    def __mul__(self,otro):
        return self.val*otro
    def __rmul__(self,otro):
        return otro*self.val
    def __add__(self,otro):
        return self.val+otro
    def __radd__(self,otro):
        return otro+self.val
    def __sub__(self,otro):
        return self.val-otro
    def __rsub__(self,otro):
        return otro-self.val
    def __div__(self,otro):
        return self.val/otro
    def __rdiv__(self,otro):
        return otro/self.val
    def __mod__(self,otro):
        return self.val%otro
    def __rmod__(self,otro):
        return otro%self.val
    def __neg__(self):
        return -self.val
    def __invert__(self):
        return -self.val
    def __pos__(self):
        return self.val
    def __nonzero__(self):
        return bool(self.val)
  
  

#fraccionario    
class frac(Fraction): 
    def latex(self):
        return "\\frac{"+str(self.numerator)+"}{"+str(self.denominator)+"}"   
    
  
#def expulgar(s):
#    print(s)
  
#matriz  
def matlab2python(lista):
        lista1=lista.split(';')
        #print('lista1')
        #print(lista1)
        lista2=map(lambda n: n.split(),lista1)
        lista3=map(lambda n: map(Num,n),lista2)
        return lista3

    
class matriz:# es una columna de renglones
  def __init__(self,lista,txt=""):
    #print('lista1 '+str(type(lista)))
    if type(lista) is str:
        self.lista= matlab2python(lista)
    elif isinstance(lista,list):
        self.lista=map(lambda n: map(Num,n),lista)
    elif type(lista) is list:
        self.lista=lista
    else:
        raise ValueError('matriz no inicializada: '+str(lista)+','+lista.__class__.__name__)
    if txt!="no_mostrar":
        mostrar(str(self))#(self.latex())
    self.ops=str(self)
    self.ultop=self
    #print('lista2 '+str(self.lista))
  @staticmethod
  def de_ceros(m,n,txt=""):
    C=list()
    for i in range(1,m+1):
      r=list()
      for j in range(1,n+1):
        r.append(0)
      C.append(r)
    return matriz(C,txt)

  @staticmethod
  def identidad(m,n,txt=""):
    C=list()
    for i in range(1,m+1):
      r=list()
      for j in range(1,n+1):
        if i==j:
            r.append(1)
        else:
            r.append(0)
      C.append(r)
    return matriz(C,txt)

  def __nonzero__(self):
      nocero=False
      (m,n)=self.size()
      for i in range(1,m+1):
        for j in range(1,n+1):
            nocero = nocero or bool(self[i,j])
      return nocero
  def __getitem__(self,(i,j)):
      return self.lista[i-1][j-1].evalu()
  def __setitem__(self,(i,j),d):
       self.lista[i-1][j-1]=Num(d)

  def size(self):
    return (len(self.lista),len(self.lista[0]))
  def __rmul__(self,vecAbs1):
    return opBin(self,Num(vecAbs1),escalar_por_matriz,"")
  def __mul__(self,vecAbs1):
    return opBin(self,vecAbs1,multiplicar_matrices,"")
  def __add__(self,vecAbs1):
    return opBin(self,vecAbs1,sumar_matrices,"+")
  def __sub__(self,vecAbs1):
    return opBin(self,vecAbs1,restar_matrices,"-")
  def __str__(self):
    espcioCol=2
    C=list()
    maximos=list()
    (m,n)=self.size()
    #print(str(m)+","+str(n))
    ancho=0
    for j in range(1,n+1):
        maximo=0
        D=list()
        for i in range(1,m+1):
            c=str(self[i,j])
            D.append(c)
            #print(c)
            #print len(c)
            maximo=max(maximo,len(c))     
        maximos.append(maximo)
        #print("max"+str(maximo))
        ancho=ancho+maximo+espcioCol
        #print(ancho)
        C.append(D)
    s=""
    for i in range(0,m):
        s=s+"|  "
        for j in range(0,n):
            c=str(C[j][i])
            #print("c="+c)
            s=s+c
            s=s+(" "*(maximos[j]-len(c)+espcioCol))
        #print("|"+s+"|")
        s=s+"|"+"\n"
        s1=" -"+(" "*(ancho))+"-\n"
    return s1+s+s1
   #~ (Am,An)=self.size()
   #~ print("[")
   #~ for i in range(1,Am+1):
        #~ print("[")
        #~ for j in range(1,An+1):
                #~ print (str(self[i,j])+", ")
        #~ print("], ")
   #~ print("]")

  def evalu(self):
      return self
  def latex(self):
    l=list(self.lista)
    s="\\begin{bmatrix} " + ren(l.pop(0))
    for a in l:
      s=s+" \\\\ " +ren(a)      
    return s + " \\end{bmatrix}"
  
  #def col(self,*indices):
  #  print(columnas)
  
  
  #menos sOlo
  #entero
  #flotante
  #fraccion
    
  def op(self,s):
    s=s.lower()
    #print(s)
    def interpretaRenglon(s1):
        s=s1.replace(' ','')
        #print("interpretando "+s)
        d=s.find("r")
        if d==-1:
            raise ValueError("fala la 'r'. Error en "+s)
        elif d==0:
            k=1
        else:
            try:
                k=Num(s[:d])
            except:
                raise ValueError("antes de 'r' sOlo debe haber un entero. Error en "+s)
        #a1=s[d+1:]
        #if not a1.isdigit():
        #print ("coef ="+str(k))
        try:
            a=int(s[d+1:])
        except:
            raise ValueError("despuEs de 'r' sOlo debe haber un dIgito. Error en "+s)
        #a=int(a1)
        return (k,a)
            
    #print (str(k)+", "+str(a))
    (size,z)=self.size()
    m=matriz.identidad(size,size,"no_mostrar")
    d=s.find("<->")
    if d!=-1:
        (k1,a1)=interpretaRenglon(s[:d])
        (k2,a2)=interpretaRenglon(s[d+3:])
        if (k1 != 1) or (k2 != 1):
            raise ValueError("al intercambiar renglones no se puede multiplicar. Error en "+s)
        r="R"+str(a1)+" <-> R"+str(a2)
        m[a1,a1]=0    
        m[a2,a2]=0    
        m[a1,a2]=1    
        m[a2,a1]=1    
        #print(str(m))
    else:
        d=s.find("->")
        if d==-1:
            raise ValueError("no se encontrO ni '->' ni '<->'. Error en "+s)
        else:
            (k2,a2)=interpretaRenglon(s[d+2:])
            e=s[:d].find("+")
            f=s[:d].find("-")
            if e!=-1:
                (k11,a11)=interpretaRenglon(s[:e])
                (k12,a12)=interpretaRenglon(s[e+1:d])
                if (a11==a2) and (a12==a2):
                    raise ValueError("en este caso es mejor multiplicar el renglOn por "+str(k11+k12)+". Error en "+s)
                elif (a11==a2):
                    if (k11!=1):
                        raise ValueError("el renglOn destino no se multiplica por "+str(k11)+". Error en "+s)
                    r=str(k12)+"R"+str(a12)+"+"+"R"+str(a2)+" -> R"+str(a2)
                    m[a2,a12]=k12
                    #print(str(m))
                elif (a12==a2):
                    if (k12!=1):
                        raise ValueError("el renglOn destino no se multiplica por "+str(k12)+". Error en "+s)
                    r=str(k11)+"R"+str(a11)+"+"+"R"+str(a2)+" -> R"+str(a2)
                    m[a2,a11]=k11
                    #print(str(m))
                else:#if (a11!=a2) and (a12!=a2):
                    raise ValueError("el renglOn destino y un origen deben coincidir. Error en "+s)
            elif f!=-1:
                c=s[:d].count('r')
                if c==0:
                    raise ValueError("faltan 'R' en "+s[:d])
                elif c==2:
                    (k11,a11)=interpretaRenglon(s[:f])
                    (k12,a12)=interpretaRenglon(s[f+1:d])
                    if (a11==a2) and (a12==a2):
                        raise ValueError("en este caso es mejor multiplicar el renglOn. Error en "+s)
                    elif (a11==a2):
                        if (k11!=1):
                            raise ValueError("el renglOn destino no se multiplica por "+str(k11)+". Error en "+s)
                        r=str(-k12)+"R"+str(a12)+"+"+"R"+str(a2)+" -> R"+str(a2)
                        m[a2,a12]=-k12
                        #print(str(m))
                    elif (a12==a2):
                        if (k12!=1):
                            raise ValueError("el renglOn destino no se multiplica por "+str(k11)+". Error en "+s)
                        r=str(-k11)+"R"+str(a11)+"+"+"R"+str(a2)+" -> R"+str(a2)
                        m[a2,a11]=-k11
                        #print(str(m))
#                        raise ValueError("el renglOn destino no se multiplica por "+str(-k12)+". Error en "+s)
                    else:#if (a11!=a2) and (a12!=a2):
                        raise ValueError("el renglOn destino y un origen deben coincidir. Error en "+s)
                elif c==1:
                    (k1,a1)=interpretaRenglon(s[:d])
                    if a1 != a2 :
                        raise ValueError("el renglOn destino y el origen deben coincidir. Error en "+s)
                    r=str(k1)+"R"+str(a1)+" -> R"+str(a2)
                    m[a2,a2]=k1
                    #print(str(m))
                
                else:
                    raise ValueError("se operan mAximo dos renglones. Error en "+s)
            else:
                (k1,a1)=interpretaRenglon(s[:d])
                if a1 != a2 :
                    raise ValueError("el renglOn destino y el origen deben coincidir. Error en "+s)
                r=str(k1)+"R"+str(a1)+" -> R"+str(a2)
                m[a2,a2]=k1
                #print(str(m))
    print("La matriz elemental asociada es \n"+str(m))
    self.ultop=multiplicar_matrices(m,self.ultop)
    self.ops=self.ops+"\n"+r+"\n"+str(self.ultop)
    print("La transformaciOn es \n"+self.ops)
    return self.ultop
    
    
    
    
    
    
  #~ def a(self,k,i,j):
    #~ lista=self.lista
    #~ s=escList(k,lista[i-1])
    #~ t=addList(s,lista[j-1])
    #~ lista[j-1]=t
    #~ cmd=str(k)+"R"+str(i)+" + R"+str(j)+" \\rightarrow R"+str(j)
#~ #    cmd1="\\stackrel{"+cmd+"}{\\rightarrow}"
    #~ cmd1="\\xrightarrow{"+cmd+"}"
    #~ mostrar("\stackrel{"+cmd1+"}{"+self.latex()+"}")
    #~ #mostrar(cmd1+self.latex())
    #~ return lista 
  #~ def e(self,k,i):
    #~ lista=self.lista
    #~ t=escList(k,lista[i-1])
    #~ lista[i-1]=t
    #~ cmd=str(k)+"R"+str(i)+" \\rightarrow R"+str(i)
    #~ cmd1="\\xrightarrow{"+cmd+"}"
    #~ mostrar("\stackrel{"+cmd1+"}{"+self.latex()+"}")
    #~ #mostrar(cmd1+self.latex())
    #~ return lista 
  #~ def i(self,i,j):
    #~ lista=self.lista
    #~ t=lista[i-1]
    #~ lista[i-1]=lista[j-1]
    #~ lista[j-1]=t
    #~ cmd="R"+str(i)+" \\leftrightarrow R"+str(j)
    #~ cmd1="\\xrightarrow{"+cmd+"}"
    #~ mostrar("\stackrel{"+cmd1+"}{"+self.latex()+"}")
    #~ #mostrar(cmd1+self.latex())
    #~ return lista 
#  def __str__(self):
#    l=list(list1)
#    s="["+ str(l.pop(0))
#    for a in l:
#        s=s+"["       
#        for b in a:
#            s=s+b+","       
#    return s 
 #   l=list(self.lista)
 #    return list_str_f(l,list_str)
  
#Operacion binaria
class opBin(matriz):
    def __init__(self,vecAbs1,vecAbs2,fun,simbLatex,txt=""):
        self.vecAbs1=vecAbs1
        self.vecAbs2=vecAbs2
        self.fun=fun
        self.simbLatex=simbLatex
        self.mat = self.fun(*(self.vecAbs1.evalu(),self.vecAbs2.evalu()))
        self.lista=self.mat.lista
        #mostrar(self.evalu().latex()=self.latex())
        if txt!="no_mostrar":
            mostrar(str(self))#(self.latex())
        #mostrar(str(self.evalu()))#(str(self.evalu())+"="+str(self))#(self.evalu().latex()+"="+self.latex())
    def evalu(self):
        return self.mat
    def latex(self):
        return "\\left("+self.vecAbs1.latex() + self.simbLatex + self.vecAbs2.latex()+"\\right)"



#Muestra el texto en las dos ventanas
def mostrar(texto):
    print(texto)
