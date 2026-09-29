+++
title = "DSR Toolbox — 絶竜詩戦争"
description = "絶竜詩戦争向け DSR Toolbox の設定"
nav = "splatoon"
eyebrow = "other"
page_title = "DSR Toolbox"
lede = "視線位置の把握や分担マーカーなど、フェーズごとの判断を補助します。"
toc = true
toc_label = "目次"
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "[準備中] [6.1] 絶竜詩戦争", href = "../../" },
  { label = "DSR Toolbox", href = "" },
]
+++

視線位置の把握や、邪念の炎の分担、チェイン相手の確認など、フェーズごとの判断を補助するプラグインです。範囲描画や散開ガイドは Splatoon 側のスクリプトを使います。

## 導入

1. `/xlsettings` コマンド → 試験的機能 → カスタムプラグインリポジトリに以下の URL を追加
2. `/xlplugins` コマンド → **DSR** で検索し、DSR Toolbox をインストール

```
https://github.com/NightmareXIV/MyDalamudPlugins/raw/main/pluginmaster.json
```

NightmareXIV のリポジトリです。

## 設定

設定はフェーズ（機能）ごとに分かれています。使うギミックだけオンにしてください。

## できること

- 邪眼フェーズでの視線位置の把握
- 邪念の炎のオートマーカー（個人 / パーティ）
- チェイン相手へのテザー表示
