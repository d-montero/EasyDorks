def writeLastFive(search):
    file_path = 'history.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) > 1:
            i = int(lines[0])
        else:
            i = -1
    i = i + 1
    print(i)
    lines.append(search + '\n')

    lines[0] = str(i) + '\n'

    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)


def readLastFive(check_reversed):
    try:
        with open('history.txt', 'r') as file:
            lines = file.readlines()

        if lines:
            history_Google = []
            history_Shodan = []
            start = int(lines[0].strip())  # Obtener la primera línea y eliminar espacios en blanco
            end = len(lines)

            start += 1

            count_Google = 0
            count_Shodan = 0

            for _ in range(end-1):
                print(str(start))
                if "https://www.google.com/search?q=" in lines[start] and count_Google < 5:
                    history_Google.append(lines[start])
                    count_Google += 1
                elif "https://www.shodan.io/search?query=" in lines[start] and count_Shodan < 5:
                    history_Shodan.append(lines[start])
                    count_Shodan += 1

                start -= 1

            if check_reversed:
                history_Google.reverse()
                history_Shodan.reverse()
            return history_Google, history_Shodan
        else:
            print("El archivo está vacío.")
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Se produjo un error: {e}")

            

#writeLastFive("jose")
#writeLastFive("prueba")
#readLastFive()