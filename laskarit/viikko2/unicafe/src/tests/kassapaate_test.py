import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_kassapaate_toimii(self):
        self.assertNotEqual(self.kassapaate, None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)


        #kassassa rahaa 100000 senttiä
    def test_kateinen_kassa_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual((self.kassapaate.kassassa_rahaa),100240)
        self.assertEqual((self.kassapaate.edulliset), 1)

    def test_kateinen_kassa_ei_kasva_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual((self.kassapaate.kassassa_rahaa),100000)
        self.assertEqual((self.kassapaate.edulliset), 0)

    def test_kateinen_kassa_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual((self.kassapaate.kassassa_rahaa),100400)
        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_kateinen_kassa_ei_kasva_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual((self.kassapaate.kassassa_rahaa),100000)
        self.assertEqual((self.kassapaate.maukkaat), 0)
        

    def test_lounas_kateisella_onnistunut(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410),10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)
    
    def test_lounas_kateisella_ei_onnistu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(10),10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(50),50)
    
    
    def test_maksukortilla_edullinen_osto_toimii(self):        
        
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 7.60 euroa")
        self.assertTrue(bool(self.maksukortti))
        self.assertGreaterEqual((self.kassapaate.edulliset), 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksukortilla_maukas_osto_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 6.00 euroa")
        self.assertTrue(bool(self.maksukortti))
        self.assertGreaterEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maksukortti_ei_toimi(self):
        self.maksukortti1 = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1)
        self.assertEqual(str(self.maksukortti1), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(str(self.maksukortti1), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        


    def test_maksukortin_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,200)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 12.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_maksukortin_lataus_ei_toimi(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
