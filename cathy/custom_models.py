from django.db import connection


def registered_users():
    with connection.cursor() as cursor:
        cursor = cursor.callproc('f_dash_number_of_cattle', [])
        row = cursor.fetchOne()
        return row
