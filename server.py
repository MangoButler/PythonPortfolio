from flask import Flask, render_template, url_for, request, redirect
import os
import csv

app = Flask(__name__)

# def write_to_file(data):
#     input_string = ''
#     for key in data:
#         input_string += key + ': ' + data[key] + ', '
#     with open('database.txt', '+a') as file:
#         file.writelines(input_string + '\n')

def write_to_csv(data):
    with open('database.csv', mode='+a', newline='') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        





@app.route('/', defaults={'page_name': ''})
@app.route("/<string:page_name>")
def html_page(page_name):
    if not page_name:
        return render_template('index.html')
    return render_template(page_name)

@app.route("/thankyou/<name>")
def thankyou_page(name=None):
    return render_template('message.html', value= name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            name = data['email'].split('@')[0]
            write_to_csv(data)
        except Exception:
            return 'something went wrong try again!'
    else:
        return 'There was a problem, try again!'
    return redirect(url_for('thankyou_page', name = name))

# @app.route("/index.html")
# def my_home_ind():
#     return render_template('index.html')

# @app.route("/works.html")
# def my_works():
#     return render_template('works.html')

# @app.route("/about.html")
# def my_about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def my_contact():
#     return render_template('contact.html')