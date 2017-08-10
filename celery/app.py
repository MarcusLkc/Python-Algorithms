import os
from flask import Flask, render_template, request, session, flash, redirect, url_for
from celery import Celery
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'double-top-secret'

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'marcuscrowder20@gmail.com'
app.config['MAIL_PASSWORD'] = 'qbmblnqriuxcdfys'
app.config['MAIL_DEFAULT_SENDER'] = 'marcuscrowder20@gmail.com'

mail = Mail(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def send_async_email(email):

	with app.app_context():
		msg = Message('Hello from Marcus',
				recipients=[email])
		msg.body = "This is such a great time to be alive"
		mail.send(msg)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html', email=session.get('email', ''))
	email = request.form['email']
	session['email'] = email

	if request.form['submit'] == 'Send':

		send_async_email.delay(email)
		flash('Sending email to {0}'.format(email))
	else:
		send_async_email.apply_async(args=[email], countdown=60)
		flash('An email will be sent to {0} in one minute'.format(email))

	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)

