def sistema_reciclaje():
   # saludado inicial
    print("--- Bienvenida a nuestro sistema de reciclaje ---")
    
    # ciclo principal del programa
    while True:
        print("\n¿Qué te gustaría hacer hoy?")
        print("1. No tengo espacio (Optimizar/Limpiar)")
        print("2. Está muy lento (Mantenimiento)")
        print("3. Donar")
        print("4. Desechar")
        print("5. Reutilizar")
        print("6. Salir")
        # creando la variable para almacenar la opción del usuario
        opcion = input("\nSelecciona una opción (1-6): ")
        # if statement para cada opción
        if opcion == "1" or opcion == "2":
            print(">> Entendido. Iniciando proceso de diagnóstico y limpieza...")
            
        elif opcion == "3":
            print(">> ¡Gracias por tu generosidad! Tráelos a la dirección: Calle 701923.")
            
        elif opcion == "4":
            print(">> Nota: Se aplicarán cargos por el servicio de desecho.")
            confirmar = input("¿Deseas continuar? (s/n): ").lower()
            if confirmar == "s":
                print(">> Perfecto, puedes traerlo a la oficina central.")
            
        elif opcion == "5":
            print(">> ¡Excelente elección! Nuestro taller está en: 725 Riverwalk Parkway.")
            
        elif opcion == "6":
            print("¡Gracias por usar nuestro sistema! Hasta luego.")
            break
            
        else:
            print(">> Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el programa
sistema_reciclaje()