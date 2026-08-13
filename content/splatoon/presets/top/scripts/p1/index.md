+++
title = "フェーズ1 スクリプト — 絶オメガ検証戦"
description = "絶オメガ検証戦 フェーズ1 スクリプト"
nav = "splatoon"
eyebrow = "script · phase 1"
page_title = "フェーズ1 オメガ"
lede = "サークルプログラム / パントクラトル"
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "[6.4] 絶オメガ検証戦", href = "../../" },
  { label = "フェーズ1", href = "" },
]
+++

## P1 サークルプログラム

デバフと優先度をもとにどの塔を踏むか、テザーを取ってどの方角に行くかがガイドされます。ブラスターの範囲も表示されます。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/Program%20Loop%20Priority.cs
```

#### コンフィグ: LilyDoll (HTDH)

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@Program_Loop_Priority","ConfigurationName":"絶オメガ_LilyDoll","Configuration":"Gw8IACwLzEPSd8DXDP8lB4HQ2s8r4yBwyKGd9fMYgxBrEJGuvqXwZNZcynaiC9lLURI9sQSAbGDpCp1ym/PjT00sYVvdWrN3HWMT3/3OpUukoAEqoBTzrQrqlRpxZfz6XaDh+rVbP8Jp7Il0CKIpYVjnHjN77kB50kdJRPntyyHPCKa0CyOOGdID9lIeHCsQ/AsrIjt6tXgU8HTEPCt99ErWyLs8DnxU6jSssretMu7/XutmTSl4dN19XH/78/71p4M80zVvlp/qtS2rK1pkF4xgfXywUsi4STi9JZhivvqtP3ZuShL9go3s+Z/tnxi8YrfLnp4z2wdoROAgdzwHk90z9/76YLJ+rZevXn9qe7RT541qa2blxHNwT6AGOaNPX2K9lLRTVY0CP52hx2w3NgT9AI6JBa0ZNfWIHphQZzkLt6iOgE2aKRcDuGkANCDk/71J6QESdhANZIn0EKKBImEXYik3mBCDTSorOrwzND/AeDSXDg==","Overrides":null}
```

## P1 パントクラトル AOE描画

直線頭割りとAOEの範囲が表示されます。このスクリプトでは優先度によるグループ分けは行われないので注意が必要です。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/Pantokrator.cs
```

#### コンフィグ: 任意

AOEの見た目を変更するのみのため導入は任意です。デフォルトでも問題ありません。

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@Pantokrator","ConfigurationName":"絶オメガ_LilyDoll","Configuration":"G98BYKwOeHNXKDqBOz5aRHjny5QKe++1+5sgIn06t9TJjB0Yc7NabQbVZsBqNsjRFduczY7bYmgnobe1wDMNouC3N3x9oAeUhzpZ+BeycDMbSfK8Qf3O2jfSoyp7o0UVBCzaQsHhaV5n7CdIu5fayCsFCgBwCuLqxSLoAwsNbWxHTfYFEJ+d8HlJBg==","Overrides":"Gzo5IKyLN4ZEz14R2eJUaFGKyOj5KMaZvlGymL3X7m+J9LnJTP39DhRUy9sf6WzaM2xJVyV15bYI11KBCPeSOiBD5TZXZWh+ufZOJZE0dYRCVpl72aQArIGEup/dlK4AKBSR19UO0HjehjN0KgTxcE3ZXlq3V6xEOFQbwZK9d0Gc1EkWK7VV5X1QT0Qg7cLGQeh/UAhdL4qMehr+vrvyKpZZfYzAKxmU2Nbh7gGvQ+7r7f9lQtRpjq5H4O30ME2nVpkoDVFeo7DoHasE0yms0tnTl7O8Z6Vc2nTKn+ii0DYuZKb/Wvu3HeK7Lgqd6Wy3r79z0PISDlRbZttdNXk7GKJ5+XVWKIqnHaBsSsAmCYmfOKyhjSqbP4d7clHozTMQPFuBuGbDQ2HalBW/KU1INYLlgRqCLLCvKCNBILeExRjOR/W2CUgZdHPWc3SBPlAoAKBnHBPy1ktLe1RkITe79g1LdkiPSdkf7xvo9aZUhJtSkXYOUT9eGryHa4XPZz+9VqvdqS/khxpLKkjiLhdFBSvU2MkTlLgLp/YTBI+Mol0vfIyaTsipuKFhF4Axhro7OcGcLdc/3zXEdna/sm87qgWPOaApp0ig0RWALOsiWz07HHM5gbEnNUaKsrXszGm2OWvig+a0ZyIlCGaTRupDH0xUWQc9QEoo8jPgHi5OZh4z75Z/B50FmEFHeJZrfHnwrMKscit1B51lmJ4DxXTQpkwqImxD+ewCIWqpzJEQQ41BiGQmMEOO2izWlG2rNrgkp/29siSiproIm0+qok4gLg0swbmciavWvDjWICGSi0wnGevUL9otpZYb54oCf4xbs7zLsixXZa6+j/jlewkQ5jO2tJkVy8GAgRB6YFEHdPmpHXysNDqKNSCsKCxNSwoAxhrNKEoznWJFCUtgilYmCMxs62IIbAUjJkcgVbUDFXjk4iirLAz1GF671bEjY9Rw2b+WHdF5BqZ9k1VTrlKiSTmPRmqkz0REJgu/15apE2YjjrVO7KX48InwRUnaARdAilIwBTukARmA9kg+hI7wBd351n3GOURZyAz51NolqEmxQmp+Y8psT5Jfn3BMq1ffItGhyeGPdgUA6lyss5aaWGVVWtHoYDQIcgsaw+/XXkd1XS2VLJtlnyujWzQZgKWQ93drd+my+sIRaW0/+QcAzNSw8WVJWDOZuhjbBdoKpnE5/y4FAI1jnyFp/FjuuxWUtsozKQ0="}
```

## P1 パントクラトル 優先度処理

優先度に基づき北または南のグループ分け、パントクラトル中の頭割りまたはAOE処理、波動砲の散開がガイドされます。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/P1_Pantokrator_Priority.cs
```

#### コンフィグ: LilyDoll (HTDH) - ポジション別

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P1_Pantokrator_Priority","ConfigurationName":"絶オメガ_LilyDoll_MT","Configuration":"GzsEAJwHdqxj6AbfM7RRKuy91+5vg4h09bXlAT34Lk7a2+so4G4wkAb5n6f3GQNaxJeOsYXKGdYrlisI+VZ10wjV16upVhjuCRtU3YBEXdAGbSaOjR7wmyjpSmgwNzNpEENfFCHLPLFLtdLSkghCZM+mncKbuRPiKPKsC3kW4W6w+v/uW/EIuB5gwBPxIBhsuE7gXScaZoUd5QzcBGQFnIMc0/SPl/O6f3/qLKoMxgchrc0pVkfwu5sVDg==","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P1_Pantokrator_Priority","ConfigurationName":"絶オメガ_LilyDoll_ST","Configuration":"GzsEAJwHdqxj6AbfM7RRKuy91+5vg4h09bXlAT34Lk7a2+so4G4wkAb5n6f3GQNaxJeOsYXKGdYrlisI+VZ10wjV16upVhjuCRtU3YBEXdAGbSaOjR7wmyjpSmgwNzNpEENfFCHLPLFLtdLSkghCZM+mncKbuRPiKPKsC3kW4W6w+v/uW/EIuB5gwBPxIBhsuE7gXScaZoUd5QzcBGQFnIMc0/SPl/O6f3/qLKoMxgchrc0pVkfwu5sVDg==","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P1_Pantokrator_Priority","ConfigurationName":"絶オメガ_LilyDoll_H1","Configuration":"GzwEAJwHtg1rj75wd5ZiyaKc23tPhd3fBhHp6mvLA3rw7jlpjV5HAXeDgTT/8/Q+Y0CL+NIxtlA5w3rFcgUh36qbmoLt28vYOhjuCTtU74BEXdAGbRTHRi/4TZTUEhroZiYNYuiLImSbJ3bpUTpaEkGI7Nm2U3ijOyGOIs++kGcRaoM1/3e/ikfA9QCDfCIeCQYLrifwrRMNs8KOykIlICvgHOSYpn+8nDfz51dnUWcwPsimtaVZHUE9XuE=","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P1_Pantokrator_Priority","ConfigurationName":"絶オメガ_LilyDoll_H2","Configuration":"GzwEAJwHdqxj6AbfM7RRKuy91+5vg4h09bXlAT34Lk7a2+so4G4wkAb5n6f3GQNaxJeOsYXKGdYrlisI+Vbd1BRs317G1sFwT9ihugGJuqAN2kwcG73gN1HSldBgbmbSIIa+KEK2eWKXGqWjJRGEyJ5tO4U3cyfEUeRZF/IsQm2w5v/uV/EIuB5gwCfiQTDYcJ3At040zAo7ylmoBGQFnIMc0/SPl/O6f//qLOoMxgchrc1pVkdQj1c4","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P1_Pantokrator_Priority","ConfigurationName":"絶オメガ_LilyDoll_D1","Configuration":"GzwEABypUx975C0V9t5r9xfKvIACvnMcaTOVaKnAncKD5KFc//P0PmNAi/jSMbZQOcN6xXIFId+qm5qC7dvL2DoY7gk7VDcDEnVBG7QpcWygF/yWlJSEBrmZSYMY+qII2eaJPdmj5GhJBCGyZ7adwpvcCXEUee4DeRahNljzf8+v4tHgegODeCIeAQYdrgfwrRMNs8IOrbtQCcgKOI/JMZX+8TK/qr9+dRZ1BuNDMmjtus3qCOrxah4=","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P1_Pantokrator_Priority","ConfigurationName":"絶オメガ_LilyDoll_D2","Configuration":"GzwEAJwHtg1lj31o2nXIhqwM23tPhd1fqNUBHfjOcUDpUwKB9hDXMTIzW6w6nbewRoO4n1K6ULhVjCj9WXSbC6y3y1kG4TU6Gt8JWNQFbVDjxNGAL/gtKTYJZQ6bJw2i7jMi+DdPtMnNZ2lOBMGwd+YyhS+HE+IopnhDnsVQGxb9fxdb0QCiAwKdiEYgIEQPknJmtgjrXDtQCdgioG/J0bb+cfDM/HnqzFAGYr8dtLj2szq0elzLAQ==","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P1_Pantokrator_Priority","ConfigurationName":"絶オメガ_LilyDoll_D3","Configuration":"GzwEABypUx975C0V9t5r9xfKvIACvnMcaTNTiJYK3Ck8SB7K9T9P7zMGtIgvHWMLlTOsVyxXEPKtuqkp2L69jK2D4Z6wQ3UzIFEXtEGbEscGesFvSUlJaJCbmTSIoS+KkG2e2JM9So6WRBAie2bbKbzJnRBHkec+kGcRaoM1//f8Kh4NrjcwiCfiEWDQ4XoA3zrRMCvs0LoLlYCsgPOYHFPpHy/zq/rrV2dRZzA+JIPWrtusjqAer+YB","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.The_Omega_Protocol@P1_Pantokrator_Priority","ConfigurationName":"絶オメガ_LilyDoll_D4","Configuration":"GzwEACyLtwV4dAIu3ekVCy+MlQp777X72yAiXX07RmZmC6hyQANfSnqaSd86LA1dK2zu8vTewhoN4uwYQ6icYb1iuYKQt9o2u8BamzzL4HE6ftDchkRdXBu0gWOjD/yGkjahgcxNmhO1L4oQbZ7YeZSOFkROiOzZ9lN4IycXRwHzc3kW8Nrgzf+9q3CA0AGCXoQjIBChByKNY17Y0S5eCcALODc5pukfL0ffX51FncH4ALR2m9Wh6vEaBw==","Overrides":null}
```

## P1 パントクラトル タンク無敵タイミングアナウンス

無敵を押すまでのカウントダウンが頭上に表示されます。タンク以外は導入不要です。

#### URL

```
https://raw.githubusercontent.com/PunishXIV/Splatoon/refs/heads/main/SplatoonScripts/Duties/Endwalker/The%20Omega%20Protocol/Pantokrator%20invincible%20Reminder.cs
```
