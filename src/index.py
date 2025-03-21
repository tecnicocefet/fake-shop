import uuid
from flask import Flask, flash, make_response, redirect, render_template, request, url_for
import os
from models.order import Order, OrderItem
from models.product import Product
from models.base import db
from flask_migrate import Migrate, upgrade
import random
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.secret_key = 'supersecretkey'  # Para manter a sessão

metrics = GunicornPrometheusMetrics(app)
metrics.register_endpoint('/metrics')

# Configuração do banco de dados
db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'ecommerce')
db_password = os.getenv('DB_PASSWORD', 'Pg1234')
db_name = os.getenv('DB_NAME', 'ecommerce')
db_port = os.getenv('DB_PORT', 5432)

db_url = f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Inicializar SQLAlchemy e Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

def generate_order_number():
    """Gera um número de pedido único com 6 dígitos."""
    return f'{random.randint(100000, 999999)}'

def apply_migrations():
    """Aplicar migrations automaticamente."""
    with app.app_context():
        try:
            upgrade()  # Aplicar todas as migrations pendentes
            print("Migrations applied successfully.")
        except Exception as e:
            print(f"Error applying migrations: {e}")

def check_db_connection():
    """Verifica se a aplicação consegue se conectar ao banco de dados."""
    with app.app_context():
        try:
            db.engine.connect()
            print("Conexão com o banco de dados estabelecida com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise e

@app.before_first_request
def initialize_app():
    """Inicializa a aplicação e aplica as migrações."""
    check_db_connection()
    apply_migrations()

# Rotas da aplicação (mantidas como estão)
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/checkout', methods=['GET'])
def checkout_get():
    # Obtém o pedido pelo cookie
    order = get_order_from_cookie()

    if not order or not order.items:
        flash("Seu carrinho está vazio. Adicione produtos antes de prosseguir para o checkout.", "warning")
        return redirect(url_for('shop'))

    items = order.items  # Carrega os itens do pedido
    subtotal = sum(item.quantity * item.product.price for item in items)
    total = subtotal + 10  # Valor fixo de envio, por exemplo

    return render_template('checkout.html', items=items, subtotal=subtotal, total=total)

# ... (restante das rotas)

if __name__ == '__main__':
    #apply_migrations()
    app.run(host='0.0.0.0', port=5000, debug=True)