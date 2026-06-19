from sqlalchemy import or_, select

from brave.api.models.core import t_container_template


def find_container_template_by_id(conn, template_id):
    stmt = select(t_container_template).where(
        or_(
            t_container_template.c.id == template_id,
            t_container_template.c.id == str(template_id),
        )
    )
    return conn.execute(stmt).mappings().first()
