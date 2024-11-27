import pandas as pd
import numpy as np
from enum import Enum


class Oferta(Enum):
    VENTA = 1
    ALQUILER = 2


'''
    Clase: TipoInmueble
    Atributos: idTipoInmueble, nombre
'''
class TipoInmueble:

    def __init__(self, idTipoInmueble, nombre):
        self.__idTipoInmueble = idTipoInmueble
        self.__nombre = nombre
    
    def __get_idTipoInmueble(self): 
        return self.__idTipoInmueble
    
    def __set_idTipoInmueble(self, idTipoInmueble):
        self.__idTipoInmueble = idTipoInmueble
    
    idTipoInmueble = property(fget=__get_idTipoInmueble, fset=__set_idTipoInmueble)

    def __get_nombre(self):
        return self.__nombre
    
    def __set_nombre(self, nombre):
        self.__nombre = nombre
    
    nombre = property(fget=__get_nombre, fset=__set_nombre)
    
    def to_dict(self):
        return dict(idPropietario=self.idPropietario, nombre=self.nombre)

    def __str__(self):
        return f"idPropietario:{self.idPropietario}, nombre:{self.nombre}"

'''
    Clase: Propietario
    Atributos: idPropietario, nombre
'''
class Propietario:

    def __init__(self, idPropietario, nombre):
        self.__idPropietario = idPropietario
        self.__nombre = nombre
    
    def __get_idPropietario(self): 
        return self.__idPropietario
    
    def __set_idPropietario(self, idPropietario):
        self.__idPropietario = idPropietario
    
    idPropietario = property(fget=__get_idPropietario, fset=__set_idPropietario)

    def __get_nombre(self):
        return self.__nombre
    
    def __set_nombre(self, nombre):
        self.__nombre = nombre
    
    nombre = property(fget=__get_nombre, fset=__set_nombre)
    
    def to_dict(self):
        return dict(idPropietario=self.idPropietario, nombre=self.nombre)

    def __str__(self):
        return f"idPropietario:{self.idPropietario}, nombre:{self.nombre}"


'''
    Clase: Vendedor
    Atributos: idVendedor, nombre, telefono
'''
class Vendedor:

    def __init__(self, idVendedor, nombre, telefono):
        self.__idVendedor = idVendedor
        self.__nombre = nombre
        self.__telefono = telefono
    
    def __get_idVendedor(self): 
        return self.__idVendedor
    
    def __set_idVendedor(self, idVendedor):
        self.__idVendedor = idVendedor
    
    idVendedor = property(fget=__get_idVendedor, fset=__set_idVendedor)

    def __get_nombre(self):
        return self.__nombre
    
    def __set_nombre(self, nombre):
        self.__nombre = nombre
    
    nombre = property(fget=__get_nombre, fset=__set_nombre)
    
    def __get_telefono(self):
        return self.__telefono
    
    def __set_telefono(self, telefono):
        self.__telefono = telefono
    
    telefono = property(fget=__get_telefono, fset=__set_telefono)
    
    def to_dict(self):
        return dict(idVendedor=self.idVendedor, nombre=self.nombre, telefono=self.telefono)

    def __str__(self):
        return f"idVendedor:{self.idVendedor}, nombre:{self.nombre}, telefono:{self.telefono}"

'''
    Clase: Inmueble
    Atributos: idInmueble, areaTotal, areaConstruida, valorMt2, precio, fechaPublicacion, fechaContrato, disponible
'''
class Inmueble:

    def __init__(self, idInmueble, areaTotal, areaConstruida, valorMt2, precio, fechaPublicacion, fechaContrato, disponible):
        self.__idInmueble = idInmueble
        self.__areaTotal = areaTotal
        self.__areaConstruida = areaConstruida
        self.__valorMt2 = valorMt2
        self.__precio = precio
        self.__fechaPublicacion = fechaPublicacion 
        self.__fechaContrato = fechaContrato
        self.__disponible = disponible
        self.__oferta: Oferta
    
    def __get_idInmueble(self): 
        return self.__idInmueble
    
    def __set_idInmueble(self, idInmueble):
        self.__idInmueble = idInmueble
    
    idInmueble = property(fget=__get_idInmueble, fset=__set_idInmueble)

    def __get_areaTotal(self):
        return self.__areaTotal
    
    def __set_areaTotal(self, areaTotal):
        self.__areaTotal = areaTotal
    
    areaTotal = property(fget=__get_areaTotal, fset=__set_areaTotal)
    
    def __get_areaConstruida(self):
        return self.__areaConstruida
    
    def __set_areaConstruida(self, areaConstruida):
        self.__areaConstruida = areaConstruida
    
    areaConstruida = property(fget=__get_areaConstruida, fset=__set_areaConstruida)
    
    def __get_valorMt2(self):
        return self.__valorMt2
    
    def __set_valorMt2(self, valorMt2):
        self.__valorMt2 = valorMt2
    
    valorMt2 = property(fget=__get_valorMt2, fset=__set_valorMt2)

    def __get_precio(self):
        return self.__precio
    
    def __set_precio(self, precio):
        self.__precio = precio
    
    precio = property(fget=__get_precio, fset=__set_precio)

    def __get_fechaPublicacion(self):
        return self.__fechaPublicacion
    
    def __set_fechaPublicacion(self, fechaPublicacion):
        self.__fechaPublicacion = fechaPublicacion
    
    fechaPublicacion = property(fget=__get_fechaPublicacion, fset=__set_fechaPublicacion)

    def __get_fechaContrato(self):
        return self.__fechaContrato
    
    def __set_fechaContrato(self, fechaContrato):
        self.__fechaContrato = fechaContrato
    
    fechaContrato = property(fget=__get_fechaContrato, fset=__set_fechaContrato)

    def __get_disponible(self):
        return self.__disponible
    
    def __set_disponible(self, disponible):
        self.__disponible = disponible
    
    disponible = property(fget=__get_disponible, fset=__set_disponible)

    def __get_oferta(self):
        return self.__oferta
    
    def __set_oferta(self, oferta:Oferta):
        self.__oferta = oferta
    
    oferta = property(fget=__get_oferta, fset=__set_oferta)

    def __str__(self):
        return f"idInmueble:{self.idInmueble}, areaTotal:{self.areaTotal}, areaConstruida:{self.areaConstruida}, valorMt2:{self.valorMt2}, precio:{self.precio}, fechaPublicacion:{self.fechaPublicacion}, fechaContrato:{self.fechaContrato}, disponible:{self.disponible}, oferta:{self.oferta}"

