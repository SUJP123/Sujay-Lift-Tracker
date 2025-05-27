import uvicorn
from backend.scripts.create_db import create_db
from backend.scripts.user_scripts import add_route_user
from backend.app import app
from backend.test.user_test import test_root_user_is_added
from backend.database.db import get_session
from backend.service.UserService import UserService


if __name__ == "__main__":
    create_db()
    session = next(get_session())
    add_route_user(session)

    # Temporary Test
    user_svc = UserService()
    test_root_user_is_added(user_svc)
    uvicorn.run(app, host="0.0.0.0", port=8000)
