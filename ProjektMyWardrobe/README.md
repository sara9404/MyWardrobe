# MyWardrobe Web servis

MyWardrobe Web servis omogućuje korisnicima organizaciju vlastite odjeće u ormaru kako bi se lakše održavao te pomoglo pri stiliziranju odjevnih kombinacija. Sustav korisniku omogućava dodavanje, uređivanje i brisanje odjevnih predmeta te prikazuje cijeli sadržaj ormara.

## Funkcionalnosti

- **Dodavanje odjevnog predmeta:** Korisnik može dodati novi odjevni predmet u svoj ormar. Potrebno je unijeti kategoriju, boju, veličinu, sezonu, brend i stil.
- **Uređivanje odjevnog predmeta:** Korisnik može uređivati postojeći odjevni predmet kako bi ispravio ili ažurirao informacije o njemu.
- **Brisanje odjevnog predmeta:** Korisnik može obrisati odjevni predmet iz svog ormara.
- **Prikaz popisa odjeće:** Korisnik može pregledati popis svih odjevnih predmeta u svom ormaru, uključujući detalje kao što su kategorija, boja, veličina, sezona, brend i stil.
- **Vizualizacija:** Korisnik može pregledati vizualnu prezentaciju svojih 
odjevnih predmeta (koliko kategorija odjeće posjeduje).

## Tehničke informacije

Projekt je izrađen koristeći Flask web framework za back-end, 
SQLAlchemy za upravljanje bazom podataka, HTML/CSS/Bootstrap za front-end 
dizajn, te SQLite za lokalnu bazu podataka. 

## Kako koristiti

1. Klonirajte repozitorij na lokalno računalo.
2. Instalirajte Docker Desktop na računalu te ga pokrenite (otvorite aplikaciju).
3. Navigirajte do korijenskog direktorija projekta (.venv).
4. Izgradite Docker image pomoću naredbe u terminalu: `docker build --tag projektmywardrobe:1.0 .`
5. Pokrenite Docker kontejner koristeći naredbu u terminalu: `docker run -d -p 5000:5000 projektmywardrobe:1.0 `
6. Posjetite http://localhost:5000 u web pregledniku.
