from flask import Flask, request, redirect, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password

mail = Mail(app)

@app.route('/')
def home():
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    visitor_email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    
    email_subject = "New Form Submission"
    email_body = (f"User Name: {name}\n"
                  f"User Email: {visitor_email}\n"
                  f"Subject: {subject}\n"
                  f"User Message: {message}\n")

    msg = Message(email_subject,
                  sender='me.akhil05@gmail.com',  # Replace with your email
                  recipients=['bharadwajsprajwal19@gmail.com'])  # Replace with recipient email
    msg.body = email_body
    
    try:
        mail.send(msg)
        return redirect('/contact.html')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
