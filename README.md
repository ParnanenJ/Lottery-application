Tämä on repositorio Laurean "Ohjelmoinnin perusteet" -kurssin projektille.

<hr>

<h1>Lottery application / Lotto sovellus</h1>
Tekijä: Jiro Pärnänen

<hr>

<h3>Demo-linkki:</h3>
Pääset sivustolleni osoitteessa google.com

<hr>

<h3>Tietoa sovelluksesta</h3>
Lotto sovellus luo käyttäjälleen satunnaisia lottorivejä riippuen siitä mitä lottopeliä käyttäjä haluaa pelata.
Sovelluksella voi luoda lottorivejä kolmelle eri lottopelille: Lotto, Vikinglotto, Eurojackpot.
Käyttäjä pystyy luomaan kerralla 1-10 lottoriviä haluttuun peliin.

<hr>

<h3>Kuvakaappaukset</h3>

<h5>Lottopelien arpominen:</h5>

![image](https://github.com/user-attachments/assets/27bba650-2b53-4224-9a29-3077e95d7317) ![image](https://github.com/user-attachments/assets/96388a0b-cc35-432a-bcf6-0a1edffd673d) ![image](https://github.com/user-attachments/assets/8c900d6a-e0ae-4b86-8869-f21b653427d7)

<h5>Lottorivien tallentaminen:</h5>

![image](https://github.com/user-attachments/assets/14718218-4889-4d6c-8411-8710b5cfb27b) 

<h5>Tallennettujen rivien näyttäminen:</h5>

![image](https://github.com/user-attachments/assets/991b6995-4ad3-489d-9a94-7e4afb2633bd)

<h5>Lopetusvalikko:</h5>

![image](https://github.com/user-attachments/assets/5e204ce5-260a-44ee-a974-7cacb28574c0)

<hr>

<h3>Teknologiat</h3>

Ohjelma on toteutettu `pythonilla`. Ohjelmassa on myös käytetty pythonin sisään rakennettua `"Random" moduulia`, joka luo satunnais numeroita.

<hr>

<h3>Suunnittelu</h3>

1) Käyttäjältä kysytään, mitä lottopeliä hän haluaa pelata ja kuinka monta riviä hän haluaa (1-10).

2) Sovellus valitsee lottopeliä vastaavat:<br>
        - Lottonumeroiden määrän ja numeroalueen<br>
        - Lisänumeroiden määrän ja numeroalueen

3) Numeroiden määrä ja numeroalue syötetään yhteiselle arvontafunktiolle, joka:<br>
        - Arpoo numerot satunnaislukugeneraattoria hyödyntäen<br>
        - Varmistaa, että numerot toistuvat vain kerran samalla lottorivillä<br>
        - Palauttaa valmiin rivin numerolistana

4) Arvontafunktiota kutsutaan niin monta kertaa, kun rivejä halutaan.
     
5) Tulostetaan arvotut rivit näytölle.

6) Lopuksi käyttäjä pystyy valitsemaan haluaako hän tallentaa rivit vielä tiedostoon.

<p>Vuokaavio:</p>

![image](https://github.com/user-attachments/assets/3dc969f4-745f-4d04-9986-06d36c54ef24)

<hr>

<h3>Tila</h3>

Lotto sovelluksen `versio 1` on valmis.

<hr>

<h3>Lähteet</h3>
Sovelluksen tulostuksen asettelussa on hyödynnetty ChatGPT:tä

<hr>

<h3>Lisenssi</h3>
MIT-lisenssi © ParnanenJ
