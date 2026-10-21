+++
title = "[7.5] 絶妖星乱舞 — Splatoon Presets"
description = "絶妖星乱舞 レイアウト / スクリプト"
nav = "splatoon"
eyebrow = "dawntrail · dmad"
page_title = "[7.5] 絶妖星乱舞"
breadcrumbs = [
  { label = "Splatoon Presets", href = "../../" },
  { label = "[7.5] 絶妖星乱舞", href = "" },
]
og_image = "https://exatrines.github.io/assets/splatoon/dmad/og.png"

[[changelog]]
date = "2026/09/28"
title = "P1 KB Support Line / P5 Forsaken Support 追加"
body = """
- （新規）Dmad P1 - KB Support Line
- （新規）Dmad P5 - Forsaken Support

追加だけしたい方はこちらから。

```
~Lv2~{"Name":"Dmad P1 - KB Support Line","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"ElementsL":[{"Name":"trap remaining 5s","type":1,"refActorPlaceholder":["<2>","<3>","<4>","<5>","<6>","<7>","<8>","<1>"],"refActorRequireBuff":true,"refActorBuffId":[5078],"refActorUseBuffTime":true,"refActorBuffTimeMax":5.0,"refActorComparisonType":5,"Conditional":true,"Nodraw":true},{"Name":"Horizontal Support Line","type":2,"refX":85.0,"refY":100.0,"offX":115.0,"offY":100.0,"radius":0.0,"color":3355508732,"fillIntensity":0.5,"thicc":6.0},{"Name":"Vertical Support Line","type":2,"Enabled":false,"refX":100.0,"refY":85.0,"offX":100.0,"offY":115.0,"radius":0.0,"color":3355508732,"fillIntensity":0.5,"thicc":6.0}]}
~Lv2~{"Name":"Dmad P5 - Forsaken Support","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"Scenes":[9],"DCond":5,"UseTriggers":true,"Triggers":[{"Type":2,"Duration":60.0,"Match":">47925"}],"ElementsL":[{"Name":"Center Circle","refX":100.0,"refY":100.0,"radius":8.0,"color":3355508735,"fillIntensity":0.5,"thicc":10.0},{"Name":"Border","refX":100.0,"refY":100.0,"radius":11.0,"color":3355508735,"Filled":false,"fillIntensity":0.17,"thicc":10.0},{"Name":"Self Position","type":1,"color":3355508480,"fillIntensity":1.0,"thicc":5.0,"refActorType":1},{"Name":"","type":1,"radius":8.0,"castAnimation":1,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47927],"refActorComparisonType":6},{"Name":"","type":1,"radius":8.0,"fillIntensity":0.5,"castAnimation":1,"pulseSize":0.35,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47928],"refActorComparisonType":6}],"BlacklistedProjectorActions":[47927,47928]}
```
"""

[[changelog]]
date = "2026/07/07"
title = "P5 エクサフレアレイアウト差し替え"
body = """
P5 エクサフレアの特定のパターンで不具合があったためレイアウトを差し替えています。

- （削除）Dmad P5 Exaflares 1
- （削除）Dmad P5 Exaflares 2
- （削除）Dmad P5 Exaflares 3
- （削除）Dmad P5 Exaflares 4
- （削除）Dmad P5 Exaflares 5
- （削除）Dmad P5 Exaflares 6
- （削除）Dmad P5 Exaflares 7
- （削除）Dmad P5 Exaflares
- （新規）Dmad P5 Exaflares 1 v2
- （新規）Dmad P5 Exaflares 2 v2
- （新規）Dmad P5 Exaflares 3 v2
- （新規）Dmad P5 Exaflares 4 v2
- （新規）Dmad P5 Exaflares 5 v2
- （新規）Dmad P5 Exaflares 6 v2
- （新規）Dmad P5 Exaflares 7 v2
- （新規）Dmad P5 Exaflares v2

追加だけしたい方はこちらから。

```
~Lv2~{"Name":"Dmad P5 - Exaflares 1 v2","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"DCond":5,"UseTriggers":true,"Freezing":true,"FreezeFor":4.7,"IntervalBetweenFreezes":0.6,"FreezeDisplayDelay":2.7,"Triggers":[{"Type":2,"Duration":0.5,"Match":">47932)","MatchDelay":0.5}],"ElementsL":[{"Name":"+1","type":1,"offY":7.071,"radius":6.0,"fillIntensity":0.5,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMin":0.3,"refActorCastTimeMax":0.8,"refActorComparisonType":6,"includeRotation":true}]}
~Lv2~{"Name":"Dmad P5 - Exaflares 2 v2","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"DCond":5,"UseTriggers":true,"Freezing":true,"FreezeFor":5.2,"IntervalBetweenFreezes":0.6,"FreezeDisplayDelay":2.7,"Triggers":[{"Type":2,"Duration":0.5,"Match":">47932)","MatchDelay":0.5}],"ElementsL":[{"Name":"+2","type":1,"offY":14.142,"radius":6.0,"fillIntensity":0.5,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMin":0.3,"refActorCastTimeMax":0.8,"refActorComparisonType":6,"includeRotation":true}]}
~Lv2~{"Name":"Dmad P5 - Exaflares 3 v2","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"DCond":5,"UseTriggers":true,"Freezing":true,"FreezeFor":5.7,"IntervalBetweenFreezes":0.6,"FreezeDisplayDelay":2.7,"Triggers":[{"Type":2,"Duration":0.5,"Match":">47932)","MatchDelay":0.5}],"ElementsL":[{"Name":"+3","type":1,"offY":21.213,"radius":6.0,"fillIntensity":0.5,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMin":0.3,"refActorCastTimeMax":0.8,"refActorComparisonType":6,"includeRotation":true}]}
~Lv2~{"Name":"Dmad P5 - Exaflares 4 v2","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"DCond":5,"UseTriggers":true,"Freezing":true,"FreezeFor":6.2,"IntervalBetweenFreezes":0.6,"FreezeDisplayDelay":2.7,"Triggers":[{"Type":2,"Duration":0.5,"Match":">47932)","MatchDelay":0.5}],"ElementsL":[{"Name":"+4","type":1,"offY":28.284,"radius":6.0,"fillIntensity":0.5,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMin":0.3,"refActorCastTimeMax":0.8,"refActorComparisonType":6,"includeRotation":true}]}
~Lv2~{"Name":"Dmad P5 - Exaflares 5 v2","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"DCond":5,"UseTriggers":true,"Freezing":true,"FreezeFor":6.7,"IntervalBetweenFreezes":0.6,"FreezeDisplayDelay":2.7,"Triggers":[{"Type":2,"Duration":0.5,"Match":">47932)","MatchDelay":0.5}],"ElementsL":[{"Name":"+5","type":1,"offY":35.355,"radius":6.0,"fillIntensity":0.5,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMin":0.3,"refActorCastTimeMax":0.8,"refActorComparisonType":6,"includeRotation":true}]}
~Lv2~{"Name":"Dmad P5 - Exaflares 6 v2","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"DCond":5,"UseTriggers":true,"Freezing":true,"FreezeFor":7.2,"IntervalBetweenFreezes":0.6,"FreezeDisplayDelay":2.7,"Triggers":[{"Type":2,"Duration":0.5,"Match":">47932)","MatchDelay":0.5}],"ElementsL":[{"Name":"+6","type":1,"offY":42.426,"radius":6.0,"fillIntensity":0.5,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMin":0.3,"refActorCastTimeMax":0.8,"refActorComparisonType":6,"includeRotation":true}]}
~Lv2~{"Name":"Dmad P5 - Exaflares 7 v2","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"DCond":5,"UseTriggers":true,"Freezing":true,"FreezeFor":7.7,"IntervalBetweenFreezes":0.6,"FreezeDisplayDelay":2.7,"Triggers":[{"Type":2,"Duration":0.5,"Match":">47932)","MatchDelay":0.5}],"ElementsL":[{"Name":"+7","type":1,"offY":49.497,"radius":6.0,"fillIntensity":0.5,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMin":0.3,"refActorCastTimeMax":0.8,"refActorComparisonType":6,"includeRotation":true}]}
~Lv2~{"Name":"Dmad P5 - Exaflares v2","Group":"絶妖星乱舞 - NXIV & mirage(translate)","ZoneLockH":[1363],"FreezeDisplayDelay":3.2,"ElementsL":[{"Name":"+1","type":1,"offY":7.071,"radius":6.0,"color":3355506687,"fillIntensity":0.3,"castAnimation":3,"animationColor":838861055,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMax":3.2,"refActorComparisonType":6,"includeRotation":true},{"Name":"+2","type":1,"offY":14.142,"radius":6.0,"color":3355506687,"fillIntensity":0.3,"castAnimation":3,"animationColor":838861055,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMax":3.2,"refActorComparisonType":6,"includeRotation":true},{"Name":"+3","type":1,"offY":21.213,"radius":6.0,"color":3355506687,"fillIntensity":0.3,"castAnimation":3,"animationColor":838861055,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMax":3.2,"refActorComparisonType":6,"includeRotation":true},{"Name":"+4","type":1,"offY":28.284,"radius":6.0,"color":3355506687,"fillIntensity":0.3,"castAnimation":3,"animationColor":838861055,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMax":3.2,"refActorComparisonType":6,"includeRotation":true},{"Name":"+5","type":1,"offY":35.355,"radius":6.0,"color":3355506687,"fillIntensity":0.3,"castAnimation":3,"animationColor":838861055,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMax":3.2,"refActorComparisonType":6,"includeRotation":true},{"Name":"+6","type":1,"offY":42.426,"radius":6.0,"color":3355506687,"fillIntensity":0.3,"castAnimation":3,"animationColor":838861055,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMax":3.2,"refActorComparisonType":6,"includeRotation":true},{"Name":"+7","type":1,"offY":49.497,"radius":6.0,"color":3355506687,"fillIntensity":0.3,"castAnimation":3,"animationColor":838861055,"refActorNPCNameID":7131,"refActorRequireCast":true,"refActorCastId":[47932],"refActorUseCastTime":true,"refActorCastTimeMax":3.2,"refActorComparisonType":6,"includeRotation":true}]}
```
"""

[[changelog]]
date = "2026/06/30"
title = "P4 デバフリマインダーの設定画面変更"
body = """
P4 デバフリマインダーの設定画面が変更されたので翻訳を追記しました。
"""

[[changelog]]
date = "2026/06/29"
title = "初版公開"
body = """
初版公開。
"""

[[sections]]
heading = "レイアウト"
items = [
  { title = "レイアウト一覧", meta = "基本レイアウトと処理法別レイアウト", href = "layout/" },
]

[[sections]]
heading = "スクリプト"
items = [
  { title = "フェーズ1", meta = "ケフカ", href = "scripts/p1/" },
  { title = "フェーズ2", meta = "ゴッドケフカ", href = "scripts/p2/" },
  { title = "フェーズ3", meta = "エクスデス＆カオス", href = "scripts/p3/" },
  { title = "フェーズ4", meta = "おちょくりソウル", href = "scripts/p4/" },
  { title = "フェーズ5", meta = "アルティメットケフカ", href = "scripts/p5/" },
]
+++
