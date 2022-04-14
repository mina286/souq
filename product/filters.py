import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
    PRDname = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields ='__all__'
        exclude=['PRDimage','PRDslug','PRDdesc','PRDcost','PRDcreated','PRDquantity']