# BOT para Discord con Python

En este template vamos a crear un bot la api de discord para python. Para llevar adelante este proyecto se recomienda leer el siguiente [tutorial](https://www.pragnakalp.com/create-discord-bot-using-python-tutorial-with-examples/) que es el más actualizado al día de la fecha (febrero de 2023).

Vale la pena decir que según lo dispuesto por Discord (leer [aquí](https://support-dev.discord.com/hc/en-us/articles/4404772028055-Message-Content-Privileged-Intent-FAQ)), no será posible que los bots creados después de septiembre del 2022 puedan acceder a todos los mensajes y su contenido dentro de un servidor. Solo podrán leer aquellos mensajes que sean enviados por mensaje privado o haciendo mención al bot en cuestión. Esto no quita merito al proyecto y si bien limita la cantidad de funcionalidades disponibles, no necesariamente limita las posibilidades a generar con bots implementados a través de estas tecnologías.

Por lo mencionado anteriormente, es posible que discord rechace bot que se encuentren configurados para acceder a todos los permisos

```python
intents = Intents.all()
bot = Client(intents=intents)
```

La clase `Intents` es la encargada de solicitar los permisos necesarios por parte de la aplicación cliente. Si desde el [portal de desarrollo](https://discord.com/developers/applications) no se configuraron los permisos adecuadamente, es probable que la línea `intents = Intents.all()` cause algunos problemas. Pero si se siguió el [tutorial](https://www.pragnakalp.com/create-discord-bot-using-python-tutorial-with-examples/) adecuadamente, no debería haber inconvenientes.

## Entorno

Asegurarse de tener instalado `git` . Esto se puede revisar muy fácilmente a través del comando `git --version` . En caso de no estar instalado, se puede hacer a través de los siguientes paso

- En Linux, a través del comando `sudo apt install git`.
- En Windows, a través de la pagina oficial https://git-scm.com/

Tener actualizado `python` a la versión `lts`. Si desea asegurarse, puede ejecutar el comando `python --version` que le indicara la versión de `python` instalado en su sistema. Este debe ser `3.9` o superior. Si no esta instalado, puede obtener:

- En windows, desde Microsoft Store.
- En Linux, consulte en las fuentes oficiales de cada distro para actualizar `python` ya que este suele estar instalado por defecto.

Por último, instalar o actualizar `pipenv` como gestor de dependencias para este proyecto. Esto se puede hacer mediante el comando `pip install --user pipenv`. Para más información, visitar https://pipenv.pypa.io/en/latest/



## Variables de entorno

- 🔐TOKEN: token de seguridad provisto por el [portal de desarrolladores](https://discord.com/developers/applications) de discord para cada bot. Adjunto a este proyecto existe un archivo `.env.example` que puede usar para colocar su propio token.

## Instalación y ejecución

- 🛠Para instalar las dependencias ejecutar el siguiente comando `pipenv install`
- ⚒Para ejecutar el modo playground o repl, ejecutar el siguiente comando `pipenv run dev`

 
