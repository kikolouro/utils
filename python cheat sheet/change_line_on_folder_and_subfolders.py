import os, time


cont = 0
global contalterados
contalterados = 0

def valida(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    global contalterados
    with open(filename) as f:
        s = f.read()
        if old_string not in s:            
            return
    

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)
        contalterados += 1

start = time.time()
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(".okm"):
            cont += 1
            valida(f"{root}/{file}", "Gestão Promoções + Prestadores", "Gestao_Promocoes_Prestadores")
            valida(f"{root}/{file}", "Dep Comercial", "Dep_Comercial")
            valida(f"{root}/{file}", "Dep Criativo", "Dep_Criativo")
            valida(f"{root}/{file}", "Dep Tecnico", "Dep_Tecnico")
end = time.time()
print(f"Demorou: {end - start}")
print(f"Número de ficheiros: {cont}")
print(f"Número de ficheiros alterados: {contalterados}")