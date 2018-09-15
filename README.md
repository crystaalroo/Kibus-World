# Kibus-World

## SECUENCIA DEL CODIGO
La función setup() siempre corre antes de que se corra el draw(), se puede decir entonces que lo que pasa en setup() no depende de los hilos que están corriendo en draw(). Es por eso, que para el hecho de que el usuario (en este caso yo), pudiera fijar primero el porcentaje de obstáculos, la función en la que se decidía tuvo que ser llamada desde setup(), que es la función seleccionarObstaculos(). La cual se encarga de, estando fijo el porcentaje de obstáculos, se calcula la cantidad de posiciones que deben tener estos obstáculos para cumplir con la cuota. En este caso, el porcentaje se calcula sobre las 400 posiciones disponibles en la matriz de 20x20. Una vez que se fijan los obstáculos, estos se representan en la matriz y se eligen sus posiciones de materia aleatoria.
Posición (x,y) en la que se coloca al destino de la actividad.
Variable que indica que elemento de la lista POS debe ser visualizada en la función draw()
Booleano que indica cuando ya se puede comenzar a trazar la ruta del agente.
Variable que guarda la posición a la que se intento llegar por medio del algoritmo pero ya estaba ocupada por un obstáculo
 Booleano que determina si el agente ya no puede seguir ningún camino para llegar al destino o si si ya alcanzo el destino.
Posición en la que se encuentra el agente durante el recorrido.

Después se espera a que se cumplan las condiciones en la función mousePressed() (función de processing) para determinar la posición en la cual se ubicará el agente y en la que se ubicará su destino. Es decir, que estos no se coloquen sobre una posición con un obstáculo.
Una vez que se han fijado, se llama a la función ruta(), la cual contiene un ciclo dentro que termina solo cuando el agente llega a su destino o bien, que se determina que el agente ya no se puede mover de su posición. La función ruta(), llama a la función bresenham() que se encarga de trazar la linea desde la posición actual del agente hasta el destino. Si no es posible que el agente avance a la posición indicada por el algoritmo, entonces es necesario recurrir al comportamiento emergente. Este esta dado en la función cambio(). La cual se encarga de determinar cuales de los movimientos permitidos llevaran al agente a una casilla sin obstáculo.
Una vez que se tienen estas casillas, se realiza un random para determinar a cual de las casillas es a la que debe moverse. Y entonces, se traza bresenham() con la nueva casilla inicial. Pero, antes de moverse a esta casilla, la casilla en la que se genero el comportamiento emergente queda marcada con un estado, que nos permite conocer si esta casilla es parte de alguna de las rutas de solución o si es mejor que se corrija la ruta. Todas las casillas están inicializadas en 0, excepto los obstaculos. Cada vez que se genera un comportamiento emergente, el estado de la casilla incrementa en 1. Cuando llega a 5 queda marcada como un obstáculo y ya no es posible pasar a esa casilla.
En el caso en el que no le es posible moverse a ninguna casilla adyacente, se verifica si es posible que se mueva a la casilla anterior a la que estaba. De ser así, el agente regresa a esa posición. Si el agente ya no puede volver a la casilla por la que llego, entonces se dice que el agente esta atrapado y ya no le es posible llegar al destino. Por lo que el programa termina de forma no satisfactoria.
Cuando el agente por fin alcanza la casilla destino o termina, es momento de llamar a draw().
Cada vez que el agente se movía, su posición y el estado de la casilla quedada guardado en una lista. Esta lista la usa draw(), quien se encarga de imprimir en pantalla el icono del agente en la posición que le indica el iterador sobre la matriz. Ademas, para representar el estado, se muestra una imagen del obstáculo un poco translucida, que se vuelve mas solida conforme aumenta el estado.

## VIDEO DE DEMOSTRACIÓN:
[Youtube](https://youtu.be/gQ6tDfe0t3E)


