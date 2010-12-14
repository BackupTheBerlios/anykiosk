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
	optionsArray_registry = {
	#'TEST.OPTION.NAME#TESTTYPE#TESTVALUE':u"""TEST DESCRIPTION""",

	#'lockPref("browser.startup.homepage", "about:blank");':u"""Установить домашнюю страницу пустой (about:blank)""",
	'browser.startup.homepage#string#about:blank': u"""Установить домашнюю страницу пустой (about:blank)""",
	
	#'lockPref("browser.startup.page", 0);':u"""Открывать пустую страницу при запуске браузера""",
	'browser.startup.page#int#0': u"""Открывать пустую страницу при запуске браузера""",
	
	#'lockPref("browser.tabs.autoHide", false);':"""Всегда показывать панель вкладок""",
	'browser.tabs.autoHide#bool#false':u"""Всегда показывать панель вкладок""",
	
	#'lockPref("network.proxy.type",0);':"""Не использовать прокси-сервер""",
	'network.proxy.type#true#0':u"""Не использовать прокси-сервер""",
	
	#'lockPref("privacy.sanitize.sanitizeOnShutdown", true);':"""Всегда удалять личные данные пользователя при закрытии браузера""",
	'privacy.sanitize.sanitizeOnShutdown#bool#true':u"""Всегда удалять личные данные пользователя при закрытии браузера""",
	
	#'lockPref("privacy.sanitize.promptOnSanitize", false);':
	'privacy.sanitize.promptOnSanitize#bool#false':
u"""Не спрашивать подтверждение 
перед удалением личных данных пользователя""",
	
	#'lockPref("privacy.item.sessions", true);':
	'privacy.item.sessions#bool#true':
"""Разрешить очистку сеансов SSL 
в меню Инструменты -> Удалить личные данные""",
	
	#'lockPref("privacy.item.passwords", true);':
	'privacy.item.passwords#bool#true':
"""Разрешить очистку паролей 
в меню Инструменты -> Удалить личные данные""",
	
	#'lockPref("privacy.item.history", true);':
	'privacy.item.history#bool#true':
"""Разрешить очистку журнала посещений
в меню Инструменты -> Удалить личные данные""",
	
	#'lockPref("privacy.item.downloads", true);':
	'privacy.item.downloads#bool#true':
"""Разрешить очистку журнала загрузок
 в меню Инструменты -> Удалить личные данные""",
	
	#'lockPref("privacy.item.formdata", true);':
	'privacy.item.formdata#bool#true':
"""Разрешить очистку данных форм
 в меню Инструменты -> Удалить личные данные""",
	
	#'lockPref("privacy.item.cookies", true);':
	'privacy.item.cookies#bool#true':
"""Разрешить очистку куки (cookies) 
в меню Инструменты -> Удалить личные данные""",
	
	#'lockPref("privacy.item.cache", true);':
	'privacy.item.cache#bool#true':
"""Разрешить очистку кэша 
в меню Инструменты -> Удалить личные данные""",
	
	#'lockPref("browser.formfill.enable", false);':"""Не сохранять введенные в формы и панель поиска данные""",
	'browser.formfill.enable#bool#false':"""Не сохранять введенные в формы и панель поиска данные""",
	
	#'lockPref("browser.search.update", false);':"""Не проверять обновления поисковых плагинов""",
	'browser.search.update#bool#false':"""Не проверять обновления поисковых плагинов""",
	
	#'lockPref("privacy.popups.showBrowserMessage", true);':
	'privacy.popups.showBrowserMessage#bol#true':
"""Показывать в верхней часть окна браузера
 уведомление о блокировки всплывающего окна""",
	
	#'lockPref("browser.shell.checkDefaultBrowser", false);':
	'browser.shell.checkDefaultBrowser#bool#false':
"""Не проверять при запуске, 
является ли Firefox браузером по умолчанию""",
	
	#'lockPref("security.enable_java", true);':"""Использовать Java""",
	'security.enable_java#bool#true':"""Использовать Java""",
	
	#'lockPref("javascript.enabled", true);':"""Использовать JavaScript""",
	'javascript.enabled#bool#true':"""Использовать JavaScript""",
	
	#'lockPref("security.warn_entering_secure", false);':
	'security.warn_entering_secure#bool#false':
"""Не предупреждать о том, что загружается 
страница, поддерживающая шифрование""",
	
	#'lockPref("security.warn_leaving_secure", false);':"""Не запрашивать разрешение об уходе с защищенной страницы""",
	'security.warn_leaving_secure#bool#false':"""Не запрашивать разрешение об уходе с защищенной страницы""",
	
	#'lockPref("security.warn_submit_insecure", false);':
	'security.warn_submit_insecure#bool#false':
"""Не запрашивать разрешение об отправке
 данных с защищенной страницы на не защищенную""",
	
	#'lockPref("browser.tabs.loadInBackground", true);':"""Загружать новые вкладки в фоновом режиме""",
	'browser.tabs.loadInBackground#bool#true':"""Загружать новые вкладки в фоновом режиме""",
	
	#'lockPref("browser.tabs.opentabfor.middleclick", true);':"""Открывать новую вкладку при нажатии средней кнопки мыши (колёсика)""",
	'browser.tabs.opentabfor.middleclick#bool#true':"""Открывать новую вкладку при нажатии средней кнопки мыши (колёсика)""",
	
	#'lockPref("browser.tabs.warnOnClose", true);':"""Спрашивать разрешение о закрытии окна, если открыта более чем одна вкладка""",
	'browser.tabs.warnOnClose#bool#true':"""Спрашивать разрешение о закрытии окна, если открыта более чем одна вкладка""",
	
	#'lockPref("extensions.update.enabled", false);':"""Не обновлять расширения автоматически""",
	'extensions.update.enabled#bool#false':"""Не обновлять расширения автоматически""",
	
	#'lockPref("signon.rememberSignons", false);':"""Не сохранять пароли входа на сайты""",
	'signon.rememberSignons#bool#false':"""Не сохранять пароли входа на сайты""",
	
	#'lockPref("browser.download.manager.closeWhenDone", true);':"""Закрывать Менеджер загрузки при завершении всех загрузок""",
	'browser.download.manager.closeWhenDone#bool#true':"""Закрывать Менеджер загрузки при завершении всех загрузок""",
	
	#'lockPref("security.enable_ssl2", true);':"""Включить поддержку SSL2""",
	'security.enable_ssl2#bool#true':"""Включить поддержку SSL2""",
	
	#'lockPref("security.enable_ssl3", true);':"""Включить поддержку SSL3""",
	'security.enable_ssl3#bool#true':"""Включить поддержку SSL3""",
	
	#'lockPref("security.enable_tls", true);':"""Включить поддержку TLS""",
	'security.enable_tls#bool#true':"""Включить поддержку TLS""",
	
	#'lockPref("signon.prefillForms", false);':"""Не подставлять пароли автоматически""",
	'signon.prefillForms#bool#false':"""Не подставлять пароли автоматически""",
	
	#'lockPref("signon.expireMasterPassword", true);':"""Не использовать мастер-пароль для сохранённых паролей""",
	'signon.expireMasterPassword#bool#true':"""Не использовать мастер-пароль для сохранённых паролей""",
	
	#'lockPref("browser.download.manager.openDelay", 0);':"""Удалять информацию об успешно загруженных файлах из Менеджера загрузки""",
	'browser.download.manager.openDelay#bool#0':"""Удалять информацию об успешно загруженных файлах из Менеджера загрузки""",
	
	#'lockPref("browser.download.manager.focusWhenStarting", true);':"""Делать окно Менеджера загрузки активным при начале новой загрузки""",
	'browser.download.manager.focusWhenStarting#bool#true':"""Делать окно Менеджера загрузки активным при начале новой загрузки""",
	
	#'lockPref("browser.download.useDownloadDir", false);':"""Спрашивать каждый раз куда сохранять файл""",
	'browser.download.useDownloadDir#bool#false':"""Спрашивать каждый раз куда сохранять файл""",
	
	#'lockPref("browser.link.open_external", 3);':"""Открывать все ссылки из внешних приложений в новых вкладках""",
	'browser.link.open_external#int#3':"""Открывать все ссылки из внешних приложений в новых вкладках""",
	
	#'lockPref("browser.download.manager.showWhenStarting", true);':"""Открывать Менеджер загрузки в начале загрузки файла""",
	'browser.download.manager.showWhenStarting#bool#true':"""Открывать Менеджер загрузки в начале загрузки файла""",
	
	#'lockPref("browser.history_expire_days", 0);':"""Отключить ведение журнала""",
	'browser.history_expire_days#int#0':"""Отключить ведение журнала""",
	
	#'lockPref("xpinstall.enabled", false);':"""Запретить установку XPI-пакетов"""  }
	'xpinstall.enabled#bool#false':"""Запретить установку XPI-пакетов"""  }

	
#*******************************************************************************
	#инициация списка опций из реестра опций
	def load(self):
		print " loading options from application config files "
		
		for opt in self.optionsArray_registry:
			# 	'имя фичи, опции или сама опция#тип#значение по умолчанию'
			regElementList=QtCore.QString(opt).split("#") #отдает QStringList
			#regElementList=opt.split("#")
			regElementListLen=len(regElementList);
			#print "regElementListLen="+QtCore.QString("%1").arg(regElementListLen);
			optionName="";
			optionValueType="string"
			optionDefValue="";
			if regElementListLen>=0: 
				optionName=regElementList[0]
			if regElementListLen>1: 
				optionValueType=regElementList[1]  #тип - сейчас не используется, но будет нужен при определении того, сколько и чего отображать в значениях
			if regElementListLen>2: 
				optionDefValue=regElementList[2] 

			 #из этого всего следует, что если
			self.optionsArray_descr_qt[optionName]=self.optionsArray_registry[opt]
			self.optionsArray_value_qt[optionName]=optionDefValue #self.optionsArray_registry[opt]
			self.optionsArray_type_qt[optionName]=optionValueType 
			self.set_option(optionName, False) # <------------ тут надо бы научиться читать конфиг файла и подставлять сюда то что нашли


		
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
			rezF0=""
			if self.options[QtCore.QString(opt)] == True :
				#rezF=rezF+str(opt)
				if (self.optionsArray_type_qt[QtCore.QString(opt)]==QtCore.QString("string")):
					rezF0=str('lockPref("'+QtCore.QString(opt)+ '","' +self.optionsArray_value_qt[QtCore.QString(opt)]+'");')
				else:
					rezF0=str('lockPref("'+QtCore.QString(opt)+ '",' +self.optionsArray_value_qt[QtCore.QString(opt)]+');')
				rezF=rezF+rezF0
				rezF=rezF+str("\n")
				print "dummyFireFox: added (",QtCore.QString(opt),"):"# ,rezF0 
		
		print "\n\nTOTAL \n dummyFireFox: \n ", rezF,"\n\n" 
		f = file(tmpWorkingPath+"mozilla.cfg.txt","w")
		f.write(str(rezF))
		f.close()

		
		
		print " :::: perl ./moz-byteshift.pl -s 13 <"+tmpWorkingPath+"mozilla.cfg.txt >"+tmpWorkingPath+mozillaCFGFilename
		rez=os.system("perl ./moz-byteshift.pl -s 13 <"+tmpWorkingPath+"mozilla.cfg.txt >"+tmpWorkingPath+mozillaCFGFilename)
		if rez!=0:
			QtGui.QMessageBox.information(None,u"Упс...",u"DВозникла непредвиденная ошибка в ходе выполнения perl ./moz-byteshift.pl. \n\n Обратитесь к системному администратору, или произведите установку программы штатными средствами. \n(скорее всего набор прав perl-скрипта не соответсвует <<755>>)\n\nНажмите [OK] для выхода.",QtGui.QMessageBox.Ok)
			pass
		# теперь у нас есть файл с настройками, пригодный для подсовывания фоксу.
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
