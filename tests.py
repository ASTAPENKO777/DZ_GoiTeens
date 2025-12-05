from django.test import TestCase
from django.urls import reverse
from .models import Product
from decimal import Decimal

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Тестовий товар',
            description='Тестовий опис товару',
            price=Decimal('1000.00')
        )
    
    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Тестовий товар')
        self.assertEqual(self.product.price, Decimal('1000.00'))
        self.assertTrue(self.product.created_at)
    
    def test_product_str(self):
        self.assertEqual(str(self.product), 'Тестовий товар')

class ProductViewTest(TestCase):
    def setUp(self):
        for i in range(8):
            Product.objects.create(
                name=f'Товар {i+1}',
                description=f'Опис товару {i+1}',
                price=Decimal(f'{1000 + i*100}.00')
            )
    
    def test_product_list_view(self):
        response = self.client.get(reverse('products:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/list.html')
        self.assertContains(response, 'Товар 1')
    
    def test_product_list_pagination(self):
        response = self.client.get(reverse('products:product_list'))
        self.assertEqual(len(response.context['products']), 4) 
        
        response = self.client.get(reverse('products:product_list') + '?page=2')
        self.assertEqual(len(response.context['products']), 4)  
    
    def test_product_detail_view(self):
        product = Product.objects.first()
        response = self.client.get(reverse('products:product_detail', args=[product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/detail.html')
        self.assertContains(response, product.name)
    
    def test_product_detail_404(self):
        response = self.client.get(reverse('products:product_detail', args=[999]))
        self.assertEqual(response.status_code, 404)