from django.urls import path, include
#foi feito o importe do include acima

#import das views index e contato criadas no core/views
from core.views import index, contato, produtos, produto_single, blogs, blog_single, produtos_categoria
#Rota na url 
# - Quando acessar a rota "raiz do site" ele chama a função index
# - Quando acessar a rota "contato" ele chama a função contato
# - O atributo name é para ser possível chamar o link com o "url" Ex: <li><a href="{% url 'index' %}">Home</a></li>
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produtos', produtos, name='produtos'),
    path('produto/<int:id>/', produto_single, name='produto_single'),
    path('blogs', blogs, name='blogs'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
    path('produtos/<str:cat_name>/', produtos_categoria, name='produtos_categoria'),
]