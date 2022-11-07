password = 2002
attempt = 0
while attempt != password:
    attempt = int(input(""))
    if attempt == password:
        print("Acceso Permitido")
        break
    else:
        print("Contraseña No Válida")