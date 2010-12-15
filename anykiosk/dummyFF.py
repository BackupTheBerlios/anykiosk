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
#+http://mozutil.mozilla-russia.org/pref/pref_4.html
class DummyFF(application.Application):
	
#*******************************************************************************

#'lockPref("security.warn_submit_insecure", false);':
#'TEST.OPTION.NAME#TESTTYPE#TESTVALUE':u"""TEST DESCRIPTION""",

	optionsArray_registry = {

	'browser.startup.homepage#string#about:blank':
u"""Адрес домашней страницы : 
( about:blank = пустая страница)""",

	'browser.tabs.autoHide#bool#false':
u"""Всегда показывать панель вкладок""",

	'privacy.sanitize.sanitizeOnShutdown#bool#true':
u"""Удалять личные данные пользователя 
при закрытии браузера""",
	
	'privacy.sanitize.promptOnSanitize#bool#false':
u"""Спрашивать подтверждение 
перед удалением личных данных пользователя""",

	'privacy.item.sessions#bool#true':
u"""Разрешить очистку сеансов SSL 
в меню Инструменты -> Удалить личные данные""",
	
	'privacy.item.passwords#bool#true':
u"""Разрешить очистку паролей 
в меню Инструменты -> Удалить личные данные""",

	'privacy.item.history#bool#true':
u"""Разрешить очистку журнала посещений
в меню Инструменты -> Удалить личные данные""",
	
	'privacy.item.downloads#bool#true':
u"""Разрешить очистку журнала загрузок
 в меню Инструменты -> Удалить личные данные""",

	'privacy.item.formdata#bool#true':
u"""Разрешить очистку данных форм
 в меню Инструменты -> Удалить личные данные""",
	
	'privacy.item.cookies#bool#true':
u"""Разрешить очистку куки (cookies) 
в меню Инструменты -> Удалить личные данные""",
	
	'privacy.item.cache#bool#true':
u"""Разрешить очистку кэша 
в меню Инструменты -> Удалить личные данные""",

	
	'browser.formfill.enable#bool#false':
"""Cохранять введенные в формы 
и панель поиска данные """,
	
	'browser.search.update#bool#false':
"""Проверять обновления поисковых плагинов""",

	'privacy.popups.showBrowserMessage#bol#true':
"""Показывать уведомление о блокировке
 всплывающего окна (в верхней части окна браузера)""",
	
	'browser.shell.checkDefaultBrowser#bool#false':
"""Проверять при запуске, 
является ли Firefox браузером по умолчанию""",
	
	'security.enable_java#bool#true':
"""Использовать Java""",
	
	'javascript.enabled#bool#true':
"""Использовать JavaScript""",
	
	'security.warn_entering_secure#bool#false':
"""Предупреждать о том, что загружается 
страница, поддерживающая шифрование""",
	
	'security.warn_leaving_secure#bool#false':
"""Запрашивать разрешение об уходе 
с защищенной страницы""",

	'security.warn_submit_insecure#bool#false':
"""Запрашивать разрешение об отправке
 данных с защищенной страницы 
на не защищенную""",
	
	'browser.tabs.loadInBackground#bool#true':
"""Загружать новые вкладки в фоновом режиме""",
	
	'browser.tabs.opentabfor.middleclick#bool#true':
"""Открывать новую вкладку по средней 
кнопке мыши (колёсику)""",
	
	'browser.tabs.warnOnClose#bool#true':
"""Спрашивать разрешение о закрытии окна, 
если открыта более чем одна вкладка""",

	'extensions.update.enabled#bool#false':
"""Обновлять расширения автоматически""",
	
	'signon.rememberSignons#bool#false':
"""Сохранять пароли входа на сайты""",
	
	'browser.download.manager.closeWhenDone#bool#true':
"""Закрывать Менеджер загрузки 
при завершении всех загрузок""",
	
	'security.enable_ssl2#bool#true':
"""Включить поддержку SSL2""",
	
	'security.enable_ssl3#bool#true':
"""Включить поддержку SSL3""",
	
	'security.enable_tls#bool#true':
"""Включить поддержку TLS""",
	
	'signon.prefillForms#bool#false':
"""Подставлять пароли автоматически""",
	
	'signon.expireMasterPassword#bool#true':
"""Использовать мастер-пароль 
для сохранённых паролей""",

	'browser.download.manager.focusWhenStarting#bool#true':
"""Делать окно Менеджера загрузки активным
 при начале новой загрузки""",
	
	'browser.download.useDownloadDir#bool#false':
"""Спрашивать каждый раз куда сохранять файл""",

	'browser.download.manager.showWhenStarting#bool#true':
"""Открывать Менеджер загрузки 
 при начале новой загрузки""",
	
	'xpinstall.enabled#bool#false':
"""Разрешить  установку XPI-пакетов""" ,

	########################
	## требуемые к правке ##
	########################
	
	'browser.startup.page#int#0':
u"""Открывать  при запуске браузера :
   * 0 - пустую страницу
   * 1 - домашнюю страница
   * 2 - последнюю посещенную страница 
   * 3 - полностью восстанавливать посл. сессию""",
	
	'network.proxy.type#true#0':
u"""Настройка прокси-сервера? ; число:
   * 0 - не использовать прокси 
   * 1 - ручная настройку прокси
   * 2 - автоматическая конфигурация (PAC)
   * 4 - автообнаружение прокси
   * 5 - исп.системные настройки""",
			
	'browser.download.manager.openDelay#bool#0':
"""Когда удалять инф. о загруженных файлах
 из Менеджера загрузки? ; число
    * 0 : После успешного окончания загрузки
    * 1 : При выходе из браузера
    * 3 : Удалять вручную""",
	
	'browser.link.open_external#int#3':
"""Каким образом открывать ссылки 
из внешних приложений?; число
    * 1 : Открывать в последней вкладке/окне
    * 2 : В новом окне
    * 3 : В новой вкладке последнего окна""",
	
	'browser.history_expire_days#int#0':
"""Количество дней, в течение которых 
хранится история браузера; число 
    * 0 = Отключить ведение журнала"""
	
}

	
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
			if optionDefValue=="false":
				self.optionsArray_descr_qt[optionName]=QtCore.QString("(нет) ")+QtCore.QString(self.optionsArray_descr_qt[optionName]);
			else:
				if optionDefValue=="true":
					self.optionsArray_descr_qt[optionName]=QtCore.QString("(да) ")+QtCore.QString(self.optionsArray_descr_qt[optionName]);
				else:
					self.optionsArray_descr_qt[optionName]=QtCore.QString("(%1) ").arg(optionDefValue)+QtCore.QString(self.optionsArray_descr_qt[optionName]);
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
	return u""" Firefox 3.6 Kiosk: заблокировать настройки от изменений. """
	
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
