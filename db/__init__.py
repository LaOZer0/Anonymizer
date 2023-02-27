from .fake import init_db, con


def generate_fake_database():
    init_db()


count = 0


def add_row(user):
    global count
    """
    Create a new user into the users table
    :param user:
    """
    try:
        sql = '''
        INSERT INTO users(firstname,middlename,lastname,sex,snils)
                  VALUES(?,?,?,?,?) '''
        cur = con.cursor()
        cur.execute(sql, user)
        con.commit()
    except Exception:
        print("Снилс не уникален, ", count)
        count += 1
