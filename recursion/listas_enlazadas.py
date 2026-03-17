import random

class Node:

  __slots__ = ('__value','__next')

  def __init__(self,value):

    self.__value = value
    self.__next = None

  @property
  def value(self):
    return self.__value

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self, new_next):
    if new_next is not None and not isinstance(new_next,Node):
      raise TypeError("El next solo pueder ser un objeto Node ó None.")
    self.__next = new_next

  @value.setter
  def value(self, new_value):
    if new_value is None:
      raise ValueError("El valor del nodo no puede ser null ó None.")
    self.__value = new_value


  def __str__(self):
    return str(self.__value)
class LinkedList:

  __slots__ = ('__head','__tail','__size')
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  def __iter__(self):
    current_node = self.__head
    while current_node is not None:
      yield current_node
      current_node = current_node.next

  def __str__(self):

    result = [str(node) for node in self]
    return ' --> '.join(result)

  def prepend(self, new_value):
    new_node = Node(new_value)

    if self.__head is None:
      self.__head = new_node
      self.__tail = new_node
    else:
      new_node.next = self.__head
      self.__head = new_node

    self.__size += 1

  def append(self, new_value):
      new_node = Node(new_value)

      if self.__head is None:
        self.__head = new_node
        self.__tail = new_node
      else:
        self.__tail.next = new_node
        self.__tail = new_node

      self.__size += 1


  def get_by_index(self, index):

    if index < -1 or index > self.__size -1:
      raise ValueError("indice fuera de rango.")

    if index == -1:
      return self.__tail

    current_index = 0
    for current_node in self:
      if index == current_index:
        return current_node
      current_index += 1



    #current_node = self.__head
    #for _ in range(index)
    #  current_node = current_node.next

    # return current_node

  def insert_by_index(self, index, new_value):

    if index < -1 or index > self.__size:
      raise ValueError("indice fuera de rango.")

    if index == 0:
      self.prepend(new_value)
    elif index == -1 or index == self.__size:
      self.append(new_value)
    else:
      new_node = Node(new_value)
      prev_node = self.get_by_index(index-1)
      new_node.next = prev_node.next
      prev_node.next = new_node
      self.__size += 1

  def search_value(self,value):

    for current_node in self:
      if current_node.value == value:
        return True

    return False


  def set_new_value(self, value, new_value):
    for current_node in self:
      if current_node.value == value:
        current_node.value = new_value
        return True

    return False

  def pop_first(self):

    if self.__head is None:
      print("Lista vacia!!")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__head
      self.__head = self.__head.next
      self.__size -= 1
      popped_node.next = None
      return popped_node

  def pop(self):

    if self.__head is None:
      print("Lista vacia!!")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__tail
      prev_tail = self.get_by_index(self.__size-2)
      print("prev_tail",prev_tail)
      self.__tail = prev_tail
      self.__tail.next = None
      self.__size -= 1
      return popped_node

class NodeD:
  __slots__ = ('__value','__next','__prev')

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__prev = node


  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue
class DoublyLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__head = node

  @property
  def tail(self):
    return self.__tail

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__tail = node

  @property
  def size(self):
    return self.__size


  @size.setter
  def size(self,new_size):
    if not isinstance(new_size,int):
      raise TypeError("size debe ser un numero entero")
    self.__size = new_size

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def prepend(self, value):

    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      newnode.next = self.__head #enlazo nuevo nodo
      self.__head.prev = newnode
      self.__head = newnode
    self.__size += 1

  def append(self,value):
    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      newnode.prev = self.__tail
      self.__tail = newnode

    self.__size += 1

  def getbyindex(self, index):
    if index < 0 or index > self.__size:
      return "Error, indice fuera de rango"

    cont = 0
    for currentNode in self:
      if cont == index:
        return currentNode
      cont += 1

  def insertinindex(self, value, index):

    if index == 0:
      self.prepend(value)
    elif index == -1 or index == self.__size:
      self.append(value)
    else:
      prevNode = self.getbyindex(index-1)
      nextNode = prevNode.next
      newNode = NodeD(value)
      newNode.next = prevNode.next #Enlazo el next del nuevo nodo, que es el next del previo
      newNode.prev = prevNode # previo del nodo nuevo
      nextNode.prev = newNode # previo del nodo next antes de la inserción
      prevNode.next = newNode
      self.__size +=1

  def searchbyvalue(self, valuetosearch):
    for currentNode in self:
      if currentNode.value == valuetosearch:
        return True

    return False

  def setnewvalue(self, valuetochange, newvalue):
    for currentNode in self:
      if currentNode.value == valuetochange:
        currentNode.value = newvalue
        return True

    return False

  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__head.prev = None

      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode


  def pop(self):
    tempNode = self.__tail
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__tail = self.__tail.prev
      self.__tail.next = None

      self.__size -= 1

    tempNode.prev = None  #limpiar la referencia al penultimo nodo, ahora nueva cola
    return tempNode


  def generate(self, num, min, max):
    for _ in range(num):
      self.append(random.randint(min,max))


via = DoublyLinkedList()
via.append("XYZ12E-moto-1")
via.append("ABC98D-auto-3")
via.append("LMN45I-moto-1")
via.append("DEF456-camion-5")
via.append("QKA12G-moto-3")
via.append("DAR40F-moto-2")
print(via)

def paso_preferencial(via):
    ultimo_vip = None
    actual = via.head 

    while actual is not None:
      siguiente = actual.next
      datos = actual.value.split("-")
      tipo = datos[1]
      prioridad = datos[2]

      if tipo == "moto" and prioridad == "1":
        if actual != via.head:
          actual.prev.next = actual.next
          if actual.next:
            actual.next.prev = actual.prev
          else:
            via.tail = actual.prev
          
          if ultimo_vip is None:
            actual.next = via.head
            via.head.prev = actual
            via.head = actual
            actual.prev = None
          else:
            actual.next = ultimo_vip.next
            actual.prev = ultimo_vip
            if ultimo_vip.next:
              ultimo_vip.next.prev = actual
              ultimo_vip.next = actual
          ultimo_vip = actual
        else:
          ultimo_vip = actual
      actual = siguiente


     
          
        

          
            

            


    

