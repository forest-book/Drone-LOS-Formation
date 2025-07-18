import csv
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict
import datetime

class DataLogger:
    """
    シミュレーション中のデータを収集し、CSVファイルに保存するクラス。
    """
    def __init__(self, follower_ids: List[int]):
        """
        Args:
            follower_ids (List[int]): 追跡対象のフォロワーのIDリスト。
        """
        self.follower_ids = follower_ids
        # ヘッダーを準備: Step, Follower1_Error, Follower2_Error, ...
        headers = ['Step'] + [f'Follower_{fid}_Error' for fid in self.follower_ids]
        self.data = [headers]

    def add_entry(self, step: int, errors: Dict[int, float]):
        """
        特定のステップにおける全フォロワーの誤差データを追加する。

        Args:
            step (int): 現在のシミュレーションステップ。
            errors (Dict[int, float]): フォロワーIDをキー、追従誤差を値とする辞書。
        """
        row = [step] + [errors.get(fid, None) for fid in self.follower_ids]
        self.data.append(row)

    def save_to_csv(self, filename: str = 'tracking_errors.csv'):
        """
        収集したデータをCSVファイルに保存する。

        Args:
            filename (str): 保存するCSVファイル名。
        """
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)
        print(f"Data successfully saved to {filename}")

class Plotter:
    """
    CSVファイルからデータを読み込み、グラフを描画するクラス。
    """
    @staticmethod
    def plot_from_csv(filename: str = 'tracking_errors.csv'):
        """
        指定されたCSVファイルから追従誤差のグラフをプロットする。

        Args:
            filename (str): 読み込むCSVファイル名。
        """
        try:
            df = pd.read_csv(filename)
            plt.figure(figsize=(12, 8))
            
            for column in df.columns:
                if 'Error' in column:
                    plt.plot(df['Step'], df[column], label=column)
            
            plt.xlabel('Step')
            plt.ylabel('Tracking Error (cm)')
            plt.title('Follower Tracking Error over Time')
            plt.legend()
            plt.grid(True)
            plt.savefig('tracking_error_graph.png')
            print("Graph successfully saved to tracking_error_graph.png")
            plt.show()

        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except Exception as e:
            print(f"An error occurred while plotting: {e}")