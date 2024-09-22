from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Change if your MySQL username is different
app.config['MYSQL_PASSWORD'] = ''  # Add your MySQL password if you have one
app.config['MYSQL_DB'] = 'portfolio'

mysql = MySQL(app)




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        message = request.form['message']
        
        # Validate inputs (basic validation)
        if not re.match(r'^[A-Za-z0-9\s]+$', name):
            return "Invalid name!"
        if not re.match(r'^[0-9]+$', mobile):
            return "Invalid mobile number!"
        if not message:
            return "Message cannot be empty!"

        # Create a cursor
        cur = mysql.connection.cursor()
        # Insert data into the info table
        cur.execute("INSERT INTO info (name, mobile, message) VALUES (%s, %s, %s)", (name, mobile, message))
        # Commit the changes
        mysql.connection.commit()
        # Close the cursor
        cur.close()
        
        return redirect(url_for('contact'))
    

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/internships')
def internships():
    return render_template('internships.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__=='__main__':
    app.run(debug=True)