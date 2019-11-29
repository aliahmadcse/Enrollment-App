from application import app
<<<<<<< HEAD
from flask import render_template, request, json, Response


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
=======
from flask import render_template, request
>>>>>>> parent of d7b3f70... Adds routing pattern for api request


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html", index=True)


@app.route('/login')
def login():
    return render_template("login.html", login=True)


@app.route('/courses')
#use of url vaariables
@app.route('/courses/<term>')
def courses(term="Fall 2019"):
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
    return render_template("courses.html", courses=True, courseData=courseData, term=term)


@app.route('/register')
def register():
    return render_template("register.html", register=True)


@app.route('/enrollment', methods=["GET", "POST"])
def enrollment():
    courseID = request.args.get("courseID")
    title = request.args.get("title")
    term = request.args.get("term")
    data = {"id": courseID, "title": title, "term": term}

    return render_template("enrollment.html", data=data)
