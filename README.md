### BingX_Auto_Order
BX makes me money.

### 如何在colab中使用
import sys \
sys.path.append('/content/drive/MyDrive/你的資料夾/bingx_api/') \
from demo import set_dual_side_position \
print(set_dual_side_position())

### 
這樣設計不只可維護性高、未來新API只需增修 endpoints 或 demo，非常適合 Colab 跑 Python，.py檔案直接丟 Google Drive，用 sys.path 加入路徑即可 import，不需 pip install，完全沒問題。
