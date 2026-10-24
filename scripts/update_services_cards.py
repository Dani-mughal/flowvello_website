import os, glob

# ==========================================
# 1. Update services.html Phase 04 Section
# ==========================================
def update_services_html():
    with open('services.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Cards for services.html WITHOUT tools badge, WITH capability highlights and 'Explore Service' link
    new_phase_04_grid = '''        <div class="shadcn-service-grid">

           <!-- Card 1: Lead & CRM Automation -->
           <a href="services/lead-crm-automation.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.1s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80" alt="Lead & CRM Automation" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">Lead & CRM Automation</h3>
                  <p class="shadcn-card-desc">Capture, qualify, route, and track leads while automating CRM updates and follow-ups.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Multi-Source Lead Ingestion & Webhooks
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Intelligent Routing & Auto-Assignment
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Real-Time Two-Way CRM Synchronization
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; display: inline-flex; align-items: center; gap: 6px; font-family: 'Sora', sans-serif; font-size: 14px; font-weight: 600; color: #FF2E3E;">
                     Explore Service <i class="fa fa-arrow-right" style="font-size: 12px; transition: transform 0.2s ease;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 2: Appointment & Follow-up Automation -->
           <a href="services/appointment-follow-up-automation.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.2s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=800&q=80" alt="Appointment & Follow-up Automation" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">Appointment & Follow-up Automation</h3>
                  <p class="shadcn-card-desc">Automate bookings, confirmations, reminders, cancellations, and missed-appointment follow-ups.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Frictionless Calendar Synchronization
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Multi-Channel SMS & Email Reminders
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Automated Missed-Appointment Recovery
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; display: inline-flex; align-items: center; gap: 6px; font-family: 'Sora', sans-serif; font-size: 14px; font-weight: 600; color: #FF2E3E;">
                     Explore Service <i class="fa fa-arrow-right" style="font-size: 12px; transition: transform 0.2s ease;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 3: AI Customer Support -->
           <a href="services/ai-customer-support.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.3s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1534536281715-e28d76689b4d?auto=format&fit=crop&w=800&q=80" alt="AI Customer Support" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">AI Customer Support</h3>
                  <p class="shadcn-card-desc">Answer approved questions, retrieve information from a business knowledge base, collect customer details, and escalate complex requests.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Grounded Knowledge Base Ingestion
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Sub-Second 24/7 FAQ Resolution
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Seamless Live Human Escalation
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; display: inline-flex; align-items: center; gap: 6px; font-family: 'Sora', sans-serif; font-size: 14px; font-weight: 600; color: #FF2E3E;">
                     Explore Service <i class="fa fa-arrow-right" style="font-size: 12px; transition: transform 0.2s ease;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 4: Business Reporting & Dashboards -->
           <a href="services/custom-dashboards.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.4s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80" alt="Business Reporting & Dashboards" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">Business Reporting & Dashboards</h3>
                  <p class="shadcn-card-desc">Consolidate operational data, visualize KPIs, schedule reports, and trigger threshold alerts.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Multi-Tool Data Aggregation & Sync
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Automated Scheduled Executive Digests
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Real-Time Anomaly & Threshold Alerts
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; display: inline-flex; align-items: center; gap: 6px; font-family: 'Sora', sans-serif; font-size: 14px; font-weight: 600; color: #FF2E3E;">
                     Explore Service <i class="fa fa-arrow-right" style="font-size: 12px; transition: transform 0.2s ease;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 5: API & Software Integration -->
           <a href="services/api-software-integration.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.5s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80" alt="API & Software Integration" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">API & Software Integration</h3>
                  <p class="shadcn-card-desc">Connect business applications through APIs, webhooks, and reliable data synchronization.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Custom REST & Webhook Pipelines
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Eradication of Duplicate Data Entry
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Self-Healing Exponential Retries
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; display: inline-flex; align-items: center; gap: 6px; font-family: 'Sora', sans-serif; font-size: 14px; font-weight: 600; color: #FF2E3E;">
                     Explore Service <i class="fa fa-arrow-right" style="font-size: 12px; transition: transform 0.2s ease;"></i>
                  </div>
              </div>
           </a>

           <!-- Card 6: AI Voice & Workflow Agents -->
           <a href="services/ai-voice-workflow-agents.html" class="shadcn-service-card wow fadeInUp" data-wow-delay="0.6s" style="display: flex; flex-direction: column;">
              <img class="shadcn-img-block" src="https://images.unsplash.com/photo-1590650516494-0c8e4a4dd67e?auto=format&fit=crop&w=800&q=80" alt="AI Voice & Workflow Agents" loading="lazy" style="object-fit: cover; width: 100%; display: block;">
              <div class="d-flex flex-column" style="gap: 8px; flex: 1;">
                  <h3 class="shadcn-card-title">AI Voice & Workflow Agents</h3>
                  <p class="shadcn-card-desc">Build narrowly scoped voice and task agents that handle approved enquiries, execute defined actions, and escalate exceptions.</p>
                  <ul style="list-style: none; padding: 0; margin: 10px 0 4px 0; display: flex; flex-direction: column; gap: 6px;">
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Ultra-Low Latency Conversational Voice
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Direct CRM Logging & Calendar Booking
                     </li>
                     <li style="font-family: 'Sora', sans-serif; font-size: 13px; color: #4b5563; display: flex; align-items: center; gap: 8px;">
                        <i class="fa fa-check" style="color: #FF2E3E; font-size: 11px;"></i> Instant Warm Transfer to Live Staff
                     </li>
                  </ul>
                  <div style="margin-top: auto; padding-top: 12px; display: inline-flex; align-items: center; gap: 6px; font-family: 'Sora', sans-serif; font-size: 14px; font-weight: 600; color: #FF2E3E;">
                     Explore Service <i class="fa fa-arrow-right" style="font-size: 12px; transition: transform 0.2s ease;"></i>
                  </div>
              </div>
           </a>

        </div>'''

    import re
    pattern = re.compile(r'(<div id="automation"[^>]*>.*?Phase 04.*?Automation.*?</div>\s*)(<div class="shadcn-service-grid">.*?</div>)(\s*</div>\s*</div>)', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(r'\1' + new_phase_04_grid + r'\3', content)
        with open('services.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated services.html Phase 04 cards without tools, with capability highlights and Explore Service links.")
    else:
        print("Failed to match Phase 04 grid pattern in services.html")

update_services_html()
