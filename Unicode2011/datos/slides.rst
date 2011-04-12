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



XML - INTRO
-----------

    - Formato de marcado.
    - Soportado en por defecto en la mayoria de los lenguajes.
    - MUY utilizado.
    - Pude validarse (felicidad para los fans de IS [puaj!])
    - Bien formado != validado.
    - APESTA!


XML - Ejemplo
-------------

    .. code-block:: xml

        <!-- Comentario -->
        <persona>
            <!-- Otro Comentario -->
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


XML - Parseando
---------------

    - 2 alternativas principales:
        - SAX
        - DOM
    - Para navegar entre los nodos:
        - Estandar DOM (W3C)
        - XPath

XML - Parseando - SAX - 1
-------------------------

    .. code-block:: python

        #python mentiroso
        class ParserSax(object):

            def start_element(self, name, atts):
                print "EMPIEZA: ", name, atts

            def end_element(self, name):
                print "TERMINA: ", name

            def char_data(self, texto):
                print "SE LEE: "


XML - Parseando - SAX - 2
-------------------------

    .. code-block:: python

        #python mentiroso
        parsear("archivo.xml", ParserSax)
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

XML - Parseando - DOM
---------------------

    - Transforma el xml en un conjunto de objetos "nodo".

    .. image:: img/dom.png
       :align: center
       :scale: 190 %


XML - Navegando - W3C DOM
-------------------------

    - Es lo mismo que usa javascript.
    - Vas pidiendo uno tras otro que cosas tiene adentro.

    .. code-block:: python

        dom = parsear("archivo.xml", DOM)
        persona = dom.getChildsNodes()
        autos = persona.getElementsByTagName("auto")
        for auto in autos:
            for color in auto.getElementByTagName("color")
                print color.getText() # uno tiraria una exception por null


XML - Lo Que Queda Afuera
-------------------------

    - XPath (es como navegar archivos pero mas complejo)
    - XSL - DTD bla bla bla


Interludio
----------

    Alguna mente brillante penso:

        "En ves de rompernos la cabeza con esa cosa complicada de xml, por que
        no hacemos algo que aprobeche lo que hay en comun en TODOS los
        lenguajes de programación?"

    Que tiene en comun un lenguaje de programacion?
        - Todos tienen tipos nativos (int, float, bool, string, etc)
        - Todos tienen algo iterable (listas, arrays, etc)
        - Todos tienen el valor nulo (null, None, nil, etc)
        - Todos tienen algo que relaciona una llave con un valor (hashes, dicts,
          etc)


JSON - INTRO
------------
    
    - Javascript Simple Object Notation
    - Define un gran hash y adentro listas, constantes otros hashes y wawawa.
    

JSON - Ejemplo
--------------

    .. code-block:: JSON

        # comentario
        {
            "persona": {
                # Otro Comentario
                "autos": [
                    {"tipo": "deportivo", "marca": "ferrari"},
                    {"tipo": "croto", "marca": "fiat", "color": "verde"}
                ],
                "basura": {"value: "solo un ejemplo"},
                "nombre": "Tito Puente",
                "direcciones": {"laboral": "Fake st 123", 
                                "personal": "Real st 456"}
                        }
        }


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


