import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_virheelliset_syotteet(self):
        varasto = Varasto(-5,-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)
        self.assertAlmostEqual(varasto.saldo, 0)
    
    def test_saldo_isompi_kuin_tilavuus(self):
        varasto = Varasto(3,6)
        self.assertAlmostEqual(varasto.paljonko_mahtuu(), 0)
    
    def test_lisaa_miinus_saldo(self):
        self.varasto.lisaa_varastoon(-4)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_lisaa_ekstra_saldo(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_miinus_saldo(self):
        self.varasto.ota_varastosta(-4)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_ota_ekstra_saldo(self):
        self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_str_funktio(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")
