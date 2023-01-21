import urllib
import urllib.parse
import ssl
import urllib3
import random
from bs4 import BeautifulSoup
from time import sleep

from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QPushButton, QMessageBox
from PySide6.QtGui import QPalette, QColor, QPixmap
from PySide6.QtCore import Qt
from image_with_lineedit_widget import ImageWithLineedit


class OlimpSector2(QWidget):
    def __init__(self, widget_id, word, with_load_button, with_image):
        super(OlimpSector2, self).__init__()
        self.widget_id = widget_id

        self.setAutoFillBackground(True)
        pal = QPalette()
        pal.setColor(self.backgroundRole(), QColor(100, 180, 200))
        self.setPalette(pal)

        self.groupBox = QGroupBox(self)
        self.groupBox.setTitle(str(widget_id))
        self.groupBox.setContentsMargins(0, 0, 0, 0)

        self.my_layout = QVBoxLayout(self.groupBox)
        self.my_layout.setAlignment(Qt.AlignCenter)
        self.my_layout.setContentsMargins(0, 0, 0, 0)
        self.image_widget = ImageWithLineedit(word, with_image)
        self.my_layout.addWidget(self.image_widget)

        if with_load_button:
            self.btn_loadChildAssoc = QPushButton(self.groupBox)
            self.btn_loadChildAssoc.setText('Загрузить дочерние ассоциации')
            self.my_layout.addWidget(self.btn_loadChildAssoc)
            self.btn_loadChildAssoc.clicked.connect(lambda: self.window().thread_manager.start(self.load_child_assoc))

    def parse_assoc(self, word):
        url = 'https://sociation.org/word/' + urllib.parse.quote_plus(word) + '/'
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        http = urllib3.PoolManager(ssl_version=ssl.PROTOCOL_TLS, ssl_context=ctx)
        rs = http.request("GET", url, preload_content=False).read()
        html = BeautifulSoup(rs, 'html.parser')
        if html.find('ol', class_='associations_list self-clear'):
            parse_set = html.find('ol', class_='associations_list self-clear').findAll('a')
            return [a.text for a in parse_set]
        else:
            return

    def load_child_assoc(self, assoc_list=[]):
        if self.window().ui.btn_stop.isChecked():
            self.window().ui.btn_stop.setChecked(False)
            return

        pal = self.palette()
        pal.setColor(self.backgroundRole(), Qt.darkGreen)
        self.setPalette(pal)

        max_retries = 10
        main_window = self.window()
        relevance = main_window.ui.spinBox_assocRelevance.value()
        sectors_count = main_window.ui.layout_olimp.count()
        word = self.image_widget.lineedit.text()
        main_window.words_set.add(word)
        if not assoc_list:
            assoc_list = self.parse_assoc(word)

        child1_num = sectors_count - (sectors_count - self.widget_id + 1) * 2
        child1 = main_window.ui.layout_olimp.itemAt(child1_num - 1).widget()
        child2_num = sectors_count - (sectors_count - self.widget_id + 1) * 2 + 1
        child2 = main_window.ui.layout_olimp.itemAt(child2_num - 1).widget()

        for i in range(max_retries):
            word1 = assoc_list.pop(random.randint(0, min(len(assoc_list) - 1, relevance)))
            sleep(main_window.ui.spinBox_assocDelay.value() / 1000)
            word1_assoc_list = [*filter(lambda x: (' ' not in x) and (x not in main_window.words_set), self.parse_assoc(word1))]
            if len(word1_assoc_list) > 3:
                break
        if i == max_retries:
            QMessageBox(text='Олимпийка сгенерирована не полностью, попробуйте догенерировать').exec()
            return

        main_window.words_set.add(word1)
        child1.image_widget.lineedit.setText(word1)
        if child1.image_widget.with_image:
            child1.image_widget.label.setPixmap(QPixmap('empty.png'))

        if child1_num > sectors_count / 2 + 1:
            child1.load_child_assoc(assoc_list=word1_assoc_list)
        else:
            pal = child1.palette()
            pal.setColor(child1.backgroundRole(), Qt.darkGreen)
            child1.setPalette(pal)

        for i in range(max_retries):
            word2 = assoc_list.pop(random.randint(0, min(len(assoc_list) - 1, relevance)))
            sleep(main_window.ui.spinBox_assocDelay.value() / 1000)
            word2_assoc_list = [*filter(lambda x: (' ' not in x) and (x not in main_window.words_set), self.parse_assoc(word2))]
            if len(word2_assoc_list) > 3:
                break
        if i == max_retries:
            QMessageBox(text='Олимпийка сгенерирована не полностью, попробуйте догенерировать').exec()
            return

        main_window.words_set.add(word2)
        child2.image_widget.lineedit.setText(word2)
        if child2.image_widget.with_image:
            child2.image_widget.label.setPixmap(QPixmap('empty.png'))
        if child2_num > sectors_count / 2 + 1:
            child2.load_child_assoc(assoc_list=word2_assoc_list)
        else:
            pal = child2.palette()
            pal.setColor(child2.backgroundRole(), Qt.darkGreen)
            child2.setPalette(pal)
