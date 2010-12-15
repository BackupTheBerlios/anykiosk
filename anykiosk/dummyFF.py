# -*- coding: UTF-8 -*-
import application

from PyQt4 import QtGui,QtCore

#2010.11.07
#2010.11.08
import os


# по описаниям http://tvxlc.livejournal.com/6943.html 
#+ http://habrahabr.ru/blogs/firefox/40098/
#+ http://habrahabr.ru/blogs/firefox/21631/
#+ https://developer.mozilla.org/en/Automatic_Mozilla_Configurator/Locked_config_settings
#+ http://users.telenet.be/mydotcom/howto/linuxkiosk/webterm02.htm
class DummyFF(application.Application):
	
#*******************************************************************************
	optionsArray = {
	'lockPref("browser.startup.homepage", "about:blank");':u"""
Установить домашнюю страницу пустой (about:blank)
""",
	
	'lockPref("browser.startup.page", 0);':u"""
Открывать пустую страницу при запуске браузера
""",
	
	'lockPref("browser.tabs.autoHide", false);':"""
Всегда показывать панель вкладок
""",
	
	'lockPref("network.proxy.type",0);':"""
Не использовать прокси-сервер
""",
	
	'lockPref("privacy.sanitize.sanitizeOnShutdown", true);':"""
Всегда удалять личные данные пользователя при закрытии браузера
""",
	
	'lockPref("privacy.sanitize.promptOnSanitize", false);':"""
Не спрашивать подтверждение перед удалением личных данных пользователя
""",
	
	'lockPref("privacy.item.sessions", true);':"""
Разрешить очистку сеансов SSL в меню Инструменты -> Удалить личные данные
""",
	
	'lockPref("privacy.item.passwords", true);':"""
Разрешить очистку паролей в меню Инструменты -> Удалить личные данные
""",
	
	'lockPref("privacy.item.history", true);':"""
Разрешить очистку журнала посещений в меню Инструменты -> Удалить личные данные
""",
	
	'lockPref("privacy.item.downloads", true);':"""
Разрешить очистку журнала загрузок в меню Инструменты -> Удалить личные данные
""",
	
	'lockPref("privacy.item.formdata", true);':"""
Разрешить очистку данных форм в меню Инструменты -> Удалить личные данные
""",
	
	'lockPref("privacy.item.cookies", true);':"""
Разрешить очистку куки (cookies) в меню Инструменты -> Удалить личные данные
""",
	
	'lockPref("privacy.item.cache", true);':"""
Разрешить очистку кэша в меню Инструменты -> Удалить личные данные
""",
	
	'lockPref("browser.formfill.enable", false);':"""
Не сохранять введенные в формы и панель поиска данные
""",
	
	'lockPref("browser.search.update", false);':"""
Не проверять обновления поисковых плагинов
""",
	
	'lockPref("privacy.popups.showBrowserMessage", true);':"""
Показывать в верхней часть окна браузера уведомление о блокировки всплывающего окна
""",
	
	'lockPref("browser.shell.checkDefaultBrowser", false);':"""
Не проверять при запуске, является ли Firefox браузером по умолчанию
""",
	
	'lockPref("security.enable_java", true);':"""
Использовать Java.
""",
	
	'lockPref("javascript.enabled", true);':"""
Использовать JavaScript.
""",
	
	'lockPref("security.warn_entering_secure", false);':"""
Не предупреждать о том, что загружается страница, поддерживающая шифрование
""",
	
	'lockPref("security.warn_leaving_secure", false);':"""
Не запрашивать разрешение об уходе с защищенной страницы
""",
	
	'lockPref("security.warn_submit_insecure", false);':"""
Не запрашивать разрешение об отправке данных с защищенной страницы на не защищенную
""",
	
	'lockPref("browser.tabs.loadInBackground", true);':"""
Загружать новые вкладки в фоновом режиме
""",
	
	'lockPref("browser.tabs.opentabfor.middleclick", true);':"""
Открывать новую вкладку при нажатии средней кнопки мыши (колёсика)
""",
	
	'lockPref("browser.tabs.warnOnClose", true);':"""
Спрашивать разрешение о закрытии окна, если открыта более чем одна вкладка
""",
	
	'lockPref("extensions.update.enabled", false);':"""
Не обновлять расширения автоматически
""",
	
	'lockPref("signon.rememberSignons", false);':"""
Не сохранять пароли входа на сайты
""",
	
	'lockPref("browser.download.manager.closeWhenDone", true);':"""
Закрывать Менеджер загрузки при завершении всех загрузок
""",
	
	'lockPref("security.enable_ssl2", true);':"""
Включить поддержку SSL2
""",
	
	'lockPref("security.enable_ssl3", true);':"""
Включить поддержку SSL3
""",
	
	'lockPref("security.enable_tls", true);':"""
Включить поддержку TLS 
""",
	
	'lockPref("signon.prefillForms", false);':"""
Не подставлять пароли автоматически
""",
	
	'lockPref("signon.expireMasterPassword", true);':"""
Не использовать мастер-пароль для сохранённых паролей
""",
	
	'lockPref("browser.download.manager.openDelay", 0);':"""
Удалять информацию об успешно загруженных файлах из Менеджера загрузки
""",
	
	'lockPref("browser.download.manager.focusWhenStarting", true);':"""
Делать окно Менеджера загрузки активным при начале новой загрузки
""",
	
	'lockPref("browser.download.useDownloadDir", false);':"""
Спрашивать каждый раз куда сохранять файл
""",
	
	'lockPref("browser.link.open_external", 3);':"""
Открывать все ссылки из внешних приложений в новых вкладках
""",
	
	'lockPref("browser.download.manager.showWhenStarting", true);':"""
Открывать Менеджер загрузки в начале загрузки файла
""",
	
	'lockPref("browser.history_expire_days", 0);':"""
Отключить ведение журнала
""",
	
	'lockPref("xpinstall.enabled", false);':"""
Запретить установку XPI-пакетов
"""  }

	
#*******************************************************************************
	def load(self):
		print " loading options from application config files "
		
		for opt in self.optionsArray:
			self.optionsArray_qt[QtCore.QString(opt)]=self.optionsArray[opt]
			self.set_option(QtCore.QString(opt), False) # <------------ тут надо бы научиться читать конфиг файла и подставлять сюда то что нашли
#		self.set_option('Опция 2', True)

		
	def save(self):
		
		#---------------------------------------------------------------------------
		# Пути проверены только для ПСПО5  
		#---------------------------------------------------------------------------
		pathToPutLocaSettingsJS="/usr/lib/firefox/defaults/preferences/"
		locaSettingsJSFilename="local-settings.kioskmode.js"
		#---------------------------------------------------------------------------
		pathToPutMozillaCFG="/usr/lib/firefox/"
		mozillaCFGFilename="mozilla.kioskmode.cfg"
		#---------------------------------------------------------------------------
		tmpWorkingPath="./tmp/"
		
		print " saving options to application config files "
		
		rezF="//\n"
		for opt in self.options.keys():
			print "dummy: saveopt", QtCore.QString(opt), "=", self.options[QtCore.QString(opt)]
			if self.options[QtCore.QString(opt)] == True :
				rezF=rezF+str(opt)
				rezF=rezF+str("\n")
		
		f = file(tmpWorkingPath+"mozilla.cfg.txt","w")
		f.write(str(rezF))
		f.close()
		
		print " :::: perl ./moz-byteshift.pl -s 13 <"+tmpWorkingPath+"mozilla.cfg.txt >"+tmpWorkingPath+mozillaCFGFilename
		os.system("perl ./moz-byteshift.pl -s 13 <"+tmpWorkingPath+"mozilla.cfg.txt >"+tmpWorkingPath+mozillaCFGFilename)
		# теперь у нас есть файл с настройками пригодный для подсовывания фоксу.
		# его покладем скорее всего в /usr/lib/firefox/ 
		
		#вот тут и нужны права рута.
		print " :::: (writing 'locaSettings.js file')  -=>",(pathToPutLocaSettingsJS+locaSettingsJSFilename),")"
		f = file(pathToPutLocaSettingsJS+locaSettingsJSFilename,"w")
		f.write('pref("general.config.filename", "'+mozillaCFGFilename+'");')
		f.close()
		
		print " :::: cp "+tmpWorkingPath+mozillaCFGFilename+" "+pathToPutMozillaCFG+mozillaCFGFilename
		os.system("cp "+tmpWorkingPath+mozillaCFGFilename+" "+pathToPutMozillaCFG+mozillaCFGFilename)
		
		#Все. теперь можно перезапустить фокс и должно быть счастье)))).


#	def checks(self):
#		pass
	
#*******************************************************************************
def name():
	return "DUMMY: Firefox 3.5 kiosk (probe)"
	
#*******************************************************************************
def descr():
	return """==================================
  Проба настройки киоск-мода для FireFox 3.5
  (см http://tvxlc.livejournal.com/6943.html )"""
	
#*******************************************************************************
def object():
	return DummyFF()
	
#*******************************************************************************
	#--------------------------------------------------------------------
	# TODO: 2010.10.24 from Denjs: 
	#--------------------------------------------------------------------
	# Нужен скроллинг внутри окна прилодения. опций много, все уезжает вниз 
	#--------------------------------------------------------------------
	# TODO: 2010.10.24 from Denjs: 
	#--------------------------------------------------------------------
	# 2010.10.24_1440: (надо доработать в следубщей части:
	# опции и конфиги могут быть 2-х видов:
  #  опции приложения, которые нам и надо менять.
	#  опции настройки плагина - такие например как путь до конфигов прилодения
	# сейчас есть меню опций только для опции target-прилодения.
	# надо как-то читать опции плагина из ini-файла что ли? инишник на первых порах подойдет.
	#--------------------------------------------------------------------
	# на текущий момент - принимаем направление движения: 
	# 
	# (1) нет "рекомендуемых опций"
	# коорые могут быть загружены по умолчанию. 
	# Все галочки грузятся из конфига программы.
	# (было бы хорошо иметь возможность сохранить набранный конфиг галочек 
  #   и загрузить его потом на другой машине)
	# 
	# (2) программа не позволяет менять опции.
	# например - сказано что "включаем Java"
	# - нет возможности ставить опцию - отключаем джава, ероме как добавлением её 
	# как ещё один пункт в меню.
