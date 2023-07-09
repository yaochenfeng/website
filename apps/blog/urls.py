from blog import views
from common.routers import router

router.register(r'blog', views.BlogViewSet)

urlpatterns = [

]
