# -*- coding: UTF-8 -*-
from PyQt4 import QtGui,QtCore

class Application:
	name = "default"
	config = 0 #for config file object from ConfigParser
#Это прототип всех "плагинов". Содержит общие мехаихмы для работы со списком опций, реестром опций и  т.п.

# каждая опция (пункт)может быть включена или выключена.
# если опция включена, то используется значение опции .
# По умолчанию отображаются галочки, описания опций и значения опций.


# это список галочек опций'. Какие опции испольовать (какие опции блокировать). Используется в рантайме. 
	options = {} 
	# см так же optionsValueArray_qt - список значений опций.
	
#*******************************************************************************
# !CHANGEIT IN CHILD! : это описания опций (имя и описание). Его надо менять в наследуемых плагинах:

	optionsArray_registry = {
	'имя фичи, опции или сама опция#тип#значение по умолчанию':"""
описание фичи
или опции
"""} 

#где
# тип=<пусто>,string, int, bool
# пусто означает, что опция не требует параметров или значения. или значение всегда фиксированное и смене не подлежит

#*******************************************************************************
#тут ключи - это строки QString - имена опций - для поиска по ним.

	optionsArray_descr_qt = {
	'имя фичи, опции или сама опция':"""
описание фичи
или опции
"""}

#тут ключи - это строки QString - значения опций в рантайме для поиска по ним. Используется в рантайме.
	optionsArray_value_qt = {
	'имя фичи, опции или сама опция':"""ЗначениеОпции"""}

#тут ключи - это строки QString - значения опций в рантайме для поиска по ним. Используется в рантайме.
	optionsArray_type_qt = {
	'имя фичи, опции или сама опция':"""типОпции"""}
	
#*******************************************************************************
	def set_options(self, options):
 		if not(isinstance(options, dict)):
			raise TypeError("dict expected")
		self.options = options
	
	def get_options(self):
		return self.options

	
	# Установить активность опции (галочка)
	def set_option(self, opt, value):
		self.options[QtCore.QString(opt)] = value
	
	# Получить активность опции  (галочка)
	def get_option(self, opt):
		return self.options[QtCore.QString(opt)]
	

	# Установить значение опции
	def set_value(self, opt, value):
		#мы не знаем что нам передали. потому попробуем плучить QString явно...
		if QtCore.QString(opt) in self.optionsArray_value_qt:
			self.optionsArray_value_qt[QtCore.QString(opt)]=value 
		retv=True
		return retv

	# Получить значение опции
	def get_value(self, opt):
		retv="-";
		#мы не знаем что нам передали. потому попробуем плучить QString явно...
		if QtCore.QString(opt) in self.optionsArray_value_qt:
			retv=self.optionsArray_value_qt[QtCore.QString(opt)] 
		return retv

		
	# Получить описание опции
	def get_descr(self, opt):
		retv="<no description>";
		#мы не знаем что нам передали. потому попробуем плучить QString явно...
		if QtCore.QString(opt) in self.optionsArray_descr_qt:
			retv=self.optionsArray_descr_qt[QtCore.QString(opt)] #
		return retv

	# Получить описание типа
	def get_type(self, opt):
		retv="";
		#мы не знаем что нам передали. потому попробуем плучить QString явно...
		if QtCore.QString(opt) in self.optionsArray_descr_qt:
			retv=self.optionsArray_type_qt[QtCore.QString(opt)] #
		return retv

	def checks(self):
		pass
	
	def load(self):
		pass
	
	def save(self):
		pass

#*******************************************************************************
# !CHANGEIT IN CHILD!: название плагина, для регистрации
def name():
	return "DUMMY koisk mode (probe)"
	
#*******************************************************************************
# !CHANGEIT IN CHILD!: краткое описание плагина, для регистрации
def descr():
	return """==================================
  Проба настройки киоск-мода 
  """
	
#*******************************************************************************
# !CHANGEIT IN CHILD!: подробное описание плагина, для регистрации
def help():
	return """
  Плагин настраивает одну из программ для работы 
  в Koisk-mode или предлагает расширенные фичи для настройки.
  """
	
#*******************************************************************************
# !CHANGEIT IN CHILD!: отдаем собственный объект 
def object():
	return Application()
