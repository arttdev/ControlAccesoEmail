#import
import mysql.connector
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from getpass import getpass

#Loggin del Çorreo

# Datos del usuario
username = "puertaprincipal@visan.net.co" # Enter your email address
password = 'Casa1242!' # Enter your password

# Crear conexión 
imap = imaplib.IMAP4_SSL("imap-mail.outlook.com")
# iniciar sesión
imap.login(username, password)

status, mensajes = imap.select("INBOX")
# print(mensajes)
# mensajes a recibir
N = 3
# cantidad total de correos
mensajes = int(mensajes[0])

for i in range(mensajes, mensajes - N, -1):
    # print(f"vamos por el mensaje: {i}")
#     # Obtener el mensaje
    try:
        res, mensaje = imap.fetch(str(i), "(RFC822)")
    except:
        break
    for respuesta in mensaje:
        if isinstance(respuesta, tuple):
            # Obtener el contenido
            mensaje = email.message_from_bytes(respuesta[1])
            # decodificar el contenido
            subject = decode_header(mensaje["Subject"])[0][0]
            if isinstance(subject, bytes):
                # convertir a string
                subject = subject.decode('iso-8859-1')
            # de donde viene el correo
            from_ = mensaje.get("From")
            print("Subject:", subject)
            print("From:", from_)
            print("Mensaje obtenido con exito")
            # si el correo es html
            if mensaje.is_multipart():
                # Recorrer las partes del correo
                for part in mensaje.walk():
                    # Extraer el contenido
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # el cuerpo del correo
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # Mostrar el cuerpo del correo
                        #print(body)
                        print("mensaje obtenido")
                    elif "attachment" in content_disposition:
#                         # download attachment
                        nm = part.get_filename()
                        #remove ? character from filename
                        nm = nm.replace("?", "")
                        #remove % character from filename
                        nm = nm.replace("%", "")
                        #remove / character from filename
                        nm = nm.replace("/", "")
                        #remove : character from filename
                        nm = nm.replace(":", "")
                        #remove * character from filename
                        nm = nm.replace("*", "")
                        #remove < character from filename
                        nm = nm.replace("<", "")
                        #remove > character from filename
                        nm = nm.replace(">", "")
                        #remove | character from filename
                        nm = nm.replace("|", "")
                        #remove \ character from filename
                        nm = nm.replace("\r\n", "")
                        #remove = character from filename
                        nm = nm.replace("=", "")
                       # nombre_archivo = nm.lstrip("?")
                        nombre_archivo = nm
                        if nombre_archivo: 
                            #if not os.path.isdir(subject):
                                # crear una carpeta para el mensaje
                                #os.mkdir(subject)
                            ruta_archivo = os.path.join("d:\\ProgramminProjects//Pdfs_Acceso", nombre_archivo)
                            # download attachment and save it
                            open(ruta_archivo, "wb").write(part.get_payload(decode=True))
                                                
            else:
                # contenido del mensaje
                content_type = mensaje.get_content_type()
                # cuerpo del mensaje
                body = mensaje.get_payload(decode=True).decode()
                if content_type == "text/plain":
#                     # mostrar solo el texto
                    print(body)
            # if content_type == "text/html":
            #     # Abrir el html en el navegador
            #     if not os.path.isdir(subject):
            #         os.mkdir(subject)
            #     nombre_archivo = f"{subject}.html"
            #     ruta_archivo = os.path.join(subject, nombre_archivo)
            #     open(ruta_archivo, "w").write(body)
            #     # abrir el navegador
            #     webbrowser.open(ruta_archivo)
#             print("********************************")
imap.close()
imap.logout()






#remover pdf
path = "d:\\ProgramminProjects//Pdfs_Acceso"
words = "CEDULA", "ARL", "Cedula", "cedula", "Arl", "cedula", "arl"
formatos = ".pdf", ".txt", ""
for filename in os.listdir(path):
    if filename.endswith(formatos): 
        for word in words:
            if word in filename:
                os.remove(os.path.join(path, filename))
                print(filename)
                break

#Analisar Autorizaciones 




#Definir Variables de excel

fnm = "Edwar B. Pérez"

cc = '12345678911'
d_in = '2022-03-01'
d_out = '2020-03-15'
#Conectar e insertar a la BD
#connect to mysql db
host = "b3cvcygkyegtm1gdqftb-mysql.services.clever-cloud.com"
user = "ubpgiv8l1efupgvl"
password = "kFLCmNZ5KaxU8l23rTij"
database = "b3cvcygkyegtm1gdqftb"
mysql.connector.connect(host=host, user=user, password=password, database=database)
if mysql.connector.connect(host=host, user=user, password=password, database=database):
    print("Conexion exitosa")
    print("Conectado a la base de datos")
    db_Info = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = db_Info.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print("Version:", version)

    query = 'INSERT INTO accessed(nm,f_in,f_out,proof) VALUES(%s,%s,%s,%s)'
    data = (fnm,d_in,d_out,cc)
    cursor.execute(query, data)
    db_Info.commit()
    print("Datos insertados")
    cursor.execute("SELECT * FROM `accessed`")
    for row in cursor:
        print(row)
    cursor.close()
    db_Info.close()
else:
    print("No se pudo conectar a la base de datos") 

