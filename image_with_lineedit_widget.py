import re

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QFileDialog, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from random import randint
from urllib import parse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


class ImageWithLineedit(QWidget):
    def __init__(self, word, with_image):
        super(ImageWithLineedit, self).__init__()
        self.with_image = with_image
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(5, 15, 5, 5)

        self.lineedit = QLineEdit(self)
        self.lineedit.setText(word)
        self.layout.addWidget(self.lineedit)
        if with_image:
            self.label = QLabel(self)
            self.label.setPixmap(QPixmap('empty.png'))
            self.layout.addWidget(self.label)
            self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
            self.label.addAction('Загрузить картинку (Яндекс)', lambda: self.load_internet_img('yandex', self.window().ui.lineEdit_yandexClass.text(), 10))
            self.label.addAction('Загрузить картинку (Google)', lambda: self.load_internet_img('google', self.window().ui.lineEdit_googleClass.text(), 10))
            self.label.addAction('Загрузить с диска', self.load_local_img)

    def load_local_img(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Image files (*.png)')
        if fname[0]:
            pixmap = QPixmap(fname[0])
            self.label.setPixmap(pixmap.scaled(200, 200))

    def load_internet_img(self, search_engine, img_class, img_relevance):
        data = self.get_internet_image(self.lineedit.text(), randint(0, img_relevance), search_engine, img_class)
        if data:
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            self.label.setPixmap(pixmap.scaled(200, 200))
        QApplication.processEvents()

    def get_internet_image(self, word, image_number, search_type, img_class):
        match search_type:
            case 'yandex':
                url = f'https://yandex.ru/images/search?text={parse.quote_plus(word)}&iorient=square'
            case 'google':
                url = f'https://www.google.com/search?tbm=isch&as_q={parse.quote_plus(word)}&tbs=iar:s'
            case _:
                return
        req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
        rs = urlopen(req)
        html = BeautifulSoup(rs, 'html.parser')
        #print(html)
        if search_type == 'google':
            image_links = html.find_all('img', class_=img_class)
            if not image_links:
                print(f'возможно блокировка капчей {search_type} {rs.url}')
                return
            if image_number < len(image_links):
                url2 = image_links[image_number].get('src')
            else:
                url2 = image_links[randint(0, len(image_links) - 1)].get('src')

        if search_type == 'yandex':
            #regex_pattern = r'https://avatars\.mds\.yandex\.net/[^&]+?/orig'
            image_links = re.findall(img_class, str(html))
            image_links = list(map(lambda x: 'https://'+x, image_links))
            if not image_links:
                print(f'возможно блокировка капчей {search_type} {rs.url}')
                return
            if image_number < len(image_links):
                url2 = image_links[image_number]
            else:
                url2 = image_links[randint(0, len(image_links) - 1)]

        return urlopen(url2).read()
