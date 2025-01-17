# Mihomo 规则转 Surge 规则

这个项目自动将 Mihomo (Meta) 规则转换为 Surge 规则格式。

## 功能特点

- 自动从 MetaCubeX/meta-rules-dat 获取最新规则
- 支持域名规则和 IP 规则转换
- 每 12 小时自动更新一次
- 支持手动触发更新
- 使用 CDN 加速规则下载
- 自动发布 Release 和更新 release 分支

## 规则列表

### 域名规则

- private.list - 私有域名
- cn.list - 中国域名
- apple-cn.list - 苹果中国域名
- github.list - GitHub 域名
- youtube.list - YouTube 域名
- google.list - Google 域名
- telegram.list - Telegram 域名
- netflix.list - Netflix 域名
- ai-chat.list - AI 聊天相关域名
- microsoft.list - 微软域名
- tiktok.list - TikTok 域名
- paypal.list - PayPal 域名
- speedtest.list - Speedtest 域名
- games.list - 游戏相关域名
- game-accelerator-cn.list - 游戏加速器中国域名
- geolocation-not-cn.list - 非中国域名

### IP 规则

- cn-ip.list - 中国 IP 地址
- google-ip.list - Google IP 地址
- netflix-ip.list - Netflix IP 地址
- telegram-ip.list - Telegram IP 地址

## 使用方法

1. 在 Surge 配置文件中引用规则：

```
# 域名规则
RULE-SET,https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/netflix.list,NETFLIX

# IP规则
RULE-SET,https://cdn.jsdelivr.net/gh/shutu777/surge-rules@release/ruleset/netflix-ip.list,NETFLIX
```

2. 规则更新时会自动发布新的 Release 并更新 release 分支
3. 使用 jsDelivr CDN 加速规则下载，无需担心 GitHub 连接问题

## 自动更新

规则在以下情况下会自动更新：

- 每 12 小时自动更新一次
- 推送到 main/master 分支时
- 手动触发 GitHub Action 工作流

## 许可证

MIT License
