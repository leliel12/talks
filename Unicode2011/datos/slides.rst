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
    - Soportado en por defecto en la mayoría de los lenguajes.
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
        - Estándar DOM (W3C)
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

    Alguna mente brillante pensó:

        "En ves de rompernos la cabeza con esa cosa complicada de xml, por que
        no hacemos algo que aproveche lo que hay en común en TODOS los
        lenguajes de programación?"

    Que tiene en común un lenguaje de programacion?
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
        {persona: {autos: [{marca: ferrari, tipo: deportivo}, 
        {color: verde, marca: fiat, tipo: croto}],
        basura: {value: solo un ejemplo}, direcciones: 
        {laboral: Fake st 123, personal: Real st 456}, nombre: Tito Puente}}

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


db40 - Intro
------------

    - Data Base 4 (for) Objects.
    - Para Java Platform y .Net
    - Persiste objetos PELADOS sin necesidad  de algun formateo especial.

    .. image:: img/db4o--png.png
       :align: center
       :scale: 300 %


db4o - UML
----------

    .. image:: img/db4ouml.jpg
       :align: center
       :scale: 300 %


db4o - Ejemplito
----------------

    .. code-block:: java

        // todas las operaciones se hacen sobre un object container
        ObjectContainer oc = Db4o.openFile(<PATH A UN ARCHIVO>);
        Auto fiat = new Auto("Fiat", 123);
        Persona tito = new Persona("tito", "peru 123 pb",  fiat);
        oc.store(fiat); // Persistimos el auto (ojo con el orden)
        oc.store(tito); // Persistimos la persona


db4o - Queries
--------------

    Db4o nos brinda 3 mecanismos para acceder a los datos almacenados:

        - QbE - Query By Example.
        - SODA - Simple Object Data Acces (no se explica)
        - NQ - Native Queries.

    En todos los casos db4o siempre nos devuelve una instancia de "ObjectSet"
    iterable y genérico al objeto buscado.

db4o - QbE
----------

    Es el mecanismo mas sencillo, consiste en crear una instancia con los
    datos que uno quiere buscar y dejando sus valores por defecto en los que
    no les interesa el valor que contenga.

    .. code-block:: java

        Persona filtro = new Persona(null, null,  fiat); //las personas que poseean
                                                        // esa instancia de auto.
        filtro = new Persona("tito", null,  null); // las personas que se llamen "tito"
        ObjectSet<Persona> os = oc.queryByExample(filtro); //realizamos la query
        while(os.hasNext()){ // mientras hayan resultados
            Persona p = os.next(); // extraemos la siguiente persona
            System.out.println(p); // imprimimos la persona por parametro
        }


db4o - QbE Problemas
--------------------

    Problemas
        - No se podrían hacer búsquedas del tipo "todos los nombres que empiezan
          por "ti";
        - No podemos buscar ocurrencias de valores por defecto, como por
          ejemplo todas las personas que no posean autos sin importar su nombre
          y su dirección; ya que la siguiente consulta traería todas las
          personas con y sin auto.

    .. code-block:: java

        filtro = new Persona(null, null,  null); // null es valor por defecto


db4o - Native Queries
---------------------

    - Es el "estándar" de búsquedas en bases de datos orientadas a objetos.
    - Se prefiere sobre Soda y QbE.
    - Existen papers proponiéndolos.
    - Consiste en crear un nuevo objeto en el lenguaje nativo de la aplicación que represente la búsqueda.
    - En el caso de java implica un objeto que extienda de la clase abstracta
      "Predicate" y redefina su unico método "match(obj)"
    - db4o compara todos los objetos de un tipo dado con  "match(obj)" y si
      este devuelve "true" se incluirá el objeto en el resultado.


db4o - Native Queries
---------------------

    .. code-block:: java

        ObjectSet<Persona> os = oc.query(
            new Predicate<Persona>(){

                @Override
                public boolean match(Persona p) {
                    return p.getName.startsWith("ti");
                }
        }); // cierro implementacion y query


db4o - Updates & Delete
-----------------------

    .. code-block:: java
        ObjectSet<Persona> os = oc.query(
            new Predicate<Persona>(){

            @Override
            public boolean match(Persona p) {
                return p.getName.startsWith("ti");
            }
        });
        Persona primero = os.get(0); // obtenemos la primer persona del resultado
        primero.setName("toto"); // cambiamos el nombre
        oc.store(primero); // actualizamos
        oc.delete(primero) // borramos


db4o - Transacciones
--------------------

    El "ObjectContainer" posee dos comandos:
        - comit()
        - rollback()
    Mas info detallada en mi blog :D


Sqlite - Intro
--------------

    - SQLite es un sistema de gestión de bases de datos relacional compatible 
      con ACID, contenida en una relativamente pequeña (~275 kiB)2 biblioteca
      en C.
    - Es un proyecto de dominio público1 creado por D. Richard Hipp.
    - Esta Embebida hasta en tu teléfono.
    - No es cliente-servidor, el motor de SQLite no es un proceso independiente.
    - La biblioteca SQLite se enlaza con el programa pasando a ser parte integral del mismo. 
    - Soporta Terabytes de tamaño, y también permite la inclusión de campos tipo BLOB.

    
Sqlite - Intro
--------------

    - No asigna un tipo de datos a una columna (una columna int no tiene necesariamente enteros
      los tipos se asignan a los valores individuales. 
    - Por ejemplo, se puede insertar un string en una columna de tipo entero 
      (a pesar de que SQLite tratará en primera instancia de convertir la cadena
      en un entero).
    - Ojo con la concurrencia.
    - Ojo con con la integridad referencial.
    - DB en memoria (rulez) :memory:


Sqlite - Ejemplo
----------------

    .. code-block:: java
    
        public class Main {

            public static void main(String[] args) {
                try {
                    Class.forName("org.sqlite.JDBC");
                    // "jdbc:sqlite::memory:"
                    Connection conn = DriverManager.getConnection("jdbc:sqlite:C:\\sqlite\\libreria.sqlite"); 
                    
                    Statement stat = conn.createStatement(); 
                    stat.execute("DELETE FROM autores");
                    
                    PreparedStatement prep = conn.prepareStatement("INSERT INTO autores (id_autor,nombre) VALUES (?, ?);");
                    prep.setInt(1,1);
                    prep.setString(2,"Deitel");
                    prep.addBatch();
                    prep.setInt(1,2);
                    prep.setString(2,"Ceballos");
                    prep.addBatch();
                    prep.setInt(1,3);
                    prep.setString(2,"Joyanes Aguilar");
                    prep.addBatch();
                    
                    conn.setAutoCommit(false);
                    prep.executeBatch();
                    conn.setAutoCommit(true);

                    ResultSet rs = stat.executeQuery("select * from autores;");
                    while (rs.next()) {
                        rs.getString("id_autor");
                        rs.getString("nombre");
                    }
                    rs.close();
                    stat.close();
                    conn.close(); 
                } catch (SQLException ex) {
                    System.out.println(ex.getMessage());
                } catch (ClassNotFoundException ex) {
                    System.out.println(ex.getMessage());
                }
              
            }
        }


RDBMS - Union de Tablas con OO
------------------------------

    - Opcion 1 a mano
    - Opcion 2 ORM
    
    .. image:: img/orm.jpg
       :align: center
       :scale: 300 %


Mongo DB - Intro
----------------

    - Orientada a documentos
    - Guarda objetos json-like NO ESTRUCTURADOS
    - Es muy, muy, muy, muy, muy...
    

Mongo DB - Intro
----------------

... muy, muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, muy,
muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, 
muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, 
muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy, muy,muy, muy,
muy...


Mongo DB - Intro
----------------

    - ... muy performante. (Oracle se rompe en pedazos y mongo sigue andando)
    - Quien la usa:
        - Foursquare
        - LHC
        - Bovespa (merval brazuca)
    - Soporta queries en javascript.


Mongo DB  - Algunos Ejemplitos
------------------------------

    .. code-block:: javascript
        
        db.food.insert({"fruit" : ["peach", "plum", "pear"]})
        db.food.find({"fruit" : "pear"})


¿Preguntas?
-----------

    - Proyectos:
        - http://bitbucket.org/leliel12/
    - Contacto:
        - Juan B Cabral 
            - Mail: `jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_
            - Twitter: `@juanBcabral <http://twitter.com/juanbcabral/>`_
            - Blog: http://jbcabral.wordpress.com/
    - Las charlas estan aca:
            - https://bitbucket.org/leliel12/talks


.. footer::
    `UNICODE 2011 <http://uni-code-group.blogspot.com/>`_
    -
    Juan B Cabral <`jbc.develop@gmail.com <mailto:jbc.develop@gmail.com>`_>

.. header::


