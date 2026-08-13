+++
title = "フェーズ3 スクリプト — 絶妖星乱舞"
description = "絶妖星乱舞 フェーズ3 スクリプト"
nav = "splatoon"
eyebrow = "script · phase 3"
page_title = "フェーズ3 エクスデス ＆ カオス"
lede = "バウル・オブ・アゴニー / リミッターカット / ブラックホール"
breadcrumbs = [
  { label = "Splatoon", href = "../../../../" },
  { label = "[7.5] 絶妖星乱舞", href = "../../" },
  { label = "フェーズ3", href = "" },
]
+++

## P3 バウル・オブ・アゴニー TLB式

TLB式のバウル・オブ・アゴニーが完全にガイドされます。ヤーンとイディルで風デバフの受け方が違うので注意してコンフィグを導入してください。

![](/assets/splatoon/dmad/20260629042502.png)

#### URL

```
https://github.com/PunishXIV/Splatoon/raw/refs/heads/main/SplatoonScripts/Duties/Dawntrail/Dancing%20Mad/P3_Bowels_of_Agony_TLB.cs
```

#### コンフィグ: ヤーン速報（８人受け） 20260629時点

![](/assets/splatoon/dmad/20260629043234.png)

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Dawntrail.Dancing_Mad@P3_Bowels_of_Agony_TLB","ConfigurationName":"絶妖星乱舞_ヤーン速報_20260629","Configuration":"G7wMACwKbKc1tIVz8WNpcF3qqlJ4r91fdU6hLnyIPqdJXpgRl3djSvbaXKocJa7xUw0F0ZknS4POT/dz1cAzzMIR33uLaJDZcHT3lxwtNJMPCMsAkbEdjOxZ9W4W04S6gA1q4FGBODiD8x2E9ZXTiVaFiF6XHw0foPmghDVADwM0F1oq+Hv4hcFIhMQohdLohM7NRrqPVBixNDuNPsEaoQbK5E7YPp6GVQSWSuhyH6C5BLjUMNZPjk7duuQOPER3YLmDyH1E7sBiHMpkGmsxPW1YcQjYBton/Zjk89AK8AOI1KK4QN35pqRN25ee6WK+rHxcIdFdGKANOg/SxbA2TAeoveBmwsbR3QM7UdX29TM9TbeaCNUmmzXpOpkmfLJ04g1RsObgM9qQOaV+r5KjhnpkP5gTIEvc5hTgxzCBxgQ+Ezjb4GgPNRNGMaE3wytBxtYT6Il9GindQxY9yUBqb/JxEBklrmIFzSWONs7Wcqxs8wq83TK/KOZ9Q23ekntxZ1T671XW4EN9yPS/qbT5DLLQPd8dw6Q4HgMbvQdQEw07KPEB","Overrides":null}
```

#### コンフィグ: イディル（ペア受け） 20260629時点

![](/assets/splatoon/dmad/20260629042951.png)

```
{"TargetScriptName":"SplatoonScriptsOfficial.Duties.Dawntrail.Dancing_Mad@P3_Bowels_of_Agony_TLB","ConfigurationName":"絶妖星乱舞_イディル_20260629","Configuration":"G8gMAJyFsbMj3YX5VW/RSKpK4b12f+Fzv4Vk6GN5yO7dH4ghG21iiv/aXKp/lLjGTzUU8Kn9/OUuGgv4DJsDI/7vNcYGycLoxrLWEgosoQAh+j+6Uxnbwe5h5KxZN4utJHUBN2hObmhAPJzBv70hcX3VdMKqgZp1+aF7EOaDIakOhGaA7opLxQcHXkVHRCrwRC6eaNSgW+HwkRVGHM/XCiTYIrQgsKUzMeJjpBoCl8qW9PuBzcXhUiNyTLlrULRLGMBEDCAMWNiwMIAEWmCLOltmfLqw4uDEHaz+A8ZGPg+tjz8BUbAoXtBVHkxerziA2ch0WcW4QhINQb4PPmSGKNb+XiPrL7yZcH40t2EN3exdO7PTNquNpNpGtSa9p9NEnxyeZENUaLnwjDbknAp+r1KihVnQf2ROIFniNqePPw0T2JjAzwSebWG0F7spUTEBZmklKHL5RHYi0nLtLbqYSXnKBMbTQ8oo8R1Xwb7irj6e1uVFOKGVdxh7TuTQUDQ2TUB8abW2vNpRbupfpq2m1mFYyVK3g4lNZFk0DUSKloTmQmFFZv17StWAjM0KveTt/9d9JDbsrNQ2","Overrides":null}
```

## P3 サイコロ

サイコロによる移動先がガイドされます。設定は初期状態で問題ありませんが、以下のように設定すると見やすくなります。

#### URL

```
https://github.com/PunishXIV/Splatoon/raw/refs/heads/main/SplatoonScripts/Duties/Dawntrail/Dancing%20Mad/P3_Limit_Cut.cs
```

#### コンフィグ: マーカー北から時計回りに A2B3C4D1

```
{"TargetScriptName":"SplaSim.SplatoonScripts.Duties.Dawntrail.DancingMadUltimate@P3_Limit_Cut","ConfigurationName":"絶妖星乱舞_A2B3C4D1","Configuration":"G8QHAKwLeDLcemUVfpbU6obnCNsZeWn8DTlkqYWPaaydwzz/feqRzFJEBpFJJoVTztsiSyzSODt9IUOO9EslirA/5n2qu5cHhQIhEV8ILe5WIDoFE1MiZ1a/3+rLv0bjhlhvEdH0oYtGMWmEJBoiPRIrER2yGXCz+Y2amfj9q0VH8EXZ/fkA0x5AG+B/UDhPWy0aHvrbAACn1r1EfINV1redcxmfBXLDvASFugXCW4U6IwFVMA1sAP9Ycz3synzfJ/77Eun+6UepAlPw5tTqF8GBUxDtdOPViiS21lrG8g2YMQRMrstivsPX/fJ+E8v7IAcObCV8jyzcN8HY050XmWSaiurjURBZcEZgVqA3JWdMu3X74s3yFCraAEyNdWCerFprRLfbN/LdPcxH/RssN8k5yIKO6TJ6rqlcjZMuwJj6e7y3eL3WIh8ThMr4zU7vGrAuiQkMm7ccJqxFaU4/4TOMsc1BD5NoZvzggLbsYJhDbaal202bES23ftJqUC4ho4BI7cBEZYNZMgNt25YLZim4HdmyARnbwfCaEoGYIAY=","Overrides":null}
```

#### コンフィグ: マーカー北から時計回りに A1B2C3D4

```
{"TargetScriptName":"SplaSim.SplatoonScripts.Duties.Dawntrail.DancingMadUltimate@P3_Limit_Cut","ConfigurationName":"絶妖星乱舞_A1B2C3D4","Configuration":"G8QHAKwLeDLcemUVfpbU6obnCNsZeWn8DTlkqYWPaaydwzz/feqRzFJEBpFJJoVTztsiSyzSODt9IUOO9EslirA/5n2qu5cHhQIhEV8ILe5WIDoFE1MiZ1a/3+rLv0bjhlhvEdH0oYtGMWmEJBoiPRIrER2yGXCz+Y2amfj9q0VH8EXZ/fkA0x5AG+B/UDhPWy0aHvrbAACn1r1EfINV1redcxmfBXLDvASFugXCW4U6IwFVMA1sAP9Ycz3synzfJ/77Eun+6UepAlPw5tTqF8GBUxDtdOPViiS21lrG8g2YMQRMrstivsPX/fJ+E8v7IAcObCV8jyzcN8HY050XmWSaiurjURBZcEZgVqA3JWdMu3X74s3yFCraAEyNdWCerFprRLfbN/LdPcxH/RssN8k5yIKO6TJ6rqlcjZMuwJj6e7y3eL3WIh8ThMr4zU7vGrAuiQkMm7ccJqxFaU4/4TOMsc1BD5NoZvzggLbsYJhDbaal2k2bES23ftJqUC4hY4FI7cBEZYNZ0gNt25YLZim4HdmyARnTwfCaEoGYIAY=","Overrides":null}
```

## P3 ブラックホール

ブラックホールの紐取りと最後の塔踏み＆頭割りがガイドされます。設定画面は日本語で記載されているので、一部の補足のみ追記しています。

![](/assets/splatoon/dmad/20260629052206.png)

#### URL

```
https://github.com/PunishXIV/Splatoon/raw/refs/heads/main/SplatoonScripts/Duties/Dawntrail/Dancing%20Mad/P3_Earthquake.cs
```

#### コンフィグ: ヤーン速報（ビーム誘導基本時計回り１本目のみ反時計回り） 20260629時点

```
{"TargetScriptName":"SplaSim.SplatoonScripts.Duties.Dawntrail.DancingMadUltimate@P3_Earthquake","ConfigurationName":"絶妖星乱舞_ヤーン速報_20260629","Configuration":"G2oQQKwObGPkYz+kLJ6YfEMqP2wqeiHYlKUWGHrTF+cUWqcj5uPktkL60HfLgsY3MUQstAipozAOOhlKu9dAgPj2yzaDakXpk1QH6sAp9L4kF1rpsudvaH18szAeCQ4tz1ok6zAZ0xRHW/pjJ8LhYH1M5+i//4niKOx4TtMuP7hXI+bQiEIyQqMr9yv0ZEaIFC11P4ovTRQ3CesoiuWpy0L8y/gakQsZEk2C7B0vNhJYUuf1zBTW52RaEuoSPUrwncPiGpLQokA5ju/aC74suPeRhKx4fILQFAStlNUoVZMIgHpInTV/T4ZOQlp7GYjjLomQbixbxKYYXESzE4MjPuorAPq9SBjOGVO2DkQTlO9S53nHl/LR6i5k1p0VmdYbqRUY+qmIKWRPSUHf9hg7oJo09kYS9HAOhjReD8xyguwh67MCI84bnd/PFRaDXV7MQHKMEwvFfHpSfIAlOjT4xIW8rKjsmwE6DylDq7FbrxtCE76yAz47Iv1gJCk/v0dEU0vDdho3M9KYuFMvWpVxIwLdMqWIoY27sPFNJ/hown9uMTUx2mgH/KhLlAvX0u2zFdzQgYxfs8BywR2NibgPukTVyQwbSXiatacTQCMDsunj38MgsNuWBLlI2CsfLW/TlAIG5l8WyKO/7iYBbHgSwDYJ4JpkcE0C0tSvMcFEE3DijYhPuVX21sf7xSJyQxTPKTXkgm3U0Tswx92nTAX/iBsQvnTKXJyHpjYfkX4cql6ukglibXlf0D80Hrok5EwnRccJrY/QJhLPtRTiAKBohFD4b/urPunlgtQ+rZwLzloIcOfcbnk8IWZ7TCuviLw3yS5gBwG/NekK6hAlmxmH+tvSn+dToAds+JKLZVE6ftv05ejCdyCaVpRt+tCfzLQiR/25wlEvFYrNeHKBwO+Y+B74fhQfFleDfFWgutZ2FiEGUHyYiD1o9wj/nVY+BydTfglGi8N/Z7WsJzRcbHMPTbwyspmcwvDfkDv0LdGkiudEC/vTLx5k1khU0fhAaY+gE87IVp/BtS9fJvqREfgWu8KcEBvr5Uc1G5eVT7jIszpgAaWcAUjYFWBox/u2V6QwZVmpm1DCVXS+nl9twVjy0kop5N7MP6bgwQXaqifONI5HFxjyq6EuxAA0DCct14tfLs9VTMj82oHRWgU=","Overrides":null}
```

#### コンフィグ: イディル（ビーム誘導全部時計回り） 20260629時点

```
{"TargetScriptName":"SplaSim.SplatoonScripts.Duties.Dawntrail.DancingMadUltimate@P3_Earthquake","ConfigurationName":"絶妖星乱舞_イディル_20260629","Configuration":"G2oQICwObGNk4Q8pDzcm/5Aam0QPgk1ZaoGhN31xTqF1OmI+Xq0tJELfufxiEXG7F1EILULqKIyDTobS7jXgV3vdTBSlKx1JlaiAU+j/du8vrXTZ97IXWhvfLIxHgkPLWIvkO0zGNMXRlvbHSoTDwfqYzvF//1PFcdSJ3KZ9fvCwRiwAhiCRkND4KhSlntQImaKVLjZicaJs07CSomAmyH8pbyN6CUuySRC+4+VGEksytZyZxAqdVEtSXU6RErznwJiGRLQoVIbr+/ZKrCvhgyTh1jw+QWoKklbCq7SquRiA+tUtNlzxpBhISusgiwDPXxIj3Vi2lEszuDjVToyOGKmvBuj3Imk4Y0zbOnCqoGynus8/vpqP9nAps/KsyLTfaO1g6MdStoTLkYS+4zF2IT1p7I9L0f1Z6BN5RVALCsKHrNAKnDhvdSQpVJaDXmDMQYKMUwvDfX1SfAA4SocmOC8R3JrK3imki4h2rCq7zbqjNNEbu2DzI9b3RhLzs3vENA0kcLk4Gotj4lG9aFfIjSh015Qijg7+2sa3gwRbyr9uMTlx6ngHE6Ay0V27lmyg7XBPB2LP5sEL4ZHGROQHZaLiZsxHIp5q9ekGbGRAV332Dz8M7LimQTAS9spHyxs1JYGe+Zdfwqe/7iYBXIASwDUJ4Jtk8E0C0jSuMt5UU2gSjYhQuRX+9sfHxW/shjiek2oIBuu4o3/gjvtPlb4gPuIehK+cKn/PI1OfkWg/DlUvV8kEsbaqr8hfmg9DknKmE8OTlNaGqFOJ51oqeQhQNkIw7PfD/z7p5YLUPqOciU5bSHCnbrc8BoLWx4zyAsl6d/kF7CFgtyphQSWiy2dmg/3tz5/nU6AHbPhagOVROn7b9OXo4jcwqtZp27SxP1lpTY76c8UjfmoskvPkEoHdMfU9ELER4+J6kK8KVNfaziJGD4uNE9EH7R9hf9DaZwBl0i8BqYHYH6yXNdBwuc08tPC/kc3kBIf9juyhbYno6niClvanXzzIrLGowLGR0i5BgXOyPeYw7cv/Ev3IEGyLfWECwbFiftSzcWE5cJnnfcACSjkDkMALQs9O9v2oTKEKs65yQihXMRl7eSvhuoaZabEl/Js5dhUfLjBWfDEmMny6wNJfDW0lRyCBCC3YO89MpqvYoNnVA+O1vg==","Overrides":null}
```
