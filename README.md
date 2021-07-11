# mutantes
Api creada con Python y base de datos Redis. Responde al enunciado adjunto nombrado como Mutantes.pdf. 

Implementado en EC2 con docker, donde también se agregó gunicorn y nginx para resolver las peticiones.

Para realizar la implementación en docker se debe ejecutar el siguiente comando:
```
docker-compose up --build -d
```
Anteriomente asegurarse de tener copiados todos los archivos y directorios, además de estar situados en donde se encuentra el archivo docker-compose.yml.

## Diagrama
![diagrama](https://github.com/jssknn/mutantes/blob/main/diagrama.png)

## Servicios
### /mutant
Se realiza una solicitud post ingresando como parámetro un adn para verificar y se obtiene una respuesta diferente según el resultado.
```
POST → /mutant/
{
  "dna":["AAAAGA", "CAGTGC", "TTCTAT", "AGAAGG", "CCCCTA", "TCACTG"]
}
```
- Si verifica que el adn pertenece a un mutante devuelve HTTP 200-OK y la siguiente respuesta:

  {
    "mutant":true
  }
- Si verifica que el adn no pertenece a un mutante devuelve 403-Forbidden y la siguiente respuesta:

  {
    "mutant":false
  }
- Si se produce una excepción por parámetros incorrectos devuelve 400-Bad Request y una respuesta como la siguiente:

  {
    "error":"Faltan ingresar parámetros"
  }

- Si existe un error interno con el servicio devuelve 500-Internal server error y la siguiente respuesta:

  {
    "error":"Error interno en el servidor"
  }
### /stats
Se realiza una solicitud GET sin ingresar parámetros y se obtiene como respuesta un json con los resultados de los análisis realizados hasta el momento.
```
GET → /stats 
```
Respuesta: {
  "count_human_dna":10, "count_mutant_dna":2, "ratio":0.2
}

## Funcionamiento
![postman](https://github.com/jssknn/mutantes/blob/main/postman.gif)

## Algoritmo
Realiza la búsqueda de coincidencias de manera secuencial. Primero horizontalmente, luego verticalmente, después de forma oblicua tomando las diagonales que van desde la esquina superior izquierda hacia la inferior derecha y por último sobre las diagonales que van desde la esquina superior derecha hacia la inferior izquierda.

Todo esto lo hace buscando la secuencia de letras consecutivas en una lista de cadenas, en cada bloque está la posibilidad de salir si el acumulador de coincidencias es mayor a uno.
 

## Coverage
El test de código se realizó mediante unittest y el reporte de cobertura con el módulo coverage de Python. 

Dentro de la carpeta /test se encuentran los archivos generados.

![diagrama](https://github.com/jssknn/mutantes/blob/main/coverage.PNG)
