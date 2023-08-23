from django.urls import path
from .views import CategoryList, CategoryDetail,ContactList,ContactDetail,HospitalList,HospitalDetail,HospitalSearchByAddress,HospitalSearchByCategory,HospitalSearchByName


urlpatterns = [
    #fsdfsd
    path("category/", CategoryList.as_view(), name="category-list"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("contact/", ContactList.as_view(), name="contact-list"),
    path("contact/<int:pk>/", ContactDetail.as_view(), name="contact-detail"),
    path("hospital/", HospitalList.as_view(), name="hospitalt-list"),
    path("hospital/<int:pk>/", HospitalDetail.as_view(), name="hospitalt-detail"),
    path('hospital/<str:address>/', HospitalSearchByAddress.as_view()),
    path('hospital/<int:category>/', HospitalSearchByCategory.as_view()),
    path('hospital/<str:name>/', HospitalSearchByName.as_view()),
    
]
