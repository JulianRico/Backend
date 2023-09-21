
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token





from usuarios.views import CreateUserView, TokenRenewView, UserDetailsView, UpdateUserView
from promociones.views import PromocionListView, EditPromocionView, EliminarPromocionView
from codigos.views import GenerarCodigoView
from historicoCodigos.views import CanjearCodigoView

schema_view = get_schema_view(
    openapi.Info(
        title="API Xolum",
        default_version='v1',
        description="API para la APP de Xolum",
        terms_of_service="",
        contact=openapi.Contact(email="juliquinterorico@hotmail.com"),
        license=openapi.License(name="No comercial, Privada"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-token-renew/', TokenRenewView.as_view(), name='api_token_renew'),
    #usuarios
    path('api/user-details/<str:username>/', UserDetailsView.as_view(), name='user-details'),
    path('api/user/create/', CreateUserView.as_view(), name='user-create'),
    path('api/user-update/', UpdateUserView.as_view(), name='user-update'),
    #usuarios 
    # # promociones
    path('api/promociones/', PromocionListView.as_view(), name='promocion-list'),
    path('api/edit-promocion/<int:pk>/', EditPromocionView.as_view(), name='edit-promocion'),
    path('api/eliminar-promocion/<int:pk>/', EliminarPromocionView.as_view(), name='eliminar-promocion'),
    # promociones   
    #Codigos
    path('api/generar-codigo/<int:idPromocion>/', GenerarCodigoView.as_view(), name='generar-codigo'),
    #codigos
    #historicos de codigos cobrados
    path('api/canjear-codigo/<str:codigo_id>/', CanjearCodigoView.as_view(), name='canjear_codigo'),
    #historicos de codigos cobrados
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]