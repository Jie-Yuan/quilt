"""empty message

Revision ID: 49843796aadf
Revises: 
Create Date: 2017-01-25 15:23:52.082295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49843796aadf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('package',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('owner', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_package', 'package', ['owner', 'name'], unique=True)
    op.create_table('version',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('package_id', sa.BigInteger(), nullable=True),
    sa.Column('hash', sa.String(length=128), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['package_id'], ['package.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_version_hash'), 'version', ['hash'], unique=False)
    op.create_table('tag',
    sa.Column('package_id', sa.BigInteger(), nullable=False),
    sa.Column('tag', sa.String(length=64), nullable=False),
    sa.Column('version_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['package_id'], ['package.id'], ),
    sa.ForeignKeyConstraint(['version_id'], ['version.id'], ),
    sa.PrimaryKeyConstraint('package_id', 'tag')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    op.drop_index(op.f('ix_version_hash'), table_name='version')
    op.drop_table('version')
    op.drop_index('idx_package', table_name='package')
    op.drop_table('package')
    # ### end Alembic commands ###
