# Mihomo 规则转 Surge 规则

这个项目自动将 Mihomo (Meta) 规则转换为 Surge 规则格式。

## 简介

本项目生成适用于 **Surge** 的规则集（RULE-SET），使用 GitHub Actions 每 12 小时自动更新一次，保证规则最新。

## 说明

本项目规则集的数据主要来源于：

- [@Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules)：Surge 规则集格式参考
- [@MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat)：规则数据来源

## 在线地址 (URL)

如果无法访问域名 raw.githubusercontent.com，可以使用第二个地址（cdn.jsdelivr.net），但是内容更新会有 12 小时的延迟。

### DOMAIN-SET:

私有域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/private.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/private.list

直连域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/cn.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/cn.list

Apple 在中国大陆可直连的域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/apple-cn.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/apple-cn.list

GitHub 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/github.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/github.list

YouTube 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/youtube.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/youtube.list

Google 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/google.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/google.list

Telegram 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/telegram.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/telegram.list

Netflix 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/netflix.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/netflix.list

HBO 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/hbo.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/hbo.list

Disney 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/disney.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/disney.list

Bahamut 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/bahamut.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/bahamut.list

AI 聊天相关域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/ai-chat.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/ai-chat.list

微软域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/microsoft.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/microsoft.list

TikTok 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/tiktok.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/tiktok.list

PayPal 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/paypal.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/paypal.list

Speedtest 域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/speedtest.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/speedtest.list

游戏相关域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/games.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/games.list

游戏加速器中国域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/game-accelerator-cn.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/game-accelerator-cn.list

非中国域名列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/geolocation-not-cn.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/geolocation-not-cn.list

### IP-SET:

中国 IP 地址列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/cn-ip.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/cn-ip.list

Google IP 地址列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/google-ip.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/google-ip.list

Netflix IP 地址列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/netflix-ip.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/netflix-ip.list

Telegram IP 地址列表：

- https://raw.githubusercontent.com/shutu777/surge-rules/release/ruleset/telegram-ip.list
- https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/telegram-ip.list

## 使用方法

在 Surge 配置文件中添加如下配置：

```
# 域名规则
RULE-SET,https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/cn.list,DIRECT
RULE-SET,https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/apple-cn.list,DIRECT
RULE-SET,https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/google.list,PROXY

# IP规则
RULE-SET,https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/cn-ip.list,DIRECT
RULE-SET,https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/google-ip.list,PROXY

```

## 自动更新

规则在以下情况下会自动更新：

- 每 12 小时自动更新一次
- 推送到 main/master 分支时
- 手动触发 GitHub Action 工作流

## 致谢

- [@Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules)
- [@MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat)

## 许可证

GPL-3.0 License
