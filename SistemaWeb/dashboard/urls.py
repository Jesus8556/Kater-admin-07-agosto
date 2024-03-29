from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('',views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('opcionCategorias/',views.categoriasOpcion, name='opcion_categorias'),
    path('opcionProformas/',views.proformasOpcion, name='opcion_proformas'),
    path('opcionServicios/', views.serviciosOpcion, name='opcion_servicios'),
    path('opcionCotizaciones/', views.cotizacionesOpcion, name='opcion_cotiza'),
    path('cliente/', views.ClienteView.as_view(), name='cliente'),
    path('cliente/nuevo/', views.ClienteAgregarView.as_view(), name='nuevo_cliente'),
    path('cliente/editar/<int:pk>/', views.ClienteEditarView.as_view(), name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.ClienteEliminarView.as_view(), name='eliminar_cliente'),
    path('vendedor/', views.VendedorView.as_view(), name='vendedor'),
    path('vendedor/agregar/', views.VendedorAgregarView.as_view(), name='agregar_vendedor'),
    path('vendedor/editar/<int:pk>/', views.VendedorEditarView.as_view(), name='editar_vendedor'),
    path('vendedor/eliminar/<int:pk>/', views.VendedorEliminarView.as_view(), name='eliminar_vendedor'),
    path('proformas/', views.ProformaView.as_view(), name='proforma'),
    path('proformas/agregar/', views.ProformaAgregarView.as_view(), name='agregar_proforma'),
    path('proformas/editar/<int:pk>/', views.ProformaEditarView.as_view(), name='editar_proforma'),
    path('proformas/eliminar/<int:pk>/', views.ProformaEliminarView.as_view(), name='eliminar_proforma'),
    path('proformasConsultoria/', views.ProformaConsultoriaView.as_view(), name='proformaconsultoria'),
    path('proformasConsultoria/agregar/', views.ProformaConsultoriaAgregarView.as_view(), name='agregar_proforma_consultoria'),
    path('proformasConsultoria/editar/<int:pk>/', views.ProformaConsultoriaEditarView.as_view(), name='editar_proforma_consultoria'),
    path('proformasConsultoria/eliminar/<int:pk>/', views.ProformaConsultoriaEliminarView.as_view(), name='eliminar_proforma_consultoria'),
    path('proformasManoDeObra/', views.ProformaManoDeObraView.as_view(), name='proformamanodeobra'),
    path('proformasManoDeObra/agregar/', views.ProformaManoDeObraAgregarView.as_view(), name='agregar_proforma_obra'),
    path('proformasManoDeObra/editar/<int:pk>/', views.ProformaManoDeObraEditarView.as_view(), name='editar_proforma_obra'),
    path('proformasManoDeObra/eliminar/<int:pk>/', views.ProformaManoDeObraEliminarView.as_view(), name='eliminar_proforma_obra'),
    path('get_vendedor_data/<int:vendedor_id>/', views.get_vendedor_data, name='get_vendedor_data'),
    path('proformas/duplicar/<int:proforma_id>/', views.duplicar_proforma, name='duplicar_proforma'),
    path('proformasConsultoria/duplicar/<int:proforma_id>/', views.duplicar_proforma_consultoria, name='duplicar_proforma_consultoria'),
    path('proformasManoDeObra/duplicar/<int:proforma_id>/', views.duplicar_proforma_obra, name='duplicar_proforma_obra'),
    path('cotizacion/agregar/', views.CotizacionAgregarView.as_view(), name='agregar_cotizacion'),
    path('cotizacion/', views.CotizacionView.as_view(), name='cotizacion'),
    path('cotizacion/editar/<int:pk>/', views.CotizacionEditarView.as_view(), name='editar_cotizacion'),
    path('cotizacion/eliminar/<int:pk>/', views.CotizacionEliminarView.as_view(), name='eliminar_cotizacion'),
    path('cotizacionConsultoria/agregar/', views.CotizacionConsultoriaAgregarView.as_view(), name='agregar_cotizacion_consultoria'),
    path('cotizacionConsultoria/', views.CotizacionConsultoriaView.as_view(), name='cotizacionconsultoria'),
    path('cotizacionConsultoria/editar/<int:pk>/', views.CotizacionConsultoriaEditarView.as_view(), name='editar_cotizacion_consultoria'),
    path('cotizacionConsultoria/eliminar/<int:pk>/', views.CotizacionConsultoriaEliminarView.as_view(), name='eliminar_cotizacion_consultoria'),
    path('cotizacionManoDeObra/agregar/', views.CotizacionManoDeObraAgregarView.as_view(), name='agregar_cotizacion_obra'),
    path('cotizacionManoDeObra/', views.CotizacionManoDeObraView.as_view(), name='cotizacionmanodeobra'),
    path('cotizacionManoDeObra/editar/<int:pk>/', views.CotizacionManoDeObraEditarView.as_view(), name='editar_cotizacion_obra'),
    path('cotizacionManoDeObra/eliminar/<int:pk>/', views.CotizacionManoDeObraEliminarView.as_view(), name='eliminar_cotizacion_obra'),
    path('cotizacion/<int:pk>/detalle/', views.detalle_cotizacion, name='detalle_cotizacion'),
    path('cotizacion/<int:pk>/detalle/<int:detalle_id>/', views.detalle_cotizacion, name='editar_detalle'),
    path('cotizacion/eliminar_detalle/<int:pk>/', views.DetalleEliminarView.as_view(), name='eliminar_detalle'),
    path('cotizacionConsultoria/<int:pk>/detalleConsultoria/', views.detalle_cotizacion_consultoria, name='detalle_cotizacion_consultoria'),
    path('cotizacionConsultoria/<int:pk>/detalleConsultoria/<int:detalle_id>/', views.detalle_cotizacion_consultoria, name='editar_detalle_consultoria'),
    path('cotizacionConsultoria/eliminar_detalle_consultoria/<int:pk>/', views.DetalleConsultoriaEliminarView.as_view(), name='eliminar_detalle_consultoria'),
    path('cotizacionManoDeObra/<int:pk>/detalleManoDeObra/', views.detalle_cotizacion_obra, name='detalle_cotizacion_obra'),
    path('cotizacionManoDeObra/<int:pk>/detalleManoDeObra/<int:detalle_id>/', views.detalle_cotizacion_obra, name='editar_detalle_obra'),
    path('cotizacionManoDeObra/eliminar_detalle_obra/<int:pk>/', views.DetalleManoDeObraEliminarView.as_view(), name='eliminar_detalle_obra'),
    path('cotizacion/generar_pdf/<int:pk>/', views.generar_pdf, name='generar_pdf'),
    path('mantenimiento/',views.MantenimientoView.as_view(), name='mantenimiento'),
    path('mantenimiento/nuevo/', views.MantenimientoAgregarView.as_view(), name='nuevo_mantenimiento'),
    path('mantenimiento/editar/<int:pk>/', views.MantenimientoEditarView.as_view(), name='editar_mantenimiento'),
    path('mantenimineto/eliminar/<int:pk>/', views.MantenimientoEliminarView.as_view(), name='eliminar_mantenimiento'),
    path('consultoria/',views.ConsultoriaView.as_view(), name='consultoria'),
    path('consultoria/nuevo/', views.ConsultoriaAgregarView.as_view(), name='nueva_consultoria'),
    path('consultoria/editar/<int:pk>/', views.ConsultoriaEditarView.as_view(), name='editar_consultoria'),
    path('consultoria/eliminar/<int:pk>/', views.ConsultoriaEliminarView.as_view(), name='eliminar_consultoria'),
    path('obra/',views.ManoDeObraView.as_view(), name='manodeobra'),
    path('obra/nuevo/', views.ManoDeObraAgregarView.as_view(), name='nueva_obra'),
    path('obra/editar/<int:pk>/', views.ManoDeObraEditarView.as_view(), name='editar_obra'),
    path('obra/eliminar/<int:pk>/', views.ManoDeObraEliminarView.as_view(), name='eliminar_obra'),
    path('agregar_direccion/', views.agregar_direccion, name='agregar_direccion'),









]