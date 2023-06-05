from django.apps import apps
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CoreSerializer


@api_view(['GET'])
def call_click(request):
    coreModel = apps.get_model('backend', 'Core')
    core = coreModel.objects.get(user=request.user)
    core.click()
    core.save()

    return Response({'Core': CoreSerializer(core).data})
