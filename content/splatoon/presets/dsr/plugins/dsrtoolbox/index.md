+++
title = "DSR Toolbox — 絶竜詩戦争"
description = "絶竜詩戦争向け DSR Toolbox の設定"
nav = "splatoon"
eyebrow = "other"
page_title = "DSR Toolbox"
toc = true
toc_label = "目次"
breadcrumbs = [
  { label = "Splatoon Presets", href = "../../../../" },
  { label = "[6.1] 絶竜詩戦争", href = "../../" },
  { label = "DSR Toolbox", href = "" },
]
+++

視線の位置の把握、プレステの紐の確認、オートマーキング、絶竜詩戦争のギミックを補助するプラグインです。必ず Splatoon と併用してください。

## 導入

1. `/xlsettings` コマンド → 試験的機能 → カスタムプラグインリポジトリに以下の URL を追加
2. `/xlplugins` コマンド → **DSR** で検索し、DSR Toolbox をインストール

```
https://github.com/NightmareXIV/MyDalamudPlugins/raw/main/pluginmaster.json
```

## 設定

設定はモジュールごとに分かれています。使うものだけオンにしてください。

### Eye Locator

P2 の聖杖 前半と、P5 の死刻の視線ギミックで有効です。

- トールダンと外周の目に青い線が表示されます。
- 視線が正しいかどうかのバナーが表示されます。正しい方角を向いていれば「Correct!」、間違っていれば「DON'T LOOK」です。Options タブでテストできます。

![](/assets/splatoon/dsr/eye_locator.png)

### Chain Tether

P1 と P5 のプレステギミック時に、線が表示されます。

![](/assets/splatoon/dsr/chain_tether.png)

### Flames Automarker

P6 の邪念の炎で、自動でマーカーを付与します。[Lemegeton](../lemegeton/) と競合するので、オートマーカーを使う場合は必ずどちらか一方だけを有効にしてください。

![](/assets/splatoon/dsr/flames_automarker.png)
