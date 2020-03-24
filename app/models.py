from . import db

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    location = db.Column(db.String(150))
    gender = db.Column(db.String(7))
    biography = db.Column(db.String(1000))
    profilePhoto = db.Column(db.String(80))
    created_on = db.Column(db.String(40))

    def __init__(self, first_name, last_name, email, location, gender, biography, profilePhoto, created_on):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.gender = gender
        self.biography = biography
        self.profilePhoto = profilePhoto
        self.created_on = created_on

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)
    
    def __repr__(self):
        return '<User %r' % (self.first_name)