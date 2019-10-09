# -*- coding: utf-8 -*-

from source.born_generator import BornGen
import unittest

class TesteGeraBorn(unittest.TestCase):
    def test_gera_born_dt(self):
        self.assertTrue(BornGen().dt_nasc != BornGen().dt_nasc)  # Gerar datas diferentes em execuções próximas (carece estresse de teste e sorte)

if __name__ == '__main__':
    unittest.main()
