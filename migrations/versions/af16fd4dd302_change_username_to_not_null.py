"""change-username-to-not-null

Revision ID: af16fd4dd302
Revises: 4c7052092665
Create Date: 2023-05-01 13:36:43.745338

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session

from models.user import User

# revision identifiers, used by Alembic.
revision = 'af16fd4dd302'
down_revision = '4c7052092665'
branch_labels = None
depends_on = None


def upgrade() -> None:
    def upgrade() -> None:
        with Session(op.get_bind()) as session:
            user = session.get(User, {"id": 1})
            user.username = "Franta"
            session.commit()

    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
                    existing_type=sa.TEXT(),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
