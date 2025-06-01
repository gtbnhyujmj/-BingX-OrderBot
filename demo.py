# 各類 demo = 功能主體
# 從BingX API文件貼過來的
# 真正的"虛擬信件"的內容擺在這邊

from .endpoints import SWAP_POSITION_DUAL
from .requester import send_request

def set_dual_side_position(dual_side=True):
    params = {
        "dualSidePosition": str(dual_side).lower(),
        "timestamp": "1702731530753"  # 需動態生成
    }
    return send_request("POST", SWAP_POSITION_DUAL, params)
