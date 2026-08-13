+++
title = "フェーズ5 スクリプト — 絶オメガ検証戦"
description = "絶オメガ検証戦 フェーズ5 スクリプト"
nav = "splatoon"
eyebrow = "script · phase 5"
page_title = "フェーズ5 デュナミス"
lede = "コード：＊＊＊ミ＊ デルタ / シグマ / オメガ"
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "[6.4] 絶オメガ検証戦", href = "../../" },
  { label = "フェーズ5", href = "" },
]
+++

## P5 デルタ

紐処理、アーム誘導、バッシュ誘導、検知、最後のハロワまで全ての行動がガイドされます。頭上にヒントも表示されますが、テンポの速いギミックなのであくまで補助として使用することをお勧めします。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/P5_Dynamis_Delta_Guid.cs
```

#### コンフィグ: LilyDoll

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P5_Dynamis_Delta_Guide","ConfigurationName":"絶オメガ_LilyDoll","Configuration":"G3AAACwKbBuh/up2JBp6IKoVdPre1e6vbvN6xfPU/hg5KDwKC2qYGCEj1cDilAP2VhRYGPAB73a4x9hVtizKkZ1F65no6KMakqUKNaTz2B7J5x/HV1Cnb8UR7mS0RqgI","Overrides":null}
```

## P5 シグマ

整列、波動砲の散開、踏む塔がガイドされます。塔マクロ押さない式を採用する場合は押さない式用のコンフィグをインポートしてください。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/Dynamis%20Sigma.cs
```

#### コンフィグ: LilyDoll (塔Wingman式)

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@Dynamis_Sigma","ConfigurationName":"絶オメガ_LilyDoll","Configuration":"Gz4DABwHbqwza9RoKC+lTsN7suz+Wrrpa9TnhGq3ZjpQvCLIuRzp35/T9QOd6e6rxCq0sADn3ebWsLaL8BHUUFdi9DkWmNyfxQT1OZUT+lhWzdr/Htxn0iAS1GpOpJ2LUjSOEq+rzJQq5WzyooCBK7CQg4IEUtDXDK5UGlPLNp4LIylsKTnGrcc41MwG/0rrp3rXyU3/TVpMqoaKKocO7+Hx0bByIAnT7LxMOfpQ4q+Fn9KcqZytkI9A/KTcJ0eDCkivRaCqNrbRHmaWghZwquqQsskItslC6ptHFKk0V3o7G/Vi5G1m/c7XnVDKWw/5wRcoaY4KlTQmIg==","Overrides":null}
```

#### コンフィグ: マクロ押さない式用 波動砲散開のみ

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@Dynamis_Sigma","ConfigurationName":"絶オメガ_シグママクロ押さない式","Configuration":"GzkDABwHbqwza9RoKC+lTsN7suz+Wrrpa9TnhGq3ZjpQvCLIuRzp4E2tD5r5VF7v4Pug+T1Ulm02VmqEj6DEzRqLPofBovuzGKE+p3JCGcvELP/vwXomDSJCLTdE2jkveWMqsrvKVEkgZ5tXUmgUDxc/FTiM1+nGIRimzja7WVE9o7SVHOPWYwjKZhV6JXdRv9ekpv8mOR3VQEUCn4O7f3wIrAZIimY2X5AcfiT+lzNPycEIXMvnIwc/8nvlsFsJ0MvJp7qNXbSHpkKQc011A2IgGZJr0om8dIiBSg6ltHNRL6peM+t7vu4Eo91m0Ae+BOPlMGGqYiIC","Overrides":null}
```

## P5 シグマ 塔踏み（マクロ押さない式）

押さない式でどの塔に入るべきかガイドされます。このスクリプトでは波動砲の散開はガイドされないので、前述のスクリプトと組み合わせて使用してください。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/P5_Dynamis_Sigma_Relative_Tower_Finder.cs
```

#### コンフィグ: 既定

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P5_Dynamis_Sigma_Relative_Tower_Finder","ConfigurationName":"絶オメガ_シグママクロ押さない式","Configuration":null,"Overrides":null}
```

## P5 シグマ ハロワ

シグマのハロワ散開がガイドされます。マーキングルールによってコンフィグを導入してください。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/P5_Dynamis_Sigma_Hello_World.cs
```

#### コンフィグ: LilyDoll (北 Attack123 - 南 その他)

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P5_Dynamis_Sigma_Hello_World","ConfigurationName":"絶オメガ_LilyDoll","Configuration":"G48EYJwHto0sPzVvKFg/SLUCSN+72v21588BTWT887a2fLgC7sqwsTKjthUKUiKpakgMkVRO9g68e4m8WTKJhPhqbg3Rh3pY31tzbUIfsXK/ibNmbHyia9V/ePhzmaGKETpM2iCXtkKHybrJf2KPAx2Ki3OyhADd9NTt7yNGX5O3Or0/q4ntziON8i9pXwklMDjpbwmpeA5eRi+C0qs143tPQElv4Tn7qHCtbNGsG78DfQwVETuSXCl3CEwufRiTynjuTutY8eGqua9YgHB46mJ6U2xPVPmRNg0Ft54Iw+rsocYhxSnYqheueipQNKx+Dp7IKag7LCz0ncz2Sy4ZpkOBtzGAnWUohmnXuzBklkDeDpACpUE=","Overrides":null}
```

#### コンフィグ: アーム誘導Bind式 (北 Bind12, Attack1 - 南 その他)

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P5_Dynamis_Sigma_Hello_World","ConfigurationName":"絶オメガ_シグマハロワアーム誘導バインド式","Configuration":"G48EYJwJdqyVoXJlD6ZSoe+9dn8tnRNqwi/VfO3Q4cdPaKYMGyvzec71fCU40gTaG45kf1XeghV3RxU4wEvbloQ9Vkfb90SbBvtES/ab2Ge58cmu1fzh4c/FUj/gBANOyJLL8DUDjsGOru0egM0wz8myFLDpqdzfRw2vabSsvD+rSd+dpzXwL5lYS62wuuhvPpl4DpGYPU5qpdaM7+0ApLyMgn1UDav6ollOfgf6GKpW7rQiSUuDanKZw3Bq53N3msEshvPpvmIBGfAIMR5ge4HxIx1tGriNZBrm3h2DQ5ojsN2uGarnEk0bXp9DpHIKrh0Wltl3mrZSctlpOpRE2xwmdtYBVpowujEg2wDZDpO0kHgC","Overrides":null}
```

## P5 オメガ 激せま安置

オメガの激せま安置がガイドされます。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/P5_Dynamis_Omega_Safe_Guide.cs
```

## P5 オメガ ハロワ

オメガのハロワ散開がガイドされます。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/P5_Dynamis_Omega_Hello_World.cs
```

#### コンフィグ: LilyDoll (前半 検知Bind その他Attack, 後半 ブラスターBind その他Attack)

前半は最低でもBind2名とAttack2名が、後半はAttack2名がマーキングされている必要があります。

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P5_Dynamis_Omega_Hello_World","ConfigurationName":"絶オメガ_LilyDoll","Configuration":"GxgCQJwHtg0rn8obWtk8TbUCSN+72v2FcFshWYrZ4E40GA02TYY6+OfDw5gZVpZnufOXV+63W+htPZVFLwEl0Ja9FGAciAb/tywbYn4plluub/solih3NGR4XZjpG1nsU4vdmiBGbvs0w80AI8uxa59kgkK8T/7oEnMtBQAAAkIVjTAF04ev/l/HL7erHgc9RBvLQWWzQA==","Overrides":null}
```
