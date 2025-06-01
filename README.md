### BingX_Auto_Order
BX makes me money.

### 如何在colab中使用
import sys \
sys.path.append('/content/drive/MyDrive/你的資料夾/bingx_api/') \
from demo import set_dual_side_position \
print(set_dual_side_position())

### 
這樣設計不只可維護性高、未來新API只需增修 endpoints 或 demo，非常適合 Colab 跑 Python，.py檔案直接丟 Google Drive，用 sys.path 加入路徑即可 import，不需 pip install，完全沒問題。

###
BingX Python API Module

1. 把全部 .py 檔放進同一資料夾（bingx_api/）。
2. config.py 填入你的 API_KEY/SECRET_KEY。
3. Colab 掛載 Google Drive，!unzip bingx_api.zip -d /content/
4. import sys; sys.path.append('/content/bingx_api')
5. from demo import set_dual_side_position, get_commission_rate
6. print(set_dual_side_position(True))
   print(get_commission_rate())

###
打包 zip 步驟（在你本機）
建立好所有檔案（內容照上面），放進 bingx_api 資料夾

用滑鼠右鍵 → 壓縮成 zip 檔

上傳到 Google Drive

依前述 Colab 範例掛載、解壓縮、import 即可
