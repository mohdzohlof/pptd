import MySQLdb

conn = None


def init_db(db, host="localhost", user="root", passw=""):
    global conn
    conn = MySQLdb.connect(host=host, user=user, passwd=passw, db=db)


def get_password(email):
    cur = conn.cursor()

    query = "SELECT password FROM account WHERE email='{email}'".format(email=email)
    cur.execute(query)

    return cur.fetchone()[0]


def get_org_id(email):
    cur = conn.cursor()

    query = "SELECT org_id FROM account WHERE email='{email}'".format(email=email)

    cur.execute(query)

    return cur.fetchone()[0]


def get_org_by_name(org_name):
    cur = conn.cursor()

    query = "SELECT id, name, password FROM organization WHERE name='{name}'".format(name=org_name)

    cur.execute(query)

    return cur.fetchone()


def get_org_by_id(org_id):
    cur = conn.cursor()

    query = "SELECT id, name, password FROM organization WHERE id='{id}'".format(id=org_id)

    cur.execute(query)

    return cur.fetchone()


def is_admin(email):
    cur = conn.cursor()

    query = "SELECT admin FROM account WHERE email='{email}'".format(email=email)

    cur.execute(query)

    admin = cur.fetchone()[0]
    if admin == 0:
        return False
    else:
        return True


def update_password(email, password):
    cur = conn.cursor()

    query = "UPDATE account SET password='{password}' WHERE email='{email}'".format(password=password, email=email)

    cur.execute(query)

    conn.commit()


def update_organization(email, org_id):
    cur = conn.cursor()

    query = "UPDATE account SET org_id = '{id}' WHERE email='{email}'".format(id=org_id, email=email)

    cur.execute(query)

    conn.commit()
