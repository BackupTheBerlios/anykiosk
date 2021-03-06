#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#
#===============================================================================
# Система дополнительной настройки программ и ОС
# с поддержкой плагинов.
#  Основное назначение - легкая подготовки рабочего места к 
#  работе в режиме kiosk-mode
#
#===============================================================================
# ОС: Linux
# Окружение: стандартный набор программ пославляемый в ПСПО5, Alt-Linux и др. родственных дистр. 
#
#===============================================================================
#
#
# 2010.10.24 Denjs:
# * Изменил механизм регистрации пагинов (думаю что стало проще подключать, 
#   хотя в плагине надо менять на 2 строчки больше)
# * Изменил механизм описания опций и их описаний.
# * Вбил в DummyFF все опции для FireFox. Выявилось, что скроллиннг в этом окне не работает....
# * Разное, мелкое типа комментов и укзания кодировки UTF-8
# 
# 2010.09.xx minoru-kun
# * первая версия "технологический прототип" )))
#
# предыстория: http://unixforum.org/index.php?showtopic=117466
#
#
#===============================================================================


import os, sys
#if os.getuid() != 0:
#    print("--------------------------------------")
#    print(" You have to be root to run AnyKiosk!")
#    print("--------------------------------------")
#
#    from PyQt4 import QtGui
#    if __name__=="__main__":
#	# создаём объект Qt-приложения и передаём его конструктору параметры командной строки:
#	app = QtGui.QApplication(sys.argv)
#	# создаём объект класса QLabel (метка), в конструкторе задаём подпись для метки:
#	#label = QtGui.QLabel(u' Вы не root !\n Вы не можете выполнить AnyKiosk от простого пользователя')    
#	QtGui.QMessageBox.information(None,u"Вы не root !",u"Вы не root ! \n\nДля запуска AnyKiosk нужны права суперпользователя.\n\nНажмите [OK] для выхода.",QtGui.QMessageBox.Ok)
#	## отображаем метку на экране:
#	#label.show()
#	#запускаем цикл обработки событий:
#	#sys.exit(app.exec_())
#    sys.exit() #quit;

#print("W are root. it is good!")

import controller_qt
import application

import os
#подготовка к разбору глобального ини-файл
try: #for python 2.5
    import ConfigParser
except:
    try: #for python 3.0
	import configparser
    except:
	print "can`t load ConfigParser module."
	exit(0)

globalConfig = ConfigParser.ConfigParser()
globalConfig.read('anykiosk.ini')
#print "tmppath=", globalConfig.get('anykiosk.main','tmppath')

pluginDir=globalConfig.get('anykiosk.main','pluginSubDir')#'./plugins'
tmpDir=globalConfig.get('anykiosk.main','tmpPath')#'./tmp'

#print "pluginDir :", pluginDir
#print "tmpDir :", tmpDir

#допишем в каталоги откуда импортирвать плагины наш спец каталог с плагинами.
import sys
import os
if pluginDir.startswith(".") or not pluginDir.startswith("/"):
    sys.path.append(os.getcwd()+'/'+pluginDir)
else :
    sys.path.append(pluginDir)

#-- plugin imports
import dummyFF
#--

controller = controller_qt.Controller()
#-- plugin initializations here
controller.register_app(dummyFF)
#--

controller.proceed()
controller.main()

