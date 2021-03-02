"""empty message

Revision ID: d554b6d4fc4a
Revises: 
Create Date: 2020-11-26 09:31:44.825333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd554b6d4fc4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    op.drop_table('iphonecategory')
    op.drop_table('ab_permission_view_role')
    op.drop_table('supportcategory')
    op.drop_table('appletv')
    op.drop_table('news_category')
    op.drop_table('menu_category')
    op.drop_table('menu_item')
    op.drop_table('benefit')
    op.drop_table('ab_user')
    op.drop_table('applemusic')
    op.drop_table('ipadcategory')
    op.drop_table('applemac')
    op.drop_table('ab_permission')
    op.drop_table('applewc')
    op.drop_table('applesupport')
    op.drop_table('ab_register_user')
    op.drop_table('appleipad')
    op.drop_table('cardscategory')
    op.drop_table('benefits_employee')
    op.drop_table('maccategory')
    op.drop_table('department')
    op.drop_table('applecards')
    op.drop_table('ab_permission_view')
    op.drop_table('appleiphone')
    op.drop_table('employee')
    op.drop_table('function')
    op.drop_table('tvcategory')
    op.drop_table('country')
    op.drop_table('ab_user_role')
    op.drop_table('musiccategory')
    op.drop_table('wcategory')
    op.drop_table('ab_role')
    op.drop_table('ab_view_menu')
    op.drop_table('employee_history')
    op.drop_table('gender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gender',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('employee_history',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('department_id', sa.INTEGER(), nullable=False),
    sa.Column('employee_id', sa.INTEGER(), nullable=False),
    sa.Column('begin_date', sa.DATE(), nullable=True),
    sa.Column('end_date', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_view_menu',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ab_role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('wcategory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('musiccategory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_user_role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('role_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['ab_role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'role_id')
    )
    op.create_table('country',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tvcategory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('function',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('employee',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('address', sa.TEXT(length=250), nullable=False),
    sa.Column('fiscal_number', sa.INTEGER(), nullable=False),
    sa.Column('employee_number', sa.INTEGER(), nullable=False),
    sa.Column('department_id', sa.INTEGER(), nullable=False),
    sa.Column('function_id', sa.INTEGER(), nullable=False),
    sa.Column('begin_date', sa.DATE(), nullable=True),
    sa.Column('end_date', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.ForeignKeyConstraint(['function_id'], ['function.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appleiphone',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['iphonecategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_permission_view',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('permission_id', sa.INTEGER(), nullable=True),
    sa.Column('view_menu_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['ab_permission.id'], ),
    sa.ForeignKeyConstraint(['view_menu_id'], ['ab_view_menu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('permission_id', 'view_menu_id')
    )
    op.create_table('applecards',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['cardscategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('maccategory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('benefits_employee',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('benefit_id', sa.INTEGER(), nullable=True),
    sa.Column('employee_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['benefit_id'], ['benefit.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cardscategory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appleipad',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['ipadcategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_register_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=256), nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('registration_date', sa.DATETIME(), nullable=True),
    sa.Column('registration_hash', sa.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('applesupport',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['supportcategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applewc',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['wcategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_permission',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('applemac',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['maccategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ipadcategory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applemusic',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['musiccategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=256), nullable=True),
    sa.Column('active', sa.BOOLEAN(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_login', sa.DATETIME(), nullable=True),
    sa.Column('login_count', sa.INTEGER(), nullable=True),
    sa.Column('fail_login_count', sa.INTEGER(), nullable=True),
    sa.Column('created_on', sa.DATETIME(), nullable=True),
    sa.Column('changed_on', sa.DATETIME(), nullable=True),
    sa.Column('created_by_fk', sa.INTEGER(), nullable=True),
    sa.Column('changed_by_fk', sa.INTEGER(), nullable=True),
    sa.CheckConstraint('active IN (0, 1)'),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('benefit',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('menu_item',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('link', sa.VARCHAR(length=150), nullable=False),
    sa.Column('menu_category_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['menu_category_id'], ['menu_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu_category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appletv',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['tvcategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supportcategory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_permission_view_role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('permission_view_id', sa.INTEGER(), nullable=True),
    sa.Column('role_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['permission_view_id'], ['ab_permission_view.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['ab_role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('permission_view_id', 'role_id')
    )
    op.create_table('iphonecategory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('newsCat_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['newsCat_id'], ['news_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
