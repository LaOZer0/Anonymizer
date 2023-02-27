from .fake import init_db, con


def generate_fake_database():
    init_db()


def add_row(user):
    """
    Create a new user into the users table
    :param user:
    """
    sql = ''' INSERT INTO users(firstname,middlename,lastname,sex,snils,email)
              VALUES(?,?,?,?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, user)
    con.commit()
