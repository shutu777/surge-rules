import requests
import os

def download_rules(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

def convert_domain_rules(rules, rule_type="DOMAIN-SUFFIX"):
    converted = []
    for line in rules:
        line = line.strip()
        if line and not line.startswith('#'):
            if rule_type == "IP-CIDR":
                converted.append(f"{rule_type},{line}")
            else:
                converted.append(f"{rule_type},{line}")
    return converted

def main():
    # 域名类规则
    domain_rules = {
        "private": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/private.list",
        "cn": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/cn.list",
        "apple-cn": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/apple-cn.list",
        "github": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/github.list",
        "youtube": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/youtube.list",
        "google": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/google.list",
        "telegram": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/telegram.list",
        "netflix": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/netflix.list",
        "ai-chat": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/category-ai-chat-!cn.list",
        "microsoft": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/microsoft.list",
        "tiktok": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/tiktok.list",
        "paypal": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/paypal.list",
        "speedtest": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/ookla-speedtest.list",
        "games": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/category-games.list",
        "game-accelerator-cn": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/category-game-accelerator-cn.list",
        "geolocation-!cn": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/geolocation-!cn.list"
    }

    # IP类规则
    ip_rules = {
        "cn": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip/cn.list",
        "google": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip/google.list",
        "netflix": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip/netflix.list",
        "telegram": "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip/telegram.list"
    }

    os.makedirs("rules", exist_ok=True)

    # 处理域名规则
    for name, url in domain_rules.items():
        try:
            rules = download_rules(url)
            converted_rules = convert_domain_rules(rules)
            with open(f"rules/{name}.list", "w") as f:
                f.write("\n".join(converted_rules))
        except Exception as e:
            print(f"Error processing {name}: {str(e)}")

    # 处理IP规则
    for name, url in ip_rules.items():
        try:
            rules = download_rules(url)
            converted_rules = convert_domain_rules(rules, "IP-CIDR")
            with open(f"rules/{name}-ip.list", "w") as f:
                f.write("\n".join(converted_rules))
        except Exception as e:
            print(f"Error processing {name} IP rules: {str(e)}")

if __name__ == "__main__":
    main() 