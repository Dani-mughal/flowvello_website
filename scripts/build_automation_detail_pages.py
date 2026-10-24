import os

PAGES = [
    {
        "filename": "lead-crm-automation.html",
        "title": "Lead & CRM Automation | Techtox",
        "meta_desc": "Capture leads from websites and forms, assign them to the right person, update the CRM, and send instant notifications and follow-up reminders.",
        "eyebrow": "OPERATIONAL AUTOMATION",
        "h1": "Lead & CRM Automation",
        "lead": "Capture leads from websites and forms, assign them to the right person, update the CRM, and send instant notifications and follow-up reminders.",
        "tools_badge": "Tools: n8n &bull; HubSpot &bull; Google Sheets &bull; Webhooks",
        "hero_img": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1920&q=80",
        "showcase_imgs": [
            "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            ("fa fa-filter", "Multi-Source Lead Ingestion", "Capture inbound inquiries instantaneously from website forms, landing pages, Typeform, Webflow, and ad campaigns via secure webhooks without latency."),
            ("fa fa-user-tag", "Intelligent Routing & Rep Assignment", "Automatically route incoming leads using custom round-robin rules, territory mapping, or deal value thresholds directly to the best-suited rep."),
            ("fa fa-sync-alt", "Bi-Directional CRM Synchronization", "Seamlessly sync lead records across HubSpot, Salesforce, Pipedrive, and Google Sheets, eliminating data entry delays and pipeline gaps."),
            ("fa fa-bell", "Instant Team Notifications & Alerts", "Trigger real-time notifications to Slack channels, Microsoft Teams, or mobile SMS the exact second a high-priority lead submits their details."),
            ("fa fa-envelope-open-text", "Automated Follow-Up Reminders", "Deploy immediate personalized confirmation emails, automated SMS touches, and reminder tasks so reps follow up within the golden 5-minute window."),
            ("fa fa-shield-check", "Data Hygiene & Deduplication", "Automatically cleanse contact information, validate business email addresses, and merge duplicate leads before they clutter your database.")
        ]
    },
    {
        "filename": "appointment-follow-up-automation.html",
        "title": "Appointment & Follow-up Automation | Techtox",
        "meta_desc": "Automate booking confirmations, reminders, rescheduling notifications, missed-appointment follow-ups, and staff alerts.",
        "eyebrow": "CALENDAR & BOOKING SYSTEMS",
        "h1": "Appointment & Follow-up Automation",
        "lead": "Automate booking confirmations, reminders, rescheduling notifications, missed-appointment follow-ups, and staff alerts.",
        "tools_badge": "Tools: n8n &bull; Google Calendar &bull; Calendly &bull; Email & Messaging APIs",
        "hero_img": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=1920&q=80",
        "showcase_imgs": [
            "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            ("fa fa-calendar-check", "Automated Booking Confirmations", "Instantly dispatch calendar invites with dynamic video meeting links (Zoom/Google Meet), timezone conversions, and custom prep documentation."),
            ("fa fa-clock", "Multi-Channel Smart Reminders", "Deliver sequenced reminders via SMS, WhatsApp, and email at 24 hours, 2 hours, and 15 minutes before appointments to minimize no-show rates."),
            ("fa fa-calendar-alt", "Self-Service Rescheduling Protocols", "Empower clients to reschedule with one click while automations instantly clear the host's calendar, notify attendees, and adjust CRM statuses."),
            ("fa fa-history", "Missed-Appointment Recovery Workflows", "When an appointment is flagged as a no-show, immediately launch polite, automated re-booking sequences to reclaim lost pipeline opportunities."),
            ("fa fa-user-clock", "Internal Staff & Host Alerts", "Notify meeting hosts on Slack or mobile with pre-call dossiers, prospect form answers, and direct links to their CRM record 10 minutes prior."),
            ("fa fa-sliders-h", "Calendar Buffer & Availability Guardrails", "Enforce automatic buffer times, prevent double-bookings across multiple team calendars, and lock out unapproved booking windows.")
        ]
    },
    {
        "filename": "ai-customer-support.html",
        "title": "AI Customer Support | Techtox",
        "meta_desc": "Answer common questions using approved business information, collect customer details, and transfer complex requests to a human.",
        "eyebrow": "INTELLIGENT SUPPORT INFRASTRUCTURE",
        "h1": "AI Customer Support",
        "lead": "Answer common questions using approved business information, collect customer details, and transfer complex requests to a human.",
        "tools_badge": "Tools: OpenAI API &bull; n8n &bull; Knowledge Base &bull; Website Chat Integration",
        "hero_img": "https://images.unsplash.com/photo-1534536281715-e28d76689b4d?auto=format&fit=crop&w=1920&q=80",
        "showcase_imgs": [
            "https://images.unsplash.com/photo-1534536281715-e28d76689b4d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            ("fa fa-book-open", "Strict Knowledge Base Grounding", "Answer inquiries using only verified company information, product catalogs, shipping terms, and refund policies with strict anti-hallucination safeguards."),
            ("fa fa-address-card", "Automated Customer Detail Intake", "Gather essential customer identifiers including name, account email, order number, and specific issue descriptions before troubleshooting."),
            ("fal fa-headset", "Sub-Second 24/7 Question Resolution", "Resolve 60-80% of repetitive questions instantly on your website chat widget without forcing customers to wait for business hours."),
            ("fa fa-user-friends", "Seamless Human Escalation Hand-Off", "Instantly route frustrated customers, billing disputes, or non-standard queries to human staff via Zendesk, Freshdesk, Slack, or email."),
            ("fa fa-ticket-alt", "Automated CRM & Ticket Generation", "Generate clean support tickets complete with conversation transcripts, automated intent tagging, and conversation summaries in your CRM."),
            ("fal fa-chart-pie", "Support Analytics & Resolution Insights", "Track customer question trends, escalation percentages, CSAT sentiment ratings, and common documentation gaps in real-time dashboards.")
        ]
    },
    {
        "filename": "business-reporting-dashboards.html",
        "title": "Business Reporting & Dashboards | Techtox",
        "meta_desc": "Combine data from business tools, generate scheduled reports, track KPIs, and notify owners when important thresholds are reached.",
        "eyebrow": "OPERATIONAL INTELLIGENCE",
        "h1": "Business Reporting & Dashboards",
        "lead": "Combine data from business tools, generate scheduled reports, track KPIs, and notify owners when important thresholds are reached.",
        "tools_badge": "Tools: Google Sheets &bull; Looker Studio &bull; n8n &bull; Custom APIs",
        "hero_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1920&q=80",
        "showcase_imgs": [
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            ("fa fa-layer-group", "Multi-Tool Data Aggregation", "Consolidate siloed data from Stripe, Shopify, QuickBooks, HubSpot, Google Ads, and Meta Ads into unified, clean reporting pipelines."),
            ("fa fa-paper-plane", "Automated Scheduled Digest Reports", "Deliver clean daily or weekly PDF/Slack reports summarizing revenue, margins, active pipeline, and operational throughput to executives automatically."),
            ("fa fa-chart-line", "Interactive Looker Studio Dashboards", "High-fidelity, interactive dashboards designed for decision-makers to inspect historical trends, filter by date ranges, and view company KPIs."),
            ("fa fa-exclamation-triangle", "Threshold & Anomaly Alert Triggers", "Set custom alert triggers that immediately notify company owners on Slack or SMS if ad CAC exceeds targets, revenue dips, or refund rates spike."),
            ("fa fa-table", "Live Google Sheets Formula Sync", "Keep live spreadsheet models populated with real-time numbers, formatted cleanly for financial forecasting and departmental budget reviews."),
            ("fa fa-check-double", "Automated Data Quality & Hygiene Audits", "Continuous background verification that flags missing entries, reconciles cross-platform discrepancies, and normalizes currencies.")
        ]
    },
    {
        "filename": "api-system-integration.html",
        "title": "API & Software Integration | Techtox",
        "meta_desc": "Connect websites, CRMs, forms, spreadsheets, and other business applications to eliminate duplicate data entry and disconnected workflows.",
        "eyebrow": "CUSTOM ARCHITECTURE & INTEGRATION",
        "h1": "API & Software Integration",
        "lead": "Connect websites, CRMs, forms, spreadsheets, and other business applications to eliminate duplicate data entry and disconnected workflows.",
        "tools_badge": "Tools: REST APIs &bull; Webhooks &bull; JavaScript &bull; n8n",
        "hero_img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1920&q=80",
        "showcase_imgs": [
            "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            ("fal fa-plug", "Custom API & Webhook Pipelines", "Engineer reliable connections between third-party SaaS tools, custom internal applications, and cloud databases using modern REST and GraphQL APIs."),
            ("fa fa-clone", "Elimination of Duplicate Data Entry", "Eradicate manual copy-pasting between websites, billing portals, inventory systems, and spreadsheets with instant background synchronization."),
            ("fa fa-network-wired", "Event-Driven Webhook Routing", "Trigger immediate downstream business logic the millisecond an event occurs—such as a signed contract, captured payment, or new order."),
            ("fab fa-js", "Custom JavaScript Data Transformation", "Transform, sanitize, and validate payload structures on the fly to bridge incompatible data formats between disparate legacy and modern systems."),
            ("fa fa-shield-alt", "Self-Healing Error Queues & Retries", "Prevent data drop-offs during third-party API downtimes with exponential backoff retries, dead-letter logging, and instant failure alerts."),
            ("fa fa-key", "Enterprise Authentication & Token Management", "Secure all endpoints using OAuth 2.0, API key rotation, HMAC signature verification, and granular role-based access control.")
        ]
    },
    {
        "filename": "ai-voice-workflow-agents.html",
        "title": "AI Voice & Workflow Agents | Techtox",
        "meta_desc": "Build narrowly scoped voice or task agents that handle approved enquiries, collect information, create CRM records, and escalate exceptions.",
        "eyebrow": "NARROWLY SCOPED AGENTS",
        "h1": "AI Voice & Workflow Agents",
        "lead": "Build narrowly scoped voice or task agents that handle approved enquiries, collect information, create CRM records, and escalate exceptions.",
        "tools_badge": "Tools: Vapi / Retell AI &bull; n8n &bull; Business APIs &bull; CRM Integrations",
        "hero_img": "https://images.unsplash.com/photo-1590650516494-0c8e4a4dd67e?auto=format&fit=crop&w=1920&q=80",
        "showcase_imgs": [
            "https://images.unsplash.com/photo-1590650516494-0c8e4a4dd67e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80"
        ],
        "features": [
            ("fal fa-headset", "Narrowly Scoped Voice Calling", "Deploy ultra-low latency voice agents on Vapi or Retell AI focused on specific operational phone calls: booking appointments, verifying info, or triage."),
            ("fa fa-shield-alt", "Approved Information & Guardrails", "Strict conversational boundaries that never guess or extrapolate—agents only speak from approved business FAQs, pricing tables, and guidelines."),
            ("fa fa-user-edit", "Structured Caller Information Collection", "Accurately capture caller contact details, property addresses, order IDs, and project scopes with phonetic spelling confirmation."),
            ("fa fa-database", "Direct CRM Record Creation", "Automatically populate new contact records, update deal stages, log full audio recordings, and generate call transcripts inside your CRM via n8n."),
            ("fa fa-phone-volume", "Intelligent Escalation & Warm Transfer", "Smoothly transfer the call to a live human representative the second a caller requests staff or when complex criteria require human expertise."),
            ("fal fa-robot", "Post-Call Workflow Execution", "Trigger immediate actions once the phone hangs up: send SMS meeting confirmations, email intake forms, and assign follow-up tasks to reps.")
        ]
    }
]

def render_page(p):
    features_html = ""
    for icon, title, desc in p["features"]:
        features_html += f'''            <div class="feature-light-card">
                <div class="fl-icon"><i class="{icon}"></i></div>
                <h3 class="fl-title">{title}</h3>
                <p class="fl-desc">{desc}</p>
            </div>\n'''

    showcase_html = ""
    for i, img in enumerate(p["showcase_imgs"]):
        showcase_html += f'''            <div style="border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; background: #f8fafc; aspect-ratio: 16/9;">
                <img src="{img}" alt="Deliverable {i+1}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>\n'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <meta http-equiv="X-UA-Compatible" content="ie=edge">
   <meta name="description" content="{p['meta_desc']}">
   <link rel="shortcut icon" href="../img/softoweb.png">
   <link rel="preconnect" href="https://fonts.gstatic.com">
   <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600;700;800&family=Teko:wght@400;500;600;700&display=swap" rel="stylesheet">
   <link rel="stylesheet" href="../css/bootstrap.css">
   <link rel="stylesheet" href="../css/animate.css">
   <link rel="stylesheet" href="../css/owl.carousel.min.css">
   <link rel="stylesheet" href="../css/owl.theme.default.min.css">
   <link rel="stylesheet" href="../css/magnific-popup.css">
   <link rel="stylesheet" href="../css/custom.css">
   <link rel="stylesheet" href="../css/index.css">
   <link rel="stylesheet" href="../css/service.css">
   <link rel="stylesheet" href="../css/chatbot.css">
   <title>{p['title']}</title>
   <link href="https://fonts.googleapis.com/css2?family=Sora:wght@100;200;300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>
/* Enterprise Mega Menu CSS */
.mega-menu-container {{
    padding: 25px !important; 
    width: 100vw !important; 
    max-width: 1100px !important; 
    left: 50% !important; 
    transform: translateX(-50%) !important;
    border-radius: 12px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
}}
.mega-title {{
    font-size: 13px !important; 
    font-weight: 700 !important; 
    color: #FF2E3E !important; 
    text-transform: uppercase !important; 
    margin-bottom: 20px !important; 
    letter-spacing: 1.5px !important;
}}
.mega-item {{
    display: flex !important; 
    align-items: center !important; 
    gap: 12px !important; 
    padding: 10px 12px !important; 
    border-radius: 8px !important;
    transition: background 0.2s !important;
}}
.mega-item:hover {{
    background-color: #f9fafb !important;
}}
.mega-item i {{
    color: #6b7280;
    width: 20px;
    text-align: center;
    font-size: 18px;
    transition: color 0.2s;
}}
.mega-item:hover i {{
    color: #FF2E3E;
}}
.mega-item span {{
    font-size: 15px !important; 
    font-weight: 500 !important; 
    color: #000000 !important;
}}
@media (max-width: 991px) {{
    .mega-menu-container {{
        width: 100% !important;
        max-width: 100% !important;
        transform: none !important;
        left: 0 !important;
        box-shadow: none !important;
        border: none !important;
        padding: 15px !important;
    }}
}}

.nested-services-menu {{
    padding: 10px; 
    border-radius: 8px; 
    box-shadow: 0 10px 25px rgba(0,0,0,0.1); 
    border: 1px solid #e5e7eb; 
    min-width: 280px; 
    background: #ffffff;
    list-style: none;
    margin: 0;
}}
.dropdown-submenu {{
    position: relative;
    padding: 2px 0;
}}
.dropdown-submenu > .dropdown-menu {{
    top: 0;
    left: 100%;
    margin-top: -5px;
    display: none;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    border: 1px solid #e5e7eb;
    min-width: 260px;
    background: #ffffff;
    padding: 10px;
}}
.dropdown-submenu:hover > .dropdown-menu {{
    display: block;
}}
.nested-item {{
    padding: 10px 15px !important;
    font-weight: 500 !important;
    font-size: 15px !important;
    color: #374151 !important;
    border-radius: 6px;
    transition: all 0.2s;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
}}
.nested-item:hover {{
    background-color: #f9fafb !important;
    color: #000000 !important;
}}
.nested-subitem {{
    padding: 8px 15px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    color: #4b5563 !important;
    border-radius: 6px;
    transition: all 0.2s;
    display: flex !important;
    align-items: center !important;
}}
.nested-subitem:hover {{
    background-color: #f9fafb !important;
    color: #FF2E3E !important;
}}
@media (max-width: 991px) {{
    .dropdown-submenu > .dropdown-menu {{
        display: block;
        position: static;
        box-shadow: none;
        border: none;
        padding-left: 20px;
        margin-top: 5px;
        background: transparent;
    }}
    .nested-item i.fa-angle-right {{ display: none; }}
}}
</style>

<!-- Techtox ENTITY SCHEMA -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": ["Service", "WebPage"],
  "name": "{p['h1']}",
  "provider": {{
    "@type": "Organization",
    "name": "Techtox",
    "url": "https://techtox.com"
  }},
  "description": "{p['meta_desc']}"
}}
</script>

    <!-- FAVICON -->
    <link rel="icon" type="image/png" href="../img/favicon.png">
    <link rel="shortcut icon" href="../img/favicon.ico">
</head>
<body>

   <!-- NAVIGATION -->
   <nav id="navigration" class="navbar fixed-top p-0">
      <div class="container">
         <a class="logo d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo.png" alt="Techtox Logo" style="height: 45px; width: auto;"></a>
         <div class="sidenav">
            <div class="header">
               <a class="logo d-lg-none d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo.png" alt="Techtox Logo" style="height: 45px; width: auto;"></a>
               <a href="#" class="d-lg-none" id="showsidenav"><i class="fa fa-times" style="font-size: 28px; color: #ffffff; cursor: pointer;"></i></a>
            </div>
             <ul class="mb-0 position-relative d-lg-flex align-items-center" id="main-nav-list">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item dropdown active">
                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#servicesDropdown" aria-expanded="false" aria-haspopup="true">Services <i class="fa fa-angle-down"></i></a>

<div id="servicesDropdown" class="dropdown-menus collapse" style="padding:0; border:none; box-shadow:none; background:transparent;">
   <ul class="nested-services-menu">
       
       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fa fa-code" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Development</span>
               <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="../services/web-applications.html"><i class="fal fa-globe" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Web Applications</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/web-based-games.html"><i class="fal fa-gamepad" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Web-Based Games</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/wordpress-solutions.html"><i class="fab fa-wordpress" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> WordPress Solutions</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/shopify-stores.html"><i class="fab fa-shopify" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Shopify Stores</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/desktop-applications.html"><i class="fal fa-desktop" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Desktop Apps</a></li>
           </ul>
       </li>

       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Automation</span>
               <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="../services/lead-crm-automation.html"><i class="fal fa-filter" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Lead & CRM Automation</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/appointment-follow-up-automation.html"><i class="fal fa-calendar-check" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Appointment & Follow-up</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/ai-customer-support.html"><i class="fal fa-headset" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> AI Customer Support</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/business-reporting-dashboards.html"><i class="fal fa-chart-pie" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Reporting & Dashboards</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/api-system-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/ai-voice-workflow-agents.html"><i class="fal fa-robot" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Voice & Workflow Agents</a></li>
           </ul>
       </li>
       
       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fa fa-paint-brush" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Creative</span>
               <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="../services/ui-ux-design.html"><i class="fa fa-mobile-alt" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> UI/UX Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/graphic-design.html"><i class="fa fa-pen-nib" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Graphic Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/video-editing.html"><i class="fa fa-video" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Video Editing</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/social-media-design.html"><i class="fa fa-share-alt" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Social Media Design</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/3d-vfx.html"><i class="fa fa-cube" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> 3D & VFX</a></li>
           </ul>
       </li>

       <li class="dropdown-submenu">
           <a class="dropdown-item nested-item" href="#">
               <span><i class="fa fa-bullhorn" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Marketing</span>
               <i class="fa fa-angle-right" style="color: #9ca3af;"></i>
           </a>
           <ul class="dropdown-menu">
               <li><a class="dropdown-item nested-subitem" href="../services/linkedin-growth.html"><i class="fab fa-linkedin" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> LinkedIn Growth</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/digital-marketing.html"><i class="fa fa-ad" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Digital Marketing</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/email-marketing.html"><i class="fa fa-envelope-open-text" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Email Marketing</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/freelancing-platform-management.html"><i class="fa fa-briefcase" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Platform Management</a></li>
           </ul>
       </li>

       <li><hr class="dropdown-divider" style="margin: 8px 0; border-top: 1px solid #e5e7eb;"></li>
       <li>
           <a class="dropdown-item nested-item" href="../services.html" style="color: #FF2E3E !important; font-weight: 600 !important; justify-content: flex-start !important;">
               <i class="fa fa-arrow-right" style="width:20px; margin-right:8px;"></i> Explore All Services
           </a>
       </li>
   </ul>
</div>

                </li>
                <li class="nav-item dropdown">
                   <a class="nav-link dropdown-toggle" data-toggle="collapse" href="#industriesDropdown" aria-expanded="false" aria-haspopup="true">Industries <i class="fa fa-angle-down"></i></a>
                   <div id="industriesDropdown" class="dropdown-menus collapse" style="padding: 15px; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); border: 1px solid #e5e7eb; min-width: 260px; background: #ffffff;">
                       <a class="dropdown-item" href="../industries/real-estate.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-building" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Real Estate</a>
                       <a class="dropdown-item" href="../industries/b2b-saas.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-cloud" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> B2B SaaS</a>
                       <a class="dropdown-item" href="../industries/ecommerce.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-shopping-cart" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> E-Commerce</a>
                       <a class="dropdown-item" href="../industries/legal.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-balance-scale" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Legal Practices</a>
                       <a class="dropdown-item" href="../industries/healthcare.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-heartbeat" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Healthcare</a>
                       <a class="dropdown-item" href="../industries/financial.html" style="padding: 10px; font-weight: 500; font-size: 15px;"><i class="fa fa-chart-line" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Financial Services</a>
                   </div>
                </li>
                <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="../faq.html">FAQ</a></li>
                <li class="nav-item"><a class="nav-link" href="../contact.html">Contact</a></li>
             </ul>
         </div>
         <a href="../contact.html" class="fv-nav-circle d-none d-md-flex" aria-label="Let's Connect">
            <i class="fa fa-arrow-right arrow-main"></i>
            <i class="fa fa-arrow-right arrow-hover"></i>
         </a>
         <div id="hamburger" class="d-lg-none"><i class="fa fa-bars" style="font-size: 28px; color: #ffffff; cursor: pointer;"></i></div>
      </div>
   </nav>

   <!-- LANDING -->
   <section class="fv-page-hero" style="background-image: linear-gradient(rgba(17, 24, 39, 0.88), rgba(17, 24, 39, 0.95)), url('{p['hero_img']}'); background-size: cover; background-position: center; border-bottom: 1px solid #000000;">
      <div class="container text-center">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">{p['eyebrow']}</span>
         <h1 class="wow fadeInUp" data-wow-delay="0.2s">{p['h1']}</h1>
         <p class="fv-lead wow fadeInUp" data-wow-delay="0.3s">{p['lead']}</p>
         <div class="wow fadeInUp" data-wow-delay="0.4s" style="margin-top: 15px;">
            <span style="display: inline-block; padding: 6px 18px; border-radius: 9999px; background: rgba(255, 46, 62, 0.15); border: 1px solid rgba(255, 46, 62, 0.4); color: #ffffff; font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 500; letter-spacing: 0.5px;">
               {p['tools_badge']}
            </span>
         </div>
      </div>
   </section>

<!-- SHADCN PORTFOLIO GALLERY -->
<section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
    <div class="container">
        <div class="mb-5 d-flex flex-column align-items-start" style="gap: 12px;">
            <div style="display: inline-flex; align-items: center; border-radius: 9999px; background-color: #000000; color: #ffffff; padding: 6px 16px; font-size: 13px; font-weight: 600; font-family: 'Sora', sans-serif; letter-spacing: 1px; text-transform: uppercase;">
                Deliverables
            </div>
            <h2 style="font-family: 'Sora', sans-serif; font-size: 42px; font-weight: 500; color: #000000; letter-spacing: -1.5px; margin: 0; line-height: 1.1;">
                Operational Implementations
            </h2>
            <p style="color: #6b7280; font-size: 18px; font-family: 'Sora', sans-serif; margin: 0; max-width: 650px; line-height: 1.6;">
                Production deployments and workflow architectures built to solve specific operational friction and eliminate manual overhead.
            </p>
        </div>
        
        <div style="display: grid; gap: 32px; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
{showcase_html}        </div>
    </div>
</section>

<!-- SHADCN LIGHT BENTO GRID (FEATURES) -->
<section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important;">
    <div class="container" style="max-width: 1100px;">
        <div class="text-center mb-5 pb-2 mx-auto" style="max-width: 700px;">
            <span style="color: #FF2E3E; font-family: 'Sora', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">INCLUDED IN SCOPE</span>
            <h2 style="font-family: 'Sora', sans-serif; font-size: 42px; font-weight: 500; color: #000000; letter-spacing: -1px; margin-bottom: 20px; line-height: 1.15;">
                Engineered Capabilities
            </h2>
            <p style="color: #6b7280; font-size: 16px; font-family: 'Sora', sans-serif; margin: 0; line-height: 1.6;">
                Everything designed, tested, and integrated when you deploy {p['h1']} across your operations.
            </p>
        </div>

        <style>
            .feature-light-grid {{ display: grid; gap: 24px; grid-template-columns: 1fr; }}
            @media (min-width: 768px) {{ .feature-light-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
            @media (min-width: 1024px) {{ .feature-light-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
            .feature-light-card {{ background: #ffffff; padding: 40px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); transition: box-shadow 0.2s ease, transform 0.2s ease; }}
            .feature-light-card:hover {{ box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); transform: translateY(-2px); }}
            .fl-icon {{ font-size: 24px; color: #FF2E3E; margin-bottom: 20px; }}
            .fl-title {{ font-family: 'Sora', sans-serif; font-size: 18px; font-weight: 600; color: #000000; margin: 0 0 12px 0; letter-spacing: -0.5px; }}
            .fl-desc {{ font-family: 'Sora', sans-serif; color: #6b7280; font-size: 15px; line-height: 1.6; margin: 0; }}
        </style>

        <div class="feature-light-grid">
{features_html}        </div>
    </div>
</section>

<!-- CLOSING CTA (SPLIT) -->
   <section class="fv-cta-split py-5" id="contactArea" style="position: relative; overflow: hidden;">
      <img src="../img/cta_bg_2.webp" alt="Abstract Background" loading="lazy" class="wow fadeIn" data-wow-duration="1.5s" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0;">
      <div style="position:absolute; inset:0; background: linear-gradient(90deg, rgba(17,24,39,0.95) 0%, rgba(17,24,39,0.7) 100%); z-index:0;"></div>
      
      <div class="container" style="position:relative; z-index:1; padding-top: 100px; padding-bottom: 100px;">
         <div class="row align-items-center">
            
            <div class="col-lg-6 mb-5 mb-lg-0 pr-lg-5 wow fadeInLeft" data-wow-delay="0.1s">
               <h2 class="fw-bold mb-4" style="color: #ffffff; font-family: 'Sora', sans-serif; font-size: 56px; line-height: 1.1; letter-spacing: -1px;">
                  Ready to solve operational friction?
               </h2>
               <p style="color: #d1d5db; font-family: 'Sora', sans-serif; font-size: 18px; line-height: 1.6; max-width: 500px; margin-bottom: 40px;">
                  Tell us where your team is losing hours to repetitive work or disconnected software. We will architect a clean, reliable system built specifically for your business.
               </p>
               <a href="../contact.html" class="fv-dual-btn">
                  <span class="fv-btn-pill">REQUEST A WORKFLOW AUDIT</span>
                  <div class="fv-btn-circle">
                     <i class="fa fa-arrow-right arrow-main"></i>
                     <i class="fa fa-arrow-right arrow-hover"></i>
                  </div>
               </a>
            </div>

            <div class="col-lg-5 offset-lg-1 wow fadeInRight" data-wow-delay="0.2s">
               <ul class="cta-check-list list-unstyled m-0">
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif; font-size: 20px; font-weight: 500;">Clear Operational ROI</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif; font-size: 20px; font-weight: 500;">Zero Vendor Lock-in (You Own the System)</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif; font-size: 20px; font-weight: 500;">Robust Error-Handling & Fallbacks</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif; font-size: 20px; font-weight: 500;">Full Team Onboarding & Documentation</span>
                  </li>
                  <li class="d-flex align-items-center">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif; font-size: 20px; font-weight: 500;">Ongoing Proactive Monitoring</span>
                  </li>
               </ul>
            </div>
            
         </div>
      </div>
   </section>

<!-- FOOTER -->
   <footer id="footerSection"><div class="container"><div class="row">
      <div class="col-lg-4 mb-5 mb-lg-0">
         <a class="logo d-flex align-items-center" href="../index.html" style="text-decoration: none;"><img src="../img/logo-dark.png" alt="Techtox Logo" style="height:40px; width: auto; margin-right:12px;"></a>
         <p class="about">Design, build, automate and scale with full-service digital solutions designed around your business.</p>
         <div class="social-links">
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
         </div>
      </div>
      <div class="col-6 col-lg-2 mb-4 mb-lg-0"><div class="footer-box"><p class="title">Company</p><a href="../about.html">About</a><a href="../faq.html">FAQ</a></div></div>
      <div class="col-6 col-lg-3 mb-4 mb-lg-0"><div class="footer-box"><p class="title">Departments</p><a href="../services.html">Development</a><a href="../services.html#automation">Automation</a><a href="../services.html">Creative</a><a href="../services.html">Marketing</a></div></div>
      <div class="col-lg-3"><div class="footer-box"><p class="title">Resources</p><a href="mailto:contact@techtox.com">Email Us</a><a href="../contact.html">Request a Strategy Call</a><a href="#">Islamabad, Pakistan</a><a href="#">Serving globally</a></div></div>
   </div><div class="row mt-5 pt-4 footer-bottom"><div class="col-md-6"><p>&copy; 2026 Techtox. All rights reserved.</p></div><div class="col-md-6 text-md-right"><a href="../terms.html" class="mr-4">Terms and Conditions</a><a href="../privacy.html">Privacy Policy</a></div></div></div></footer>

   <a href="#" class="scroll-up"><i class="fa fa-chevron-up"></i></a>
   <script src="../js/jquery.min.js"></script>
   <script src="../js/bootstrap.min.js"></script>
   <script src="../js/popper.min.js"></script>
   <script src="../js/font-awesome-pro.js"></script>
   <script src="../js/wow.min.js"></script>
   <script src="../js/mixitup.min.js"></script>
   <script src="../js/jquery.magnific-popup.min.js"></script>
   <script src="../js/jquery.counterup.min.js"></script>
   <script src="../js/jquery.waypoints.min.js"></script>
   <script src="../js/owl.carousel.min.js"></script>
   <script src="../js/custom.js"></script>
   <script src="../js/chatbot.js"></script>
</body>
</html>'''

def build_all():
    os.makedirs('services', exist_ok=True)
    for p in PAGES:
        path = os.path.join('services', p['filename'])
        html_content = render_page(p)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Generated: {path}")

if __name__ == '__main__':
    build_all()
