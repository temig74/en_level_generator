from random import shuffle
from time import sleep
import os

from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from PySide6.QtCore import Qt, QThreadPool

from ui.ui_mainwindow import Ui_MainWindow
from olimp_gen2 import generate_img_table, generate_olimp_rows
from dump_gen import gen_random_format
from image_with_lineedit_widget import ImageWithLineedit
from olimp_sector_widget import OlimpSector2
import en_engine_upload


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.thread_manager = QThreadPool()  # Thread manager to run tasks in background without freezing app
        self.ui.btn_loadImagesYandex.clicked.connect(lambda: self.thread_manager.start(lambda: self.load_all_images('yandex')))
        self.ui.btn_loadImagesGoogle.clicked.connect(lambda: self.thread_manager.start(lambda: self.load_all_images('google')))
        self.ui.btn_saveToDisk.clicked.connect(self.save_images)
        self.ui.btn_loadSectors.clicked.connect(lambda: self.thread_manager.start(self.upload_sectors))
        self.ui.btn_loadBonuses.clicked.connect(lambda: self.thread_manager.start(self.upload_bonuses))
        self.ui.btn_loadTask.clicked.connect(self.upload_task)

        # Олимпийка
        self.ui.layout_olimp.setSpacing(0)
        self.ui.layout_olimp.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.ui.btn_generateGrid.clicked.connect(self.generate_olimp_grid)
        self.ui.btn_clearGrid.clicked.connect(self.clear_area)
        self.words_set = set()  # Set of used words
        # Свалка
        self.ui.btn_generateDump.clicked.connect(self.gen_dump)
        self.ui.btn_addDump.clicked.connect(self.add_dump_row)
        self.ui.btn_clearDump.clicked.connect(lambda: self.ui.tableWidget.setRowCount(0))
        with open('dict.txt', 'r', encoding='utf-8') as dict_file:
            self.my_dict = tuple(dict_file.read().lower().splitlines())
        self.ui.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.tableWidget.addAction('Удалить строку', lambda: self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow()))

    # Сохранение картинок на диск
    def save_images(self):
        file_prefix = self.ui.lineEdit_prefix.text()
        folder_name = self.ui.lineEdit_gameId.text()
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        match self.ui.tabWidget.currentIndex():
            case 0:
                for i in range(self.ui.layout_olimp.count()):
                    my_widget = self.ui.layout_olimp.itemAt(i).widget().image_widget
                    if my_widget.with_image:
                        my_widget.label.pixmap().save(f'{folder_name}/{file_prefix}_{i + 1}.png', 'PNG')
                    if self.ui.btn_stop.isChecked():
                        self.ui.btn_stop.setChecked(False)
                        return
            case 1:
                for i in range(self.ui.tableWidget.rowCount()):
                    widget1 = self.ui.tableWidget.cellWidget(i, 1)
                    widget1_id = self.ui.tableWidget.item(i, 4).text()
                    widget1.label.pixmap().save(f'{folder_name}/{file_prefix}_{widget1_id}.png', 'PNG')
                    widget2 = self.ui.tableWidget.cellWidget(i, 2)
                    widget2_id = self.ui.tableWidget.item(i, 5).text()
                    widget2.label.pixmap().save(f'{folder_name}/{file_prefix}_{widget2_id}.png', 'PNG')

    def load_all_images(self, search_engine):
        if search_engine == 'yandex':
            img_class = self.ui.lineEdit_yandexClass.text()
        else:
            img_class = self.ui.lineEdit_googleClass.text()
        img_relevance = self.ui.spinBox_imagesRelevance.value()
        delay = self.ui.spinBox_imagesDelay.value()

        match self.ui.tabWidget.currentIndex():
            case 0:  # олимпийка
                for i in range(self.ui.layout_olimp.count()):
                    my_widget = self.ui.layout_olimp.itemAt(i).widget().image_widget
                    if my_widget.with_image:
                        sleep(delay / 1000)
                        my_widget.load_internet_img(search_engine, img_class, img_relevance)
                    if self.ui.btn_stop.isChecked():  # Останавливаем, если нажимаем стоп
                        self.ui.btn_stop.setChecked(False)
                        return
            case 1:  # свалка
                for i in range(self.ui.tableWidget.rowCount()):
                    widget1 = self.ui.tableWidget.cellWidget(i, 1)
                    widget1.load_internet_img(search_engine, img_class, img_relevance)
                    sleep(delay / 1000)
                    widget2 = self.ui.tableWidget.cellWidget(i, 2)
                    widget2.load_internet_img(search_engine, img_class, img_relevance)
                    sleep(delay / 1000)
                    if self.ui.btn_stop.isChecked():  # Останавливаем, если нажимаем стоп
                        self.ui.btn_stop.setChecked(False)
                        return

    def upload_sectors(self):
        my_session = en_engine_upload.get_auth_session(self.ui.lineEdit_domain.text(), self.ui.lineEdit_login.text(), self.ui.lineEdit_password.text())
        if not my_session:
            QMessageBox(text='Ошибка авторизации').exec()
            return

        for i in range(self.ui.spinBox_startLoad.value()-1, self.ui.spinBox_endLoad.value()):
            match self.ui.tabWidget.currentIndex():
                case 0:
                    txt_sector_name = ''
                    answer = [self.ui.layout_olimp.itemAt(i).widget().image_widget.lineedit.text()]
                    if self.ui.checkBox_yo.isChecked() and 'ё' in answer[0].lower():
                        answer.append(answer[0].lower().replace('ё', 'е'))
                case 1:
                    txt_sector_name = self.ui.tableWidget.item(i, 0).text()
                    answer = []
                    for elem in self.ui.tableWidget.item(i, 3).text().split('|'):
                        answer.append(elem)
                        if self.ui.checkBox_yo.isChecked() and 'ё' in elem.lower():
                            answer.append(elem.lower().replace('ё', 'е'))

            en_engine_upload.sector_upload(my_session, txt_sector_name, answer, self.ui.spinBox_levelNum.value(), self.ui.lineEdit_gameId.text(), self.ui.lineEdit_domain.text())
            sleep(self.ui.spinBox_uploadDelay.value()/1000)
            self.ui.btn_loadSectors.setText(f'Выгружаю {i+1} сектор')

            QApplication.processEvents()
            if self.ui.btn_stop.isChecked():
                self.ui.btn_stop.setChecked(False)
                return

        self.ui.btn_loadSectors.setText('Выгр. секторы')

    def upload_bonuses(self):
        my_session = en_engine_upload.get_auth_session(self.ui.lineEdit_domain.text(), self.ui.lineEdit_login.text(), self.ui.lineEdit_password.text())
        if not my_session:
            QMessageBox(text='Ошибка авторизации').exec()
            return
        level_num = self.ui.spinBox_levelNum.value()
        level_id = en_engine_upload.get_level_id(my_session, self.ui.lineEdit_domain.text(), self.ui.lineEdit_gameId.text(), level_num)

        match self.ui.tabWidget.currentIndex():
            case 0:
                with open('./patterns/olimp_bonus_hint.txt', encoding='utf-8') as f:
                    bonus_hint = f.read()
                with open('./patterns/olimp_bonus_img_hint.txt', encoding='utf-8') as f:
                    bonus_img_hint = f.read()

                for i in range(self.ui.spinBox_startLoad.value()-1, self.ui.spinBox_endLoad.value()):
                    answer = [self.ui.layout_olimp.itemAt(i).widget().image_widget.lineedit.text()]
                    if self.ui.checkBox_yo.isChecked() and 'ё' in answer[0].lower():
                        answer.append(answer[0].lower().replace('ё', 'е'))
                    txt_help = bonus_hint.replace('{level_num}', str(level_num)).replace('{i}', str(i+1)).replace('{answer}', answer[0])
                    if i < self.ui.layout_olimp.count()/2:
                        txt_help += bonus_img_hint.replace('{level_num}', str(level_num)).replace('{i}', str(i+1))

                    en_engine_upload.bonus_upload(my_session, '', '', txt_help, level_id, answer, self.ui.spinBox_hours.value(), self.ui.spinBox_minutes.value(), self.ui.spinBox_seconds.value(), self.ui.lineEdit_domain.text(), level_num, self.ui.lineEdit_gameId.text())
                    sleep(self.ui.spinBox_uploadDelay.value() / 1000)
                    self.ui.btn_loadBonuses.setText(f'Выгружаю {i+1} бонус')

                    QApplication.processEvents()
                    if self.ui.btn_stop.isChecked():
                        self.ui.btn_stop.setChecked(False)
                        return
            case 1:
                with open('./patterns/dump_bonus_img_hint.txt', encoding='utf-8') as f:
                    bonus_img_hint = f.read()
                for i in range(self.ui.spinBox_startLoad.value()-1, self.ui.spinBox_endLoad.value()):
                    answer = []
                    for elem in self.ui.tableWidget.item(i, 3).text().split('|'):
                        answer.append(elem)
                    if self.ui.checkBox_yo.isChecked() and 'ё' in elem.lower():
                        answer.append(elem.lower().replace('ё', 'е'))
                    txt_help = bonus_img_hint.replace('{level_num}', str(level_num)).replace('{n1}', self.ui.tableWidget.item(i, 4).text()).replace('{n2}', self.ui.tableWidget.item(i, 5).text())
                    en_engine_upload.bonus_upload(my_session, '', '', txt_help, level_id, answer, self.ui.spinBox_hours.value(), self.ui.spinBox_minutes.value(), self.ui.spinBox_seconds.value(), self.ui.lineEdit_domain.text(), level_num, self.ui.lineEdit_gameId.text())
                    sleep(self.ui.spinBox_uploadDelay.value() / 1000)
                    self.ui.btn_loadBonuses.setText(f'Выгружаю {i + 1} бонус')
                    QApplication.processEvents()
                    if self.ui.btn_stop.isChecked():
                        self.ui.btn_stop.setChecked(False)
                        return

        self.ui.btn_loadBonuses.setText(f'Выгр. бонусы')

    def upload_task(self):
        my_session = en_engine_upload.get_auth_session(self.ui.lineEdit_domain.text(), self.ui.lineEdit_login.text(), self.ui.lineEdit_password.text())
        if not my_session:
            QMessageBox(text='Ошибка авторизации').exec()
            return
        task = ''
        match self.ui.tabWidget.currentIndex():
            case 0:
                with open('./patterns/olimp_task.txt', encoding='utf-8') as f:
                    task_pattern = f.read()
                with open('./patterns/olimp_rows.txt', encoding='utf-8') as f:
                    rows_pattern = f.read()
                rows = generate_olimp_rows(self.ui.spinBox_gridHeight.value(), rows_pattern, self.ui.spinBox_levelNum.value())
                task = task_pattern.replace('{generated_rows}', rows)
                task += generate_img_table(2**(self.ui.spinBox_gridHeight.value() - 1), self.ui.lineEdit_prefix.text(), self.ui.spinBox_levelNum.value(), self.ui.lineEdit_gameId.text())

            case 1:
                with open('./patterns/dump_task.txt', encoding='utf-8') as f:
                    task_pattern = f.read()
                task = task_pattern + generate_img_table(self.ui.tableWidget.rowCount()*2, self.ui.lineEdit_prefix.text(), self.ui.spinBox_levelNum.value(), self.ui.lineEdit_gameId.text())

        en_engine_upload.task_upload(my_session, task, self.ui.spinBox_levelNum.value(), self.ui.lineEdit_gameId.text(), self.ui.lineEdit_domain.text())

    ######### СВАЛКА #########
    # Генерация форматов свалки
    def gen_dump(self):
        match self.ui.comboBox_formatType.currentText():
            case 'Метаграмма':
                word1, word2 = gen_random_format('meta', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1} {word2}|{word2} {word1}')
            case 'Метаграмма 2':
                word1, word2 = gen_random_format('meta2', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1} {word2}|{word2} {word1}')
            case 'Логогриф':
                word1, word2 = gen_random_format('logo', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1} {word2}|{word2} {word1}')
            case 'Логогриф 2':
                word1, word2 = gen_random_format('logo2', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1} {word2}|{word2} {word1}')
            case 'Брюква':
                word1, word2 = gen_random_format('brukva', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1} {word2}|{word2} {word1}')
            case 'Гибрид 3':
                word1, word2 = gen_random_format('gib3', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1[:-3]}{word2}')
            case 'Гибрид 4':
                word1, word2 = gen_random_format('gib4', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1[:-4]}{word2}')
            case 'Плюсограмма':
                word1, word2 = gen_random_format('plus', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1} {word2}|{word2} {word1}')
            case 'Анаграмма':
                word1, word2 = gen_random_format('anag', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1} {word2}|{word2} {word1}')
            case 'Шарада':
                word1, word2 = gen_random_format('shar', self.my_dict)
                self.ui.lineEdit_answer.setText(f'{word1}{word2}')
        self.ui.lineEdit_dump1.setText(word1)
        self.ui.lineEdit_dump2.setText(word2)

    # Генерация случайных id для картинок свалки
    def gen_random_ids(self):
        mytablewidget = self.ui.tableWidget
        row_cnt = mytablewidget.rowCount()
        free_nums = [i for i in range(1, 2*row_cnt+1)]
        shuffle(free_nums)
        for i in range(row_cnt):
            mytablewidget.setItem(i, 4, QTableWidgetItem(str(free_nums.pop(0))))
            mytablewidget.setItem(i, 5, QTableWidgetItem(str(free_nums.pop(0))))

    # Добавляем формат свалки в таблицу
    def add_dump_row(self):
        mytablewidget = self.ui.tableWidget
        mytablewidget.insertRow(0)
        mytablewidget.setItem(0, 0, QTableWidgetItem(self.ui.comboBox_formatType.currentText()))
        mytablewidget.setCellWidget(0, 1, ImageWithLineedit(self.ui.lineEdit_dump1.text(), True))
        mytablewidget.setCellWidget(0, 2, ImageWithLineedit(self.ui.lineEdit_dump2.text(), True))
        mytablewidget.setItem(0, 3, QTableWidgetItem(self.ui.lineEdit_answer.text()))
        mytablewidget.resizeRowsToContents()
        mytablewidget.resizeColumnsToContents()
        self.gen_random_ids()
        self.ui.spinBox_endLoad.setValue(mytablewidget.rowCount())

    #############ОЛИМПИЙКА#############
    def clear_area(self):
        self.words_set = set()
        while self.ui.layout_olimp.count() > 0:
            item = self.ui.layout_olimp.takeAt(0)
            item.widget().deleteLater()

    def generate_olimp_grid(self):
        self.clear_area()
        olimp_height = self.ui.spinBox_gridHeight.value()
        self.ui.spinBox_endLoad.setValue(2**olimp_height-1)
        cnt = 0
        base_size = 200
        for i in range(olimp_height):
            for j in range(2**(olimp_height-i-1)):
                cnt += 1
                if i == 0:
                    my_widget = OlimpSector2(cnt, '', False, True)
                else:
                    my_widget = OlimpSector2(cnt, '', True, False)
                my_widget.setMinimumSize(base_size + 10, (base_size+50)*(2**i)+20)
                my_widget.groupBox.setMinimumSize(base_size, (base_size+50)*(2**i))
                self.ui.layout_olimp.addWidget(my_widget, (2**i)*j, i, 2**i, 1, alignment=Qt.AlignmentFlag.AlignCenter)
