import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    #alkutilanne
    def test_rahamaara_oikein_luomisen_jalkeen(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edulliset_lounaat_oikein_luomisen_jalkeen(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_lounaat_oikein_luomisen_jalkeen(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    #syo_edullisesti_kateisella
    def test_syo_edullisesti_kateisella_kassa_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_syo_edullisesti_kateisella_vaihtoraha_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
    
    def test_syo_edullisesti_kateisella_lisaa_myytyja_edullisia(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_kassa_toimii_jos_maksu_riittamaton(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_vaihtoraha_toimii_jos_maksu_riittamattoman(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
    
    def test_syo_edullisesti_kateisella_edulliset_ennallaan_jos_maksu_riittamaton(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #syo_maukkaasti_kateisella
    def test_syo_maukkaasti_kateisella_kassa_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_syo_maukkaasti_kateisella_vaihtoraha_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
    
    def test_syo_maukkaasti_kateisella_lisaa_myytyja_maukkaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisella_kassa_toimii_jos_maksu_riittamaton(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_vaihtoraha_toimii_jos_maksu_riittamattoman(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
    
    def test_syo_maukkaasti_kateisella_maukkaat_ennallaan_jos_maksu_riittamaton(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #syo_edullisesti_kortilla
    def test_syo_edullisesti_kortilla_veloittaa_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_syo_edullisesti_kortilla_lisaa_myytyja_edullisia(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_kortin_rahamaara_ennallaan_jos_rahamaara_riittamaton(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_syo_edullisesti_kortilla_edulliset_ennallaan_jos_rahamaara_riittamaton(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)        
    
    def test_syo_edullisesti_kortilla_ei_kasvata_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    #syo_maukkaasti_kortilla
    def test_syo_maukkaasti_kortilla_veloittaa_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_syo_maukkaasti_kortilla_lisaa_myytyja_maukkaita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_kortin_rahamaara_ennallaan_jos_rahamaara_riittamaton(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_syo_maukkaasti_kortilla_maukkaat_ennallaan_jos_rahamaara_riittamaton(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)        
    
    def test_syo_maukkaasti_kortilla_ei_kasvata_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    #lataa_rahaa_kortille
    def test_lataa_rahaa_kortille_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_lataa_rahaa_kortille_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_lataa_rahaa_kortille_ei_muuta_kortin_saldoa_negatiivisilla_arvoilla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataa_rahaa_kortille_ei_muuta_kassan_rahamaaraa_negatiivisilla_arvoilla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

