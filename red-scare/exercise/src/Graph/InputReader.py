from pathlib import Path
from typing import List

class InputReader:
    @staticmethod
    def Read() -> List[Path]:
        data_root = Path(__file__).resolve().parents[3] / "data"

        if not data_root.exists():
            raise FileNotFoundError(f"Data folder not found: {data_root}")
        if not data_root.is_dir():
            raise NotADirectoryError(f"Data path is not a directory: {data_root}")

        files = [p for p in data_root.glob("*.txt") if p.is_file()]
        files.sort(key=lambda p: str(p).lower())
        return files

    """
    if __name__ == "__main__":
        # Quick test when run directly
        try:
            for p in collect_data_txt_paths():
                print(p)
        except Exception as e:
            print(e)
    """