from brave.api.models.core import go_file


def find_by_ids(conn, ids):
    stmt = go_file.select().where(go_file.c.id.in_(ids))
    return conn.execute(stmt).mappings().all()


def find_by_file_id(conn, file_id):
    stmt = go_file.select().where(go_file.c.id == file_id)
    return conn.execute(stmt).mappings().first()
