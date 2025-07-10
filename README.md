<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <!-- 制御スクリプト -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=plastic">
  <!-- シミュレータ環境 -->
  <img src="https://img.shields.io/badge/-CoppeliaSim-232F3E.svg?style=plastic">
</p>

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [環境](#環境)
3. [ディレクトリ構成](#ディレクトリ構成)
4. [開発環境構築](#開発環境構築)
5. [CoppeliaSimのインストールと起動](#CoppeliaSimのインストールと起動)
6. [シミュレーションの実行](#シミュレーションの実行)

<!-- プロジェクト名を記載 -->

# Drone-LOS-Formation

LOS誘導に基づくクワッドロータ群のフォーメーション制御

<!-- プロジェクトについて -->

## プロジェクトについて

関西大学2024年3月期の卒論「クワッドロータ群のチョークポイント通過に関する研究（塩田氏著）」について，<br>
「line-of-sight(LOS)に基づくリーダ・フォロワ制御」の内容をMATLABからPythonでの実装に変換した．<br>
動作環境はWindows 11を想定．


<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

<!-- 言語、パッケージ，シミュレータの一覧とバージョンを記載 -->

| 言語・シミュレータ  | バージョン |
| --------------------- | ---------- |
| Python                | 3.13.3     |
| CoppeliaSim           | 4.10.0     |


Pythonパッケージのバージョンは requirements.txt を参照してください

<p align="right">(<a href="#top">トップへ</a>)</p>

## ディレクトリ構成

```
.
├── .venv
├── CoppeliaSim
│   └── Scene
|       └── tuizyuu.ttt
├── main
│   ├── control_strategies.py
│   ├── formations.py
│   ├── main.py
│   ├── simulation.py
│   └── swarm_components.py
├── sandbox
│   └── diagnosis_drone.py
├── thesis
│   └── B2023Shiota.pdf
├── .gitignore
├── README.md
└── requirements.txt
```

<p align="right">(<a href="#top">トップへ</a>)</p>

## 開発環境構築

<!-- 仮想環境の作成方法、パッケージのインストール方法など、開発環境構築に必要な情報を記載 -->

### Python仮想環境の作成と起動

プロジェクトのルートディレクトリにて，ターミナル上で以下のコマンドを実行

```
python -m venv .venv
```

<p>.venvという名前の仮想環境が作成される</p>

### 仮想環境のアクティベーション
ターミナル上で

```
.venv\Scripts\activate
```

を実行．<br>
(.venv) PS E:\Github\Drone-LOS-Formation> <br>
のようにディレクトリパスの前に(.venv)と記述されていたら仮想環境が起動している状態である

### Pythonパッケージのインストール
仮想環境が起動した状態で，ターミナル上で
```
pip install requirements.txt
```
を実行．requirements.txt内に記述されているモジュールがインストールされる．

### インストール済みのPythonモジュール確認
```
pip list
```
をターミナル上で実行すると，インストールされているパッケージの名前とバージョンが一覧で確認できる<br>
requirements.txtの記述と相違なければ問題ない

### 仮想環境の終了
```
deactivate
```
をターミナル上で実行すると，仮想環境から出られる


## CoppeliaSimのインストールと起動
### CoppeliaSimのインストール
<a href="https://www.coppeliarobotics.com/">CoppeliaSim公式サイト</a>からCoppeliaSimのEducation版をダウンロード．<br>
セットアップ用のexeファイルを実行し，インストールを完了させる．

### CoppeliaSimの起動
CoppeliaSimを起動させる．Toolバーから[File] ⇒ [Open Scene ...] から tuizyuu.tttを選択し，シーンを開く．

<p align="right">(<a href="#top">トップへ</a>)</p>

## シミュレーションの実行
### スクリプトの実行
```
cd main 
```

でmainディレクトリに移動し，

```
python main.py
```

を実行すると，シミュレーションがスタートする．5台のクワッドロータがフォーメーションを組みながら目標位置(Cylinder)へと移動する．<br>
ターミナル上で Ctrl + Cキーを押下すると，シミュレーションがストップする．

<p align="right">(<a href="#top">トップへ</a>)</p>
