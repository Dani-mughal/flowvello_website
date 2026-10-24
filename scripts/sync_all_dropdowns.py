import os, glob

def update_file_dropdown(filepath, is_sub):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines(keepends=True)
    new_lines = []
    in_automation_dropdown = False
    replaced = False

    prefix = "../services/" if is_sub else "services/"

    for i, line in enumerate(lines):
        if '<li class="dropdown-submenu">' in line and i + 2 < len(lines) and 'Automation</span>' in lines[i+2]:
            in_automation_dropdown = True
            new_lines.append(line)
            continue

        if in_automation_dropdown:
            if '<ul class="dropdown-menu">' in line:
                new_lines.append(line)
                new_lines.append(f'                <li><a class="dropdown-item nested-subitem" href="{prefix}lead-crm-automation.html"><i class="fal fa-filter" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Lead & CRM Automation</a></li>\n')
                new_lines.append(f'                <li><a class="dropdown-item nested-subitem" href="{prefix}appointment-follow-up-automation.html"><i class="fal fa-calendar-check" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Appointment & Follow-up</a></li>\n')
                new_lines.append(f'                <li><a class="dropdown-item nested-subitem" href="{prefix}ai-customer-support.html"><i class="fal fa-headset" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> AI Customer Support</a></li>\n')
                new_lines.append(f'                <li><a class="dropdown-item nested-subitem" href="{prefix}custom-dashboards.html"><i class="fal fa-chart-pie" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Reporting & Dashboards</a></li>\n')
                new_lines.append(f'                <li><a class="dropdown-item nested-subitem" href="{prefix}api-software-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>\n')
                new_lines.append(f'                <li><a class="dropdown-item nested-subitem" href="{prefix}ai-voice-workflow-agents.html"><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Voice & Workflow Agents</a></li>\n')
                continue
            if '</ul>' in line and in_automation_dropdown:
                new_lines.append(line)
                in_automation_dropdown = False
                replaced = True
                continue
            if in_automation_dropdown and '<li><a class="dropdown-item nested-subitem"' in line:
                continue

        new_lines.append(line)

    if replaced:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated dropdown in {filepath}")

# Update root pages
for path in glob.glob('*.html'):
    update_file_dropdown(path, False)

# Update industries pages
for path in glob.glob('industries/*.html'):
    update_file_dropdown(path, True)

# Update non-redirect services pages
for path in glob.glob('services/*.html'):
    with open(path, 'r', encoding='utf-8') as f:
        head = f.read(500)
    if 'http-equiv="refresh"' not in head:
        update_file_dropdown(path, True)
