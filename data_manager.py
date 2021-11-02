from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:
    query = f"""
        SELECT first_name, last_name, city
        FROM mentor
        where last_name = '{last_name}' ORDER BY first_name """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_city(cursor: RealDictCursor, city: str) ->list:
    query = f'''
        SELECT first_name, last_name, city 
        FROM mentor
        where city = '{city}' ORDER BY first_name'''
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant(cursor: RealDictCursor, applicant: str) ->list:
    query = f'''
        SELECT first_name, last_name, phone_number
        FROM applicant
        where first_name = '{applicant}' or last_name = '{applicant}'
        ORDER BY first_name'''
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_by_email(cursor:RealDictCursor, email_part:str) ->list:
    query = f'''
        select  first_name, last_name, phone_number
        FROM applicant
        WHERE email LIKE '%{email_part}%'
        ORDER BY first_name  '''
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_all_applicants(cursor):
    query = f'''
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant
        ORDER BY first_name'''
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_specific_applicant(cursor:RealDictCursor, code):
    query = f'''
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant
        WHERE application_code = {code}
        '''
    cursor.execute(query)
    return cursor.fetchall()



@database_common.connection_handler
def update_applicant_phone_number(cursor, phone_number, code):
    query = f'''
        UPDATE applicant
        SET phone_number = '{phone_number}'
        WHERE {code} = application_code '''
    cursor.execute(query)


@database_common.connection_handler
def delete_applicant(cursor, code):
    query = f'''
    DELETE FROM applicant
    WHERE {code} = application_code'''
    cursor.execute(query)


@database_common.connection_handler
def delete_applicant_by_email(cursor, part_of_email):
    query = f'''
    DELETE FROM applicant
    WHERE email LIKE '%{part_of_email}%'
    '''
    cursor.execute(query)


@database_common.connection_handler
def add_new_applicant(cursor, a_inf):
    query =  f'''
    INSERT INTO applicant 
    (first_name, last_name, phone_number, email, application_code) 
    VALUES('{a_inf[0]}', '{a_inf[1]}', '{a_inf[2]}', '{a_inf[3]}', {a_inf[4]})
    '''
    cursor.execute(query)

