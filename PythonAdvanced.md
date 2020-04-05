
# Table of Contents

1.  [Python套件管理](#org0269362)
    1.  [pip v.s. conda](#org1d5ade8)
        1.  [pip or conda](#orga391ae1)
        2.  [pip](#org8787687)
        3.  [conda](#orgb476c7b)
        4.  [In both cases:](#orgde19cbe)
        5.  [difference between conda, anaconda, and miniconda ](#orgec76e82)
    2.  [conda安裝與使用](#orge01e2c9)
        1.  [下載 v.s. 安裝](#org6c037aa)
        2.  [常見 conda 指令](#org25aa33c)
    3.  [Python常用函式庫](#org4c9708e)
        1.  [爬蟲](#org2fa9a88)
        2.  [網站](#org5fbe339)
        3.  [資料處理科學計算](#orge32411e)
        4.  [視覺化](#orgbe12028)
        5.  [機器學習](#org579430d)
        6.  [地圖學/地圖視覺化](#orgf6ac324)
        7.  [ArcGIS](#orga5dfa68)
    4.  [python package安裝(conda)](#org85c6895)
    5.  [python執行環境建立與維護](#org0690cf0)
2.  [Numpy模組](#org8a2ed87)
    1.  [Numpy](#orgb14d5df)
    2.  [匯入模組](#org218320d)
    3.  [Create ndarray](#orgf5ad278)
        1.  [一維陣列](#orgef63c24)
        2.  [二維陣列](#org0ff8958)
        3.  [多維陣列](#org4c46aaa)
        4.  [隨機矩陣](#orga3236d0)
3.  [Matplotlib](#orga838e38)
    1.  [Matplotlib簡介](#org523520c)
    2.  [折線圖](#org35777ec)
        1.  [基本語法](#org786f4d9)
        2.  [練習1：繪製折線圖](#orgabba7f5)
        3.  [圖形美化: plot() function](#orgc266607)
            1.  [plot()函式參數可分為兩類：fmt字串 和 kwarg參數](#org0384676)
            2.  [kwgarg參數](#org85d6718)
            3.  [色彩對照](#org7e152ca)
            4.  [折線示範#1](#orge1ca7f8)
            5.  [折線示範#2](#org954f98c)
            6.  [其他參數](#orga996960)
        4.  [練習2：圖表美化](#orgbd8e5cb)
    3.  [bar chart: plt.bar()](#orgd6b7bcf)
    4.  [pie chart: plt.pie()](#org8ba3e4b)
        1.  [語法： ](#orge8a2970)
        2.  [參數：](#orgd3fc874)
        3.  [範例](#org1d9172e)
    5.  [其它圖表](#orgd8e0482)
    6.  [文字註解: plt.text()](#orgd6ed9f4)
        1.  [語法](#orgefa3ff7)
        2.  [範例](#org89fbe43)
    7.  [子圖表: plt.subplot()](#org21b0fbd)
4.  [區域資料檔分析](#org47d5ae0)
    1.  [Excel/CSV: Pandas模組](#org1697bd2)
        1.  [CSV](#orgcdb9c08)
        2.  [Pandas](#org15f6486)
        3.  [Pandas資料結構](#org78eb494)
    2.  [Pandas functions](#org4593917)
        1.  [資料選取](#org9ab2110)
            1.  [Select as dictinoary (column): ](#orga3584e8)
            2.  [Select using index (row):](#orgacaacda)
            3.  [loc, iloc, between ](#orgc708ccf)
        2.  [條件式選取資料](#org60f30cc)
            1.  [語法](#orga9863eb)
            2.  [範例](#org7ed0017)
    3.  [進階分析](#org1abc7d8)
        1.  [計算: Aggregation, Groupby](#orgac01ec3)
            1.  [create new column based on other column](#orge087879)
            2.  [simple aggregation](#org32b61b2)
            3.  [groupby with aggregation function](#org1d073e1)
            4.  [範例](#org86df465)
        2.  [資料檔下載: file:scores.csv](#orgbd64f19)
    4.  [資料視覺化](#org3e73a3e)
        1.  [Bar chart](#orgd9a508e)
        2.  [Pie chart](#orgb473491)
        3.  [Scatter chart](#orgb9de778)
        4.  [Line chart](#org41051e9)
5.  [網路爬蟲](#org495eca5)
    1.  [parse JSON](#org4816b7a)
        1.  [What is JSON?](#orgd9a1c14)
        2.  [JSON的優點](#org2ed2515)
        3.  [JSON結構](#org0fcf257)
        4.  [實作1: 國際主要國家貨幣每月匯率概況](#org8833f59)
            1.  [下載JSON](#org2bd8556)
            2.  [資料視覺化](#orgc0bd9aa)
        5.  [實作2: 澎湖生活博物館每月參觀人次統計資料](#orgd72d30b)
        6.  [實作3: 下載JSON](#orgc6f6761)
        7.  [實作: 解析JSON](#org585ad27)
        8.  [練習](#orge1abd9d)
    2.  [parse HTML](#org493faed)
        1.  [所需套件](#orgd7af94f)
    3.  [範例: 以程式抓取PTT電影板header](#org568a4dc)
        1.  [原則](#org115394f)
        2.  [實作: 取得HTML資料](#org1804dec)
            1.  [第一版](#orga7e0ec7)
            2.  [第二版:加入header](#org61fbaec)
        3.  [實作：解析HTML資料內容](#org3629082)
            1.  [安裝解析HTML所需套件](#org7afeb4c)
            2.  [第三版: 解析HTML](#org4496c5c)
            3.  [第四版: 解析HTML](#org657c8fc)
6.  [如何把python程式publish成網站應用程式](#orgab3faec)



<a id="org0269362"></a>

# Python套件管理


<a id="org1d5ade8"></a>

## pip v.s. conda


<a id="orga391ae1"></a>

### pip or conda

-   Python的一大優勢之一便是龐大的第三方函式庫，讓使用python的程式設計師可以方便的呼叫、進行如網路資料下載解析、資料的視覺化、甚或是大數據的複雜分析與人工智慧的相關套件。，
-   目前用來管理這些龐大套件的工具主要有二：pip與Conda。


<a id="org8787687"></a>

### pip

-   Pip是[Python Packaging Authority](https://www.pypa.io/en/latest/)推薦、用於從[Python Package Index](https://pypi.org/)安裝套件的工具，提供了對Python 套件的搜㝷、下載、安裝、卸載的功能。
-   若在 python.org 下載最新版本的python，則已內建pip安裝套件。 Python 3.4+ 以上版本均已包括pip
-   該工具類似Linux下的apt/yum或MAC下的[Homebrew](https://brew.sh/index_zh-tw)。


<a id="orgb476c7b"></a>

### conda

-   Conda 是一個開源的跨平台工具軟體，它被設計作為 Python、R、Lua、Scala 與 Java 等任何程式語言的套件、依賴性以及工作環境管理員，特別受到以 Python 作為主要程式語言的資料科學團隊所喜愛。
-   傳統 Python 使用者以 pip 作為套件管理員（package manager）、以 venv 作為工作環境管理員（environment manager），而 conda 則達成了「兩個願望、一次滿足」既可以管理套件亦能夠管理工作環境。<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>


<a id="orgde19cbe"></a>

### In both cases:

-   Written in Python
-   Open source (Conda is BSD and pip is MIT)


<a id="orgec76e82"></a>

### difference between conda, anaconda, and miniconda <sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup>

-   conda is both a command line tool, and a python package.
-   Anaconda發行版會預裝很多pydata生態圈裡的軟件，而Miniconda是最小的conda安裝環境， 一個乾淨的conda環境。
-   pip  只是運與安裝python package，而conda 用來安裝管理任何語言的包。
-   不一定要安裝Anaconda或Miniconda，也可透過pip直接安裝conda  
    
        pip install conda


<a id="orge01e2c9"></a>

## conda安裝與使用


<a id="org6c037aa"></a>

### 下載 v.s. 安裝

-   [Anaconda](https://www.anaconda.com/distribution/)
-   [Miniconda](https://docs.conda.io/en/latest/miniconda.html)


<a id="org25aa33c"></a>

### 常見 conda 指令

-   ` conda --version `: 檢視 conda 版本
-   ` conda update PACKAGE_NAME `: 更新指定套件
-   ` conda --help `: 檢視 conda 指令說明文件
-   ` conda list `: 檢視目前工作環境安裝的套件清單
-   ` conda list --ENVIRMOMENT `: 檢視指定工作環境安裝的套件清單
-   ` conda install PACKAGE_NAME=Version `: 在目前的工作環境安裝指定套件
-   ` conda remove PACKAGE_NAME `: 在目前的工作環境移除指定套件
-   ` conda create --name ENVIRMOMENT python=Version `: 建立新的工作環境且安裝指定 Python 版本
-   ` conda activate ENVIRONMENT `: 切換至指定工作環境
-   ` conda deactivate `: 回到 base 工作環境
-   ` conda env export --name ENVIRMOMENT --file ENVIRMOMENT.yml `: 將指定工作環境之設定匯出為 .yml 檔藉此複製且重現工作環境


<a id="org4c9708e"></a>

## Python常用函式庫


<a id="org2fa9a88"></a>

### 爬蟲

-   Scrapy: 舉世聞名，分散式爬蟲框架，不僅僅是簡單的庫
-   beautifulsoup4: Beautiful Soup 是一個可以從HTML或XML文件中提取數據的Python庫.<sup><a id="fnr.3" class="footref" href="#fn.3">3</a></sup>
-   urllib/urllib2: urllib is a package that collects several modules for working with URLs
-   selenium: Selenium原為網頁測試工具，但由於可以直接以程式碼操控瀏覽器的特性，使其成為網路爬蟲必備的工具之一。<sup><a id="fnr.4" class="footref" href="#fn.4">4</a></sup>


<a id="org5fbe339"></a>

### 網站

-   Django: 重量級網頁框架
-   Flask: 輕量級網頁框架


<a id="orge32411e"></a>

### 資料處理科學計算

-   Numpy: 陣列矩陣神器
-   Scipy: 科學計算神器
-   Pandas


<a id="orgbe12028"></a>

### 視覺化

-   matplotlib: matlab風格式的套件
-   seaborn: 散點圖矩陣神器
-   ggplot: R語言視覺化神器的Python版本
-   plotly: 這個神器是個js庫，不過也有各種流行的語言介面


<a id="org579430d"></a>

### 機器學習

-   scikit-learn:幾乎所有機器學習演算法都囊括
-   NLTK: 自然語言處理工具套件
-   Theano/TensorFlow/Keras: 深度學習套件
-   PyTorch: Numpy的GPU版


<a id="orgf6ac324"></a>

### 地圖學/地圖視覺化

-   basemap/cartopy: 畫地圖的package
-   Folium: leaflet的Python版本
-   GDAL: 開源GIS package
-   geocoder: 地理編碼神器
-   geopandas: 地理資料的熊貓套件
-   PySAL: 空間計量經濟學的一個神套件


<a id="orga5dfa68"></a>

### ArcGIS

-   arcpy: ArcGIS內嵌Python的神器，可以非常方便呼叫ArcGIS各項功能，但是有一點就是不開源（畢竟人家是商業軟體嘛，所以那些老想著在自己安裝的Python上import arcpy的同學可以省省
-   ArcGIS API for Python: 基於portal和online的一套API，還是有些可以玩的價值，後面也會考慮介紹這個內容。


<a id="org85c6895"></a>

## python package安裝(conda)

-   安裝package:  
    ` conda install packageName `  
    
        1    conda install pandas
-   移除package:  
    ` conda remove packageName `  
    
        1    conda remove pandas
-   安裝特定版本python  
    ` conda install python=version `  
    
        1    conda install python=3.5
-   了解目前系統可用套件  
    
        1      conda list


<a id="org0690cf0"></a>

## python執行環境建立與維護<sup><a id="fnr.5" class="footref" href="#fn.5">5</a></sup>

-   建立  
    
        1    conda create -n envName
-   啟用  
    
        1      source activate envName
-   退出  
    
        1      source deactiveate
-   刪除  
    
        1      conda env remove -n envName
-   列出目前系統中所有的虛擬環境  
    
        1      conda env list


<a id="org8a2ed87"></a>

# Numpy模組


<a id="orgb14d5df"></a>

## Numpy

-   Numpy 是 Python 的一個重要模組，主要用於資料處理上。Numpy 底層以 C 和 Fortran 語言實作，所以能快速操作多重維度的陣列。<sup><a id="fnr.6" class="footref" href="#fn.6">6</a></sup>
-   當 Python 處理龐大資料時，其原生 list 效能表現並不理想（但可以動態存異質資料），而 Numpy 具備平行處理的能力，可以將操作動作一次套用在大型陣列上。
-   Python 其餘重量級的資料科學相關套件（例如：Pandas、SciPy、Scikit-learn 等）都幾乎是奠基在 Numpy 的基礎上。因此學會 Numpy 對於往後學習其他資料科學相關套件打好堅實的基礎。


<a id="org218320d"></a>

## 匯入模組

-   使用模組裡的函式要加模組名稱  
    
        import numpy
-   匯入numpy模組並使用np作為簡寫，這是Numpy官方倡導的寫法  
    
        import numpy as np
-   Numpy中的多維資料型別稱為ndarray


<a id="orgf5ad278"></a>

## Create ndarray

-   Numpy 的重點在於陣列的操作，其所有功能特色都建築在同質且多重維度的 ndarray（N-dimensional array）上。
-   ndarray 的關鍵屬性是維度（ndim）、形狀（shape）和數值類型（dtype）。 一般我們稱一維陣列為 vector 而二維陣列為 matrix<sup><a id="fnr.6.100" class="footref" href="#fn.6">6</a></sup>。


<a id="orgef63c24"></a>

### 一維陣列

-   list 或 tuple 轉入  
    
        1      import numpy as np
        2      np1 = np.array( [1, 2, 3, 4] )
        3      print(np1)
    
        [1 2 3 4]

-   使用 np.arange( ) 方法  
    
        1    import numpy as np
        2    np2 = np.arange(5)
        3    print(np2)
    
        [0 1 2 3 4]


<a id="org0ff8958"></a>

### 二維陣列

    1    import numpy as np
    2    np4 = np.array( [[1, 2, 4], [3,4,5]])
    3    print("np4:\n", np4)
    4    
    5    np5 = np.array([np.arange(3), np.arange(3)])
    6    print('np5:\n', np5)
    7    
    8    np6 = np.arange(8).reshape(2, 4)
    9    print('np6:\n', np6)

    np4:
     [[1 2 4]
     [3 4 5]]
    np5:
     [[0 1 2]
     [0 1 2]]
    np6:
     [[0 1 2 3]
     [4 5 6 7]]


<a id="org4c46aaa"></a>

### 多維陣列

    1    import numpy as np
    2    
    3    np7 = np.arange(24).reshape(2, 3, 4)
    4    print('np7:\n',np7)

    np7:
     [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]


<a id="orga3236d0"></a>

### 隨機矩陣

    1    import numpy as np
    2  
    3    np8 = np.random.random((3, 2)) #矩陣大小以tuple表示
    4    print('np8:\n', np8)
    5  
    6    np9 = np.random.randint(0, 100, size=[4, 3]) #矩陣大小以list表示
    7    print('np9:\n', np9)

    np8:
     [[0.64716686 0.89109206]
     [0.86738452 0.95346256]
     [0.40312749 0.71623046]]
    np9:
     [[32 82 99]
     [88 41  3]
     [72 58 79]
     [66 85  5]]


<a id="orga838e38"></a>

# Matplotlib


<a id="org523520c"></a>

## Matplotlib簡介

-   NumPy的可視化操作界面
-   為Python最多人使用的2D繪圖工具
-   優點：圖形美觀、類型多、相容於Matlab
-   官方社群網站 <https://matplotlib.org/>
-   維基百科 <https://zh.wikipedia.org/wiki/Matplotlib>


<a id="org35777ec"></a>

## 折線圖


<a id="org786f4d9"></a>

### 基本語法

-   import matplotlib.pyplot as plt
-   plt.plot( )函式為matplotlib.pyplot模組畫線條方法，其語法如下   
    
        1      plt.plot( [x座標資料,] y座標資料 [, 參數1, 參數2, ...] )
-   np.sin( )函式為Numpy模組求正弦值
-   plt.show( )函式用來顯示圖形

    1    import matplotlib.pyplot as plt
    2    import numpy as np
    3  
    4    x = np.arange(-3, 3, 0.01)
    5    plt.clf()
    6    plt.plot(x, np.sin(x))
    7    # for web-based: plt.show() 
    8  
    9    plt.savefig('SimpleSin.png', dpi=300)

![img](simpleSin.png "簡單的sin圖形")  


<a id="orgabba7f5"></a>

### <a id="orga28ea3b"></a>練習1：繪製折線圖

-   利用 list 繪製   
    -   x1 = [1, 2, 3, 4, 5, 6] 
    -   y1 = [1, 2, 3, 4, 5, 6] 
-   執行 plt.plot(y1) 和 plt.plot(x1, y1) 有何差別??
-   利用 numpy 繪製   
    -   x2 = np.arange(0, 3, 0.01) 
-   執行plt.plot(x2, x2\*\*2)看看畫出什麼圖形??


<a id="orgc266607"></a>

### 圖形美化: plot() function


<a id="org0384676"></a>

#### plot()函式參數可分為兩類：fmt字串 和 kwarg參數

-   fmt 定義基本格式：顏色、標記、線條樣式
-   kwarg 為Line2D屬性(參考資料)：color, linestyle, marker, label, linewidth, ….
-   若 fmt 和 kwarg 設定衝突時，以 kwarg 為主
-   plot(): fmt字串

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">字元</th>
<th scope="col" class="org-left">顏色</th>
<th scope="col" class="org-left">字元</th>
<th scope="col" class="org-left">標記</th>
<th scope="col" class="org-left">字元</th>
<th scope="col" class="org-left">標記</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">&rsquo;b&rsquo;</td>
<td class="org-left">藍</td>
<td class="org-left">&rsquo;.&rsquo;</td>
<td class="org-left">點</td>
<td class="org-left">&rsquo;\*&rsquo;</td>
<td class="org-left">\*</td>
</tr>


<tr>
<td class="org-left">&rsquo;g&rsquo;</td>
<td class="org-left">綠</td>
<td class="org-left">&rsquo;o&rsquo;</td>
<td class="org-left">圓圈</td>
<td class="org-left">&rsquo;+&rsquo;</td>
<td class="org-left">+</td>
</tr>


<tr>
<td class="org-left">&rsquo;r&rsquo;</td>
<td class="org-left">紅</td>
<td class="org-left">&rsquo;v&rsquo;</td>
<td class="org-left">三角形(下)</td>
<td class="org-left">&rsquo;x&rsquo;</td>
<td class="org-left">x</td>
</tr>


<tr>
<td class="org-left">&rsquo;c&rsquo;</td>
<td class="org-left">青</td>
<td class="org-left">&rsquo;^&rsquo;</td>
<td class="org-left">三角形(上)</td>
<td class="org-left">&rsquo;d&rsquo;</td>
<td class="org-left">鑽石</td>
</tr>


<tr>
<td class="org-left">&rsquo;m&rsquo;</td>
<td class="org-left">洋紅</td>
<td class="org-left">&rsquo;<&rsquo;</td>
<td class="org-left">三角形(左)</td>
<td class="org-left">字元</td>
<td class="org-left">線條</td>
</tr>


<tr>
<td class="org-left">&rsquo;y&rsquo;</td>
<td class="org-left">黃</td>
<td class="org-left">&rsquo;>&rsquo;</td>
<td class="org-left">三角形(右)</td>
<td class="org-left">&rsquo;-&rsquo;</td>
<td class="org-left">實線</td>
</tr>


<tr>
<td class="org-left">&rsquo;k&rsquo;</td>
<td class="org-left">黑</td>
<td class="org-left">&rsquo;s&rsquo;</td>
<td class="org-left">正方形</td>
<td class="org-left">&rsquo;&#x2013;&rsquo;/&rsquo;:&rsquo;</td>
<td class="org-left">虛線</td>
</tr>


<tr>
<td class="org-left">&rsquo;w&rsquo;</td>
<td class="org-left">白</td>
<td class="org-left">&rsquo;p&rsquo;</td>
<td class="org-left">五邊形</td>
<td class="org-left">&rsquo;-.&rsquo;</td>
<td class="org-left">-.-.-.-.</td>
</tr>
</tbody>
</table>


<a id="org85d6718"></a>

#### kwgarg參數

-   colorg  
    -   單字，如g：color = &rsquo;lime&rsquo;
    -   字母，如g：color = &rsquo;k&rsquo;
    -   色碼，如g：color = &rsquo;#FF0000&rsquo;
    -   RGB值(0~g1之間)，如：color = (1, 0, 0)
-   label：g呈現線條標籤，如 label = &rsquo;y = x<sup>2</sup>&rsquo;  
    -   需搭配 pglt.legend()函式方能呈現 label


<a id="org7e152ca"></a>

#### 色彩對照

![img](colors.jpg "色表")  


<a id="orge1ca7f8"></a>

#### 折線示範#1

    1    import matplotlib.pyplot as plt
    2    import numpy as np
    3  
    4    x1 = [1, 2, 3, 4, 5, 6]
    5    y1 = [1, 2, 3, 4, 5, 6]
    6    plt.clf()
    7    plt.plot(x1, y1, color='c', linestyle='-', marker='p')
    8    plt.savefig('line1.png', dpi=300)

![img](line1.png "簡單的折線圖形#1")  


<a id="org954f98c"></a>

#### 折線示範#2

     1    import matplotlib.pyplot as plt
     2    import numpy as np
     3  
     4    x1 = [1, 2, 3, 4, 5, 6]
     5    y1 = [1, 2, 3, 4, 5, 6]
     6    x2 = np.arange(0, 3, 0.01)
     7    x3 = np.arange(8).reshape(2, 4)
     8  
     9    plt.plot(y1, 'c-p', x2, x2**2, x3, x3+3, '-*')
    10    plt.savefig('line2.png', dpi=300)

![img](line2.png "簡單的折線圖形2")  


<a id="orga996960"></a>

#### 其他參數

-   x / y 座標範圍：plt.xlim(起始值, 終止值)  / plt.ylim(起, 止)
-   圖表標題：plt.title(字串)
-   x / y 座標標題：plt.xlabel(字串) / plt.ylabel(字串)
-   顯示kwarg參數裡的label：plt.legend()


<a id="orgbd8e5cb"></a>

### <a id="org790760d"></a>練習2：圖表美化

1.  將[3.2.2](#orga28ea3b)的圖表加上標記、線條標籤，換線條顏色、線條樣式
2.  請將下列資料繪成折線圖(男女折線不同顏色、樣式，加標記)  
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">初婚年齡</th>
    <th scope="col" class="org-right">2006</th>
    <th scope="col" class="org-right">2011</th>
    <th scope="col" class="org-right">2014</th>
    <th scope="col" class="org-right">2015</th>
    <th scope="col" class="org-right">2016</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">男</td>
    <td class="org-right">30.7</td>
    <td class="org-right">31.8</td>
    <td class="org-right">32.1</td>
    <td class="org-right">32.2</td>
    <td class="org-right">32.4</td>
    </tr>
    
    
    <tr>
    <td class="org-left">女</td>
    <td class="org-right">27.8</td>
    <td class="org-right">29.4</td>
    <td class="org-right">29.9</td>
    <td class="org-right">30.0</td>
    <td class="org-right">30.0</td>
    </tr>
    </tbody>
    </table>
    
    -   圖表標題: Age of first marriage 
    -   座標軸標題: x ⇒ Year、y ⇒ Age 
    -   線條標籤: 男 ⇒ Male、女 ⇒ Female


<a id="orgd6b7bcf"></a>

## bar chart: plt.bar()

-   語法  
    ` plt.bar( x座標資料, y座標資料 [, 參數1, 參數2, ...] ) `
-   練習3: 請將[3.2.4](#org790760d)的男女初婚年齡改成長條圖


<a id="org8ba3e4b"></a>

## pie chart: plt.pie()


<a id="orge8a2970"></a>

### 語法： 

plt.pie( 比例列表 [, 參數1, 參數2, &#x2026;] )  


<a id="orgd3fc874"></a>

### 參數：

-   colors：各子圖顏色，多以 list 表示
-   labels：各子圖標籤，多以 list 表示
-   explode：各子圖分離突出比例，0.1代表分離10%，多以 list 表示
-   autopct：顯示各子圖比例值，格式為%x.y%%
-   startangle：繪製起始角度，預設為0 (與三角函數角度相同)
-   若要以正圓形繪製，請再加上plt.axis(&rsquo;equal&rsquo;)


<a id="org1d9172e"></a>

### 範例

     1    import matplotlib.pyplot as plt
     2    import numpy as np
     3  
     4    parts = [35.35, 23, 26.65, 15]
     5    labels = ['Harrison', 'Vanessa', 'James', 'Ruby']
     6    colors = ['red', 'lightblue', 'purple', 'yellow']
     7    explodes = [0.1, 0, 0, 0.1]
     8    plt.pie(parts, colors = colors, labels = labels, explode = explodes, autopct = '%3.2f%%')
     9    plt.axis('equal')
    10    plt.legend()
    11  
    12    #plt.show()
    13    plt.savefig('simplePie.png', dpi=300)

![img](simplePie.png "簡單的pie chart")  


<a id="orgd8e0482"></a>

## 其它圖表

-   直方圖(Histogram)：用來呈現各資料統計結果([參考資料](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html))
-   散佈圖(Scatter)：用來呈現群聚關係([參考資料](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html))
-   [進階學習資源](https://matplotlib.org/gallery/index.html)


<a id="orgd6ed9f4"></a>

## 文字註解: plt.text()


<a id="orgefa3ff7"></a>

### 語法

-   ` plt.text( x相對座標, y相對座標 , 文字字串 [, 其它參數] ) `
-   [參考資料](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html)


<a id="org89fbe43"></a>

### 範例

    1    import matplotlib.pyplot as plt
    2  
    3    x = [1, 2, 3, 4, 5, 6, 7, 8]
    4    y = [1, 4, 9, 16, 25, 36, 49, 64]
    5    plt.plot(x, y, 'r--')
    6    for x, y in zip(x, y):
    7        plt.text(x-0.2, y+0.6, '(%d, %d)' %(x, y))
    8    #plt.show()
    9    plt.savefig('simpleText.png', dpi = 300)

![img](simpleText.png "簡單的文字註解")  


<a id="org21b0fbd"></a>

## 子圖表: plt.subplot()

-   範例<sup><a id="fnr.7" class="footref" href="#fn.7">7</a></sup>

     1    import numpy as np
     2    import matplotlib.pyplot as plt
     3  
     4    from matplotlib.ticker import NullFormatter  # useful for `logit` scale
     5  
     6    # Fixing random state for reproducibility
     7    np.random.seed(19680801)
     8  
     9    # make up some data in the interval ]0, 1[
    10    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    11    y = y[(y > 0) & (y < 1)]
    12    y.sort()
    13    x = np.arange(len(y))
    14  
    15    # plot with various axes scales
    16    plt.figure()
    17  
    18    # linear
    19    plt.subplot(221)
    20    plt.plot(x, y)
    21    plt.yscale('linear')
    22    plt.title('linear')
    23    plt.grid(True)
    24  
    25  
    26    # log
    27    plt.subplot(222)
    28    plt.plot(x, y)
    29    plt.yscale('log')
    30    plt.title('log')
    31    plt.grid(True)
    32  
    33  
    34    # symmetric log
    35    plt.subplot(223)
    36    plt.plot(x, y - y.mean())
    37    plt.yscale('symlog', linthreshy=0.01)
    38    plt.title('symlog')
    39    plt.grid(True)
    40  
    41    # logit
    42    plt.subplot(224)
    43    plt.plot(x, y)
    44    plt.yscale('logit')
    45    plt.title('logit')
    46    plt.grid(True)
    47    # Format the minor tick labels of the y-axis into empty strings with
    48    # `NullFormatter`, to avoid cumbering the axis with too many labels.
    49    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    50    # Adjust the subplot layout, because the logit one may take more space
    51    # than usual, due to y-tick labels like "1 - 10^{-3}"
    52    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
    53                        wspace=0.35)
    54  
    55    plt.savefig('simpleSubplot.png', dpi = 300)

![img](simpleSubplot.png "簡單的子圖表")  

-   [參考資料](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html)


<a id="org47d5ae0"></a>

# 區域資料檔分析


<a id="org1697bd2"></a>

## Excel/CSV: Pandas模組


<a id="orgcdb9c08"></a>

### CSV

-   為純文字檔，以逗號分隔值（Comma-Separated Values，CSV，有時也稱為字元分隔值，因為分隔字元也可以不是逗號）。
-   純文字意味著該檔案是一個字元序列，不含必須像二進位制數字那樣被解讀的資料。
-   CSV檔案由任意數目的記錄組成，記錄間以某種換行符分隔；每條記錄由欄位組成，欄位間的分隔符是其它字元或字串，最常見的是逗號或製表符。通常，所有記錄都有完全相同的欄位序列<sup><a id="fnr.2.100" class="footref" href="#fn.2">2</a></sup>。


<a id="org15f6486"></a>

### Pandas

-   Pandas是python的一個數據分析模組，2009 年底開源出來，提供高效能、簡易使用的資料格式(Data Frame)讓使用者可以快速操作及分析資料。
-   Pandas強化了資料處理的方便性也能與處理網頁資料與資料庫資料等，有點類似於Office的Excel能更加方便的進行運算、分析等<sup><a id="fnr.8" class="footref" href="#fn.8">8</a></sup>。
-   Pandas主要特色有<sup><a id="fnr.5.100" class="footref" href="#fn.5">5</a></sup>：  
    1.  在異質數據的讀取、轉換和處理上，都讓分析人員更容易處理，例如：從列欄試算表中找到想要的值。
    2.  Pandas 提供兩種主要的資料結構，Series 與 DataFrame。Series 顧名思義就是用來處理時間序列相關的資料(如感測器資料等)，主要為建立索引的一維陣列。DataFrame 則是用來處理結構化(Table like)的資料，有列索引與欄標籤的二維資料集，例如關聯式資料庫、CSV 等等。
    3.  透過載入至 Pandas 的資料結構物件後，可以透過結構化物件所提供的方法，來快速地進行資料的前處理，如資料補值，空值去除或取代等。
    4.  更多的輸入來源及輸出整合性，例如：可以從資料庫讀取資料進入 Dataframe，也可將處理完的資料存回資料庫。


<a id="org78eb494"></a>

### Pandas資料結構

-   Pandas是Python的資料分析函式庫，從2009年底開放原始碼，提供簡易使用的資料結構和分析工具，讓分析人員可以快速方便的處理結構化資料。
-   要使用Pandas之前，先瞭解兩個主要資料結構<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>：  
    -   Series: 是一維標籤陣列（array），能夠保存任何資料類型（整數、字符串、浮點數等）。
    -   DataFrame: 是一個二維標籤資料結構，可以具有不同類型的行（column），類似Excel的資料表，對於有使用過統計軟體的分析人員應該不陌生。
    -   簡單來說，Series可以想像為一行多列（row）的資料，而DataFrame是多行多列的資料，藉由選擇索引（列標籤）和行（行標籤）的參數來操作資料，就像使用統計軟體透過樣本編號或變項名稱來操作資料。


<a id="org4593917"></a>

## Pandas functions


<a id="org9ab2110"></a>

### 資料選取


<a id="orga3584e8"></a>

#### Select as dictinoary (column): <sup><a id="fnr.9" class="footref" href="#fn.9">9</a></sup>

-   ` df[[[['col1', 'col2']]]] `
-   ` df.col1 `
-   [下載範例檔:scores.csv](./scores.csv)

    1    import pandas as pd
    2  
    3    # 讀取csv
    4    df = pd.read_csv("scores.csv")
    5  
    6    # colum 
    7    print(df.id)
    8    print(df[['id', 'typing']])

    Pandas version: 0.25.1
    0      201910901
    1      201910902
    2      201910903
    3      201910904
    4      201910905
             ...    
    207    201911726
    208    201911727
    209    201911728
    210    201911729
    211    201911730
    Name: id, Length: 212, dtype: int64
                id  typing
    0    201910901      72
    1    201910902      56
    2    201910903      76
    3    201910904      64
    4    201910905      56
    ..         ...     ...
    207  201911726      80
    208  201911727      60
    209  201911728      48
    210  201911729      84
    211  201911730      72
    
    [212 rows x 2 columns]


<a id="orgacaacda"></a>

#### Select using index (row):

-   ` df[1:20] `

    1    import pandas as pd
    2  
    3    df = pd.read_csv("scores.csv")
    4  
    5    print(df[1:3])
    6    print(df[df.homework<30])

              id  classparti  typing  homework  midexam  finalexam
    1  201910902          96      56     93.42     60.0       40.0
    2  201910903          96      76    102.63     45.0       28.0
                id  classparti  typing  homework  midexam  finalexam
    10   201910911          62      44     20.39      4.0        0.0
    18   201910919          14      56     25.92      0.0        0.0
    23   201910924          75      48     10.75      0.0        0.0
    124  201911315          71     120     15.35      0.0        0.0
    140  201911331          93     120     25.88      0.0       16.0
    0      False
    1      False
    2      False
    3      False
    4      False
           ...  
    207    False
    208    False
    209    False
    210    False
    211    False
    Name: homework, Length: 212, dtype: bool


<a id="orgc708ccf"></a>

#### loc, iloc, between <sup><a id="fnr.10" class="footref" href="#fn.10">10</a></sup>

-   loc: 基於行標籤和列標籤（x<sub>label</sub>、y<sub>label</sub>）進行索引，以column名做為index
-   iloc: 基於行索引和列索引（index，columns） 都是從 0 開始，以數字做為index
-   between: 檢查區間值, ` Series.between(self, left, right, inclusive=True) `

1.  範例1

        1    import pandas as pd
        2  
        3    df = pd.read_csv("scores.csv")
        4  
        5    print(df.loc[df.homework<25, ['id', 'homework']])
        6    print(df.iloc[:5, 2:5])
        7    
    
                    id  homework
        10   201910911     20.39
        23   201910924     10.75
        124  201911315     15.35
           typing  homework  midexam
        0      72     92.11     48.0
        1      56     93.42     60.0
        2      76    102.63     45.0
        3      64     86.84     44.0
        4      56     42.11      0.0

2.  範例2

         1    # 載入函式庫
         2    import pandas as pd
         3  
         4    print("Pandas version:", pd.__version__)
         5    # 讀取csv
         6    df = pd.read_csv("scores.csv")
         7    # 輸出前3筆
         8    print(df.iloc[:3])
         9    # 輸出前3筆的第2,3欄
        10    print(df.iloc[:2, 1:3])
        11    # 輸出第3筆user的homework成績
        12    print(df.loc[2,'homework'])
        13  
        14    print(df['midexam'].between(50, 60))
        15    midFilter = df['midexam'].between(50, 55)
        16    print(df[midFilter])
    
        Pandas version: 0.25.1
                  id  classparti  typing  homework  midexam  finalexam
        0  201910901         100      72     92.11     48.0       16.0
        1  201910902          96      56     93.42     60.0       40.0
        2  201910903          96      76    102.63     45.0       28.0
           classparti  typing
        0         100      72
        1          96      56
        102.63
        0      False
        1       True
        2      False
        3      False
        4      False
               ...  
        207    False
        208    False
        209    False
        210    False
        211    False
        Name: midexam, Length: 212, dtype: bool
                    id  classparti  typing  homework  midexam  finalexam
        6    201910907         101     120     92.11     55.0       20.0
        65   201911029          93      60     82.00     50.0       16.0
        72   201911036          88      80    102.63     53.0       76.0
        92   201911119          82     104     89.47     50.0       20.0
        94   201911121          95     100     88.51     52.0       72.0
        109  201911136          91     100     81.58     51.0        4.0
        171  201911626          98      72     97.37     50.0       75.0


<a id="org60f30cc"></a>

### 條件式選取資料


<a id="orga9863eb"></a>

#### 語法

-   ` df[(condition)] `
-   ` df[(condition 1) & (condition 2) ] `


<a id="org7ed0017"></a>

#### 範例

    1    import pandas as pd
    2  
    3    df = pd.read_csv("scores.csv") 
    4  
    5    print(df[(df.midexam >= 100) & (df.finalexam >= 100)])

                id  classparti  typing  homework  midexam  finalexam
    11   201910912          87      92     92.11    110.8     103.75
    70   201911034         104      92    102.63    100.8     101.00
    88   201911115         120      88    105.26    113.5     111.00
    98   201911125         119      80    107.89    113.2     115.00
    102  201911129         106      52    102.63    103.6     100.00
    127  201911318         108      80    102.63    104.8     100.00
    138  201911329         105      48    107.89    100.0     100.00
    143  201911334         100     120     81.58    104.8     113.00
    153  201911608          88       0    102.63    100.0     100.00
    169  201911624          82     100    102.63    101.5     105.00
    182  201911701         103     108     92.63    100.0     100.00
    189  201911708         106     108    102.63    107.2     101.00
    190  201911709         108      88    107.89    104.8     105.00
    191  201911710         102     100    102.63    100.0     105.00
    193  201911712         105      96    101.58    107.5     100.00
    195  201911714         102      44    107.89    110.0     110.00
    196  201911715         106     120    107.89    102.4     105.00
    198  201911717          80     120    107.89    106.0     100.00
    201  201911721         109      76    100.00    100.0     100.00
    203  201911722         105     120    102.63    101.5     105.00
    210  201911729          87      84    105.26    112.3     103.00


<a id="org1abc7d8"></a>

## 進階分析


<a id="orgac01ec3"></a>

### 計算: Aggregation, Groupby


<a id="orge087879"></a>

#### [create new column based on other column](https://is.gd/y4tUl8)


<a id="org32b61b2"></a>

#### simple aggregation


<a id="org1d073e1"></a>

#### groupby with aggregation function


<a id="org86df465"></a>

#### 範例

     1    # 載入函式庫
     2    import pandas as pd
     3  
     4    # 讀取csv
     5    df = pd.read_csv("scores.csv")
     6  
     7    # 計算總分'
     8    df['Final'] = df.classparti*.1 + df.typing*.1 + df.homework*.2 + df.midexam*.3 + df.finalexam*.3
     9  
    10    # create new column according to typing speed
    11    df.loc[df.typing < 30, 'TypingSpeed' ] = 'LOW'
    12    df.loc[df.typing.between(30, 60), 'TypingSpeed' ] = 'MID'
    13    df.loc[df.typing > 60, 'TypingSpeed' ] = 'HIGH'
    14  
    15    print(df)
    16  
    17    # 依打字速度分組
    18    print(df.groupby('TypingSpeed')['Final'].mean())
    19  
    20    # PASS/FAIL
    21    df.loc[df.Final < 60, 'PASS'] = False
    22    df.loc[df.Final >= 60, 'PASS'] = True
    23  
    24    print(df.groupby('PASS')['typing'].mean())
    25  

                id  classparti  typing  ...  finalexam    Final  TypingSpeed
    0    201910901         100      72  ...       16.0   54.822         HIGH
    1    201910902          96      56  ...       40.0   63.884          MID
    2    201910903          96      76  ...       28.0   59.626         HIGH
    3    201910904          93      64  ...       25.0   53.768         HIGH
    4    201910905          93      56  ...       20.0   29.322          MID
    ..         ...         ...     ...  ...        ...      ...          ...
    207  201911726         106      80  ...      103.0   98.976         HIGH
    208  201911727          82      60  ...      100.0   89.926          MID
    209  201911728          83      48  ...       75.0   81.026          MID
    210  201911729          87      84  ...      103.0  102.742         HIGH
    211  201911730          96      72  ...      100.0   94.626         HIGH
    
    [212 rows x 8 columns]
    TypingSpeed
    HIGH    69.977451
    LOW     68.517333
    MID     64.086303
    Name: Final, dtype: float64
    PASS
    False    77.567568
    True     84.525547
    Name: typing, dtype: float64


<a id="orgbd64f19"></a>

### 資料檔下載: <scores.csv>


<a id="org3e73a3e"></a>

## 資料視覺化


<a id="orgd9a508e"></a>

### Bar chart

     1    # 載入函式庫
     2    import pandas as pd
     3    import matplotlib.pyplot as plt
     4    # 讀取csv
     5    df = pd.read_csv("scores.csv")
     6  
     7    # 計算總分'
     8    df['Final'] = df.classparti*.1 + df.typing*.1 + df.homework*.2 + df.midexam*.3 + df.finalexam*.3
     9  
    10    # create new column according to typing speed
    11    df.loc[df.typing < 30, 'TypingSpeed' ] = 'Level-1'
    12    df.loc[df.typing.between(30, 60), 'TypingSpeed' ] = 'Level-2'
    13    df.loc[df.typiohong > 60, 'TypingSpeed' ] = 'Level-3'
    14  
    15    fig = df.groupby('TypingSpeed')['homework','classparti'].mean().plot(kind='bar', title="XXX", rot=0, legend=True)
    16    fig.set_xlabel("Typing Speed")
    17    fig.set_ylabel("score")
    18    savefig = fig.get_figure()
    19    savefig.savefig('pandasPlot1.png', bbox_inches='tight')

![img](pandasPlot1.png "Pandas plot bar chart")  


<a id="orgb473491"></a>

### Pie chart

     1    # 載入函式庫
     2    import pandas as pd
     3    import matplotlib.pyplot as plt
     4    # 讀取csv
     5    df = pd.read_csv("scores.csv")
     6  
     7    # 計算總分'
     8    df['Final'] = df.classparti*.1 + df.typing*.1 + df.homework*.2 + df.midexam*.3 + df.finalexam*.3
     9  
    10    # create new column according to typing speed
    11    df.loc[df.typing < 60, 'TypingSpeed' ] = 'Level-1'
    12    df.loc[df.typing.between(60, 80), 'TypingSpeed' ] = 'Level-2'
    13    df.loc[df.typing > 80, 'TypingSpeed' ] = 'Level-3'
    14    print(df.groupby('TypingSpeed').count())
    15  
    16    fig = df.groupby('TypingSpeed')['TypingSpeed'].count().plot(kind='pie', title="XXX", rot=0, legend=True)
    17    savefig = fig.get_figure()
    18    savefig.savefig('pandasPlot2.png', bbox_inches='tight')

                  id  classparti  typing  homework  midexam  finalexam  Final
    TypingSpeed                                                              
    Level-1       25          25      25        25       25         25     25
    Level-2       86          86      86        86       86         86     86
    Level-3      101         101     101       101      100        101    100

![img](pandasPlot2.png "Pandas plot pie chart")  


<a id="orgb9de778"></a>

### Scatter chart

     1    # 載入函式庫
     2    import pandas as pd
     3    import matplotlib.pyplot as plt
     4  
     5    # 讀取csv
     6    df = pd.read_csv("scores.csv")
     7  
     8    fig = df[['typing','homework']].plot(kind='scatter', x=0, y=1)
     9    df[['typing','homework']].plot.line(x=0, y=1)
    10    #fig = df[['typing','finalexam']].plot(kind='scatter', x=0, y=1)
    11  
    12    savefig = fig.get_figure()
    13    savefig.savefig('PandasPlot3.png')

![img](PandasPlot3.png "Pandas plot scatter chart")  


<a id="org41051e9"></a>

### Line chart

     1    # 載入函式庫
     2    import pandas as pd
     3    import matplotlib.pyplot as plt
     4  
     5    # 讀取csv
     6    df = pd.read_csv("scores.csv")
     7  
     8    fig = df[['midexam','finalexam']].plot(kind='scatter', x=0, y=1)
     9  
    10    savefig = fig.get_figure()
    11    savefig.savefig('PandasPlot4.png')
    12  

![img](PandasPlot4.png "Pandas plot scatter chart")  


<a id="org495eca5"></a>

# 網路爬蟲


<a id="org4816b7a"></a>

## parse JSON


<a id="orgd9a1c14"></a>

### What is JSON?

-   JSON(JavaScript Object Notation，JavaScript物件表示法)是個以純文字為基底去儲存和傳送簡單結構資料，你可以透過特定的格式去儲存任何資料(字串,數字,陣列,物件)，也可以透過物件或陣列來傳送較複雜的資料。<sup><a id="fnr.11" class="footref" href="#fn.11">11</a></sup>
-   一旦建立了您的 JSON 資料，就可以非常簡單的跟其他程式溝通或交換資料，因為 JSON 就只是純文字個格式。


<a id="org2ed2515"></a>

### JSON的優點

-   相容性高
-   格式容易瞭解，閱讀及修改方便
-   支援許多資料格式 (number,string,booleans,nulls,array,associative array)
-   許多程式都支援函式庫讀取或修改 JSON 資料


<a id="org0fcf257"></a>

### JSON結構

-   物件: {}
-   陣列: []


<a id="org8833f59"></a>

### 實作1: [國際主要國家貨幣每月匯率概況](https://data.gov.tw/dataset/31897)


<a id="org2bd8556"></a>

#### 下載JSON

     1      import requests
     2  
     3      json_url = 'https://quality.data.gov.tw/dq_download_json.php?nid=11339&md5_url=f2fdbc21603c55b11aead08c84184b8f'
     4      response = requests.get(json_url)
     5  
     6      jsonRes = response.json()
     7      print(type(jsonRes))
     8      print(jsonRes)
     9      print('日期', ":\t", '美元／新台幣')
    10      for item in jsonRes:
    11          print(item['日期'], ":\t", item['美元／新台幣'])

    <class 'list'>
    [{'日期': '2020/2/3', '美元／新台幣': '30.332', '人民幣／新台幣': '4.321461', '歐元／美元': '1.1077', '美元／日幣': '108.535', '英鎊／美元': '1.3147', '澳幣／美元': '0.6695', '美元／港幣': '7.7685', '美元／人民幣': '7.0189', '美元／南非幣': '14.9376', '紐幣／美元': '0.64675'}, {'日期': '2020/2/4', '美元／新台幣': '30.207', '人民幣／新台幣': '4.320537', '歐元／美元': '1.1056', '美元／日幣': '108.945', '英鎊／美元': '1.29605', '澳幣／美元': '0.67185', '美元／港幣': '7.76895', '美元／人民幣': '6.9915', '美元／南非幣': '14.8117', '紐幣／美元': '0.6466'}, {'日期': '2020/2/5', '美元／新台幣': '30.152', '人民幣／新台幣': '4.306248', '歐元／美元': '1.1044', '美元／日幣': '109.345', '英鎊／美元': '1.3046', '澳幣／美元': '0.6741', '美元／港幣': '7.7644', '美元／人民幣': '7.0019', '美元／南非幣': '14.8205', '紐幣／美元': '0.6484'}, {'日期': '2020/2/6', '美元／新台幣': '30.082', '人民幣／新台幣': '4.315112', '歐元／美元': '1.1002', '美元／日幣': '109.905', '英鎊／美元': '1.29915', '澳幣／美元': '0.6751', '美元／港幣': '7.7633', '美元／人民幣': '6.9713', '美元／南非幣': '14.73', '紐幣／美元': '0.6466'}, {'日期': '2020/2/7', '美元／新台幣': '30.126', '人民幣／新台幣': '4.311904', '歐元／美元': '1.09685', '美元／日幣': '109.905', '英鎊／美元': '1.29315', '澳幣／美元': '0.6706', '美元／港幣': '7.76115', '美元／人民幣': '6.9867', '美元／南非幣': '14.9919', '紐幣／美元': '0.64405'}, {'日期': '2020/2/10', '美元／新台幣': '30.102', '人民幣／新台幣': '4.30883', '歐元／美元': '1.0946', '美元／日幣': '109.845', '英鎊／美元': '1.28835', '澳幣／美元': '0.6697', '美元／港幣': '7.76475', '美元／人民幣': '6.9861', '美元／南非幣': '15.014', '紐幣／美元': '0.64075'}, {'日期': '2020/2/11', '美元／新台幣': '30.068', '人民幣／新台幣': '4.307872', '歐元／美元': '1.0908', '美元／日幣': '109.915', '英鎊／美元': '1.2897', '澳幣／美元': '0.6707', '美元／港幣': '7.76335', '美元／人民幣': '6.9798', '美元／南非幣': '14.92815', '紐幣／美元': '0.6385'}, {'日期': '2020/2/12', '美元／新台幣': '30.032', '人民幣／新台幣': '4.305388', '歐元／美元': '1.0917', '美元／日幣': '109.885', '英鎊／美元': '1.2969', '澳幣／美元': '0.6732', '美元／港幣': '7.76805', '美元／人民幣': '6.97545', '美元／南非幣': '14.78', '紐幣／美元': '0.6464'}, {'日期': '2020/2/13', '美元／新台幣': '30.037', '人民幣／新台幣': '4.301749', '歐元／美元': '1.08805', '美元／日幣': '109.735', '英鎊／美元': '1.2975', '澳幣／美元': '0.67255', '美元／港幣': '7.76855', '美元／人民幣': '6.9825', '美元／南非幣': '14.96025', '紐幣／美元': '0.64555'}, {'日期': '2020/2/14', '美元／新台幣': '30.051', '人民幣／新台幣': '4.301741', '歐元／美元': '1.08345', '美元／日幣': '109.775', '英鎊／美元': '1.3052', '澳幣／美元': '0.67255', '美元／港幣': '7.7672', '美元／人民幣': '6.9858', '美元／南非幣': '14.88945', '紐幣／美元': '0.6434'}, {'日期': '2020/2/17', '美元／新台幣': '30.056', '人民幣／新台幣': '4.305011', '歐元／美元': '1.084', '美元／日幣': '109.865', '英鎊／美元': '1.3042', '澳幣／美元': '0.6726', '美元／港幣': '7.76665', '美元／人民幣': '6.98165', '美元／南非幣': '14.8793', '紐幣／美元': '0.643'}, {'日期': '2020/2/18', '美元／新台幣': '30.125', '人民幣／新台幣': '4.300163', '歐元／美元': '1.0828', '美元／日幣': '109.765', '英鎊／美元': '1.2976', '澳幣／美元': '0.6686', '美元／港幣': '7.7684', '美元／人民幣': '7.00555', '美元／南非幣': '15.0167', '紐幣／美元': '0.64095'}, {'日期': '2020/2/19', '美元／新台幣': '30.152', '人民幣／新台幣': '4.307877', '歐元／美元': '1.08', '美元／日幣': '110.075', '英鎊／美元': '1.30015', '澳幣／美元': '0.66955', '美元／港幣': '7.77105', '美元／人民幣': '6.99925', '美元／南非幣': '14.96755', '紐幣／美元': '0.6395'}, {'日期': '2020/2/20', '美元／新台幣': '30.254', '人民幣／新台幣': '4.307928', '歐元／美元': '1.0789', '美元／日幣': '111.745', '英鎊／美元': '1.28955', '澳幣／美元': '0.66375', '美元／港幣': '7.77715', '美元／人民幣': '7.02285', '美元／南非幣': '15.0643', '紐幣／美元': '0.63455'}, {'日期': '2020/2/21', '美元／新台幣': '30.403', '人民幣／新台幣': '4.310203', '歐元／美元': '1.07965', '美元／日幣': '111.585', '英鎊／美元': '1.28955', '澳幣／美元': '0.6591', '美元／港幣': '7.78995', '美元／人民幣': '7.05375', '美元／南非幣': '15.1692', '紐幣／美元': '0.6307'}, {'日期': '2020/2/24', '美元／新台幣': '30.472', '人民幣／新台幣': '4.327359', '歐元／美元': '1.0823', '美元／日幣': '111.475', '英鎊／美元': '1.2929', '澳幣／美元': '0.65925', '美元／港幣': '7.7927', '美元／人民幣': '7.0417', '美元／南非幣': '15.157', '紐幣／美元': '0.6309'}, {'日期': '2020/2/25', '美元／新台幣': '30.402', '人民幣／新台幣': '4.329458', '歐元／美元': '1.0854', '美元／日幣': '110.665', '英鎊／美元': '1.29505', '澳幣／美元': '0.66115', '美元／港幣': '7.7886', '美元／人民幣': '7.02215', '美元／南非幣': '15.1187', '紐幣／美元': '0.63345'}, {'日期': '2020/2/26', '美元／新台幣': '30.383', '人民幣／新台幣': '4.320979', '歐元／美元': '1.08795', '美元／日幣': '110.455', '英鎊／美元': '1.299', '澳幣／美元': '0.65775', '美元／港幣': '7.79095', '美元／人民幣': '7.0315', '美元／南非幣': '15.2246', '紐幣／美元': '0.6309'}, {'日期': '2020/2/27', '美元／新台幣': '30.33', '人民幣／新台幣': '4.318689', '歐元／美元': '1.09285', '美元／日幣': '110.03', '英鎊／美元': '1.29145', '澳幣／美元': '0.65645', '美元／港幣': '7.7964', '美元／人民幣': '7.02295', '美元／南非幣': '15.3078', '紐幣／美元': '0.6307'}, {'日期': '2020/3/2', '美元／新台幣': '30.124', '人民幣／新台幣': '4.329783', '歐元／美元': '1.10845', '美元／日幣': '108.375', '英鎊／美元': '1.27755', '澳幣／美元': '0.6566', '美元／港幣': '7.7788', '美元／人民幣': '6.9574', '美元／南非幣': '15.46135', '紐幣／美元': '0.6264'}, {'日期': '2020/3/3', '美元／新台幣': '30.087', '人民幣／新台幣': '4.309963', '歐元／美元': '1.11255', '美元／日幣': '108.025', '英鎊／美元': '1.2796', '澳幣／美元': '0.65635', '美元／港幣': '7.78075', '美元／人民幣': '6.9808', '美元／南非幣': '15.4663', '紐幣／美元': '0.6274'}, {'日期': '2020/3/4', '美元／新台幣': '30.038', '人民幣／新台幣': '4.331359', '歐元／美元': '1.11675', '美元／日幣': '107.375', '英鎊／美元': '1.2792', '澳幣／美元': '0.6599', '美元／港幣': '7.76875', '美元／人民幣': '6.935', '美元／南非幣': '15.4147', '紐幣／美元': '0.6282'}, {'日期': '2020/3/5', '美元／新台幣': '29.96', '人民幣／新台幣': '4.318824', '歐元／美元': '1.1132', '美元／日幣': '107.27', '英鎊／美元': '1.2887', '澳幣／美元': '0.66275', '美元／港幣': '7.77055', '美元／人民幣': '6.93705', '美元／南非幣': '15.3171', '紐幣／美元': '0.6307'}, {'日期': '2020/3/6', '美元／新台幣': '30.04', '人民幣／新台幣': '4.326661', '歐元／美元': '1.12395', '美元／日幣': '105.845', '英鎊／美元': '1.297', '澳幣／美元': '0.6637', '美元／港幣': '7.7718', '美元／人民幣': '6.943', '美元／南非幣': '15.61445', '紐幣／美元': '0.63545'}, {'日期': '2020/3/9', '美元／新台幣': '30.13', '人民幣／新台幣': '4.337093', '歐元／美元': '1.14195', '美元／日幣': '102.395', '英鎊／美元': '1.3165', '澳幣／美元': '0.655', '美元／港幣': '7.76875', '美元／人民幣': '6.94705', '美元／南非幣': '16.13755', '紐幣／美元': '0.6272'}, {'日期': '2020/3/10', '美元／新台幣': '30.036', '人民幣／新台幣': '4.323292', '歐元／美元': '1.13965', '美元／日幣': '103.975', '英鎊／美元': '1.3064', '澳幣／美元': '0.6562', '美元／港幣': '7.76865', '美元／人民幣': '6.9475', '美元／南非幣': '15.9612', '紐幣／美元': '0.6305'}, {'日期': '2020/3/11', '美元／新台幣': '30.095', '人民幣／新台幣': '4.328082', '歐元／美元': '1.13145', '美元／日幣': '105.055', '英鎊／美元': '1.29175', '澳幣／美元': '0.6522', '美元／港幣': '7.76705', '美元／人民幣': '6.95345', '美元／南非幣': '15.9834', '紐幣／美元': '0.63125'}, {'日期': '2020/3/12', '美元／新台幣': '30.15', '人民幣／新台幣': '4.314405', '歐元／美元': '1.1305', '美元／日幣': '103.665', '英鎊／美元': '1.28265', '澳幣／美元': '0.64575', '美元／港幣': '7.7712', '美元／人民幣': '6.9882', '美元／南非幣': '16.3743', '紐幣／美元': '0.62745'}, {'日期': '2020/3/13', '美元／新台幣': '30.21', '人民幣／新台幣': '4.311481', '歐元／美元': '1.11935', '美元／日幣': '105.865', '英鎊／美元': '1.2612', '澳幣／美元': '0.6286', '美元／港幣': '7.76655', '美元／人民幣': '7.00685', '美元／南非幣': '16.3106', '紐幣／美元': '0.612'}, {'日期': '2020/3/16', '美元／新台幣': '30.22', '人民幣／新台幣': '4.308465', '歐元／美元': '1.1186', '美元／日幣': '106.555', '英鎊／美元': '1.23585', '澳幣／美元': '0.6173', '美元／港幣': '7.7653', '美元／人民幣': '7.0141', '美元／南非幣': '16.53155', '紐幣／美元': '0.6038'}, {'日期': '2020/3/17', '美元／新台幣': '30.25', '人民幣／新台幣': '4.309385', '歐元／美元': '1.11425', '美元／日幣': '106.925', '英鎊／美元': '1.2227', '澳幣／美元': '0.6091', '美元／港幣': '7.76535', '美元／人民幣': '7.01955', '美元／南非幣': '16.48065', '紐幣／美元': '0.60435'}, {'日期': '2020/3/18', '美元／新台幣': '30.276', '人民幣／新台幣': '4.296013', '歐元／美元': '1.0986', '美元／日幣': '107.335', '英鎊／美元': '1.2043', '澳幣／美元': '0.5962', '美元／港幣': '7.76725', '美元／人民幣': '7.04745', '美元／南非幣': '16.7624', '紐幣／美元': '0.58935'}, {'日期': '2020/3/19', '美元／新台幣': '30.506', '人民幣／新台幣': '4.282432', '歐元／美元': '1.082', '美元／日幣': '109.17', '英鎊／美元': '1.148', '澳幣／美元': '0.5683', '美元／港幣': '7.76295', '美元／人民幣': '7.1235', '美元／南非幣': '17.4708', '紐幣／美元': '0.56175'}, {'日期': '2020/3/20', '美元／新台幣': '30.302', '人民幣／新台幣': '4.278976', '歐元／美元': '1.0777', '美元／日幣': '109.655', '英鎊／美元': '1.18145', '澳幣／美元': '0.59435', '美元／港幣': '7.75695', '美元／人民幣': '7.0816', '美元／南非幣': '17.1728', '紐幣／美元': '0.5837'}, {'日期': '2020/3/23', '美元／新台幣': '30.405', '人民幣／新台幣': '4.257491', '歐元／美元': '1.0691', '美元／日幣': '110.135', '英鎊／美元': '1.16085', '澳幣／美元': '0.5786', '美元／港幣': '7.75575', '美元／人民幣': '7.14155', '美元／南非幣': '17.83985', '紐幣／美元': '0.5651'}, {'日期': '2020/3/24', '美元／新台幣': '30.316', '人民幣／新台幣': '4.276921', '歐元／美元': '1.0837', '美元／日幣': '110.655', '英鎊／美元': '1.165', '澳幣／美元': '0.5955', '美元／港幣': '7.75545', '美元／人民幣': '7.0883', '美元／南非幣': '17.68235', '紐幣／美元': '0.58255'}, {'日期': '2020/3/25', '美元／新台幣': '30.325', '人民幣／新台幣': '4.260996', '歐元／美元': '1.0808', '美元／日幣': '111.53', '英鎊／美元': '1.18305', '澳幣／美元': '0.6037', '美元／港幣': '7.7547', '美元／人民幣': '7.1169', '美元／南非幣': '17.3912', '紐幣／美元': '0.5877'}, {'日期': '2020/3/26', '美元／新台幣': '30.306', '人民幣／新台幣': '4.262327', '歐元／美元': '1.0934', '美元／日幣': '110.415', '英鎊／美元': '1.1927', '澳幣／美元': '0.5954', '美元／港幣': '7.7538', '美元／人民幣': '7.1102', '美元／南非幣': '17.4674', '紐幣／美元': '0.5852'}]
    日期 :	 美元／新台幣
    2020/2/3 :	 30.332
    2020/2/4 :	 30.207
    2020/2/5 :	 30.152
    2020/2/6 :	 30.082
    2020/2/7 :	 30.126
    2020/2/10 :	 30.102
    2020/2/11 :	 30.068
    2020/2/12 :	 30.032
    2020/2/13 :	 30.037
    2020/2/14 :	 30.051
    2020/2/17 :	 30.056
    2020/2/18 :	 30.125
    2020/2/19 :	 30.152
    2020/2/20 :	 30.254
    2020/2/21 :	 30.403
    2020/2/24 :	 30.472
    2020/2/25 :	 30.402
    2020/2/26 :	 30.383
    2020/2/27 :	 30.33
    2020/3/2 :	 30.124
    2020/3/3 :	 30.087
    2020/3/4 :	 30.038
    2020/3/5 :	 29.96
    2020/3/6 :	 30.04
    2020/3/9 :	 30.13
    2020/3/10 :	 30.036
    2020/3/11 :	 30.095
    2020/3/12 :	 30.15
    2020/3/13 :	 30.21
    2020/3/16 :	 30.22
    2020/3/17 :	 30.25
    2020/3/18 :	 30.276
    2020/3/19 :	 30.506
    2020/3/20 :	 30.302
    2020/3/23 :	 30.405
    2020/3/24 :	 30.316
    2020/3/25 :	 30.325
    2020/3/26 :	 30.306


<a id="orgc0bd9aa"></a>

#### 資料視覺化

     1      import requests
     2      import pandas as pd
     3      json_url = 'https://quality.data.gov.tw/dq_download_json.php?nid=11339&md5_url=f2fdbc21603c55b11aead08c84184b8f'
     4      response = requests.get(json_url)
     5      jsonRes = response.json()
     6  
     7      dates = [i['日期'] for i in jsonRes]
     8      NTUS = [float(i['美元／新台幣']) for i in jsonRes]
     9      df = pd.DataFrame({'日期':dates, '美元/新台幣':NTUS})
    10  
    11      import matplotlib.pyplot as plt
    12  
    13      plt.clf()
    14      plt.plot(df['日期'], NTUS)
    15      plt.xticks(rotation=60, fontsize=6)
    16      ##plt.plot(dates, JPY)
    17      ##plt.plot(dates, EUR)
    18      plt.savefig('jsonLine.png', dpi=300)

![img](jsonLine.png "匯率")  


<a id="orgd72d30b"></a>

### 實作2: [澎湖生活博物館每月參觀人次統計資料](https://data.gov.tw/dataset/113063)

1.  中文亂碼處理  
    -   [Python-MacOS上matplotlib顯示中文字體](https://blog.csdn.net/lztttao/article/details/99697813)
    -   [關於python：Matplotlib使刻度標籤字體更小](https://www.codenong.com/6390393/)
2.  DEMO  
    
         1       #coding:utf-8 
         2       import requests
         3       import pandas as pd
         4       from datetime import datetime
         5  
         6       json_url = 'http://opendataap2.penghu.gov.tw/resource/files/2020-01-12/eaa641fc3af66277e60b13201ca11232.json'
         7  
         8       response = requests.get(json_url)
         9       jsonRes = response.json()
        10  
        11       year = [i['年度'] for i in jsonRes]
        12       month = [i['月份'] for i in jsonRes]
        13       visitor = [int(i['人數']) for i in jsonRes]
        14  
        15       df = pd.DataFrame({'year':year, 'month':month, 'visitor':visitor})
        16       df['date'] = [str(int(i)+1911)+'-'+j for i, j in zip(df['year'], df['month'])]
        17  
        18       df['time'] = [pd.to_datetime(i, format='%y%m', errors='ignore') for i in df['date']]
        19  
        20       import matplotlib.pyplot as plt
        21       plt.rcParams['font.family'] = 'cwTeXFangSong'
        22       plt.clf()
        23       plt.bar(df['date'], df['visitor'])
        24       plt.xticks(rotation=60, fontsize=6)
        25       plt.ylabel('人數')
        26       plt.xlabel('日期')
        27       plt.title('澎湖生活博物館每月參觀人次')
        28       plt.savefig('jsonBar.png', dpi=300, bbox_inches='tight')
    
    ![img](jsonBar.png "參觀人數")


<a id="orgc6f6761"></a>

### 實作3: 下載JSON

     1    import requests
     2    import json
     3    json_url = 'http://www.kh.edu.tw/json/bulletin/employ/datagrid?page=1&rows=20'
     4    response = requests.get(json_url)
     5  
     6    print(response)
     7    # 方法1
     8    jsonRes1 = response.json()
     9    print(type(jsonRes1))
    10    # 
    11    jsonRes2 = json.loads(response.text)
    12    print(type(jsonRes2))
    13  
    14    print(jsonRes2)

    <Response [200]>
    <class 'dict'>
    <class 'dict'>
    {'total': 20, 'rows': [{'author': '文德國小', 'attributes': {'subjects': '普通科留職停薪', 'url': 'https://employ.kh.edu.tw/Html/2020/3/鳳山區108學年度文德國小第5號第3次公告簡章.html', 'target': '_blank'}, 'title': '108學年度文德國小第5號第3次公告', 'pubDate': '109-03-12'}, {'author': '興仁國中', 'attributes': {'subjects': '生物', 'url': 'https://employ.kh.edu.tw/Html/2020/3/前鎮區108學年度興仁國中第8號第1次公告簡章.html', 'target': '_blank'}, 'title': '108學年度興仁國中第8號第1次公告', 'pubDate': '109-03-12'}, {'author': '燕巢國中', 'attributes': {'subjects': '資訊科技科(電腦科)', 'url': 'https://employ.kh.edu.tw/Html/2020/3/燕巢區108學年度燕巢國中第13號第2次公告簡章.html', 'target': '_blank'}, 'title': '108學年度燕巢國中第13號第2次公告', 'pubDate': '109-03-12'}, {'author': '登發國小', 'attributes': {'subjects': '普通科', 'url': 'https://employ.kh.edu.tw/Html/2020/3/仁武區108學年度登發國小第3號第2次公告簡章.html', 'target': '_blank'}, 'title': '108學年度登發國小第3號第2次公告', 'pubDate': '109-03-11'}, {'author': '青年國中', 'attributes': {'subjects': '國文', 'url': 'https://employ.kh.edu.tw/Html/2020/3/鳳山區108學年度青年國中第13號第1次公告簡章.html', 'target': '_blank'}, 'title': '108學年度青年國中第13號第1次公告', 'pubDate': '109-03-10'}, {'author': '龍華國中', 'attributes': {'subjects': '地理', 'url': 'https://employ.kh.edu.tw/Html/2020/3/左營區108學年度龍華國中第11號第1次公告簡章.html', 'target': '_blank'}, 'title': '108學年度龍華國中第11號第1次公告', 'pubDate': '109-03-10'}, {'author': '鼓山高中', 'attributes': {'subjects': '', 'url': 'https://employ.kh.edu.tw/Html/2020/3/鼓山區108學年度鼓山高中第11號第1次公告簡章.html', 'target': '_blank'}, 'title': '108學年度鼓山高中第11號第1次公告', 'pubDate': '109-03-10'}, {'author': '烏林國小', 'attributes': {'subjects': '特教身心障礙巡迴輔導班', 'url': 'https://employ.kh.edu.tw/Html/2020/3/仁武區108學年度烏林國小第3號第2次公告簡章.html', 'target': '_blank'}, 'title': '108學年度烏林國小第3號第2次公告', 'pubDate': '109-03-10'}, {'author': '七賢國中', 'attributes': {'subjects': '數學', 'url': 'https://employ.kh.edu.tw/Html/2020/3/鼓山區108學年度七賢國中第9號第2次公告簡章.html', 'target': '_blank'}, 'title': '108學年度七賢國中第9號第2次公告', 'pubDate': '109-03-09'}, {'author': '溪埔國中', 'attributes': {'subjects': '特殊教育數學專長', 'url': 'https://employ.kh.edu.tw/Html/2020/3/大樹區108學年度溪埔國中第7號第2次公告簡章.html', 'target': '_blank'}, 'title': '108學年度溪埔國中第7號第2次公告', 'pubDate': '109-03-09'}, {'author': '楠梓國中', 'attributes': {'subjects': '歷史', 'url': 'https://employ.kh.edu.tw/Html/2020/3/楠梓區108學年度楠梓國中第8號第4次公告簡章.html', 'target': '_blank'}, 'title': '108學年度楠梓國中第8號第4次公告', 'pubDate': '109-03-09'}, {'author': '甲仙國中', 'attributes': {'subjects': '', 'url': 'https://employ.kh.edu.tw/Html/2020/3/甲仙區108學年度甲仙國中第5號第2次公告簡章.html', 'target': '_blank'}, 'title': '108學年度甲仙國中第5號第2次公告', 'pubDate': '109-03-09'}, {'author': '立志高中', 'attributes': {'subjects': '', 'url': 'https://employ.kh.edu.tw/Html/2020/3/三民區108學年度立志高中第1號第1次公告簡章.html', 'target': '_blank'}, 'title': '108學年度立志高中第1號第1次公告', 'pubDate': '109-03-06'}, {'author': '阿蓮國小', 'attributes': {'subjects': '五年級自然與生活科技領域', 'url': 'https://employ.kh.edu.tw/Html/2020/3/阿蓮區108學年度阿蓮國小第12號第3次公告簡章.html', 'target': '_blank'}, 'title': '108學年度阿蓮國小第12號第3次公告', 'pubDate': '109-03-06'}, {'author': '金潭國小', 'attributes': {'subjects': '學前不分類巡迴輔導班', 'url': 'https://employ.kh.edu.tw/Html/2020/3/林園區108學年度金潭國小第6號第3次公告簡章.html', 'target': '_blank'}, 'title': '108學年度金潭國小第6號第3次公告', 'pubDate': '109-03-06'}, {'author': '中崙國中', 'attributes': {'subjects': '英語', 'url': 'https://employ.kh.edu.tw/Html/2020/3/鳳山區108學年度中崙國中第7號第3次公告簡章.html', 'target': '_blank'}, 'title': '108學年度中崙國中第7號第3次公告', 'pubDate': '109-03-05'}, {'author': '巴楠花部落中小學', 'attributes': {'subjects': '生物', 'url': 'https://employ.kh.edu.tw/Html/2020/3/杉林區108學年度巴楠花部落中小學第14號第3次公告簡章.html', 'target': '_blank'}, 'title': '108學年度巴楠花部落中小學第14號第3次公告', 'pubDate': '109-03-04'}, {'author': '中山國小', 'attributes': {'subjects': '綜合科', 'url': 'https://employ.kh.edu.tw/Html/2020/3/鼓山區108學年度中山國小第10號第2次公告簡章.html', 'target': '_blank'}, 'title': '108學年度中山國小第10號第2次公告', 'pubDate': '109-03-03'}, {'author': '福誠高中', 'attributes': {'subjects': '地理', 'url': 'https://employ.kh.edu.tw/Html/2020/3/鳳山區108學年度福誠高中第19號第3次公告簡章.html', 'target': '_blank'}, 'title': '108學年度福誠高中第19號第3次公告', 'pubDate': '109-03-03'}, {'author': '彌陀國小', 'attributes': {'subjects': '', 'url': 'https://employ.kh.edu.tw/Html/2020/3/彌陀區108學年度彌陀國小第5號第1次公告簡章.html', 'target': '_blank'}, 'title': '108學年度彌陀國小第5號第1次公告', 'pubDate': '109-03-03'}]}


<a id="org585ad27"></a>

### 實作: 解析JSON

     1    import requests
     2    import json
     3  
     4    response = requests.get('http://www.kh.edu.tw/json/bulletin/employ/datagrid?page=1&rows=20')
     5    jsonRes = response.json()
     6    #print(jsonRes['rows'])
     7    for item in jsonRes['rows']:
     8        print(item['author'], ":", item['title']," / ", item['pubDate'])
     9    sortJR = jsonRes['rows']
    10    print(type(sortJR))
    11  
    12    sortJR.sort(key=lambda x: x['author'], reverse=False)
    13    for item in sortJR:
    14        print(item['author'], ":", item['title']," / ", item['pubDate'])

    文德國小 : 108學年度文德國小第5號第3次公告  /  109-03-12
    興仁國中 : 108學年度興仁國中第8號第1次公告  /  109-03-12
    燕巢國中 : 108學年度燕巢國中第13號第2次公告  /  109-03-12
    登發國小 : 108學年度登發國小第3號第2次公告  /  109-03-11
    青年國中 : 108學年度青年國中第13號第1次公告  /  109-03-10
    龍華國中 : 108學年度龍華國中第11號第1次公告  /  109-03-10
    鼓山高中 : 108學年度鼓山高中第11號第1次公告  /  109-03-10
    烏林國小 : 108學年度烏林國小第3號第2次公告  /  109-03-10
    七賢國中 : 108學年度七賢國中第9號第2次公告  /  109-03-09
    溪埔國中 : 108學年度溪埔國中第7號第2次公告  /  109-03-09
    楠梓國中 : 108學年度楠梓國中第8號第4次公告  /  109-03-09
    甲仙國中 : 108學年度甲仙國中第5號第2次公告  /  109-03-09
    立志高中 : 108學年度立志高中第1號第1次公告  /  109-03-06
    阿蓮國小 : 108學年度阿蓮國小第12號第3次公告  /  109-03-06
    金潭國小 : 108學年度金潭國小第6號第3次公告  /  109-03-06
    中崙國中 : 108學年度中崙國中第7號第3次公告  /  109-03-05
    巴楠花部落中小學 : 108學年度巴楠花部落中小學第14號第3次公告  /  109-03-04
    中山國小 : 108學年度中山國小第10號第2次公告  /  109-03-03
    福誠高中 : 108學年度福誠高中第19號第3次公告  /  109-03-03
    彌陀國小 : 108學年度彌陀國小第5號第1次公告  /  109-03-03
    <class 'list'>
    七賢國中 : 108學年度七賢國中第9號第2次公告  /  109-03-09
    中山國小 : 108學年度中山國小第10號第2次公告  /  109-03-03
    中崙國中 : 108學年度中崙國中第7號第3次公告  /  109-03-05
    巴楠花部落中小學 : 108學年度巴楠花部落中小學第14號第3次公告  /  109-03-04
    彌陀國小 : 108學年度彌陀國小第5號第1次公告  /  109-03-03
    文德國小 : 108學年度文德國小第5號第3次公告  /  109-03-12
    楠梓國中 : 108學年度楠梓國中第8號第4次公告  /  109-03-09
    溪埔國中 : 108學年度溪埔國中第7號第2次公告  /  109-03-09
    烏林國小 : 108學年度烏林國小第3號第2次公告  /  109-03-10
    燕巢國中 : 108學年度燕巢國中第13號第2次公告  /  109-03-12
    甲仙國中 : 108學年度甲仙國中第5號第2次公告  /  109-03-09
    登發國小 : 108學年度登發國小第3號第2次公告  /  109-03-11
    福誠高中 : 108學年度福誠高中第19號第3次公告  /  109-03-03
    立志高中 : 108學年度立志高中第1號第1次公告  /  109-03-06
    興仁國中 : 108學年度興仁國中第8號第1次公告  /  109-03-12
    金潭國小 : 108學年度金潭國小第6號第3次公告  /  109-03-06
    阿蓮國小 : 108學年度阿蓮國小第12號第3次公告  /  109-03-06
    青年國中 : 108學年度青年國中第13號第1次公告  /  109-03-10
    鼓山高中 : 108學年度鼓山高中第11號第1次公告  /  109-03-10
    龍華國中 : 108學年度龍華國中第11號第1次公告  /  109-03-10


<a id="orge1abd9d"></a>

### 練習

-   以程式抓取[高雄市政府資料開放平台](https://data.kcg.gov.tw/dataset?res_format=JSON)的線上JSON資料，parse並輸出所需結果


<a id="org493faed"></a>

## parse HTML

-   what is HTML
-   精神：將程式模仿成一般user


<a id="orgd7af94f"></a>

### 所需套件

-   BeautifulSoup

pip install beautifulsoup4  


<a id="org568a4dc"></a>

## 範例: 以程式抓取PTT電影板header


<a id="org115394f"></a>

### 原則

1.  要抓網路資料，就要先仔細觀察網頁內容
2.  要儘量欺騙網站自己是browser


<a id="org1804dec"></a>

### 實作: 取得HTML資料


<a id="orga7e0ec7"></a>

#### 第一版

    1    # 抓取PTT電影版header
    2    import urllib.request as req
    3    url = "https://www.ptt.cc/bbs/Stock/index.html"
    4  
    5    with req.urlopen(url) as response:
    6        data = response.read().decode("utf-8")
    7    print(data)

    urllib.error.HTTPError: HTTP Error 403: Forbidden

被拒絕原因：這隻程式的行為不像一般使用者，被網站伺服器拒絕。403 Forbidden 是HTTP協議中的一個HTTP狀態碼（Status Code）。可以簡單的理解為沒有權限訪問此站，服務器收到請求但拒絕提供服務<sup><a id="fnr.12" class="footref" href="#fn.12">12</a></sup>。  


<a id="org61fbaec"></a>

#### 第二版:加入header

     1    import urllib.request as req
     2    url = "https://www.ptt.cc/bbs/Stock/index.html"
     3    # 幫request加上一個header
     4    request = req.Request(url, headers = {
     5        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
     6    })
     7  
     8    with req.urlopen(request) as response:
     9        data = response.read().decode("utf-8")
    10    print('所取得的資料型態：',type(data))
    11    print(data[700:1200])

    所取得的資料型態： <class 'str'>
    api.js'></script></head>
        <body>
    		
    <div id="topbar-container">
    	<div id="topbar" class="bbs-content">
    		<a id="logo" href="/bbs/">批踢踢實業坊</a>
    		<span>&rsaquo;</span>
    		<a class="board" href="/bbs/Stock/index.html"><span class="board-label">看板 </span>Stock</a>
    		<a class="right small" href="/about.html">關於我們</a>
    		<a class="right small" href="/contact.html">聯絡資訊</a>
    	</div>
    </div>
    
    <div id="main-container">
    	<div id="action-bar-container">
    		<div class="action-bar">
    			<div class="btn-group bt


<a id="org3629082"></a>

### 實作：解析HTML資料內容


<a id="org7afeb4c"></a>

#### 安裝解析HTML所需套件

    pip install beautifulsoup4

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">Requirement</td>
<td class="org-left">already</td>
<td class="org-left">satisfied:</td>
<td class="org-left">beautifulsoup4</td>
<td class="org-left">in</td>
<td class="org-left">/Users/letranger/anaconda3/lib/python3.7/site-packages</td>
<td class="org-left">(4.8.0)</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">Requirement</td>
<td class="org-left">already</td>
<td class="org-left">satisfied:</td>
<td class="org-left">soupsieve>=1.2</td>
<td class="org-left">in</td>
<td class="org-left">/Users/letranger/anaconda3/lib/python3.7/site-packages</td>
<td class="org-left">(from</td>
<td class="org-left">beautifulsoup4)</td>
<td class="org-left">(1.9.4)</td>
</tr>
</tbody>
</table>


<a id="org4496c5c"></a>

#### 第三版: 解析HTML

     1    import urllib.request as req
     2    url = "https://www.ptt.cc/bbs/Stock/index.html"
     3    # 幫request加上一個header
     4    request = req.Request(url, headers = {
     5        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
     6    })
     7  
     8    with req.urlopen(request) as response:
     9        data = response.read().decode("utf-8")
    10  
    11    import bs4
    12    root = bs4.BeautifulSoup(data,"html.parser")
    13  
    14    titles = root.find("div", class_="title")
    15    titles = root.find_all("div", class_="title")
    16  
    17    for title in titles:
    18        if title.a != None:
    19            print(title.a.string)

    [請益] 股市經典圖準嗎?
    [請益] 布蘭特和西德州原油差異和淨值更新
    Re: [新聞] 慘！無薪假人數飆到7916人 創8年新高
    Re: [新聞] 一桶原油驚見「賣負5元」！全球儲油空間快爆滿 生產商倒
    [標的]防疫概念股 大同2371
    [請益] 股票還在高檔是否已反應疫情快結束?
    [創作] 陳嘉偉 江偉 （改林俊傑 江南）
    [心得] 日本是領先指標
    Re: [心得] 日本是領先指標
    Re: [新聞] 國際油價又崩跌回到25美元 川普推文只有
    [心得] 美國非農數據 + 3月失業率
    [標的] 中租-KY(5871)
    請問UWT怎麼沒開盤了?
    [公告] 精華區導覽Q&A
    [公告] Stock 板規V2.6             (2019/06/20)
    [公告] 版規修正
    [閒聊] 2020/04/01 盤後閒聊


<a id="org657c8fc"></a>

#### 第四版: 解析HTML

     1    import urllib.request as req
     2    url = "https://huodalife.pixnet.net/blog/"
     3    # 幫request加上一個header
     4    request = req.Request(url, headers = {
     5        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
     6    })
     7  
     8    with req.urlopen(request) as response:
     9        data = response.read().decode("utf-8")
    10  
    11    import bs4
    12    root = bs4.BeautifulSoup(data,"html.parser")
    13  
    14    titles = root.find_all("li", class_="title")
    15    pubs = root.find_all("li", class_="publish")
    16    for pub, title in zip(pubs, titles):
    17        print(pub.span.string,title.a.string)
    18  

    Dec  豁達人生選股機－免費開放使用中！
    Mar  博智(8155)_強勢型成長股_2019.4Q&2020/02
    Mar  月報（2019.3Q&2020/02）－好好思考長期機率的分配
    Mar  個股回顧_原相(3227)
    Feb  月報_穩定型成長股＆強勢型成長股_2019.3Q&2020/01－崩盤起因於過於繁榮
    Jan  豁達人生2019年回顧－報酬率、再論大盤MACD、白銀ETF、傻瓜精神
    Jan  原相(3227)_強勢型成長股_2019.3Q&2019/12
    Jan  鈺太(6679)_穩定型成長股_2019.3Q&2019/12
    Jan  月報_穩定型成長股＆強勢型成長股_2019.3Q&2019/12
    Jan  個股回顧_博智(8155)
    Jan  個股回顧_優群(3217)
    Dec  月報_穩定型成長股＆強勢型成長股_2019.3Q&2019/11
    Nov  博智(8155)_強勢型成長股_2019.3Q&2019/10
    Nov  信驊(5274)_穩定型成長股_2019.3Q&2019/10
    Nov  優群(3217)_穩定型成長股_2019.3Q&2019/10


<a id="orgab3faec"></a>

# 如何把python程式publish成網站應用程式


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> [輕鬆學習 Python：conda 的核心功能](https://medium.com/datainpoint/python-essentials-conda-quickstart-1f1e9ecd1025)

<sup><a id="fn.2" href="#fnr.2">2</a></sup> [What are the differences between Conda nd Anaconda?](https://stackoverflow.com/questions/30034840/what-are-the-differences-between-conda-and-anaconda)

<sup><a id="fn.3" href="#fnr.3">3</a></sup> [Python爬蟲解析庫——BeautifulSoup4](https://kknews.cc/code/y3mzkgg.html)

<sup><a id="fn.4" href="#fnr.4">4</a></sup> [python網路爬蟲教學-Selenium基本操作](https://freelancerlife.info/zh/blog/python%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2%E6%95%99%E5%AD%B8-selenium%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/)

<sup><a id="fn.5" href="#fnr.5">5</a></sup> [Day01 Anaconda環境安裝!](https://ithelp.ithome.com.tw/articles/10192460)

<sup><a id="fn.6" href="#fnr.6">6</a></sup> [從零開始學資料科學：Numpy 基礎入門](https://blog.techbridge.cc/2017/07/28/data-science-101-numpy-tutorial/)

<sup><a id="fn.7" href="#fnr.7">7</a></sup> [matplotlib.pyplot.subplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html)

<sup><a id="fn.8" href="#fnr.8">8</a></sup> [conda、miniconda、anaconda的區別以及在pycharm中選擇conda的虛擬環境](https://blog.csdn.net/qq_18668137/article/details/80807829)

<sup><a id="fn.9" href="#fnr.9">9</a></sup> [Python讀寫csv檔案的幾種方法 及 pandas.read<sub>csv引數全解</sub>](https://www.itread01.com/content/1547569271.html)

<sup><a id="fn.10" href="#fnr.10">10</a></sup> [Day23- 資料處理模組-Pandas 介紹](https://ithelp.ithome.com.tw/articles/10208412)

<sup><a id="fn.11" href="#fnr.11">11</a></sup> [你不可不知的 JSON 基本介紹](https://blog.wu-boy.com/2011/04/%E4%BD%A0%E4%B8%8D%E5%8F%AF%E4%B8%8D%E7%9F%A5%E7%9A%84-json-%E5%9F%BA%E6%9C%AC%E4%BB%8B%E7%B4%B9/)

<sup><a id="fn.12" href="#fnr.12">12</a></sup> [Anaconda、Miniconda、Conda、pip的相互關係 (轉載)](https://medium.com/ai%E5%8F%8D%E6%96%97%E5%9F%8E/anaconda-miniconda-conda-pip%E7%9A%84%E7%9B%B8%E4%BA%92%E9%97%9C%E4%BF%82-%E8%BD%89%E8%BC%89-a0536f3a257)
