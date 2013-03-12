
RAE
===

.. image:: https://travis-ci.org/marsam/rae.png?branch=master

.. important::

    Este paquete no posee ninguna afiliación con la RAE.

Una pequeña api para los diccionarios de la `Real Academia Española <http://rae.es/>`_

`Diccionario de la lengua española <http://lema.rae.es/drae/>`_:

.. code:: python

    >>> from rae import Drae
    >>> drae = Drae()
    >>> drae.search(u'calato')   # Es necesario ingresar unicode
    [{'definiciones': [u'  1. adj. Bol. y Per\xfa. Desnudo, en cueros.'],
      'etimologia': '',
      'id': '13245',
      'lema': 'calato, ta.'}]

`Diccionario panhispánico de dudas <http://lema.rae.es/dpd/>`_. Soporte parcial, devuelve la deficion en el lema.

.. code:: python

    >>> from rae import Dpd
    >>> dpd = Dpd()
    >>> dpd.search(u'lapsus cálami')
    [{'definiciones': [],
      'etimologia': None,
      'id': None,
      'lema': u'lapsus c\xe1lami. Loc. lat. que significa literalmente \u2018error de la pluma\u2019. Se emplea como locuci\xf3n nominal masculina con el sentido de \u2018error involuntario que se comete al escribir\u2019: \xabLa explicaci\xf3n de esta frase como errata de imprenta o lapsus c\xe1lami debe rechazarse\xbb (Madariaga Col\xf3n [Esp. 1940-47]). Es invariable en plural (\u2192 plural, 1k): los lapsus c\xe1lami.'}]

Enlaces
-------

* `Qué es el Diccionario panhispánico de dudas <http://lema.rae.es/dpd/html/quees.htm>`_
* http://lema.rae.es/drae/html/advertencia.html
