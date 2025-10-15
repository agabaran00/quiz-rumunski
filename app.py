from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import random

app = Flask(__name__, static_folder='statics')

@app.route("/")
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)
app.config["SECRET_KEY"] = "tajny_klucz_123"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

pytan_na_runde = 10  # liczba pytań w jednej rundzie

# --- Lista pytań ---
pytania = [
    {"pytanie": "Jak odmienić czasownik a fi (być) w 3.os?", "odpowiedzi": ["fie", "fie"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a avea (mieć) w 3.os?", "odpowiedzi": ["aibă", "aiba"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a face (robić) w 3.os?", "odpowiedzi": ["facă", "faca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a merge (iść) w 3.os?", "odpowiedzi": ["meargă", "mearga"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a veni (przychodzić) w 3.os?", "odpowiedzi": ["vină", "vina"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a vedea (widzieć) w 3.os?", "odpowiedzi": ["vadă", "vada"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a auzi (słyszeć) w 3.os?", "odpowiedzi": ["audă", "auda"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a spune (mówić, powiedzieć) w 3.os?", "odpowiedzi": ["spună", "spuna"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a da (dawać) w 3.os?", "odpowiedzi": ["dea", "dea"], "poziom": "podstawowy"}, 
    {"pytanie": "Jak odmienić czasownik a lua (brać) w 3.os?", "odpowiedzi": ["ia", "ia"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a mânca (jeść) w 3.os?", "odpowiedzi": ["mănânce", "manance"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a bea (pić) w 3.os?", "odpowiedzi": ["bea", "bea"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a dormi (spać) w 3.os?", "odpowiedzi": ["doarmă", "doarma"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a lucra (pracować) w 3.os?", "odpowiedzi": ["lucreze", "lucreze"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a citi (czytać) w 3.os?", "odpowiedzi": ["citească", "citeasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a scrie (pisać) w 3.os?", "odpowiedzi": ["scrie", "scrie"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a învăța (uczyć się) w 3.os?", "odpowiedzi": ["învețe", "invete"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a înțelege (rozumieć) w 3.os?", "odpowiedzi": ["înțeleagă", "inteleaga"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a crede (wierzyć, myśleć) w 3.os?", "odpowiedzi": ["creadă", "creada"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a ști (wiedzieć) w 3.os?", "odpowiedzi": ["știe", "stie"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a putea (móc) w 3.os?", "odpowiedzi": ["poată", "poata"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a vrea (chcieć) w 3.os?", "odpowiedzi": ["vrea", "vrea"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a trebui (musieć) w 3.os?", "odpowiedzi": ["trebuiască", "trebuiasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a iubi (kochać) w 3.os?", "odpowiedzi": ["iubească", "iubeasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a plăcea (lubić, podobać się) w 3.os?", "odpowiedzi": ["placă", "placa"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a urî (nienawidzić) w 3.os?", "odpowiedzi": ["urască", "urasca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a râde (śmiać się) w 3.os?", "odpowiedzi": ["râdă", "râda"],"poziom": "sredniozawansowany" },
    {"pytanie": "Jak odmienić czasownik a glumi (żartować) w 3.os?", "odpowiedzi": ["glumeasca", "glumească"],"poziom": "sredniozawansowany" },
    {"pytanie": "Jak odmienić czasownik a plânge (płakać) w 3.os?", "odpowiedzi": ["plângă", "planga"], "poziom": "sredniozawansowany" }, 
    {"pytanie": "Jak odmienić czasownik a cânta (śpiewać) w 3.os?", "odpowiedzi": ["cânte", "cante"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a dansa (tańczyć) w 3.os?", "odpowiedzi": ["danseze", "danseze"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a întârzia (spóźniać się) w 3.os?", "odpowiedzi": ["întârzie", "intarzie"],"poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a tăia (ciąć) w 3.os?", "odpowiedzi": ["taie", "taie"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a deschide (otwierać) w 3.os?", "odpowiedzi": ["deschidă", "deschida"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a închide (zamykać) w 3.os?", "odpowiedzi": ["închidă", "inchida"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a folosi (używać) w 3.os?", "odpowiedzi": ["folosească", "foloseasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a porni (włączać, uruchamiać) w 3.os?", "odpowiedzi": ["pornească", "porneasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a opri (zatrzymywać, wyłączać) w 3.os?", "odpowiedzi": ["oprească", "opreasca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a scoate (wyjmować) w 3.os?", "odpowiedzi": ["scoată", "scoata"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a băga (wkładać) w 3.os?", "odpowiedzi": ["bage", "bage"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a pune (kłaść) w 3.os?", "odpowiedzi": ["pună", "puna"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a aduce (przynosić) w 3.os?", "odpowiedzi": ["aducă", "aduca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a duce (nieść, zanieść) w 3.os?", "odpowiedzi": ["ducă", "duca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a pleca (odchodzić) w 3.os?", "odpowiedzi": ["plece", "plece"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a ajunge (dojechać, dotrzeć) w 3.os?", "odpowiedzi": ["ajungă", "ajunga"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a intra (wchodzić) w 3.os?", "odpowiedzi": ["intre", "intre"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a ieși (wychodzić) w 3.os?", "odpowiedzi": ["iasă", "iasa"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a coborî (schodzić, wysiadać) w 3.os?", "odpowiedzi": ["coboare", "coboare"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a urca (wchodzić, wsiadać) w 3.os?", "odpowiedzi": ["urce", "urce"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a cumpăra (kupować) w 3.os?", "odpowiedzi": ["cumpere", "cumpere"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a vinde (sprzedawać) w 3.os?", "odpowiedzi": ["vândă", "vanda"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a plăti (płacić) w 3.os?", "odpowiedzi": ["plătească", "plateasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a întreba (pytać) w 3.os?", "odpowiedzi": ["întrebe", "intrebe"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a răspunde (odpowiadać) w 3.os?", "odpowiedzi": ["răspundă", "raspunda"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a arăta (pokazywać) w 3.os?", "odpowiedzi": ["arăte", "arate"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a explica (wyjaśniać) w 3.os?", "odpowiedzi": ["explice", "explice"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a repeta (powtarzać) w 3.os?", "odpowiedzi": ["repete", "repete"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a alege (wybierać) w 3.os?", "odpowiedzi": ["aleagă", "aleaga"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a prefera (woleć) w 3.os?", "odpowiedzi": ["prefere", "prefere"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a încerca (próbować) w 3.os?", "odpowiedzi": ["încerce", "incearce"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a gândi (myśleć) w 3.os?", "odpowiedzi": ["gândească", "gandeasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a simți (czuć) w 3.os?", "odpowiedzi": ["simtă", "simta"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a trăi (żyć) w 3.os?", "odpowiedzi": ["trăiască", "traiasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a visa (śnić, marzyć) w 3.os?", "odpowiedzi": ["viseze", "viseze"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a munci (pracować) w 3.os?", "odpowiedzi": ["muncească", "munceasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a găsi (znajdować) w 3.os?", "odpowiedzi": ["găsească", "gaseasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a lăsa (zostawiać) w 3.os?", "odpowiedzi": ["lase", "lase"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a ține (trzymać) w 3.os?", "odpowiedzi": ["țină", "tina"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a suna (dzwonić) w 3.os?", "odpowiedzi": ["sune", "sune"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a chema (wołać, nazywać) w 3.os?", "odpowiedzi": ["cheme", "cheme"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a ajuta (pomagać) w 3.os?", "odpowiedzi": ["ajute", "ajute"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a curăța (czyścić, sprzątać) w 3.os?", "odpowiedzi": ["curețe", "curete"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a spăla (myć) w 3.os?", "odpowiedzi": ["spele", "spele"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a vorbi (mówić) w 3.os?", "odpowiedzi": ["vorbească", "vorbeasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a șterge (wycierać, usuwać) w 3.os?", "odpowiedzi": ["șteargă", "stearga"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a amâna (odkładać, opóźniać) w 3.os?", "odpowiedzi": ["amâne", "amane"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a extinde (rozszerzać) w 3.os?", "odpowiedzi": ["extindă", "extinda"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a posta (publikować, zamieszczać) w 3.os?", "odpowiedzi": ["posteze", "posteze"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a păstra (zachowywać, przechowywać) w 3.os?", "odpowiedzi": ["păstreze", "pastreze"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a mișca (ruszać, poruszać) w 3.os?", "odpowiedzi": ["miște", "miste"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a angaja (zatrudniać) w 3.os?", "odpowiedzi": ["angajeze", "angajeze"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a anula (anulować) w 3.os?", "odpowiedzi": ["anuleze", "anuleze"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a pierde (tracić, gubić) w 3.os?", "odpowiedzi": ["piardă", "piarda"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a edita (edytować) w 3.os?", "odpowiedzi": ["editeze", "editeze"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a preface (udawać, przemieniać) w 3.os?", "odpowiedzi": ["prefacă", "prefaca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a cădea (upaść, spadać) w 3.os?", "odpowiedzi": ["cadă", "cada"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a scădea (zmniejszać, obniżać) w 3.os?", "odpowiedzi": ["scadă", "scada"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a povesti (opowiadać) w 3.os?", "odpowiedzi": ["povestească", "povesteasca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a mări (zwiększać, powiększać) w 3.os?", "odpowiedzi": ["mărească", "mareasca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a păcăli (oszukiwać, nabierać) w 3.os?", "odpowiedzi": ["păcălească", "pacaleasca"], "poziom": "sredniozawansowany"}, 
    {"pytanie": "Jak odmienić czasownik a slăbi (chudnąć, osłabiać) w 3.os?", "odpowiedzi": ["slăbească", "slabeasca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a îngrășa (tyć, tuczyć) w 3.os?", "odpowiedzi": ["îngrașe", "ingrase"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a arăta (pokazywać) w 3.os?", "odpowiedzi": ["arăte", "arate"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a stinge (gasić, wyłączać) w 3.os?", "odpowiedzi": ["stingă", "stinga"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a strica (psuć) w 3.os?", "odpowiedzi": ["strice", "strice"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a apăsa (naciskać) w 3.os?", "odpowiedzi": ["apese", "apese"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a se mira (dziwić się) w 3.os?", "odpowiedzi": ["se mire", "se mire"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a presupune (przypuszczać, zakładać) w 3.os?", "odpowiedzi": ["presupună", "presupuna"]},
    {"pytanie": "Jak odmienić czasownik a ține (trzymać) w 3.os?", "odpowiedzi": ["țină", "tina"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a întreține (utrzymywać, dbać) w 3.os?", "odpowiedzi": ["întrețină", "intretina"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a susține (wspierać, podtrzymywać) w 3.os?", "odpowiedzi": ["susțină", "sustina"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a alege (wybierać) w 3.os?", "odpowiedzi": ["aleagă", "aleaga"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a privi (patrzeć, oglądać) w 3.os?", "odpowiedzi": ["privească", "priveasca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a cheltui (wydawać pieniądze) w 3.os?", "odpowiedzi": ["cheltuiască", "cheltuiasca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a crește (rosnąć, wychowywać) w 3.os?", "odpowiedzi": ["crească", "creasca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a nota (zaznaczać, notować) w 3.os?", "odpowiedzi": ["noteze", "noteze"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a cauza (powodować) w 3.os?", "odpowiedzi": ["cauzeze", "cauzeze"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a participa (uczestniczyć) w 3.os?", "odpowiedzi": ["participe", "participe"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a greși (popełniać błąd, mylić się) w 3.os?", "odpowiedzi": ["greșească", "gresesca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a vindeca (leczyć, uzdrawiać) w 3.os?", "odpowiedzi": ["vindece", "vindece"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a zbura (latać) w 3.os?", "odpowiedzi": ["zboare", "zboare"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a trece (przechodzić, mijać) w 3.os?", "odpowiedzi": ["treacă", "treaca"], "poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a printa (drukować) w 3.os?", "odpowiedzi": ["printeze", "printeze"],"poziom": "sredniozawansowany"},
    {"pytanie": "Jak odmienić czasownik a se gândi (zastanawiać się, myśleć) w 3.os?", "odpowiedzi": ["se gândească", "se gandeasca"], "poziom": "podstawowy"},
    {"pytanie": "Jak odmienić czasownik a găti (gotować) w 3.os?", "odpowiedzi": ["gătească", "gateasca"], "poziom": "podstawowy"},
]

# --- Funkcja losująca pytania dla danego poziomu ---
def wybierz_pytania(poziom):
    pytania_poziom = [p for p in pytania if p.get("poziom") == poziom]
    if not pytania_poziom:
        # fallback do podstawowego, jeśli nie ma pytań dla danego poziomu
        pytania_poziom = [p for p in pytania if p.get("poziom") == "podstawowy"]
    return random.sample(pytania_poziom, min(len(pytania_poziom), pytan_na_runde))

# --- Strona główna ---
@app.route("/")
def home():
    return redirect(url_for("login"))

# --- Logowanie ---
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        poziom = request.form.get("poziom")
        session["poziom"] = poziom

        # przygotowanie sesji do quizu
        session["index"] = 0
        session["score_rundy"] = 0
        session["suma_punktow"] = 0
        session["bledy"] = []
        session["runda"] = 1

        # losujemy pytania dla poziomu
        session["pytania"] = wybierz_pytania(poziom)

        return redirect(url_for("quiz"))

    return render_template("login.html")

# --- Quiz ---
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "poziom" not in session:
        return redirect(url_for("login"))

    pytania_runda = session["pytania"]
    index = session["index"]
    score_rundy = session.get("score_rundy", 0)
    bledy = session.get("bledy", [])
    komunikat = session.get("komunikat", "")
    pokaz_odp = session.get("pokaz_odp", False)

    if request.method == "POST":
        action = request.form.get("action")
        if action == "sprawdz":
            odp = request.form.get("odp", "").strip().lower()
            poprawne_odp = [o.lower() for o in pytania_runda[index]["odpowiedzi"]]

            if odp in poprawne_odp:
                komunikat = "✅ Dobrze!"
                score_rundy += 1
            else:
                poprawna = pytania_runda[index]["odpowiedzi"][0]
                komunikat = f"❌ Źle! Poprawna odpowiedź to: {poprawna}"
                bledy.append({"twoja": odp, "poprawna": poprawna})

            session["score_rundy"] = score_rundy
            session["bledy"] = bledy
            session["komunikat"] = komunikat
            session["pokaz_odp"] = True
            return redirect(url_for("quiz"))

        elif action == "nastepne":
            index += 1
            session["index"] = index
            session["komunikat"] = ""
            session["pokaz_odp"] = False

            if index >= len(pytania_runda):
                session["suma_punktow"] += score_rundy
                session.pop("pytania")  # usuń pytania po rundzie
                return redirect(url_for("wynik"))

            return redirect(url_for("quiz"))

    if index < len(pytania_runda):
        pytanie = pytania_runda[index]["pytanie"]
    else:
        return redirect(url_for("wynik"))

    return render_template(
        "quiz.html",
        pytanie=pytanie,
        index=index + 1,
        score=session.get("suma_punktow", 0),
        score_rundy=score_rundy,
        pytan_na_runde=len(pytania_runda),
        komunikat=komunikat,
        pokaz_odp=pokaz_odp,
    )

# --- Wynik ---
@app.route("/wynik", methods=["GET", "POST"])
def wynik():
    if "poziom" not in session:
        return redirect(url_for("login"))

    score_rundy = session.get("score_rundy", 0)
    bledy = session.get("bledy", [])

    if request.method == "POST":
        kontynuacja = request.form.get("kontynuacja")
        if kontynuacja == "nowa_runda":
            poziom = session["poziom"]
            session["pytania"] = wybierz_pytania(poziom)
            session["index"] = 0
            session["score_rundy"] = 0
            session["bledy"] = []
            session["komunikat"] = ""
            session["pokaz_odp"] = False
            session["runda"] += 1
            return redirect(url_for("quiz"))
        else:
            return redirect(url_for("login"))

    return render_template(
        "wynik.html",
        score_rundy=score_rundy,
        bledy=bledy,
        suma_punktow=session.get("suma_punktow", 0),
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
