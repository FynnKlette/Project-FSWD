from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo

app = Flask(__name__)


@app.route("/")
def login_seite():
    return render_template("show.html")



app.config["SECRET_KEY"] = "schlüssel"


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=15),
    Regexp(r'^[A-Za-z]+$', message="Der Username darf nur Buchstaben enthalten")])



    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=20),
    Regexp( #.*? = suche vom Anfang bis zum Ende nach einem Muster, das die folgenden Bedingungen erfüllt
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_.\-])[A-Za-z\d@$!%*?&_.\-]$',
            #kleinb.   großb.     zahl digit   sonderz.      alle erlaubten Zeichen im Passwort
        message="Das Passwort muss mindestens einen Großbuchstaben, einen Kleinbuchstaben, eine Zahl und ein Sonderzeichen (@$!%*?&_.-) enthalten.")])
    
    


    password_confirm = PasswordField("Passwort bestätigen", validators=[
        DataRequired(message="Bitte bestätige dein Passwort."),
        # EqualTo zeigt auf den Variablennamen des ersten Feldes ("password")
        EqualTo("password", message="Die Passwörter stimmen nicht überein. Bitte überprüfe deine Eingabe!")
    ])
    
    matrikelnummer = StringField("Matrikelnummer", validators=[DataRequired(),
    Regexp(r"^7720\d{8}$", message="Bitte die Matrikelnummer eingeben")])
    
    name = StringField("Name", validators=[DataRequired(),Length(min=2, max=20),
    Regexp(r'^[A-Za-z]+$', message="Der Username darf nur Buchstaben enthalten")])
    

    vorname = StringField("Vorname", validators=[DataRequired(),Length(min=2, max=20),
    Regexp(r'^[A-Za-z]+$', message="Der Vorname darf nur Buchstaben enthalten")])
    
    email = StringField("HWR-Email", validators=[DataRequired(),
     Regexp(r".*@stud.hwr-berlin.de$", message="Bitte eine gültige HWR-E-Mail eingeben" )])
    
    
    studiengang = SelectField(
    "Studiengang",
    choices=[
        ("WI", "Wirtschaftsinformatik"),
        ("Wirtschaftsingenieur/in - Umwelt und Nachhaltigkeit", "Wirtschaftsingenieur/in - Umwelt und Nachhaltigkeit"),
        ("BA", "Business Administration"),
        ("VWL", "Volkswirtschaftslehre"),
        ("WR", "Wirtschaftsrecht"),
        ("International Digital Business", "International Digital Business"),
        ("Internationales Management / Management International", "Internationales Management / Management International"),
        ("Unternehmensgründung und Unternehmensnachfolge", "Unternehmensgründung und Unternehmensnachfolge")
    ],
    validators=[DataRequired()]
)

    submit = SubmitField("Registrieren")


@app.route("/registrieren", methods=["GET", "POST"])
def registrieren():

    form = RegisterForm()


    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        matrikelnummer = form.matrikelnummer.data
        name = form.name.data
        vorname = form.vorname.data
        email = form.email.data
        studiengang = form.studiengang.data


        print(username)
        print(password)
        print(matrikelnummer)
        print(name)
        print(vorname)
        print(email)
        print(studiengang)


        return "Registrierung erfolgreich"


    return render_template("register.html",form=form)



@app.route("/studienbuero")
def studbuero():
    return render_template("studbuero.html")






if __name__ == "__main__":
    app.run(debug=True, port=5001)
