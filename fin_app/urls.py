from django.contrib import admin
from django.urls import path,include
from fin_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name="index"),
   
    path('plan',views.pageplan,name="pageplan"),
   
    path('jeevanlabh',views.pagejl,name="pagejl"),
    path('jl',views.jl),
    path("resetjl",views.resetjl,name="resetjl"),
    
    path('jeevanumang',views.pageju,name="pageju"),
    path('ju',views.ju),
    path("resetju",views.resetju,name="resetju"),
   
    path('bonus',views.pagebonus,name='pagebonus'),
    path('bonusCal',views.bonusCal),
    path("resetbonus",views.resetbonus,name="resetbonus"),
   
    path('agent',views.pageagent,name="pageagent"),
    path('agentCal',views.agentCal),
    path("resetagent",views.resetagent,name="resetagent"),
    
    path('equity',views.pageequity,name='pageequity'),
    path('epf',views.epf),
    path("resetepf",views.resetepf,name="resetepf"),
    
    path('debtfinal',views.pagedebtfinal,name="pagedebtfinal"),
    path('dept',views.dept),
    path("resetdebt",views.resetdebt,name="resetdebt"),
    
    path('ppf',views.pageppf,name="pageppf"),
    path('productppf',views.productppf),
    path("resetppf",views.resetppf,name="resetppf"),

    path('bpension',views.pagebp,name="pagebp"),
    path('bp',views.bp),
    path("resetbp",views.resetbp,name="resetbp"),
    

    path('fpension',views.pagefp,name="pagefp"),
    path('fpcal',views.fpcal),
    path("resetfp",views.resetfp,name="resetfp"),
    
    path('ploan',views.pageploan,name='pageploan'),
    path('pl',views.pl),
    path("resetpl",views.resetpl,name="resetpl"),

    path('hloan',views.pagehloan,name='pagehloan'),
    path('hl',views.hl),
    path("resethl",views.resethl,name="resethl"),
    
    path('ment',views.brok,name='invest1'),
    path('broker',views.broker),
    path("resetbroker",views.resetbroker,name="resetbroker"),
    
    path('retrun',views.rein,name='returninm'),
    path('returnonin',views.returnonin),
    path("resetROI",views.resetROI,name="resetROI"),
    
    path('help',views.pagehelp,name="pagehelp"),
    
    path('aboutus',views.pageabout,name="pageabout"),

]