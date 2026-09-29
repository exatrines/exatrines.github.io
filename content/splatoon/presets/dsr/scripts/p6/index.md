+++
title = "フェーズ6 スクリプト — 絶竜詩戦争"
description = "絶竜詩戦争 フェーズ6 スクリプト"
nav = "splatoon"
eyebrow = "script · phase 6"
page_title = "フェーズ6 二天竜"
lede = "竜の息吹 / 邪念の炎 / カータライズ"
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "[準備中] [6.1] 絶竜詩戦争", href = "../../" },
  { label = "フェーズ6", href = "" },
]
+++

邪念の炎の分担マーカーは [DSR Toolbox](../../plugins/dsrtoolbox/) 側でも出せます。範囲描画は Splatoon を使います。

## P6 竜の息吹 1回目

エンチャント（火 / 氷）とタンク頭割りをもとに、散開先がガイドされます。優先度設定が必要です。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/Dragonsong's%20Reprise/P6%20Wyrmsbreath%20First.cs
```

#### コンフィグ: 既定

`PriorityEditor`（`/splatoon p`）の設定を行ってください。

```
設定不要
```

## P6 邪念の炎

散開デバフ / 頭割りデバフ / 無職をもとに、安置と散開先がガイドされます。翼と尾のブレス向きも見ます。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/Dragonsong's%20Reprise/P6%20Wroth%20Flames.cs
```

#### コンフィグ: 既定

マクロの散開位置に合わせて設定画面を確認してください。

```
設定不要
```

## P6 カータライズ 危険範囲

沸騰中はニーズヘッグ、氷結中はフレースヴェルグのカータライズ範囲が表示されます。自分が踏んではいけない方だけ出ます。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/DSR_P6_Cauterize_Unsafe.cs
```

#### コンフィグ: 既定

```
設定不要
```

## P6 オートターゲットスイッチャー

二体の HP 差を見てターゲットを切り替えます。アク・アファーやブレスのタイミングに合わせた切替もあります。導入は任意です。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/Dragonsong's%20Reprise/P6%20AutoTargetSwitcher.cs
```

#### コンフィグ: 既定

切替の閾値は設定画面で調整できます。

```
設定不要
```
