+++
title = "フェーズN スクリプト — （コンテンツ名）"
description = "（コンテンツ名） フェーズN スクリプト"
nav = "splatoon"
eyebrow = "script · phase N"
page_title = "フェーズN （ボス/系統名）"
lede = "（ギミック名 / ギミック名）"
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "（コンテンツ名）", href = "../../" },
  { label = "フェーズN", href = "" },
]
+++

<!--
  使い方
  - このファイルを scripts/pN/index.md にコピーして編集する
  - content/_templates/ はビルド対象外（dist に出ない）
  - スクリプト名は ##（ページ見出しは frontmatter の h1）
  - 既存の設定画面スクショは「説明の直後」に置く（動作スクショ専用枠は不要）
  - 真の動作スクショを足す場合も、とりあえず説明の後ろでよい
  - 「設定不要」のときは コンフィグ のコードを「設定不要」にする
  - コンフィグが複数あるときは #### コンフィグ: 名前 を並べる
  - スクリプト間に --- は使わない（見出し ## のスタイルで区切る）
-->

## （スクリプト名）

（動作の説明。何がガイドされるか、注意点、誰向けかなどを書く。）

![](/assets/splatoon/（コンテンツ）/（スクリプト）_screenshot.png)

#### URL

```
https://raw.githubusercontent.com/.../ScriptName.cs
```

#### コンフィグ: （プリセット名A）

![](/assets/splatoon/（コンテンツ）/（スクリプト）_config_a.png)

（このコンフィグの説明。どのマクロ／戦略向けか、適用手順、注意など。）

```
{"TargetScriptName":"...","ConfigurationName":"...","Configuration":"...","Overrides":null}
```

#### コンフィグ: （プリセット名B）

![](/assets/splatoon/（コンテンツ）/（スクリプト）_config_b.png)

（別コンフィグの説明。不要ならこの節ごと削除。）

```
{"TargetScriptName":"...","ConfigurationName":"...","Configuration":"...","Overrides":null}
```

## （別スクリプト名）

（説明文）

![](/assets/splatoon/（コンテンツ）/（別スクリプト）_screenshot.png)

#### URL

```
https://raw.githubusercontent.com/.../OtherScript.cs
```

#### コンフィグ: 既定

![](/assets/splatoon/（コンテンツ）/（別スクリプト）_config.png)

（説明。設定不要の場合は下を「設定不要」のみにする。）

```
設定不要
```
