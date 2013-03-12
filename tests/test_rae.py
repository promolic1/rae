#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

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
        assert self.drae.search('sonido') == [
            {
                'etimologia': u' (Del lat. son\u012dtus, por analog\xeda pros\xf3dica con ruido, chirrido, rugido, etc.).',
                'id': '65959',
                'definiciones': [
                    u'  1. m. Sensaci\xf3n producida en el \xf3rgano del o\xeddo por el movimiento vibratorio de los cuerpos, transmitido por un medio el\xe1stico, como el aire.',  # nopep8
                    u'  2. m. Significaci\xf3n y valor literal que tienen en s\xed las palabras. Estar al sonido de las palabras.',  # nopep8
                    u'  3. m. Noticia, fama.',
                    u'  4. m. F\xeds. Vibraci\xf3n mec\xe1nica transmitida por un medio el\xe1stico.', u'  5. m. Fon. Realizaci\xf3n oral de un fonema, constituida por rasgos pertinentes y no pertinentes.',  # nopep8
                    u'\u25a1 V. ',
                    u'banda de sonido', 'barrera del sonido', 'cadena de sonido',
                    u'intensidad del sonido'], 'lema': 'sonido.'
            }
        ]

    @patch(URLOPEN)
    def test_palabra_sugerencias(self, urlopen_mock):
        urlopen_mock.return_value = open(os.path.join(HERE, 'html', 'drae_palabra_python.html')).read()
        assert self.drae.search('python') == {
            'aviso': u'La palabra python no est\xe1 registrada en el Diccionario. Las que se muestran a continuaci\xf3n tienen formas con una escritura cercana.',  # nopep8
            'sugerencias': [u'o\xedr.', u'pacho1, cha., pacho2, cha.', u'pach\xf3n, na.', u'pat\xe1n.', u'patao.', u'patear.', u'pateo.', u'pat\xedn1., pat\xedn2.', u'patio.', u'pato-., pato1., pato2.', u'pat\xf3n, na.', u'patr\xf3n, na., patrono, na.', u'payar.', u'pechar1., pechar2., pechar3.', u'pech\xedn.', 'pecho1., pecho2., pecho3.', 'peer.', 'petar1., petar2.', 'peto.', 'piar.', u'pich\xedn.', 'picho.', 'pichoa.', u'pich\xf3n.', 'pichona.', u'pion1, na o pi\xf3n1, na., pion2 o pi\xf3n2.', 'pitao.', 'pitar1., pitar2.', 'pitear.', 'pitio, tia.', 'pito1., pito2., pito3, ta.', u'pit\xf3n1., pit\xf3n2.', 'pleon.', 'pocho, cha.', 'pon.', 'potar1., potar2.', 'potear.', 'poto1., poto2.', 'potro.', 'poyar.', u'prion o pri\xf3n.', 'puar.', 'pucho.', 'putear.', 'puto, ta.', u'put\xf3n.', 'puyar.', 'ton.']  # nopep8
        }

    @patch(URLOPEN)
    def test_palabra_sugerencias_empty(self, urlopen_mock):
        urlopen_mock.return_value = open(os.path.join(HERE, 'html', 'drae_palabra_arco.html')).read()
        assert self.drae.search('arco') == {
            'aviso': u'',
            'sugerencias': [u'arcar.', u'arco.']  # nopep8
        }

    @patch(URLOPEN)
    def test_palabra_noexiste(self, urlopen_mock):
        urlopen_mock.return_value = open(os.path.join(HERE, 'html', 'drae_palabra_UnladenSwallow.html')).read()
        assert self.drae.search('UnladenSwallow') == {'aviso': u' La palabra UnladenSwallow no está en el Diccionario. '}
