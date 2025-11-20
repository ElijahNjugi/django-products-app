# Django Products App

This project is a simple Django application created for a class assignment.  
It demonstrates how to:

- Create a `Product` model with image support
- Link products to categories
- Insert and display products
- Register models in the Django admin
- Render product listings in templates
- Display a Product Detail page

## Features

- View all products
- Add a new product with an image
- View individual product details
- Products are categorized
- Images are uploaded and displayed in the app

## Requirements

- Python 3.10+ (recommended)
- Django 5.2.8
- Pillow (for image uploads)
- Virtual environment recommended

## Installation

1. Clone the repository:
```bash
git clone <your-repo-link>
cd django-products-app

python -m venv venv
# Windows
venv\Scripts\activate

pip install -r requirements.txt

Apply migrations:

python manage.py migrate


Create a superuser (optional, for admin access):

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Access the app in your browser at:

http://127.0.0.1:8000/products/all/


Note: Images uploaded will be stored in the media/ folder. Make sure this folder exists before adding products.

Usage
Visit /products/all/ to see all products.
Click "Add New Product" to create a new product.
Click "View Details" to see more information about a produ