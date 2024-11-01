from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from django.conf import settings

from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    API_KEY = settings.API_KEY
    URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(URL).json()
    return Response(response)

@api_view(['GET'])
def save_deposit_products(request):
    API_KEY = settings.API_KEY
    URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(URL).json()

    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        if DepositProducts.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            kor_co_nm=kor_co_nm,
            fin_prdt_nm=fin_prdt_nm,
            etc_note=etc_note,
            join_deny=join_deny,
            join_member=join_member,
            join_way=join_way,
            spcl_cnd=spcl_cnd
        ).exists():
            continue

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd
        }

        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = li.get('intr_rate')
        if intr_rate == None:
            intr_rate = -1

        intr_rate2 = li.get('intr_rate2')
        if intr_rate2 == None:
            intr_rate2 = -1

        save_trm = li.get('save_trm')         

        if DepositOptions.objects.filter(
            fin_prdt_cd = fin_prdt_cd,
            intr_rate_type_nm = intr_rate_type_nm,
            intr_rate = intr_rate,
            intr_rate2 = intr_rate2,
            save_trm = save_trm,       
        ).exists():
            continue

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,   
        }

        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return Response({ 'message': 'okay' })
        

@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = get_list_or_404(DepositProducts)
        serializers = DepositProductsSerializer(products, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = DepositProductsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return JsonResponse({ 'message': '이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.'})
    

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = get_list_or_404(DepositOptions, fin_prdt_cd=fin_prdt_cd)
    serializers = DepositOptionsSerializer(options, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def top_rate(request):
    product_option = get_list_or_404(DepositOptions.objects.order_by('-intr_rate'))[0]
    # product_option = DepositOptions.objects.all().order_by('-intr_rate')[0]
    option_serializer = DepositOptionsSerializer(product_option)
    product = get_object_or_404(DepositProducts, fin_prdt_cd=option_serializer.data['fin_prdt_cd'])
    product_serializer = DepositProductsSerializer(product)
    result_data = {
        'deposit_product': product_serializer.data,
        'options': [option_serializer.data],
    }
    
    return Response(result_data)