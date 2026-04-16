import logging
import oracledb
from config import DB_CONFIG

logger = logging.getLogger("db")

def get_connection():
    return oracledb.connect(
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        dsn=DB_CONFIG["dsn"]
    )


def insert_order(order):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO ORDERS (ORDER_ID, CUSTOMER_NAME, AMOUNT)
            VALUES (:1, :2, :3)
        """

        cursor.execute(query, (
            order['order_id'],
            order['customer_name'],
            order['amount']
        ))

        conn.commit()
        logger.info(f"Inserted Order ID: {order['order_id']}")

    except oracledb.IntegrityError:
        logger.warning(f"Duplicate Order ID skipped: {order['order_id']}")

    except Exception as e:
        logger.error(f"DB Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()