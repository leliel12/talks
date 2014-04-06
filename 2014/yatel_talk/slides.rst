.. =============================================================================
.. ICONS
.. =============================================================================

.. |utnico| image:: img/utnico.png
.. |intaico| image:: img/intaico.png
.. |conicetico| image:: img/conicetico.png


.. =============================================================================
.. CONTENT
.. =============================================================================

Análisis de datos a través de grafos
------------------------------------

.. class:: center

    Ing. Garcia, M. Alejandro - Ing. Cabral, Juan B.

    08/04/2014 - Córdoba


.. image:: img/log.png
    :align: center
    :scale: 24 %


.. class:: center

    Universidad Tecnológica Nacional - Facultad Regional Córdoba


Integrantes
-----------

- |utnico|  - García, Mario Alejandro
- |utnico|  - Cabral, Juan Bautista
- |utnico|  - Liberal, Rodrigo
- |utnico|  - Ramirez, Emilio
- |utnico|  - Arnaud, Máximo "El Topo"

- |intaico|  - Gimenez Pecci, María de la Paz
- |conicetico| |intaico|  - Laguna, Irma Graciela
- |intaico|  - Raspanti Monteoliva, Jorge G
- |intaico|  - Maurino, Fernanda

.. image:: img/lotr.png
    :align: right
    :scale: 55 %


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
    :align: right
    :scale: 30 %


Agenda
------

- Un poco de historia y motivaciones.
- Un poco de KDD.
- Un poco de Network Science.
- Proceso de Analisis.
- DW - OLAP - BI.
- El proyecto en sí
- Mini Demo

.. image:: img/to_do_list.jpg
    :align: right
    :scale: 30 %


Historia: Mal de Río Cuarto virus
---------------------------------

- Base de datos formada por

    - Perfiles electroforéticos.
    - Atributos que definen el ambiente de la planta

        .. image:: img/electroforesis.png
            :align: center
            :scale: 20 %

- Variabilidad (redes vs árboles).

.. image:: img/r4to.png
    :align: center
    :scale: 50 %


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

.. figure:: img/vuelos.png
    :align: center
    :scale: 200 %

    Topologías en redes de comunicación


Networks 1
----------

.. figure:: img/proteina.png
    :align: center
    :scale: 25 %

    Interacción proteína-proteína


Networks 2
----------

.. figure:: img/money.png
    :align: center
    :scale: 60 %

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

    Red semántica TBBT (Season 3)


Proceso de análisis
-------------------

Los ejemplos van con nuestra investigación (osea: resumen del paper)

.. image:: img/kdd0.png
    :align: center
    :scale: 50 %


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


Proceso de análisis: Visualización y análisis topológico
--------------------------------------------------------

.. image:: img/est.png
    :align: center
    :scale: 60 %


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
    :align: center
    :scale: 20 %

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

.. image:: img/dwolapbi.png
    :align: center
    :scale: 30 %

- Se denomina **inteligencia empresarial**, inteligencia de negocios o BI (del inglés
  business intelligence) al conjunto de estrategias y herramientas enfocadas a
  la administración y creación de conocimiento mediante el análisis de datos
  existentes en una organización o empresa.


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


Y donde estamos con nuestro problema
------------------------------------

- Los Sql eran muy engorrosos (http://wiki.getyatel.org/analysis/exp2014/)
- Para Cubos y BI en general, la solución no era natural.
- Las bases de datos de redes no son tan difundidas como las RDBMS.
- Solución Nuevo Paradigma: **NW-OLAP**


.. image:: img/where-are-we.png
    :align: center
    :scale: 60 %


Yatel - Red OLAP
----------------

.. image:: img/olapnw.png
    :align: center
    :scale: 100 %


Yatel
-----

.. image:: img/yatelred.png
    :align: center
    :scale: 50 %

- http://getyatel.org
- Es una implementación de referencia de NW-OLAP
- Wiskey-Ware License
- Es la implementación en gran parte del proceso mencionado anteriormente.
- Falta trabajo (se aceptan colaboraciones)
- Posee un lenguaje intermedio denominado QBJ
- Puede usarse como librería o como DB remota (alpha)
- Posee soportes de ETL, estadísticas y DM rudimentaria.


Yatel - Arquitectura
--------------------

.. image:: img/arquitectura.png
    :align: center
    :scale: 200 %


En que se puede aportar

- YatelQL sin implementar.
- Más minería de datos propiamente dicha (solo tiene kmeans)
- Agregar autenticación rudimentaria en yatel server y dar soporte a algo como... LDAP¿?¿?.
- Como es un proyecto homologado por una universidad puede extenderse como parte
  de un proyecto de fin de carrera.
- La parte científica per-se no esta desarrollada (algún doctorando en la sala?)
- Documentación (mucha)


Yatel Kaani - (Not even started)
--------------------------------

- En funcionamiento... (0.2 algo así va a ser Yatel BI)
- http://kaani.getyatel.org/

.. image:: img/sshot.png
    :align: center
    :scale: 25 %


Yatel Teper - (Not even started)
--------------------------------

- Va a ser el entorno visual de ETL
- Va a permitir ordenar fuentes para alimentar DW NW-OLAP

.. image:: img/etl.png
    :align: center
    :scale: 30 %


¿Preguntas?
-----------

    - Charla: http://goo.gl/65e3vc
    - Contactos:
        - http://forum.getyatel.org
        - Alejandro Garcia <`malegrandogarcia@hotmail.com <mailto:malegrandogarcia@hotmail.com>`_>
        - Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_>

.. image:: img/questions.png
    :align: right
    :scale: 25 %



