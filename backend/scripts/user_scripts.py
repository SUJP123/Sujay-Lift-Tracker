from backend.entity.UserEntity import UserEntity
from backend.model.User import Role, User
from sqlalchemy.orm import Session


def add_route_user(session: Session):
    root_user = User(id=1, first_name='Sujay', last_name='Patel', role=Role.ROOT)
    root_entity = UserEntity().model_to_entity(root_user)
    session.add(root_entity)
    session.commit()