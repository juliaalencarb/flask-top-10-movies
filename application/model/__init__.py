from sqlalchemy import text


def init_model(db_instance):
    from application.model.movie import Movie
    try:
        db_instance.create_all()
        movie_1 = Movie(title='Phone Booth', year=2002, description='Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist\'s sniper rifle. Unable to leave or receive outside help, Stuart\'s negotiation with the caller leads to a jaw-dropping climax.', rating=7.3, review='My favourite character was the caller.', img_url='https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg')
        db_instance.session.add(movie_1)
        db_instance.session.commit()
        db_instance.session.close()
    except Exception as e:
        print(e)
