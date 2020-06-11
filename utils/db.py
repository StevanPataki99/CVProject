# Kako bi se izbegle ciklicne zavisnosti
# i pojednostavio pristup deljenom objektu
# za pristup bazi podataka, ovaj objekat
# ce biti instanciran u modulu db koji ce
# se po potrebi ukljucivati u druge delove
# implementacije.

from flaskext.mysql import MySQL # Importovanje klase za rad sa MySQL serverom.
from flaskext.mysql import pymysql # Importovanje paketa za podesavanje tipa kursora.

# Instanciranje objekta za upravljanje konekcijama sa bazom podataka.
mysql = MySQL(cursorclass=pymysql.cursors.DictCursor) # Potrebno je proslediti flask aplikaciju iz koje
                                                      # je moguce procitati konfiguraciju, u ovom slucaju
                                                      # to nije moguce uciniti jer josuvek ne postoji
                                                      # instanca koja se moze proslediti. Posto instanca
                                                      # aplikacije nije navedena podrazumevace se da ce
                                                      # instanca biti dostavljena naknadno.
                                                      # Argument cursorclass se koristi za podesavanje tipa
                                                      # kursora. U ovom slucaju kurosr je podesen da bude
                                                      # DictCursor sto znaci da ce rezultati upita biti vracani
                                                      # kao liste recnika ciju kljucevi su nazivi kolona a vrednosti
                                                      # vrednosti u datim kolonama. Ukliko se izostavi podesavanje
                                                      # za tip kursora koristi se podrazumevani tip kursora koji
                                                      # vraca torke torki u kojima se, redom navedenim u upitu
                                                      # nalaze vrednosti koje su rezultat upita.