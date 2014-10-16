.. =============================================================================
.. ICONS
.. =============================================================================




.. =============================================================================
.. CONTENT
.. =============================================================================

Fundamentos de Bussines Intelligence
------------------------------------

.. class:: center

    Ing. Cabral, Juan B.


.. image:: imgs/bi.png
    :align: center
    :scale: 60 %


.. class:: center

    Universidad Nacional del Sur

    SciPyCon Argentina 2014

    10/2014 - Bahía Blanca - Argentina


About Me
--------

Juan B Cabral

- Software engineer.
- Data scientist.

.. image:: imgs/eng.png
    :align: center
    :scale: 60 %


Agenda
------

::

    - Historia y descripción del BI
    - Bases de datos transaccionales (OLTP) vs Analíticas (OLAP)
    - Data Marts y Data Warehouse
    - Estructura de datos para análisis multidimensional (OLAP Cubes)
    - Implementaciones OLAP: ROLAP - MOLAP - HOLAP
    - Modelado relacional para RDBMS (ROLAP)
    - Diferentes alternativas de OLAP libres y gratuitas (Mondrian & Cubes)
    - Aplicaciones BI (Pentaho - Saiku - Cubes Viewer)
    - Consultas MDX (Multi Dimensional eXpressions)
    - ETL (Extract, Transform and Load)


.. image:: imgs/agenda.png
    :align: center
    :scale: 50 %


Demo Time
---------

.. image:: imgs/demotime.png
    :align: center
    :scale: 100 %

.. class:: center

    **Veamos a que apuntamos con este tutorial**


Historia y descripción del BI - Definición
------------------------------------------

El término inteligencias empresariales se refiere al uso de datos en una
**empresa** para facilitar la toma de decisiones. Abarca la comprensión del
funcionamiento actual de la **empresa**, bien como la anticipación de
acontecimientos futuros, con el objetivo de ofrecer conocimientos para
respaldar las decisiones **empresariales**. [WIKIPEDIA]_

En 1989, Howard Dresner (más tarde, un analista de Gartner Group) propuso la
"inteligencia de negocios" como un término general para describir
"los conceptos y métodos para mejorar la toma de decisiones **empresariales**
mediante el uso de sistemas basados en hechos de apoyo" [WIKIPEDIA]_

.. class:: center

    **Uno de los pocos casos que Nace en la industria migra a la Ciencia**


.. image:: imgs/bihist.png
    :align: center
    :scale: 30 %

Historia y descripción del BI - Características
-----------------------------------------------

- **Accesibilidad a la información.** El acceso a datos debe ser de forma
  independiente a su procedencia
- **Apoyo en la toma de decisiones.** La herramientas debe permitir la
  selección, análisis  y manipulación selectiva de datos
- **Orientación al usuario final.** Se busca independencia entre los
  conocimientos técnicos de los usuarios y su capacidad para utilizar estas
  herramientas.

.. image:: imgs/insta.png
    :align: center
    :scale: 40 %


OLTP & OLAP
-----------

.. class:: Center

    Existen diferentes formas de clasificar bases de datos


.. image:: imgs/dbtypes.png
    :align: center
    :scale: 50 %


- Segun la estructura que almacentan:
  **OO** (db4o), **Document-Oriented** (mongoDB, CouchDB), **RDBMS** (MySql,
  SQLite, PostgreSQL, Oracle, MicrosoftSQL Server, DB2), **Key-Value**
  (Redis, riak) o **Graph** (Neo4J)
- Segun si implementan o no SQL:
  **SQL** (MySql, SQLite, PostgreSQL, Oracle, MicrosoftSQL Server, DB2) o
  **NO-SQL** (Todas las demas)
- Segun su objetivo:
    **OLAP** (Mondrian, Cubes, Cognos) y **OLTP** (Todas las demas)




¿Preguntas?
-----------

    - Charla:
    - Contactos:
        - `jbcabral.com <http://jbcabral.com>`_
        - Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_>

.. image:: imgs/questions.png
    :align: right
    :scale: 35 %


.. [WIKIPEDIA] http://es.wikipedia.org/wiki/Inteligencia_empresarial


