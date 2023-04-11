def main():
    doc = open('./miDoc.txt', 'a')
    doc.write('Nombre: Angel\nApellido: Pacheco\nEdad:23\n\nEstoy aprendiendo a desarrollar.\n\n')
    doc.write('Accediendo dos veces al texto.')

if __name__ == '__main__':
    main()