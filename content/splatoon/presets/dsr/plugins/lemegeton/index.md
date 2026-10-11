+++
title = "Lemegeton — 絶竜詩戦争"
description = "絶竜詩戦争向け Lemegeton の設定"
nav = "splatoon"
eyebrow = "other"
page_title = "Lemegeton"
toc = true
toc_label = "目次"
breadcrumbs = [
  { label = "Splatoon Presets", href = "../../../../" },
  { label = "[6.1] 絶竜詩戦争", href = "../../" },
  { label = "Lemegeton", href = "" },
]
+++

ギミックに応じてオートマーカーを付与するプラグインです。オートマーキングはパーティメンバーに「ツールバレ」するリスクがあるので注意が必要です。アップデート直後は、プラグインが使えるようになるまで時間がかかることが多いです。

## 導入

1. `/xlsettings` コマンド → 試験的機能 → カスタムプラグインリポジトリに以下の URL を追加
2. `/xlplugins` コマンド → Lemegeton をインストール

```
https://raw.githubusercontent.com/paissaheavyindustries/Dalamud-Repo/main/repo.json
```

## 設定

- クイックトグル > オートマーカーを許可する → オン
- オートマーカーの設定 > 戦闘終了後、全てのマークを除去する → オン
- オートマーカーの設定 > ワイプ後、全てのマークを除去する → オン
- オートマーカーの設定 > ソフトオートマーカーを使う → オフ

![](/assets/splatoon/endwalker/lemegeton_settings.png)

## ギミック別設定

コンテンツ > 絶レイド > 絶竜詩戦争で、必要なギミックだけ有効にしてください。

![](/assets/splatoon/dsr/lemegeton_contents.png)

### チェインライトニングオートマーカー

![](/assets/splatoon/dsr/lemegeton_p5_chain.png)

### 邪念の炎オートマーカー

[DSR Toolbox](../dsrtoolbox/) の Flames Automarker と競合するので、オートマーカーを使う場合は必ずどちらか一方だけを有効にしてください。

![](/assets/splatoon/dsr/lemegeton_p6_flames.png)
