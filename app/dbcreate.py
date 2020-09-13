from app import db, students

db.create_all()


test_rec = students(
        'Rodrigo Marcelino',
        'São José',
        '138 Miquelina Adamo',
        '12345'
        )


db.session.add(test_rec)
db.session.commit()
