"""create persons table

Revision ID: 520826c74397
Revises: 
Create Date: 2023-11-07 18:26:53.214872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '520826c74397'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'persons',
        sa.Column('id',sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column('apelido',sa.String, unique=True),
        sa.Column('nome',sa.String),
        sa.Column('nascimento',sa.Date),
        sa.Column('stack',sa.ARRAY(sa.String),nullable=True),
        sa.Column('concatenado',sa.String),
    )

def downgrade() -> None:
    op.drop_table('persons')
