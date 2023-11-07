def writeLastFive(search):
    file_path = 'C:\\Users\\usuario\\Desktop\\Universidad\\Tercer año\\Ing.Software\\EasyDorks-1\\easydorks\\history.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) > 1:
            i = int(lines[0])
        else:
            i = 0
    i = (i + 1) % 5
    search_lines = lines[1:]  # Excluye la primera línea (índice)
    search_lines.append(search + '\n')
    
    if len(search_lines) > 5:
        search_lines = search_lines[-5:]

    search_lines.insert(0, str(i) + '\n')  # Inserta i en la primera posición

    with open(file_path, 'w') as file:
        for line in search_lines:
            file.write(line)

  

 

    
def readLastFive():
    try:
        with open('easydorks\history.txt', 'r') as file:
            lines = file.readlines()

        if lines:
            start = int(lines[0].strip()) # Obtener la primera línea y eliminar espacios en blanco
            end = len(lines)

            for line in range(start, end):
                print(lines[line].strip())
            
            end = start
            start = 1
            for line in range(start,end):
                print(lines[line].strip())
        else:
            print("El archivo está vacío.")
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Se produjo un error: {e}")



            

#writeLastFive("jose")
#writeLastFive("prueba")
readLastFive()