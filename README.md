# Multi-Currency Invoice Analytics API

## Overview

This project provides an API to handle customer invoices in multiple currencies, converts the invoice amounts into a standard currency (USD), and provides analytics such as total revenue, and average invoice size.

It is built with **Django** and the **Django REST Framework** and uses **PostgreSQL** as the database. A third-party exchange rate API (ExchangeRate-API) is used for currency conversion.

## Features

- **Create, Retrieve, Update, and Delete invoices**.
- **Support for multiple currencies**.
- **Automatic conversion of invoice amounts to USD** using real-time exchange rates.
- **Analytics**: Total revenue, and average invoice size.

## Requirements

- Python 3.8+
- Django 3.2+
- PostgreSQL
- Django REST Framework
- ExchangeRate-API

## Installation

1. **Clone the repository**:
    
    ```bash
    git clone https://github.com/yourusername/invoice-analytics-api.git
    cd invoice-analytics-api
    ```
    
2. **Create a virtual environment** and activate it:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
    
3. **Install the dependencies**:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Set up PostgreSQL**:
    - Install PostgreSQL and create a database for the project.
    - Configure the `DATABASES` setting in `settings.py` to use PostgreSQL:
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
    
5. **Set up environment variables**:
    - Create a `.env` file in the project root for sensitive information like the `SECRET_KEY`, `DATABASE_URL`, and API keys (e.g., ExchangeRate-API key).
    
    Example `.env` file:
    
    ```bash
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/invoice_db
    EXCHANGE_RATE_API_KEY=your_api_key
    ```
    
6. **Apply database migrations**:
    
    ```bash
    python manage.py migrate
    ```
    
7. **Create a superuser** (optional, for admin access):
    
    ```bash
    python manage.py createsuperuser
    ```
    
8. **Run the development server**:
    
    ```bash
    python manage.py runserver
    ```
    

## API Endpoints

### Invoice Endpoints

- `POST /api/invoices/`: Create a new invoice.
- `GET /api/invoices/`: Retrieve all invoices.
- `GET /api/invoices/{id}/`: Retrieve a specific invoice by ID.
- `PUT /api/invoices/{id}/`: Update an existing invoice.
- `DELETE /api/invoices/{id}/`: Delete an invoice.

### Analytics Endpoints

- `GET /api/analytics/revenue/`: Get the total revenue in USD.
- `GET /api/analytics/average/`: Get the average invoice size.

### Currency Endpoints

- `GET /api/currency/{id}/exchange/`: Get the exchange rate of an invoice.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### Notes:

1. You can add or remove sections based on your project.
2. Ensure to replace placeholders like `yourusername`, `your-app-name`, and `your-db-name` with actual values specific to your project.
