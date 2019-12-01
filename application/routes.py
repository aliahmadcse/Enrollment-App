from application import app, db
from flask import render_template, request, json, Response, redirect, flash
from application.models import User, Enrollment, Course
from application.forms import LoginForm, RegisterForm

courseData = [
    {
        "courseID": "1111",
        "title": "PHP 101",
        "description": "Intro to PHP",
        "credits": 3,
        "term": "Fall, Spring"
    },
    {
        "courseID": "2222",
        "title": "Java 1",
        "description": "Intro to Java Programming",
        "credits": 4,
        "term": "Spring"
    },
    {
        "courseID": "3333",
        "title": "Adv PHP 201",
        "description": "Advanced PHP Programming",
        "credits": 3,
        "term": "Fall"
    },
    {
        "courseID": "4444",
        "title": "Angular 1",
        "description": "Intro to Angular",
        "credits": 3,
        "term": "Fall, Spring"
    },
    {
        "courseID": "5555",
        "title": "Java 2",
        "description": "Advanced Java Programming",
        "credits": 4,
        "term": "Fall"
    }
]


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html", index=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        if request.form.get('email') == "test@uta.com":
            flash("Logged in Successfully","success")
            return redirect("/index")
        else:
            flash("Something went wrong","danger")
    return render_template("login.html", login=True, form=form, title="Login")


@app.route('/courses')
# use of url vaariables
@app.route('/courses/<term>')
def courses(term="Fall 2019"):
    return render_template("courses.html", courses=True, courseData=courseData, term=term)


@app.route('/register')
def register():
    form=RegisterForm()
    return render_template("register.html", register=True,title="Register",form=form)


@app.route('/enrollment', methods=["GET", "POST"])
def enrollment():
    courseID = request.form.get("courseID")
    title = request.form.get("title")
    term = request.form.get("term")
    data = {"id": courseID, "title": title, "term": term}

    return render_template("enrollment.html", data=data)


@app.route('/api/')
@app.route('/api/<idx>')
def api(idx=None):
    if idx == None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype='application/json')


@app.route('/user')
def user():
    # User(user_id=3, first_name="Ali", last_name="Ahmad",
    #      email="aliahmad@gmail.com", password="abc123").save()
    # User(user_id=4, first_name="Asad", last_name="Rehman",
    #      email="asad@gmail.com", password="asad123").save()
    users = User.objects.all()
    return render_template("user.html", users=users)
