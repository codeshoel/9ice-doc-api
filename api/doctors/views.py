from rest_framework import generics
from rest_framework.response import Response
from .models import Stakeholder
from .serializers import StakeholdersSerializer


class StakeholdersListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholdersSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = StakeholdersSerializer(queryset, many=True)
        return Response(serializer.data)


    def perform_create(self, serializer):
        serializer.save()

stakeholders_list_create_view = StakeholdersListCreateAPIView.as_view()



class StakeholderRetrieveDestroyAPIView(generics.RetrieveAPIView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholdersSerializer
        
stakeholders_retrieve_destroy_view = StakeholderRetrieveDestroyAPIView.as_view()