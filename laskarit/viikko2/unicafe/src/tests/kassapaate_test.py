import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassa_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    def test_kateisosto_toimii_maksu_riittaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)
        
    
    def test_kateisosto_toimii_maksu_riittaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410),10)

    def test_kateisosto_ei_toimii_maksu_puuttuu_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)

    def test_kateisosto_ei_toimii_maksu_puuttuu_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200),200)

    def test_maksukortilla_osto_toimii_edullinen(self):
        self.kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kortti.saldo ,1000-240)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti),True)
    
    def test_maksukortilla_osto_toimii_maukas(self):
        self.kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kortti.saldo ,1000-400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti),True)
    
    def test_maksukortilla_osto_ei_toimi_edullinen(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kortti.saldo ,100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti),False)
    
    def test_maksukortilla_osto_ei_toimi_maukas(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kortti.saldo ,100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti),False)

    def test_kortin_lataus_toimii(self):
        self.kortti=Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(self.kortti,1000)
        self.assertEqual(self.kortti.saldo,1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+1000)
    
    def test_kortin_lataus_ei_toimi(self):
        self.kortti=Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(self.kortti,-1000)
        self.assertEqual(self.kortti.saldo,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    