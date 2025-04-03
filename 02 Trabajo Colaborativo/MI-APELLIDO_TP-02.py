Trabajo Colaborativo, Máximo Ponce 
qué es github 
 es una plataforma online para almacenar y gestionar código usando git, permite trabajar en equipo y llevar el control de versiones 

cómo crear un repositorio en github 
 iniciar sesión en github, ir a "new repository", ponerle un nombre, elegir si será público o privado y hacer clic en "create repository" 

cómo crear una rama en git 
 usar el comando: 
 git branch nombre_de_la_rama 

cómo cambiar a una rama en git 
 git checkout nombre_de_la_rama 

cómo fusionar ramas en git 
 primero cambiar a la rama principal (main o master): 
 git checkout main 
 luego fusionar la otra rama: 
 git merge nombre_de_la_rama 

cómo crear un commit en git 
 agregar los cambios: 
 git add . 
 luego hacer el commit: 
 git commit -m "mensaje del commit" 

cómo enviar un commit a github 
 git push origin nombre_de_la_rama 

qué es un repositorio remoto 
 es un repositorio alojado en la nube sincronizado con el local 

cómo agregar un repositorio remoto en git 
 git remote add origin url_del_repositorio 

cómo subir cambios a un repositorio remoto 
 git push origin nombre_de_la_rama 

cómo obtener cambios de un repositorio remoto 
 git pull origin nombre_de_la_rama 

qué es un fork en github 
 es una copia de un repositorio de otra persona en tu cuenta para modificarlo sin afectar el original 

cómo hacer un fork en github 
 entrar al repositorio y hacer clic en "fork" 

cómo hacer un pull request en github 
 ir a "pull requests" en github y crear uno, seleccionando la rama que querés fusionar 

cómo aceptar un pull request 
 el dueño del repo va a "pull requests", revisa y hace clic en "merge pull request" 

qué es una etiqueta en git 
 un marcador para versiones o hitos importantes dentro del historial de commits 

cómo crear una etiqueta en git 
 git tag -a v1.0 -m "mensaje de la etiqueta" 

cómo subir una etiqueta a github 
 git push origin v1.0 

qué es el historial de git 
 es el registro de todos los commits realizados en el repositorio 

cómo ver el historial de git 
 git log 

cómo buscar en el historial de git 
 git log --grep="palabra clave" 

cómo borrar el historial de git 
 no se puede borrar del todo pero se puede resetear con: 
 git reset --hard HEAD~n (para deshacer los últimos "n" commits) 

qué es un repositorio privado en github 
 un repositorio que solo pueden ver quienes tengan permiso 

cómo crear un repositorio privado en github 
 en "new repository", seleccionar "private" 

cómo invitar a alguien a un repositorio privado 
 ir a "settings" > "manage access" y agregar colaboradores 

qué es un repositorio público en github 
 un repositorio visible para cualquiera 

cómo crear un repositorio público en github 
 en "new repository", seleccionar "public" 

cómo compartir un repositorio público en github 
 basta con compartir el enlace del repositorio 
