def writeLastFive(search):
    file_path = 'history.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) > 1:
            i = int(lines[0])
        else:
            i = 0
    i = (i + 1) % 5
    print(i)
    if len(lines) < 6:
        lines.append(search + '\n')
    else:
        lines[i+1] = search + '\n'

    lines[0] = str(i) + '\n'

    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)

  

 

    
def readLastFive():
    try:
        with open('history.txt', 'r') as file:
            lines = file.readlines()

        if lines:
            history = []
            start = int(lines[0].strip())  # Obtener la primera línea y eliminar espacios en blanco
            end = len(lines)

            for _ in range(end-1):
                print(str(start))
                history.append(lines[start+1])
                start = (start-1) % 5

            print(history)
            return history
        else:
            print("El archivo está vacío.")
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Se produjo un error: {e}")

            

#writeLastFive("jose")
#writeLastFive("prueba")
#readLastFive()