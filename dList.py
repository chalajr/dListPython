# Clases para crear una lista doblemente ligada utilizando python.
# El codigo original en el cual se basa este proyecto se encuentra en: stackabuse.com
# Partes del codigo fueron tomadas del original con algunas modificaciones.
# Autor: Juan Ricardo Chalita Pérez.
# Autor original del codigo: Usman Malik.





#Creacion de la clase nodo, el constructor toma de valores a self y a elemento el cual sera el elemento que se encuentre dentro del nodo,
#ademas podemos ver que se encuentran otros dos atributos los cuales nos van a indicar las conecciones entre los nodos.
class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento  
        self.siguiente = None
        self.anterior = None
    

#Creacion de la clase de la lista doblemente ligada y su constructor, la cual contiene unicamente el nodo inicial o el root de la lista el cual le da un inicio a la lista 
class doubleList:
    def __init__(self):
        self.root = None


    #Insertando datos a la lista doblemente ligada
    #Insertando datos a una lista vacia
    def insertar_lista_vacia(self, dato):
        #si la lista esta vacia:
        if self.root is None:
            #creamos un nuevo nodo
            nuevoNodo = Nodo(dato)
            #El root de la lista ahora apunta al nuevo nodo
            self.root = nuevoNodo
        #si no esta vacia la lista
        else:
            print("La lista no esta vacia")


    #Insertando datos al inicio de la lista
    def insertar_inicio(self, dato):
        #si la lista esta vacia:
        if self.root is None:
            #utilizamos la funcion de agregar a lista vacia
            self.insertar_lista_vacia(dato)
            return
        #si no esta vacia la lista
        else:
            #creamos un nuevo nodo 
            nuevoNodo = Nodo(dato)
            #asignamos como el siguiente nodo de nuestro nuevo nodo al nodo inicial o root
            nuevoNodo.siguiente = self.root
            #asignamos como nodo anterior en el root al nuevo nodo
            self.root.anterior = nuevoNodo
            #asignamos al nuevo nodo como root
            self.root = nuevoNodo


    #Insertando datos al final de la lista 
    def insertar_final(self,dato):
        #si la lista esta vacia:
        if self.root is None:
            #Agregamos el nodo al inicio 
            nuevoNodo = Nodo(dato)
            self.root = nuevoNodo
            return
        #si no esta vacia la lista
        # Creamos un apuntador a el root
        apuntador = self.root
        #Nos movemos a travez de la lista ligada hasta que el siguiente nodo se convierta en None (El ultimo nodo)
        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente
        #Creamos un nuevo nodo
        nuevoNodo = Nodo(dato)
        #Insertamos el nodo al final de la fila
        apuntador.siguiente = nuevoNodo
        #conectamos el nodo nuevo al ultimo nodo que existia
        nuevoNodo.anterior = apuntador


    #Insertando elementos despues del elemento buscado
    def insertar_despues_elemento(self, x, dato):
        #si la lista esta vacia
        if self.root is None:
            #Informamos si esta vacia la lista
            print("La lista esta vacia")
        else:
            #Utilizamos un apuntador temporal para el nodo inicial
            apuntador = self.root
            #Encontramos el elemento buscado
            while apuntador is not None:
                #Si el elemento en apuntador es igual al que estamos buscando detener el ciclo
                if apuntador.elemento == x:
                    break
                #Si no nos movemos al siguiente nodo
                apuntador = apuntador.siguiente
            #Si el apuntador esta vacio quiere decir que no existe ese elemento en la lista
            if apuntador is None:
                print("El elemento no se encuentra en la lista")
            else:
                #Si encontramos el elemento que buscabamos
                #Ahora necesitamos un nuevo nodo 
                nuevoNodo = Nodo(dato)
                #Ahora apuntamos el nodo anterior del nuevo nodo al apuntador
                nuevoNodo.anterior = apuntador
                #Ahora el siguiente del nuevo nodo sera el siguiente del apuntador 
                nuevoNodo.siguiente = apuntador.siguiente
                #Si el nodo siguiente al cual estamos apuntando no es None
                if apuntador.siguiente is not None:
                    #El nodo siguiente del apuntador ahora apuntara a nuestro nuevo nodo
                    apuntador.siguiente.anterior = nuevoNodo
                #El sifguiente del apuntador sera apuntara a nuestro nuevo nodo
                apuntador.siguiente = nuevoNodo


    #Insertando elementos antes del elemento buscado, muy similar al caso anterior 
    # con algunas excepciones al momento de haber encontrado el elemento ya que queremos 
    # agregar ahora ese nodo antes del encontrado
    #Nuestra funcion toma como datos a x el cual es el elemento buscado y a dato el cual es el valor del elemento del nuevo nodo
    def insertar_antes_elemento(self, x, dato):
        if self.root is None: 
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento == x:
                    break
                apuntador = apuntador.siguiente
            if apuntador is None:
                print("El elemento no se encuentra en la lista")
            else:
                #Si encontramos el elemento que buscabamos
                #Ahora necesitamos un nuevo nodo 
                nuevoNodo = Nodo(dato)
                #Ahora apuntamos el nodo anterior del nuevo nodo al apuntador
                nuevoNodo.siguiente = apuntador
                #Ahora el siguiente del nuevo nodo sera el siguiente del apuntador 
                nuevoNodo.anterior = apuntador.anterior
                #Si el nodo siguiente al cual estamos apuntando no es None
                if apuntador.anterior is not None:
                    #El nodo siguiente del apuntador ahora apuntara a nuestro nuevo nodo
                    apuntador.anterior.siguiente = nuevoNodo
                #El sifguiente del apuntador sera apuntara a nuestro nuevo nodo
                apuntador.anterior = nuevoNodo


    #Navegando a travez de la lista doblemente ligada
    def navegar_lista(self):
        #De nuevo revisamos que la lista no este vacia
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            #Utilizamos un apuntador para movernos a travez de la lista
            apuntador = self.root
            #Mientras que el nodo sea diferente de None
            while apuntador is not None:
                print(apuntador.elemento , " ")
                apuntador = apuntador.siguiente
    

    #Eliminando nodos
    #Eliminando nodos al inicio de la lista
    #En este caso la funcion no va a recibir nada ya que sabemos cual nodo queremos eliminar
    def eliminar_inicio(self):
        #Revisamos que la lista no este vacia 
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        #Revisamos que no tengamos un unico nodo en la lista en cuyo caso tenemos que apuntar la raiz a None
        if self.root.siguiente is None:
            #Apuntamos la raiz a None eliminando el unico nodo que existia en la lista
            self.root = None 
        #Si no se da el caso que solo tengamos un nodo eliminamos los apuntadores y ponemos al siguiente de root como root
        self.root = self.root.siguiente
        self.root.anterior = None


    #Eliminando Nodos al final de la lista
    def eliminar_final(self):
        #Revisamos que la lista no este vacia 
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        #Revisamos que no tengamos un unico nodo en la lista en cuyo caso tenemos que apuntar la raiz a None
        if self.root.siguiente is None:
            #Apuntamos la raiz a None eliminando el unico nodo que existia en la lista
            self.root = None
            return
        #Con apoyo de un apuntador nos moveremos a travez de la lista hasta llegar al ultimo nodo
        apuntador = self.root
        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente
        #Una vez estando en el ultimo nodo apuntamos el nodo anterior del apuntador a None para eliminarlo de la lista
        apuntador.anterior.siguiente = None
        


    #Eliminando nodos buscando por el elemento del nodo
    def eliminar_elemento(self, x):
        #Revisamos que la lista no este vacia
        if self.root is None:
            print("La lista esta vacia")
            return
        #Revisamos si la lista solo contiene un nodo en cuyo caso si contiene el elemento que buscamos lo eliminamos 
        # apuntando el root a None
        if self.root.siguiente is None:
            if self.root.elemento == x:
                self.root = None
        #en caso contrario desplegamos un mensaje al usuario
            else:
                print("Elemento no encontrado")
        #Si la lista contiene varios nodos y se da el caso que el elemento buscado se encuentra en el primer nodo
        if self.root.elemento == x:
            #reutilizamos la funcion para elimnar el nodo en el inicio
            self.eliminar_inicio()
            return
        
        #En caso de que el elemento no se encuentre en el primer nodo tenemos que buscarlo
        #Utilizamos un apuntador temporal para movernos en la lista
        apuntador = self.root
        while apuntador.siguiente is not None:
            if apuntador.elemento == x:
                break
            apuntador = apuntador.siguiente
        #Una vez encontrado el elemento que estabamos buscando comenzamos a eliminar el nodo
        #Si el elemento que encontramos no se encuentra en el ultimo nodo de la lista
        if apuntador.siguiente is not None:
            #Vamos a eliminar el nodo de la lista apuntando el nodo anterior, al siguiente del encontrado
            apuntador.anterior.siguiente = apuntador.siguiente
            #Y vamos a apuntar el nodo siguiente al anterior del encontrado
            apuntador.siguiente.anterior = apuntador.anterior
        #Si el elemento que queremos eliminar se encuentra en el ultimo nodo reutilizamos la funcion para eliminar el ultimo nodo
        else:
            if apuntador.elemento == x:
                self.eliminar_final()
            else:
                #Si no el elemento no se encuentra en ninguno de los nodos
                return print("Elemento no encontrado")


    #Invirtiendo una lista doblemente ligada
    def invertir(self):
        #iniciamos revisando que la lista no este vacia
        if self.root is None:
            print("La lista esta vacia")
            return 
        #Para invertir la lista nos apoyaremos de dos apuntadores
        #P apunta al primer nodo de la lista
        #Q apunta al segundo nodo de la lista
        p = self.root 
        q = p.siguiente
        #Primero apuntaremos el primer nodo a None ya que este sera el ultimo nodo de la lista
        p.siguiente = None
        #Invertimos el apuntador del primer nodo y lo apuntamos al siguiente nodo de la lista como anterior
        p.anterior = q
        #En este ciclo vamos a mover los apuntadores p y q hasta que q sea igual a None,
        #esto porque lo que vamos a invertir son los apuntadores del medio
        while q is not None:
            #El apuntador anterior de q ahora sera el apuntador siguiente de q
            q.anterior = q.siguiente
            #El apuntador siguiente de q ahora sera p, el cual esta apuntando a el nodo que esta antes de q 
            q.siguiente = p
            #Movemos los apuntadores
            p = q 
            q = q.anterior
        self.root = p







