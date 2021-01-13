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

        self.status = QStatusBar()
        self.status.setFont(QFont('Segoe UI', 20)) 
        self.status.setStyleSheet("QStatusBar { border: 1px solid black } !important;") 
        self.setStatusBar(self.status)

        bitcoin_label = QLabel("Bitcoin: ")
        self.bitcoin_price = QLabel(get_price("bitcoin"))
        ethereum_label = QLabel("Ethereum: ")
        self.ethereum_price = QLabel(get_price("ethereum"))
        aave_label = QLabel("Aave: ")
        self.aave_price = QLabel(get_price("aave"))
        maker_label = QLabel("Maker: ")
        self.maker_price = QLabel(get_price("maker"))
        yfi_label = QLabel("YFI: ")
        self.yfi_price = QLabel(get_price("yearn-finance"))
        uniswap_label = QLabel("Uniswap: ")
        self.uniswap_price = QLabel(get_price("uniswap"))
        sushiswap_label = QLabel("Sushiswap: ")
        self.sushiswap_price = QLabel(get_price("sushiswap"))
        compound_label = QLabel("Compound: ")
        self.compound_price = QLabel(get_price("compound"))
        snx_label = QLabel("Synthetix: ")
        self.snx_price = QLabel(get_price("synthetix-network-token"))

        btc = QLabel()
        btc_pixmap = QPixmap('static/images/btc25.png')
        btc.setPixmap(btc_pixmap)

        eth = QLabel()
        eth_pixmap = QPixmap('static/images/eth25.png')
        eth.setPixmap(eth_pixmap)

        aave = QLabel()
        aave_pixmap = QPixmap('static/images/aave25.png')
        aave.setPixmap(aave_pixmap)

        maker = QLabel()
        maker_pixmap = QPixmap('static/images/maker25.png')
        maker.setPixmap(maker_pixmap)

        yfi = QLabel()
        yfi_pixmap = QPixmap('static/images/yfi25.png')
        yfi.setPixmap(yfi_pixmap)

        uniswap = QLabel()
        uniswap_pixmap = QPixmap('static/images/uniswap25.png')
        uniswap.setPixmap(uniswap_pixmap)

        sushiswap = QLabel()
        sushiswap_pixmap = QPixmap('static/images/sushi25.png')
        sushiswap.setPixmap(sushiswap_pixmap)

        compound = QLabel()
        compound_pixmap = QPixmap('static/images/comp25.png')
        compound.setPixmap(compound_pixmap)

        snx = QLabel()
        snx_pixmap = QPixmap('static/images/snx25.png')
        snx.setPixmap(snx_pixmap)

        self.status.addWidget(VLine())
        self.status.addWidget(btc)
        self.status.addWidget(bitcoin_label)
        self.status.addWidget(self.bitcoin_price)
        self.status.addWidget(VLine())
        self.status.addWidget(eth)
        self.status.addWidget(ethereum_label)
        self.status.addWidget(self.ethereum_price)
        self.status.addWidget(VLine())
        self.status.addWidget(aave)
        self.status.addWidget(aave_label)
        self.status.addWidget(self.aave_price)
        self.status.addWidget(VLine())
        self.status.addWidget(maker)
        self.status.addWidget(maker_label)
        self.status.addWidget(self.maker_price)
        self.status.addWidget(VLine())
        self.status.addWidget(yfi)
        self.status.addWidget(yfi_label)
        self.status.addWidget(self.yfi_price)
        self.status.addWidget(VLine())
        self.status.addWidget(uniswap)
        self.status.addWidget(uniswap_label)
        self.status.addWidget(self.uniswap_price)
        self.status.addWidget(VLine())
        self.status.addWidget(sushiswap)
        self.status.addWidget(sushiswap_label)
        self.status.addWidget(self.sushiswap_price)
        self.status.addWidget(VLine())
        self.status.addWidget(compound)
        self.status.addWidget(compound_label)
        self.status.addWidget(self.compound_price)
        self.status.addWidget(VLine())
        self.status.addWidget(snx)
        self.status.addWidget(snx_label)
        self.status.addWidget(self.snx_price)
        self.status.addWidget(VLine())

        self.setStyleSheet(""" QTabBar::tab:selected {background: AliceBlue;} <!--QTabWidget>QWidget>QWidget{background: red;}--> """)

        self.sound = QSound("static/sounds/update_sound.wav") # This plays when prices are updated.

        # Creating first tabs 
        self.add_new_tab(QUrl('http://app.aave.com'), '         AAVE         ')
        self.add_new_tab(QUrl('http://compound.finance'), '        Compound        ')
        self.add_new_tab(QUrl('http://oasis.app/borrow'), '        MakerDAO        ')
        self.add_new_tab(QUrl('http://yearn.finance'), '         Yearn         ')
        self.add_new_tab(QUrl('http://harvest.finance'), '        Harvest        ')
        self.add_new_tab(QUrl('http://app.uniswap.org'), '         Uniswap        ')
        self.add_new_tab(QUrl('http://sushiswap.fi'), '         Sushiswap         ')
        self.add_new_tab(QUrl('http://zapper.fi'), '         Zapper         ') 

        self.update_prices() # Timer to update cryptocurrency prices

        self.show() 
   
        self.setWindowTitle("DeFi-Desktop | The ultimate DeFi desktop experience")
        self.showMaximized()

    def add_new_tab(self, qurl = None, label = "Blank"): 
   
        if qurl is None:  
            qurl = QUrl('http://www.google.com') 
   
        browser = QWebEngineView()  
        browser.setUrl(qurl) 
  
        # Set tab index
        i = self.tabs.addTab(browser, label) 
        self.tabs.setCurrentIndex(i) 
  
        browser.loadFinished.connect(lambda _, i = i, browser = browser: self.tabs.setTabText(i, label)) 
  
    def tab_open_doubleclick(self, i):  
        # No tab under the click 
        if i == -1:  
            self.add_new_tab()
   
    def close_current_tab(self, i):  
        if self.tabs.count() < 2:  # if there is only one tab
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
    # a simple VLine, like the one you get from designer
    def __init__(self):
        super(VLine, self).__init__()
        self.setFrameShape(self.VLine|self.Sunken)
