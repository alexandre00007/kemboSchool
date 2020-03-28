# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Backend.models import MySchoolUser
from Backend.models import MySchoolMenu
from Backend.models import MySchoolSousMenu


class dao_menu(object):

    @staticmethod
    def getUtilisateur(id):
        try:
            utilisateur = MySchoolUser.objects.filter(utilisateur=id)
            print("Utilisateur __id",utilisateur)
            return utilisateur
        except Exception as e:
            print("IL Y A PAS D'UTILISATION AVEC CETTE IDENTIFIANT",e)
