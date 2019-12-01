from application import app, db
from flask import render_template, request, json, Response, redirect, flash,session
from application.models import User, Enrollment, Course
from application.forms import LoginForm, RegisterForm

#courseData=[{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html", index=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        # or you can use request.form.get(email)
        password = form.password.data
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash("Logged in Successfully", "success")
            session["user_id"]=user.user_id
            session["username"]=user.first_name
            return redirect("/index")
        else:
            flash("Something went wrong", "danger")
    return render_template("login.html", login=True, form=form, title="Login")


@app.route('/courses')
# use of url vaariables
@app.route('/courses/<term>')
def courses(term=None):
    if term is None:
        term = "Spring 2019"
    # + means sorting the course in ascending order
    classes = Course.objects.order_by("+courseID")
    return render_template("courses.html", courses=True, courseData=classes, term=term)


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        print(user_id)
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        # updating the database
        user = User(user_id=user_id, email=email,
                    first_name=first_name, last_name=last_name,)
        user.set_password(password)
        user.save()
        flash("You are successfully registered", "success")
        return redirect('/index')

    return render_template("register.html", register=True, title="Register", form=form)


@app.route('/enrollment', methods=["GET", "POST"])
def enrollment():
    courseID = request.form.get("courseID")
    courseTitle = request.form.get("title")
    user_id = 1
    if courseID:
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(
                f"You are already enrolled in this course {courseTitle}", "danger")
            return redirect('/courses')
        else:
            Enrollment(user_id=user_id, courseID=courseID).save()
            flash(f"You are enrolled in {courseTitle}", "success")
    classes = list(User.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'enrollment',
                'localField': 'user_id',
                'foreignField': 'user_id',
                'as': 'r1'
            }
        }, {
            '$unwind': {
                'path': '$r1',
                'includeArrayIndex': 'r1_id',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'course',
                'localField': 'r1.courseID',
                'foreignField': 'courseID',
                'as': 'r2'
            }
        }, {
            '$unwind': {
                'path': '$r2',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'user_id': user_id
            }
        }, {
            '$sort': {
                'courseID': 1
            }
        }
    ]))

    return render_template("enrollment.html", title="Enrollment", enrollment=True, classes=classes)


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
