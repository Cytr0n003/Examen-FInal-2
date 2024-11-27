class CPU:
    def __init__(self, numero_serie, socket):
        # Atributos de instancia
        self.__numero_serie = numero_serie
        self.__socket = socket
    

    @property
    def numero_serie(self):
        return self.__numero_serie
    
    @numero_serie.setter
    def numero_serie(self, numero_serie):
        self.__numero_serie = numero_serie
    

    @property
    def socket(self):
        return self.__socket
    
    @socket.setter
    def socket(self, socket):
        self.__socket = socket
    
    def __str__(self):
        return f"codigo:{self.__numero_serie}, ip:{self.__socket}"


class Computadora:
    def __init__(self, codigo, ip, cpu1, cpu2):
        # Atributos de instancia
        self.__codigo = codigo
        self.__ip = ip
        self.__cpu1 = None
        if not cpu1 is None:
            self.set_cpu1(cpu1)

        self.__cpu2 = None
        if not cpu2 is None: 
            self.set_cpu2(cpu2)

    # Métodos de acceso
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    

    @property
    def ip(self):
        return self.__ip
    
    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    # Métodos para gestionar la composición
    def get_cpu1(self):
        return self.__cpu1
    
    def set_cpu1(self, cpu):
        if isinstance(cpu, CPU):
            # La composición requiere que el obtejo parte sea construido en el objeto todo
            self.__cpu1 = CPU(cpu.numero_serie, cpu.socket)
        else:
            raise ValueError("El objeto recibido debe ser de tipo CPU.")
    
    def get_cpu2(self):
        return self.__cpu2
    
    def set_cpu2(self, cpu):
        if isinstance(cpu, CPU):
            # La composición requiere que el obtejo parte sea construido en el objeto todo
            self.__cpu2 = CPU(cpu.numero_serie, cpu.socket)
        else:
            raise ValueError("El objeto recibido debe ser de tipo CPU.")

    def __str__(self):
        return f"codigo:{self.__codigo}, ip:{self.__ip}"


cpu1 = CPU("123456", "A3+")
print(f"id del cpu1 : {id(cpu1)}")

cpu2 = CPU("987654", "Pentium")
print(f"id del cpu2 : {id(cpu2)}")

compu = Computadora("COMP01","255.255.255.255", cpu1, cpu2)

print(f"id del cpu1 : {id(compu.get_cpu1())}")
print(f"id del cpu2 : {id(compu.get_cpu2())}")
