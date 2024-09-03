import psycopg2
import config
from collections import namedtuple
from psycopg2 import errors
from psycopg2 import sql

UserInfo = namedtuple(
    "FoodInfo",
    [
        "id",
        "email",
        "password",
    ],
)


def create_user(email, password, conn, cursor):
    try:
        insert_query = sql.SQL(
            """
            INSERT INTO users (email, password)
            VALUES (%s, %s)
            RETURNING id, created_at;
        """
        )

        cursor.execute(insert_query, (email, password))

        user_id, created_at = cursor.fetchone()

        conn.commit()

        return f"Usuário criado com email '{email}'"

    except errors.UniqueViolation as e:
        print(f"O email '{email}' já existe no sistema. Insira um novo e-mail")
        if conn:
            conn.rollback()  # Rollback in case of an error
    except psycopg2.Error as e:
        print(f"Error: {e}")
        if conn:
            conn.rollback()  # Rollback in case of an error
    # finally:
    #     if cursor:
    #         cursor.close()
    #     if conn:
    #         conn.close()


def update_user(email, current_password, new_password1, new_password2, conn, cursor):
    if new_password1 != new_password2:
        return "As senhas fornecidas não coincidem. Tente novamente"

    try:
        # Prepare the SELECT statement
        select_query = """
            SELECT id, email, password, created_at
            FROM users
            WHERE email = %s AND password = %s;
        """

        # Execute the SELECT statement
        cursor.execute(select_query, (email, current_password))

        # Fetch the result
        user = cursor.fetchone()

        if not user:
            return f"Não foi encontrado nenhum usuário com o email '{email}' e a senha fornecida. Tente novamente"

        # Prepare the UPDATE statement
        update_query = """
            UPDATE users
            SET password = %s, created_at = CURRENT_TIMESTAMP
            WHERE email = %s
            RETURNING id, email, created_at;
        """

        # Execute the UPDATE statement
        cursor.execute(update_query, (new_password1, email))

        updated_user = cursor.fetchone()

        conn.commit()

        if updated_user:
            return "Senha do usuário atualizada com sucesso!"

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return None
    # finally:
    #     if cursor:
    #         cursor.close()
    #     if conn:
    #         conn.close()


import psycopg2
from psycopg2 import sql


def delete_user(email, password, conn, cursor):
    try:

        # Prepare the DELETE statement
        delete_query = """
            DELETE FROM users
            WHERE email = %s AND password = %s
            RETURNING id, email, created_at;
        """

        # Execute the DELETE statement
        cursor.execute(delete_query, (email, password))

        deleted_user = cursor.fetchone()

        conn.commit()

        if deleted_user:
            print(f"Usuário com email {email} foi removido com sucesso.")
            return deleted_user
        else:
            print(f"Não foi encontrado um usuário com o email {email}")
            return None

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
        return None
    # finally:
    #     if cursor:
    #         cursor.close()
    #     if conn:
    #         conn.close()


def read_user(email, password):
    try:
        conn, cursor = config.connect()

        select_query = """
            SELECT id, email, password
            FROM users
            WHERE email = %s AND password = %s;
        """

        cursor.execute(select_query, (email, password))

        user = cursor.fetchone()

        if not user:
            return None

        return UserInfo(*user)

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return None
    # finally:
    #     if cursor:
    #         cursor.close()
    #     if conn:
    #         conn.close()
