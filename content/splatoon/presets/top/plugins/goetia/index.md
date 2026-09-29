+++
title = "Goetia — 絶オメガ検証戦"
description = "絶オメガ検証戦向け Goetia の設定"
nav = "splatoon"
eyebrow = "other"
page_title = "Goetia"
lede = "ギミックに応じてマーカー用のホットバーをハイライトします。"
toc = true
toc_label = "目次"
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "[6.4] 絶オメガ検証戦", href = "../../" },
  { label = "Goetia", href = "" },
]
+++

ギミックに応じてマーカー用のホットバーをハイライトする、手動マーカー補助プラグインです。ホットバーの対応付け設定が必要なので、詳細は [Goetia](/dalamud-plugins/goetia/) を参照してください。

## 導入

1. `/xlsettings` コマンド → 試験的機能 → カスタムプラグインリポジトリに以下の URL を追加
2. `/xlplugins` コマンド → Goetia をインストール

```
https://raw.githubusercontent.com/exatrines/DalamudPlugins/refs/heads/main/pluginmaster.json
```

## ギミック別設定

### コードデュナミス・デルタ

- Near/Far World → Stop

### コードデュナミス・シグマ（オメガと同じ）

- Near/Far World → Stop
- Dynamis ×1 (max 2) → Bind
- Remaining → Attack

### コードデュナミス・シグマ（LilyDoll設定）

- Near/Far World → Stop
- Dynamis ×1 (max 2) → Attack
- Remaining → Attack

### コードデュナミス・オメガ

- Half1: FirstInLine + Near/Far World → Stop
- Half1: Dynamis ×2 (max 2) → Bind
- Half1: Remaining → Attack
- Half2: SecondInLine + Near/Far World → Stop
- Half2: Dynamis ×3 (max 2) → Bind
- Half2: Remaining → Attack
