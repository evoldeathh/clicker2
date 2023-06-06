from django.apps import apps
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Core, Boost
from .serializers import CoreSerializer, BoostSerializer


#

@api_view(['GET'])
def call_click(request):
    coreModel = apps.get_model('backend', 'core')
    core = coreModel.objects.get(user=request.user)
    is_levelup = core.click()
    if is_levelup:
        Boost.objects.create(core=core, price=core.level*50, power=core.level*20)
    core.save()

    return Response({'core': CoreSerializer(core).data, 'is_levelup': is_levelup})


class BoostViewSet(viewsets.ModelViewSet):
    queryset = Boost.objects.all()
    serializer_class = BoostSerializer

    def get_queryset(self):
        core = Core.objects.get(user=self.request.user)
        boosts = Boost.objects.filter(core=core)
        return boosts
