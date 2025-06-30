from pathlib import Path

current_folder = Path(__file__).resolve().parent
project_root = current_folder.parent  # Go one level up
auth = project_root / "resources" / "car_prices.csv"
