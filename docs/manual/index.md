# SIMPLE_REGITRATIONデータセットテンプレート

## 概要
データの保存・蓄積に特化した、基本的なテンプレートです。データの構造化・可視化を行いません。

- DT0001: 試料メタあり＋自由記述メタ(key1～10)あり
- DT0002: 試料メタあり＋自由記述メタなし
- DT0003: 試料メタなし＋自由記述メタ(key1～10)あり
- DT0004: 試料メタなし＋自由記述メタなし

## データセットテンプレートシートについて

　メタデータ定義(metadata-def.json)、送状定義(invoice.schema.json)、カタログ定義(catalog.schema.json)をエクセル形式のシートから生成することができるツールを以下に用意してあります。

[RDE/データセットテンプレート生成、確認ツール](https://github.com/nims-mdpf/RDE_datasettemplate-schemafile-make-tool)

　上記のツールで利用可能な本データセットテンプレート用のデータセットテンプレートシートは以下の通りです。

- [templates/DT0001用](./RDEDatasetTemplateSheet_RDE_SIMPLE_REGISTRATION_dt0001.xlsx)
- [templates/DT0002用](./RDEDatasetTemplateSheet_RDE_SIMPLE_REGISTRATION_dt0002.xlsx)
- [templates/DT0003用](./RDEDatasetTemplateSheet_RDE_SIMPLE_REGISTRATION_dt0003.xlsx)
- [templates/DT0004用](./RDEDatasetTemplateSheet_RDE_SIMPLE_REGISTRATION_dt0004.xlsx)
