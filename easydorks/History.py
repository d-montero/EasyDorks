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
        file = open('C:\\Users\\usuario\\Desktop\\Universidad\\Tercer año\\Ing.Software\\EasyDorks-1\\easydorks\\history.txt','r')
        file.seek(0)
        start = file.read()
        lines = file.readlines()
        end = len(lines-1)
        for line in range(start,end):
            print(lines[line])
        
        end = end-start 
        start = 0
        for i in range(start,end):
            print(lines[i])
    except:
        print("Fichero no encontrado")  
            

writeLastFive("jose")
writeLastFive("prueba")
readLastFive()