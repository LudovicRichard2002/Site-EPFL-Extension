from flask import Flask, render_template, request
from flask_mail import Mail, Message




app = Flask(__name__)

app.config['MAIL_SERVER'] = 'infomaniak.ch'
app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'contactastrocat@wewfamily.ch'
app.config['MAIL_PASSWORD'] = 'Removed for Github'

mail = Mail(app)




def sendTestEmail():
    msg = Message("Our first Python Email",
                  sender="contactastrocat@wewfamily.ch",
                  recipients=["receiveastrocat@wewfamily.ch"])

    msg.body = """ 
    Hello there,
    I am sending this message from python.
    say Hello
    regards,
    Me
    """


    msg.html = """
    <div>
    <h5>Hello there</h5>
    <br>
    <p>
    I am sending this message from Python 
    <br>
    Say hello 
    <br>
    Regards
    </p>
    </div>
    """

    mail.send(msg)


def sendContactForm(result):
    msg = Message("Contact from Astrocatgames website",
                  sender="contactastrocat@wewfamily.ch",
                  recipients=["receiveastrocat@wewfamily.ch"])

    msg.body = """
    Hello there,
    You just received a contact form.
    Name: {}
    Email: {}
    Message: {}
    regards,
    Webmaster
    """.format(result['name'], result['email'], result['message'])

    mail.send(msg)



@app.route("/")
def hello():

    sendTestEmail()

    

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == 'POST':
        result = {}
        
        result['name'] = request.form['name']
        result['email'] = request.form['email'].replace(' ', '').lower()
        result['message'] = request.form['message']

        sendContactForm(result)

        return render_template('contact.html', **locals())


    return render_template('contact.html', **locals())



# if __name__ == "__main__":
#     app.run(host='0.0.0.0')