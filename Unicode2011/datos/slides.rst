DATOS
-----

    .. image:: img/data_logo.png
       :align: center
       :scale: 100 %

    DATOS

    Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_>

    `UNICODE 2011 <http://uni-code-group.blogspot.com/>`_


Ecosistema
----------

    .. image:: img/ecosistema.png
       :align: center
       :scale: 100 %
       
    (PONER LOGUITOS DE PROGRAMA ENLAZADOS CON GODZILLA)
    
    - Muchos lenguajes de programación.

    - Interoperatibilidad.
    
    - Ejecucion de "cosas remotas".
    
    - Caos!
    
    
¿Que Es lo que se Trasmite?
---------------------------
    
    - DATOS!
        - Se almacenan.
        - Se trasmiten.
        
Moraleja
--------
        
    **Lo que importan son los datos**
    
    
ESTADO ACTUAL
-------------

    - Existen Standares para:
        - Transmitir: XML - JSON - YAML
        - Almacenar: RDBMS - OODB - NoSQL
        


TRASMISION - XML - INTRO
------------------------
    
    - Formato de marcado.
    - Soportado en por defecto en la mayoria de los lenguajes.
    - MUY utilizado.
    - Pude validarse (felicidad para los fans de IS [puaj!])
    - APESTA!


TRASNMISION - XML - EJ. 1
-------------------------

    .. code-block:: xml
    
        <persona>
            <auto tipo="deportivo">
                <marca>ferrari</marca>
            </auto>
            <auto tipo="croto">
                <marca>fiat</marca>
                <color>verde</color>
            </auto>
            <basura value="solo ejemplo"/>
            <nombre>Tito Puente</nombre>
            <direcciones>
                <direccion tipo="laboral">Fake st 123</direccion>
                <direccion tipo="personal">Real st 456</direccion>
            <direcciones>
        </persona>
                   
        
TRASNMISION - XML - PARSEANDO
-----------------------------
    
    - 2 alternativas principales:
        - SAX
        - DOM
    - Para navegar entre los nodos:
        - Estandar DOM (W3C)
        - XPath
        
TRASNMISION - XML - PARSEANDO - SAX - 1
---------------------------------------
    
    .. code-block:: python
        
        #python mentiroso
        class ParserSax(object):
            
            def start_element(self, name, atts):
                print "EMPIEZA: ", name, atts
                
            def end_element(self, name):
                print "TERMINA: ", name
                
            def char_data(self, texto):
                print "SE LEE: "
                
                
TRASNMISION - XML - PARSEANDO - SAX - 2
---------------------------------------

    .. code-block:: python
        
        #python mentiroso
        parsear(archivo.xml, ParserSax)
        # salida
        EMPIEZA: persona {}
        EMPIEZA: auto {"tipo": "deportivo"}
        EMPIEZA: marca {}
        SE LEE: ferrari
        TERMINA: marca
        TERMINA: auto
        EMPIEZA: auto {"tipo": "croto"}
        EMPIEZA: marca {}
        SE LEE:  fiat
        TERMINA: marca
        EMPIEZA: color {}
        SE LEE: verde
        TERMINA: color
        TERMINA: auto
        EMPIEZA: basura {"value": "solo ejemplo"}
        TERMINA: basura
        ...
        
TRASNMISION - XML - PARSEANDO - DOM 
-----------------------------------

    - Transforma el xml en un conjunto de objetos "nodo".
    
    .. image:: img/dom.png
       :align: center
       :scale: 100 %
        

¿Preguntas?
-----------

    - Proyectos:
        - http://bitbucket.org/leliel12/
    - Contacto:
        - Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_> 
          / `@leliel12 <http://twitter.com/leliel12/>`


.. footer:: 
    `UNICODE 2011 <http://uni-code-group.blogspot.com/>`_
    -
    Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_>

.. header::
    
    
