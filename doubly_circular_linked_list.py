from node import Node

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None

    def print_list(self):
        if not self.head:
            print("La lista esta vacia")
            return

        current = self.head
        while True:
            print(f"Nombre: {current.name}\nAutor: {current.author}", end="")
            current = current.next

            if current == self.head:
                break
        print()

    def insert_at_start(self, name, author):
        new_node = Node(name, author)

        if not self.head:
            self.head = new_node
            self.prev = new_node
            self.head.next = self.head
            self.head.prev = self.prev
        else:
            new_node.next = self.head
            new_node.prev = self.prev
            self.head.prev = new_node
            self.prev.next = new_node
            self.head = new_node

    def delete(self, name, author):
        if not self.head:
            print("La lista esta vacia")
            return

        current = self.head

        while True:
            if current.name == name and current.author == author:
                break
            current = current.next
            if current == self.head:

                return

        if current.next == self.head and current.prev == self.head:
            self.head = None
        else:
            if current == self.head:
                self.head = current.next


            current.prev.next = current.next
            current.next.prev = current.prev


        current.prev = None
        current.next = None

    def update(self, old_name, old_author, new_name, new_author):
        if not self.head:
            print("La lista esta vacia")
            return

        current = self.head
        while True:
            if current.name == old_name and current.author == old_author:
                break
            current = current.next
            if current == self.head:
                return

        current.name = new_name
        current.author = new_author

    def search(self, name, author):
        if not self.head:
            print("La lista está vacía.")
            return

        current = self.head
        while True:
            if current.name == name and current.author == author:
                print(f"La canción '{name}' de '{author}' está en la lista.")
                return

            current = current.next
            if current == self.head:
                print(f"La canción '{name}' de '{author}' no está en la lista.")
                return

    def get_previous_song(self, name, author):
        if not self.head:
            print("La lista está vacía.")
            return

        current = self.head
        while True:
            if current.name == name and current.author == author:
                print(
                    f"La canción anterior a '{name}' de '{author}' es '{current.prev.name}' de '{current.prev.author}'.")
                return

            current = current.next
            if current == self.head:
                print(f"La canción '{name}' de '{author}' no está en la lista.")
                return

    def get_next_song(self, name, author):
        if not self.head:
            print("La lista está vacía.")
            return

        current = self.head
        while True:
            if current.name == name and current.author == author:
                print(
                    f"La siguiente canción a '{name}' de '{author}' es '{current.next.name}' de '{current.next.author}'.")
                return

            current = current.next
            if current == self.head:
                print(f"La canción '{name}' de '{author}' no está en la lista.")
                return