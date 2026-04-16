def validate_order(data):
    required_fields = ['order_id', 'customer_name', 'amount']

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    return True