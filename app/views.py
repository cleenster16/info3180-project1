import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import ProfileForm
from app.models import UserProfile
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime as dateFormat

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html')

###
#Helper functions for the application
###

def format_date_joined(date_joined):
    return "Joined " + date_joined.strftime("%B, %Y")

#Iterate over contents of uploads folder and returns list of filenames.
def getUploadedImages():
    rootDirect = os.getcwd()
    pathList = []
    for subdir, dirs, files in os.walk(rootDirect + app.config['UPLOAD_FOLDER']):
        for file in files:
            if file.endswith(tuple([".jpg", ".png"])):
                #pathList.append(os.path.join(subdir, file))
                pathList.append("uploads/" + os.path.basename(file))
    return pathList
###

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()

    if request.method == 'POST' and newProfileForm.validate_on_submit():
        profilePhoto = form.photo.data
        filename = secure_filename(profilePhoto.filename)
        profilePhoto.save(os.path.join(
            app.config['UPLOAD_FOLDER'],filename))
        newUser = UserProfile(
            first_name = newProfileForm.first_name.data,
            last_name = newProfileForm.last_name.data,
            email = newProfileForm.email.data,
            location = newProfileForm.location.data,
            gender = newProfileForm.gender.data,
            biography = newProfileForm.biography.data,
            profilePhoto = filename,
            created_on = format_date_joined(dateFormat.now)
        )
        db.session.add(newUser)
        db.session.commit()
        flash('You have successfully added a new profile.', 'success')
        pictures = getUploadedImages()
        return redirect(url_for('profiles', pictures = pictures))
    return render_template('profile.html', form=form)

@app.route('/profiles')
def profiles():
    profiles = db.session.query(UserProfile).all()
    return render_template('profiles.html', profiles = profiles)

@app.route('/profile/<int:userid>')
def uniqueProfile(userid):
    user = db.session.query(UserProfile).filter_by(id=userid).first()
    return render_template('uniqueProfile.html', user = user)



###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")