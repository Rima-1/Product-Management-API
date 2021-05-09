from settings import *
from sqlalchemy.sql import exists
from werkzeug.utils import secure_filename
import json
import base64

# Initializing our database
db = SQLAlchemy(app)


# the class Movie will inherit the db.Model of SQLAlchemy
class Art(db.Model):
    __tablename__ = 'art'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    year = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(80), nullable=False)
    synopsis = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)

    def json(self):
        return {'Art ID': self.id, 'Art Title': self.title,
                'Year': self.year, 'Category': self.category, 'Price': self.price, 'Description': self.synopsis, 'Image': self.img}
        # this method we are defining will convert our output to json

    def add_art(_title, _year, _category, _price, _synopsis, _img):
        """function to add movie to database using _title, _year, _genre
        as parameters"""
        # creating an instance of our Movie constructor
        new_art = Art(title=_title, year=_year, category=_category, price=_price, synopsis=_synopsis, img=_img)
        exists = db.session.query(
            db.session.query(Art).filter_by(title=_title).exists()
        ).scalar()
        if exists == False:
            db.session.add(new_art)  # add new movie to database session
            db.session.commit()  # commit changes to session
            return 1
        else:
            return 0

    def get_all_art():
        """function to get all movies in our database"""
        return [Art.json(art) for art in Art.query.all()]

    def get_art(_id):
        """function to get movie using the id of the movie as parameter"""
        try:
            return [Art.json(Art.query.filter_by(id=_id).first())]
        except:
            return 0
        # Movie.json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned

    def update_art(_id, _title, _year, _category):
        """function to update the details of a movie using the id, title,
        year and genre as parameters"""
        try:
            art_to_update = Art.query.filter_by(id=_id).first()
            art_to_update.title = _title
            art_to_update.year = _year
            art_to_update.category = _category
            db.session.commit()
            return 1
        except:
            return 0

    def delete_art(_id):
        """function to delete a movie from our database using
           the id of the movie as a parameter"""
        art_to_delete = Art.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # committing the new change to our database
        return art_to_delete
