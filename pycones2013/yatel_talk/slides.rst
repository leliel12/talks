.. =============================================================================
.. ICONS
.. =============================================================================

.. |utnico| image:: img/utnico.png
.. |intaico| image:: img/intaico.png
.. |conicetico| image:: img/conicetico.png


.. =============================================================================
.. CONTENT
.. =============================================================================

Yatel - OLAP sobre redes
------------------------

.. image:: img/log.png
    :align: center
    :scale: 100 %


Integrantes
-----------

- |utnico|  - García, Mario Alejandro
- |utnico|  - Cabral, Juan Bautista
- |intaico|  - Gimenez Pecci, María de la Paz
- |utnico|  - Vera, Carlos
- |utnico|  - Liberal, Rodrigo
- |conicetico| |intaico|  - Laguna, Irma Graciela
- |intaico|  - Bisonard, Eduardo Matías
- |intaico|  - Maurino, Fernanda
- |intaico|  - Vankeirsbilck, Inés
- |utnico|  - Cucco, Noelia del Valle
- |utnico|  - Nieto Castillo, Adrián L.

Paper
-----

- **Título:** “Interactive network exploration in the KDD process, Contributions
  in the study of population variability of a Corn Fijivirus”
- **Autores:** M. A. García, M. P. Giménez Pecci, J. B. Cabral, A. Nieto, I. G. Laguna.
- **Publicación:** Journal of Data Mining in Genomics & Proteomics 2012 3:3
- **Editorial:** OMICS Publishing Group
- **ISSN:** 2153-0602. Año: 2012
- **URL:** http://goo.gl/pcjdG

.. image:: img/qr.png
    :align: center
    :scale: 100 %


Agenda
------

- Un poco de historia y motivaciones.
- Un poco de KDD.
- Un poco de Network Science.
- Proceso de Analisis.
- DW - OLAP - BI (hasta acá debería tardar no mas de 20 minutos)
- El proyecto en sí
- Mini Demo

.. image:: img/to_do_list.jpg
    :align: center
    :scale: 120 %


Historia: Mal de Río Cuarto virus
---------------------------------

- Análisis electroforético:

.. image:: img/electroforesis.png
    :align: center
    :scale: 100 %

- Base de datos formada por

    - Perfiles electroforéticos.
    - Atributos que definen el ambiente de la planta

- Pocos datos: Propuesta transformar la DB en una red y medir su variabilidad.

.. image:: img/r4to.png
    :align: right
    :scale: 40 %


Knowledge Discovery in Database (KDD)
-------------------------------------

- Es un proceso no trivial de identificación de información útil y desconocida
  que permanece oculta en una base de datos [Fayyad, 1996]

- Es un proceso centrado en la persona (human-centered) [Brachman, 1996]


.. image:: img/mining.png
    :align: center
    :scale: 20 %


Network Science
---------------

- Es el estudio de las redes que representan fenómenos físicos, biológicos y
  sociales conduciendo a modelos predictivos de estos fenómenos.
- Topologías.
- Características comunes.

.. image:: img/vuelos.png
    :align: right
    :scale: 35 %


Networks 1
----------

.. figure:: img/proteina.png
    :align: center
    :scale: 100 %

    Interacción proteína-proteína


Networks 2
----------

.. figure:: img/money.png
    :align: center
    :scale: 50 %

    Redes sociales/económicas


Networks 3
----------

.. figure:: img/energy.png
    :align: center
    :scale: 100 %

    Red de distribución de energía


Networks 4
----------

.. figure:: img/motor.png
    :align: center
    :scale: 100 %

    Relación entre automotrices


Networks 5
----------

.. figure:: img/bbt.png
    :align: center
    :scale: 35 %

    Red semántica TBBT


Proceso de análisis
-------------------

Los ejemplos van con nuestra investigación (osea: resumen del paper)

.. image:: img/kdd0.png
    :align: center
    :scale: 200 %


Proceso de análisis: Identificación y representación de haplotipos
------------------------------------------------------------------

.. image:: img/kdd1.png
    :align: center
    :scale: 200 %


Proceso de análisis: Identificación y representación de haplotipos
------------------------------------------------------------------

.. image:: img/viejo.png
    :align: center
    :scale: 35 %


Proceso de análisis: Identificación y representación de haplotipos
------------------------------------------------------------------

.. image:: img/tablaperfiles.png
    :align: center
    :scale: 200 %


Proceso de análisis: Definición de medidas de distancia
-------------------------------------------------------

.. image:: img/kdd2.png
    :align: center
    :scale: 200 %


Proceso de análisis: Definición de medidas de distancia
-------------------------------------------------------

.. image:: img/dit.png
    :align: center
    :scale: 60 %


Proceso de análisis: Cálculo de distancias
------------------------------------------

.. image:: img/kdd3.png
    :align: center
    :scale: 200 %


Proceso de análisis: Cálculo de distancias
------------------------------------------

.. image:: img/calc.png
    :align: center
    :scale: 200 %


Proceso de análisis: Creación de la red
---------------------------------------

.. image:: img/kdd4.png
    :align: center
    :scale: 200 %


Proceso de análisis: Creación de la red
---------------------------------------

.. image:: img/red0.png
    :align: center
    :scale: 200 %


Proceso de análisis: Visualización y análisis topológico
--------------------------------------------------------

.. image:: img/kdd5.png
    :align: center
    :scale: 200 %


Visualización y análisis topológico
-----------------------------------

.. image:: img/est.png
    :align: center
    :scale: 300 %


Proceso de análisis: Exploración
--------------------------------

.. image:: img/kdd6.png
    :align: center
    :scale: 200 %


Proceso de análisis: Exploración
--------------------------------

.. image:: img/exp.png
    :align: center
    :scale: 150 %


Proceso de análisis: Generación de hipótesis y conclusiones
-----------------------------------------------------------

.. image:: img/kdd7.png
    :align: center
    :scale: 200 %


Proceso de análisis: Generación de hipótesis y conclusiones
-----------------------------------------------------------

.. image:: img/conc.png
    :align: center
    :scale: 60 %


Proceso de análisis: Generación de hipótesis y conclusiones
-----------------------------------------------------------

.. image:: img/conc2.png
    :align: center
    :scale: 75 %


Proceso de análisis: Conclusiones del proyecto
----------------------------------------------

- Según el índice calculado, la variabilidad del Mal de Río Cuarto virus,
  ha disminuido con el tiempo, habiendo una clara división del
  indicador en la campaña posterior a la epidemia de la campaña
  1996/97.
- La utilización de redes en el proceso de KDD resultó muy
  satisfactoria y logró resaltar un comportamiento del objeto de
  estudio que no había sido evidente hasta el momento.
- En un proceso centrado en la persona (human-centered), donde la
  creatividad y experiencia del analista juega un rol fundamental, la
  herramienta propuesta es capaz de ofrecer una perspectiva
  novedosa y complementaria con las demás técnicas del proceso de
  KDD

.. image:: img/sher.png
    :align: right
    :scale: 50 %

Data Warehouse - OLAP - BI
--------------------------

Concluimos que nuestro problema se adaptaba a algo muy similar a "algo" de BI

- En el contexto de la informática, un **almacén de datos**
  (del inglés data warehouse) es una colección de datos orientada a un
  determinado ámbito (empresa, organización, etc.), integrado, no volátil y
  variable en el tiempo, que ayuda a la toma de decisiones en la entidad en la
  que se utiliza.
- **OLAP** es el acrónimo en inglés de procesamiento analítico en línea
  (On-Line Analytical Processing). Es una solución utilizada en el campo de la
  llamada Inteligencia empresarial (o Business Intelligence)
  cuyo objetivo es agilizar la consulta de grandes cantidades de datos.
  Para ello utiliza estructuras multidimensionales (o **Cubos OLAP**) que contienen
  datos resumidos de grandes Bases de datos o Sistemas Transaccionales (OLTP).
  Se usa en informes de negocios de ventas, marketing, informes de dirección,
  minería de datos y áreas similares.
- Se denomina **inteligencia empresarial**, inteligencia de negocios o BI (del inglés
  business intelligence) al conjunto de estrategias y herramientas enfocadas a
  la administración y creación de conocimiento mediante el análisis de datos
  existentes en una organización o empresa.

.. image:: img/dwolapbi.png
    :align: center
    :scale: 150 %


Cubo OLAP
---------

Es una base de datos multidimensional, en la cual el almacenamiento físico de los
datos se realiza en un vector multidimensional. Los cubos OLAP se pueden
considerar como una ampliación de las dos dimensiones de una hoja de cálculo.

.. image:: img/cube.png
    :align: center
    :scale: 50 %

- Las olap pueden ser implementados en ROLAP - MOLAP - HOLAP
- Las consultas OLAP se llaman MDX (son bastante parecidas a SQL)
- Para consultas remotas se utiliza XMLA sobre SOAP

Soluciones OpenSource
---------------------

- **Mondrian** (todo en java soporta XML y MDX) (http://mondrian.pentaho.com/)
- **python xmla** (``pip install xmla``) para comunicarse con casi cualquier OLAP (https://pypi.python.org/pypi/xmla/)
- **Cubes** (``pip install cubes``) puro python pero muy verde (pythonhosted.org/cubes/)
- **Pentaho** (http://www.pentaho.com/),  **Saiku** (http://meteorite.bi/saiku),
  **OpenI** (http://openi.org/)

.. image:: img/floss.png
    :align: center
    :scale: 60 %


Yatel
-----

- http://bitbucket.org/yatel/yatel
- Wiskey-Ware License
- Es la implementación en gran parte del proceso mencionado anteriormente.
- En vez de Cubos usa **redes** olap.
- Falta trabajo (se aceptan colaboraciones)
- Posee un lenguaje intermedio denominado QBJ
- Puede usarse como librería o como DB remota (alpha)
- Posee soportes de ETL, estadísticas y DM rudimentaria.
- Su version 0.2 es pip-instalable (``pip install yatel``) necesitan tener
  previamente numpy y pyqt, usa una bd distinta, y es una aplicación desktop

.. image:: img/yatelred.png
    :align: right
    :scale: 80 %

Yatel - Red OLAP
----------------

.. image:: img/olapnw.png
    :align: center
    :scale: 100 %



Yatel - la app
--------------

En funcionamiento... (0.2 algo así va a ser Yatel BI)

.. image:: img/sshot.png
    :align: center
    :scale: 25 %


Yatel - Arquitectura
--------------------

.. image:: img/arquitectura.png
    :align: center
    :scale: 200 %




En que se puede aportar

- YQL sin implementar.
- Más minería de datos propiamente dicha (solo tiene kmeans)
- Agregar autenticación rudimentaria en yatel server y dar soporte a algo como... LDAP¿?¿?.
- Como es un proyecto homologado por una universidad puede extenderse como parte
  de un proyecto de fin de carrera.
- La parte científica per-se no esta desarrollada (algún doctorando en la sala?)
- Documentación (mucha)


¿Preguntas?
-----------

    - Charlas:
        - http://bitbucket.org/leliel12/talks
    - Contacto:
        - Juan B Cabral
            - Mail: `jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_
            - Twitter: `@JuanBCabral <http://twitter.com/JuanBCabral/>`_
            - Blog: http://jbcabral.com/

.. image:: img/questions.png
    :align: right
    :scale: 75 %



