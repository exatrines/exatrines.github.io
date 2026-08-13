+++
title = "フェーズ5 スクリプト — 絶妖星乱舞"
description = "絶妖星乱舞 フェーズ5 スクリプト"
nav = "splatoon"
eyebrow = "script · phase 5"
page_title = "フェーズ5 アルテマケフカ"
lede = "狂気のオーケストラ / フラッド / スリースターズ ..."
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "[7.5] 絶妖星乱舞", href = "../../" },
  { label = "フェーズ5", href = "" },
]
+++

## P5 フラッド

フラッドがガイドされます。中央で避けるようにガイドされます。散開が表示されてしまうので、エレメント設定で無効化する必要があります。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Dawntrail/Dancing%20Mad/P5_Chaotic_Flood_Guide.cs
```

#### コンフィグ: エレメント設定

![](/assets/splatoon/dmad/20260629200323.png)

散開表示を無効化するためのエレメント設定。

```
{"Elements":{"Spread":{"Name":"","type":0,"Enabled":false,"refX":110.0,"refY":106.0,"refZ":0.0,"offX":0.0,"offY":0.0,"offZ":0.0,"radius":1.0,"color":3355508503,"Filled":true,"fillIntensity":0.3,"overlayBGColor":3221225472,"overlayTextColor":4294967295,"overlayVOffset":1.5,"overlayFScale":2.0,"overlayPlaceholders":false,"thicc":6.0,"overlayText":"Spread","refActorName":"","refActorTargetingYou":0,"refActorNamePlateIconID":0,"refActorComparisonAnd":false,"refActorRequireCast":false,"refActorCastReverse":false,"refActorUseCastTime":false,"refActorCastTimeMin":0.0,"refActorCastTimeMax":0.0,"refActorUseOvercast":false,"refTargetYou":false,"refActorRequireBuff":false,"refActorRequireAllBuffs":false,"refActorRequireBuffsInvert":false,"refActorUseBuffTime":false,"refActorUseBuffParam":false,"refActorBuffTimeMin":0.0,"refActorBuffTimeMax":0.0,"refActorObjectLife":false,"TargetAlteration":0,"refActorComparisonType":0,"refActorType":0,"includeHitbox":false,"includeOwnHitbox":false,"includeRotation":false,"onlyTargetable":false,"onlyUnTargetable":false,"onlyVisible":false,"tether":true,"ExtraTetherLength":0.0,"LineEndA":0,"LineEndB":0,"AdditionalRotation":0.0,"LineAddHitboxLengthX":false,"LineAddHitboxLengthY":false,"LineAddHitboxLengthZ":false,"LineAddHitboxLengthXA":false,"LineAddHitboxLengthYA":false,"LineAddHitboxLengthZA":false,"LineAddPlayerHitboxLengthX":false,"LineAddPlayerHitboxLengthY":false,"LineAddPlayerHitboxLengthZ":false,"LineAddPlayerHitboxLengthXA":false,"LineAddPlayerHitboxLengthYA":false,"LineAddPlayerHitboxLengthZA":false,"FaceMe":false,"LimitDistance":false,"LimitDistanceInvert":false,"DistanceSourceX":0.0,"DistanceSourceY":0.0,"DistanceSourceZ":0.0,"DistanceMin":0.0,"DistanceMax":0.0,"UseDistanceSourcePlaceholder":false,"LimitRotation":false,"refActorTether":false,"refActorTetherTimeMin":0.0,"refActorTetherTimeMax":0.0,"refActorTetherParam1":null,"refActorTetherParam2":null,"refActorTetherParam3":null,"refActorIsTetherSource":null,"refActorIsTetherInvert":false,"refActorIsTetherLive":false,"refActorUseTransformation":false,"mechanicType":0,"refMark":false,"refMarkID":0,"faceplayer":"","FaceInvert":false,"FillStep":0.5,"LegacyFill":false,"RenderEngineKind":0,"Conditional":false,"RotationOverride":false,"RotationOverrideFaceMode":false,"IsCapturing":false,"Nodraw":true,"UseHitboxRadius":false,"MapEffectInvert":false,"MapEffectAnd":false,"UseCastRotation":false,"UseCastPosition":false,"UseCastTarget":false,"IsDead":null,"Enumeration":0,"AnimationInverted":false,"UsePlaceholderAsRefPosition":false,"UsePlaceholderAsOffPosition":false,"PairingMode":0}},"Layouts":{}}
```

## P5 スリースターズ

スリースターズがガイドされます。デバフ持ちはその属性から時計回りに見た時の最初の塔へガイドされ、無職は余った塔へガイドされます。設定は不要です。

#### URL

```
https://github.com/PunishXIV/Splatoon/raw/refs/heads/main/SplatoonScripts/Duties/Dawntrail/Dancing%20Mad/P5_Celestriad.cs
```

#### コンフィグ: 既定

```
設定不要
```
