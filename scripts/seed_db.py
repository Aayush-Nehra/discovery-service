from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.models.user import User
from app.models.service import Service
from app.core.security import hash_password


def init_db():
    Base.metadata.create_all(bind=engine)


def seed():
    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            u1 = User(
                email="alice@example.com",
                hashed_password=hash_password("alicepass"),
                is_admin=True,
            )
            u2 = User(email="bob@example.com", hashed_password=hash_password("bobpass"))
            db.add_all([u1, u2])
            db.flush()  # get ids
            s1 = Service(
                name="Joe's Tyres",
                category="tyre",
                description="Puncture repair",
                latitude=12.9716,
                longitude=77.5946,
                owner_id=u1.id,
            )
            db.add(s1)
            db.commit()
            print("Seeded DB")
        else:
            print("DB already seeded")
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
    seed()
