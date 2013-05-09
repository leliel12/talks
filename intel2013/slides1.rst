mongokit-django
---------------

.. code-block:: python

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'example-sqlite3.db',
            },
            'mongodb': {
                'ENGINE': 'django_mongokit.mongodb',
                'NAME': 'example',
            },
        }


mongokit-django
---------------

.. code-block:: python

        from django_mongokit.document import DjangoDocument
        from django_mongokit import connection

        from django_mongokit import get_database
        database = get_database()

        class Talk(DjangoDocument):
            structure = {
           'topic': unicode,
           'date': datetime.datetime
        }

        connection.register([Talk])


mongokit-django
---------------

.. code-block:: python

    database = conn.mydb
    collection = database.mycollection
    instances = collection.Talk.find()

    instance = collection.Computer()
    ...
    instance.save()


Ejercicio
---------

Implementar el poll con mongokit-django
