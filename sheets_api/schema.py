import graphene
from graphene_django.types import DjangoObjectType
from .models import XLSX

class XLSXType(DjangoObjectType):
    class Meta:
        model = XLSX
        fields = "__all__"

class Query(graphene.ObjectType):
    all_items = graphene.List(XLSXType)

    def resolve_all_items(root, info) -> list[XLSXType]:
        return MyModel.objects.all()

schema = graphene.Schema(query=Query)
