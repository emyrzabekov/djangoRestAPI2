from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from news.models import News
from news.serializers import NewsSerializer



class NewsCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class NewsDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'
