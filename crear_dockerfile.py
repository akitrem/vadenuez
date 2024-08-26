import subprocess

FROM=input("ingresa el nombre de la imagen y versión: ")
print("FROM",FROM)

puerto=input("leva puerto? s/n ")
if  puerto == "s":
    EXPOSE=input("coloca los valores:" )
else:
    directorio=input("quieres elegir un directorio de trabajo? s/n ")
    if directorio == "s":
        WORKDIR=input("coloca el directorio: ")
    else:
        archivos=input("lleva archivos? s/n")
        if archivos=="s":
            COPY=input("indica el archivo html que quieras se muestre: ")
        else: 
            ejecuciones=print("lleva ejecuciones? s/n")
            if ejecuciones=="s":
                RUN=input("indica los comandos")
            else:
                CMD=input("requieres CMD?: s / n  ")
            if CMD == "s":
                print("coloca los valores:" )
            else:
                with open("Dockerfile", "w") as archivo:
    # Escribir las variables en el archivo
                    archivo.write(f"FROM {FROM}\n")
                    archivo.write(f"WORKDIR {WORKDIR}\n")
                    archivo.write(f"COPY {COPY} {WORKDIR}")
                    #archivo.write(f"RUN {RUN}")
                    archivo.write(f"EXPOSE {EXPOSE}\n")
                    archivo.write(f"COPY {COPY} /usr/share/nginx/html\n")


print("se ejecuta la creación de la imagen con el Dockerfile")
subprocess.run(["docker", "build", "-t", "nginx", "."])

print("se levanta el contenedor con la imagen creada")

subprocess.run(["docker", "run", "-d", "--name","web", f"-p{EXPOSE}:80",  "nginx"])
    
