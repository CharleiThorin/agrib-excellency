from . import main
from flask import render_template, session, redirect, flash, url_for
from .forms import ContactForm, RegistrationForm
from ..email import send_email


@main.route('/', methods=['GET'])
def index():
    session['ind'] = 'active'
    return render_template('index.html', indx=session.get('ind'))


@main.route('/about', methods=['GET'])
def about():
    session['abt'] = 'active'
    return render_template('about.html', abt=session.get('abt'))


@main.route('/blog', methods=['GET'])
def blog():
    session['blg'] = 'active'
    return render_template('blog.html', blg=session.get('blg'))


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    session['cont'] = 'active'
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['phone'] = form.phone.data
        session['message'] = form.message.data
        send_email('infor@agrib-excellency.com', 'New Subscriber', 'email/subscriber', name=session.get('name'),
                   email=session.get('email'), phone=session.get('phone'), message=session.get('message'))
        flash('Message sent successfully',)
        return redirect(url_for('main.contact'))
    return render_template('contact.html', form=form, cont=session.get('cont'))


@main.route('/work', methods=['GET'])
def work():
    session['wrk'] = 'active'
    return render_template('work.html', wrk=session.get('wrk'))


# @main.route('/work-single', methods=['GET'])
# def work_single():
#     session['active'] = 'active'
#     return render_template('workSingle.html', link=session.get('active'))


@main.route('/argentina-expo', methods=['GET'])
def argentina_expo():
    session['wrk'] = 'active'
    return render_template('argentinaTrip.html', arge=session.get('wrk'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    session['wrk'] = 'active'
    if form.validate_on_submit():
        session['first_name'] = form.first_name.data
        session['last_name'] = form.last_name.data
        session['email'] = form.email.data
        session['phone'] = form.phone.data
        session['message'] = form.message.data
        send_email('infor@agrib-excellency.com', 'New Subscriber', 'email/registered',
                   first_name=session.get('first_name'), last_name=session.get('last_name'),
                   email=session.get('email'), phone=session.get('phone'), message=session.get('message'))
        flash('You have successfully Registered',)
        return redirect(url_for('main.argentina_expo'))
    return render_template('register.html', form=form, reg=session.get('wrk'))
