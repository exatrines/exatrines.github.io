+++
title = "[6.4] 絶オメガ検証戦 — Splatoon"
description = "絶オメガ検証戦 レイアウト / スクリプト"
nav = "splatoon"
eyebrow = "endwalker · top"
page_title = "[6.4] 絶オメガ検証戦"
lede = "基本りりどを基準にしたレイアウトとスクリプトです。PriorityEditor（/splatoon p）の設定は必ず行ってください。"
breadcrumbs = [
  { label = "Splatoon", href = "../../" },
  { label = "[6.4] 絶オメガ検証戦", href = "" },
]

[[changelog]]
date = "2026/08/13"
title = "Workspace から移植"
body = "Splatoon Workspace の絶オメガ検証戦ドキュメントを移植しました。"

[[sections]]
heading = "フェーズ"
items = [
  { title = "フェーズ1", meta = "オメガ", href = "p1/" },
  { title = "フェーズ2", meta = "オメガM ＆ オメガF", href = "p2/" },
  { title = "フェーズ3", meta = "ファイナルオメガ", href = "p3/" },
  { title = "フェーズ4", meta = "リブート", href = "p4/" },
  { title = "フェーズ5", meta = "デルタ", href = "p5/delta/" },
  { title = "フェーズ5", meta = "シグマ", href = "p5/sigma/" },
  { title = "フェーズ5", meta = "オメガ", href = "p5/omega/" },
  { title = "フェーズ6", meta = "アルファオメガ", href = "p6/" },
]

[[sections]]
heading = "スクリプト解説"
items = [
  { title = "P1 パントクラトル 優先度処理", meta = "優先度処理", href = "scripts/p1-pantokrator-priority/" },
  { title = "P3 コロッサスブロー", meta = "コロッサスブロー", href = "scripts/p3-transition/" },
  { title = "P5 シグマ 塔マクロ押さない式", meta = "塔ガイド", href = "scripts/p5-sigma-tower/" },
  { title = "P5 シグマ ハロワ", meta = "ハロワ", href = "scripts/p5-sigma-hello-world/" },
  { title = "P5 オメガ 激せま安置ガイド", meta = "激せま安置", href = "scripts/p5-omega-safe/" },
  { title = "P5 オメガ ハロワ", meta = "ハロワ", href = "scripts/p5-omega-hello-world/" },
]

[[sections]]
heading = "その他"
items = [
  { title = "その他", meta = "Lemegeton / Chibi Omega", href = "other/" },
]
+++

絶オメガ検証戦におけるレイアウトとスクリプトのまとめです。ほとんどのスクリプトにおいて優先度設定が必要なため、PriorityEditor ( `/splatoon p` ) の設定は必ず行ってください。

日本で多く採用されている [基本りりど《HTDH/縦2列,南誘導/検知アスト/デルタハムカツ/シグマりょんめ塔wingwan式/最終ぬけまる》](https://jp.finalfantasyxiv.com/lodestone/character/34120564/blog/5178791/) を基準としています。ただし、固定などで採用されているP3検知式波動砲の十字式や、P5シグマの塔マクロ押さない式についても記載しています。

## thanks

このまとめは様々な方の協力があって作成されました。

- [FF14 Splatoon 絶オメガで便利なレイアウトとスクリプトまとめ - 光のツーラー](https://tooleroflight.blog.jp/archives/24065980.html)
- [絶オメガ検証戦 - ungeho blog](https://ungeho.netlify.app/posts/splatoon-top/)

ほか、スクリプト・レイアウト・設定情報を提供いただいた皆様。
