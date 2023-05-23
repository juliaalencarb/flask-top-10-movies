from application.database import database_service

db = database_service.instance


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(2048), nullable=True, default="")

    def __repr__(self):
        return self.title
