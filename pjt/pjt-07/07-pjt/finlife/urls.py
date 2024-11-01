from django.urls import path
from . import views

app_name = 'finlife'
urlpatterns = [
    path('', views.index, name='index'),
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'), # 정기 예금 상품 목록 DB에 저장
    path('deposit-products/', views.deposit_products, name='deposit_products'), # 전체 정기 예금 상품 출력 / 데이터 삽입
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name='deposit_product_options'), # 특정 상품 옵션 리스트 출력
    path('deposit-products/top_rate/', views.top_rate, name='top_rate'), # 가입 기간 상관 없이 최고 그림가 가장 높은 금융 상품과 옵션 리스트 출력
]