```python
import numpy as np
from scipy.stats import *
import pandas as pd
import math

# Jupyter Notebook의 출력을 소수점 이하 3자리로 제한
%precision 3

```




    '%.3f'




```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
```


```python
import matplotlib.font_manager as fm  # 폰트확인 
font_list = [font.name for font in fm.fontManager.ttflist] # 설치된 폰트 확인 
font_list
plt.rcParams['font.family'] = 'Malgun Gothic' #폰트 변경 
```




    ['DejaVu Sans Mono',
     'STIXSizeOneSym',
     'cmex10',
     'cmsy10',
     'DejaVu Sans Mono',
     'STIXSizeFourSym',
     'STIXNonUnicode',
     'STIXSizeTwoSym',
     'DejaVu Serif Display',
     'cmtt10',
     'STIXGeneral',
     'STIXSizeFiveSym',
     'STIXSizeThreeSym',
     'DejaVu Serif',
     'STIXSizeFourSym',
     'STIXGeneral',
     'DejaVu Sans',
     'DejaVu Sans Display',
     'STIXSizeOneSym',
     'DejaVu Sans Mono',
     'DejaVu Sans Mono',
     'STIXNonUnicode',
     'cmmi10',
     'STIXNonUnicode',
     'STIXSizeTwoSym',
     'cmss10',
     'STIXSizeThreeSym',
     'cmb10',
     'DejaVu Serif',
     'STIXGeneral',
     'DejaVu Sans',
     'DejaVu Serif',
     'DejaVu Sans',
     'STIXNonUnicode',
     'cmr10',
     'STIXGeneral',
     'DejaVu Serif',
     'DejaVu Sans',
     'Cambria',
     'Onyx',
     'Algerian',
     'Impact',
     'Colonna MT',
     'Gadugi',
     'Calisto MT',
     'Lucida Fax',
     'HYShortSamul-Medium',
     'HYsupM',
     'Tw Cen MT Condensed Extra Bold',
     'Eras Demi ITC',
     'Goudy Old Style',
     'Courier New',
     'Broadway',
     'HYMyeongJo-Extra',
     'Verdana',
     'Century Gothic',
     'Microsoft Yi Baiti',
     'Lucida Handwriting',
     'Playbill',
     'Batang',
     'Berlin Sans FB Demi',
     'Bodoni MT',
     'FZSong_Superfont',
     'Rockwell',
     'Bauhaus 93',
     'Footlight MT Light',
     'Yu Gothic',
     'Georgia',
     'Garamond',
     'Berlin Sans FB',
     'Calibri',
     'Rockwell Condensed',
     'Tahoma',
     'Tahoma',
     'Bodoni MT',
     'Symbol',
     'Trebuchet MS',
     'Rage Italic',
     'Candara',
     'Consolas',
     'Candara',
     'Kunstler Script',
     'Ami R',
     'Book Antiqua',
     'Franklin Gothic Demi',
     'Nirmala UI',
     'Gigi',
     'Tw Cen MT Condensed',
     'Elephant',
     'Arial',
     'Mistral',
     'Constantia',
     'Wingdings 2',
     'Lucida Sans Unicode',
     'Arial',
     'Franklin Gothic Heavy',
     'Century Schoolbook',
     'Garamond',
     'Microsoft PhagsPa',
     'Niagara Engraved',
     'Leelawadee UI',
     'Segoe UI',
     'Gadugi',
     'Wingdings',
     'MS Reference Sans Serif',
     'Eras Medium ITC',
     'Calibri',
     'Cooper Black',
     'Haansoft Dotum',
     'Segoe Script',
     'Tw Cen MT Condensed',
     'Mistral',
     'Tempus Sans ITC',
     'Microsoft YaHei',
     'Trebuchet MS',
     'Segoe UI',
     'Edwardian Script ITC',
     'Segoe UI',
     'Sitka Small',
     'Century Gothic',
     'HYporM',
     'Calibri',
     'Segoe UI',
     'Perpetua Titling MT',
     'Tahoma',
     'Wingdings 3',
     'Lucida Sans Typewriter',
     'MV Boli',
     'Gill Sans MT',
     'Segoe UI',
     'NanumGothic',
     'Centaur',
     'Malgun Gothic',
     'MingLiU-ExtB',
     'HYtbrB',
     'Playbill',
     'Bodoni MT',
     'Lucida Sans Typewriter',
     'Verdana',
     'HYporM',
     'Palatino Linotype',
     'Rockwell',
     'Bodoni MT',
     'Jokerman',
     'Brush Script MT',
     'NanumGothic',
     'Harlow Solid Italic',
     'Georgia',
     'Stencil',
     'Cambria',
     'Gulim',
     'Pristina',
     'HYmprL',
     'Yu Gothic',
     'Times New Roman',
     'HYkanM',
     'Segoe UI',
     'HYdnkM',
     'OCR A Extended',
     'Bell MT',
     'Courier New',
     'Segoe UI',
     'SimSun-ExtB',
     'Malgun Gothic',
     'Niagara Solid',
     'Leelawadee UI',
     'Eras Medium ITC',
     'HyhwpEQ',
     'Lucida Calligraphy',
     'Tw Cen MT Condensed',
     'HoloLens MDL2 Assets',
     'Lucida Bright',
     'Verdana',
     'Gill Sans MT Condensed',
     'Lucida Bright',
     'Verdana',
     'HoloLens MDL2 Assets',
     'Lucida Sans',
     'Papyrus',
     'HYMyeongJo-Extra',
     'Microsoft Tai Le',
     'Haettenschweiler',
     'Consolas',
     'Californian FB',
     'Matura MT Script Capitals',
     'Franklin Gothic Medium',
     'Yu Gothic',
     'Algerian',
     'Tempus Sans ITC',
     'HYmprL',
     'Corbel',
     'Courier New',
     'Century Schoolbook',
     'Georgia',
     'Gloucester MT Extra Condensed',
     'Perpetua Titling MT',
     'Snap ITC',
     'HYPost-Medium',
     'New Gulim',
     'Perpetua',
     'Palace Script MT',
     'Century Schoolbook',
     'FZSong_Superfont',
     'HYnamB',
     'Franklin Gothic Medium',
     'Segoe UI Symbol',
     'HYsupM',
     'Agency FB',
     'Informal Roman',
     'Copperplate Gothic Light',
     'ahn2006-B',
     'Leelawadee UI',
     'Sitka Small',
     'MS Outlook',
     'Lucida Sans Typewriter',
     'Lucida Calligraphy',
     'Mongolian Baiti',
     'NanumGothic',
     'Vladimir Script',
     'Gill Sans MT',
     'Arial',
     'Nirmala UI',
     'Georgia',
     'Wide Latin',
     'Engravers MT',
     'MT Extra',
     'Vivaldi',
     'Gill Sans MT',
     'Myanmar Text',
     'HYPost-Light',
     'Lucida Fax',
     'High Tower Text',
     'Footlight MT Light',
     'Gill Sans MT',
     'Tw Cen MT',
     'OCR A Extended',
     'HYHeadLine-Medium',
     'Microsoft JhengHei',
     'Franklin Gothic Book',
     'Segoe UI',
     'Bradley Hand ITC',
     'Bernard MT Condensed',
     'HYgsrB',
     'Microsoft New Tai Lue',
     'Gill Sans Ultra Bold Condensed',
     'HYShortSamul-Medium',
     'Sitka Small',
     'Headline R',
     'Franklin Gothic Demi Cond',
     'Arial Unicode MS',
     'Comic Sans MS',
     'Arial',
     'Century Gothic',
     'Segoe Script',
     'Constantia',
     'Colonna MT',
     'Palace Script MT',
     'Felix Titling',
     'Malgun Gothic',
     'Bodoni MT',
     'Calibri',
     'Bodoni MT',
     'Rockwell Condensed',
     'Blackadder ITC',
     'Myanmar Text',
     'Rockwell',
     'Lucida Bright',
     'HYGothic-Extra',
     'Pyunji R',
     'Script MT Bold',
     'Matura MT Script Capitals',
     'Freestyle Script',
     'Microsoft YaHei',
     'HYsnrL',
     'HYPost-Light',
     'Calisto MT',
     'Gill Sans MT Ext Condensed Bold',
     'Century Gothic',
     'Segoe UI',
     'Berlin Sans FB',
     'Magic R',
     'Javanese Text',
     'Ravie',
     'Microsoft JhengHei',
     'Rage Italic',
     'HYGothic-Medium',
     'Bell MT',
     'Segoe UI',
     'Eras Light ITC',
     'Agency FB',
     'Verdana',
     'Corbel',
     'NanumGothic',
     'Century Schoolbook',
     'Bodoni MT',
     'Kunstler Script',
     'ahn2006-M',
     'Poor Richard',
     'Palatino Linotype',
     'ahn2006-B',
     'Arial',
     'Cambria',
     'Arial',
     'Segoe Print',
     'Ebrima',
     'Tw Cen MT',
     'Segoe UI',
     'Lucida Handwriting',
     'Gill Sans MT',
     'Lucida Sans Unicode',
     'Tw Cen MT',
     'Eras Light ITC',
     'Sitka Small',
     'Brush Script MT',
     'Webdings',
     'Perpetua',
     'MT Extra',
     'Bookman Old Style',
     'Candara',
     'Arial',
     'Californian FB',
     'Engravers MT',
     'Bell MT',
     'Goudy Old Style',
     'Corbel',
     'Lucida Sans',
     'Comic Sans MS',
     'HYwulM',
     'Bodoni MT',
     'HYkanB',
     'Calisto MT',
     'Bookman Old Style',
     'Calisto MT',
     'Century Gothic',
     'Calisto MT',
     'Myanmar Text',
     'Juice ITC',
     'Century Schoolbook',
     'Segoe MDL2 Assets',
     'Palatino Linotype',
     'Chiller',
     'Sylfaen',
     'Perpetua',
     'HYsanB',
     'Marlett',
     'Microsoft JhengHei',
     'Freestyle Script',
     'Tw Cen MT',
     'Garamond',
     'HYbdaM',
     'Old English Text MT',
     'Corbel',
     'Microsoft JhengHei',
     'High Tower Text',
     'Perpetua',
     'Century',
     'Tahoma',
     'Lucida Fax',
     'Microsoft YaHei',
     'Lucida Sans',
     'Times New Roman',
     'Franklin Gothic Medium Cond',
     'NanumGothic',
     'Lucida Fax',
     'Bookman Old Style',
     'Pristina',
     'Imprint MT Shadow',
     'Bookman Old Style',
     'Jokerman',
     'Eras Demi ITC',
     'Ink Free',
     'Segoe UI Historic',
     'Haansoft Batang',
     'Californian FB',
     'Tw Cen MT Condensed',
     'Book Antiqua',
     'Microsoft YaHei',
     'Mongolian Baiti',
     'Bodoni MT',
     'Comic Sans MS',
     'Nirmala UI',
     'Segoe UI',
     'Segoe Script',
     'Modern No. 20',
     'Consolas',
     'MingLiU-ExtB',
     'Copperplate Gothic Bold',
     'Calibri',
     'Arial',
     'Kristen ITC',
     'HYnamM',
     'Bahnschrift',
     'Segoe UI',
     'Californian FB',
     'Bahnschrift',
     'Leelawadee UI',
     'Javanese Text',
     'Microsoft YaHei',
     'Consolas',
     'Vladimir Script',
     'Times New Roman',
     'HYcysM',
     'Candara',
     'Haansoft Dotum',
     'Agency FB',
     'Gigi',
     'HYwulB',
     'Ink Free',
     'Goudy Old Style',
     'Sitka Small',
     'Bodoni MT',
     'MS Reference Specialty',
     'HYbdaM',
     'Bookman Old Style',
     'Trebuchet MS',
     'HYgtrE',
     'HYhaeseo',
     'Wingdings',
     'Rockwell',
     'Cambria',
     'HYkanB',
     'HYGraphic-Medium',
     'Perpetua',
     'Nirmala UI',
     'Castellar',
     'Rockwell',
     'Magic R',
     'Goudy Old Style',
     'HYhaeseo',
     'Book Antiqua',
     'Bookman Old Style',
     'Copperplate Gothic Light',
     'Calibri',
     'Rockwell Condensed',
     'Tw Cen MT',
     'HYdnkB',
     'Candara',
     'Candara',
     'Trebuchet MS',
     'Centaur',
     'Arial',
     'Lucida Fax',
     'HYmjrE',
     'Rockwell Condensed',
     'Gadugi',
     'Tw Cen MT Condensed Extra Bold',
     'Georgia',
     'Comic Sans MS',
     'HYkanM',
     'Modern No. 20',
     'HYbdaL',
     'Century Gothic',
     'Arial',
     'Segoe UI',
     'Candara',
     'Bookshelf Symbol 7',
     'Elephant',
     'Monotype Corsiva',
     'NanumGothic',
     'Calisto MT',
     'Lucida Bright',
     'Trebuchet MS',
     'MS Reference Sans Serif',
     'Edwardian Script ITC',
     'Microsoft New Tai Lue',
     'HYsupB',
     'Bodoni MT',
     'Britannic Bold',
     'Segoe MDL2 Assets',
     'Batang',
     'Broadway',
     'Parchment',
     'Curlz MT',
     'HYgprM',
     'New Gulim',
     'Arial',
     'Bodoni MT',
     'Garamond',
     'Cooper Black',
     'Harrington',
     'Trebuchet MS',
     'Headline R',
     'Niagara Solid',
     'Microsoft Himalaya',
     'HYgtrE',
     'Segoe Script',
     'Arial',
     'Corbel',
     'Blackadder ITC',
     'Century Gothic',
     'Bodoni MT',
     'Candara',
     'Franklin Gothic Heavy',
     'Segoe UI',
     'Lucida Sans',
     'Wingdings 3',
     'Goudy Old Style',
     'Agency FB',
     'HYdnkM',
     'Constantia',
     'Perpetua Titling MT',
     'Calibri',
     'Franklin Gothic Medium Cond',
     'HYGungSo-Bold',
     'Copperplate Gothic Bold',
     'Cambria',
     'Corbel',
     'Malgun Gothic',
     'Webdings',
     'Wide Latin',
     'Arial',
     'Bodoni MT',
     'Cambria',
     'HYGothic-Extra',
     'Perpetua Titling MT',
     'Segoe UI',
     'Microsoft New Tai Lue',
     'Bauhaus 93',
     'Candara',
     'Segoe UI Symbol',
     'Constantia',
     'Viner Hand ITC',
     'Calibri',
     'MS Outlook',
     'MS Reference Specialty',
     'Bodoni MT',
     'SimSun',
     'Georgia',
     'Century Schoolbook',
     'HYcysM',
     'Arial Rounded MT Bold',
     'Franklin Gothic Book',
     'Candara',
     'Symbol',
     'Constantia',
     'Parchment',
     'Gill Sans MT',
     'Arial',
     'Script MT Bold',
     'Yu Gothic',
     'Goudy Old Style',
     'Courier New',
     'Tw Cen MT',
     'Segoe Print',
     'Franklin Gothic Medium',
     'Californian FB',
     'Verdana',
     'HYGothic-Medium',
     'Perpetua',
     'Rockwell',
     'HYtbrB',
     'Maiandra GD',
     'Arial',
     'Microsoft YaHei',
     'Segoe UI',
     'High Tower Text',
     'Haettenschweiler',
     'HYbsrB',
     'HYdnkB',
     'Segoe UI Historic',
     'Rockwell Extra Bold',
     'Wingdings 2',
     'HYsupB',
     'Kristen ITC',
     'Comic Sans MS',
     'Sitka Small',
     'Microsoft PhagsPa',
     'Segoe UI',
     'Sitka Small',
     'Verdana',
     'Berlin Sans FB Demi',
     'Tw Cen MT',
     'Lucida Sans',
     'Gulim',
     'Gabriola',
     'Consolas',
     'MoeumT R',
     'Bodoni MT',
     'Britannic Bold',
     'Corbel',
     'Constantia',
     'Perpetua',
     'Bookman Old Style',
     'Myanmar Text',
     'Berlin Sans FB',
     'HYPMokGak-Bold',
     'Courier New',
     'Garamond',
     'Goudy Stout',
     'MS Gothic',
     'Franklin Gothic Book',
     'High Tower Text',
     'Microsoft Sans Serif',
     'Verdana',
     'Trebuchet MS',
     'Snap ITC',
     'Franklin Gothic Heavy',
     'Microsoft JhengHei',
     'Rockwell Extra Bold',
     'Bradley Hand ITC',
     'Ebrima',
     'Lucida Bright',
     'Calibri',
     'Yu Gothic',
     'Gill Sans Ultra Bold',
     'Leelawadee UI',
     'Palatino Linotype',
     'Lucida Fax',
     'Lucida Sans Typewriter',
     'Maiandra GD',
     'Lucida Sans',
     'HYnamM',
     'Lucida Sans Typewriter',
     'Book Antiqua',
     'Palatino Linotype',
     'Book Antiqua',
     'Corbel',
     'HYPost-Medium',
     'Comic Sans MS',
     'Book Antiqua',
     'Bodoni MT',
     'Vivaldi',
     'Franklin Gothic Demi',
     'Candara',
     'Garamond',
     'Segoe UI Emoji',
     'Californian FB',
     'Segoe UI',
     'Times New Roman',
     'Arial Rounded MT Bold',
     'Georgia',
     'HYSinMyeongJo-Medium',
     'French Script MT',
     'Monotype Corsiva',
     'Elephant',
     'Franklin Gothic Demi Cond',
     'Lucida Bright',
     'Palatino Linotype',
     'Gloucester MT Extra Condensed',
     'Nirmala UI',
     'SimSun-ExtB',
     'Constantia',
     'Microsoft Tai Le',
     'Corbel',
     'HYsnrL',
     'Gill Sans MT',
     'Informal Roman',
     'Cambria',
     'Lucida Bright',
     'HYPMokGak-Bold',
     'Curlz MT',
     'Poor Richard',
     'Gabriola',
     'ahn2006-L',
     'Consolas',
     'MoeumT R',
     'Papyrus',
     'MV Boli',
     'Lucida Fax',
     'Bell MT',
     'Showcard Gothic',
     'Segoe Print',
     'Lucida Console',
     'Georgia',
     'Bodoni MT',
     'Palatino Linotype',
     'Ebrima',
     'Lucida Sans Typewriter',
     'Courier New',
     'Courier New',
     'Malgun Gothic',
     'Microsoft Himalaya',
     'Elephant',
     'Calibri',
     'Microsoft JhengHei',
     'Segoe UI',
     'Times New Roman',
     'Felix Titling',
     'Corbel',
     'Calibri',
     'Gill Sans MT Condensed',
     'Century Schoolbook',
     'Bookshelf Symbol 7',
     'Gill Sans MT Ext Condensed Bold',
     'Impact',
     'HyhwpEQ',
     'MS Gothic',
     'Niagara Engraved',
     'Bell MT',
     'Franklin Gothic Demi',
     'Gadugi',
     'Ebrima',
     'Cambria',
     'HYmjrE',
     'Magneto',
     'Sitka Small',
     'Gill Sans Ultra Bold Condensed',
     'Rockwell',
     'Chiller',
     'Magneto',
     'Corbel',
     'Lucida Console',
     'Gill Sans MT',
     'Candara',
     'Calisto MT',
     'Goudy Stout',
     'HYHeadLine-Medium',
     'Lucida Sans Typewriter',
     'French Script MT',
     'Bernard MT Condensed',
     'Microsoft Yi Baiti',
     'Arial',
     'Microsoft Tai Le',
     'Segoe UI',
     'Franklin Gothic Medium',
     'Palatino Linotype',
     'Castellar',
     'Berlin Sans FB',
     'Sylfaen',
     'Century Schoolbook',
     'Yet R',
     'Book Antiqua',
     'Yu Gothic',
     'HYSinMyeongJo-Medium',
     'Bookman Old Style',
     'Nirmala UI',
     'Pyunji R',
     'Yu Gothic',
     'Bodoni MT',
     'Times New Roman',
     'Imprint MT Shadow',
     'Constantia',
     'Bodoni MT',
     'HYsanB',
     'Century',
     'Gill Sans Ultra Bold',
     'Haansoft Batang',
     'Lucida Sans',
     'Yet R',
     'Perpetua',
     'Ravie',
     'Comic Sans MS',
     'Viner Hand ITC',
     'Franklin Gothic Demi',
     'Segoe UI',
     'Franklin Gothic Heavy',
     'Lucida Bright',
     'Malgun Gothic',
     'Stencil',
     'Calibri',
     'Ami R',
     'HYwulB',
     'Century Gothic',
     'Consolas',
     'Eras Bold ITC',
     'ahn2006-M',
     'HYGungSo-Bold',
     'HYGraphic-Medium',
     'Times New Roman',
     'HYbdaL',
     'Segoe UI Emoji',
     'Bodoni MT',
     'Tw Cen MT',
     'Segoe UI',
     'Baskerville Old Face',
     'Calisto MT',
     'SimSun',
     'Juice ITC',
     'Microsoft New Tai Lue',
     'HYnamL',
     'Onyx',
     'Microsoft Sans Serif',
     'Baskerville Old Face',
     'HYgprM',
     'HYnamB',
     'Leelawadee UI',
     'Trebuchet MS',
     'Times New Roman',
     'Yu Gothic',
     'Comic Sans MS',
     'Arial',
     'Showcard Gothic',
     'Microsoft PhagsPa',
     'HYbsrB',
     'Lucida Sans',
     'Courier New',
     'Lucida Sans Typewriter',
     'Rockwell',
     'Old English Text MT',
     'Arial Unicode MS',
     'HYgsrB',
     'Franklin Gothic Book',
     'Forte',
     'Segoe UI',
     'HYwulM',
     'Consolas',
     'Harrington',
     'Harlow Solid Italic',
     'ahn2006-L',
     'Lucida Fax',
     'Bodoni MT',
     'Arial',
     'Bell MT',
     'Microsoft Tai Le',
     'Segoe Print',
     'HYnamL',
     'Corbel',
     'Forte',
     'Eras Bold ITC',
     'Book Antiqua',
     'Microsoft PhagsPa']




    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[4], line 4
          2 font_list = [font.name for font in fm.fontManager.ttflist] # 설치된 폰트 확인 
          3 font_list
    ----> 4 plt.rcParams['font.family'] = 'Malgun Gothic'
    

    NameError: name 'plt' is not defined


![image.png](attachment:image.png)

![image.png](attachment:image.png)

# 기술 통계량

### 데이터의 특징을 요약, 기술하는 통계량
- 위치 통계량(measure of location)
    - 데이터의 중심 위치를 나타내는 척도(대표값)
    - 평균, 중위수, 절사평균, 최빈수, 사분위수 등

- 변이 통계량(measure of dispersion)
    - 데이터의 퍼짐,흩어진 정도를 나타내는 척도(산포도)
    - 표준편차, 분산, 사분위간범위 등

- 모양 통계량(measure of shape)
    - 왜도
        - 중심 위치로부터 어느 한쪽으로 치우친(비대칭) 정도를 나타내는 척도
    - 첨도
        - 분포의 뾰족한 정도
        
      ![image.png](attachment:image.png)  


### 위치 통계량(중심경향성)

####  평균(mean)
- 가장 많이 사용되는 대표값
    - 모든 데이터의 합을 데이터의 개수로 나눈 값(산술평균)
   ![](평균.png)

- 특징
    - 계산이 쉽고, 수학적으로 활용하기 편리하며 각 자료에 대해 유일한 값을 가짐
    - 분산의 계산, 모수 추정, 가설검정 등 통계분석의 대표적인 통계량으로 널리 사용됨
    - 데이터에 극단적인 값이 포함될 경우 평균이 왜곡되는 경향이 있음
    - 이러한 경우, 대표 값으로 중앙값을 사용 

- 모평균 : 값을 구하기 위한 모든 데이터들의 평균
- 표준평균 : 모든 값을 구할 수 없기 때문에 신뢰도가 훼손되지 않는 선에서 값들을 추출하여 구한 평균

#### 산술 평균 계산
- 가장 널리 사용되는 평균으로 연속형 변수에 대해 사용
- 다른 관측치에 비해 매우크거나 작은값에 크게 영향을받음


```python
x = [1, 2, 3, 4, 5]
np.mean(x) # 넘파이
np.array(x).mean() # 파이썬
pd.Series(x).mean() # 판다스 시리즈
```




    3.000






    3.000






    3.000




```python
# 이진 변수(0과 1로 구성)에 대한 평균 - 이진 변수에 대한 산술평균은 1의 비율과 같음
x = [1, 0, 0, 0, 1]
np.mean(x) # 넘파이
np.array(x).mean() # 파이썬
pd.Series(x).mean() # 판다스 시리즈
```




    0.400






    0.400






    0.400




```python
df = pd.read_csv('../jupyter/ch2_scores_em.csv',
                 index_col='student number')
# df의 처음 5행을 표시
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>english</th>
      <th>mathematics</th>
    </tr>
    <tr>
      <th>student number</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>42</td>
      <td>65</td>
    </tr>
    <tr>
      <th>2</th>
      <td>69</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>56</td>
      <td>63</td>
    </tr>
    <tr>
      <th>4</th>
      <td>41</td>
      <td>63</td>
    </tr>
    <tr>
      <th>5</th>
      <td>57</td>
      <td>76</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 10개 영어점수만 추출 후 저장
scores = np.array(df['english'])[:10]
scores
```




    array([42, 69, 56, 41, 57, 48, 65, 49, 65, 58], dtype=int64)




```python
scores_df = pd.DataFrame({'score':scores},
                         index=pd.Index(['A', 'B', 'C', 'D', 'E',
                                         'F', 'G', 'H', 'I', 'J'],
                                        name='student'))
scores_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
    </tr>
    <tr>
      <th>student</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>42</td>
    </tr>
    <tr>
      <th>B</th>
      <td>69</td>
    </tr>
    <tr>
      <th>C</th>
      <td>56</td>
    </tr>
    <tr>
      <th>D</th>
      <td>41</td>
    </tr>
    <tr>
      <th>E</th>
      <td>57</td>
    </tr>
    <tr>
      <th>F</th>
      <td>48</td>
    </tr>
    <tr>
      <th>G</th>
      <td>65</td>
    </tr>
    <tr>
      <th>H</th>
      <td>49</td>
    </tr>
    <tr>
      <th>I</th>
      <td>65</td>
    </tr>
    <tr>
      <th>J</th>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 산술평균
sum(scores)/len(scores)
np.mean(scores)
scores_df.mean()

```




    55.000






    55.000






    score    55.0
    dtype: float64



#### 기하평균
- n개의 양수 값을 모두 곱한 것의 n 제곱근
- 성장률의 평균
![](기하평균.png)


- 아래 year데이터는 어느 회사의 매출 증가율을 수집해 놓은 데이터임
    - 1차년도에 200% , 2차년도에 800%, 3차년도에 300% 성장을 했다면 연평균 성장율은 어떻게 되는가?


```python
year = [2,8,3]
```


```python
# 위 데이터의 산술 평균
np.mean(year)

# 매년 430% 성장으로 나타남 - 1차년도에 430% 2차년도 430% 3차년도 430% 라면 전년대비 성장이므로 이 회사는 3개년동안
#  430*430*430 성장한게 되므로 총 79507000 성장한상황이 됨

# 실제 성장은 200*800*300 으로 48000000 성장한 것 이므로 차이가 많다

# 이렇게 곱하기를 해서 나오는 값에 대한 평균은 산술평균을 사용하면 의미가 달라지므로 기하평균을 사용해야 함
```




    4.333



### 매출 증가율 예시
![image.png](attachment:image.png)


```python
# 집합자료형을 인수로 받아 모든 원소를 곱한 결과를 반환하는 함수

def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
                return 0
        ans *= n
    return ans
```


```python
# 기하평균
multiply(year) ** (1/len(year))

# 연평균 약 363% 증가

3.634*3.634*3.634
```




    3.634






    47.990



#### 조화 평균
- mmean() 함수 사용
- 비율 및 변화율에 대한 평균을 계산할 때 사용
- 주어진 수들의 역수들의 산술평균에서 역수를 취한 값
![](조화평균.png)

![image.png](attachment:image.png)

##### 100km 떨어진 도시까지 차로 다녀오면서 가는길에는 시속 80km 오는길은 시속 120km로 달렸을때 평균 속력은 얼마나 되는가?
- 움직인 거리 200km
- 움직인 시간 100/80 + 100/120

![](조화평균예제.png)


```python
x=np.array([80,120])
print(len(x)/np.sum(1/x))
print(hmean(x))
```

    95.99999999999999
    95.99999999999999
    


```python
x = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
print(len(x)/np.sum(1/x))
print(hmean(x))  # 조화평균
np.mean(x)       # 산술평균
```

    0.21897810218978103
    0.21897810218978103
    




    0.300



### 중앙값(median)

- 중위수, 중간값
- 데이터를 크기 순서대로 나열할 때 가운데 위치하는 숫자
- 데이터의 개수가 홀수일 경우 : 가운데 위치하는 유일한 숫자
- 데이터의 개수가 짝수일 경우 : 가운데 위치하는 2개의 숫자의 평균값
    
![image.png](attachment:image.png)
    
- 특징
    - 극단적인 값에 영향을 받지 않는 장점
    - 가운데 위치하는 한 개 또는 두 개의 데이터만으로 계산



- 극단적인 값이 포함된 데이터의 대표 값 비교

- 평균 : 모든 데이터를 전부 고려하여 계산한 값, 무게 중심
- 중앙값 : 데이터의 개수와 순서만을 고려하여 계산 
- 예. 세 개의 추(10kg, 20kg, 60kg)가 있는 경우
    - 평균은 세 무게의 균형을 나타내는 시소의 중심
    - 중앙값은 개수(3)의 중앙(2)을 나타냄 
    - 만약 60kg의 추를 80kg으로 대체할 경우 평균을 나타내는 시소의 중심은 오른쪽으로 이동하지만, 중앙값은 변화하지 않고 그대로 20kg이 됨
![](평균과중앙값의비교.png)


```python
scores
```




    array([42, 69, 56, 41, 57, 48, 65, 49, 65, 58], dtype=int64)




```python
sorted_scores = np.sort(scores)
sorted_scores
len(sorted_scores)
```




    array([41, 42, 48, 49, 56, 57, 58, 65, 65, 69], dtype=int64)






    10




```python
n = len(sorted_scores)
if n % 2 == 0:
    # 중앙 위치 2개값의 평균이 중앙값
    m0 = sorted_scores[n//2-1]
    m1 = sorted_scores[n//2]
    median = (m0 + m1)/2
else:
    # 중앙 위치 1개 값
    median = sorted_scores[(n+1)//2-1]
median
```




    56.500




```python
np.median(scores)
scores_df.median()
```




    56.500






    score    56.5
    dtype: float64



#### 절사 평균(trimmed mean)이 필요한 이유

- 평균의 장점과 중앙값의 장점을 갖는 대표값 
- 예.
    - 체조, 다이빙, 피겨스케이팅 등에서 심판의 주관적인 편견을 배제, 보완하기 위해 제일 높은 점수와 제일 낮은 점수를 제외(중앙값의 장점)한 나머지 심판들의 점수에 대한 평균(평균의 장점)으로 판정
    

- 절사평균을 계산하려면 절사비율(%)을 결정해야 함 

    - 절사비율은 전체 데이터의 개수에 대해 몇 %의 데이터(상위+하위)를 배제할 것인가로 결정
    - 만약 5개의 데이터에 대해 가장 낮은 점수와 가장 높은 점수 각각 1개씩을 배제한다면 절사율은 40%(2/5)가 됨
    - 5개의 데이터에 대해 40% 절사평균
    - 데이터를 순서대로 정렬한 경우 가운데 위치하는 3개의 평균으로 계산



```python
np.random.seed(0)
# 소득 평균이 2백만원이고 표준편차가 50만원인 정규분포를 따르는 소득 생성
# 100명의 소득 생성
income = np.random.normal(2000000,500000,100)
income
np.mean(income)
```




    array([2882026.173, 2200078.604, 2489368.992, 3120446.6  , 2933778.995,
           1511361.06 , 2475044.209, 1924321.396, 1948390.574, 2205299.251,
           2072021.786, 2727136.753, 2380518.863, 2060837.508, 2221931.616,
           2166837.164, 2747039.537, 1897420.868, 2156533.851, 1572952.13 ,
            723505.092, 2326809.298, 2432218.099, 1628917.49 , 3134877.312,
           1272817.163, 2022879.259, 1906408.075, 2766389.607, 2734679.385,
           2077473.713, 2189081.26 , 1556107.126, 1009601.766, 1826043.925,
           2078174.485, 2615145.34 , 2601189.924, 1806336.591, 1848848.625,
           1475723.517, 1289991.031, 1146864.905, 2975387.698, 1745173.909,
           1780962.849, 1373602.32 , 2388745.178, 1193051.076, 1893629.86 ,
           1552266.719, 2193451.249, 1744597.431, 1409683.908, 1985908.886,
           2214165.935, 2033258.611, 2151235.949, 1682838.953, 1818629.417,
           1663769.776, 1820223.419, 1593426.859, 1136858.699, 2088713.071,
           1799109.532, 1184900.827, 2231391.128, 1546350.818, 2025972.698,
           2364545.281, 2064491.455, 2569700.342, 1382587.09 , 2201170.821,
           1657594.955, 1564601.425, 1710575.168, 1844223.734, 2028082.671,
           1417425.08 , 2450413.243, 2232831.22 , 1231878.157, 2744126.097,
           2947944.588, 2589389.786, 1910037.582, 1464623.689, 2527225.863,
           1798411.527, 2611222.535, 2104137.489, 2488319.518, 2178183.199,
           2353286.584, 2005250.01 , 2892935.247, 2063456.046, 2200994.682])






    2029904.008




```python
 # 소득이 10억원인 사람의 등장
income = np.append(income, 10**9)
 # 100명의 소득이 200만원에 가까운데, 한 명 때문에 대표값인 평균이 1200만원에 달함
np.mean(income)
```




    11910796.047



#### 절사 평균 계산: trim_mean((x,proportiontocnt)

proportiontocnt : 절사율


- 매우 크거나 작은 값에 의한 영향을 줄이기 위해 고안 됨
- 데이터에서 범위에 속하는 데이터에 대해서만 평균을 낸 것


```python
trim_mean(income, 0.2)  # 절사율 20%  20~80% 범위 내의 값
```




    2031747.353



### 최빈값(mode)

- 자료 중 가장 자주 나타나는(빈도가 가장 많은) 관측치
   - 평균, 중위수와 달리 자료에 따라 존재하지 않을수도 있고, 유일한 값이 아닐 수도 있음
   - 질적 변수에도 활용
   

- 중앙값과 최빈값의 특징

   -  자료 속에 극단적인 `이상치가 있는 경우 극단적 관찰치에 덜 민감한 중앙값을 사용`
   -  `자료의 분포가 비대칭`인 경우 평균의 보조 자료로 활용
   -  개방 구간을 갖는 도수분포표의 경우 `중앙값 또는 최빈값을 대표값`으로 사용
   -  `명목자료와 서열자료의 경우 최빈값` 사용

#### 최빈값 계산
- 한 변수가 가장 많이 취한 값을의미,범주형 변수에 대해서만적용


```python
np.random.seed()
x = np.random.choice(['A', 'B', 'C','D'], 1000) # A, B, C라는 요소로 구성
x[:10]
len(x)
```




    array(['B', 'B', 'A', 'B', 'C', 'D', 'C', 'D', 'D', 'D'], dtype='<U1')






    1000




```python
mode(x)
mode(x).mode  # 가장 빈도가 높은 원소
mode(x).count # 가장 빈도가 높은 원소의 빈도수
```




    ModeResult(mode=array(['C'], dtype='<U1'), count=array([269]))






    array(['C'], dtype='<U1')






    array([269])




```python
# value_counts()의 결과는 빈도에 따라 내림차순으로 반환
# C 343
# B 250
pd.Series(x).value_counts().index[0]
pd.Series(x).value_counts()[0]

```




    'C'






    269



### 사분위수(quartile)


- 자료를 크기 순으로 늘어 놓은 수 4등분하여 각각의 경계에 있는 수
    - 제1사분위수(하사분위수, Q1, the first quartile)
        - 자료의 ¼  또는 25%에 해당하는 값
        - 𝑄1=(𝑛+1)1/4=(𝑛+1)25/100 번째순위값 

    - 제2사분위수(중위수, Q2, the second quartile)
        - 자료의 2/4 또는 50%에 해당하는 값

    - 제3사분위수(상사분위수, Q3, the third quartile)
        - 자료의 ¾ 또는 75%에 해당하는 값
        - 𝑄3=(𝑛+1)3/4=(𝑛+1)75/100 번째순위값


### 백분위수(percentile)
- 크기 순으로 나열한 수들을 백등분하여 각각의 경계에 있는 수
    - 제25백분위수
        - 자료의 ¼  또는 25%에 해당하는 값
        - 제1사분위수와 같음(Q1)
        - 𝑄1=(𝑛+1)1/4=(𝑛+1)25/100 번째순위값 

    - 제50백분위수
        - 자료의 2/4 또는 50%에 해당하는 값
        - 제2사분위수(중앙값) 

    - 제75백분위수
        - 자료의 ¾ 또는 75%에 해당하는 값
        - 𝑄3=(𝑛+1)3/4=(𝑛+1)75/100 번째순위값


### 위치 통계량

- 최소값, 제1사분위수, 중위수, 제3사분위수, 최대값
- 상자-수염그림(boxplot)
![](사분위수.png)


```python
np.random.seed(0)
x = np.random.normal(100, 20, size = 1000) 
#평균이 100 표준편차가 20인 데이터 셋 생성(원소 수 1000)
x

```




    array([135.281, 108.003, 119.575, 144.818, 137.351,  80.454, 119.002,
            96.973,  97.936, 108.212, 102.881, 129.085, 115.221, 102.434,
           108.877, 106.673, 129.882,  95.897, 106.261,  82.918,  48.94 ,
           113.072, 117.289,  85.157, 145.395,  70.913, 100.915,  96.256,
           130.656, 129.387, 103.099, 107.563,  82.244,  60.384,  93.042,
           103.127, 124.606, 124.048,  92.253,  93.954,  79.029,  71.6  ,
            65.875, 139.016,  89.807,  91.239,  74.944, 115.55 ,  67.722,
            95.745,  82.091, 107.738,  89.784,  76.387,  99.436, 108.567,
           101.33 , 106.049,  87.314,  92.745,  86.551,  92.809,  83.737,
            65.474, 103.549,  91.964,  67.396, 109.256,  81.854, 101.039,
           114.582, 102.58 , 122.788,  75.303, 108.047,  86.304,  82.584,
            88.423,  93.769, 101.123,  76.697, 118.017, 109.313,  69.275,
           129.765, 137.918, 123.576,  96.402,  78.585, 121.089,  91.936,
           124.449, 104.165, 119.533, 107.127, 114.131, 100.21 , 135.717,
           102.538, 108.04 , 137.663,  73.045,  74.59 , 119.388,  76.538,
           138.872,  91.728,  85.051, 138.459, 129.61 , 137.351, 118.121,
            82.775, 138.201,  94.64 , 116.049, 118.945,  96.9  , 112.282,
           118.444, 107.529,  78.012, 105.965, 126.528,  86.109,  97.007,
            91.297, 136.985, 113.446, 108.149,  84.602, 110.785,  86.513,
           100.637,  87.283, 113.529, 111.532,  95.834, 107.92 ,  78.139,
            70.175, 108.788, 103.333, 112.701, 147.663, 118.89 ,  81.744,
           122.34 ,  73.682,  90.768,  98.635, 134.267,  85.105,  83.471,
            98.031,  86.73 , 122.533,  78.401,  77.051,  91.244,  90.039,
           138.591, 118.988, 101.751,  75.491, 116.887,  79.996,  69.105,
           123.761, 106.339, 118.417, 106.375, 117.137,  86.979,  79.315,
           113.632,  83.932,  86.209,  90.889, 100.35 ,  92.92 ,  72.501,
            87.128,  55.532, 112.505,  67.959,  77.912, 101.043,  85.209,
           130.86 ,  74.143, 105.341,  99.214,  76.638, 110.466,  96.569,
           115.436, 116.47 , 143.265, 126.731,  92.616,  95.212, 121.993,
           113.105, 112.803,  67.661,  99.513,  85.239, 105.598,  98.037,
           118.204, 106.344, 115.727,  90.672,  81.111,  91.799,  99.66 ,
           107.583, 145.186,  99.155,  80.881,  93.08 ,  90.728, 109.63 ,
            69.184, 101.265, 103.13 , 104.644,  88.054,  95.242,  71.519,
            90.134,  89.143, 108.321,  76.876, 115.624, 129.89 ,  58.6  ,
           108.525, 113.538,  87.251,  92.055,  97.342,  94.044,  93.82 ,
            66.48 , 123.047, 121.592,  83.733,  70.672, 110.421,  88.484,
           102.839,  93.613, 113.831, 113.895,  85.488,  72.333,  68.341,
           112.208,  76.223,  89.864,  88.074,  98.949,  61.274, 103.776,
           110.478, 101.768,  93.782, 101.948, 107.981,  44.548, 139.118,
           107.802,  86.952,  92.181, 109.875,  97.678,  59.386, 141.29 ,
            97.789, 120.403,  86.159, 130.728, 105.727, 112.177,  79.095,
           124.223, 113.796, 126.037,  87.438,  90.379, 146.078,  78.8  ,
            97.281, 122.738, 101.954, 111.659,  92.011, 107.401,  73.869,
           133.163,  97.637,  86.396, 113.328,  90.786,  73.315,  73.066,
           113.875,  96.809,  97.326, 121.555,  77.463,  85.386,  92.302,
           101.887,  99.157,  94.262,  98.767,  97.854,  85.608,  83.74 ,
           105.49 ,  82.182,  76.853,  93.754,  96.847, 145.134,  85.906,
           118.865, 114.944,  76.221, 115.465,  76.322,  46.817, 112.126,
            64.882, 109.019,  86.32 , 133.191, 121.37 ,  90.932,  86.243,
            75.718,  91.182,  94.393,  92.706, 103.134, 111.57 , 106.993,
            84.717,  71.244, 127.291,  86.211,  86.954,  89.576,  63.139,
            90.441,  90.407, 112.407, 113.969, 100.075, 118.637, 106.799,
            99.686, 103.219,  96.187,  92.103,  94.645,  77.44 , 105.609,
            80.138, 116.833,  95.011, 100.99 , 109.877, 112.866,  68.588,
            95.862, 117.604,  66.038, 107.746,  54.889,  79.55 , 100.773,
            66.866,  80.29 ,  70.563, 132.963, 103.285, 111.346,  95.546,
            92.931,  67.671,  94.163,  84.77 , 117.158, 122.822, 129.332,
           117.051,  88.027,  77.682, 115.333, 107.126,  64.629, 107.11 ,
           116.29 , 101.179,  96.299,  83.847,  71.069, 116.006,  93.818,
            95.331, 134.654, 113.69 , 107.417, 102.841, 130.4  , 134.392,
           118.59 , 111.644,  58.108, 102.474,  97.398, 101.879, 118.861,
            45.206,  88.614, 105.398,  90.663,  71.662, 117.379, 105.537,
            80.578, 106.296, 116.432, 100.106, 116.011, 101.565,  92.095,
            76.812,  98.281, 103.886, 117.517,  97.698, 109.148,  80.708,
            84.347,  97.792,  78.907, 116.405, 109.263, 105.582, 106.778,
           140.421,  90.623,  55.971, 103.986,  98.988,  89.65 ,  80.423,
            91.216, 103.627,  89.944, 148.249,  80.79 ,  84.138,  54.228,
           105.03 ,  59.672,  89.211,  94.487,  85.805, 134.777, 119.888,
           126.383,  82.352, 122.572, 109.92 , 115.428, 120.589,  81.825,
            91.514, 117.252,  46.888, 130.267, 111.063,  99.086, 104.41 ,
            79.401,  93.001, 122.006, 125.96 , 153.924,  98.522,  86.829,
            89.715,  79.639,  98.443, 107.655,  99.315, 121.927,  95.316,
            93.051,  88.375,  67.347,  68.645,  76.417, 126.029, 117.905,
           127.499,  73.356,  60.628,  86.799, 103.516, 109.974, 120.959,
           105.686, 134.853,  95.548,  81.738,  66.376,  82.221, 104.842,
            82.226, 118.735, 128.247,  52.608, 117.281,  55.208, 108.03 ,
           124.497, 101.297,  74.406,  88.291,  94.767,  96.355,  95.942,
            97.802, 104.27 ,  75.829,  95.16 , 130.365,  92.307,  91.123,
           121.564,  48.816, 123.628,  87.362, 103.279, 101.926, 118.849,
            94.648,  86.439, 125.957,  52.717, 100.407,  73.041,  84.769,
           140.225,  99.108, 103.901,  64.369,  85.419, 103.931, 107.095,
           112.338, 100.173, 110.54 , 109.076,  63.405, 100.74 , 115.358,
           111.798,  92.723,  83.887,  77.634,  97.379, 122.662,  60.964,
            86.802,  77.204, 115.699,  88.914,  90.587,  95.661, 108.908,
            92.152,  39.077, 110.866, 108.781,  95.609,  78.319, 107.036,
           107.585,  90.599,  95.665,  81.397,  96.428,  68.991, 108.346,
            81.113, 104.762,  71.881,  88.199,  97.79 ,  66.786, 102.303,
            92.417,  65.153,  73.935, 112.102, 117.911,  97.362, 108.095,
           104.477, 106.592, 125.72 ,  69.86 , 113.529,  92.36 ,  95.515,
            93.955,  92.497,  75.476, 103.667, 133.419,  98.877,  99.972,
            86.254,  97.651, 109.323,  92.595,  90.924, 108.065,  81.64 ,
           105.05 , 116.406, 127.199,  98.192, 127.352, 120.688,  80.076,
            75.641,  93.901, 120.579,  98.554,  87.987, 131.045, 105.738,
            53.588, 106.343, 110.401, 104.512, 108.994,  98.654,  73.632,
            92.586,  81.088,  81.345,  74.739, 109.05 , 101.958,  91.037,
            87.013,  99.532, 121.584,  59.916, 107.538,  89.086,  62.308,
            61.086,  81.744, 104.39 , 107.861,  81.22 , 120.34 , 128.46 ,
           107.922,  88.172, 122.488, 115.108, 117.348,  86.871,  43.309,
           142.336,  67.782,  99.285, 147.615, 106.612, 118.985,  69.952,
            64.447,  89.346, 121.815,  93.075,  84.107, 103.959, 121.639,
            71.101,  75.789,  84.227, 121.893, 104.696, 142.643, 118.729,
            99.298, 125.302, 104.23 ,  85.902, 113.599,  86.073,  94.192,
           126.556,  97.974,  83.937,  90.713, 120.436,  88.949,  92.263,
            89.794, 103.679,  92.29 ,  67.963,  82.256,  81.344, 124.866,
           116.253, 111.745,  89.893,  83.684,  89.85 ,  78.962, 149.944,
            55.094, 111.28 ,  74.309,  97.913,  80.24 ,  76.447,  77.196,
           135.1  ,  97.34 ,  84.686, 111.116, 100.207, 114.401,  63.515,
           106.072, 115.454,  66.768, 108.964, 133.924,  99.703, 116.428,
           113.411,  85.85 , 100.795,  68.66 ,  90.974, 105.314, 114.462,
           100.492, 114.4  ,  77.942,  97.966, 100.386, 136.992,  95.717,
            90.02 , 100.427,  81.618, 103.855,  92.699,  64.173,  98.828,
            93.649,  67.352,  98.657, 129.787, 110.426, 112.239,  73.17 ,
           109.538, 102.969, 110.581, 108.453,  72.804,  99.172,  84.843,
            98.998,  82.052, 126.249,  82.821,  82.021, 101.492,  78.458,
            91.507,  83.401, 128.223, 115.716,  98.851,  92.176, 118.818,
           108.104, 109.961,  99.476,  66.235,  97.751,  89.35 , 112.901,
           120.237,  86.841, 109.368, 134.718,  86.646, 133.638,  82.948,
           100.459,  99.777, 100.23 ,  83.246,  88.176,  86.646, 106.539,
           106.601, 144.519, 127.42 ,  89.803, 106.497, 119.942, 100.612,
            98.607, 101.031, 117.346,  83.034,  93.487, 109.409, 106.229,
           104.792,  92.604, 119.451, 142.677, 108.128,  96.136, 115.115,
            89.217,  85.006, 100.656,  48.344,  76.921,  93.041,  72.932,
            79.347,  91.265,  67.141,  91.879,  89.295, 100.508, 123.084,
           103.45 , 100.421, 101.989, 104.548,  79.665,  97.704, 106.175,
            72.585, 117.313, 121.628,  87.372,  95.173,  82.436, 113.988,
            78.776,  95.55 ,  82.822, 101.019,  64.115, 126.529,  80.708,
           101.198,  95.75 ,  84.758,  82.244, 118.728,  89.487, 105.423,
            83.97 ,  87.056, 109.445, 118.608,  96.494,  71.562, 139.959,
            82.869,  69.168, 151.888,  91.919,  70.765,  86.331, 107.351,
           103.806,  82.965, 136.454,  89.568,  76.306, 119.214, 126.581,
            83.65 ,  71.973, 120.609,  59.054,  75.468, 119.349,  98.893,
            94.721, 107.056,  96.945,  74.026, 125.522, 126.5  , 104.107,
           100.903, 146.792,  94.471,  94.808, 107.29 , 129.426, 131.855,
            94.829, 106.167,  72.438,  93.76 ,  83.194,  79.863, 133.632,
            84.154,  89.368, 107.317, 125.957, 109.622, 155.187,  98.507,
           105.174, 105.512, 128.701, 110.145,  97.675,  81.05 , 104.889,
           128.027,  91.792, 110.579, 104.923, 117.27 ,  83.905, 146.933,
            74.417,  92.689, 118.762, 105.935, 116.6  ,  90.078,  98.504,
           100.245, 131.385, 113.809, 115.933,  86.841, 119.378, 104.512,
           127.783, 140.281,  93.865,  91.874,  82.719,  97.128,  92.359,
           107.19 ,  97.109,  92.768, 121.292,  81.242, 108.662,  91.881,
           114.487, 127.705,  93.938, 108.821, 103.576,  84.012, 104.816,
           105.782, 108.257,  96.032, 101.884,  77.048,  92.838])




```python
# 최대최소 범위값을 반환(범위는 최대값 - 최소값)
# np.ptp(array)
print(np.ptp(x))
print(np.max(x) - np.min(x)) #최대 최소가 왔다갔다하는게 116정도 된다
```

    116.10996337643019
    116.10996337643019
    

#### IQR : 사분위 범위(데이터의 하위 75% - 하위 25%)
- IQR = Q3-Q1
- np.quantile(data,분위) : 사분위수 연산
- Q2 : 중앙값 (np.quantile(x, 0.5)


```python
# 사분위범위 : 이상치 영향을줄이기위해 25%~ 75% 까지
# IQR 이라고도 함(이상치 탐색할 때 사용-box plot에서 수염으로 표시됨)
# 25%에서 75%의 범위가 26정도이다. 직관적이지 못함
np.quantile(x,0.75) - np.quantile(x,0.25)
iqr(x)


```




    26.107






    26.107




```python
# 시각화로 표현
import matplotlib.pyplot as plt


```




    {'whiskers': [<matplotlib.lines.Line2D at 0x1d08c6a9e80>,
      <matplotlib.lines.Line2D at 0x1d08c6bf220>],
     'caps': [<matplotlib.lines.Line2D at 0x1d08c6bf580>,
      <matplotlib.lines.Line2D at 0x1d08c6bf8e0>],
     'boxes': [<matplotlib.lines.Line2D at 0x1d08c6a9b20>],
     'medians': [<matplotlib.lines.Line2D at 0x1d08c6bfc40>],
     'fliers': [<matplotlib.lines.Line2D at 0x1d08c6bffa0>],
     'means': []}




    
![png](output_52_1.png)
    


**df.quantile(q=0.5, axis=0, numeric_only=True, interpolation='linear')**
- q : 분위수 입니다. 소수로 표현합니다. (예 : 75% = 0.75)
- aixs : 분위수의 값을 구할 축입니다.
- numeric_only : 수(소수)만 대상으로할지 여부입니다. False일 경우 datetime 및 timedelta 데이터의 분위수도 계산됩니다.
- interpolation : 분위수에 값이 없을때 보간하는 방법입니다. 방식은 아래와 같습니다.

    - liner : i + (j - i) x 비율 [분위수 앞, 뒤 수 간격 * 비율]
    - lower : i [분위수 앞, 뒤수 중 작은수]
    - higher : j [분위수 앞, 뒤수 중 큰수]
    - midpoint : (i+j)÷2 [분위수 앞, 뒤수의 중간값]
    - nearest : i or j [분위수 앞, 뒤수중 분위수에 가까운 수]


```python
# 사분위수
scores
scores.sort()
scores
```




    array([42, 69, 56, 41, 57, 48, 65, 49, 65, 58], dtype=int64)






    array([41, 42, 48, 49, 56, 57, 58, 65, 65, 69], dtype=int64)



- 분위수 위치는 0을 시작으로 하고 오사 오입 방식을 사용함
    - 오사오입(round-to-nearest-even) (파이썬의 특징)
        - 반올림에서 5 미만의 숫자는 내림, 5 초과의 숫자는 올림
        - 5의 앞자리가 홀수인 경우에는 올림을, 짝수인 경우에는 내림


```python
# 오사오입 예제
 # 5의 앞자리가 0(짝수)이므로 내림
round(0.5)
 # 5의 앞자리가 1(홀수)이므로 올림
round(1.5)
 # 5의 앞자리가 2(짝수)이므로 내림
round(2.5)
 # 5의 앞자리가 7(홀수)이므로 올림
round(7.5)
```




    0






    2






    2






    8




```python
scores
```




    array([41, 42, 48, 49, 56, 57, 58, 65, 65, 69], dtype=int64)




```python
# 오사오입이 올림일 때는 값, 값-1
# 오사오입이 내림일 때는 값  값+1

# 올림 내림이 발생하지 않음
np.quantile(scores, q=0.00, interpolation='linear')
```

    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\1625004179.py:5: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.00, interpolation='linear')
    




    41.000




```python
# 오사오입이 내림일 때는 값  값+1
np.quantile(scores, q=0.25, interpolation='linear')
# scores의 개수는 10개
# 위치 2.5 : 2와 3
# i + (j - i) x 비율 
48+(49-48)*0.25
```

    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\3964510783.py:2: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.25, interpolation='linear')
    




    48.250






    48.250




```python
# 오사오입이 올림일 때는 값, 값-1
# array([41, 42, 48, 49, 56, 57, 58, 65, 65, 69]
np.quantile(scores, q=0.75, interpolation='linear')
# 50%가 넘어가면 
# 위치 7.5 => 8
# 7과 8
58+(65-58)*0.75
```

    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\74201385.py:3: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.75, interpolation='linear')
    




    63.250






    63.250




```python
np.quantile(scores, q=0.25, interpolation='lower')
np.quantile(scores, q=0.25, interpolation='higher')
np.quantile(scores, q=0.75, interpolation='lower')
np.quantile(scores, q=0.75, interpolation='higher')
        
```

    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\2605855798.py:1: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.25, interpolation='lower')
    




    48



    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\2605855798.py:2: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.25, interpolation='higher')
    




    49



    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\2605855798.py:3: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.75, interpolation='lower')
    




    58



    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\2605855798.py:4: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.75, interpolation='higher')
    




    65




```python
np.quantile(scores, q=0.25, interpolation='midpoint')
(48+49)/2
np.quantile(scores, q=0.75, interpolation='midpoint')
(58+65)/2
```

    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\182059468.py:1: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.25, interpolation='midpoint')
    




    48.500






    48.500



    C:\Users\PC\AppData\Local\Temp\ipykernel_10524\182059468.py:3: DeprecationWarning: the `interpolation=` argument to quantile was renamed to `method=`, which has additional options.
    Users of the modes 'nearest', 'lower', 'higher', or 'midpoint' are encouraged to review the method they used. (Deprecated NumPy 1.22)
      np.quantile(scores, q=0.75, interpolation='midpoint')
    




    61.500






    61.500


