from .endpoints import SWAP_POSITION_DUAL
from .requester import send_request

def set_dual_side_position(dual_side=True):
    params = {
        "dualSidePosition": str(dual_side).lower(),
        "timestamp": "1702731530753"  # 需動態生成
    }
    return send_request("POST", SWAP_POSITION_DUAL, params)
