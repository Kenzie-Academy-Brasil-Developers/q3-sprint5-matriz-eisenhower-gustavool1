"""empty message

Revision ID: 21c8ec4fe802
Revises: e986d6ca9568
Create Date: 2022-02-17 17:46:20.894751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c8ec4fe802'
down_revision = 'e986d6ca9568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('eisenhower', sa.Integer(), nullable=False))
    op.drop_constraint('tasks_eisenhower_id_fkey', 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'eisenhowers', ['eisenhower'], ['id'])
    op.drop_column('tasks', 'eisenhower_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('eisenhower_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key('tasks_eisenhower_id_fkey', 'tasks', 'eisenhowers', ['eisenhower_id'], ['id'])
    op.drop_column('tasks', 'eisenhower')
    # ### end Alembic commands ###