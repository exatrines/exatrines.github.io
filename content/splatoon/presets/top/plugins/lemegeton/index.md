+++
title = "Lemegeton — 絶オメガ検証戦"
description = "絶オメガ検証戦向け Lemegeton の設定"
nav = "splatoon"
eyebrow = "other"
page_title = "Lemegeton"
lede = "ギミックに応じてオートマーカーを付与します。"
toc = true
toc_label = "目次"
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "[6.4] 絶オメガ検証戦", href = "../../" },
  { label = "Lemegeton", href = "" },
]
+++

ギミックに応じてオートマーカーを付与するプラグインです。オートマーキングはパーティメンバーに「ツールバレ」するリスクがあるので注意が必要です。また、アップデート直後はプラグインが使用できるようになるまでに時間がかかることが多いです。

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

コンテンツ > 絶レイド > 絶オメガ検証戦で、必要なギミックだけ有効にしてください。

![](/assets/splatoon/endwalker/lemegeton_contents.png)

### コードデュナミス・デルタ

![](/assets/splatoon/endwalker/lemegeton_p5_delta.png)

### コードデュナミス・シグマ（オメガと同じ）

![](/assets/splatoon/endwalker/lemegeton_p5_sigma_bind.png)

### コードデュナミス・シグマ（LilyDoll設定）

![](/assets/splatoon/endwalker/lemegeton_p5_sigma_attack.png)

### コードデュナミス・オメガ

![](/assets/splatoon/endwalker/lemegeton_p5_omega.png)
