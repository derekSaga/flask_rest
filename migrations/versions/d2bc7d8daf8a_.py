"""empty message

Revision ID: d2bc7d8daf8a
Revises: 53529d9a4060
Create Date: 2020-07-15 14:32:52.952885

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2bc7d8daf8a'
down_revision = '53529d9a4060'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tarefa', sa.Column('projeto_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tarefa', 'projeto', ['projeto_id'], ['id'])
    op.drop_column('tarefa', 'data_registro')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tarefa', sa.Column('data_registro', mysql.DATETIME(), nullable=True))
    op.drop_constraint(None, 'tarefa', type_='foreignkey')
    op.drop_column('tarefa', 'projeto_id')
    # ### end Alembic commands ###
