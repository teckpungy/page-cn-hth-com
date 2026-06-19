import json
from typing import Dict, List, Optional

# 内置站点资料
SITE_DATA = {
    "name": "华体会站点",
    "url": "https://page-cn-hth.com",
    "keywords": ["华体会", "体育", "娱乐", "在线平台"],
    "tags": ["体育", "娱乐", "互动"],
    "description": "华体会提供丰富的体育赛事与娱乐互动体验，致力于打造高品质线上平台。"
}

def format_summary(data: Dict[str, object]) -> str:
    """将站点资料格式化为结构化摘要"""
    lines = []
    lines.append("站点摘要".center(40, "="))
    lines.append(f"名称: {data.get('name', '未知')}")
    lines.append(f"URL: {data.get('url', '无')}")
    lines.append(f"关键词: {', '.join(data.get('keywords', []))}")
    lines.append(f"标签: {', '.join(data.get('tags', []))}")
    lines.append(f"说明: {data.get('description', '无')}")
    lines.append("=" * 42)
    return "\n".join(lines)

def generate_json_output(data: Optional[Dict[str, object]] = None) -> str:
    """生成 JSON 格式的结构化摘要"""
    if data is None:
        data = SITE_DATA
    output = {
        "title": data["name"],
        "url": data["url"],
        "keywords": data["keywords"],
        "tags": data["tags"],
        "summary": data["description"]
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def collect_site_info() -> Dict[str, object]:
    """返回站点资料的副本"""
    return dict(SITE_DATA)

def print_summary(custom_data: Optional[Dict[str, object]] = None) -> None:
    """打印结构化摘要"""
    data = custom_data if custom_data else collect_site_info()
    print(format_summary(data))

def validate_site_data(data: Dict[str, object]) -> bool:
    """验证站点资料是否完整"""
    required_keys = ["name", "url", "keywords", "tags", "description"]
    for key in required_keys:
        if key not in data:
            return False
    if not isinstance(data.get("keywords"), list):
        return False
    if not isinstance(data.get("tags"), list):
        return False
    return True

def main() -> None:
    """主入口：输出结构化摘要"""
    if not validate_site_data(SITE_DATA):
        print("站点资料无效")
        return

    print("文本摘要:")
    print_summary()

    print("\nJSON 摘要:")
    json_string = generate_json_output()
    print(json_string)

if __name__ == "__main__":
    main()