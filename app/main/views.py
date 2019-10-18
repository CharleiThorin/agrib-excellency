from . import main
from flask import render_template, session, redirect, flash, url_for
from .forms import ContactForm
from ..email import send_email


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@main.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['phone'] = form.phone.data
        session['message'] = form.message.data
        send_email('infor@agrib-excellency.com', 'New Subscriber', 'email/subscriber', name=session.get('name'),
                   email=session.get('email'), phone=session.get('phone'), message=session.get('message'))
        flash('Message sent successfully',)
        return redirect(url_for('main.contact'))
    return render_template('contact.html', form=form)


@main.route('/work', methods=['GET'])
def work():
    return render_template('work.html')


@main.route('/work-single', methods=['GET'])
def work_single():
    return render_template('workSingle.html')
