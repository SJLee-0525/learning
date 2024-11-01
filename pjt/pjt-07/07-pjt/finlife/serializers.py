from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

# class DepositProductsOptionsSerializer(serializers.ModelSerializer):
#     class DepositProductOptionSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = DepositOptions
#             fields = '__all__'

#     options = DepositProductOptionSerializer(DepositOptions.objects.all().order_by('intr_rate')[0], read_only=True)

#     class Meta:
#         model = DepositProducts
#         fields = '__all__'