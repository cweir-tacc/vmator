import flask
from flask_mysqldb import MySQL
import flask_sqlalchemy


############################################

app = flask.Flask(__name__)  # Initiate the App
app.config.from_pyfile('settings.py') # import settings (secret key. DB URI...)
database = flask_sqlalchemy.SQLAlchemy(app)


############################################

@app.route('/', methods=['GET'])
def login_get():
    # LDAP Login Authentication landing page
    # Ensure User in is the system and allow them to create VM, or update info on one of their other VM's
    flask.render_template('tacc_login.html')


@app.route('/', methods=['POST'])
def login_post():
    # LDAP Login Authentication landing page
    # Ensure User in is the system and allow them to create VM, or update info on one of their other VM's
    username = flask.request.form['username']  # 'user' refers to the label 'user' for the form input in the html file
    password = flask.request.form['password']  # 'password' refers to the form input with the label password1
    # LDAP TEST THINGY
    # Redirect to home

    flask.redirect('/home')


@app.route('/logout', methods=['GET'])
def logout():
    del flask.session['auth_user']
    return flask.redirect(flask.request.args.get('url', '/'), 303)


#########

@app.route("/home", methods=['GET'])
def home_get():
    # show the user which VM's they are registered for, and then show the option to create or update new VM
    pass


@app.route("/home", methods=['POST'])
def home_post():
    # show the user which VM's they are registered for, and then show the option to create or update new VM
    pass

#########

@app.route("/create_vm", methods=['GET'])
def create_VM_get():
    # show the fields to create a new VM
    # only the user that created VM can update the
    pass


@app.route("/create_vm", methods=['POST'])
def create_VM_post():
    # show the fields to create a new VM
    # only the user that created VM can update the
    pass

#########

@app.route("/update_vm", methods=['GET'])
def update_VM_get():
    # update one of the users VM's
    # also update the information in zabbix and IPAM
    pass


@app.route("/update_vm", methods=['POST'])
def update_VM_post():
    # update one of the users VM's
    # also update the information in zabbix and IPAM
    pass

#########

@app.route("/delete_vm", methods=['GET'])
def delete_vm_get():
    # TODO: confirm whether or not this would be useful
    # speculative
    pass

#########

@app.route("/hostList", methods=['GET'])
def hostList_get():
    # List all the Hosts currently registered, Allow for people to claim???
    pass


@app.route("/hostList", methods=['POST'])
def hostList_post():
    # List all the Hosts currently registered, Allow for people to claim???
    pass

#########


############################################
# Move this into separate file


if __name__ == "__main__":
    app.run()
