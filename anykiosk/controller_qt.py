# -*- coding: UTF-8 -*-
#import pygtk
#pygtk.require('2.0')
from PyQt4 import QtGui,QtCore
import sys
import os

class Controller:
	apps = {}
	descrs = {}
	qapp = QtGui.QApplication(sys.argv)
	
	def __init__(self):
		#Хочу русские буквы.)))) это надо сделать до вывода каких-либо сообщений.
		codec=QtCore.QTextCodec.codecForName('UTF-8')
		QtCore.QTextCodec.setCodecForTr(codec)
		QtCore.QTextCodec.setCodecForCStrings(codec)
		QtCore.QTextCodec.setCodecForLocale(codec)
		
		# check superuser privileges
		if os.getuid() != 0:
			QtGui.QMessageBox.critical(None, 
			    QtGui.qApp.tr("Ошибка: вы не root"),
			    QtGui.qApp.tr("Вы не root ! \n\nДля запуска AnyKiosk нужны права суперпользователя.\n\nНажмите [OK] для выхода."), #о переводе- потом будем думать. This program is required superuser privileges.\nProgram will be terminated now. 
			    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
			    QtGui.QMessageBox.NoButton)
			self.qapp.quit()
			sys.exit(1)

		boxLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom);
		
		self.window = QtGui.QWidget()
		self.window.resize(750,440)
		self.window.setWindowTitle("AnyKiosk. 0.0.5") 
		self.window.setLayout(boxLayout)
		
		
		#self.window.connect("destroy", self.destroy)
		#QtCore.QObject.connect( self.window, QtCore.SIGNAL("anySig1"), self, QtCore.SLOT("destroy") )
		self.qapp.connect(self.qapp, QtCore.SIGNAL("lastWindowClosed()"),self.qapp, QtCore.SLOT("quit()"))
		
		self.treestore=QtGui.QTreeWidget()
		self.treestore.setColumnCount(3)  #check&description; value; tech-key
		
		# Hide table column titles
		# Note: was introduced in Qt 4.4
#		self.treestore.setHeaderHidden(True)

		# Resize option description by content
		self.treestore.resizeColumnToContents(1)

		self.treestore.setAlternatingRowColors(True)
		self.treeview=self.treestore
		
		help_btn = QtGui.QPushButton(u"Помощь")
		showKeys_btn = QtGui.QPushButton(u"Режим эксперта: Ключи и Значения")
		apply_btn = QtGui.QPushButton(u"Установить")
		#restore_btn = QtGui.QPushButton("Restore")
		close_btn = QtGui.QPushButton(u"Закрыть")
		
		#QtCore.QObject.connect( apply_btn, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("apply_cb()") )
		QtCore.QObject.connect( apply_btn, QtCore.SIGNAL("clicked()"), self.apply_cb )
		QtCore.QObject.connect( close_btn, QtCore.SIGNAL("clicked()"), self.close_cb )
		QtCore.QObject.connect( showKeys_btn, QtCore.SIGNAL("clicked()"), self.keys_cb )
		QtCore.QObject.connect( help_btn, QtCore.SIGNAL("clicked()"), self.help_cb )
		QtCore.QObject.connect( self.treestore, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem *,int)"), self.itemDblClicked_cb )
		
		boxLayout.addWidget(self.treeview)

		button_hboxLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight);
		button_window = QtGui.QWidget()
		button_window.setLayout(button_hboxLayout)
		button_hboxLayout.addStretch(80)

		button_hboxLayout.addWidget(help_btn)
		button_hboxLayout.addSpacing(50) 
		button_hboxLayout.addWidget(showKeys_btn)
		button_hboxLayout.addSpacing(50) 
		button_hboxLayout.addWidget(apply_btn)
		#button_hboxLayout.addWidget(restore_btn)
		button_hboxLayout.addWidget(close_btn)
		boxLayout.addWidget(button_window)

		self.window.show()
		self.treestore.setColumnWidth(0,600)
		self.treestore.setColumnWidth(1,80)
		self.treestore.setColumnWidth(2,150)

#		self.treestore.setHorizontalHeaderLabels(self, QtGui.QString("Блокируемые опции#Значения опции#Пункт конфига").split("#"))  
#		(QtGui.QString("Блокируемые опции#Значения опции#Пункт конфига").split("#"))
#		self.treestore.setVerticalHeaderLabels(QtGui.QString("Блокируемые опции#Значения опции#Пункт конфига").split("#"))
		headers=[u"Блокируемые (значения) и опции", u"Значения опций", u"Имена пунктов конфиг.файла"]
        	self.treestore.setHeaderLabels(headers)

		#self.treestore.hideColumn(1)
		self.treestore.hideColumn(2)

	
	def main(self):
		sys.exit(self.qapp.exec_())
		
	def destroy(self, widget, data=None):
		self.qapp.quit();
	
	#def cell_toggled_cb(self, cell, path, treestore):
		##не нужно - потому что в QTreeWidget галочки сами так работают
	
	def register_app(self, module): #name, app, descr):
		self.apps[QtCore.QString(module.name())] = module.object() #app
		self.descrs[QtCore.QString(module.name())] = module.descr()
	
	def proceed(self):
		for app_name in self.apps.keys():
			app = self.apps[app_name]
			app.checks()
			app.load()
			descr = self.descrs[app_name]
			#master_iter = self.treestore.append(None, [app_name, descr, None])
			treeWidgetEl=QtGui.QTreeWidgetItem()
			treeWidgetEl.setFlags(treeWidgetEl.flags()|QtCore.Qt.ItemIsUserCheckable)
			treeWidgetEl.setFlags(treeWidgetEl.flags()|QtCore.Qt.ItemIsTristate) #need to be added for child checks update ok
			treeWidgetEl.setText(0,app_name)
#			treeWidgetEl.setText(1,descr)
#			treeWidgetEl.setData(2,QtCore.Qt.CheckStateRole,QtCore.Qt.Checked)
			self.treestore.addTopLevelItem(treeWidgetEl)
			master_iter = treeWidgetEl
			
			# Add application options
			for opt in app.get_options().keys():
				#self.treestore.append(master_iter, [opt, app.get_descr(opt), app.get_option(opt)])
				treeWidgetEl2=QtGui.QTreeWidgetItem(treeWidgetEl)
				treeWidgetEl2.setFlags(treeWidgetEl.flags()|QtCore.Qt.ItemIsUserCheckable)
				# Checkbox
				if app.get_option(opt): #нужно-ли фиксировать данную опцию
					treeWidgetE12.setCheckState(0, QtCore.Qt.Checked)
				else:
					treeWidgetEl2.setCheckState(0, QtCore.Qt.Unchecked)
				# Option description
				treeWidgetEl2.setText(0, app.get_descr(opt)) #описание опции
				# Option key
				treeWidgetEl2.setData(0, 100, QtCore.QVariant(opt))
				treeWidgetEl2.setText(1, app.get_value(opt) ) # значение опции 
				treeWidgetEl2.setText(2, opt)  #название опции
				
	def help_cb(self):
		helpMsg=u"""
Отметьте галочками опции которые вы хотите заблокировать от изменения,
или состояние которых хотите зафиксировать.

Если опция не отмечена - она "снимается" с блокировки .

Двойным нажатием на значении опции вы сможте изменить фиксируемое значение.

Кнопка [показать ключи] отображает 
технические имена пунктов конфигурационного файла,(смотрите техническое
 описание настраиваемой программы).

Сайт программы AnyKiosk: http://anykiosk.berlios.de

Страничка форума: http://unixforum.org/index.php?showtopic=120779

Авторы: Denjs, Minoru-kun, Skull (Cas)

"""
		QtGui.QMessageBox.information(None,u"AnyKiosk: Краткая помощь",helpMsg,QtGui.QMessageBox.Ok)


	def keys_cb(self):
		widthNewCol1=0  # ширина новой колонки
		widthNewCol2=120  # ширина новой колонки
		if self.treestore.isColumnHidden(2):
			#self.treestore.showColumn( 1)
			self.treestore.showColumn( 2)
			self.treestore.setColumnWidth(0,self.treestore.columnWidth(0)-(widthNewCol1+widthNewCol2))
			#self.treestore.setColumnWidth(1,widthNewCol1)
			#self.treestore.setColumnWidth(2,widthNewCol2)
			##print ("def keys_cb: show")
		else:
			self.treestore.setColumnWidth(0,self.treestore.columnWidth(0)+(widthNewCol1+widthNewCol2))
			#self.treestore.hideColumn( 1)
			self.treestore.hideColumn( 2)
			#print ("def keys_cb: hide")

	#def apply_cb(self, button):
	def apply_cb(self):
		i = 0
		while i<self.treestore.topLevelItemCount():
			try:
				master_row = self.treestore.topLevelItem(i)
				i=i+1
				#if (master_row==0):
				#  break
				
				i = i + 1
				app_name = master_row.text(0)
				
				childrencount=master_row.childCount()
				childrencount_i=0;
				
				app = self.apps[app_name]
				while childrencount_i<childrencount :
					try:
						x=master_row.child(childrencount_i)
						childrencount_i=childrencount_i+1;
						
						option_key = x.data(0, 100).toString()
						option_status = (x.checkState(0)==QtCore.Qt.Checked)
						#print option_key, option_status
						app.set_option(option_key, option_status)
						
					except StopIteration:
						break
				app.save()
			except IndexError:
				break
	
	#обработка двойного клика
	def itemDblClicked_cb(self, qTreeWidgetItem, column):
		parentWidget=qTreeWidgetItem.parent()
		if parentWidget==0:
			pass
		#теперь от родительского элемента получим приложение
		app_name=parentWidget.text(0)
		app=self.apps[app_name]
		#и получим ключ, галочку активности...
		option_key = qTreeWidgetItem.data(0, 100).toString()
		option_status = (qTreeWidgetItem.checkState(0)==QtCore.Qt.Checked)
		#print '::dpl Click for app['+unicode(app_name) + "] option ["+unicode(option_key)+"] "
		#... значение блокируемой опции
		option_value = app.get_value(option_key)
		option_type = app.get_type(option_key)
		option_descr = app.get_descr(option_key)
		print '::OLD VALUE:: option ['+unicode(option_key)+"] value ["+unicode(option_value)+"] type ["+unicode(option_type)+"]"
		
		#теперь надо разобрать тип и вывести меню выбора значения
		print "TODO: controller_qt.py::[00234] doubleClick TODO"
		option_value_new=option_value;
		#TODO: СДЕЛАТЬ ПРОВЕРКУ НА ОТКАЗ ВВОДА
		if option_type=="string":
			option_value_new,okSel=QtGui.QInputDialog.getText(None, u'Введите значение (строка)', u'Введите значение для \n\n'+option_descr+"", 0, option_value_new)
			if okSel==False:
			    option_value_new=option_value
			option_value_new=unicode(option_value_new)
			
		elif option_type=="int":
			try:
			    intValue=int(option_value)
			except:
			    intValue=0
			
			option_value_new, okSel=QtGui.QInputDialog.getInt(None, u'Введите значение (число)', u'Введите значение для \n\n'+option_descr+"", intValue )
			#print "RAW option_value_new = ["+ unicode(option_value_new)+"]"
			option_value_new=unicode(option_value_new)
			if okSel==False:
			    option_value_new=option_value
			print "RES option_value_new = ["+ option_value_new+"]"
			
		elif option_type=="bool":
			items=QtCore.QStringList();
			cTrueString=u"True: Да,Истина"
			items.append(cTrueString)
			items.append(u"False: Нет,Ложь")
			current_option_value=0
			if option_value=='false': #в javascript true/false с маленкой буквы
			    current_option_value=1
			option_value_new,okSel=QtGui.QInputDialog.getItem(None, u'Введите значение (истина/ложь)', u'Введите значение для \n\n'+option_descr+"", items, current_option_value )
			if okSel==False:
			    option_value_new=option_value
			elif option_value_new==cTrueString:
			    option_value_new="true"
			else:
			    option_value_new="false"
			#option_value_new=unicode(option_value_new).split(":")[0]
			
		elif unicode(option_type).startswith("{"): #перечисленне в виде {значение:описание;значение:описание;}
			items=QtCore.QStringList();
			#tmp_val=unicode(option_type).chop(1)
			current_option_value_index=0
			cpos_count=0
			for val in unicode(option_type).split(";"):
			    
			    if val[0]=="{":
				val=val[1:]
			    if val[-1]=="}":
				val=val[:-1]
			    if val.startswith(option_value):
				current_option_value_index=cpos_count
			    cpos_count+=1
			    items.append(val)
			#items.append(u"1: второе значение")
			option_value_new, okSel=QtGui.QInputDialog.getItem(None, u'Выберите значение', u'Введите значение для \n'+option_descr+"", items, current_option_value_index )
			
			#print "RAW option_value_new = ["+ unicode(option_value_new)+"]"
			if okSel==False:
			    option_value_new=option_value
			option_value_new=unicode(option_value_new).split(":")[0]
			
		#выведем устанавливаемое значение 
		print u"устанавливаемое значение:"
		print '::NEW VALUE:: option ['+unicode(option_key)+"] value ["+unicode(option_value_new)+"] type ["+unicode(option_type)+"]"
		
		app.set_value(option_key,option_value_new)
		qTreeWidgetItem.setText(1,option_value_new)
			
		#if column == 1 :
			
	#сохранить значения галочек и выбранных значений в файл
	def saveBlockingValuesSet_cb(self):
		pass
			
	#def close_cb(self, button):
	def close_cb(self):
		self.qapp.quit();
