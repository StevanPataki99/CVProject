import flask
from flask.blueprints import Blueprint

from utils.db import mysql

korisnik_blueprint = Blueprint("korisnik_blueprint", __name__)

@korisnik_blueprint.route("/korisnik", methods=["GET"])
def dobavi_korisnike():
    cursor = mysql.get_db().cursor() # Dobavljanje instance kursora.
    cursor.execute("SELECT * FROM korisnik") # Izvrsavanje upita za dobavljanje svih proizvoda
                                                                # cija kolicina je veca od 0. Ovime je posao filtriranja
                                                                # proizvoda po kolicini izmesten iz generisanja sablona
                                                                # na server baze podataka koji je optimivan za ovakve
                                                                # zadatke.
    korisnik = cursor.fetchall() # Dobavljanje svih rezultat prethodni izvrsenog upita.
    return flask.jsonify(korisnik) # Vracanje proizvoda u JSON formatu.
                                    # Funkcija jsonify pretvara prosledjeni objekat u JSON format
                                    # i pakuje ga u response objekat u kojem su podesena sva
                                    # neophodna zaglavlja. Upotreba dumps funkcije iz
                                    # JSON modula vratila bi JSON ali ne bi napravila i response
                                    # objekat, koji bi se morao napraviti naknadno rucno.

@korisnik_blueprint.route("/korisnik/<int:id_korisnika>", methods=["GET"])
def dobavi_korisnika(id_korisnika):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM korisnik WHERE id=%s", (id_korisnika,))
    korisnik = cursor.fetchone() # Kako je rezultat upita samo jedna torka dovoljno je
                                 # pozvati metodu fetchone() nad kursorom koja vraca
                                 # sledecu torku koja zadovoljava upit.
    if korisnik is not None:
        return flask.jsonify(korisnik) # Ukoliko je pronadje, proizvod se prosledjuje klijentu.
    else:
        return "", 404 # Ukoliko proizvod nije pronadjen klijent ce dobiti status odgovora 404.
                       # Odnosno podatak da trazeni resurs nije pronadjen.

@korisnik_blueprint.route("/korisnik", methods=["POST"])
def dodaj_korisnika():
    print("DJAVO JE NOCAS OPET U GRADU")
    # Provera da li je korisnik prijavljen.
    db = mysql.get_db() # Dobavljanje instance konekcije ka bazi.
    cursor = db.cursor() # Dobavljanje kursora.

    # Izvrsava se parametrizovani upit sa imenovanim parametrima. Ukoliko se koriste imenovani parametri
    # umesto torkse sa podacima moguce je proslediti recnik koji u se bi sadrzi kljuceve koji odgovaraju
    # imenima parametara. Vrednosti na datim kljucevima ce automatski biti preuzete u istoimenim parametrima.
    # Kako se sadrzaj forme u Flasku predstavlja kao imutabilni recnik koji nasledjuje recnik moguce je umesto
    # obicnog recnika proslediti sam sadrzaj forme. Takodje konverzija podatak nije neophodna jer ce se ispravna
    # konverzija izvrsiti na serveru za upravljanje bazama podataka.
    # Dodatna napomena: Iako je id kolona koja postoji u tabeli proizvod, ona nije navedena prilikom dodavanja
    # jer je ova kolona podesena da bude auto increment, odnosno da se njena vrednost moze automatski generisati.
    # Ovo generisanje ce se desiti samo ukoliko se prilikom izvrsavanja insert naredbe izostavi podesavanje vrednosti
    # za kolonu koja je auto increment ili ako se za njenu vrednost postavi NULL vrednost.
    print(flask.request.json)
    cursor.execute("INSERT INTO korisnik(korisnicko_ime, ime, prezime) VALUES(%(korisnicko_ime)s, %(ime)s, %(prezime)s)", flask.request.json)
    # Request objekat u flasku sadrzi atribut json, ovaj atribut sadrzace recnik koji je nastao
    # parsiranjem tela zahteva. Telo ce biti parsirano ukoliko je content type bio application/json
    # a recnik ce biti formiran samo ukoliko se u telu nalazio ispravan JSON dokument.
    db.commit() # Upiti se izvrsavaju u transakcijama. Uskladistavanje rezultata transakcije je neophodno rucno potvrditi.
                # Za to se koristi commit() metoda nad konekcijom. Ukoliko se ne pozove commit() transakcija nece biti
                # potvrdjena pa se samim tim rezultat nece uskladistiti u bazu podataka. Vise upita koji zavise
                # jedan od drugo moguce je grupisati u jednu transakciju tako sto se nakon izvrsavanja cele grupe
                # upita pozove commit().
    return flask.jsonify(flask.request.json), 201 # Status kod 201 oznacava uspesno kreiran resurs.

@korisnik_blueprint.route("/korisnik/<int:id_korisnika>", methods=["PUT"])
def izmeni_korisnika(id_korisnika):
    # Provera da li je korisnik prijavljen.
    print("DJAVO JE NOCAS OPET U GRADU")
    db = mysql.get_db()
    cursor = db.cursor()
    data = flask.request.json
    data["id"] = id_korisnika # Id proizvoda koji treba azurirati preuzima
                              # se iz vrednosti parametra URL-a.
    cursor.execute("UPDATE korisnik SET korisnicko_ime=%(korisnicko_ime)s, prezime=%(prezime)s, ime=%(ime)s WHERE id=%(id)s", data)
    db.commit()
    return "", 200

# Uklanjanje proizvoda vrsi se po id-ju proizvoda.
# Id ce biti prosledjen kao parametar URL-a.
@korisnik_blueprint.route("/korisnik/<int:id_korisnika>", methods=["DELETE"])
def ukloni_korisnika(id_korisnika):
    print(id_korisnika)
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM karta WHERE korisnik_id=%s", (id_korisnika))
    db.commit()
    cursor.execute("DELETE FROM korisnik WHERE id=%s", (id_korisnika,))
    db.commit()
    return "", 204 # Operacija je uspesna ali je telo odgovora prazno.f