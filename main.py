from application import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

# TODO 1: Create SQLite db.
# TODO 2: Create Movie model containing: id, title, year, description, rating, ranking, review, img_url.
# TODO 3: Insert data into the table.
# TODO 4: Each entry on the db should be displayed on home page. The component should be a card that has image and
#  ranking on the front and on click it flips and has title, year, rating, review, description on the back.
