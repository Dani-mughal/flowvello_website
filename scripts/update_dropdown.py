import re

with open('services.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_automation_dropdown = False
replaced_dropdown = False

for i, line in enumerate(lines):
    if '<li class="dropdown-submenu">' in line and i + 2 < len(lines) and 'Automation</span>' in lines[i+2]:
        in_automation_dropdown = True
        new_lines.append(line)
        continue

    if in_automation_dropdown:
        if '<ul class="dropdown-menu">' in line:
            new_lines.append(line)
            new_lines.append('                <li><a class="dropdown-item nested-subitem" href="services/lead-crm-automation.html"><i class="fal fa-filter" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Lead & CRM Automation</a></li>\n')
            new_lines.append('                <li><a class="dropdown-item nested-subitem" href="services/appointment-follow-up-automation.html"><i class="fal fa-calendar-check" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Appointment & Follow-up</a></li>\n')
            new_lines.append('                <li><a class="dropdown-item nested-subitem" href="services/ai-customer-support.html"><i class="fal fa-headset" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> AI Customer Support</a></li>\n')
            new_lines.append('                <li><a class="dropdown-item nested-subitem" href="services/business-reporting-dashboards.html"><i class="fal fa-chart-pie" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Reporting & Dashboards</a></li>\n')
            new_lines.append('                <li><a class="dropdown-item nested-subitem" href="services/api-system-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>\n')
            new_lines.append('                <li><a class="dropdown-item nested-subitem" href="services/ai-voice-workflow-agents.html"><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Voice & Workflow Agents</a></li>\n')
            continue
        if '</ul>' in line and in_automation_dropdown:
            new_lines.append(line)
            in_automation_dropdown = False
            replaced_dropdown = True
            continue
        if in_automation_dropdown and '<li><a class="dropdown-item nested-subitem"' in line:
            # skip old items
            continue

    new_lines.append(line)

with open('services.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Replaced dropdown: {replaced_dropdown}")
