import os

REDIRECTS = {
    "ai-agents.html": "ai-voice-workflow-agents.html",
    "calling-agents.html": "ai-voice-workflow-agents.html",
    "custom-ai-agents.html": "ai-voice-workflow-agents.html",
    "custom-dashboards.html": "business-reporting-dashboards.html",
    "executive-dashboards.html": "business-reporting-dashboards.html",
    "gohighlevel.html": "lead-crm-automation.html",
    "sales-automation.html": "lead-crm-automation.html",
    "workflow-automation.html": "lead-crm-automation.html",
}

for legacy, target in REDIRECTS.items():
    path = os.path.join('services', legacy)
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url={target}">
    <link rel="canonical" href="https://techtox.com/services/{target}">
    <title>Redirecting to {target} | Techtox</title>
</head>
<body>
    <p>Redirecting to <a href="{target}">{target}</a>...</p>
</body>
</html>'''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated legacy redirect: {legacy} -> {target}")
