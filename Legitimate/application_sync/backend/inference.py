"""Production Inference Engine Synchronized with Promoted Research Model.

Autonomous Publication Engineering System - Current Promoted Model Engine.
Loads xgb_coldstart_rich_promoted.json (24 features) and executes launch-blind
predictions with bit-for-bit parity to the research pipeline.
"""

from pathlib import Path
import sys

LEGIT_DIR = Path(__file__).resolve().parents[2]
if str(LEGIT_DIR) not in sys.path:
    sys.path.insert(0, str(LEGIT_DIR))

from test_application_parity import SynchronizedAppPredictor

def get_engine():
    return SynchronizedAppPredictor()

if __name__ == "__main__":
    engine = get_engine()
    test_sample = {
        "product_uid": "demo_sample",
        "name": "SoundCore Motion Boom Plus",
        "brand": "Anker",
        "price": 149.99,
        "category": "bluetooth_speakers",
        "specs": {
            "features": ["80W output", "IP67 waterproof", "20 hours playtime", "Bluetooth 5.3"]
        }
    }
    res = engine.predict(test_sample, "bluetooth_speakers")
    print("Inference Demo Output:")
    print(res)
