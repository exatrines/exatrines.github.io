+++
title = "Goetia — 絶竜詩戦争"
description = "絶竜詩戦争向け Goetia の設定"
nav = "splatoon"
eyebrow = "other"
page_title = "Goetia"
toc = true
toc_label = "目次"
breadcrumbs = [
  { label = "Splatoon Presets", href = "../../../../" },
  { label = "[6.1] 絶竜詩戦争", href = "../../" },
  { label = "Goetia", href = "" },
]
+++

ギミックに応じてマーカー用のホットバーをハイライトする、手動マーカー補助プラグインです。ホットバーの対応付けが必要なので、詳細は [Goetia](/dalamud-plugins/goetia/) を参照してください。

## 導入

1. `/xlsettings` コマンド → 試験的機能 → カスタムプラグインリポジトリに以下の URL を追加
2. `/xlplugins` コマンド → Goetia をインストール

```
https://raw.githubusercontent.com/exatrines/DalamudPlugins/refs/heads/main/pluginmaster.json
```

## ギミック別設定

### 至天の陣：風槍

- `サンダーウィング` の対象2名に `Stop`

![](/assets/splatoon/dsr/goetia_wrath.png)

### 邪念の炎

- `復讐の炎` の対象4名に `Attack`
- `道連れの炎` の対象2名に `Bind`
- 残りの2名に `Stop`

![](/assets/splatoon/dsr/goetia_wroth.png)
