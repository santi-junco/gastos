from . import apiviews

from django.urls import path

urlpatterns = [
    #### Ingreso
    path("ingresos/list/", apiviews.IngresoListApiView.as_view()),
    path("ingresos/create/", apiviews.IngresoCreateApiView.as_view()),
    path("ingresos/update/<int:pk>/", apiviews.IngresoUpdateApiView.as_view()),
    path("ingresos/delete/<int:pk>/", apiviews.IngresoDeleteApiView.as_view()),

    #### Gasto Fijo
    path("gasto-fijo/list/", apiviews.GastoFijoListApiView.as_view()),
    path("gasto-fijo/create/", apiviews.GastoFijoCreateApiView.as_view()),
    path("gasto-fijo/update/<int:pk>/", apiviews.GastoFijoUpdateApiView.as_view()),
    path("gasto-fijo/delete/<int:pk>/", apiviews.GastoFijoDeleteApiView.as_view()),

    ####Gasto Variable
    path("gasto-variable/list/", apiviews.GastoVariableListApiView.as_view()),
    path("gasto-variable/create/", apiviews.GastoVariableCreateApiView.as_view()),
    path("gasto-variable/update/<int:pk>/", apiviews.GastoVariableUpdateApiView.as_view()),
    path("gasto-variable/delete/<int:pk>/", apiviews.GastoVariableDeleteApiView.as_view()),
]
