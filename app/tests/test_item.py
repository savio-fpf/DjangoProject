# app/tests/test_item.py
import pytest
from django.urls import reverse
from app.models import Item

@pytest.mark.django_db
class TestItemCRUD:
    @pytest.fixture(autouse=True)
    def init_items(self):
        # Popula o banco com um item de exemplo
        Item.objects.create(name="Item1", description="Descrição 1")

    def test_item_listagem(self, client):
        url = reverse('item_list')
        response = client.get(url)
        assert response.status_code == 200
        assert b"Item1" in response.content

    def test_criar_item(self, client):
        url = reverse('item_create')
        # envia um POST para criar um novo item
        response = client.post(url, {'name': 'NovoItem', 'description': 'Desc Novo'})
        assert response.status_code == 302  # redireciona para a lista
        assert Item.objects.filter(name="NovoItem").exists()

    def test_editar_item(self, client):
        item = Item.objects.first()
        url = reverse('item_update', args=[item.pk])
        response = client.post(url, {'name': 'ItemEditado', 'description': 'Desc Edit'})
        assert response.status_code == 302
        item.refresh_from_db()
        assert item.name == "ItemEditado"

    def test_deletar_item(self, client):
        item = Item.objects.first()
        url = reverse('item_delete', args=[item.pk])
        response = client.post(url)
        assert response.status_code == 302
        assert Item.objects.count() == 0
