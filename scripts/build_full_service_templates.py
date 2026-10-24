import os

SERVICES_DATA = [
    # -------------------------------------------------------------
    # 1. Lead & CRM Automation
    # -------------------------------------------------------------
    {
        "filename": "lead-crm-automation.html",
        "title": "Lead & CRM Automation | Techtox",
        "meta_desc": "Capture, qualify, route, and track leads while automating CRM updates, instant team notifications, and follow-up reminders.",
        "eyebrow": "OPERATIONAL AUTOMATION",
        "h1": "Lead & CRM Automation",
        "hero_desc": "Capture, qualify, route, and track inbound leads while eliminating manual data entry, accelerating response times, and keeping your CRM perfectly up to date.",
        "hero_img": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("Slow Response Times Cost Deals", "Inquiries sit in form inboxes or email notifications for hours. Research shows 78% of buyers purchase from the business that responds first."),
            ("Reps Waste 10+ Hours on Data Entry", "Sales professionals lose valuable selling time copying contact details, company notes, and deal sizes manually between web forms and the CRM."),
            ("Dropped Leads & Routing Confusion", "Without centralized automated routing, leads get missed, assigned to inactive reps, or contacted by two salespeople simultaneously."),
            ("Pipeline Invisibility & Gaps", "Deal stages, lead source tags, and follow-up notes are entered inconsistently, leaving leadership blind to actual conversion rates and pipeline velocity.")
        ],
        
        "solution": {
            "title": "A Systematic, Resilient Lead Capture & Routing Engine",
            "desc": "We build automated lead intake pipelines that connect directly to your forms, ad campaigns, and landing pages via secure webhooks. The moment a lead arrives, the system validates contact data, assigns the prospect using your exact routing rules, updates your CRM, and alerts your sales rep within seconds."
        },
        
        "outcomes": [
            ("<60s", "Lead Response Time", "Instant automated confirmation to the lead and immediate notification to the assigned sales rep."),
            ("100%", "Data Entry Elimination", "All contact details, custom form answers, and UTM attribution synced directly to your CRM."),
            ("Zero", "Dropped Leads", "Automated failover queues guarantee every lead is captured and assigned even during traffic spikes.")
        ],
        
        "workflow": [
            ("01", "Lead Submission", "Lead submits inquiry on website, Webflow, Typeform, or ad campaign via secure webhook."),
            ("02", "Sanitization & Deduplication", "Validates business email, cleans phone formatting, and checks CRM for existing contact records."),
            ("03", "Intelligent Routing", "Assigns lead to the appropriate rep using round-robin, geography, deal size, or product category logic."),
            ("04", "Two-Way CRM Sync", "Creates or updates contact, company, and deal records in your CRM with complete attribution metadata."),
            ("05", "Instant Alert & Reminders", "Sends structured lead card to rep's Slack or Teams channel and schedules automated follow-up tasks.")
        ],
        
        "capabilities": [
            ("fa fa-filter", "Multi-Source Webhook Ingestion", "Capture leads instantaneously from website forms, custom landing pages, ad networks, and landing page builders."),
            ("fa fa-user-tag", "Custom Routing & Auto-Assignment", "Route leads using round-robin distribution, territory mapping, account tiers, or rep availability rules."),
            ("fa fa-sync-alt", "Bi-Directional CRM Synchronization", "Keep contacts, companies, pipeline stages, and communication histories synchronized in real time."),
            ("fa fa-bell", "Instant Slack & Teams Alerting", "Deliver rich lead cards with direct CRM links to your team chat the second high-priority leads submit."),
            ("fa fa-envelope-open-text", "Automated Follow-Up Cadences", "Deploy immediate personalized email confirmations and automated reminder tasks to ensure sub-5-minute outreach."),
            ("fa fa-shield-check", "Data Hygiene & Deduplication", "Automatically verify email deliverability, enrich company domains, and prevent duplicate contact clutter.")
        ],
        
        "tools": {
            "native": ["HubSpot", "GoHighLevel (GHL)", "Monday.com", "Salesforce", "Pipedrive", "Zoho CRM", "Google Sheets"],
            "custom": ["n8n Middleware", "Make (Integromat)", "Zapier", "REST APIs", "Secure Webhooks", "Slack & MS Teams"]
        },
        
        "portfolio": [
            {
                "title": "B2B SaaS Lead Ingestion & HubSpot Routing",
                "img": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80",
                "problem": "Inbound demo requests sat in Typeform for over 4 hours before manual assignment.",
                "built": "Real-time webhook workflow routing leads to 6 account executives via round-robin with instant Slack alerts.",
                "tools": "HubSpot, Typeform, n8n, Slack Webhooks"
            },
            {
                "title": "High-Ticket Service Agency GoHighLevel Pipeline",
                "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
                "problem": "Meta Ads leads were missing phone numbers and failing to update pipeline stages.",
                "built": "Automated data validation pipeline syncing ad leads directly to GoHighLevel CRM opportunities with instant SMS dispatch.",
                "tools": "GoHighLevel (GHL), Meta Ads API, n8n, Twilio"
            },
            {
                "title": "Consulting Firm Monday.com Opportunity Engine",
                "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
                "problem": "Enterprise inquiries required manual research and manual deal creation on Monday.com boards.",
                "built": "Automated domain enrichment and deal generation workflow linking website forms to Monday.com with automated task reminders.",
                "tools": "Monday.com CRM, Google Sheets, Make, Clearbit API"
            }
        ],
        
        "faqs": [
            ("How long does it take to implement Lead & CRM Automation?", "Standard lead capture and CRM routing pipelines are typically architected, tested, and deployed within 5 to 7 business days."),
            ("Do we have to migrate or replace our existing CRM?", "No. We integrate directly with your current CRM—whether that is HubSpot, GoHighLevel, Monday.com, Salesforce, or Google Sheets."),
            ("What happens if a webhook fails or our CRM API is down?", "Our workflows utilize self-healing retry queues with exponential backoff. If an endpoint is temporarily unreachable, requests are logged in a dead-letter queue and retried automatically with instant alerts sent to your technical team."),
            ("Can we customize the lead assignment rules later?", "Yes. We design modular routing tables so your team can easily update rep names, territory assignments, or round-robin weights without altering code."),
            ("Who owns the workflows and integrations once built?", "You own 100% of the workflows, credentials, and documentation. We build in client-owned accounts with zero vendor lock-in.")
        ]
    },

    # -------------------------------------------------------------
    # 2. Appointment & Follow-up Automation
    # -------------------------------------------------------------
    {
        "filename": "appointment-follow-up-automation.html",
        "title": "Appointment & Follow-up Automation | Techtox",
        "meta_desc": "Automate bookings, confirmations, multi-channel reminders, cancellations, and missed-appointment follow-ups.",
        "eyebrow": "CALENDAR & BOOKING SYSTEMS",
        "h1": "Appointment & Follow-up Automation",
        "hero_desc": "Automate booking triggers, branded calendar invites, multi-channel reminders, seamless rescheduling, and automated missed-appointment recovery.",
        "hero_img": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("High No-Show Rates Drain Revenue", "Without timely, sequenced multi-channel reminders, up to 30% of scheduled consultation calls fail to show up."),
            ("Back-and-Forth Availability Emails", "Trading emails to find a mutual meeting time creates friction and causes warm prospects to lose interest."),
            ("Zero Automated Recovery on Missed Calls", "When a prospect misses an appointment, reps rarely send timely follow-up messages, permanently losing pipeline revenue."),
            ("Disconnected CRM & Calendar Records", "Completed, cancelled, or rescheduled appointments are not reflected in your sales pipeline without manual data entry.")
        ],
        
        "solution": {
            "title": "Frictionless Scheduling and Multi-Channel Attendance Protection",
            "desc": "We integrate your booking platforms directly into your CRM and communication channels. Clients book instantly with automated timezone conversion, receive branded invites with dynamic video conference links, get sequenced SMS and email reminders, and trigger automated recovery cadences if an appointment is missed."
        },
        
        "outcomes": [
            ("<5%", "Average No-Show Rate", "Sequenced 24-hour, 2-hour, and 15-minute SMS & email reminders keep attendance exceptionally high."),
            ("100%", "Calendar Synchronization", "Dynamic video links (Zoom / Google Meet) and buffer rules prevent scheduling conflicts."),
            ("Automated", "No-Show Re-Engagement", "Immediate empathetic follow-up sequences reclaim lost consultation opportunities.")
        ],
        
        "workflow": [
            ("01", "Booking Trigger", "Prospect selects an open slot on Calendly, Cal.com, or your embedded custom scheduler."),
            ("02", "Instant Confirmation", "Calendar invite with dynamic Zoom or Google Meet link and custom prep brief is generated."),
            ("03", "Sequenced Reminders", "Delivers personalized SMS and email reminders 24 hours, 2 hours, and 15 minutes prior to the call."),
            ("04", "Outcome Tagging", "Host marks call as completed, rescheduled, or no-show; CRM stage updates automatically."),
            ("05", "Post-Call / Recovery", "Triggers immediate post-call resource email or launches polite automated re-booking cadence for no-shows.")
        ],
        
        "capabilities": [
            ("fa fa-calendar-check", "Direct Calendar Synchronization", "Bi-directional integration with Google Calendar, Outlook, Calendly, and Cal.com with timezone handling."),
            ("fa fa-video", "Dynamic Video Link Generation", "Automatically generates unique Zoom or Google Meet links inside the calendar invite with prep materials."),
            ("fa fa-sms", "Multi-Channel Timed Reminders", "Deliver sequenced SMS, WhatsApp, and email reminders at custom intervals to maximize attendance."),
            ("fa fa-calendar-alt", "One-Click Self-Service Rescheduling", "Allow clients to reschedule seamlessly with auto-cancellation of prior slots and instant host alerts."),
            ("fa fa-history", "Missed-Appointment Recovery Sequences", "Automatically trigger polite re-booking sequences when an appointment is flagged as a no-show."),
            ("fa fa-user-clock", "Host Pre-Call Briefing Notifications", "Send sales reps a Slack briefing 10 minutes before the call with prospect answers and CRM history.")
        ],
        
        "tools": {
            "native": ["Calendly", "Google Calendar", "GoHighLevel (GHL)", "HubSpot", "Monday.com", "Cal.com"],
            "custom": ["Twilio SMS", "n8n", "Make", "SendGrid", "Zoom API", "Google Meet API", "Slack Alerts"]
        },
        
        "portfolio": [
            {
                "title": "B2B Sales Agency Calendly-to-HubSpot Engine",
                "img": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=800&q=80",
                "problem": "Consultants experienced a 28% no-show rate and lost hours manually rescheduling missed prospects.",
                "built": "Automated 3-tier SMS reminder workflow with instant Zoom link generation and automated 3-day recovery cadence.",
                "tools": "Calendly, HubSpot, n8n, Twilio SMS, Zoom"
            },
            {
                "title": "Private Medical & Wellness Clinic Booking Suite",
                "img": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=800&q=80",
                "problem": "Patients booked appointments but frequently forgot dates, causing expensive practitioner downtime.",
                "built": "Google Calendar sync with GoHighLevel sending 2-way SMS confirmation prompts and automated cancellation handling.",
                "tools": "Google Calendar, GoHighLevel (GHL), Twilio, Webhooks"
            },
            {
                "title": "Financial Advisory Consultation Scheduling",
                "img": "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=800&q=80",
                "problem": "Advisors spent 30 minutes before each meeting finding client background notes across multiple spreadsheets.",
                "built": "Automated pre-meeting Slack dossier delivered to advisor 15 minutes before call with client financial questionnaire data.",
                "tools": "Monday.com, Calendly, Slack API, Google Workspace"
            }
        ],
        
        "faqs": [
            ("How do reminders prevent no-shows without annoying clients?", "We structure reminders thoughtfully: a confirmation immediately upon booking, an agenda reminder 24 hours prior, and a quick text with the video link 15 minutes before."),
            ("Can prospects reschedule easily without staff involvement?", "Yes. Every invite includes a secure one-click reschedule link that frees up the old calendar slot and updates your CRM automatically."),
            ("Does this work across different time zones?", "Yes. The system automatically detects the client's local time zone, converts calendar times accurately, and delivers reminders at appropriate local hours."),
            ("What messaging channels are supported for reminders?", "We support SMS (via Twilio), email (via SendGrid/Google Workspace), and WhatsApp (via approved Meta business APIs)."),
            ("Can we prevent double bookings across multiple team calendars?", "Yes. We configure calendar pooling and check busy times across multiple team calendars before offering availability.")
        ]
    },

    # -------------------------------------------------------------
    # 3. AI Customer Support
    # -------------------------------------------------------------
    {
        "filename": "ai-customer-support.html",
        "title": "AI Customer Support | Techtox",
        "meta_desc": "Answer approved questions, retrieve information from a business knowledge base, collect customer details, and escalate complex requests.",
        "eyebrow": "INTELLIGENT SUPPORT INFRASTRUCTURE",
        "h1": "AI Customer Support",
        "hero_desc": "Answer common customer inquiries instantly using verified company information, collect essential customer details, and seamlessly transfer complex requests to human staff.",
        "hero_img": "https://images.unsplash.com/photo-1534536281715-e28d76689b4d?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("Slow First-Response Times", "Customers wait hours or days for basic answers regarding order status, pricing tiers, or standard documentation links."),
            ("High Support Costs on Repetitive Tickets", "Support staff spend 70% of their workday answering the exact same 15 questions instead of solving complex customer problems."),
            ("Lost Leads from After-Hours Visitors", "Website visitors seeking pricing or service details outside regular business hours leave without engaging when no one is available to answer."),
            ("Fear of Uncontrolled AI Hallucinations", "Businesses avoid AI support because generic chatbots invent false policies, inaccurate discounts, or misleading commitments.")
        ],
        
        "solution": {
            "title": "Strictly Grounded, Guardrailed Support Automation",
            "desc": "We deploy customer support agents trained strictly on your approved documentation, product specs, and operational FAQs. They provide sub-second responses 24/7, gather customer identifiers, create organized helpdesk tickets, and route complex or sensitive questions to your human team with full conversational context."
        },
        
        "outcomes": [
            ("60-80%", "Routine Ticket Deflection", "Common questions resolved instantly without requiring human agent time."),
            ("<1s", "Response Latency", "Instant customer assistance across website chat, portals, and helpdesks 24/7."),
            ("Zero", "Unsupported Hallucinations", "Strict anti-hallucination guardrails that cite only approved company documentation.")
        ],
        
        "workflow": [
            ("01", "Inquiry Ingestion", "Customer asks a question via website chat widget, portal, or support email."),
            ("02", "Knowledge Retrieval (RAG)", "Semantic search queries approved company documentation, FAQs, and policy records."),
            ("03", "Grounded Response", "Generates a clear, friendly answer referencing only verified company information."),
            ("04", "Customer Intake", "Collects customer email, order number, and specific issue details if action is required."),
            ("05", "Human Escalation & Ticket", "Creates formatted ticket in Zendesk, Freshdesk, or HubSpot and alerts live agents if necessary.")
        ],
        
        "capabilities": [
            ("fa fa-book-open", "Grounded Knowledge Base Ingestion", "Trained exclusively on your approved knowledge base, FAQs, refund policies, and product documentation."),
            ("fa fa-address-card", "Automated Customer Detail Intake", "Collect customer identifiers, account emails, order IDs, and categorized problem summaries."),
            ("fal fa-headset", "Sub-Second 24/7 Question Resolution", "Resolve high-volume routine inquiries instantly without customer queues or off-hours delays."),
            ("fa fa-user-friends", "Seamless Live Human Hand-Off", "Detect customer frustration, billing disputes, or non-standard queries and route immediately to staff."),
            ("fa fa-ticket-alt", "Automated CRM & Ticket Generation", "Log complete transcripts, intent categorization, and actionable summaries directly into your helpdesk."),
            ("fal fa-chart-pie", "Support Sentiment & Resolution Analytics", "Track customer inquiry volume, resolution rates, escalation triggers, and documentation gaps.")
        ],
        
        "tools": {
            "native": ["HubSpot Service Hub", "Zendesk", "Freshdesk", "GoHighLevel (GHL)", "Intercom"],
            "custom": ["OpenAI API (GPT-4o)", "Pinecone Vector DB", "n8n", "Make", "Slack API", "Custom Chat Widget"]
        },
        
        "portfolio": [
            {
                "title": "SaaS Platform 24/7 Documentation Assistant",
                "img": "https://images.unsplash.com/photo-1534536281715-e28d76689b4d?auto=format&fit=crop&w=800&q=80",
                "problem": "Software users waited an average of 4 hours for simple API documentation references and billing inquiries.",
                "built": "Embedded chat assistant answering from verified docs, deflecting 68% of tier-1 support tickets and logging bugs to Slack.",
                "tools": "OpenAI API, Pinecone, Zendesk, n8n"
            },
            {
                "title": "E-Commerce Customer Intake & Order Lookup Bot",
                "img": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80",
                "problem": "Retail store received hundreds of daily requests asking for shipping policies and return window guidelines.",
                "built": "Grounded AI support widget resolving return questions and gathering order numbers before creating Zendesk tickets.",
                "tools": "Shopify API, Zendesk, Make, OpenAI API"
            },
            {
                "title": "Professional Services Pre-Qualification Chat",
                "img": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=800&q=80",
                "problem": "After-hours website visitors left without providing contact information or project scope details.",
                "built": "HubSpot-connected chat assistant providing service overviews, capturing prospect emails, and booking consultation calls.",
                "tools": "HubSpot CRM, Calendly, n8n, OpenAI API"
            }
        ],
        
        "faqs": [
            ("How do you guarantee the AI will not hallucinate or make false promises?", "We configure strict retrieval-augmented generation (RAG) prompts that instruct the model to answer solely from your approved knowledge base. If an inquiry falls outside the documentation, the AI politely offers to route to human staff."),
            ("How easily can we update our business information?", "You maintain complete control over the knowledge source (such as a Google Doc, Notion workspace, or FAQ database). When you edit policies, the agent updates automatically."),
            ("Which chat widgets or platforms are supported?", "We can deploy lightweight chat widgets directly into your website (Webflow, WordPress, custom HTML) or integrate into Zendesk, Freshdesk, and Intercom."),
            ("What happens when a customer requests a human?", "The agent recognizes handoff keywords or frustrated sentiment and immediately prompts for customer contact details, creates an urgent helpdesk ticket, and notifies your team via Slack."),
            ("Is customer conversation data kept private and secure?", "Yes. We configure enterprise API endpoints with zero-data-retention agreements so your company documentation and customer chats are never used to train public models.")
        ]
    },

    # -------------------------------------------------------------
    # 4. Business Reporting & Dashboards
    # -------------------------------------------------------------
    {
        "filename": "custom-dashboards.html",
        "title": "Business Reporting & Dashboards | Techtox",
        "meta_desc": "Consolidate operational data, visualize KPIs, schedule reports, and trigger threshold alerts.",
        "eyebrow": "OPERATIONAL INTELLIGENCE",
        "h1": "Business Reporting & Dashboards",
        "hero_desc": "Consolidate siloed business data, visualize core KPIs in real-time dashboards, automate scheduled executive reports, and trigger alerts when vital thresholds are breached.",
        "hero_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("Data Trapped in Siloed Software", "Revenue is in Stripe, pipeline is in HubSpot, ad spend is in Meta/Google, and operations are locked in disconnected spreadsheets."),
            ("Hours Wasted on Weekly Manual Reporting", "Founders and managers spend hours every Monday copy-pasting numbers into slides and sheets instead of executing strategy."),
            ("Lagging Visibility on Critical Metrics", "Leadership discovers that CAC jumped or revenue dropped weeks after the fact because reporting is retrospective rather than live."),
            ("Formula Errors & Conflicting Definitions", "Different departments calculate churn, margin, or customer acquisition costs differently, leading to conflicting data and decision paralysis.")
        ],
        
        "solution": {
            "title": "A Single Source of Truth for Executive Decision-Making",
            "desc": "We engineer automated data aggregation pipelines that pull metrics from your revenue, marketing, CRM, and operational tools into clean, standardized databases. We build interactive Looker Studio dashboards, automate daily or weekly executive digest summaries delivered to Slack or email, and configure threshold alert triggers for vital KPIs."
        },
        
        "outcomes": [
            ("Zero", "Hours on Manual Reports", "Automated daily, weekly, and monthly digest summaries delivered directly to executives."),
            ("100%", "Single Source of Truth", "Unified KPI calculations agreed upon and synced across all business tools."),
            ("Real-Time", "Threshold Anomaly Alerts", "Instant Slack or SMS pings the moment ad spend spikes, revenue dips, or target metrics are hit.")
        ],
        
        "workflow": [
            ("01", "Automated Extraction", "Scheduled API pipelines pull daily transactional, marketing, and CRM data from your platforms."),
            ("02", "Hygiene & Normalization", "Cleans raw payloads, reconciles currency exchange, eliminates duplicates, and structures records."),
            ("03", "KPI Calculation", "Computes blended CAC, LTV, pipeline velocity, net revenue, and operational throughput automatically."),
            ("04", "Visual Dashboard Sync", "Populates interactive Looker Studio, Google Sheets, or custom dashboard charts in real time."),
            ("05", "Digest Delivery & Alerts", "Dispatches morning executive digests to Slack and triggers instant alerts if thresholds are breached.")
        ],
        
        "capabilities": [
            ("fa fa-layer-group", "Multi-Platform Data Aggregation", "Extract and merge metrics from Stripe, Shopify, HubSpot, GoHighLevel, Google Ads, and Meta Ads."),
            ("fa fa-chart-line", "Interactive Looker Studio Dashboards", "High-clarity visual dashboards built for leadership to inspect trends, filter date ranges, and evaluate performance."),
            ("fa fa-paper-plane", "Automated Scheduled Digest Reports", "Deliver formatted executive summaries directly to company Slack channels or leadership inboxes automatically."),
            ("fa fa-exclamation-triangle", "Anomaly & Threshold Alerting", "Set automated triggers that notify owners immediately if revenue drops, ad CAC breaches targets, or errors occur."),
            ("fa fa-table", "Live Google Sheets Formula Sync", "Keep financial and operational spreadsheet models updated with clean, formulas-ready data pipelines."),
            ("fa fa-check-double", "Automated Data Hygiene & Reconciliation", "Continuous background verification that flags missing entries and reconciles cross-platform financial discrepancies.")
        ],
        
        "tools": {
            "native": ["Google Sheets", "Looker Studio", "HubSpot", "GoHighLevel (GHL)", "Monday.com", "Stripe", "Shopify"],
            "custom": ["n8n Middleware", "Google Ads API", "Meta Ads API", "PostgreSQL", "REST APIs", "Slack Webhooks"]
        },
        
        "portfolio": [
            {
                "title": "Executive Agency Operations & Billing Dashboard",
                "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
                "problem": "Agency leadership lacked a unified view of client retainer revenue, billable hours, and team throughput.",
                "built": "Consolidated Looker Studio dashboard pulling Stripe billings and Monday.com task tracking with automated Monday morning digest.",
                "tools": "Looker Studio, Stripe API, Monday.com, n8n"
            },
            {
                "title": "E-Commerce Multi-Brand Financial & Ad Spend Model",
                "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
                "problem": "E-commerce founder spent 6 hours every weekend pulling sales from Shopify, Amazon, and ad costs from Meta.",
                "built": "Automated data pipeline calculating true blended ROAS and net margins in live Google Sheets and Looker Studio.",
                "tools": "Google Sheets, Shopify API, Meta Ads API, Make"
            },
            {
                "title": "B2B Sales Pipeline Velocity & Rep Throughput Tracker",
                "img": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=800&q=80",
                "problem": "Sales director could not identify which stage of the sales cycle was causing deals to stall.",
                "built": "HubSpot-to-Looker Studio pipeline tracking time-in-stage, rep activity ratios, and projected cash collection.",
                "tools": "HubSpot CRM, Looker Studio, n8n, Slack Alerts"
            }
        ],
        
        "faqs": [
            ("How frequently does the dashboard data update?", "We can configure updates in real-time via webhooks, hourly, or once daily depending on your API rate limits and business reporting requirements."),
            ("Do we have to purchase expensive enterprise BI software?", "No. We build primarily on Looker Studio and Google Sheets, which have zero recurring platform software licensing fees for your business."),
            ("Can we customize which team members have access to sensitive financial metrics?", "Yes. We implement granular role-based permissions so executives can view full margins while department heads see only operational KPIs."),
            ("What happens if a third-party platform updates its API?", "Our data pipelines are built with schema validation and error logging. If an upstream field changes, our monitoring system alerts us immediately for seamless maintenance."),
            ("Can we export the data into our own models or accounting tools?", "Yes. All aggregated data is stored in clean tabular formats that can be exported or queried anytime.")
        ]
    },

    # -------------------------------------------------------------
    # 5. API & Software Integration
    # -------------------------------------------------------------
    {
        "filename": "api-software-integration.html",
        "title": "API & Software Integration | Techtox",
        "meta_desc": "Connect business applications through APIs, webhooks, and reliable data synchronization.",
        "eyebrow": "CUSTOM ARCHITECTURE & INTEGRATION",
        "h1": "API & Software Integration",
        "hero_desc": "Connect websites, CRMs, forms, spreadsheets, and business applications through resilient API pipelines, event webhooks, and error-tolerant data synchronization.",
        "hero_img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("Disconnected Software Silos", "Your tools don't talk to each other. Information captured in your website or billing platform never flows into your CRM or operations."),
            ("Manual, Error-Prone Copy-Pasting", "Employees spend hours daily re-typing customer info, invoices, order numbers, and project files between disparate tools."),
            ("Silent Native Integration Breakages", "Basic out-of-the-box native integrations disconnect without warning, leaving teams unaware that vital data was lost."),
            ("Inflexible Data Mapping & Logic", "Standard native connectors cannot handle custom fields, complex formatting, conditional routing, or multi-step business logic.")
        ],
        
        "solution": {
            "title": "Custom, Resilient Data Bridges Engineered for Your Operations",
            "desc": "We architect robust custom integrations using REST APIs, webhooks, JavaScript data transformation, and dedicated middleware. We connect your software with customized business logic, automated retry queues, full execution logging, and zero data loss."
        },
        
        "outcomes": [
            ("100%", "Manual Re-Entry Elimination", "Automatic background synchronization of contacts, orders, invoices, and records."),
            ("Zero", "Data Loss Resilience", "Self-healing exponential backoff retry queues prevent lost payloads during server outages."),
            ("Custom", "Data Transformation Logic", "Custom field formatting, conditional mapping, and data sanitization tailored to your exact workflows.")
        ],
        
        "workflow": [
            ("01", "Event Detection", "Webhook or scheduled API trigger detects an event (new contract, invoice paid, record updated) in the source tool."),
            ("02", "Payload Validation", "Verifies authentication signature and validates payload schema completeness."),
            ("03", "Data Transformation", "Executes custom JavaScript mapping to sanitize fields, format dates, and harmonize identifiers."),
            ("04", "Destination Sync", "Securely transmits processed payload to destination platform via authenticated API call."),
            ("05", "Audit Logging & Retries", "Stores execution log and automatically retries with exponential backoff if destination responds with an error.")
        ],
        
        "capabilities": [
            ("fal fa-plug", "Custom REST & GraphQL Pipelines", "Connect modern web applications, cloud tools, and proprietary internal databases with tailored endpoints."),
            ("fa fa-clone", "Complete Duplicate Data Elimination", "Eradicate manual copy-pasting between websites, billing portals, inventory systems, and operational boards."),
            ("fa fa-network-wired", "Real-Time Event Webhook Routing", "Trigger immediate downstream operational actions the second an event occurs in any business application."),
            ("fab fa-js", "Custom JavaScript Data Transformation", "Clean, format, and translate data structures seamlessly between incompatible third-party software formats."),
            ("fa fa-shield-alt", "Self-Healing Retry Queues & Dead-Letters", "Prevent dropped data during third-party downtimes with automatic exponential retries and dead-letter monitoring."),
            ("fa fa-key", "Enterprise OAuth & Token Management", "Secure all integration endpoints using encrypted tokens, API key rotation, and role-based access protocols.")
        ],
        
        "tools": {
            "native": ["HubSpot", "GoHighLevel (GHL)", "Monday.com", "Salesforce", "Stripe", "QuickBooks", "Google Workspace"],
            "custom": ["n8n Middleware", "Make", "Zapier", "REST APIs", "Webhooks", "PostgreSQL", "Node.js / JavaScript"]
        },
        
        "portfolio": [
            {
                "title": "CRM-to-Billing & Accounting Synchronization",
                "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80",
                "problem": "Won deals in HubSpot required manual invoice creation in Stripe and duplicate ledger entry in QuickBooks.",
                "built": "Real-time webhook integration automatically generating Stripe invoices upon deal close and logging ledger records.",
                "tools": "HubSpot CRM, Stripe API, QuickBooks API, n8n"
            },
            {
                "title": "Multi-Platform E-Commerce & Warehouse Inventory Sync",
                "img": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&q=80",
                "problem": "Shopify stock counts were out of sync with third-party logistics warehouse software, causing overselling.",
                "built": "Bi-directional inventory sync script with error queuing that reconciles stock levels every 10 minutes.",
                "tools": "Shopify API, 3PL REST API, n8n, PostgreSQL"
            },
            {
                "title": "Project Management & Client Portal Live Feed",
                "img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80",
                "problem": "Agency team managed tasks in Monday.com but had to manually email progress updates to enterprise clients.",
                "built": "Custom webhook pipeline reflecting Monday.com status changes directly to client-facing portal dashboards.",
                "tools": "Monday.com API, Webhooks, Google Cloud, Node.js"
            }
        ],
        
        "faqs": [
            ("Can you connect proprietary or legacy software with modern cloud tools?", "Yes. As long as your software provides an accessible API, database connection, webhook, or export protocol, we can engineer custom bridges."),
            ("How do you handle API rate limits and throttling?", "We build rate-limiting and queuing logic into the middleware to ensure requests never exceed third-party provider limits."),
            ("What happens if a connected third-party service experiences downtime?", "Our workflows log failed attempts and execute automated retries with exponential backoff until the service returns online, alerting your team if issues persist."),
            ("Are our company credentials and customer records secure?", "Yes. We utilize environment-level secret encryption and OAuth 2.0 authentication. We never hard-code credentials."),
            ("Who maintains the integrations if third-party APIs update?", "We provide comprehensive documentation and handover, along with proactive ongoing maintenance and monitoring packages.")
        ]
    },

    # -------------------------------------------------------------
    # 6. AI Voice & Workflow Agents
    # -------------------------------------------------------------
    {
        "filename": "ai-voice-workflow-agents.html",
        "title": "AI Voice & Workflow Agents | Techtox",
        "meta_desc": "Build narrowly scoped voice and task agents that handle approved enquiries, execute defined actions, and escalate exceptions.",
        "eyebrow": "NARROWLY SCOPED AGENTS",
        "h1": "AI Voice & Workflow Agents",
        "hero_desc": "Build narrowly scoped, low-latency voice and workflow agents that handle approved customer inquiries, collect caller information, book calendar slots, and escalate exceptions.",
        "hero_img": "https://images.unsplash.com/photo-1590650516494-0c8e4a4dd67e?auto=format&fit=crop&w=1920&q=80",
        "demo_video_url": "https://www.youtube.com/watch?v=LXb3EKWsInQ",
        
        "problems": [
            ("Missed Inbound Phone Calls & Leads", "Over 60% of incoming phone calls to service businesses go unanswered during peak hours or after business hours, losing qualified buyers."),
            ("Staff Burdened by Routine Phone Calls", "Front-desk and sales staff lose hours answering identical questions regarding service areas, hours, appointment availability, and pricing."),
            ("Unrecorded Phone Details in the CRM", "Valuable information discussed verbally on calls never gets logged in the CRM, resulting in missed follow-ups and lost context."),
            ("Robotic, High-Latency Voice Bots", "Traditional automated phone menus and generic voice bots sound unnatural, interrupt callers, and create customer frustration.")
        ],
        
        "solution": {
            "title": "Ultra-Low Latency, Purpose-Built Voice Agents",
            "desc": "We build narrowly scoped voice and task agents powered by dedicated low-latency voice platforms (Vapi / Retell AI). They are constrained strictly to approved conversational paths: answering routine questions, gathering caller details, booking appointments on live calendars, updating your CRM, and executing warm transfers to live human staff."
        },
        
        "outcomes": [
            ("100%", "Inbound Call Answer Rate", "Zero missed calls, operational 24 hours a day, 7 days a week, 365 days a year."),
            ("<600ms", "Conversational Latency", "Human-like conversational flow without awkward robotic pauses or unnatural interruptions."),
            ("Instant", "CRM Audio & Transcripts", "Complete audio recordings, transcript summaries, and caller details logged automatically.")
        ],
        
        "workflow": [
            ("01", "Call Ingestion", "Caller dials business phone number; voice agent answers immediately with approved greeting."),
            ("02", "Intent Recognition", "Sub-second speech-to-text and intent parsing identifies caller's specific inquiry."),
            ("03", "Information Gathering", "Collects caller name, phone number, address, and inquiry details with phonetic confirmation."),
            ("04", "Action Execution", "Queries live calendar availability to book appointment or updates CRM deal stage via n8n."),
            ("05", "Warm Transfer & Post-Call", "Transfers call to live human staff if requested and dispatches SMS confirmation to caller.")
        ],
        
        "capabilities": [
            ("fal fa-headset", "Ultra-Low Latency Conversational Voice", "Deploy voice bots powered by Vapi or Retell AI with sub-600ms response latency for natural conversations."),
            ("fa fa-shield-alt", "Strict Approved Scripts & Guardrails", "Enforce strict boundaries so agents only answer approved business FAQs and never improvise false commitments."),
            ("fa fa-user-edit", "Structured Caller Data Collection", "Accurately capture caller names, phone numbers, service addresses, and inquiry details with verbal confirmation."),
            ("fa fa-database", "Direct CRM & Calendar Action Execution", "Book appointment slots directly in Calendly or Google Calendar and update contact records in your CRM in real time."),
            ("fa fa-phone-volume", "Instant Warm Transfer to Live Staff", "Detect caller requests for human assistance and execute an immediate warm transfer to available team members."),
            ("fal fa-robot", "Post-Call Workflow Execution", "Automatically trigger follow-up SMS confirmations, email intake forms, and assign CRM follow-up tasks.")
        ],
        
        "tools": {
            "native": ["GoHighLevel (GHL)", "HubSpot", "Monday.com", "Google Calendar", "Calendly"],
            "custom": ["Vapi", "Retell AI", "Twilio Voice", "OpenAI API", "Deepgram", "n8n", "Make"]
        },
        
        "portfolio": [
            {
                "title": "After-Hours Inbound Service Booking Agent",
                "img": "https://images.unsplash.com/photo-1590650516494-0c8e4a4dd67e?auto=format&fit=crop&w=800&q=80",
                "problem": "Home service contractor missed 40+ after-hours calls weekly, representing thousands in lost estimates.",
                "built": "Vapi voice agent answering 24/7, answering service area FAQs, and booking morning estimates in Google Calendar.",
                "tools": "Vapi, Twilio Voice, Google Calendar, n8n"
            },
            {
                "title": "Private Practice Clinic Inbound Patient Triage",
                "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
                "problem": "Clinic reception was overwhelmed by repetitive calls asking for appointment availability and directions.",
                "built": "Retell AI voice bot handling routine triage, collecting patient contact info, and routing complex calls to staff.",
                "tools": "Retell AI, GoHighLevel (GHL), Twilio, Webhooks"
            },
            {
                "title": "Commercial Real Estate Lead Qualification Agent",
                "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80",
                "problem": "Brokers were tied up answering tire-kicker calls on property listing signs during client meetings.",
                "built": "Voice agent qualifying caller budget and square footage requirements before patching qualified buyers to senior brokers.",
                "tools": "Vapi, HubSpot CRM, Twilio, Zapier"
            }
        ],
        
        "faqs": [
            ("Does the voice bot sound robotic or pause awkwardly?", "No. By pairing specialized voice engines (Vapi / Retell AI) with ultra-fast LLM infrastructure and low-latency speech pipelines, the agent achieves human-like sub-600ms latency without awkward pauses."),
            ("What happens if a caller asks to speak with a human?", "The agent immediately respects the request and executes a live warm phone transfer to your designated office or mobile phone number."),
            ("How are recording consent and regulatory disclosures handled?", "We configure automated compliance greetings at the start of the call informing the caller that the conversation is recorded, compliant with state and federal regulations."),
            ("Can the voice agent book appointments on our live calendar?", "Yes. The agent queries your live calendar API during the call, proposes open slots, and confirms the booking on the spot."),
            ("What are the ongoing voice call operating costs?", "Voice platforms typically charge transparent pay-as-you-go per-minute rates (typically $0.08 to $0.14 per minute). You hold direct account ownership with zero agency markups.")
        ]
    }
]

def render_detail_page(s):
    # 02 Problems HTML with WOW animation
    problems_html = ""
    for i, (title, desc) in enumerate(s["problems"]):
        delay = f"{0.1 * (i+1):.1f}s"
        problems_html += f'''            <div class="problem-card wow fadeInUp" data-wow-delay="{delay}">
               <div class="problem-badge"><i class="fa fa-exclamation-circle"></i> Operational Friction</div>
               <h3 class="problem-title">{title}</h3>
               <p class="problem-desc">{desc}</p>
            </div>\n'''

    # 04 Outcomes HTML with WOW animation & Sora typography
    outcomes_html = ""
    for i, (stat, title, desc) in enumerate(s["outcomes"]):
        delay = f"{0.1 * (i+1):.1f}s"
        outcomes_html += f'''            <div class="outcome-card wow fadeInUp" data-wow-delay="{delay}">
               <div class="outcome-stat">{stat}</div>
               <h4 class="outcome-title">{title}</h4>
               <p class="outcome-desc">{desc}</p>
            </div>\n'''

    # 05 Workflow HTML with WOW animation & Sora typography
    workflow_html = ""
    for i, (step_num, title, desc) in enumerate(s["workflow"]):
        delay = f"{0.08 * (i+1):.2f}s"
        workflow_html += f'''            <div class="workflow-step-card wow fadeInUp" data-wow-delay="{delay}">
               <div class="workflow-step-num">{step_num}</div>
               <h4 class="workflow-step-title">{title}</h4>
               <p class="workflow-step-desc">{desc}</p>
            </div>\n'''

    # 06 Capabilities HTML with WOW animation & Sora typography
    capabilities_html = ""
    for i, (icon, title, desc) in enumerate(s["capabilities"]):
        delay = f"{0.1 * ((i%3)+1):.1f}s"
        capabilities_html += f'''            <div class="feature-light-card wow fadeInUp" data-wow-delay="{delay}">
                <div class="fl-icon"><i class="{icon}"></i></div>
                <h3 class="fl-title">{title}</h3>
                <p class="fl-desc">{desc}</p>
            </div>\n'''

    # 07 Tools HTML (Native vs Custom)
    native_tools_pills = "".join([f'<span class="tool-tag tool-tag-native"><i class="fa fa-check-circle" style="color: #10b981; margin-right: 6px;"></i> {t}</span>' for t in s["tools"]["native"]])
    custom_tools_pills = "".join([f'<span class="tool-tag tool-tag-custom"><i class="fa fa-code-branch" style="color: #FF2E3E; margin-right: 6px;"></i> {t}</span>' for t in s["tools"]["custom"]])

    # 08 Portfolio HTML with WOW animation
    portfolio_html = ""
    for i, p in enumerate(s["portfolio"]):
        delay = f"{0.15 * (i+1):.2f}s"
        portfolio_html += f'''            <div class="portfolio-item-card wow fadeInUp" data-wow-delay="{delay}">
               <div class="portfolio-item-img-wrap">
                  <img src="{p['img']}" alt="{p['title']}" loading="lazy">
               </div>
               <div class="portfolio-item-body">
                  <h3 class="portfolio-item-title">{p['title']}</h3>
                  <div class="portfolio-meta-row">
                     <span class="portfolio-meta-label">Problem:</span>
                     <span class="portfolio-meta-val">{p['problem']}</span>
                  </div>
                  <div class="portfolio-meta-row">
                     <span class="portfolio-meta-label">Built:</span>
                     <span class="portfolio-meta-val">{p['built']}</span>
                  </div>
                  <div class="portfolio-meta-row">
                     <span class="portfolio-meta-label">Platforms:</span>
                     <span class="portfolio-meta-val" style="color: #FF2E3E; font-weight: 600;">{p['tools']}</span>
                  </div>
               </div>
            </div>\n'''

    # 12 FAQs HTML using the website's EXACT native .fv-faq-modern-accordion classes
    faqs_html = ""
    for i, (q, a) in enumerate(s["faqs"]):
        delay = f"{0.05 * (i+1):.2f}s"
        faqs_html += f'''            <div class="fv-faq-item fv-faq-modern-item wow fadeInUp" data-wow-delay="{delay}">
               <div class="fv-faq-header fv-faq-modern-header">
                  <h3>{q}</h3>
                  <i class="fa fa-chevron-down"></i>
               </div>
               <div class="fv-faq-content fv-faq-modern-content">
                  <p>{a}</p>
               </div>
            </div>\n'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <meta http-equiv="X-UA-Compatible" content="ie=edge">
   <meta name="description" content="{s['meta_desc']}">
   <link rel="shortcut icon" href="../img/softoweb.png">
   <link rel="preconnect" href="https://fonts.gstatic.com">
   <!-- TECHTOX BRAND GUIDELINES TYPOGRAPHY: SORA ACROSS ALL WEIGHTS (100 to 800) -->
   <link href="https://fonts.googleapis.com/css2?family=Sora:wght@100;200;300;400;500;600;700;800&display=swap" rel="stylesheet">
   <link rel="stylesheet" href="../css/bootstrap.css">
   <link rel="stylesheet" href="../css/animate.css">
   <link rel="stylesheet" href="../css/owl.carousel.min.css">
   <link rel="stylesheet" href="../css/owl.theme.default.min.css">
   <link rel="stylesheet" href="../css/magnific-popup.css">
   <link rel="stylesheet" href="../css/custom.css">
   <link rel="stylesheet" href="../css/index.css">
   <link rel="stylesheet" href="../css/service.css">
   <link rel="stylesheet" href="../css/chatbot.css">
   <title>{s['title']}</title>

<style>
/* -------------------------------------------------------------
   TECHTOX BRAND GUIDELINES TYPOGRAPHY (SORA ONLY, TRACKING -10)
------------------------------------------------------------- */
body, h1, h2, h3, h4, h5, h6, p, span, a, li, button, input, label {{
   font-family: 'Sora', sans-serif !important;
   letter-spacing: -0.015em;
}}

/* Navigation Dropdown */
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

/* Brand Section Titles & Eyebrows */
.vibe-eyebrow {{
   color: #FF2E3E !important;
   font-family: 'Sora', sans-serif !important;
   font-size: 13px !important;
   font-weight: 700 !important;
   letter-spacing: 2px !important;
   text-transform: uppercase !important;
   margin-bottom: 12px !important;
   display: inline-block;
}}
.vibe-heading {{
   font-family: 'Sora', sans-serif !important;
   font-size: 40px !important;
   font-weight: 700 !important;
   color: #000000 !important;
   letter-spacing: -1.2px !important;
   margin-bottom: 16px !important;
   line-height: 1.15 !important;
}}
.vibe-lead {{
   color: #6b7280 !important;
   font-size: 17px !important;
   font-family: 'Sora', sans-serif !important;
   font-weight: 400 !important;
   margin: 0 !important;
   line-height: 1.65 !important;
   letter-spacing: -0.3px !important;
}}


/* Hero View Demo Button */
.vibe-btn-demo {{
   color: #ffffff !important;
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 600;
   padding: 12px 26px;
   border: 1px solid rgba(255, 255, 255, 0.25);
   border-radius: 9999px;
   text-decoration: none !important;
   display: inline-flex;
   align-items: center;
   gap: 10px;
   background: rgba(255, 255, 255, 0.08);
   backdrop-filter: blur(8px);
   transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
   letter-spacing: -0.01em;
   cursor: pointer;
}}
.vibe-btn-demo:hover {{
   background: rgba(255, 46, 62, 0.2);
   border-color: #FF2E3E;
   color: #ffffff !important;
   transform: translateY(-2px);
   box-shadow: 0 10px 25px rgba(255, 46, 62, 0.3);
}}
.vibe-btn-demo .vibe-play-circle {{
   width: 26px;
   height: 26px;
   border-radius: 50%;
   background: #FF2E3E;
   color: #ffffff;
   display: inline-flex;
   align-items: center;
   justify-content: center;
   font-size: 10px;
   padding-left: 2px;
   transition: transform 0.25s ease;
}}
.vibe-btn-demo:hover .vibe-play-circle {{
   transform: scale(1.15);
}}

/* Section 05 Live Demo Video Card */
.video-demo-card {{
   position: relative;
   border-radius: 16px;
   overflow: hidden;
   background: #0b0f17;
   border: 1px solid rgba(255, 255, 255, 0.1);
   box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
   margin-bottom: 40px;
}}
.video-demo-inner {{
   position: relative;
   height: 360px;
   width: 100%;
   display: flex;
   align-items: center;
   justify-content: center;
   background-size: cover;
   background-position: center;
}}
.video-play-pulse {{
   width: 80px;
   height: 80px;
   border-radius: 50%;
   background: #FF2E3E;
   display: flex;
   align-items: center;
   justify-content: center;
   box-shadow: 0 0 0 14px rgba(255, 46, 62, 0.25), 0 12px 30px rgba(255, 46, 62, 0.45);
   transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
   cursor: pointer;
}}
.video-demo-card:hover .video-play-pulse {{
   transform: scale(1.1);
   box-shadow: 0 0 0 20px rgba(255, 46, 62, 0.35), 0 15px 35px rgba(255, 46, 62, 0.55);
}}
.video-play-trigger {{
   display: flex;
   flex-direction: column;
   align-items: center;
   gap: 18px;
   text-decoration: none !important;
}}

/* Magnific Popup Fade Animation */
.mfp-fade.mfp-bg {{
  opacity: 0;
  transition: all 0.25s ease-out;
}}
.mfp-fade.mfp-bg.mfp-ready {{
  opacity: 0.88;
}}
.mfp-fade.mfp-bg.mfp-removing {{
  opacity: 0;
}}
.mfp-fade.mfp-wrap .mfp-content {{
  opacity: 0;
  transform: scale(0.95);
  transition: all 0.25s ease-out;
}}
.mfp-fade.mfp-wrap.mfp-ready .mfp-content {{
  opacity: 1;
  transform: scale(1);
}}
.mfp-fade.mfp-wrap.mfp-removing .mfp-content {{
  opacity: 0;
  transform: scale(0.95);
}}

/* 02 - Problem Cards */
.problem-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 24px;
}}
@media (min-width: 768px) {{ .problem-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
.problem-card {{
   background: #ffffff;
   border: 1px solid #fee2e2;
   border-radius: 12px;
   padding: 32px;
   box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
}}
.problem-card:hover {{
   transform: translateY(-4px);
   box-shadow: 0 12px 24px -4px rgba(239, 68, 68, 0.12);
}}
.problem-badge {{
   display: inline-flex;
   align-items: center;
   gap: 6px;
   background: #fef2f2;
   color: #ef4444;
   font-family: 'Sora', sans-serif !important;
   font-size: 12px;
   font-weight: 700;
   padding: 4px 10px;
   border-radius: 6px;
   margin-bottom: 16px;
   letter-spacing: 0.5px;
   text-transform: uppercase;
}}
.problem-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 20px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 10px;
   letter-spacing: -0.5px;
}}
.problem-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 15px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.6;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 03 - Solution Box */
.solution-box {{
   background: #000000;
   color: #ffffff;
   border-radius: 16px;
   padding: 56px 48px;
   border: 1px solid rgba(255, 255, 255, 0.1);
   position: relative;
   overflow: hidden;
}}
.solution-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 34px;
   font-weight: 700;
   color: #ffffff;
   letter-spacing: -1px;
   margin-bottom: 16px;
   line-height: 1.2;
}}
.solution-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 17px;
   font-weight: 300;
   color: #d1d5db;
   line-height: 1.7;
   max-width: 820px;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 04 - Outcome Cards */
.outcome-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 24px;
}}
@media (min-width: 768px) {{ .outcome-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
.outcome-card {{
   background: #f9fafb;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 36px 28px;
   text-align: center;
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
}}
.outcome-card:hover {{
   transform: translateY(-4px);
   box-shadow: 0 10px 20px -2px rgba(0, 0, 0, 0.06);
}}
.outcome-stat {{
   font-family: 'Sora', sans-serif !important;
   font-size: 52px;
   font-weight: 800;
   color: #FF2E3E;
   line-height: 1;
   margin-bottom: 10px;
   letter-spacing: -2px;
}}
.outcome-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 18px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 8px;
   letter-spacing: -0.4px;
}}
.outcome-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.55;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 05 - Workflow Horizontal Flow */
.workflow-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 20px;
}}
@media (min-width: 992px) {{ .workflow-grid {{ grid-template-columns: repeat(5, 1fr); }} }}
.workflow-step-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 28px 22px;
   position: relative;
   display: flex;
   flex-direction: column;
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
}}
.workflow-step-card:hover {{
   transform: translateY(-4px);
   box-shadow: 0 10px 20px -2px rgba(0, 0, 0, 0.06);
}}
.workflow-step-num {{
   font-family: 'Sora', sans-serif !important;
   font-size: 32px;
   font-weight: 800;
   color: #FF2E3E;
   line-height: 1;
   margin-bottom: 14px;
   letter-spacing: -1px;
}}
.workflow-step-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 16px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 8px;
   letter-spacing: -0.4px;
}}
.workflow-step-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 13px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.5;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 06 - Capabilities Grid */
.feature-light-grid {{ display: grid; gap: 24px; grid-template-columns: 1fr; }}
@media (min-width: 768px) {{ .feature-light-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
@media (min-width: 1024px) {{ .feature-light-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
.feature-light-card {{ 
   background: #ffffff; 
   padding: 38px 32px; 
   border-radius: 12px; 
   border: 1px solid #e5e7eb; 
   box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04); 
   transition: box-shadow 0.25s ease, transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); 
}}
.feature-light-card:hover {{ 
   box-shadow: 0 14px 28px -4px rgba(0, 0, 0, 0.09); 
   transform: translateY(-4px); 
}}
.fl-icon {{ font-size: 24px; color: #FF2E3E; margin-bottom: 16px; }}
.fl-title {{ 
   font-family: 'Sora', sans-serif !important; 
   font-size: 19px; 
   font-weight: 700; 
   color: #000000; 
   margin: 0 0 10px 0; 
   letter-spacing: -0.5px; 
}}
.fl-desc {{ 
   font-family: 'Sora', sans-serif !important; 
   color: #6b7280; 
   font-size: 14px; 
   font-weight: 400;
   line-height: 1.6; 
   margin: 0; 
   letter-spacing: -0.2px; 
}}

/* 07 - Tools Pills */
.tool-category-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 34px;
   height: 100%;
}}
.tool-category-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 19px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 16px;
   letter-spacing: -0.4px;
}}
.tool-pills-wrap {{
   display: flex;
   flex-wrap: wrap;
   gap: 10px;
}}
.tool-tag {{
   display: inline-flex;
   align-items: center;
   padding: 8px 16px;
   border-radius: 9999px;
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 600;
   letter-spacing: -0.2px;
   transition: transform 0.2s ease;
}}
.tool-tag:hover {{
   transform: scale(1.03);
}}
.tool-tag-native {{
   background: #ecfdf5;
   border: 1px solid #a7f3d0;
   color: #065f46;
}}
.tool-tag-custom {{
   background: #fef2f2;
   border: 1px solid #fecaca;
   color: #991b1b;
}}

/* 08 - Portfolio Items */
.portfolio-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 32px;
}}
@media (min-width: 992px) {{ .portfolio-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
.portfolio-item-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   overflow: hidden;
   display: flex;
   flex-direction: column;
   box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
}}
.portfolio-item-card:hover {{
   transform: translateY(-4px);
   box-shadow: 0 14px 28px -4px rgba(0, 0, 0, 0.09);
}}
.portfolio-item-img-wrap {{
   aspect-ratio: 16/10;
   background: #f3f4f6;
   overflow: hidden;
}}
.portfolio-item-img-wrap img {{
   width: 100%;
   height: 100%;
   object-fit: cover;
   transition: transform 0.4s ease;
}}
.portfolio-item-card:hover .portfolio-item-img-wrap img {{
   transform: scale(1.05);
}}
.portfolio-item-body {{
   padding: 26px;
   display: flex;
   flex-direction: column;
   gap: 12px;
   flex: 1;
}}
.portfolio-item-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 19px;
   font-weight: 700;
   color: #111827;
   margin: 0;
   letter-spacing: -0.4px;
}}
.portfolio-meta-row {{
   font-family: 'Sora', sans-serif !important;
   font-size: 13px;
   line-height: 1.55;
   color: #4b5563;
   letter-spacing: -0.2px;
}}
.portfolio-meta-label {{
   font-weight: 700;
   color: #111827;
   display: inline-block;
   margin-right: 4px;
}}

/* 09 - Reliability */
.reliability-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 20px;
}}
@media (min-width: 768px) {{ .reliability-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
@media (min-width: 1024px) {{ .reliability-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
.reliability-card {{
   background: #f9fafb;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 26px;
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}}
.reliability-card:hover {{
   transform: translateY(-3px);
}}
.reliability-card h4 {{
   font-family: 'Sora', sans-serif !important;
   font-size: 16px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 8px;
   letter-spacing: -0.3px;
}}
.reliability-card p {{
   font-family: 'Sora', sans-serif !important;
   font-size: 13px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.55;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 10 - Implementation Process */
.process-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 16px;
}}
@media (min-width: 768px) {{ .process-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
@media (min-width: 1024px) {{ .process-grid {{ grid-template-columns: repeat(6, 1fr); }} }}
.process-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 10px;
   padding: 22px 16px;
   text-align: center;
   transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}}
.process-card:hover {{
   transform: translateY(-3px);
}}
.process-num {{
   font-family: 'Sora', sans-serif !important;
   font-size: 26px;
   font-weight: 800;
   color: #FF2E3E;
   line-height: 1;
   margin-bottom: 8px;
   letter-spacing: -1px;
}}
.process-title {{
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 6px;
   letter-spacing: -0.3px;
}}
.process-desc {{
   font-family: 'Sora', sans-serif !important;
   font-size: 12px;
   font-weight: 400;
   color: #6b7280;
   line-height: 1.45;
   margin: 0;
   letter-spacing: -0.2px;
}}

/* 11 - Scope Split */
.scope-grid {{
   display: grid;
   grid-template-columns: 1fr;
   gap: 24px;
}}
@media (min-width: 768px) {{ .scope-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
.scope-card {{
   background: #ffffff;
   border: 1px solid #e5e7eb;
   border-radius: 12px;
   padding: 34px;
}}
.scope-card h4 {{
   font-family: 'Sora', sans-serif !important;
   font-size: 19px;
   font-weight: 700;
   color: #111827;
   margin-bottom: 18px;
   letter-spacing: -0.4px;
}}
.scope-list {{
   list-style: none;
   padding: 0;
   margin: 0;
   display: flex;
   flex-direction: column;
   gap: 12px;
}}
.scope-list li {{
   font-family: 'Sora', sans-serif !important;
   font-size: 14px;
   font-weight: 400;
   color: #4b5563;
   display: flex;
   align-items: flex-start;
   gap: 10px;
   letter-spacing: -0.2px;
}}
.scope-list li i {{
   margin-top: 3px;
}}

/* 12 - Website Native FAQ Accordion (matching faq.html exactly) */
.fv-faq-modern-accordion .fv-faq-modern-item {{
  background: transparent !important;
  border: none !important;
  border-bottom: 1px solid #e5e7eb !important;
  border-radius: 0 !important;
  padding: 24px 0 !important;
  margin-bottom: 0 !important;
  box-shadow: none !important;
  cursor: pointer;
}}
.fv-faq-modern-accordion .fv-faq-modern-item:last-child {{
  border-bottom: none !important;
}}
.fv-faq-modern-header {{
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  cursor: pointer;
}}
.fv-faq-modern-header h3 {{
  color: #000000 !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 18px !important;
  font-weight: 600 !important;
  margin: 0 !important;
  letter-spacing: -0.3px !important;
  transition: color 0.3s ease !important;
}}
.fv-faq-modern-header .fa {{
  color: #000000 !important;
  font-size: 16px !important;
  transition: transform 0.3s ease, color 0.3s ease !important;
}}
.fv-faq-modern-content {{
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  transition: all 0.4s ease;
  transform: translateY(-8px);
}}
.fv-faq-modern-content p {{
  color: #6b7280 !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 15px !important;
  font-weight: 400 !important;
  line-height: 1.65 !important;
  margin: 0 !important;
  padding-top: 14px !important;
  letter-spacing: -0.2px !important;
}}
.fv-faq-modern-accordion .fv-faq-item.active .fv-faq-header h3 {{
  color: #FF2E3E !important;
}}
.fv-faq-modern-accordion .fv-faq-item.active .fv-faq-header .fa {{
  color: #FF2E3E !important;
  transform: rotate(180deg) !important;
}}
.fv-faq-modern-accordion .fv-faq-item.active .fv-faq-content {{
  max-height: 400px;
  opacity: 1;
  transform: translateY(0);
}}
</style>

<!-- Techtox ENTITY SCHEMA -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": ["Service", "WebPage"],
  "name": "{s['h1']}",
  "provider": {{
    "@type": "Organization",
    "name": "Techtox",
    "url": "https://techtox.com"
  }},
  "description": "{s['meta_desc']}"
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
               <li><a class="dropdown-item nested-subitem" href="../services/custom-dashboards.html"><i class="fal fa-chart-pie" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> Reporting & Dashboards</a></li>
               <li><a class="dropdown-item nested-subitem" href="../services/api-software-integration.html"><i class="fal fa-plug" style="width:20px; color:#FF2E3E; margin-right:8px; display:inline-block; text-align:center;"></i> API & Integrations</a></li>
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

   <!-- =============================================================
        01 — HERO SECTION
   ============================================================= -->
   <section class="fv-page-hero" style="background-image: linear-gradient(rgba(17, 24, 39, 0.88), rgba(17, 24, 39, 0.96)), url('{s['hero_img']}'); background-size: cover; background-position: center; border-bottom: 1px solid #000000;">
      <div class="container text-center">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">{s['eyebrow']}</span>
         <h1 class="wow fadeInUp" data-wow-delay="0.2s">{s['h1']}</h1>
         <p class="fv-lead wow fadeInUp" data-wow-delay="0.3s">{s['hero_desc']}</p>
         <div class="d-flex justify-content-center align-items-center flex-wrap wow fadeInUp" data-wow-delay="0.4s" style="gap: 16px; margin-top: 32px;">
            <a href="../contact.html" class="fv-dual-btn">
               <span class="fv-btn-pill">DISCUSS YOUR WORKFLOW</span>
               <div class="fv-btn-circle">
                  <i class="fa fa-arrow-right arrow-main"></i>
                  <i class="fa fa-arrow-right arrow-hover"></i>
               </div>
            </a>
            <a href="{s['demo_video_url']}" class="popup-youtube vibe-btn-demo" target="_blank" rel="noopener noreferrer">
               <span class="vibe-play-circle"><i class="fa fa-play"></i></span>
               <span>View Demo</span>
            </a>
         </div>
      </div>
   </section>

   <!-- =============================================================
        02 — THE PROBLEM
   ============================================================= -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">THE OPERATIONAL FRICTION</span>
            <h2 class="vibe-heading">What's Slowing Down Your Operations?</h2>
            <p class="vibe-lead">Common bottlenecks businesses face prior to implementing structured workflow automation.</p>
         </div>
         <div class="problem-grid">
{problems_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        03 — THE SOLUTION
   ============================================================= -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="solution-box wow fadeInUp" data-wow-delay="0.1s">
            <span style="color: #FF2E3E; font-family: 'Sora', sans-serif !important; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; display: inline-block;">THE ARCHITECTED SOLUTION</span>
            <h2 class="solution-title">{s['solution']['title']}</h2>
            <p class="solution-desc">{s['solution']['desc']}</p>
         </div>
      </div>
   </section>

   <!-- =============================================================
        04 — OUTCOMES
   ============================================================= -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="vibe-eyebrow">TANGIBLE BUSINESS RESULTS</span>
            <h2 class="vibe-heading">Predictable Operational Outcomes</h2>
            <p class="vibe-lead">Measurable efficiency gains achieved by replacing manual processes with automated pipelines.</p>
         </div>
         <div class="outcome-grid">
{outcomes_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        05 — HOW IT WORKS & DEMO VIDEO
   ============================================================= -->
   <section class="py-5" id="how-it-works" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">OPERATIONAL BLUEPRINT</span>
            <h2 class="vibe-heading">How It Works & Live Architecture</h2>
            <p class="vibe-lead">Watch the end-to-end workflow walkthrough or inspect the structured 5-step operational pipeline below.</p>
         </div>

         <!-- Live Demo Video Card -->
         <div class="video-demo-card wow fadeInUp" data-wow-delay="0.15s">
            <div class="video-demo-inner" style="background-image: linear-gradient(rgba(11, 15, 23, 0.72), rgba(11, 15, 23, 0.88)), url('{s['hero_img']}');">
               <a href="{s['demo_video_url']}" class="popup-youtube video-play-trigger" target="_blank" rel="noopener noreferrer">
                  <div class="video-play-pulse">
                     <i class="fa fa-play" style="color: #ffffff; font-size: 26px; margin-left: 4px;"></i>
                  </div>
                  <div class="text-center">
                     <span style="display: block; color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 700; letter-spacing: -0.4px;">Watch {s['h1']} Live Demo</span>
                     <span style="display: inline-flex; align-items: center; gap: 6px; color: #d1d5db; font-family: 'Sora', sans-serif !important; font-size: 14px; font-weight: 400; margin-top: 6px;">
                        <i class="fa fa-play-circle" style="color: #FF2E3E;"></i> Click to launch live video walkthrough
                     </span>
                  </div>
               </a>
            </div>
         </div>

         <div class="workflow-grid">
{workflow_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        06 — CAPABILITIES INCLUDED
   ============================================================= -->
   <section class="py-5" id="capabilities" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="vibe-eyebrow">INCLUDED IN SCOPE</span>
            <h2 class="vibe-heading">Engineered Capabilities</h2>
            <p class="vibe-lead">Everything built, tested, and integrated when you deploy {s['h1']}.</p>
         </div>
         <div class="feature-light-grid">
{capabilities_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        07 — TOOLS & INTEGRATIONS
   ============================================================= -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">TECHNOLOGY STACK</span>
            <h2 class="vibe-heading">Supported Platforms & Integrations</h2>
            <p class="vibe-lead">We integrate directly with your existing software stack using native connectors or custom API endpoints.</p>
         </div>
         
         <div class="row">
            <div class="col-lg-6 mb-4 mb-lg-0 wow fadeInLeft" data-wow-delay="0.1s">
               <div class="tool-category-card">
                  <h4 class="tool-category-title">Popular Native & Supported Platforms</h4>
                  <p style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #6b7280; line-height: 1.5; margin-bottom: 20px;">
                     Pre-built connectors with full two-way data sync capabilities for market-leading platforms.
                  </p>
                  <div class="tool-pills-wrap">
                     {native_tools_pills}
                  </div>
               </div>
            </div>
            
            <div class="col-lg-6 wow fadeInRight" data-wow-delay="0.1s">
               <div class="tool-category-card">
                  <h4 class="tool-category-title">Custom Middleware & Automation Engines</h4>
                  <p style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #6b7280; line-height: 1.5; margin-bottom: 20px;">
                     Advanced integration engines, custom webhook pipelines, and resilient middleware tailored to your custom logic.
                  </p>
                  <div class="tool-pills-wrap">
                     {custom_tools_pills}
                  </div>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- =============================================================
        08 — OPERATIONAL IMPLEMENTATIONS / PORTFOLIO
   ============================================================= -->
   <section class="py-5" id="portfolio" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">OPERATIONAL EVIDENCE</span>
            <h2 class="vibe-heading">Recent Deployments & Architectures</h2>
            <p class="vibe-lead">Production-tested workflows engineered to eliminate friction in live client environments.</p>
         </div>
         <div class="portfolio-grid">
{portfolio_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        09 — RELIABILITY & HUMAN OVERSIGHT
   ============================================================= -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">FAIL-SAFE ARCHITECTURE</span>
            <h2 class="vibe-heading">Reliability, Error Handling & Oversight</h2>
            <p class="vibe-lead">Automations engineered with strict validation, automatic retries, and immediate human escalation.</p>
         </div>
         
         <div class="reliability-grid">
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.05s">
               <h4><i class="fa fa-shield-alt text-danger mr-2"></i> Payload Schema Validation</h4>
               <p>Every incoming webhook is verified against expected data schemas before processing to filter malformed payloads.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.1s">
               <h4><i class="fa fa-redo text-danger mr-2"></i> Exponential Backoff Retries</h4>
               <p>If a destination API is temporarily down, requests automatically queue and retry exponentially without data loss.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.15s">
               <h4><i class="fa fa-file-alt text-danger mr-2"></i> Dead-Letter Audit Logs</h4>
               <p>Comprehensive execution logs record every transaction ID, payload timestamp, and response code for 30 days.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.2s">
               <h4><i class="fa fa-key text-danger mr-2"></i> Encrypted Credentials</h4>
               <p>OAuth 2.0 tokens and API keys are stored in encrypted client environment vaults—never exposed in client code.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.25s">
               <h4><i class="fa fa-bell text-danger mr-2"></i> Slack Anomaly Alerts</h4>
               <p>If an unrecoverable exception occurs, instant alerts notify our engineering channel and your team lead immediately.</p>
            </div>
            <div class="reliability-card wow fadeInUp" data-wow-delay="0.3s">
               <h4><i class="fa fa-user-check text-danger mr-2"></i> Human-in-the-Loop Triggers</h4>
               <p>Edge cases or flagged VIP accounts automatically route to human representatives before automated actions execute.</p>
            </div>
         </div>
      </div>
   </section>

   <!-- =============================================================
        10 — IMPLEMENTATION PROCESS
   ============================================================= -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container">
         <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="vibe-eyebrow">DEPLOYMENT METHODOLOGY</span>
            <h2 class="vibe-heading">Our 6-Stage Delivery Process</h2>
            <p class="vibe-lead">A structured engineering process from initial workflow audit to production deployment.</p>
         </div>
         
         <div class="process-grid">
            <div class="process-card wow fadeInUp" data-wow-delay="0.05s">
               <div class="process-num">01</div>
               <div class="process-title">Discovery</div>
               <div class="process-desc">Audit current workflows, data fields, and bottlenecks.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.1s">
               <div class="process-num">02</div>
               <div class="process-title">Architecture</div>
               <div class="process-desc">Map logic trees, data schemas, and failovers.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.15s">
               <div class="process-num">03</div>
               <div class="process-title">Build</div>
               <div class="process-desc">Configure connectors, scripts, and endpoints.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.2s">
               <div class="process-num">04</div>
               <div class="process-title">QA & Testing</div>
               <div class="process-desc">Simulate edge cases, traffic spikes, and payload errors.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.25s">
               <div class="process-num">05</div>
               <div class="process-title">Deployment</div>
               <div class="process-desc">Switch endpoints live with active monitoring.</div>
            </div>
            <div class="process-card wow fadeInUp" data-wow-delay="0.3s">
               <div class="process-num">06</div>
               <div class="process-title">Handover</div>
               <div class="process-desc">Documentation handover and team onboarding.</div>
            </div>
         </div>
      </div>
   </section>

   <!-- =============================================================
        11 — SCOPE & REQUIREMENTS
   ============================================================= -->
   <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
      <div class="container">
         <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="vibe-eyebrow">CLEAR BOUNDARIES</span>
            <h2 class="vibe-heading">Scope & Requirements</h2>
            <p class="vibe-lead">Transparent expectations regarding deliverables, client inputs, and ownership.</p>
         </div>
         
         <div class="scope-grid">
            <div class="scope-card wow fadeInLeft" data-wow-delay="0.1s">
               <h4><i class="fa fa-check text-danger mr-2"></i> What Is Included</h4>
               <ul class="scope-list">
                  <li><i class="fa fa-check text-success"></i> Full architectural diagram and data schema documentation</li>
                  <li><i class="fa fa-check text-success"></i> Custom webhook endpoints and API integrations</li>
                  <li><i class="fa fa-check text-success"></i> Complete error-handling and dead-letter retry queues</li>
                  <li><i class="fa fa-check text-success"></i> Team chat notifications (Slack or Microsoft Teams)</li>
                  <li><i class="fa fa-check text-success"></i> 14-day post-launch hypercare monitoring and support</li>
               </ul>
            </div>
            
            <div class="scope-card wow fadeInRight" data-wow-delay="0.1s">
               <h4><i class="fa fa-info-circle text-danger mr-2"></i> Client Requirements & Ownership</h4>
               <ul class="scope-list">
                  <li><i class="fa fa-arrow-right text-muted"></i> Client owns all third-party software accounts (Zero lock-in)</li>
                  <li><i class="fa fa-arrow-right text-muted"></i> Admin or developer API access to relevant platforms</li>
                  <li><i class="fa fa-arrow-right text-muted"></i> Provisioning of sample test data and expected field formats</li>
                  <li><i class="fa fa-arrow-right text-muted"></i> Designation of a primary team contact for feedback</li>
                  <li><i class="fa fa-arrow-right text-muted"></i> Complex custom database migrations quoted as separate scope</li>
               </ul>
            </div>
         </div>
      </div>
   </section>

   <!-- =============================================================
        12 — FAQS (EXACT NATIVE ACCORDION WITH ANIMATION)
   ============================================================= -->
   <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
      <div class="container" style="max-width: 860px;">
         <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp">
            <span class="vibe-eyebrow">COMMON QUESTIONS</span>
            <h2 class="vibe-heading">Frequently Asked Questions</h2>
            <p class="vibe-lead">Practical answers regarding implementation, maintenance, security, and timelines.</p>
         </div>
         
         <!-- NATIVE ACCORDION CONTAINER -->
         <div class="fv-faq-modern-accordion">
{faqs_html}         </div>
      </div>
   </section>

   <!-- =============================================================
        13 — FINAL CTA (SPLIT)
   ============================================================= -->
   <section class="fv-cta-split py-5" id="contactArea" style="position: relative; overflow: hidden;">
      <img src="../img/cta_bg_2.webp" alt="Abstract Background" loading="lazy" class="wow fadeIn" data-wow-duration="1.5s" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0;">
      <div style="position:absolute; inset:0; background: linear-gradient(90deg, rgba(17,24,39,0.95) 0%, rgba(17,24,39,0.7) 100%); z-index:0;"></div>
      
      <div class="container" style="position:relative; z-index:1; padding-top: 100px; padding-bottom: 100px;">
         <div class="row align-items-center">
            
            <div class="col-lg-6 mb-5 mb-lg-0 pr-lg-5 wow fadeInLeft" data-wow-delay="0.1s">
               <h2 class="fw-bold mb-4" style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 56px; line-height: 1.1; letter-spacing: -1.5px;">
                  Ready to eliminate operational friction?
               </h2>
               <p style="color: #d1d5db; font-family: 'Sora', sans-serif !important; font-size: 18px; line-height: 1.6; max-width: 500px; margin-bottom: 40px; letter-spacing: -0.2px;">
                  Tell us where your team is losing hours to repetitive work or disconnected tools. We will design a clean, reliable automation pipeline built around your business.
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
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Clear Operational ROI</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Zero Vendor Lock-in (You Own the System)</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Robust Error-Handling & Fallbacks</span>
                  </li>
                  <li class="d-flex align-items-center mb-4 pb-2">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Full Team Onboarding & Documentation</span>
                  </li>
                  <li class="d-flex align-items-center">
                     <i class="fa fa-check text-white mr-4" style="font-size: 22px;"></i>
                     <span style="color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 600; letter-spacing: -0.3px;">Ongoing Proactive Monitoring</span>
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
         <p class="about" style="font-family: 'Sora', sans-serif !important;">Design, build, automate and scale with full-service digital solutions designed around your business.</p>
         <div class="social-links">
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
         </div>
      </div>
      <div class="col-6 col-lg-2 mb-4 mb-lg-0"><div class="footer-box"><p class="title" style="font-family: 'Sora', sans-serif !important;">Company</p><a href="../about.html">About</a><a href="../faq.html">FAQ</a></div></div>
      <div class="col-6 col-lg-3 mb-4 mb-lg-0"><div class="footer-box"><p class="title" style="font-family: 'Sora', sans-serif !important;">Departments</p><a href="../services.html#development">Development</a><a href="../services.html#automation">Automation</a><a href="../services.html#creative">Creative</a><a href="../services.html#marketing">Marketing</a></div></div>
      <div class="col-lg-3"><div class="footer-box"><p class="title" style="font-family: 'Sora', sans-serif !important;">Resources</p><a href="mailto:contact@techtox.com">Email Us</a><a href="../contact.html">Request a Strategy Call</a><a href="#">Islamabad, Pakistan</a><a href="#">Serving globally</a></div></div>
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
   
   <!-- NATIVE FAQ ACCORDION & DEMO VIDEO LIGHTBOX SCRIPT -->
   <script>
   $(document).ready(function() {{
      // Native FAQ Accordion
      $('.fv-faq-modern-header').on('click', function() {{
         var item = $(this).closest('.fv-faq-modern-item');
         var isActive = item.hasClass('active');
         $('.fv-faq-modern-item').removeClass('active');
         if (!isActive) {{
            item.addClass('active');
         }}
      }});

      // Magnific Popup YouTube Video Lightbox
      if ($.fn.magnificPopup) {{
         $('.popup-youtube').magnificPopup({{
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false,
            iframe: {{
               patterns: {{
                  youtube: {{
                     index: 'youtube.com/',
                     id: 'v=',
                     src: 'https://www.youtube.com/embed/%id%?autoplay=1&rel=0'
                  }}
               }}
            }}
         }});
      }}
   }});
   </script>
</body>
</html>'''

def build_all():
    os.makedirs('services', exist_ok=True)
    for s in SERVICES_DATA:
        filepath = os.path.join('services', s['filename'])
        html = render_detail_page(s)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Built brand-compliant detail page: {filepath}")

    # Aliases / Redirects for backward compatibility
    ALIASES = {
        "business-reporting-dashboards.html": "custom-dashboards.html",
        "executive-dashboards.html": "custom-dashboards.html",
        "api-system-integration.html": "api-software-integration.html",
        "ai-agents.html": "ai-voice-workflow-agents.html",
        "calling-agents.html": "ai-voice-workflow-agents.html",
        "custom-ai-agents.html": "ai-voice-workflow-agents.html",
        "gohighlevel.html": "lead-crm-automation.html",
        "sales-automation.html": "lead-crm-automation.html",
        "workflow-automation.html": "lead-crm-automation.html"
    }

    for alias, target in ALIASES.items():
        path = os.path.join('services', alias)
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
        print(f"Created alias/redirect: {alias} -> {target}")

if __name__ == '__main__':
    build_all()
