from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia import QSound
from price_data import get_price
import os 
import sys 

class MainWindow(QMainWindow):  
    def __init__(self, *args, **kwargs): 
        super(MainWindow, self).__init__(*args, **kwargs) 
 
        self.tabs = QTabWidget()  
        self.tabs.setDocumentMode(True)  
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick) 
        self.tabs.setTabsClosable(True) 
        self.tabs.tabCloseRequested.connect(self.close_current_tab)  
        self.setCentralWidget(self.tabs)
        self.setWindowTitle("DeFi-Desktop | The ultimate DeFi desktop experience")
        self.showMaximized()

        self.status = QStatusBar()
        self.status.setFont(QFont('Segoe UI', 20)) 
        self.status.setStyleSheet("QStatusBar { border: 1px solid black } !important;") 
        self.setStatusBar(self.status)

        self.bitcoin_price = QLabel(get_price("bitcoin"))
        self.ethereum_price = QLabel(get_price("ethereum"))
        self.aave_price = QLabel(get_price("aave"))
        self.maker_price = QLabel(get_price("maker"))
        self.yfi_price = QLabel(get_price("yearn-finance"))
        self.uniswap_price = QLabel(get_price("uniswap"))
        self.sushiswap_price = QLabel(get_price("sushiswap"))
        self.compound_price = QLabel(get_price("compound"))
        self.snx_price = QLabel(get_price("synthetix-network-token"))

        coin_prices = [self.bitcoin_price, self.ethereum_price, self.aave_price, self.maker_price, self.yfi_price, self.uniswap_price, self.sushiswap_price, self.compound_price, self.snx_price]
        coin_names = ["Bitcoin: ", "Ethereum: ", "Aave: ", "Maker: ", "YFI: ", "Sushiswap: ", "Uniswap:", "Compound: ", "Synthetix: "]
        coin_images = ["btc25.png", "eth25.png", "aave25.png", "maker25.png", "yfi25.png", "uniswap25.png", "sushi25.png", "comp25.png", "snx25.png"]

        # Add widgets to status bar
        for i in range(0, 9):
            icon = QLabel()
            icon_pixmap = QPixmap('static/images/' + coin_images[i])
            icon.setPixmap(icon_pixmap)

            self.status.addWidget(VLine())
            self.status.addWidget(icon)
            self.status.addWidget(QLabel(coin_names[i]))
            self.status.addWidget(coin_prices[i])
        self.status.addWidget(VLine())

        self.setStyleSheet(""" QTabBar::tab:selected {background: AliceBlue;} <!--QTabWidget>QWidget>QWidget{background: red;}--> """)

        self.sound = QSound("static/sounds/update_sound.wav") # This plays when prices are updated.

        tab_list = {'http://app.aave.com': '         AAVE         ', 'http://compound.finance': '        Compound        ', 'http://oasis.app/borrow': '        MakerDAO        ', 'http://yearn.finance': '         Yearn         ', 'http://harvest.finance': '        Harvest        ', 'http://app.uniswap.org': '         Uniswap        ', 'http://sushiswap.fi': '         Sushiswap         ', 'http://zapper.fi': '         Zapper         '}
        
        # Create all tabs        
        for x in tab_list.keys():
            self.add_new_tab(QUrl(x), tab_list[x])

        self.update_prices()
        self.show() 
 
    def add_new_tab(self, qurl = None, label = "Blank"): 
   
        if qurl is None:  
            qurl = QUrl('http://www.google.com') 
   
        browser = QWebEngineView()  
        browser.setUrl(qurl) 
  
        # setting tab index 
        i = self.tabs.addTab(browser, label) 
        self.tabs.setCurrentIndex(i) 
  
        # adding action to the browser when loading is finished 
        # set the tab title 
        browser.loadFinished.connect(lambda _, i = i, browser = browser: self.tabs.setTabText(i, label)) 
  
    def tab_open_doubleclick(self, i):   
        if i == -1: # No tab under the click
            self.add_new_tab()
   
    def close_current_tab(self, i):  
        if self.tabs.count() < 2: # if there is only one tab
            return 
        self.tabs.removeTab(i)

    def update_prices(self):
        try:
            self.bitcoin_price.setText(get_price("bitcoin"))
            self.ethereum_price.setText(get_price("ethereum"))
            self.aave_price.setText(get_price("aave"))
            self.maker_price.setText(get_price("maker"))
            self.yfi_price.setText(get_price("yearn-finance"))
            self.uniswap_price.setText(get_price("uniswap"))
            self.sushiswap_price.setText(get_price("sushiswap"))
            self.sound.play()
            print("All cryptocurrency prices have been updated!")
        finally:
            QTimer.singleShot(600000, self.update_prices) # 10m

class VLine(QFrame):
    def __init__(self):
        super(VLine, self).__init__()
        self.setFrameShape(self.VLine|self.Sunken)
