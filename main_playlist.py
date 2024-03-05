from doubly_circular_linked_list import DoublyCircularLinkedList

playlist = DoublyCircularLinkedList()

while True:
    title = "Menu reproductor de cancines"
    print("\n" + title + "\n" + len(title) * '-')
    print("1. Agregar cancion a la playlist")
    print("2. Eliminar cancion de la playlist")
    print("3. Editar la playlist")
    print("4. Buscar cancion en la playlist")
    print("5. Cancion anterior")
    print("6. Siguiente cancion")
    print("7. Mostrar la playlist")
    print("8. Salir del programa")

    playlist_menu = input("\nIngrese una opcion: ")

    if playlist_menu == "1":
        name = input('Ingrese el nombre de la cancion: ')
        author = input('Ingrese el autor de la cancion: ')

        playlist.insert_at_start(name, author)
        print(f"La cancion {name} del autor {author}, se agrego exitosamente")

    elif playlist_menu == "2":
        name = input("Ingrese el nombre de la canción a eliminar: ")
        author = input("Ingrese el autor de la canción a eliminar: ")

        playlist.delete(name, author)
        print(f"Canción '{name}' de '{author}' eliminada exitosamente.")

    elif playlist_menu == "3":
        old_name = input("Ingrese el nombre de la canción a actualizar: ")
        old_author = input("Ingrese el autor de la canción a actualizar: ")
        new_name = input("Ingrese el nuevo nombre de la canción: ")
        new_author = input("Ingrese el nuevo autor de la canción: ")

        playlist.update(old_name, old_author, new_name, new_author)
        print(f"Información de la canción '{old_name}' de '{old_author}'"
              f" actualizada a '{new_name}' de '{new_author}'.")

    elif playlist_menu == "4":
        name = input("Ingrese el nombre de la canción a buscar: ")
        author = input("Ingrese el autor de la canción a buscar: ")

        playlist.search(name, author)

    elif playlist_menu == "5":
        name = input("Ingrese el nombre de la canción: ")
        author = input("Ingrese el autor de la canción: ")

        playlist.get_previous_song(name, author)

    elif playlist_menu == "6":
        name = input("Ingrese el nombre de la canción: ")
        author = input("Ingrese el autor de la canción: ")

        playlist.get_next_song(name, author)

    elif playlist_menu == "7":
        print("Playlist actual")

        playlist.print_list()

    elif playlist_menu == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Ingrese una opcion valida")