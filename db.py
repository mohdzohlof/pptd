import MySQLdb

conn = None
cur = None


def init_db(db, host="localhost", user="root", passw=""):
    global conn, cur
    conn = MySQLdb.connect(host=host, user=user, passwd=passw, db=db)
    cur = conn.cursor()


def create_user(email, password, first_name, last_name):
    query = """INSERT INTO account (email, password, admin, first_name, last_name) VALUES ('{email}', '{password}',
     {admin}, '{first_name}', '{last_name}')""".format(email=email, password=password, admin=0, first_name=first_name,
                                                       last_name=last_name)

    cur.execute(query)

    conn.commit()


def get_user(email, passw):
    query = "SELECT email FROM account WHERE email='{}' AND password='{}'".format(email, passw)

    res = cur.execute(query)

    if res is None:
        return None
    else:
        return cur.fetchone()[0]


def get_users_by_org(org_id):
    query = "SELECT email FROM account WHERE org_id='{org_id}'".format(org_id=org_id)

    cur.execute(query)

    res = cur.fetchall()

    result = [user[0] for user in res]

    return result


def get_password(email):
    query = "SELECT password FROM account WHERE email='{email}'".format(email=email)

    cur.execute(query)

    return cur.fetchone()[0]


def get_org_id(email):
    query = "SELECT org_id FROM account WHERE email='{email}'".format(email=email)

    cur.execute(query)

    return cur.fetchone()[0]


def get_org_by_name(org_name):
    query = "SELECT id, name, password FROM organization WHERE name='{name}'".format(name=org_name)

    cur.execute(query)

    return cur.fetchone()


def get_org_by_id(org_id):
    query = "SELECT id, name, password FROM organization WHERE id='{id}'".format(id=org_id)

    cur.execute(query)

    return cur.fetchone()


def is_admin(email):
    query = "SELECT admin FROM account WHERE email='{email}'".format(email=email)

    cur.execute(query)

    admin = cur.fetchone()[0]
    if admin == 0:
        return False
    else:
        return True


def update_password(email, password):
    query = "UPDATE account SET password='{password}' WHERE email='{email}'".format(password=password, email=email)

    cur.execute(query)

    conn.commit()


def update_organization(email, org_id):
    query = "UPDATE account SET org_id = '{id}' WHERE email='{email}'".format(id=org_id, email=email)

    cur.execute(query)

    conn.commit()


def update_org_password(org_id, password):
    query = "UPDATE organization SET password='{password}' WHERE id='{id}'".format(id=org_id, password=password)

    cur.execute(query)

    conn.commit()


def remove_user_org(email):
    query = "UPDATE account SET org_id=Null WHERE email='{email}'".format(email=email)

    cur.execute(query)

    conn.commit()
