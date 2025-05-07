GET_ALL_USERS = """
    SELECT id, name FROM users
"""

GET_USER_BY_ID = """
    SELECT id, name FROM users WHERE id = ?
"""

INSERT_INTO_USERS = """
    INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)
"""

UPDATE_USER_BY_ID = """
    UPDATE users SET name = ?, email = ?, password_hash = ? WHERE id = ?
"""

UPDATE_USER_BY_ID_NO_PASSWORD = """
    UPDATE users SET name = ?, email = ? WHERE id = ?
"""

DELETE_USER_BY_ID = """
    DELETE FROM users WHERE id = ?
"""