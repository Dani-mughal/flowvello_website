import re

def update_services_html():
    with open('services.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Phase 04 Automation block and replace its grid
    pattern = re.compile(
        r'(<!-- Dept Header -->\s*<div class="mb-5 d-flex flex-column align-items-start wow fadeInUp"[^>]*>.*?Phase 04.*?Automation.*?</div>\s*<div class="shadcn-service-grid">)(.*?)(</div>\s*</div>\s*</div>\s*</section>)',
        re.DOTALL
    )

    new_cards = '''
           <!-- Card 1: Lead & CRM Automation -->
           <a href="services/lead-crm-automation.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.1s">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80" alt="Lead & CRM Automation" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px;">
                  <h3 class="shadcn-card-title">Lead & CRM Automation</h3>
                  <p class="shadcn-card-desc">Capture leads from websites and forms, assign them to the right person, update the CRM, and send instant notifications and follow-up reminders.</p>
                  <div style="font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 500; color: #FF2E3E; margin-top: 4px;">
                     <span style="color: #6b7280; font-weight: 600;">Tools:</span> n8n, HubSpot, Google Sheets, webhooks
                  </div>
              </div>
           </a>

           <!-- Card 2: Appointment & Follow-up Automation -->
           <a href="services/appointment-follow-up-automation.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.2s">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=800&q=80" alt="Appointment & Follow-up Automation" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px;">
                  <h3 class="shadcn-card-title">Appointment & Follow-up Automation</h3>
                  <p class="shadcn-card-desc">Automate booking confirmations, reminders, rescheduling notifications, missed-appointment follow-ups, and staff alerts.</p>
                  <div style="font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 500; color: #FF2E3E; margin-top: 4px;">
                     <span style="color: #6b7280; font-weight: 600;">Tools:</span> n8n, Google Calendar, Calendly, email or approved messaging APIs
                  </div>
              </div>
           </a>

           <!-- Card 3: AI Customer Support -->
           <a href="services/ai-customer-support.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.3s">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1534536281715-e28d76689b4d?auto=format&fit=crop&w=800&q=80" alt="AI Customer Support" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px;">
                  <h3 class="shadcn-card-title">AI Customer Support</h3>
                  <p class="shadcn-card-desc">Answer common questions using approved business information, collect customer details, and transfer complex requests to a human.</p>
                  <div style="font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 500; color: #FF2E3E; margin-top: 4px;">
                     <span style="color: #6b7280; font-weight: 600;">Tools:</span> OpenAI API, n8n, knowledge base, website chat integration
                  </div>
              </div>
           </a>

           <!-- Card 4: Business Reporting & Dashboards -->
           <a href="services/business-reporting-dashboards.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.4s">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80" alt="Business Reporting & Dashboards" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px;">
                  <h3 class="shadcn-card-title">Business Reporting & Dashboards</h3>
                  <p class="shadcn-card-desc">Combine data from business tools, generate scheduled reports, track KPIs, and notify owners when important thresholds are reached.</p>
                  <div style="font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 500; color: #FF2E3E; margin-top: 4px;">
                     <span style="color: #6b7280; font-weight: 600;">Tools:</span> Google Sheets, Looker Studio, n8n, APIs
                  </div>
              </div>
           </a>

           <!-- Card 5: API & Software Integration -->
           <a href="services/api-system-integration.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.5s">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80" alt="API & Software Integration" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px;">
                  <h3 class="shadcn-card-title">API & Software Integration</h3>
                  <p class="shadcn-card-desc">Connect websites, CRMs, forms, spreadsheets, and other business applications to eliminate duplicate data entry and disconnected workflows.</p>
                  <div style="font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 500; color: #FF2E3E; margin-top: 4px;">
                     <span style="color: #6b7280; font-weight: 600;">Tools:</span> REST APIs, webhooks, JavaScript, n8n
                  </div>
              </div>
           </a>

           <!-- Card 6: AI Voice & Workflow Agents -->
           <a href="services/ai-voice-workflow-agents.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.6s">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1590650516494-0c8e4a4dd67e?auto=format&fit=crop&w=800&q=80" alt="AI Voice & Workflow Agents" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px;">
                  <h3 class="shadcn-card-title">AI Voice & Workflow Agents</h3>
                  <p class="shadcn-card-desc">Build narrowly scoped voice or task agents that handle approved enquiries, collect information, create CRM records, and escalate exceptions.</p>
                  <div style="font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 500; color: #FF2E3E; margin-top: 4px;">
                     <span style="color: #6b7280; font-weight: 600;">Tools:</span> a voice platform such as Vapi or Retell AI, n8n, business APIs
                  </div>
              </div>
           </a>
'''

    # Ensure id="automation" on wrapper
    content = content.replace(
        '<div class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">\n      <div class="container mx-auto">\n        <!-- Dept Header -->\n        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">\n            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #000000; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: \'Sora\', sans-serif; letter-spacing: 1px; text-transform: uppercase;">\n              Phase 04\n            </div>\n            <h2 style="font-family: \'Sora\', sans-serif; font-size: 48px; font-weight: 500; color: #000000; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">\n              Automation',
        '<div id="automation" class="w-full py-5 lg:py-5" style="border-bottom: 1px solid #f3f4f6; padding-top: 80px !important; padding-bottom: 80px !important;">\n      <div class="container mx-auto">\n        <!-- Dept Header -->\n        <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 12px; margin-bottom: 50px !important;">\n            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #000000; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: \'Sora\', sans-serif; letter-spacing: 1px; text-transform: uppercase;">\n              Phase 04\n            </div>\n            <h2 style="font-family: \'Sora\', sans-serif; font-size: 48px; font-weight: 500; color: #000000; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">\n              Automation'
    )

    # Update description under Phase 04 Automation
    content = content.replace(
        '<p style="color: #6b7280; font-size: 18px; font-family: \'Sora\', sans-serif; margin: 0; max-width: 600px; line-height: 1.6;">\n              Eliminating bottlenecks with intelligent systems.\n            </p>',
        '<p style="color: #6b7280; font-size: 18px; font-family: \'Sora\', sans-serif; margin: 0; max-width: 650px; line-height: 1.6;">\n              Clear, business-focused solutions engineered to solve real operational bottlenecks and eliminate repetitive work.\n            </p>'
    )

    if pattern.search(content):
        content = pattern.sub(r'\1' + new_cards + r'\3', content)
        print("Replaced Phase 04 cards successfully.")
    else:
        print("Pattern match failed for Phase 04 cards.")

    # Also update the navigation dropdown for Automation
    old_dropdown_automation = '''        <li class="dropdown-submenu">
            <a class="dropdown-item nested-item" href="#">
                <span><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Automation</span>
                <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
            </a>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item nested-subitem" href="services/ai-agents.html"><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> AI Agents</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/custom-dashboards.html"><i class="fal fa-chart-pie" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Custom Dashboards</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/calling-agents.html"><i class="fal fa-headset" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Calling Agents</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/api-system-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API Integrations</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/gohighlevel.html"><i class="fa fa-funnel-dollar" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> GoHighLevel (GHL)</a></li>
            </ul>
        </li>'''

    new_dropdown_automation = '''        <li class="dropdown-submenu">
            <a class="dropdown-item nested-item" href="#">
                <span><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Automation</span>
                <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
            </a>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item nested-subitem" href="services/lead-crm-automation.html"><i class="fal fa-filter" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Lead & CRM Automation</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/appointment-follow-up-automation.html"><i class="fal fa-calendar-check" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Appointment & Follow-up</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/ai-customer-support.html"><i class="fal fa-headset" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> AI Customer Support</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/business-reporting-dashboards.html"><i class="fal fa-chart-pie" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Reporting & Dashboards</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/api-system-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>
                <li><a class="dropdown-item nested-subitem" href="services/ai-voice-workflow-agents.html"><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Voice & Workflow Agents</a></li>
            </ul>
        </li>'''

    if old_dropdown_automation in content:
        content = content.replace(old_dropdown_automation, new_dropdown_automation)
        print("Updated navbar dropdown in services.html")

    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_services_html()
