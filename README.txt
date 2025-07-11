*Exposicipon del problema--> Dentro del campus empresarial se hizo adquisicion de un huellero ZKTIME para el control y registro de asistencia
    El cual dispone de una gestion de descarga manual a través de una USB, siendo esta una gestion muy ineficiente.
    Posterior a eso el area de sistemas -Michael y Juan, comenzaron el desarrollo de una aplicacion que tuviera el poencial de facilitar la gestion de dichos registros

Implementacion de la solucion -> Usando las tecnologias de python, mysql y sqlserver;
    Se analizó el problema buscando la solucion más eficiente,
    despues del analisis se llegó a la concluysion que lo mejor era fetchear los registros a traves de la libreria diseñada para ZKTIME
    , para posteriormente almacenarlos de forma ordenada en una base de datos Relacional (MySQL), procediendo con la exportacion base de PHPMyAdmin a CSV
    y con las herramientas de excel generar tabla dinamica que maneje el registro de forma comoda y visual
