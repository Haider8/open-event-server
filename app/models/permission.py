from app.models import db

from app.models.base import SoftDeletionModel


class Permission(SoftDeletionModel):
    """Role-Service Permissions
    """

    __tablename__ = 'permissions'
    __table_args__ = (
        db.UniqueConstraint(
            'role_id', 'service_id', 'deleted_at', name='role_service_deleted_at_uc'
        ),
    )

    id = db.Column(db.Integer, primary_key=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))
    role = db.relationship('Role')

    service_id = db.Column(db.Integer, db.ForeignKey('services.id', ondelete='CASCADE'))
    service = db.relationship('Service')

    can_create = db.Column(db.Boolean, nullable=False, default=True)
    can_read = db.Column(db.Boolean, nullable=False, default=True)
    can_update = db.Column(db.Boolean, nullable=False, default=True)
    can_delete = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return '<Perm %r for %r>' % (self.role, self.service,)
