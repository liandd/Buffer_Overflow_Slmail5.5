# Practica_Bof
Buffer Overflow al Binario Slmail 5.5

## Firewall de Windows y reglas de Entrada/Salida - Configuracion Parte 1

Lo primero es configurar una maquina Windows para montar el entorno de practica, y es importante que este bien configurado para tener comunicacion entre maquinas `(La maquina Windows con el binario vulnerable, y nuestra maquina de atacante).`

> *Se usara un sistema Windows 7 de 32 bits, la version starter.*

![W7](https://github.com/liandd/Practica_Bof/assets/114973749/feba7cd3-eff2-4f1d-b48f-2a5bc8c19a60)


> 

Despues de instalar la maquina Windows, es muy importante que haya comunicacion entre las 2 maquinas mediante trazas **ICMP**, debido a que por defecto estas reglas vienen deshabilitadas, por tanto, para lograr esta configuracion debemos ir a la configuracion avanzada de firewall de Windows y habilitar las reglas de Entrada/Salida para tener la comunicacion por iPv4 y por iPv6:

![ReglasEntrada](https://github.com/liandd/Practica_Bof/assets/114973749/16f4d2e5-2dab-43eb-afea-e7595c602dce)


> En la imagen se muestran las reglas de entrada donde hay que habilitar las 4 reglas para poder recibir una comunicacion de nuestra maquina de atacante, de esta forma habra una comunicacion, por tanto hay que repetir el proceso para las reglas de salida:

![ReglasSalida](https://github.com/liandd/Practica_Bof/assets/114973749/2e52b53c-1f11-46c4-aadd-b19c25689bce)


> 

Una vez con las reglas habilitadas probamos la comunicacion:

![PruebaPing](https://github.com/liandd/Practica_Bof/assets/114973749/b6958bf8-b00e-4a8c-9618-fcd339db4a0f)


> 

Al enviar 4 paquetes y recibirlos confirma que hay comunicacion entre maquinas completando el primer paso para dar inicio a la practica del BufferOverflow.

## Desactivar el DEP - Configuracion Parte 2

Esta parte es importante, debemos abrir un simbolo del sistema como administrador y ejecutar el siguiente comando:

```cmd
bcdedit.exe /set {current} nx AlwaysOff
```

![DEP](https://github.com/liandd/Practica_Bof/assets/114973749/5020a115-7f7e-4295-95e0-efa448f5bbe5)


>
Estamos desactivando el *DEP* `(Data Execution Protection)`, pero para todo el sistema, tambien se puede hacer para el binario Slmail concretamente desde el apartado GUI, pero al ser una maquina virtual que su unico proposito es la practica de BufferOverflow y despues sera eliminada. La verdad es que no supone ningun problema este comando.

> *Debemos reiniciar el sistema para que se apliquen los cambios* 


## Utilidades - Configuracion Parte 3

Para las utilidades se descargaran unas aplicaciones para hacer el trabajo mas comodo, por tanto, se descargara el binario al cual vamos a atacar *(Slmail_5.5 ya que es vulnerable a BOF)* la aplicacion Inmunity Debugger para monitorizar todo a bajo nivel.

![image](https://github.com/liandd/Practica_Bof/assets/114973749/e23e9548-3803-475a-97b5-8a4924fc237b)


![BOFF](https://github.com/liandd/Practica_Bof/assets/114973749/2ec231d8-77d5-4b7c-b7be-1ed46a96d507)
