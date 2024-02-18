# Password Manager


## Español
Primero que nada destaco que no recomiendo usar este metodo para la protección de sus contraseñas, en su lugar existen muchas opciones de gestores de contraseñas de gran calidad. Usar bajo su propio riesgo.

Se requiere  instalar la libreria chyptography para que el programa funcione.
El comando para la instalación es:

- pip install cryptography  

Este es un simple proyecto para probar las funcionalidades principales de cryptography.fernet y la automatización del uso de archivos python con un archivo .bat, el cual eh creado para mi propio uso.

1. Crear un archivo .txt
2. Escribir el siguiente comando:

- @echo off
- "la dirección de python.exe" "la dirección de password_manager.py"
- @pause

Por ejemplo, el mío es:

- @echo off
- "C:\Python311\python.exe" "C:\User\Desktop\repositories\password_manager\password_manager.py"
- @pause

3. Guardar el archivo como .bat en la misma carpeta del password_manager.py
4. Por último simplemente ejecuta el archvo .bat y una ventana de terminal deberia aparecer con el gestor abierto.

Si no logro crear el archivo .bat o recibio algun error al querer ejecutarlo existen múltiples tutoriales de como realizar esta tarea, por lo que no debe preocuparse y tan solo que busque alguno de ellos para encontrar solucion a sus problemas.


Por ultimo existe la posibilidad de que cambie los archivos .key existentes para utilizar uasn key generadas propias:
- Para lograrlo simplemente borre ambos archivos .key y utilizando vscode descomente las funciones writeMasterKey() y writeKey(), luego ejecute el archivo password_manager.py una vez para que estas key se creen. Por ultimo no olvide volver a comentar ambas funciones para evitar que se produzca un error o que se sobreescriban las key generadas.
- Esto debe realizarse la primera vez que se usa el programa o en su defecto borrando el archivo master_password.txt dado que no podra desencriptar la contraseña al ser borrad el archivo masterKey.key.

## English
First of all I emphasize that I do not recommend using this method for password protection, instead there are many options of high quality password managers. Use at your own risk.

The chyptography library must be installed for the program to work.
The command to install it is:

- pip install cryptography

This is a simple proyect to test core functionalities of cryptography.fernet and the automation of the usage of python files with a .bat file, which i create for my own doing this steps.

1. Create a .txt file
2. write the following command:

- @echo off
- "the addres of python.exe" "the addres of password_manager.py"
- @pause

For example, mine is:

- @echo off   
- "C:\Python311\python.exe" "C:\User\Desktop\repositories\password_manager\password_manager.py"
- @pause

3. save the file as .bat in the same folder of the password_manager.py
4. Now just open .bat file and a terminal window should appear with the password manager running.

If you did not manage to create the .bat file or received an error when trying to execute it, there are multiple tutorials on how to perform this task, so you should not worry and just look for any of them to find a solution to your problems.


Finally there is the possibility to change the existing .key files to use your own generated keys:
- To achieve this simply delete both .key files and using vscode uncomment the writeMasterKey() and writeKey() functions, then run the password_manager.py file once so that these keys are created. Finally do not forget to comment out both functions again to avoid getting an error or overwriting the generated keys.
- This must be done the first time you use the program or by deleting the master_password.txt file since you will not be able to decrypt the password when the masterKey.key file is deleted.