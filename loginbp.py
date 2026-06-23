from flask import Blueprint, render_template, request,flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
import sqlite3, os
import bcrypt 
from flask_login import login_user, logout_user


login_blueprint= Blueprint('login_blueprint',__name__)

@login_blueprint.route("/")
def login_seite():
    return render_template("show.html")

#os für Dateipfade
skript_ordner = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(skript_ordner, "tauschdaten.db")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=15),
    Regexp(r'^[A-Za-z\d]+$', message="Der Username darf nur Buchstaben und Zahlen enthalten")])

    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=20),
    Regexp( #.*? = suche vom Anfang bis zum Ende nach einem Muster, das die folgenden Bedingungen erfüllt
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_.\-])[A-Za-z\d@$!%*?&_.\-]+$',
            #kleinb.   großb.     zahl digit   sonderz.      alle erlaubten Zeichen im Passwort
        message="Das Passwort muss mindestens einen Großbuchstaben, einen Kleinbuchstaben, eine Zahl und ein Sonderzeichen (@$!%*?&_.-) enthalten.")])
    
    

    #Zweites passwortfeld für Bestaätigung
    password_confirm = PasswordField("Passwort bestätigen", validators=[
        DataRequired(message="Bitte bestätige dein Passwort."),
        # EqualTo zeigt auf den Variablennamen des ersten Feldes ("password")
        EqualTo("password", message="Die Passwörter stimmen nicht überein. Bitte überprüfe deine Eingabe!")
    ])
    
    matrikelnummer = StringField("Matrikelnummer", validators=[DataRequired(),
    Regexp(r"^7720\d{7}$", message="Bitte die Matrikelnummer eingeben")])
    
    name = StringField("Name", validators=[DataRequired(),Length(min=2, max=20),
    Regexp(r'^[A-Za-z]+$', message="Der Nachname darf nur Buchstaben enthalten")])
    

    vorname = StringField("Vorname", validators=[DataRequired(),Length(min=2, max=20),
    Regexp(r'^[A-Za-z]+$', message="Der Vorname darf nur Buchstaben enthalten")])
    
    email = StringField("HWR-Email", validators=[DataRequired(),
     Regexp(r".*@stud.hwr-berlin.de$", message="Bitte eine gültige HWR-E-Mail eingeben" )])
    
    
    studiengang = SelectField(
    "Studiengang",
    choices=[],
    validators=[DataRequired()])

    submit = SubmitField("Registrieren")



@login_blueprint.route("/registrieren", methods=["GET", "POST"])
def registrieren():

    #leeres formular ertellen
    form = RegisterForm()



    with sqlite3.connect(path) as conn:
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM studiengang")
     datenbank_zeilen = cursor.fetchall()


    #für flask muss es 2x angegeben werden also ("WiInfo", "WiInfo") --> (Value für backend, Label für frontend)
    form.studiengang.choices = [(zeile[0], zeile[0]) for zeile in datenbank_zeilen]
   

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        matrikelnummer = form.matrikelnummer.data
        name = form.name.data
        vorname = form.vorname.data
        email = form.email.data
        studiengang = form.studiengang.data

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
      
        with sqlite3.connect(path) as conn:
            cursor = conn.cursor()
        # Übereinstimmungen bei Username, E-Mail ODER Matrikelnummer
            cursor.execute("""
                SELECT * FROM studenten 
                WHERE username = ? OR email = ? OR matrikelnummer = ?
            """, (username, email, matrikelnummer))
            
            existierender_user = cursor.fetchone()
        if existierender_user is not None:
            # Wenn man jemanden findet, abbrechen 
            flash("Ein Account mit diesem Usernamen, dieser E-Mail oder dieser Matrikelnummer existiert bereits!", "r_danger")
            return render_template("register.html", form=form)
       
        #ansonsten speichern
        with sqlite3.connect(path) as conn:
            cursor = conn.cursor()
            cursor.execute(
             """INSERT INTO studenten (username, matrikelnummer, name , vorname, email  ,password , studiengang)
                VALUES (?, ?, ?, ?, ?, ?, ?)
             """, (username, matrikelnummer, name , vorname, email, hashed_password , studiengang))
            conn.commit()
        flash("Account ertellt, bitte logen Sie sich ein", "succes")
        return redirect(url_for(".login_seite"))
    return render_template("register.html",form=form)


#Anmelden!!
@login_blueprint.route("/anmelden", methods=["GET", "POST"])
def anmelden():

 if request.method== "POST": 
    a_email=request.form.get("email")
    a_passwort= request.form.get("password")

    with sqlite3.connect(path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM studenten WHERE email = ?", (a_email,))
            student = cursor.fetchone()

    if student is None:
            flash("Der Account wurde nicht gefunden, bitte nochmal versuchen", "danger")
    else:
            # Index 5, weil sich in der Tabelle Student, das Passwordt in der 6. Spalte befindet
            db_passwort_hash = student[5] 
            
            #verschlüsseltes Passwort wird übersetzt
            if isinstance(db_passwort_hash, str):
                db_passwort_hash=db_passwort_hash.encode('utf-8')
            

            if not bcrypt.checkpw(a_passwort.encode('utf-8'), db_passwort_hash):
                flash("Das Passwort ist falsch.", "danger")
            else:
                session.clear()
                session["user"] = student[0] # Username in der Session speichern!
                from app import User
                user_obj = User(id=str(student[0]), # wird von flask-login gebraucht
                    username=student[0],
                    vorname=student[1],
                    name=student[2],
                    email=student[3],
                    matrikelnummer=student[4],
                    studiengang=student[5])
                login_user(user_obj)

                return redirect(url_for("dashboard")) # Weiterleitung zum Dashboard!
                #open start application()
            
    # falls es nicht klappt, dann wird die Startseite neu geladen
    return redirect("/")


@login_blueprint.route("/slog", methods=["GET", "POST"])
def s_anmelden():
 
 if  request.method == 'POST':
     ma_id = request.form.get("ma_id")
     m_passwort = request.form.get("password")
     m_email = request.form.get("Email")

     with sqlite3.connect(path) as conn:
            cursor = conn.cursor() #ma_id la pk und davon alles auswähle (ganze Zeile)
            cursor.execute("SELECT * FROM studienbüro_ma WHERE ma_id = ?", (ma_id,))
            mitarbeiter = cursor.fetchone()

     if mitarbeiter is None: 
         flash("Angaben nicht gefunden!.", "s_danger")
     # 4= index angabe für Spalte--> da befindet sich das Passwoert
     else:
        mh_passwort = mitarbeiter[4]
        db_email = mitarbeiter[3]
        
        if isinstance(mh_passwort, str):
            mh_passwort=mh_passwort.encode('utf-8')

         # index 4= Spalte 5 in db
        if not bcrypt.checkpw(m_passwort.encode('utf-8'), mh_passwort):
                flash("Das Passwort ist falsch.", "s_danger")
        
        elif m_email != db_email:
                flash("Die Email ist falsch.", "s_danger")
        else: 
          session.clear()
          session["mitarbeiter"] = mitarbeiter[0] # In Session merken
          from app import User
          user_obj = User(id=str(mitarbeiter[0]), # wird von flask-login gebraucht
                ma_id=mitarbeiter[0],
                vorname=mitarbeiter[1],
                name=mitarbeiter[2],
                email=mitarbeiter[3])
          login_user(user_obj)

          return redirect(url_for("profil"))
         
# Seite neu laden falls die Angaben falsch sind
 return render_template("studbuero.html")


@login_blueprint.route("/logout")
def logout ():
    logout_user()
    session.clear()
    flash("Erfolgreich abgemeldet", "logout_success")
    return redirect(url_for(".login_seite"))

@login_blueprint.route("/studienbuero")
def studbuero():
    return render_template("studbuero.html")
 