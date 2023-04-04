# Vaatimusmäärittely

### Sovelluksen tarkoitus
Sovelluksena on tetris -pelin klooni. Kuten tetriksessäkin on pelissä ideana sijoittaa vaihtuvalla muodolla ruudulle ilmestyvät palikat siten että ruudulle jo asettuneet palikat muodostavat kokonaisia vaakasuuntaisia rivejä. 

### Käyttäjät
 - Pelissä ainoa käyttäjä on pelaaja itse, joten käyttäjärooleja ei sen ulkopuolella ole.

### Suunniteltu toiminnallisuus

 - Jos vaakasuuntainen rivi saadaan täytettyä, katoaa rivi näkyvistä ja pelaaja saa pisteitä
	- Peli nopeutuu suhteessa pisteiden kasvuun
 - Peli loppuu kun vaakarivien maksimikorkeus ylittää pelaajalle näkyvän ruudukon
	- Maksimipisteet tallennetaan jos saadaan uusi ennätys
 - Pelissä on kaikki tetriksen vakiomuotoiset palikat
	- Jonkinlainen satunnaisgeneraattori palikoiden tekemistä varten
