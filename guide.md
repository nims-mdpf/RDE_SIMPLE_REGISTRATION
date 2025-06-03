# RDE シンプル登録データセットテンプレート

# 概要
データの保存・蓄積に特化した、基本的なテンプレートです。データの構造化・可視化を行いません。

- DT0001: 試料メタあり＋自由記述メタ(key1～10)あり
- DT0002: 試料メタあり＋自由記述メタなし
- DT0003: 試料メタなし＋自由記述メタ(key1～10)あり
- DT0004: 試料メタなし＋自由記述メタなし

## 基本情報

### コンテナ情報

- 【コンテナ名】nims_simple_registration

### テンプレート情報
- DT0001:
    - 【データセットテンプレートID】NIMS_DT0001_SIMPLE_REGISTRATION_v1.0
    - 【データセットテンプレート名日本語】シンプル登録データセットテンプレート(試料メタあり＋自由記述メタあり)
    - 【データセットテンプレート名英語】simple registration dataset-template(sample + free-text)
    - 【データセットテンプレートの説明】入力されたファイルをそのまま登録するだけのデータセットテンプレートです。構造化処理を行わないのでデータファイルの種類は問いません。メタデータは試料メタ＋自由記述(key1～10)メタです。
- DT0002:
    - 【データセットテンプレートID】NIMS_DT0002_SIMPLE_REGISTRATION_v1.0
    - 【データセットテンプレート名日本語】シンプル登録データセットテンプレート(試料メタあり)
    - 【データセットテンプレート名英語】simple registration dataset-template(sample)
    - 【データセットテンプレートの説明】入力されたファイルをそのまま登録するだけのデータセットテンプレートです。構造化処理を行わないのでデータファイルの種類は問いません。メタデータは試料メタのみです。
- DT0003:
    - 【データセットテンプレートID】NIMS_DT0003_SIMPLE_REGISTRATION_v1.0
    - 【データセットテンプレート名日本語】シンプル登録データセットテンプレート(自由記述メタあり)
    - 【データセットテンプレート名英語】simple registration dataset-template(free-text)
    - 【データセットテンプレートの説明】入力されたファイルをそのまま登録するだけのデータセットテンプレートです。構造化処理を行わないのでデータファイルの種類は問いません。メタデータは自由記述(key1～10)メタのみです。
- DT0004:
    - 【データセットテンプレートID】NIMS_DT0004_SIMPLE_REGISTRATION_v1.0
    - 【データセットテンプレート名日本語】シンプル登録データセットテンプレート(メタなし)
    - 【データセットテンプレート名英語】simple registration dataset-template(no-meta)
    - 【データセットテンプレートの説明】入力されたファイルをそのまま登録するだけのデータセットテンプレートです。構造化処理を行わないのでデータファイルの種類は問いません。メタデータの記述欄はありません。
- 【バージョン】1.0
- 【データセット種別】その他
- 【データ構造化】あり (システム上「あり」を選択)
- 【取り扱い事業】NIMS研究および共同研究プロジェクト (PROGRAM)
- 【装置名】(なし)

## データ登録方法
登録したいファイルを登録ファイル欄にドラッグアンドドロップする。

複数の画像ファイルを登録する場合は、代表画像ファイルを指定することが可能。
- 送り状の「代表画像ファイル名」欄に代表画像に指定したい画像ファイル名を入力。
- 指定しない場合は、先頭(アスキーコード順)の画像ファイルが選択される。

登録する画像ファイルのフォーマットについて
- jpeg, png, gifは、そのまま(代表)画像ファイルフォルダに格納される。
- pdfは、1ページ目をpngに変換したファイルが、(代表)画像ファイルフォルダに格納される。
- それ以外(tif, svg等)は、pngに変換したファイルが、(代表)画像ファイルフォルダに格納される。

複数ファイルを登録する際、それぞれのファイルに、送り状に違う値(Value)を設定したい場合は、エクセルインボイスを使用する。

## 構成

### レポジトリ構成

```
simple_registration
├── LICENSE
├── README.md
├── container
│   ├── Dockerfile
│   ├── data (入出力(下記参照))
│   ├── main.py
│   ├── modules (ソースコード)
│   ├── pip.conf
│   ├── pyproject.toml
│   ├── requirements-test.txt
│   ├── requirements.txt
│   ├── tests (テストコード(DT0001のみ))
│   └── tox.ini
├── gitlab-ci.yml
├── inputdata (入力ファイル)
│   └── examples (サンプル群)
│       ├── dt0001 (試料メタあり＋自由記述メタありサンプル)
│       │   ├── excelinvoice_file (エクセルインボイス(ファイル))
│       │   ├── excelinvoice_folder (エクセルインボイス(ファイル))
│       │   ├── invoice_multidatatile (マルチデータタイル対応)
│       │   ├── invoice_no-image (インボイス(画像なし))
│       │   └── invoice_with-image (インボイス(画像あり))
│       ├── dt0002 (試料メタあり＋自由記述メタなしサンプル)
│       │   ├── excelinvoice_file (エクセルインボイス(ファイル))
│       │   ├── excelinvoice_folder (エクセルインボイス(ファイル))
│       │   ├── invoice_multidatatile (マルチデータタイル対応)
│       │   ├── invoice_no-image (インボイス(画像なし))
│       │   └── invoice_with-image (インボイス(画像あり))
│       ├── dt0003 (試料メタなし＋自由記述メタありサンプル)
│       │   ├── excelinvoice_file (エクセルインボイス(ファイル))
│       │   ├── excelinvoice_folder (エクセルインボイス(ファイル))
│       │   ├── invoice_multidatatile (マルチデータタイル対応)
│       │   ├── invoice_no-image (インボイス(画像なし))
│       │   └── invoice_with-image (インボイス(画像あり))
│       └── dt0004 (試料メタなし＋自由記述メタなしサンプル)
│           ├── excelinvoice_file (エクセルインボイス(ファイル))
│           ├── excelinvoice_folder (エクセルインボイス(ファイル))
│           ├── invoice_multidatatile (マルチデータタイル対応)
│           ├── invoice_no-image (インボイス(画像なし))
│           └── invoice_with-image (インボイス(画像あり))
└── templates (テンプレート群)
    ├── dt0001 (試料メタあり＋自由記述メタありテンプレートファイル)
    ├── dt0002 (試料メタあり＋自由記述メタなしテンプレートファイル)
    ├── dt0003 (試料メタなし＋自由記述メタありテンプレートファイル)
    └── dt0004 (試料メタなし＋自由記述メタなしテンプレートファイル)
```

### 動作環境
- Python: 3.11
- RDEToolKit: 1.0.0

### 動作環境ファイル入出力

```
container/data
├── inputdata
│   ├── 登録ファイル欄にドラッグアンドドロップした任意のファイル
│   └──  :
├── invoice
│   └── invoice.json (送り状)
├── main_image
│   └── 代表画像ファイル (画像ファイルがなければ作成されません)
├── meta
│   └── metadata.json (中身は空)
├── other_image
│   ├── (代表画像以外の)画像ファイル
│   └──  :
├── raw
│   ├── inputdataからコピーした入力ファイル
│   └──  :
├── structured
│   └── invoice_org.json (送り状原本)
├── tasksupport
│   ├── default_value.csv
│   ├── invoice.schema.json
│   ├── metadata-def.json
│   └── rdeconfig.yaml
├── temp
└── thumbnail
    └──  (サムネイル用)代表画像ファイル
```

### release note
* 2024-07-31 初版作成
