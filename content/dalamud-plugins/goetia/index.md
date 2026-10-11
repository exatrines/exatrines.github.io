+++
title = "Goetia — Dalamud"
description = "ギミックに応じてマーカー用のホットバーをハイライトする、手動マーカー補助プラグイン。"
nav = "dalamud"
eyebrow = "dalamud · goetia"
page_title = "Goetia"
footer_href = "https://github.com/exatrines/Goetia"
footer_label = "Repo on GitHub"
toc = true
toc_label = "目次"
breadcrumbs = [
  { label = "Dalamud Plugins", href = "../" },
  { label = "Goetia", href = "" },
]
+++

## Goetia とは

![パーティリスト上の Attack / Bind / Stop ハイライト](/assets/goetia/party-highlight-1280x720.png)

Goetia は、手動マーカー付与を補助する Dalamud プラグインです。パーティリスト順（`<1>`–`<8>`）に合わせ、Attack / Bind / Stop のホットバースロットをハイライトします。

Goetia 自体は `/mk` を発行しません。`/mk` マクロは割り当てたホットバーに自分で配置する必要があります。設定でホットバーとスロットを対応づけ、使うモジュールを有効にすれば、戦闘中に対応するスロットがハイライトされます。

## インストール方法

1. `/xlsettings` コマンド → 試験的機能 → カスタムプラグインリポジトリに以下の URL を追加
2. `/xlplugins` コマンド → Goetia をインストール

```
https://raw.githubusercontent.com/exatrines/DalamudPlugins/refs/heads/main/pluginmaster.json
```

## ホットバー設定

`/goetia settings` で Attack / Bind / Stop のホットバーと、`<1>` の基準スロットを対応づけます。3 本のホットバーを割り当て、連続する 8 スロットをパーティリスト順 `<1>`–`<8>` にします。

例: ホットバー 6 / 7 / 8 のスロット 5〜12 が `<1>`〜`<8>`（Attack / Bind / Stop）。

![ホットバー設定](/assets/goetia/goetia-settings-1280x720.png)

## モジュール

`/goetia` でモジュール画面を開き、使うモジュールをオンにします。

![メイン画面](/assets/goetia/goetia-main-1280x720.png)

### TOP（絶オメガ検証戦）

各モジュールと初期設定は以下の通りです。

#### Run Dynamis Delta (コードデュナミス・デルタ)

1. `ハローワールド・ニア/ファー` の対象2名に `Stop`

#### Run Dynamis Sigma (コードデュナミス・シグマ)

1. `ハローワールド・ニア/ファー` の対象2名に `Stop`
2. `デュナミスの高揚` 1スタックの対象（最大2名）に `Bind`
3. 残りの4名に `Attack`

#### Run Dynamis Omega (コードデュナミス・オメガ) 前半

1. `ファーストターゲット` の対象2名に `Stop`
2. `セカンドターゲット` かつ `デュナミスの高揚` 2スタックの対象に `Bind`
3. 手順2と合わせて2名になるように、`デュナミスの高揚` 2スタックの対象に `Bind`
4. 残りの4名に `Attack`

#### Run Dynamis Omega (コードデュナミス・オメガ) 後半

1. `ハローワールド・ニア/ファー` の対象2名に `Stop`
2. `デュナミスの高揚` 3スタックの対象2名に `Bind`
3. 残りの4名に `Attack`

絶オメガのギミック別設定は [Goetia](/splatoon/presets/top/plugins/goetia/) を参照してください。

### DSR（絶竜詩戦争）

各モジュールと初期設定は以下の通りです。

#### Wrath of the Heavens（至天の陣：風槍）

1. `サンダーウィング` の対象2名に `Stop`

#### Wroth Flames（邪念の炎）

1. `復讐の炎` の対象4名に `Attack`
2. `道連れの炎` の対象2名に `Bind`
3. 残りの2名に `Stop`

絶竜詩戦争のギミック別設定は [Goetia](/splatoon/presets/dsr/plugins/goetia/) を参照してください。

## コマンド

- `/goetia` — モジュール画面の表示切替
- `/goetia settings` — プラグイン設定画面の表示切替
