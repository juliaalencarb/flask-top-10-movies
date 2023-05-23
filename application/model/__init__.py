from sqlalchemy import text


def init_model(db_instance):
    try:
        db_instance.create_all()
        db_instance.session.execute(text(
            "INSERT INTO movies(title, year, description, rating, ranking, review, img_url) "
            "VALUES('Phone Booth', 2002,'Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down "
            "by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the "
            "caller leads to a jaw-dropping climax.', 7.3, 10, 'My favourite character was the caller.', "
            "'https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg');"))

        db_instance.session.commit()
        db_instance.session.close()
    except Exception as e:
        print(e)
