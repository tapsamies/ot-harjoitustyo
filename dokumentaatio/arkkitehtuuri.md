# Arkkitehtuuri

### Rakenne

 - Sovelluksen logiikka on eriytetty omiin tiedostoihin suurpiirteisesti
 - Tiedon pysyväistallennus on toteutettu neuroverkoilla (=Käyttäjän aivot)

### Käyttöliittymä

 Käyttöliittymässä on kolme erilaista näkymää:
 
 - Peliruutu, joka näkyy vakiona heti aluksi
 - Pause -valikko
 - Pelin loppuruutu

### Päätoiminnallisuus

 Pelissä on valtaosa tetriksen toiminnallisuudesta. Johtuen aikataulullisista haasteista, rivien tuhoaminen ei toimi niinkuin pitää eikä seuraavaa palikkaa näytetä käyttäjälle. Pelissä oli myös jossain vaiheessa toiminnallisuutta hiirelle mutta siitä koitui sen verran ongelmaa että päätin ottaa sen pois.
 
 - Pelin nopeus ei muutu missään vaiheessa, mutta peli osaa laskea pisteitä tyhjennettyjen rivien muodossa
 - Pelin voi laittaa pauselle
 - Pelin voi uudelleenkäynnistää

### Heikkoudet ja puutteet

 Pelin rakennetta ja toimintaa tuli hoidettua aika optimistisella aikataululla ja se kostautui lopullisen tuotteen laatuna. Esimerkiksi rivien tyhjennys oli mekaniikkana sellainen että se ei meinannut klikata ollenkaan ja sain raakileen siitä kuntoon noin 90minuuttia ennen Deadlineä. 
