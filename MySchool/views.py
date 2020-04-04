from django.shortcuts import render
from securityLogs.views import iam_authenticated
from Backend.dao_menu.dao_menu import dao_menu
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
# Create your views here.


def MySchoolAccueil(request):
    try:
        if request.user.is_authenticated:
            #recuperation de l'idUser Connecter
            getuser_id=request.user.id
            #recuperation de l'utilisateur dans le Système
            userId= dao_menu.getUtilisateur(getuser_id)
            #recuperateur des application
            lesApp = dao_menu.getapps(userId)
            #recuperation du profil User
            lesProfils = dao_menu.getprofils(userId)
            #recuperer l'ecole
            ecole = dao_menu.getschool(userId)
            context = {
                'index': 'Dashboard',
                'getapps': lesApp,
                'profils': lesProfils,
                'ecole': ecole
            }
            template = loader.get_template('MySchool/index.html')
            return HttpResponse(template.render(context, request))
        else:
            context = {'login': 'login'}
            template = loader.get_template('securityLog/login.html')
            return HttpResponse(template.render(context, request))
    except Exception as e:
        print("ERREUR MySchoolAccueil", e)
        context = {'login': 'login'}
        template = loader.get_template('securityLog/login.html')
        return HttpResponse(template.render(context, request))

def nothing(request):
    return HttpResponse("Url reussi avec succes")


