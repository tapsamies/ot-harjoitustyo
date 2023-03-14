import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")
    
    def test_saldon_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 11.00 euroa")
    
    def test_saldon_pienenee_oikein_rahaa_on(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 9.00 euroa")
    
    def test_saldon_pienenee_oikein_rahaa_ei_ole(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")
    
    def test_palauttaa_oikein_rahaa_on(self):
        self.assertTrue(self.maksukortti.ota_rahaa(100))            
    
    def test_palauttaa_oikein_rahaa_ei(self):
        self.assertFalse(self.maksukortti.ota_rahaa(10000))        