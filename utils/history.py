import sqlite3


def save_query(query):

    conn = sqlite3.connect(
        "healthcare.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(query)
        VALUES(?)
        """,
        (query,)
    )

    conn.commit()

    conn.close()