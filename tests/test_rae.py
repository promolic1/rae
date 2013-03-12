#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa

import os
import sys
import json

try:
    from unittest.mock import patch  # python >= 3.3
except ImportError:
    from mock import patch   # noqa

import rae


if sys.version_info[0] == 2:
    URLOPEN = 'urllib.urlopen'
else:
    URLOPEN = 'urllib.request.urlopen'

HERE = os.path.abspath(os.path.dirname(__file__))


class TestDrae:
    def setup_method(self, method):
        self.drae = rae.Drae()

    def test_search(self):
        assert self.drae.search() == {'errors': 'You need a to specify a word.'}

    @patch(URLOPEN)
    def test_palabra_sonido(self, urlopen_mock):
        urlopen_mock.return_value = open(os.path.join(HERE, 'html', 'drae_palabra_sonido.html')).read()
        assert self.drae.search('sonido') == json.loads("""
        [
          {
            "etimologia": " (Del lat. son\u012dtus, por analog\u00eda pros\u00f3dica con ruido, chirrido, rugido, etc.).",
            "id": "65959",
            "definiciones": [
              "  1. m. Sensaci\u00f3n producida en el \u00f3rgano del o\u00eddo por el movimiento vibratorio de los cuerpos, transmitido por un medio el\u00e1stico, como el aire.",
              "  2. m. Significaci\u00f3n y valor literal que tienen en s\u00ed las palabras. Estar al sonido de las palabras.",
              "  3. m. Noticia, fama.",
              "  4. m. F\u00eds. Vibraci\u00f3n mec\u00e1nica transmitida por un medio el\u00e1stico.",
              "  5. m. Fon. Realizaci\u00f3n oral de un fonema, constituida por rasgos pertinentes y no pertinentes.",
              "\u25a1 V. ",
              "banda de sonido",
              "barrera del sonido",
              "cadena de sonido",
              "intensidad del sonido"
            ],
            "lema": "sonido."
          }
        ]
        """)

    @patch(URLOPEN)
    def test_palabra_sugerencias(self, urlopen_mock):
        urlopen_mock.return_value = open(os.path.join(HERE, 'html', 'drae_palabra_python.html')).read()
        assert self.drae.search('python') == json.loads("""
        {
          "aviso": "La palabra python no est\\u00e1 registrada en el Diccionario. Las que se muestran a continuaci\\u00f3n tienen formas con una escritura cercana.",
          "sugerencias": ["o\\u00edr.", "pacho1, cha., pacho2, cha.", "pach\\u00f3n, na.", "pat\\u00e1n.", "patao.", "patear.", "pateo.", "pat\\u00edn1., pat\\u00edn2.", "patio.", "pato-., pato1., pato2.", "pat\\u00f3n, na.", "patr\\u00f3n, na., patrono, na.", "payar.", "pechar1., pechar2., pechar3.", "pech\\u00edn.", "pecho1., pecho2., pecho3.", "peer.", "petar1., petar2.", "peto.", "piar.", "pich\\u00edn.", "picho.", "pichoa.", "pich\\u00f3n.", "pichona.", "pion1, na o pi\\u00f3n1, na., pion2 o pi\\u00f3n2.", "pitao.", "pitar1., pitar2.", "pitear.", "pitio, tia.", "pito1., pito2., pito3, ta.", "pit\\u00f3n1., pit\\u00f3n2.", "pleon.", "pocho, cha.", "pon.", "potar1., potar2.", "potear.", "poto1., poto2.", "potro.", "poyar.", "prion o pri\\u00f3n.", "puar.", "pucho.", "putear.", "puto, ta.", "put\\u00f3n.", "puyar.", "ton."]
        }
        """)

    @patch(URLOPEN)
    def test_palabra_sugerencias_empty(self, urlopen_mock):
        urlopen_mock.return_value = open(os.path.join(HERE, 'html', 'drae_palabra_arco.html')).read()
        assert self.drae.search('arco') == json.loads('{"aviso": "", "sugerencias": ["arcar.", "arco."]}')

    @patch(URLOPEN)
    def test_palabra_noexiste(self, urlopen_mock):
        urlopen_mock.return_value = open(os.path.join(HERE, 'html', 'drae_palabra_UnladenSwallow.html')).read()
        assert self.drae.search('UnladenSwallow') == json.loads('{"aviso": " La palabra UnladenSwallow no est\\u00e1 en el Diccionario. "}')
