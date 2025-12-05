from django.core.management.base import BaseCommand
from products.models import Product
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Create sample products'
    
    def handle(self, *args, **kwargs):
        products = [
            {
                'name': 'Ноутбук Dell XPS 13',
                'description': 'Потужний ноутбук з екраном 13.3 дюйма, процесором Intel Core i7 та 16 ГБ оперативної пам\'яті. Ідеальний для роботи та розваг.',
                'price': Decimal('34999.99'),
            },
            {
                'name': 'Смартфон Samsung Galaxy S23',
                'description': 'Флагманський смартфон з потрійною камерою, екраном Dynamic AMOLED 2X та потужним акумулятором.',
                'price': Decimal('28999.50'),
            },
            {
                'name': 'Навушники Sony WH-1000XM5',
                'description': 'Бездротові навушники з активним шумозаглушенням, чудовою якістю звуку та тривалим часом роботи від акумулятора.',
                'price': Decimal('12999.00'),
            },
            {
                'name': 'Фотоапарат Canon EOS R6',
                'description': 'Дзеркальний фотоапарат з повнокадровим сенсором, швидкою автофокусуванням та можливістю зйомки 4K відео.',
                'price': Decimal('75999.00'),
            },
            {
                'name': 'Планшет Apple iPad Pro',
                'description': 'Потужний планшет з дисплеєм Liquid Retina XDR, чипом M2 та підтримкою Apple Pencil другого покоління.',
                'price': Decimal('45999.00'),
            },
            {
                'name': 'Смарт-годинник Apple Watch Series 9',
                'description': 'Розумний годинник з функціями моніторингу здоров\'я, GPS та підтримкою cellular зв\'язку.',
                'price': Decimal('18999.00'),
            },
            {
                'name': 'Монітор LG UltraGear',
                'description': 'Ігровий монітор з частотою оновлення 240 Гц, роздільною здатністю 2K та технологією NVIDIA G-Sync.',
                'price': Decimal('21999.00'),
            },
            {
                'name': 'Клавітура Logitech MX Keys',
                'description': 'Ергономічна бездротова клавіатура з підсвічуванням, мультидевайсовою підтримкою та довгим часом роботи від акумулятора.',
                'price': Decimal('4599.00'),
            },
        ]
        
        for i, product_data in enumerate(products):
            created_at = timezone.now() - timedelta(days=i*2)
            Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                created_at=created_at
            )
            self.stdout.write(self.style.SUCCESS(f'Створено продукт: {product_data["name"]}'))
        
        self.stdout.write(self.style.SUCCESS('Успішно створено тестові продукти!'))