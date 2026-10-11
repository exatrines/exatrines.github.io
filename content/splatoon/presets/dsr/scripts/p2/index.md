+++
title = "フェーズ2 スクリプト — 絶竜詩戦争"
description = "絶竜詩戦争 フェーズ2 スクリプト"
nav = "splatoon"
eyebrow = "script · phase 2"
page_title = "フェーズ2 騎神トールダン"
breadcrumbs = [
  { label = "Splatoon Presets", href = "../../../../" },
  { label = "[6.1] 絶竜詩戦争", href = "../../" },
  { label = "フェーズ2", href = "" },
]
+++

## P2 蒼天の陣：聖杖 前半

自分とペアの頭上マーカーをもとに、ゼフィランの後ろか対角のどちらに向かうかと、ブライトスフィアの回避までガイドされます。

自動で視線を回避する設定は不安定なので、オフにしています。[DSR Toolbox](../../plugins/dsrtoolbox/) を使用して回避することをお勧めします。

#### URL

```
https://github.com/PunishXIV/Splatoon/raw/main/SplatoonScripts/Duties/Endwalker/Dragonsong's%20Reprise/P2%20Sanctity%20Of%20The%20Ward%20First.cs
```

#### コンフィグ: ポジション別

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_First","ConfigurationName":"絶竜詩戦争_LilyDoll_MT","Configuration":"G/wBIKyKx/lHJ+DSnVqoOIhcK8Tsvavd3wYR6epbMFuWt5A+dPusFMVmMxSTBOMLmw9HsegYdPMD0BDvGmMRtuk/DGiipm5KQUXw8BmJMl32lR79sREUdR4/pvBtqxYwAhLBmWlI+sIThax6Ui2PMCQWIm/Xnv4OKcMzpylZWZ8YPAuyFzBHFEMtsjN5wDdlb27f4Ixh8KzSdHf4dgnIWbFKf96sGgpovAzYmu9t+h9hQb+shEsMwYzQU9Rpnq9qdz7BuEIK5C+VCAV2ANamf2yC1y5u7W8dcQ==","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_First","ConfigurationName":"絶竜詩戦争_LilyDoll_ST","Configuration":"G/wBICwK7FgYSivU7pZgOXGpsPeeW7u/DSLS1dfe24ckdLusFMVmMxSTBOMVf/svHMWiY9DND0BDvPvGGIRt+sKAJmra1jgwCXr4iU1Lm79xj37cGZR0fWEuwWrvHSATEsHM1Ge96YkCqJ5U0xEGY1GHRu1odygZrp1NAWU5Y/AsyOzAf0TRJ0Ijkwd8Vbba+g3OAIOzStM14O0S3EOrQ/n9qldfZOViIJZ8d837FZT0yzRc4SESk6mnqNOs/Krd+ATDRqmUt1UiFNgBWavzYxfeevH7vGiNAw==","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_First","ConfigurationName":"絶竜詩戦争_LilyDoll_H1","Configuration":"G/wBIKwKeHM4pbTC7L0lWE5cKuy91+5vg4h09S2YLctbSB+6fVaKYrMZikmC8YXNh6NYdCy3jRAqMd6xZ8NhYRb9FA0cCY2GZDBW1U0pqAg7fEaiTJftKj36YyMUdR4/pvBpXy2QAhLBmcmTvvBElVVPqnmEIbEQrVUP+jqmjGJ2s7HS7xg8g/IE5ojCa6uVyQMuZTT0CZ4YBs+qEN3h2xXwX5E6/V5meQGNhwHr+WVj+VUL+mUJl/BgKfQUddryVe3gFZwrpED+UolQYDdgSf/YBK+93NrfdnI=","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_First","ConfigurationName":"絶竜詩戦争_LilyDoll_H2","Configuration":"G/wBIKwKeHM4pbTC7L0lWE5cKuy91+5vg4h09a2YLctbSB+6fVaKYrMZikmC8YXNh6NYdCy3jRAqMd6xZ8NhYRb9FA0cCY2GZDBW1U0pqAg7fEaiTJftKj36YyMUdR4/pvBpXy2QAhLBmcmTvvBElVVPqnmEIbEQrVUP+jqmjGJ2s7HS7xg8g/IE5ojCa6uVyQMuZTT0CZ4YBs+qEN3h2xXwY5E6/V5meQGNhwHr+WVj+VUL+mUJl/BgKfQUddryVe3gFZwrpED+UolQYDdgSf/YBK+93NrfdnI=","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_First","ConfigurationName":"絶竜詩戦争_LilyDoll_D1","Configuration":"G/wBIKwKeHMOpWklw3uMMWtQu1TYe6/d3wYR6erbMFszMS1vIX3o9lkpis1mKCYJxhc2H45i0THy9AKgQfxPxxiE3ZQWCzRRq25KQUXw8BmJMl32lR79sRGKOo8fU/i29xZQAYngzNQnfeGJAlY9qaZHGBILkbVrR3+HluGa0xSsLE8MnglZC5gjir4stDN5wFdla67f4Ixh8KwS0jp8u8TtrGp/Xq3qC2i8DNiS7256H0FBv8yES/TBVOgp6jTLV7Ubn2BYIQXyl0qEAjsAa9U/NsFrF7f2t5Yc","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_First","ConfigurationName":"絶竜詩戦争_LilyDoll_D2","Configuration":"G/wBIKyKx/lHJ+DSnVqoNBK5VoDZe1e7vw0i0tU3t2ZiLG8hfej2WSmKzWYoJgnGFzYfjmLRMfL0AqBB/E/HGITdlBYLNFGrbkpBRPDQYyTKdNlXevTHRlDUefyYwre9t4AKSARnpj7pC08UsOpJNT3CkFiIrF07+ju0DNecpmBleWLwTMhawBxR9LHQzuQBX5WtsX6DM4bBs0pIdfh2iXjnqmt/Xq3qC6i8DNiS725470FBv8yES/SFqdBT1GmWr2o3PsGwQgrkL5UIBXYA1qp9bIJXL27tby1x","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_First","ConfigurationName":"絶竜詩戦争_LilyDoll_D3","Configuration":"G/wBIKwKeHMOpWklw3uMMWtQu1TYe6/d3wYR6eqbMDNblreQPnT7rBTFZjMUkwTjC5sPR7HoGHl6AdAg/qdjDMJuSosFmqhVN6WgInj4jESZLvtKj/7YCEWdx48pfNt7C6iARHBm6pO+8EQBq55U0yMMiYXI2rWjv0PLcM1pClaWJwbPhKwFzBFF3xbamTzgq7I1129wxjB4VgnpHb5d4hZV7c+rVX0BjZcBW/LdTe8jKOiXmXCJPpgKPUWdZvmqduMTDCukQP5SiVBgB2Ct+scmeO3i1v7WkgM=","Overrides":null}
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_First","ConfigurationName":"絶竜詩戦争_LilyDoll_D4","Configuration":"G/wBICyLtwV4dAIu3VELlZ5ELhX23mv3t0FEuvrm1kyM5S2kD90+K0Wx2QzFJMH4wubDUSw6BSNj5OkFQIP4n44xCLspLRZoolbdlIKK4OEzEmW67Cs9+mMjFHUeP6bwbe8toAISwZmpT/rCEwWselJNjzAkFiJr147+Di3DNacpWFmeGDwTshYwRxR9LLQzecBXZWuu3+CMYfCsElIdvl3iNqv259WqvoDGy4At+e6m9xEU9MtMuERfmAo9RZ1m+ap24xMMK6RA/lKJUGAHYK36xyZ47eLW/taSAw==","Overrides":null}
```

## P2 蒼天の陣：聖杖 後半

コメットロールをもとに、現在いる位置からどの塔を踏むべきかがガイドされます。コメット担当の場合は、コメットの捨て位置も表示されます。

自動でアームズレングスを使用する設定をオンにしているので、注意してください。

#### URL

```
https://github.com/PunishXIV/Splatoon/raw/main/SplatoonScripts/Duties/Endwalker/Dragonsong's%20Reprise/P2%20Sanctity%20Of%20The%20Ward%20Second.cs
```

#### コンフィグ

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Endwalker.Dragonsong_s_Reprise@P2_Sanctity_Of_The_Ward_Second","ConfigurationName":"絶竜詩戦争_LilyDoll","Configuration":"G3QBwCwO7DYva0BSm6l7ZVMHJ6XC3nvq7P5a3lK9Xf5C0VVRgPaTzIaNTZIwMTbV4GJ5y7/J4fczNeAIJhTTbIJunSyJ1egND3t87ilJfHJ43wHQa7+bRM0QiB/ATCgRKgxVlkoWly8RJSswFa5kxcB7pO3UZawNp7mm+HQfNp3nR5irjZJljrrjMPThjRIVaI9P947c4it8","Overrides":null}
```