import simplejson


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def getArrayJson(cursor):
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns,row)) for row in rows]
    return simplejson.dumps(results)


def getDictJson(cursor):
    rows = cursor.fetchall()
    if len(rows) == 1:
        columns = [column[0] for column in cursor.description]
        rs = [dict(zip(columns,row)) for row in rows][0]
    else:
        rs = {}
    return simplejson.dumps(rs)


def getContextPage(request):
    user = request.user
    token = ''
    ispopup = request.GET.get('ispopup', '')
    context = None
    if ispopup == 'true':
        ispopup = True
    else:
        ispopup = False
    if hasattr(user, "auth_token"):
        token = user.auth_token.key
    context = {'username': user.username,
               'fullname': user.first_name,
               'token': token,
               'ispopup': ispopup}
    return context


def getJsonArrayBySql(connection, sql, params):
    json = '[]'
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        rs = cursor.fetchone()
        json = rs[0]
    return json