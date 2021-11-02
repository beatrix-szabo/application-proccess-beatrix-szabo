from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/applicant-phone')
def applicant_phone():
    applicant_name = request.args.get('app_name')
    applicant_email = request.args.get('app_email')
    if applicant_name:
        applicant = data_manager.get_applicant(applicant_name)
    elif applicant_email:
        applicant = data_manager.get_applicant_by_email(applicant_email)
    return render_template('applicant_phone.html', applicant=applicant)


@app.route('/applicants')
def applicants():
    applicants = data_manager.get_all_applicants()
    return render_template("applicants.html", applicants=applicants)


@app.route('/applicants/<code>', methods=['GET', 'POST'])
def applicant_profile(code):
    if request.method == 'POST':
        phone_number = request.form.get("phone")
        data_manager.update_applicant_phone_number(phone_number, code)
        return redirect(f'/applicants/{code}')
    applicant = data_manager.get_specific_applicant(code)
    return render_template('applicant_profile.html', applicant=applicant)


@app.route('/applicants/<code>/delete')
def applicant_profile_delete(code):
    data_manager.delete_applicant(code)
    return redirect('/applicants')


@app.route('/applicants/delete_by_email', methods=['GET', 'POST'])
def delete_by_email():
    part_of_email = request.form.get('delete_by_email')
    data_manager.delete_applicant_by_email(part_of_email)
    return redirect('/applicants')


@app.route('/add-applicant', methods=['GET', 'POST'])
def add_nem_applicant():
    if request.method == "POST":
        first_name=request.form.get('first_name')
        last_name= request.form.get('last_name')
        phone_number=request.form.get('phone_number')
        email=request.form.get('email')
        application_number=request.form.get('app_num')
        data_manager.add_new_applicant([first_name, last_name,phone_number,email, application_number])
        return redirect('/applicants')
    elif request.method =="GET":
        return render_template('add_applicant.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('name-input')
    city = request.args.get('city_input')

    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city:
        mentor_details = data_manager.get_mentors_by_city(city)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details)


if __name__ == '__main__':
    app.run(debug=True)
