import sys
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, mapped_column, Mapped

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product: Mapped[str] = mapped_column(String(50), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)

    def __repr__(self):
        return f"<Order(product='{self.product}, price='{self.price}, status='{self.status}')>"


def run_sqlachemy():
    print("1. Initialzing SQLAlchemy Engine")
    engine = create_engine("sqlite:///:memory:", echo=False)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    print("2. [Insering rows]")
    order1 = Order(
        product="Laptop", category="Electronics", price=1200.0, status="completed"
    )
    order2 = Order(
        product="Phone", category="Electronics", price=800.0, status="completed"
    )
    order3 = Order(product="Shirt", category="Apparel", price=40.0, status="completed")
    order4 = Order(product="Chair", category="Furniture", price=150.0, status="pending")

    session.add_all([order1, order2, order3, order4])

    session.commit()
    print("Successfully inserted 4 rows")

    print("3. [Reading completed rows]")

    completed_orders = session.query(Order).filter(Order.status == "completed").all()

    for order in completed_orders:
        print(f"   - {order.product} (${order.price})")

    print("4. [Updating pending to completed]")

    chair_order = session.query(Order).filter(Order.product == "Chair").first()
    if chair_order:
        chair_order.status = "completed"
        session.commit()
        print("Database updated!")

    print("5. [Deleting Rows from the DB]")

    apparel_to_delete = session.query(Order).filter(Order.category == "Apparel").all()

    for item in apparel_to_delete:
        session.delete(item)

    session.commit()
    print("Deleted Rows successfully!")

    print("\n[READ] Remaining items in SQL table:")
    remaining_rows = session.query(Order).all()
    for row in remaining_rows:
        print(f"   - {row.product} ({row.category}) - Status: {row.status}")

    session.close()


run_sqlachemy()
"""
O/P:
1. Initialzing SQLAlchemy Engine
2. [Insering rows]
Successfully inserted 4 rows
3. [Reading completed rows]
   - Laptop ($1200.0)
   - Phone ($800.0)
   - Shirt ($40.0)
4. [Updating pending to completed]
Database updated!
5. [Deleting Rows from the DB]
Deleted Rows successfully!

[READ] Remaining items in SQL table:
   - Laptop (Electronics) - Status: completed
   - Phone (Electronics) - Status: completed
   - Chair (Furniture) - Status: completed
"""