DATOS
-----

    .. image:: img/disketes.jpg
       :align: center
       :scale: 150 %

    DATOS

    Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_>

    `UNICODE 2011 <http://uni-code-group.blogspot.com/>`_


Ecosistema
----------

    .. image:: img/caos.jpg
       :align: center
       :scale: 50 %


¿Que Es lo que se Trasmite?
---------------------------

    - DATOS!
        - Se almacenan.
        - Se trasmiten.

Moraleja
--------

    **Lo que importan son los datos**

    .. image:: img/disketes.jpg
       :align: center
       :scale: 150 %

ESTADO ACTUAL
-------------

    - Existen Standares para:
        - Transmitir: XML - JSON - YAML
        - Almacenar: RDBMS - OODB - NoSQL



XML - INTRO
-----------

    .. image:: img/xml.png
       :align: center
       :scale: 150 %

    - Formato de marcado.
    - Soportado en por defecto en la mayoria de los lenguajes.
    - MUY utilizado.
    - Pude validarse (felicidad para los fans de IS [puaj!])
    - Bien formado != validado.
    - **APESTA!**


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


XML - Leyendo - W3C DOM
-----------------------

    - Es lo mismo que usa javascript.
    - Vas pidiendo uno tras otro que cosas tiene adentro.

    .. code-block:: python

        dom = parsear("archivo.xml", DOM)
        persona = dom.getChildsNodes()
        autos = persona.getElementsByTagName("auto")
        for auto in autos:
            for color in auto.getElementByTagName("color")
                print color.getText() # uno tiraria una exception por null


XML - Escribiendo - W3C DOM
---------------------------

    - Es lo mismo que usa javascript.
    - Vas Armando la estructura uno tras otro que cosas tiene adentro.

    .. code-block:: python

        doc = Documento()
        persona = Elemento("Elemento")
        persona.set_attribute("nombre", "tito")
        auto = Element("auto")
        persona.insert_child_node(auto)
        documento.insert_child_node(persona)
        ...


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

    .. image:: img/json.gif
       :align: center
       :scale: 150 %

    - Javascript Simple Object Notation
    - Define un gran hash y adentro listas, constantes otros hashes y wawawa.


JSON - Ejemplo
--------------

    .. code-block:: json

        {
            "persona": {
                "autos": [
                    {"tipo": "deportivo", "marca": "ferrari"},
                    {"tipo": "croto", "marca": "fiat", "color": "verde"}
                ],
                "basura": {"value": "solo un ejemplo"},
                "nombre": "Tito Puente",
                "direcciones": {"laboral": "Fake st 123",
                                "personal": "Real st 456"}
                        }
        }


JSON - Leyendo
--------------

    - Crea objetos "nativos" en el lenguaje destino.

    .. code-block:: python
        # esto si es python enserio

        import json

        objs = json.load("file.json")
        persona = obj["persona"]
        persona["autos"][0]["marca"]  # ferrari


YAML - Intro
------------

    - Yaml Ain't Markup Language.
    - Super conjunto de JSON.
    - Tiene dos formatos de escritura, el compacto y el indentado.
    - Caracteristica secreta!!!
    - Ruby lo prefiere  por sobre xml.
    - Mi formato preferido.

    .. image:: img/yaml.png
       :align: center
       :scale: 150 %

YAML - Ejemplo
--------------

    .. code-block:: yaml

        # formato compacto
        {persona: {autos: [{marca: ferrari, tipo: deportivo}, {color: verde, marca: fiat,
        tipo: croto}], basura: {value: solo un ejemplo}, direcciones: {laboral: Fake
        st 123, personal: Real st 456}, nombre: Tito Puente}}


    .. code-block:: yaml

        # formato compacto
        persona:
          autos:
          - marca: ferrari
            tipo: deportivo
          - color: verde
            marca: fiat
            tipo: croto
          basura:
            value: solo un ejemplo
          direcciones:
            laboral: Fake st 123
            personal: Real st 456
          nombre: Tito Puente


YAML - Leyendo
--------------

    Crea objetos "nativos" en el lenguaje destino.

    .. code-block:: python
        # esto si es python enserio

        import yaml # libreria externa

        objs = yaml.load("file.yaml")
        persona = obj["persona"]
        persona["autos"][0]["marca"]  # ferrari


YAML - Secreto
--------------

    CARACTERISTICA MAS PULENTA QUE LA VIDA MISMA!!!!



¿Preguntas?
-----------

    - Proyectos:
        - http://bitbucket.org/leliel12/
    - Contacto:
        - Juan B Cabral
            - Mail: `jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_
            - Twitter: `@leliel12 <http://twitter.com/leliel12/>`


.. footer::
    `UNICODE 2011 <http://uni-code-group.blogspot.com/>`_
    -
    Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_>

.. header::


