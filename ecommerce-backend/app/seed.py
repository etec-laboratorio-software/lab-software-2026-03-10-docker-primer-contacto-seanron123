from app.database import SessionLocal, engine, Base
from app.models.models import Category, Product
from app.models.order import Order, OrderItem

# Crear todas las tablas si no existen
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Limpiar datos en orden correcto (primero los que tienen foreign keys)
db.query(OrderItem).delete()
db.query(Order).delete()
db.query(Product).delete()
db.query(Category).delete()
db.commit()

# Crear categorías de ejemplo
categories = [
    Category(name="Ropa"),
    Category(name="Zapatos"),
    Category(name="Accesorios")
]
db.add_all(categories)
db.commit()

ropa = db.query(Category).filter_by(name="Ropa").first()
zapatos = db.query(Category).filter_by(name="Zapatos").first()
accesorios = db.query(Category).filter_by(name="Accesorios").first()

# Crear productos de ejemplo
products = [
    Product(name="Remera Básica", description="Remera de algodón", price=19.99, stock=50, category_id=ropa.id),
    Product(name="Zapatillas Deportivas", description="Cómodas y ligeras", price=79.99, stock=30, category_id=zapatos.id),
    Product(name="Gorra", description="Gorra unisex", price=15.00, stock=20, category_id=accesorios.id)
]
db.add_all(products)
db.commit()
db.close()

print("¡Datos de prueba agregados correctamente!")
