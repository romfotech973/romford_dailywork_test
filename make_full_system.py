# -*- coding: utf-8 -*-
import sys
import base64

with open('logo_b64.txt', 'r', encoding='utf-8') as f:
    b64_logo = f.read().strip()

# Build index.html
html = rf'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Romford Holidays - Office ERP & Booking Management</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <!-- SheetJS & jsPDF for Excel/PDF exports -->
  <script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <style>
    :root {{
      --brand: #153A68;
      --brand-dark: #0D2646;
      --brand-light: #EBF3FC;
      --brand-border: #C8DCF2;
      --accent: #2563EB;
      --accent-soft: #EFF6FF;
      --bg: #F4F6F9;
      --card: #FFFFFF;
      --text: #1E293B;
      --text-muted: #64748B;
      --border: #E2E8F0;
      --border-dark: #CBD5E1;
      
      --success: #16A34A;
      --success-soft: #DCFCE7;
      --warning: #D97706;
      --warning-soft: #FEF3C7;
      --danger: #DC2626;
      --danger-soft: #FEE2E2;
      
      --conf: #6B3FA0;
      --conf-soft: #F5F0FB;
      --conf-line: #DCCDEF;
      --owed: #B54708;
      --owed-soft: #FEF0E6;

      --visa: #0D9488;
      --visa-soft: #CCFBF1;

      --radius-sm: 8px;
      --radius: 12px;
      --radius-lg: 16px;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      font-size: 13.5px;
      line-height: 1.5;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
    }}

    input, select, textarea, button {{
      font-family: inherit;
      font-size: inherit;
    }}
    .mono {{ font-family: 'JetBrains Mono', monospace; }}

    /* UTILITY CLASSES */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 600;
      white-space: nowrap;
    }}
    .badge-success {{ background: var(--success-soft); color: var(--success); }}
    .badge-warning {{ background: var(--warning-soft); color: var(--warning); }}
    .badge-danger {{ background: var(--danger-soft); color: var(--danger); }}
    .badge-brand {{ background: var(--brand-light); color: var(--brand); }}
    .badge-purple {{ background: var(--conf-soft); color: var(--conf); border: 1px solid var(--conf-line); }}
    .badge-owed {{ background: var(--owed-soft); color: var(--owed); }}
    .badge-visa {{ background: var(--visa-soft); color: var(--visa); }}
    .badge-muted {{ background: #F1F5F9; color: var(--text-muted); }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 13px;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .btn:hover {{ opacity: 0.95; transform: translateY(-1px); }}
    .btn:active {{ transform: translateY(0); }}
    .btn-primary {{ background: var(--brand); color: #fff; }}
    .btn-primary:hover {{ background: var(--brand-dark); }}
    .btn-outline {{ background: #fff; border-color: var(--border-dark); color: var(--text); }}
    .btn-outline:hover {{ background: #f8fafc; border-color: var(--brand); color: var(--brand); }}
    .btn-success {{ background: var(--success); color: #fff; }}
    .btn-danger {{ background: #fff; border-color: var(--danger); color: var(--danger); }}
    .btn-danger:hover {{ background: var(--danger-soft); }}
    .btn-sm {{ padding: 5px 10px; font-size: 12px; border-radius: 6px; }}
    .btn-link {{ background: none; border: none; color: var(--brand); padding: 0; text-decoration: underline; cursor: pointer; }}

    /* FORM STYLES */
    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 12px;
    }}
    .form-group label {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
    }}
    .form-control {{
      width: 100%;
      padding: 8px 12px;
      border: 1.5px solid var(--border-dark);
      border-radius: var(--radius-sm);
      background: #fff;
      color: var(--text);
      font-size: 13.5px;
      outline: none;
      transition: border-color 0.15s, box-shadow 0.15s;
    }}
    .form-control:focus {{
      border-color: var(--brand);
      box-shadow: 0 0 0 3px rgba(21, 58, 104, 0.12);
    }}
    .form-grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }}
    .form-grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }}
    .form-grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }}
    @media (max-width: 768px) {{
      .form-grid-2, .form-grid-3, .form-grid-4 {{ grid-template-columns: 1fr; }}
    }}

    /* ACCORDION SECTIONS */
    .sec-card {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow-sm);
      margin-bottom: 16px;
      overflow: hidden;
    }}
    .sec-card.conf {{
      background: #FCFAFF;
      border-color: var(--conf-line);
      box-shadow: inset 4px 0 0 var(--conf);
    }}
    .sec-head {{
      padding: 14px 20px;
      background: #fff;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
    }}
    .sec-card.conf .sec-head {{ background: #FCFAFF; border-bottom-color: var(--conf-line); }}
    .sec-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--brand);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .sec-card.conf .sec-title {{ color: var(--conf); }}
    .sec-subtitle {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 500;
      margin-left: 10px;
    }}
    .sec-toggle {{
      font-size: 12px;
      font-weight: 600;
      color: var(--brand);
    }}
    .sec-body {{
      padding: 18px 20px;
    }}

    /* SERVICE SELECTOR GRID */
    .svc-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-bottom: 16px;
    }}
    .svc-card {{
      border: 2px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      background: #fff;
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .svc-card:hover {{ border-color: var(--brand-border); background: var(--brand-light); }}
    .svc-card.active {{
      border-color: var(--brand);
      background: var(--brand-light);
      box-shadow: 0 0 0 1px var(--brand);
    }}
    .svc-card b {{ font-size: 15px; color: var(--brand); }}
    .svc-card small {{ color: var(--text-muted); font-size: 12px; }}

    /* KPI STATS CARDS */
    .stats-row {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      margin-bottom: 20px;
    }}
    .stat-card {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      box-shadow: var(--shadow-sm);
    }}
    .stat-card.conf {{
      background: var(--conf-soft);
      border-color: var(--conf-line);
    }}
    .stat-card.conf span {{ color: var(--conf); }}
    .stat-card.conf b {{ color: var(--conf); }}
    .stat-card span {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
    }}
    .stat-card b {{
      font-size: 22px;
      font-weight: 800;
      color: var(--brand);
    }}

    /* TABLES */
    .tbl-wrapper {{
      border: 1px solid var(--border);
      border-radius: var(--radius);
      overflow-x: auto;
      background: #fff;
      box-shadow: var(--shadow-sm);
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }}
    th {{
      background: #F8FAFC;
      padding: 12px 16px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      color: var(--text-muted);
      border-bottom: 1.5px solid var(--border);
      white-space: nowrap;
    }}
    td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
      font-size: 13px;
    }}
    tr:last-child td {{ border-bottom: none; }}
    tr.rowlink {{ cursor: pointer; transition: background 0.1s; }}
    tr.rowlink:hover td {{ background: var(--brand-light); }}
    .num {{ text-align: right; font-variant-numeric: tabular-nums; }}

    /* LOGIN SCREEN */
    #login-page {{
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      background: radial-gradient(circle at top right, #EBF3FC, #F4F6F9 65%);
    }}
    .login-box {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 36px 32px;
      width: 100%;
      max-width: 440px;
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .login-logo-wrap {{
      text-align: center;
    }}
    .login-logo-wrap img {{
      max-height: 64px;
      max-width: 220px;
      object-fit: contain;
    }}
    .login-title {{
      text-align: center;
      margin-top: 8px;
    }}
    .login-title h2 {{
      font-size: 20px;
      font-weight: 800;
      color: var(--brand);
      letter-spacing: -0.5px;
    }}
    .login-title p {{
      font-size: 13px;
      color: var(--text-muted);
    }}
    .role-dropdown-group {{
      background: var(--brand-light);
      border: 1.5px solid var(--brand-border);
      border-radius: 12px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .role-dropdown-group label {{
      font-size: 11px;
      font-weight: 800;
      color: var(--brand);
      text-transform: uppercase;
      letter-spacing: 0.6px;
    }}
    .role-dropdown-group select {{
      padding: 10px;
      font-weight: 700;
      border: 1.5px solid #A8C7EB;
      border-radius: 8px;
      background: #fff;
      color: var(--brand-dark);
      cursor: pointer;
    }}

    /* MAIN APP SHELL */
    #app-shell {{
      display: none;
      flex-direction: column;
      min-height: 100vh;
    }}
    .navbar {{
      background: #fff;
      border-bottom: 1.5px solid var(--border);
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: var(--shadow-sm);
    }}
    .navbar-brand {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .navbar-logo {{
      height: 38px;
      max-width: 150px;
      object-fit: contain;
    }}
    .role-pill {{
      padding: 5px 12px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      background: var(--brand-light);
      color: var(--brand);
      border: 1px solid var(--brand-border);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .navbar-user {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .user-tag {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 600;
      font-size: 13px;
      background: #F1F5F9;
      padding: 4px 12px 4px 6px;
      border-radius: 999px;
    }}
    .user-avatar {{
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--brand);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
    }}

    /* ROLE SWITCHER IN TOPBAR */
    .role-quick-switch {{
      padding: 6px 10px;
      border-radius: 8px;
      border: 1px solid var(--border-dark);
      background: #fff;
      font-weight: 600;
      font-size: 12px;
      color: var(--brand);
      cursor: pointer;
    }}

    /* TABS */
    .tabbar {{
      background: #fff;
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      display: flex;
      gap: 6px;
      overflow-x: auto;
    }}
    .tab-btn {{
      padding: 12px 16px;
      border: none;
      background: none;
      font-weight: 600;
      font-size: 13px;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 3px solid transparent;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }}
    .tab-btn:hover {{ color: var(--brand); }}
    .tab-btn.active {{
      color: var(--brand);
      border-bottom-color: var(--brand);
    }}
    .tab-count {{
      background: var(--danger);
      color: #fff;
      border-radius: 999px;
      font-size: 10px;
      padding: 1px 6px;
      font-weight: 700;
    }}

    /* CONTAINER */
    .main-wrap {{
      max-width: 1280px;
      width: 100%;
      margin: 0 auto;
      padding: 24px;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    /* ACTION BAR */
    .actionbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .actionbar-title {{
      font-size: 20px;
      font-weight: 800;
      color: var(--brand);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .actionbar-tools {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    /* SWITCH / TOGGLES */
    .switch-label {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid var(--border);
      cursor: pointer;
    }}
    .switch-label:last-child {{ border-bottom: none; }}
    .switch-text b {{ display: block; font-weight: 600; font-size: 13.5px; }}
    .switch-text small {{ color: var(--text-muted); font-size: 12px; }}
    .switch-inp {{
      appearance: none;
      width: 44px;
      height: 24px;
      border-radius: 999px;
      background: #CBD5E1;
      position: relative;
      cursor: pointer;
      outline: none;
      transition: background 0.15s;
    }}
    .switch-inp::after {{
      content: "";
      position: absolute;
      top: 3px; left: 3px;
      width: 18px; height: 18px;
      border-radius: 50%;
      background: #fff;
      transition: left 0.15s;
      box-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }}
    .switch-inp:checked {{ background: var(--brand); }}
    .switch-inp:checked::after {{ left: 23px; }}

    /* TOAST */
    #toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #1E293B;
      color: #fff;
      padding: 12px 20px;
      border-radius: 10px;
      font-weight: 600;
      font-size: 13px;
      box-shadow: var(--shadow-lg);
      display: none;
      z-index: 1000;
    }}

    /* PRINT / EXPORT */
    @media print {{
      .navbar, .tabbar, .actionbar-tools, .btn {{ display: none !important; }}
      body {{ background: #fff; }}
      .main-wrap {{ padding: 0; }}
    }}
  </style>
</head>
<body>

  <!-- 1. LOGIN SCREEN WITH ROLE SELECTOR -->
  <div id="login-page">
    <div class="login-box">
      <div class="login-logo-wrap">
        <img src="data:image/jpeg;base64,{b64_logo}" alt="Romford Holidays">
      </div>
      <div class="login-title">
        <h2>Office Booking Portal</h2>
        <p>Romford Holidays Management & Follow-up System</p>
      </div>

      <!-- ROLE DROPDOWN AT THE VERY TOP OF LOGIN -->
      <div class="role-dropdown-group">
        <label for="select-role">1. Choose Department / Login View</label>
        <select id="select-role">
          <option value="sales">🟢 Sales Department (Packages, Flights, Hotels, Visa, Other)</option>
          <option value="res">🔵 Reservations (Flight Ticketing & Group Fare)</option>
          <option value="ops">🟠 Operations (DMC Costing & Payment Approvals)</option>
          <option value="accounts">🟣 Accounts (Verification, Payouts, Invoicing, Cash Book)</option>
          <option value="visa">🟡 Visa Consultancy Desk (Process, VFS & Docs)</option>
          <option value="admin">🔴 Super Admin (Full Control, P&L, Audit & Rules)</option>
        </select>
      </div>

      <form onsubmit="handleLoginSubmit(event)">
        <div class="form-group">
          <label>Username / Staff ID</label>
          <input type="text" id="login-username" class="form-control" placeholder="Enter username" value="admin" required>
        </div>
        <div class="form-group">
          <label>Password</label>
          <input type="password" id="login-password" class="form-control" placeholder="••••••••" value="admin123" required>
        </div>
        <button type="submit" class="btn btn-primary" style="width:100%; padding:12px; margin-top:8px; font-size:14px;">
          Login to System →
        </button>
      </form>
      <div style="text-align:center; font-size:11px; color:var(--text-muted);">
        Romford Holidays · Internal Office Network
      </div>
    </div>
  </div>

  <!-- 2. MAIN APPLICATION SHELL -->
  <div id="app-shell">
    <header class="navbar">
      <div class="navbar-brand">
        <img class="navbar-logo" src="data:image/jpeg;base64,{b64_logo}" alt="Romford Holidays">
        <div id="nav-role-badge" class="role-pill">
          Sales Department
        </div>
      </div>
      <div class="navbar-user">
        <select class="role-quick-switch" id="topbar-role-switch" onchange="quickSwitchRole(this.value)">
          <option value="sales">Switch to: Sales</option>
          <option value="res">Switch to: Reservations</option>
          <option value="ops">Switch to: Operations</option>
          <option value="accounts">Switch to: Accounts</option>
          <option value="visa">Switch to: Visa Desk</option>
          <option value="admin">Switch to: Admin</option>
        </select>
        <div class="user-tag">
          <div class="user-avatar" id="avatar-circle">A</div>
          <span id="nav-user-name">Arjun (Sales)</span>
        </div>
        <button class="btn btn-outline btn-sm" onclick="handleLogout()">Logout</button>
      </div>
    </header>

    <!-- NAVIGATION TABS -->
    <nav class="tabbar" id="subnav-tabs">
      <!-- Injected dynamically based on role -->
    </nav>

    <!-- CONTENT WRAPPER -->
    <main class="main-wrap" id="main-content-view">
      <!-- Rendered views -->
    </main>
  </div>

  <div id="toast"></div>

  <script>
    /* ========================================================
       APPLICATION STATE & PERSISTENT STORAGE
       ======================================================== */
    const DB_KEY = "romford_office_db_v3";

    const INITIAL_DATA = {{
      rules: {{
        ownOnly: true,
        enterDmc: true,
        flightNet: true,
        seeSupplier: false,
        seeCost: false,
        seeMarkup: false,
        editAfter: true,
        editPriceAfter: false,
        seeHistory: false,
        canExport: true,
        opsSeeSell: false
      }},
      suppliers: [
        {{
          id: "sup-1",
          name: "Desert Rose Tourism LLC",
          type: "DMC",
          payBy: "Bank transfer",
          country: "United Arab Emirates",
          contact: "Sunil Sharma",
          phone: "+971 50 123 4567",
          email: "reservations@desertrose.ae",
          notes: "50% at booking, balance 7 days before checkin",
          bank: "Emirates NBD Dubai",
          accName: "Desert Rose Tourism LLC",
          accNo: "AE070330000000123456789",
          code: "EBILAEAD"
        }},
        {{
          id: "sup-2",
          name: "Akbar Travels Portal",
          type: "Flight portal",
          payBy: "Portal wallet",
          country: "India",
          contact: "Portal Support",
          phone: "022 40666444",
          email: "support@akbartravels.com",
          notes: "Instant ticketing via portal deposit wallet",
          bank: "HDFC Bank",
          accName: "Akbar Online Booking Co.",
          accNo: "50200012345678",
          code: "HDFC0000123"
        }},
        {{
          id: "sup-3",
          name: "Siam Discovery Thailand DMC",
          type: "DMC",
          payBy: "Bank transfer",
          country: "Thailand",
          contact: "Krittapak",
          phone: "+66 81 987 6543",
          email: "ops@siamdiscovery.co.th",
          notes: "100% advance required 14 days prior",
          bank: "Kasikornbank Bangkok",
          accName: "Siam Discovery Co Ltd",
          accNo: "TH73004000123456",
          code: "KASITHBK"
        }}
      ],
      bookings: [
        {{
          id: "RH-2026-0001",
          service: "tour",
          client: "Muhammed Shafi & Family",
          mobile: "+91 98470 12345",
          address: "Kochi, Kerala",
          dest: "Dubai 5D/4N Package",
          start: "2026-12-10",
          end: "2026-12-15",
          pax: 4,
          sell: 185000,
          owner: "Arjun",
          submitted: true,
          salesKnows: true,
          dmcName: "Desert Rose Tourism LLC",
          dmcNet: 142000,
          cost: 142000,
          costPending: false,
          opsApproved: true,
          supplierPaid: false,
          utr: "",
          invoiceNo: "RH/26/0045",
          vyapar: true,
          receipts: [
            {{ date: "2026-11-15", amount: 50000, mode: "Bank transfer", ref: "IMPS982341", by: "Arjun", verified: true }}
          ],
          schedule: [
            {{ id: "sch-1", item: "Desert Rose Tourism LLC", amount: 142000, due: "2026-12-01", status: "approved" }}
          ]
        }},
        {{
          id: "RH-2026-0002",
          service: "flight",
          client: "Dr. Anil Kumar",
          mobile: "+91 94471 55667",
          address: "Trivandrum",
          from: "COK",
          to: "LHR",
          tripType: "Return",
          depart: "2026-11-28",
          ret: "2026-12-20",
          airline: "Emirates",
          pax: 2,
          paxNames: "1. Anil Kumar / Dr  2. Radhika Nair / Mrs",
          fareType: "portal",
          ticketStatus: "Issued",
          ticketNo: "EK-176-9923847192",
          pnr: "W8Q2KP",
          issuedBy: "Reservation Head",
          issueDate: "2026-11-16",
          sell: 165000,
          owner: "Arjun",
          submitted: true,
          salesKnows: true,
          portalNet: 152000,
          cost: 152000,
          costPending: false,
          opsApproved: true,
          supplierPaid: true,
          utr: "HDFC9823471",
          invoiceNo: "RH/26/0046",
          vyapar: true,
          receipts: [
            {{ date: "2026-11-16", amount: 165000, mode: "UPI", ref: "UPI4982301", by: "Arjun", verified: true }}
          ],
          schedule: [
            {{ id: "sch-2", item: "Akbar Travels Portal", amount: 152000, due: "2026-11-16", status: "paid" }}
          ]
        }},
        {{
          id: "RH-2026-0003",
          service: "visa",
          client: "Faisal Rahman",
          mobile: "+91 97450 99887",
          address: "Calicut, Kerala",
          country: "United Kingdom",
          visaType: "Tourist Visa (6 Months)",
          pax: 1,
          appt: "2026-11-25",
          sell: 14500,
          owner: "Arjun",
          submitted: true,
          cost: 12000,
          costPending: false,
          opsApproved: false,
          supplierPaid: false,
          utr: "",
          invoiceNo: "",
          vyapar: false,
          visaStatus: "Under Process at VFS",
          docsChecked: true,
          receipts: [
            {{ date: "2026-11-16", amount: 14500, mode: "UPI", ref: "UPI883491", by: "Arjun", verified: true }}
          ],
          schedule: []
        }}
      ],
      changeLog: [
        {{ when: "17 Nov, 05:03 pm", who: "Arjun", role: "Sales", file: "RH-2026-0003", what: "Booking submitted", change: "Visa · UK" }},
        {{ when: "17 Nov, 04:52 pm", who: "Salahu", role: "Operations", file: "Desert Rose Tourism LLC", what: "Supplier added", change: "DMC" }},
        {{ when: "17 Nov, 04:48 pm", who: "Reservation Head", role: "Reservations", file: "RH-2026-0002", what: "Ticket issued", change: "PNR W8Q2KP" }}
      ],
      loginLog: [
        {{ time: "18 Nov, 09:30 am", user: "admin", role: "Super Admin", ip: "Office-PC-1" }},
        {{ time: "17 Nov, 10:15 am", user: "Arjun", role: "Sales", ip: "Office-PC-2" }}
      ]
    }};

    let DB = loadData();

    function loadData() {{
      try {{
        const str = localStorage.getItem(DB_KEY);
        return str ? JSON.parse(str) : INITIAL_DATA;
      }} catch(e) {{
        return INITIAL_DATA;
      }}
    }}

    function saveData() {{
      try {{
        localStorage.setItem(DB_KEY, JSON.stringify(DB));
      }} catch(e) {{
        alert("Failed to save to local storage.");
      }}
    }}

    /* ========================================================
       STATE & ROLE CONFIGURATIONS
       ======================================================== */
    let currentRole = "sales";
    let currentUser = "Arjun";
    let activeTab = "bookings";
    let currentEditingFileId = null; // null = list view

    const ROLES = {{
      sales: {{ label: "Sales Department", defaultUser: "Arjun", badge: "badge-brand" }},
      res: {{ label: "Reservations (Flights)", defaultUser: "Reservation Head", badge: "badge-brand" }},
      ops: {{ label: "Operations & Costing", defaultUser: "Salahu", badge: "badge-warning" }},
      accounts: {{ label: "Accounts & Management", defaultUser: "Accountant", badge: "badge-purple" }},
      visa: {{ label: "Visa Consultancy Desk", defaultUser: "Visa Consultant", badge: "badge-visa" }},
      admin: {{ label: "Super Admin", defaultUser: "Shahinsha", badge: "badge-danger" }}
    }};

    function showToast(msg) {{
      const t = document.getElementById("toast");
      t.innerText = msg;
      t.style.display = "block";
      setTimeout(() => {{ t.style.display = "none"; }}, 3500);
    }}

    function formatINR(val) {{
      if (val === null || val === undefined || isNaN(val)) return "—";
      return "₹" + Math.round(+val).toLocaleString("en-IN");
    }}

    function addLog(who, role, file, what, change) {{
      const d = new Date();
      const timeStr = d.toLocaleDateString("en-IN", {{ day:"numeric", month:"short" }}) + ", " + d.toLocaleTimeString("en-IN", {{ hour:"2-digit", minute:"2-digit" }});
      DB.changeLog.unshift({{
        when: timeStr,
        who,
        role,
        file,
        what,
        change
      }});
      saveData();
    }}

    /* ========================================================
       AUTH & NAVIGATION
       ======================================================== */
    function handleLoginSubmit(e) {{
      e.preventDefault();
      const role = document.getElementById("select-role").value;
      const user = document.getElementById("login-username").value.trim() || ROLES[role].defaultUser;

      currentRole = role;
      currentUser = user;
      currentEditingFileId = null;

      // Add to login log
      const d = new Date();
      const timeStr = d.toLocaleDateString("en-IN", {{ day:"numeric", month:"short" }}) + ", " + d.toLocaleTimeString("en-IN", {{ hour:"2-digit", minute:"2-digit" }});
      DB.loginLog.unshift({{
        time: timeStr,
        user: currentUser,
        role: ROLES[role].label,
        ip: "Office-Local-PC"
      }});
      saveData();

      // Switch screens
      document.getElementById("login-page").style.display = "none";
      document.getElementById("app-shell").style.display = "flex";

      // Setup navbar
      document.getElementById("nav-role-badge").innerText = ROLES[role].label;
      document.getElementById("nav-user-name").innerText = currentUser + " (" + ROLES[role].label + ")";
      document.getElementById("avatar-circle").innerText = currentUser.charAt(0).toUpperCase();
      document.getElementById("topbar-role-switch").value = role;

      setRoleTabs();
      showToast("Logged in as " + ROLES[role].label);
    }}

    function handleLogout() {{
      document.getElementById("app-shell").style.display = "none";
      document.getElementById("login-page").style.display = "flex";
      showToast("Logged out");
    }}

    function quickSwitchRole(newRole) {{
      currentRole = newRole;
      currentUser = ROLES[newRole].defaultUser;
      currentEditingFileId = null;

      document.getElementById("nav-role-badge").innerText = ROLES[newRole].label;
      document.getElementById("nav-user-name").innerText = currentUser + " (" + ROLES[newRole].label + ")";
      document.getElementById("avatar-circle").innerText = currentUser.charAt(0).toUpperCase();

      setRoleTabs();
      showToast("Switched to " + ROLES[newRole].label);
    }}

    function setRoleTabs() {{
      const nav = document.getElementById("subnav-tabs");
      nav.innerHTML = "";

      let tabs = [];
      if (currentRole === "sales") {{
        tabs = [
          {{ id: "bookings", label: "My Bookings" }},
          {{ id: "new_file", label: "+ New Booking File" }}
        ];
      }} else if (currentRole === "res") {{
        tabs = [
          {{ id: "flight_bookings", label: "Flight Bookings" }},
          {{ id: "new_flight", label: "+ New Flight File" }}
        ];
      }} else if (currentRole === "ops") {{
        tabs = [
          {{ id: "bookings", label: "Bookings" }},
          {{ id: "supplier_pays", label: "Supplier Payments", badge: DB.bookings.filter(b=>b.submitted && !b.opsApproved).length }},
          {{ id: "suppliers", label: "DMCs & Suppliers" }}
        ];
      }} else if (currentRole === "accounts") {{
        tabs = [
          {{ id: "today", label: "Today's Tasks", badge: getTodayActionCount() }},
          {{ id: "bookings", label: "Bookings" }},
          {{ id: "supplier_pays", label: "Supplier Payments", badge: DB.bookings.filter(b=>b.opsApproved && !b.supplierPaid).length }},
          {{ id: "cash", label: "Money In & Out (Cash Book)" }},
          {{ id: "profit", label: "Profit & Markup" }},
          {{ id: "suppliers", label: "DMCs & Suppliers" }},
          {{ id: "changelog", label: "Change Log" }}
        ];
      }} else if (currentRole === "visa") {{
        tabs = [
          {{ id: "visa_bookings", label: "Visa Applications" }},
          {{ id: "new_visa", label: "+ New Visa File" }}
        ];
      }} else if (currentRole === "admin") {{
        tabs = [
          {{ id: "today", label: "Today" }},
          {{ id: "bookings", label: "All Bookings" }},
          {{ id: "supplier_pays", label: "Supplier Payments" }},
          {{ id: "cash", label: "Money In & Out" }},
          {{ id: "profit", label: "Profit & Markup" }},
          {{ id: "suppliers", label: "DMCs & Suppliers" }},
          {{ id: "changelog", label: "Change Log" }},
          {{ id: "rules", label: "Access Rules" }},
          {{ id: "security", label: "Security & Login History" }}
        ];
      }}

      activeTab = tabs[0].id;

      tabs.forEach((t, i) => {{
        const b = document.createElement("button");
        b.className = "tab-btn" + (i === 0 ? " active" : "");
        b.innerHTML = `${{t.label}} ${{t.badge ? `<span class="tab-count">${{t.badge}}</span>` : ""}}`;
        b.onclick = () => {{
          document.querySelectorAll(".tab-btn").forEach(el => el.classList.remove("active"));
          b.classList.add("active");
          activeTab = t.id;
          currentEditingFileId = null; // return to list if switching tab
          renderMain();
        }};
        nav.appendChild(b);
      }});

      renderMain();
    }}

    function getTodayActionCount() {{
      let count = 0;
      // 1. Unverified receipts
      DB.bookings.forEach(b => {{
        b.receipts.forEach(r => {{ if (!r.verified) count++; }});
      }});
      // 2. Approved payments to pay
      count += DB.bookings.filter(b => b.opsApproved && !b.supplierPaid).length;
      // 3. Invoices to raise
      count += DB.bookings.filter(b => b.submitted && b.cost > 0 && !b.invoiceNo).length;
      return count;
    }}

    /* ========================================================
       MAIN RENDER DISPATCHER
       ======================================================== */
    function renderMain() {{
      const container = document.getElementById("main-content-view");
      container.innerHTML = "";

      if (currentEditingFileId) {{
        renderBookingDetailPage(container, currentEditingFileId);
        return;
      }}

      if (activeTab === "bookings") {{
        renderBookingsListPage(container);
      }} else if (activeTab === "new_file") {{
        renderNewFileCreation(container, "all");
      }} else if (activeTab === "flight_bookings") {{
        renderBookingsListPage(container, "flight");
      }} else if (activeTab === "new_flight") {{
        renderNewFileCreation(container, "flight");
      }} else if (activeTab === "visa_bookings") {{
        renderBookingsListPage(container, "visa");
      }} else if (activeTab === "new_visa") {{
        renderNewFileCreation(container, "visa");
      }} else if (activeTab === "today") {{
        renderTodayDashboard(container);
      }} else if (activeTab === "supplier_pays") {{
        renderSupplierPaymentsPage(container);
      }} else if (activeTab === "cash") {{
        renderCashBookPage(container);
      }} else if (activeTab === "profit") {{
        renderProfitMarkupPage(container);
      }} else if (activeTab === "suppliers") {{
        renderSuppliersPage(container);
      }} else if (activeTab === "changelog") {{
        renderChangeLogPage(container);
      }} else if (activeTab === "rules") {{
        renderAccessRulesPage(container);
      }} else if (activeTab === "security") {{
        renderSecurityLogsPage(container);
      }}
    }}

    /* ========================================================
       PAGE 1: BOOKINGS LIST (WITH METRICS & EXCEL/PDF EXPORTS)
       ======================================================== */
    function renderBookingsListPage(container, filterService = "all") {{
      let files = DB.bookings;
      if (filterService !== "all") {{
        files = files.filter(f => f.service === filterService);
      }}

      // Metrics calculation
      const totalSold = files.reduce((acc, f) => acc + (+f.sell || 0), 0);
      const totalRecv = files.reduce((acc, f) => acc + f.receipts.reduce((racc, r) => racc + (r.verified ? +r.amount : 0), 0), 0);
      const toCollect = Math.max(0, totalSold - totalRecv);
      const totalCost = files.reduce((acc, f) => acc + (+f.cost || 0), 0);
      const totalMarkup = totalSold - totalCost;

      let statsHtml = `
        <div class="stats-row">
          <div class="stat-card">
            <span>Active Bookings</span>
            <b>${{files.length}}</b>
          </div>
          <div class="stat-card">
            <span>Total Sold</span>
            <b>${{formatINR(totalSold)}}</b>
          </div>
          <div class="stat-card">
            <span>To Collect (Balance)</span>
            <b style="color:var(--warning);">${{formatINR(toCollect)}}</b>
          </div>
          <div class="stat-card">
            <span>Received (Verified)</span>
            <b style="color:var(--success);">${{formatINR(totalRecv)}}</b>
          </div>
          ${{(currentRole === 'accounts' || currentRole === 'admin') ? `
          <div class="stat-card conf">
            <span>Total Markup</span>
            <b>${{formatINR(totalMarkup)}}</b>
          </div>` : ''}}
        </div>
      `;

      let headerTitle = "All Client Bookings";
      if (currentRole === "sales") headerTitle = "Sales Bookings";
      if (filterService === "flight") headerTitle = "Flight & Group Fare Bookings";
      if (filterService === "visa") headerTitle = "Visa Consultancy Files";

      container.innerHTML = `
        ${{statsHtml}}
        <div class="actionbar">
          <div class="actionbar-title">
            ${{headerTitle}}
          </div>
          <div class="actionbar-tools">
            <input type="text" id="search-box" class="form-control" placeholder="Search client, mobile, ID..." style="width:250px;" oninput="filterBookingsTable(this.value)">
            <button class="btn btn-primary" onclick="startNewBookingFlow('${{filterService}}')">+ New Booking</button>
            <button class="btn btn-outline" onclick="exportBookingsExcel()">Export Excel</button>
            <button class="btn btn-outline" onclick="exportBookingsPDF()">Export PDF</button>
          </div>
        </div>

        <div class="tbl-wrapper">
          <table id="bookings-table">
            <thead>
              <tr>
                <th>Booking ID</th>
                <th>Client Name & Contact</th>
                <th>Service & Destination</th>
                <th>Travel Date</th>
                <th class="num">Client Price</th>
                <th class="num">Received</th>
                <th class="num">Balance</th>
                ${{(currentRole === 'accounts' || currentRole === 'admin') ? '<th class="num" style="color:var(--conf);">Cost / Markup</th>' : ''}}
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              ${{renderBookingsTableRows(files)}}
            </tbody>
          </table>
        </div>
      `;
    }}

    function renderBookingsTableRows(files) {{
      if (!files.length) {{
        return `<tr><td colspan="10" style="text-align:center; padding:30px; color:var(--text-muted);">No booking records found. Click "+ New Booking" to create one.</td></tr>`;
      }}
      return files.map(f => {{
        const rec = f.receipts.reduce((a, b) => a + (b.verified ? +b.amount : 0), 0);
        const bal = Math.max(0, (+f.sell || 0) - rec);
        const mk = (+f.sell || 0) - (+f.cost || 0);

        let svcLabel = "Tour";
        if (f.service === "flight") svcLabel = "Flight (" + (f.fareType || "portal").toUpperCase() + ")";
        if (f.service === "hotel") svcLabel = "Hotel";
        if (f.service === "visa") svcLabel = "Visa";
        if (f.service === "other") svcLabel = "Other";

        let stBadge = '<span class="badge badge-warning">Draft</span>';
        if (f.submitted) {{
          if (bal === 0) stBadge = '<span class="badge badge-success">Paid in Full</span>';
          else stBadge = '<span class="badge badge-brand">In Progress</span>';
        }}

        return `
          <tr class="rowlink" onclick="openBookingFile('${{f.id}}')">
            <td><strong class="mono" style="color:var(--brand);">${{f.id}}</strong><br><small class="badge badge-muted">${{svcLabel}}</small></td>
            <td><strong>${{f.client}}</strong><br><small class="mono text-muted">${{f.mobile}}</small></td>
            <td>${{f.dest || f.country || (f.from ? f.from + " ➔ " + f.to : "—")}}</td>
            <td>${{f.start || f.depart || f.appt || "—"}}</td>
            <td class="num"><strong>${{formatINR(f.sell)}}</strong></td>
            <td class="num" style="color:var(--success); font-weight:600;">${{formatINR(rec)}}</td>
            <td class="num" style="color:${{bal > 0 ? "var(--warning)" : "var(--text-muted)"}}; font-weight:600;">${{formatINR(bal)}}</td>
            ${{(currentRole === 'accounts' || currentRole === 'admin') ? `
            <td class="num" style="color:var(--conf); font-weight:700;">
              ${{formatINR(f.cost)}}<br><small style="color:var(--conf);">${{formatINR(mk)}} mk</small>
            </td>` : ''}}
            <td>${{stBadge}}</td>
            <td>
              <button class="btn btn-outline btn-sm" onclick="event.stopPropagation(); openBookingFile('${{f.id}}')">Open File ➔</button>
            </td>
          </tr>
        `;
      }}).join("");
    }}

    function filterBookingsTable(query) {{
      const q = query.toLowerCase();
      const filtered = DB.bookings.filter(b => 
        b.id.toLowerCase().includes(q) ||
        (b.client && b.client.toLowerCase().includes(q)) ||
        (b.mobile && b.mobile.includes(q)) ||
        (b.dest && b.dest.toLowerCase().includes(q))
      );
      document.querySelector("#bookings-table tbody").innerHTML = renderBookingsTableRows(filtered);
    }}

    function startNewBookingFlow(prefService) {{
      if (prefService === "flight") {{
        createNewBookingRecord("flight");
      }} else if (prefService === "visa") {{
        createNewBookingRecord("visa");
      }} else {{
        renderNewFileCreation(document.getElementById("main-content-view"), "all");
      }}
    }}

    function renderNewFileCreation(container, filterType) {{
      container.innerHTML = `
        <div class="actionbar">
          <div class="actionbar-title">Start a New Booking File</div>
          <button class="btn btn-outline" onclick="currentEditingFileId=null; renderMain();">← Cancel & Back</button>
        </div>
        <div class="sec-card">
          <div class="sec-body">
            <h3 style="margin-bottom:16px; color:var(--brand);">Select the Service you are booking:</h3>
            <div class="svc-grid">
              <div class="svc-card active" onclick="createNewBookingRecord('tour')">
                <b>🌴 Tour Package</b>
                <small>Through a DMC or self-arranged package</small>
              </div>
              <div class="svc-card" onclick="createNewBookingRecord('flight')">
                <b>✈️ Flight Ticket</b>
                <small>Portal fare or Group fare with PNR</small>
              </div>
              <div class="svc-card" onclick="createNewBookingRecord('hotel')">
                <b>🏨 Hotel Stay</b>
                <small>Standalone hotel or online supplier</small>
              </div>
              <div class="svc-card" onclick="createNewBookingRecord('visa')">
                <b>🛂 Visa Consultancy</b>
                <small>Visa application, documents & VFS appointment</small>
              </div>
              <div class="svc-card" onclick="createNewBookingRecord('other')">
                <b>📑 Other Service</b>
                <small>Insurance, transfer, forex, car rental</small>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    function createNewBookingRecord(svc) {{
      const year = new Date().getFullYear();
      const nextNum = String(DB.bookings.length + 1).padStart(4, '0');
      const id = `RH-${{year}}-${{nextNum}}`;

      const newRec = {{
        id,
        service: svc,
        client: "",
        mobile: "",
        address: "",
        dest: "",
        start: "",
        end: "",
        pax: 1,
        sell: 0,
        owner: currentUser,
        submitted: false,
        salesKnows: false,
        dmcName: "",
        dmcNet: 0,
        cost: 0,
        costPending: true,
        opsApproved: false,
        supplierPaid: false,
        utr: "",
        invoiceNo: "",
        vyapar: false,
        receipts: [],
        schedule: []
      }};

      if (svc === "flight") {{
        newRec.tripType = "Return";
        newRec.fareType = (currentRole === "res" ? "group" : "portal");
        newRec.ticketStatus = "Not issued";
        newRec.from = "";
        newRec.to = "";
        newRec.depart = "";
        newRec.ret = "";
        newRec.airline = "";
        newRec.paxNames = "";
        newRec.pnr = "";
        newRec.ticketNo = "";
        newRec.issuedBy = "Booking staff";
        newRec.issueDate = "";
      }} else if (svc === "hotel") {{
        newRec.hotel = "";
        newRec.city = "";
        newRec.checkin = "";
        newRec.checkout = "";
        newRec.rooms = 1;
      }} else if (svc === "visa") {{
        newRec.country = "";
        newRec.visaType = "Tourist Visa";
        newRec.appt = "";
        newRec.visaStatus = "Document Collection";
        newRec.docsChecked = false;
      }} else if (svc === "other") {{
        newRec.what = "";
        newRec.date = "";
      }}

      DB.bookings.unshift(newRec);
      addLog(currentUser, ROLES[currentRole].label, id, "Draft created", svc.toUpperCase());
      saveData();
      openBookingFile(id);
    }}

    function openBookingFile(id) {{
      currentEditingFileId = id;
      renderMain();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    /* ========================================================
       PAGE 2: COMPREHENSIVE BOOKING FILE VIEW & EDIT
       (Includes: Client/Trip, Flight/Hotel/Visa/DMC, Payments,
        Supplier Costing, Approvals, Invoicing & Vyapar)
       ======================================================== */
    function renderBookingDetailPage(container, fileId) {{
      const f = DB.bookings.find(b => b.id === fileId);
      if (!f) {{
        container.innerHTML = `<div class="sec-card"><div class="sec-body">Booking not found. <button class="btn btn-outline" onclick="currentEditingFileId=null;renderMain();">Back</button></div></div>`;
        return;
      }}

      const rec = f.receipts.reduce((a, b) => a + (b.verified ? +b.amount : 0), 0);
      const bal = Math.max(0, (+f.sell || 0) - rec);
      const mk = (+f.sell || 0) - (+f.cost || 0);

      let serviceTitle = "Tour Package";
      if (f.service === "flight") serviceTitle = "Flight Ticket (" + (f.fareType || "portal").toUpperCase() + ")";
      if (f.service === "hotel") serviceTitle = "Hotel Booking";
      if (f.service === "visa") serviceTitle = "Visa Consultancy";
      if (f.service === "other") serviceTitle = "Other Service";

      container.innerHTML = `
        <div class="actionbar">
          <div class="actionbar-title">
            <button class="btn btn-outline btn-sm" onclick="currentEditingFileId=null; renderMain();">← Back to List</button>
            <span>${{f.id}} · ${{serviceTitle}}</span>
            ${{!f.submitted ? '<span class="badge badge-warning">Draft (Only Sales Can View)</span>' : '<span class="badge badge-success">Submitted & Active</span>'}}
          </div>
          <div class="actionbar-tools">
            ${{!f.submitted ? `
            <button class="btn btn-primary" onclick="submitBookingToDepartments('${{f.id}}')">✓ Submit Booking File</button>
            ` : `
            <button class="btn btn-success" onclick="saveBookingChanges('${{f.id}}')">💾 Save Updates</button>
            `}}
            <button class="btn btn-outline btn-sm" onclick="window.print()">🖨️ Print / Download</button>
          </div>
        </div>

        <!-- QUICK FINANCIAL SUMMARY BANNER -->
        <div class="stats-row" style="margin-top:10px;">
          <div class="stat-card">
            <span>Client Selling Price</span>
            <b>${{formatINR(f.sell)}}</b>
          </div>
          <div class="stat-card">
            <span>Received (Verified)</span>
            <b style="color:var(--success);">${{formatINR(rec)}}</b>
          </div>
          <div class="stat-card">
            <span>Balance to Collect</span>
            <b style="color:${{bal > 0 ? "var(--warning)" : "var(--text-muted)"}};">${{formatINR(bal)}}</b>
          </div>
          ${{(currentRole === "accounts" || currentRole === "admin" || currentRole === "ops") ? `
          <div class="stat-card conf">
            <span>Supplier Cost</span>
            <b>${{formatINR(f.cost)}}</b>
          </div>
          <div class="stat-card conf">
            <span>Gross Markup (Profit)</span>
            <b>${{formatINR(mk)}}</b>
          </div>` : ''}}
        </div>

        <!-- SECTION 1: CLIENT & PASSENGER INFO -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">👤 Client & Passenger Details</div>
          </div>
          <div class="sec-body">
            <div style="background:#F8FAFC; border:1px dashed #94A3B8; border-radius:10px; padding:12px 14px; margin-bottom:14px;">
              <div style="display:flex; align-items:center; justify-content:space-between; gap:12px; flex-wrap:wrap;">
                <div>
                  <b style="display:block; font-size:13px; color:var(--brand, #153A68);">Auto-fill from Customer Document</b>
                  <small style="color:var(--muted, #64748B);">Upload a PDF or text document (ticket, itinerary, inquiry, invoice) to prefill customer details. Review before saving.</small>
                </div>
                <div style="display:flex; gap:8px; align-items:center;">
                  <input type="file" id="bf-doc-upload" accept=".pdf,.txt,.csv,.json,application/pdf,text/plain" style="display:none" onchange="handleCustomerDocUpload(this)">
                  <button type="button" class="btn btn-outline btn-sm" onclick="triggerCustomerDocImport('${{f.id}}')">Import PDF / Document</button>
                </div>
              </div>
              <div id="bf-doc-import-status" style="margin-top:8px; font-size:12px; color:var(--muted, #64748B);"></div>
            </div>
            <div class="form-grid-3">
              <div class="form-group">
                <label>Client / Lead Passenger Name *</label>
                <input type="text" id="bf-client" class="form-control" value="${{f.client || ""}}" placeholder="Full Name" onchange="markUnsaved('${{f.id}}')">
              </div>
              <div class="form-group">
                <label>Mobile / WhatsApp *</label>
                <input type="text" id="bf-mobile" class="form-control" value="${{f.mobile || ""}}" placeholder="+91 00000 00000" onchange="markUnsaved('${{f.id}}')">
              </div>
              <div class="form-group">
                <label>Billing Address / City</label>
                <input type="text" id="bf-address" class="form-control" value="${{f.address || ""}}" placeholder="City, State" onchange="markUnsaved('${{f.id}}')">
              </div>
            </div>
            ${{renderServiceSpecificInputs(f)}}
          </div>
        </div>

        <!-- SECTION 2: DMC / SUPPLIER SECTION (USER REQUESTED: DMC Name & Net Rate in Tour) -->
        ${{renderDmcSupplierSection(f)}}

        <!-- SECTION 3: RESERVATIONS / TICKETING (FOR FLIGHTS) -->
        ${{f.service === "flight" ? renderFlightTicketingSection(f) : ""}}

        <!-- SECTION 4: VISA CONSULTANCY TRACKING (FOR VISAS) -->
        ${{f.service === "visa" ? renderVisaTrackingSection(f) : ""}}

        <!-- SECTION 5: CLIENT PAYMENTS & ADVANCE ENTRY -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">💳 Client Payments & Advance Received</div>
            <span class="badge badge-brand">Total Verified: ${{formatINR(rec)}}</span>
          </div>
          <div class="sec-body">
            <div class="form-grid-3" style="margin-bottom:14px;">
              <div class="form-group">
                <label>Total Package Price to Client (₹) *</label>
                <input type="number" id="bf-sell" class="form-control" value="${{f.sell || 0}}" onchange="f.sell=+this.value; saveData(); renderMain();">
              </div>
              <div class="form-group">
                <label>Verified in Bank</label>
                <input type="text" class="form-control" value="${{formatINR(rec)}}" readonly style="background:#F8FAFC;">
              </div>
              <div class="form-group">
                <label>Pending Client Balance</label>
                <input type="text" class="form-control" value="${{formatINR(bal)}}" readonly style="background:#F8FAFC; color:${{bal > 0 ? "var(--warning)" : "var(--success)"}}; font-weight:700;">
              </div>
            </div>

            <!-- Client Payment Table -->
            <div class="tbl-wrapper" style="margin-bottom:14px;">
              <table>
                <thead>
                  <tr>
                    <th>Date</th>
                    <th class="num">Amount (₹)</th>
                    <th>Payment Mode</th>
                    <th>UTR / Transaction Ref</th>
                    <th>Collected By</th>
                    <th>Bank Verification</th>
                  </tr>
                </thead>
                <tbody>
                  ${{f.receipts.length ? f.receipts.map((r, i) => `
                    <tr>
                      <td>${{r.date}}</td>
                      <td class="num font-weight-bold" style="color:var(--success);">${{formatINR(r.amount)}}</td>
                      <td>${{r.mode}}</td>
                      <td class="mono">${{r.ref || "—"}}</td>
                      <td>${{r.by || "—"}}</td>
                      <td>
                        ${{r.verified ? '<span class="badge badge-success">✓ Verified in Bank</span>' : `
                          ${{(currentRole === 'accounts' || currentRole === 'admin') ? `
                            <button class="btn btn-success btn-sm" onclick="verifyReceipt('${{f.id}}', ${{i}})">Mark Verified</button>
                          ` : '<span class="badge badge-warning">Awaiting Accounts Check</span>'}}
                        `}}
                      </td>
                    </tr>
                  `).join("") : '<tr><td colspan="6" style="text-align:center; padding:16px; color:var(--text-muted);">No payment entries yet. Add advance below.</td></tr>'}}
                </tbody>
              </table>
            </div>

            <!-- Add Payment Form -->
            <div style="background:#F8FAFC; padding:12px; border-radius:var(--radius-sm); border:1px solid var(--border);">
              <b style="display:block; margin-bottom:8px; font-size:12px; color:var(--brand);">+ Record Client Payment / Advance:</b>
              <div class="form-grid-4">
                <input type="date" id="new-pay-date" class="form-control" value="${{new Date().toISOString().slice(0, 10)}}">
                <input type="number" id="new-pay-amt" class="form-control" placeholder="Amount (₹)">
                <select id="new-pay-mode" class="form-control">
                  <option>UPI / GPay</option>
                  <option>Bank Transfer (IMPS/NEFT)</option>
                  <option>Cash</option>
                  <option>Card / POS Machine</option>
                </select>
                <input type="text" id="new-pay-ref" class="form-control" placeholder="UTR / Ref Number">
              </div>
              <div style="margin-top:10px; text-align:right;">
                <button class="btn btn-primary btn-sm" onclick="addClientPaymentEntry('${{f.id}}')">Add Payment to Booking</button>
              </div>
            </div>
          </div>
        </div>

        <!-- SECTION 6: ACCOUNTS, INVOICING & VYAPAR (VISIBLE TO ACCOUNTS & ADMIN) -->
        ${{(currentRole === "accounts" || currentRole === "admin") ? `
        <div class="sec-card conf">
          <div class="sec-head">
            <div class="sec-title" style="color:var(--conf);">🧾 Accounts & Vyapar Invoicing</div>
            <span class="badge badge-purple">Confidential Accounts Desk</span>
          </div>
          <div class="sec-body">
            <div class="form-grid-3">
              <div class="form-group">
                <label>Official Tax Invoice No.</label>
                <input type="text" id="bf-inv" class="form-control" value="${{f.invoiceNo || ""}}" placeholder="e.g. RH/26-27/0120" onchange="f.invoiceNo=this.value; saveData();">
              </div>
              <div class="form-group" style="justify-content:flex-end;">
                <label style="display:flex; align-items:center; gap:8px; cursor:pointer; padding-top:24px;">
                  <input type="checkbox" id="bf-vyapar" ${{f.vyapar ? "checked" : ""}} onchange="f.vyapar=this.checked; saveData();">
                  <b>✓ Entered in Vyapar Accounting Software</b>
                </label>
              </div>
              <div class="form-group">
                <label>Quick Action</label>
                <button class="btn btn-outline" style="border-color:var(--conf); color:var(--conf);" onclick="saveData(); showToast('Invoicing status updated');">Save Invoice Details</button>
              </div>
            </div>
          </div>
        </div>` : ''}}
      `;
    }}

    /* SERVICE SPECIFIC INPUT FORM ELEMENTS */
    function renderServiceSpecificInputs(f) {{
      if (f.service === "tour") {{
        return `
          <div class="form-grid-4">
            <div class="form-group">
              <label>Tour Destination *</label>
              <input type="text" id="bf-dest" class="form-control" value="${{f.dest || ""}}" placeholder="e.g. Dubai, Thailand, Europe">
            </div>
            <div class="form-group">
              <label>Travel From (Start Date) *</label>
              <input type="date" id="bf-start" class="form-control" value="${{f.start || ""}}">
            </div>
            <div class="form-group">
              <label>Travel To (End Date) *</label>
              <input type="date" id="bf-end" class="form-control" value="${{f.end || ""}}">
            </div>
            <div class="form-group">
              <label>No. of People (Pax) *</label>
              <input type="number" id="bf-pax" class="form-control" value="${{f.pax || 1}}" min="1">
            </div>
          </div>
        `;
      }} else if (f.service === "flight") {{
        return `
          <div class="form-grid-4">
            <div class="form-group">
              <label>From (Airport/City) *</label>
              <input type="text" id="bf-from" class="form-control" value="${{f.from || ""}}" placeholder="e.g. COK">
            </div>
            <div class="form-group">
              <label>To (Airport/City) *</label>
              <input type="text" id="bf-to" class="form-control" value="${{f.to || ""}}" placeholder="e.g. DXB">
            </div>
            <div class="form-group">
              <label>Departure Date *</label>
              <input type="date" id="bf-depart" class="form-control" value="${{f.depart || ""}}">
            </div>
            <div class="form-group">
              <label>Return Date</label>
              <input type="date" id="bf-ret" class="form-control" value="${{f.ret || ""}}">
            </div>
          </div>
          <div class="form-grid-3">
            <div class="form-group">
              <label>Airline Preferred</label>
              <input type="text" id="bf-airline" class="form-control" value="${{f.airline || ""}}" placeholder="e.g. Emirates, Air India">
            </div>
            <div class="form-group">
              <label>No. of Passengers *</label>
              <input type="number" id="bf-pax" class="form-control" value="${{f.pax || 1}}" min="1">
            </div>
            <div class="form-group">
              <label>Trip Type</label>
              <select id="bf-triptype" class="form-control">
                <option value="Return" ${{f.tripType === "Return" ? "selected" : ""}}>Return Trip</option>
                <option value="One way" ${{f.tripType === "One way" ? "selected" : ""}}>One Way</option>
                <option value="Multi-city" ${{f.tripType === "Multi-city" ? "selected" : ""}}>Multi-City</option>
              </select>
            </div>
          </div>
          <div class="form-group">
            <label>Passenger Names (as on Passport - full list)</label>
            <textarea id="bf-paxnames" class="form-control" rows="2" placeholder="1. Name / Title   2. Name / Title">${{f.paxNames || ""}}</textarea>
          </div>
        `;
      }} else if (f.service === "hotel") {{
        return `
          <div class="form-grid-4">
            <div class="form-group">
              <label>Hotel Name *</label>
              <input type="text" id="bf-hotel" class="form-control" value="${{f.hotel || ""}}" placeholder="e.g. Grand Hyatt">
            </div>
            <div class="form-group">
              <label>City / Location *</label>
              <input type="text" id="bf-city" class="form-control" value="${{f.city || ""}}" placeholder="e.g. Dubai">
            </div>
            <div class="form-group">
              <label>Check-in Date *</label>
              <input type="date" id="bf-checkin" class="form-control" value="${{f.checkin || ""}}">
            </div>
            <div class="form-group">
              <label>Check-out Date *</label>
              <input type="date" id="bf-checkout" class="form-control" value="${{f.checkout || ""}}">
            </div>
          </div>
          <div class="form-grid-2">
            <div class="form-group">
              <label>No. of Rooms</label>
              <input type="number" id="bf-rooms" class="form-control" value="${{f.rooms || 1}}" min="1">
            </div>
            <div class="form-group">
              <label>No. of Guests</label>
              <input type="number" id="bf-pax" class="form-control" value="${{f.pax || 1}}" min="1">
            </div>
          </div>
        `;
      }} else if (f.service === "visa") {{
        return `
          <div class="form-grid-4">
            <div class="form-group">
              <label>Destination Country *</label>
              <input type="text" id="bf-country" class="form-control" value="${{f.country || ""}}" placeholder="e.g. UK, Canada, Schengen">
            </div>
            <div class="form-group">
              <label>Visa Category *</label>
              <input type="text" id="bf-visatype" class="form-control" value="${{f.visaType || ""}}" placeholder="e.g. Tourist, Business, Student">
            </div>
            <div class="form-group">
              <label>No. of Applicants *</label>
              <input type="number" id="bf-pax" class="form-control" value="${{f.pax || 1}}" min="1">
            </div>
            <div class="form-group">
              <label>VFS / Biometric Appointment Date</label>
              <input type="date" id="bf-appt" class="form-control" value="${{f.appt || ""}}">
            </div>
          </div>
        `;
      }} else {{
        return `
          <div class="form-grid-3">
            <div class="form-group">
              <label>What is it (Description) *</label>
              <input type="text" id="bf-what" class="form-control" value="${{f.what || ""}}" placeholder="e.g. Travel Insurance, Airport Transfer">
            </div>
            <div class="form-group">
              <label>Service Date *</label>
              <input type="date" id="bf-date" class="form-control" value="${{f.date || ""}}">
            </div>
            <div class="form-group">
              <label>No. of People</label>
              <input type="number" id="bf-pax" class="form-control" value="${{f.pax || 1}}" min="1">
            </div>
          </div>
        `;
      }}
    }}

    /* DMC & SUPPLIER SECTION (USER REQUIREMENT) */
    function renderDmcSupplierSection(f) {{
      return `
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">🏢 DMC / Supplier & Net Rate (B2B)</div>
          </div>
          <div class="sec-body">
            <label style="display:flex; align-items:center; gap:8px; margin-bottom:12px; cursor:pointer;">
              <input type="checkbox" id="bf-salesknows" ${{f.salesKnows ? "checked" : ""}} onchange="toggleDmcInputs(this.checked)">
              <b>I know the DMC / Supplier and the Net Rate</b>
            </label>

            <div id="dmc-inputs-wrapper" style="display:${{f.salesKnows ? "grid" : "none"}};" class="form-grid-3">
              <div class="form-group">
                <label>DMC / Supplier Name *</label>
                <input type="text" id="bf-dmcname" class="form-control" value="${{f.dmcName || ""}}" placeholder="e.g. Desert Rose DMC, Riya, Akbar">
              </div>
              <div class="form-group">
                <label>Net Rate (Supplier Cost ₹) *</label>
                <input type="number" id="bf-dmcnet" class="form-control" value="${{f.dmcNet || f.cost || 0}}" placeholder="₹ 0">
              </div>
              <div class="form-group" style="justify-content:flex-end;">
                <button class="btn btn-outline" style="margin-top:20px;" onclick="quickSaveDmc('${{f.id}}')">Save DMC & Rate</button>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    function toggleDmcInputs(checked) {{
      document.getElementById("dmc-inputs-wrapper").style.display = checked ? "grid" : "none";
    }}

    function quickSaveDmc(fileId) {{
      const f = DB.bookings.find(b => b.id === fileId);
      f.salesKnows = document.getElementById("bf-salesknows").checked;
      f.dmcName = document.getElementById("bf-dmcname").value.trim();
      f.dmcNet = +document.getElementById("bf-dmcnet").value || 0;
      f.cost = f.dmcNet;
      saveData();
      renderMain();
      showToast("DMC Details Saved!");
    }}

    /* FLIGHT TICKETING SECTION */
    function renderFlightTicketingSection(f) {{
      const isResOrAdmin = (currentRole === "res" || currentRole === "admin");
      return `
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">✈️ Reservations: Fare & Flight Ticketing Queue</div>
            <span class="badge ${{f.ticketStatus === "Issued" ? "badge-success" : "badge-warning"}}">${{f.ticketStatus || "Not Issued"}}</span>
          </div>
          <div class="sec-body">
            <div class="form-grid-4">
              <div class="form-group">
                <label>Fare Category</label>
                <select id="bf-faretype" class="form-control">
                  <option value="portal" ${{f.fareType === "portal" ? "selected" : ""}}>Portal Fare (Akbar/Riya/TBO)</option>
                  <option value="group" ${{f.fareType === "group" ? "selected" : ""}}>Group Fare (Reservation Head)</option>
                </select>
              </div>
              <div class="form-group">
                <label>Ticket Status</label>
                <select id="bf-ticketstatus" class="form-control">
                  <option value="Not issued" ${{f.ticketStatus === "Not issued" ? "selected" : ""}}>Not Issued</option>
                  <option value="Issued" ${{f.ticketStatus === "Issued" ? "selected" : ""}}>Issued</option>
                </select>
              </div>
              <div class="form-group">
                <label>PNR *</label>
                <input type="text" id="bf-pnr" class="form-control mono font-weight-bold" value="${{f.pnr || ""}}" placeholder="e.g. W8Q2KP">
              </div>
              <div class="form-group">
                <label>Ticket Number(s)</label>
                <input type="text" id="bf-ticketno" class="form-control" value="${{f.ticketNo || ""}}" placeholder="e.g. EK-176-000000000">
              </div>
            </div>
            <div style="text-align:right;">
              <button class="btn btn-primary btn-sm" onclick="saveFlightTicketing('${{f.id}}')">Update Ticketing Status</button>
            </div>
          </div>
        </div>
      `;
    }}


    /* ========================================================
       CUSTOMER DOCUMENT AUTO-FILL (PDF / TEXT)
       ======================================================== */
    let __docAutoFillTargetFileId = null;

    function triggerCustomerDocImport(fileId) {{
      __docAutoFillTargetFileId = fileId;
      const el = document.getElementById('bf-doc-upload');
      if (el) {{ el.value = ''; el.click(); }}
    }}

    async function handleCustomerDocUpload(input) {{
      const file = input && input.files && input.files[0];
      if (!file) return;
      const status = document.getElementById('bf-doc-import-status');
      const setStatus = (msg, isErr) => {{
        if (!status) return;
        status.textContent = msg;
        status.style.color = isErr ? 'var(--danger, #DC2626)' : 'var(--success, #16A34A)';
      }};
      setStatus('Reading document...', false);
      try {{
        let text = '';
        const name = (file.name || '').toLowerCase();
        if (file.type === 'application/pdf' || name.endsWith('.pdf')) {{
          text = await extractTextFromPdfFile(file);
        }} else {{
          text = await readFileAsText(file);
        }}
        text = (text || '').replace(/\r/g, '');
        if (!text.trim()) {{
          setStatus('No readable text found. Use a text-based PDF or paste details manually.', true);
          return;
        }}
        const parsed = parseCustomerDetailsFromText(text);
        const applied = applyParsedCustomerDetails(parsed, __docAutoFillTargetFileId);
        if (applied.length) {{
          setStatus('Auto-filled: ' + applied.join(', ') + '. Please review before saving.', false);
          showToast('Customer details auto-filled from document');
        }} else {{
          setStatus('Document read, but no matching customer fields were detected. Please fill manually.', true);
        }}
      }} catch (err) {{
        console.error(err);
        setStatus('Could not read this document. Try another PDF/text file or fill manually.', true);
      }}
    }}

    function readFileAsText(file) {{
      return new Promise((resolve, reject) => {{
        const reader = new FileReader();
        reader.onload = () => resolve(String(reader.result || ''));
        reader.onerror = reject;
        reader.readAsText(file);
      }});
    }}

    async function extractTextFromPdfFile(file) {{
      const buf = await file.arrayBuffer();
      if (window.pdfjsLib && window.pdfjsLib.getDocument) {{
        try {{
          if (window.pdfjsLib.GlobalWorkerOptions && !window.pdfjsLib.GlobalWorkerOptions.workerSrc) {{
            window.pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
          }}
          const pdf = await window.pdfjsLib.getDocument({{ data: buf }}).promise;
          let out = '';
          const maxPages = Math.min(pdf.numPages, 20);
          for (let i = 1; i <= maxPages; i++) {{
            const page = await pdf.getPage(i);
            const content = await page.getTextContent();
            const strings = (content.items || []).map(it => it.str).filter(Boolean);
            out += strings.join(' ') + '\n';
          }}
          if (out.trim()) return out;
        }} catch (e) {{
          console.warn('PDF.js extraction failed, falling back to raw scan', e);
        }}
      }}
      const raw = new TextDecoder('utf-8', {{ fatal: false }}).decode(new Uint8Array(buf));
      const matches = raw.match(/\(([^()]{{2,}})\)\s*Tj|\[(.*?)\]\s*TJ/g) || [];
      let text = matches.map(m => m.replace(/^\(|\)\s*Tj$/g, '').replace(/^\[|\]\s*TJ$/g, '').replace(/\(([^)]*)\)/g, '$1')).join(' ');
      if (!text.trim()) text = raw.replace(/[^\x09\x0A\x0D\x20-\x7E]/g, ' ');
      return text;
    }}

    function parseCustomerDetailsFromText(text) {{
      const clean = String(text || '').replace(/\t/g, ' ').replace(/[ ]{{2,}}/g, ' ').trim();
      const lines = clean.split(/\n+/).map(l => l.trim()).filter(Boolean);
      const label = (names) => {{
        const re = new RegExp('(?:^|\\b)(?:' + names + ')\\s*[:\\-]\\s*(.+)$', 'i');
        for (const line of lines) {{
          const m = line.match(re);
          if (m && m[1]) return m[1].trim();
        }}
        return '';
      }};

      let name = label('Client Name|Customer Name|Passenger Name|Lead Passenger|Name|Full Name|Traveller Name|Traveler Name');
      if (!name) {{
        for (const line of lines.slice(0, 12)) {{
          if (/^(invoice|ticket|booking|pnr|date|address|phone|mobile|email|passport|from|to|flight|airline|total|amount|gst|itinerary)/i.test(line)) continue;
          if (/^[A-Z][a-z]+(?:\s+[A-Z][a-z]+){{1,3}}$/.test(line) && line.length <= 40) {{ name = line; break; }}
        }}
      }}

      let mobile = label('Mobile|Phone|Contact|WhatsApp|Tel|Telephone');
      if (!mobile) {{
        const m = clean.match(/(?:\+?\d{{1,3}}[\s\-]?)?(?:\(?\d{{2,5}}\)?[\s\-]?)?\d{{3,5}}[\s\-]?\d{{4,6}}/);
        if (m) mobile = m[0].trim();
      }}

      let email = label('Email|E-mail');
      if (!email) {{
        const m = clean.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{{2,}}/i);
        if (m) email = m[0].trim();
      }}

      let address = label('Address|Billing Address|City|Location');
      if (!address) {{
        const idx = lines.findIndex(l => /^address\b/i.test(l));
        if (idx >= 0) {{
          address = lines.slice(idx, idx + 2).join(', ').replace(/^address\s*[:\-]\s*/i, '').trim();
        }}
      }}

      const paxNames = label('Passenger Names|Passengers|Pax Names|Traveller Names|Traveler Names');
      const pnr = label('PNR|Booking Reference|Booking Ref');
      const passport = label('Passport|Passport No|Passport Number');
      const from = label('From|Origin|Departure From');
      const to = label('To|Destination|Arrival To');
      const dest = label('Destination|Tour Destination|Package Destination|City\\/Location');
      const paxCount = label('Pax|Passengers Count|No\\. of Passengers|No\\. of People|Adults');

      const dateMatches = clean.match(/\b(20\d{{2}}[-\/]\d{{1,2}}[-\/]\d{{1,2}}|\d{{1,2}}[-\/]\d{{1,2}}[-\/]20\d{{2}})\b/g) || [];
      const normDate = (d) => {{
        if (!d) return '';
        let m = d.match(/^(\d{{4}})[-\/](\d{{1,2}})[-\/](\d{{1,2}})$/);
        if (m) return m[1] + '-' + m[2].padStart(2,'0') + '-' + m[3].padStart(2,'0');
        m = d.match(/^(\d{{1,2}})[-\/](\d{{1,2}})[-\/](\d{{4}})$/);
        if (m) return m[3] + '-' + m[2].padStart(2,'0') + '-' + m[1].padStart(2,'0');
        return '';
      }};

      return {{
        name, mobile, email, address, paxNames, pnr, passport, from, to, dest, paxCount,
        dates: dateMatches.map(normDate).filter(Boolean)
      }};
    }}

    function applyParsedCustomerDetails(p, fileId) {{
      const applied = [];
      const setVal = (id, val) => {{
        if (!val) return false;
        const el = document.getElementById(id);
        if (!el) return false;
        if (String(el.value || '').trim() && String(el.value).trim() === String(val).trim()) return false;
        el.value = val;
        el.dispatchEvent(new Event('input', {{ bubbles: true }}));
        el.dispatchEvent(new Event('change', {{ bubbles: true }}));
        return true;
      }};

      if (setVal('bf-client', p.name)) applied.push('Client Name');
      if (setVal('bf-mobile', p.mobile)) applied.push('Mobile');
      if (setVal('bf-address', p.address || p.email)) applied.push(p.address ? 'Address' : 'Contact Info');

      if (setVal('bf-dest', p.dest || p.to)) applied.push('Destination');
      if (setVal('bf-from', p.from)) applied.push('From');
      if (setVal('bf-to', p.to || p.dest)) applied.push('To');
      if (setVal('bf-pnr', p.pnr)) applied.push('PNR');
      if (setVal('bf-paxnames', p.paxNames || (p.passport ? ('Passport: ' + p.passport) : ''))) applied.push(p.paxNames ? 'Passenger Names' : 'Passport');
      if (p.paxCount) {{
        const n = parseInt(String(p.paxCount).replace(/[^0-9]/g, ''), 10);
        if (n > 0 && setVal('bf-pax', String(n))) applied.push('Pax');
      }}
      if (p.dates && p.dates.length) {{
        if (setVal('bf-start', p.dates[0])) applied.push('Start/Travel Date');
        if (setVal('bf-depart', p.dates[0])) applied.push('Departure Date');
        if (p.dates[1]) {{
          if (setVal('bf-end', p.dates[1])) applied.push('End Date');
          if (setVal('bf-ret', p.dates[1])) applied.push('Return Date');
          if (setVal('bf-checkout', p.dates[1])) applied.push('Checkout Date');
        }}
        if (setVal('bf-checkin', p.dates[0])) applied.push('Check-in Date');
        if (setVal('bf-date', p.dates[0])) applied.push('Service Date');
        if (setVal('bf-appt', p.dates[0])) applied.push('Appointment Date');
      }}

      try {{
        if (fileId) {{
          const f = DB.bookings.find(b => b.id === fileId);
          if (f) saveFormValuesToRecord(f);
        }}
      }} catch (e) {{}}
      return Array.from(new Set(applied));
    }}


    function saveFlightTicketing(fileId) {{
      const f = DB.bookings.find(b => b.id === fileId);
      f.fareType = document.getElementById("bf-faretype").value;
      f.ticketStatus = document.getElementById("bf-ticketstatus").value;
      f.pnr = document.getElementById("bf-pnr").value.trim();
      f.ticketNo = document.getElementById("bf-ticketno").value.trim();
      if (f.ticketStatus === "Issued" && !f.issueDate) {{
        f.issueDate = new Date().toISOString().slice(0, 10);
      }}
      addLog(currentUser, ROLES[currentRole].label, f.id, "Ticket updated", `${{f.ticketStatus}} · PNR ${{f.pnr}}`);
      saveData();
      renderMain();
      showToast("Flight Ticketing Details Saved!");
    }}

    /* VISA TRACKING SECTION */
    function renderVisaTrackingSection(f) {{
      return `
        <div class="sec-card" style="border-left:4px solid var(--visa);">
          <div class="sec-head">
            <div class="sec-title" style="color:var(--visa);">🛂 Visa Processing & VFS Appointment</div>
            <span class="badge badge-visa">${{f.visaStatus || "Document Collection"}}</span>
          </div>
          <div class="sec-body">
            <div class="form-grid-3">
              <div class="form-group">
                <label>Current Visa Stage</label>
                <select id="bf-visastatus" class="form-control">
                  <option value="Document Collection" ${{f.visaStatus === "Document Collection" ? "selected" : ""}}>1. Document Collection</option>
                  <option value="VFS Appointment Scheduled" ${{f.visaStatus === "VFS Appointment Scheduled" ? "selected" : ""}}>2. VFS Appointment Scheduled</option>
                  <option value="Under Process at VFS" ${{f.visaStatus === "Under Process at VFS" ? "selected" : ""}}>3. Under Process at VFS</option>
                  <option value="Approved" ${{f.visaStatus === "Approved" ? "selected" : ""}}>4. Approved</option>
                  <option value="Rejected" ${{f.visaStatus === "Rejected" ? "selected" : ""}}>5. Rejected</option>
                  <option value="Delivered to Client" ${{f.visaStatus === "Delivered to Client" ? "selected" : ""}}>6. Delivered to Client</option>
                </select>
              </div>
              <div class="form-group">
                <label>VFS / Embassy Date</label>
                <input type="date" id="bf-vfsdate" class="form-control" value="${{f.appt || ""}}">
              </div>
              <div class="form-group" style="justify-content:flex-end;">
                <label style="display:flex; align-items:center; gap:8px; cursor:pointer; padding-top:20px;">
                  <input type="checkbox" id="bf-docs" ${{f.docsChecked ? "checked" : ""}}>
                  <b>✓ All Required Documents Verified</b>
                </label>
              </div>
            </div>
            <div style="text-align:right; margin-top:8px;">
              <button class="btn btn-primary btn-sm" onclick="saveVisaDeskUpdates('${{f.id}}')">Update Visa Status</button>
            </div>
          </div>
        </div>
      `;
    }}

    function saveVisaDeskUpdates(fileId) {{
      const f = DB.bookings.find(b => b.id === fileId);
      f.visaStatus = document.getElementById("bf-visastatus").value;
      f.appt = document.getElementById("bf-vfsdate").value;
      f.docsChecked = document.getElementById("bf-docs").checked;
      addLog(currentUser, ROLES[currentRole].label, f.id, "Visa status updated", f.visaStatus);
      saveData();
      renderMain();
      showToast("Visa Application Updated!");
    }}

    /* SAVE & SUBMIT HANDLERS */
    function submitBookingToDepartments(fileId) {{
      const f = DB.bookings.find(b => b.id === fileId);
      saveFormValuesToRecord(f);

      if (!f.client || !f.mobile) {{
        alert("Please enter at least Client Name and Mobile number.");
        return;
      }}

      f.submitted = true;
      addLog(currentUser, ROLES[currentRole].label, f.id, "Booking submitted", f.service.toUpperCase());
      saveData();
      renderMain();
      showToast("Booking Submitted! Operations & Accounts notified.");
    }}

    function saveBookingChanges(fileId) {{
      const f = DB.bookings.find(b => b.id === fileId);
      saveFormValuesToRecord(f);
      addLog(currentUser, ROLES[currentRole].label, f.id, "Booking details updated", f.client);
      saveData();
      renderMain();
      showToast("All Changes Saved!");
    }}

    function saveFormValuesToRecord(f) {{
      f.client = document.getElementById("bf-client").value.trim();
      f.mobile = document.getElementById("bf-mobile").value.trim();
      f.address = document.getElementById("bf-address").value.trim();

      if (f.service === "tour") {{
        f.dest = document.getElementById("bf-dest").value.trim();
        f.start = document.getElementById("bf-start").value;
        f.end = document.getElementById("bf-end").value;
        f.pax = +document.getElementById("bf-pax").value || 1;
      }} else if (f.service === "flight") {{
        f.from = document.getElementById("bf-from").value.trim();
        f.to = document.getElementById("bf-to").value.trim();
        f.depart = document.getElementById("bf-depart").value;
        f.ret = document.getElementById("bf-ret").value;
        f.airline = document.getElementById("bf-airline").value.trim();
        f.pax = +document.getElementById("bf-pax").value || 1;
        f.tripType = document.getElementById("bf-triptype").value;
        f.paxNames = document.getElementById("bf-paxnames").value.trim();
      }} else if (f.service === "hotel") {{
        f.hotel = document.getElementById("bf-hotel").value.trim();
        f.city = document.getElementById("bf-city").value.trim();
        f.checkin = document.getElementById("bf-checkin").value;
        f.checkout = document.getElementById("bf-checkout").value;
        f.rooms = +document.getElementById("bf-rooms").value || 1;
        f.pax = +document.getElementById("bf-pax").value || 1;
      }} else if (f.service === "visa") {{
        f.country = document.getElementById("bf-country").value.trim();
        f.visaType = document.getElementById("bf-visatype").value.trim();
        f.pax = +document.getElementById("bf-pax").value || 1;
        f.appt = document.getElementById("bf-appt").value;
      }} else if (f.service === "other") {{
        f.what = document.getElementById("bf-what").value.trim();
        f.date = document.getElementById("bf-date").value;
        f.pax = +document.getElementById("bf-pax").value || 1;
      }}

      // DMC checkbox & inputs
      const sKnows = document.getElementById("bf-salesknows");
      if (sKnows) {{
        f.salesKnows = sKnows.checked;
        if (f.salesKnows) {{
          f.dmcName = document.getElementById("bf-dmcname").value.trim();
          f.dmcNet = +document.getElementById("bf-dmcnet").value || 0;
          f.cost = f.dmcNet;
        }}
      }}
    }}

    function addClientPaymentEntry(fileId) {{
      const f = DB.bookings.find(b => b.id === fileId);
      const amt = +document.getElementById("new-pay-amt").value;
      if (!amt || amt <= 0) {{
        alert("Please enter a valid payment amount.");
        return;
      }}
      const date = document.getElementById("new-pay-date").value;
      const mode = document.getElementById("new-pay-mode").value;
      const ref = document.getElementById("new-pay-ref").value.trim();

      f.receipts.push({{
        date,
        amount: amt,
        mode,
        ref,
        by: currentUser,
        verified: (currentRole === "accounts" || currentRole === "admin")
      }});

      addLog(currentUser, ROLES[currentRole].label, f.id, "Client payment added", `${{formatINR(amt)}} · ${{mode}}`);
      saveData();
      renderMain();
      showToast("Payment entry added!");
    }}

    function verifyReceipt(fileId, receiptIndex) {{
      const f = DB.bookings.find(b => b.id === fileId);
      if (f.receipts[receiptIndex]) {{
        f.receipts[receiptIndex].verified = true;
        addLog(currentUser, ROLES[currentRole].label, f.id, "Payment verified in bank", formatINR(f.receipts[receiptIndex].amount));
        saveData();
        renderMain();
        showToast("Payment verified!");
      }}
    }}

    /* ========================================================
       PAGE 3: TODAY'S DASHBOARD (ACCOUNTS & ADMIN)
       ======================================================== */
    function renderTodayDashboard(container) {{
      const unverifiedRecs = [];
      DB.bookings.forEach(b => {{
        b.receipts.forEach((r, idx) => {{
          if (!r.verified) unverifiedRecs.push({{ b, r, idx }});
        }});
      }});

      const toPay = DB.bookings.filter(b => b.opsApproved && !b.supplierPaid);
      const readyForInvoice = DB.bookings.filter(b => b.submitted && b.cost > 0 && !b.invoiceNo);

      container.innerHTML = `
        <div class="actionbar">
          <div class="actionbar-title">🌅 Today's Action Center</div>
          <span class="badge badge-brand">${{new Date().toLocaleDateString("en-IN", {{ weekday:'long', year:'numeric', month:'long', day:'numeric' }})}}</span>
        </div>

        <!-- TASK 1: CHECK CLIENT PAYMENTS -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">
              <span class="badge badge-brand">1</span> Check Client Payments in Bank
            </div>
            <span class="badge ${{unverifiedRecs.length ? "badge-warning" : "badge-success"}}">
              ${{unverifiedRecs.length}} Pending Verification
            </span>
          </div>
          <div class="sec-body">
            <p style="color:var(--text-muted); margin-bottom:12px;">Confirm the money has credited to the bank before marking it verified.</p>
            <div class="tbl-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Booking</th>
                    <th>Client</th>
                    <th>Date</th>
                    <th class="num">Amount</th>
                    <th>Mode & Reference</th>
                    <th>Collected By</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  ${{unverifiedRecs.length ? unverifiedRecs.map(item => `
                    <tr>
                      <td><a class="btn-link" onclick="openBookingFile('${{item.b.id}}')">${{item.b.id}}</a></td>
                      <td><strong>${{item.b.client}}</strong></td>
                      <td>${{item.r.date}}</td>
                      <td class="num font-weight-bold" style="color:var(--success);">${{formatINR(item.r.amount)}}</td>
                      <td>${{item.r.mode}}<br><small class="mono text-muted">${{item.r.ref || "—"}}</small></td>
                      <td>${{item.r.by}}</td>
                      <td>
                        <button class="btn btn-success btn-sm" onclick="verifyReceipt('${{item.b.id}}', ${{item.idx}})">Mark Verified</button>
                      </td>
                    </tr>
                  `).join("") : '<tr><td colspan="7" style="text-align:center; padding:16px; color:var(--text-muted);">✓ All client payments are verified in the bank.</td></tr>'}}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- TASK 2: PAY SUPPLIERS -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">
              <span class="badge badge-brand">2</span> Pay Approved Suppliers
            </div>
            <span class="badge ${{toPay.length ? "badge-danger" : "badge-success"}}">
              ${{toPay.length}} Approved by Operations
            </span>
          </div>
          <div class="sec-body">
            <p style="color:var(--text-muted); margin-bottom:12px;">Operations has given clearance. Transfer the money and enter the UTR number.</p>
            <div class="tbl-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Booking</th>
                    <th>Supplier / DMC</th>
                    <th class="num">Amount Due</th>
                    <th>Bank Details</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  ${{toPay.length ? toPay.map(b => `
                    <tr>
                      <td><a class="btn-link" onclick="openBookingFile('${{b.id}}')">${{b.id}}</a><br><small>${{b.client}}</small></td>
                      <td><strong>${{b.dmcName || b.supplier || "Supplier"}}</strong></td>
                      <td class="num font-weight-bold" style="color:var(--owed);">${{formatINR(b.cost)}}</td>
                      <td><small>Direct Bank Transfer / Portal Wallet</small></td>
                      <td>
                        <button class="btn btn-primary btn-sm" onclick="recordSupplierPayout('${{b.id}}')">Mark Paid (Enter UTR)</button>
                      </td>
                    </tr>
                  `).join("") : '<tr><td colspan="5" style="text-align:center; padding:16px; color:var(--text-muted);">✓ No pending supplier payments waiting for payout.</td></tr>'}}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- TASK 3: RAISE INVOICES & VYAPAR -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">
              <span class="badge badge-brand">3</span> Raise Invoices & Enter in Vyapar
            </div>
            <span class="badge badge-purple">${{readyForInvoice.length}} Ready for Invoicing</span>
          </div>
          <div class="sec-body">
            <p style="color:var(--text-muted); margin-bottom:12px;">Costing is confirmed. Generate invoice numbers and record them into Vyapar.</p>
            <div class="tbl-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Booking</th>
                    <th>Client</th>
                    <th class="num">Selling Price</th>
                    <th class="num">Supplier Cost</th>
                    <th class="num" style="color:var(--conf);">Markup</th>
                    <th>Invoice No & Vyapar</th>
                  </tr>
                </thead>
                <tbody>
                  ${{readyForInvoice.length ? readyForInvoice.map(b => `
                    <tr>
                      <td><a class="btn-link" onclick="openBookingFile('${{b.id}}')">${{b.id}}</a></td>
                      <td><strong>${{b.client}}</strong></td>
                      <td class="num">${{formatINR(b.sell)}}</td>
                      <td class="num">${{formatINR(b.cost)}}</td>
                      <td class="num font-weight-bold" style="color:var(--conf);">${{formatINR(b.sell - b.cost)}}</td>
                      <td>
                        <div style="display:flex; gap:6px; align-items:center;">
                          <input type="text" id="today-inv-${{b.id}}" class="form-control" style="width:130px; padding:4px 8px;" placeholder="RH/26/0000">
                          <label style="font-size:11px; display:flex; align-items:center; gap:4px;">
                            <input type="checkbox" id="today-vy-${{b.id}}"> In Vyapar
                          </label>
                          <button class="btn btn-primary btn-sm" onclick="saveTodayInvoice('${{b.id}}')">Save</button>
                        </div>
                      </td>
                    </tr>
                  `).join("") : '<tr><td colspan="6" style="text-align:center; padding:16px; color:var(--text-muted);">✓ All completed bookings are invoiced.</td></tr>'}}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      `;
    }}

    function recordSupplierPayout(fileId) {{
      const b = DB.bookings.find(x => x.id === fileId);
      const utr = prompt(`Enter Payment Reference / UTR for ${{b.dmcName || "Supplier"}} (${{formatINR(b.cost)}}):`);
      if (!utr) return;
      b.supplierPaid = true;
      b.utr = utr;
      addLog(currentUser, ROLES[currentRole].label, b.id, "Supplier paid", `UTR: ${{utr}}`);
      saveData();
      renderMain();
      showToast("Supplier payment recorded!");
    }}

    function saveTodayInvoice(fileId) {{
      const b = DB.bookings.find(x => x.id === fileId);
      const inv = document.getElementById("today-inv-" + fileId).value.trim();
      const vy = document.getElementById("today-vy-" + fileId).checked;
      if (!inv) {{
        alert("Please enter invoice number.");
        return;
      }}
      b.invoiceNo = inv;
      b.vyapar = vy;
      addLog(currentUser, ROLES[currentRole].label, b.id, "Invoice raised", `${{inv}} ${{vy ? "(In Vyapar)" : ""}}`);
      saveData();
      renderMain();
      showToast("Invoice saved for " + b.id);
    }}

    /* ========================================================
       PAGE 4: SUPPLIER PAYMENTS APPROVAL PIPELINE
       ======================================================== */
    function renderSupplierPaymentsPage(container) {{
      const waitingOps = DB.bookings.filter(b => b.submitted && b.cost > 0 && !b.opsApproved);
      const approvedToPay = DB.bookings.filter(b => b.opsApproved && !b.supplierPaid);
      const paidHistory = DB.bookings.filter(b => b.supplierPaid);

      container.innerHTML = `
        <div class="actionbar">
          <div class="actionbar-title">🏢 Supplier Payments Pipeline</div>
          <div class="actionbar-tools">
            <button class="btn btn-outline" onclick="exportSupplierPaymentsExcel()">Export Supplier Payments (Excel)</button>
          </div>
        </div>

        <!-- 1. WAITING FOR OPERATIONS APPROVAL -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">1. Waiting for Operations Approval</div>
            <span class="badge badge-warning">${{waitingOps.length}} Payments</span>
          </div>
          <div class="sec-body">
            <div class="tbl-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Booking</th>
                    <th>Client</th>
                    <th>Supplier / DMC</th>
                    <th class="num">Net Rate</th>
                    <th>Status</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  ${{waitingOps.length ? waitingOps.map(b => `
                    <tr>
                      <td><a class="btn-link" onclick="openBookingFile('${{b.id}}')">${{b.id}}</a></td>
                      <td><strong>${{b.client}}</strong></td>
                      <td>${{b.dmcName || b.supplier || "Supplier"}}</td>
                      <td class="num font-weight-bold">${{formatINR(b.cost)}}</td>
                      <td><span class="badge badge-warning">Awaiting Ops Approval</span></td>
                      <td>
                        ${{(currentRole === "ops" || currentRole === "admin") ? `
                          <button class="btn btn-success btn-sm" onclick="opsApprovePayment('${{b.id}}')">✓ Approve for Payment</button>
                        ` : '<span class="text-muted">Operations Only</span>'}}
                      </td>
                    </tr>
                  `).join("") : '<tr><td colspan="6" style="text-align:center; padding:16px; color:var(--text-muted);">No payments waiting for approval.</td></tr>'}}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 2. APPROVED - TO PAY -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">2. Approved · To Pay Now</div>
            <span class="badge badge-danger">${{approvedToPay.length}} Ready for Payout</span>
          </div>
          <div class="sec-body">
            <div class="tbl-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Booking</th>
                    <th>Supplier / DMC</th>
                    <th class="num">Amount to Pay</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  ${{approvedToPay.length ? approvedToPay.map(b => `
                    <tr>
                      <td><a class="btn-link" onclick="openBookingFile('${{b.id}}')">${{b.id}}</a></td>
                      <td><strong>${{b.dmcName || b.supplier || "Supplier"}}</strong></td>
                      <td class="num font-weight-bold" style="color:var(--owed);">${{formatINR(b.cost)}}</td>
                      <td>
                        <button class="btn btn-primary btn-sm" onclick="recordSupplierPayout('${{b.id}}')">Send Payment & Add UTR</button>
                      </td>
                    </tr>
                  `).join("") : '<tr><td colspan="4" style="text-align:center; padding:16px; color:var(--text-muted);">No approved payments awaiting dispatch.</td></tr>'}}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 3. PAID HISTORY -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">3. Completed Supplier Payouts</div>
            <span class="badge badge-success">${{paidHistory.length}} Completed</span>
          </div>
          <div class="sec-body">
            <div class="tbl-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Booking</th>
                    <th>Supplier</th>
                    <th class="num">Amount Paid</th>
                    <th>UTR / Ref</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  ${{paidHistory.length ? paidHistory.map(b => `
                    <tr>
                      <td><a class="btn-link" onclick="openBookingFile('${{b.id}}')">${{b.id}}</a></td>
                      <td>${{b.dmcName || b.supplier || "Supplier"}}</td>
                      <td class="num font-weight-bold" style="color:var(--success);">${{formatINR(b.cost)}}</td>
                      <td class="mono font-weight-bold">${{b.utr || "—"}}</td>
                      <td><span class="badge badge-success">✓ Paid</span></td>
                    </tr>
                  `).join("") : '<tr><td colspan="5" style="text-align:center; padding:16px; color:var(--text-muted);">No completed payouts yet.</td></tr>'}}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      `;
    }}

    function opsApprovePayment(fileId) {{
      const b = DB.bookings.find(x => x.id === fileId);
      b.opsApproved = true;
      addLog(currentUser, ROLES[currentRole].label, b.id, "Payment approved", `${{formatINR(b.cost)}} to Accounts`);
      saveData();
      renderMain();
      showToast("Approved! Accounts team can now release payment.");
    }}

    /* ========================================================
       PAGE 5: CASH BOOK (MONEY IN & OUT)
       ======================================================== */
    function renderCashBookPage(container) {{
      let cashIn = 0;
      let cashOut = 0;
      const transactions = [];

      DB.bookings.forEach(b => {{
        // Client inflows
        b.receipts.forEach(r => {{
          if (r.verified) {{
            cashIn += +r.amount;
            transactions.push({{
              date: r.date,
              type: "in",
              booking: b.id,
              party: b.client,
              amount: +r.amount,
              mode: r.mode,
              ref: r.ref,
              status: "Verified Inflow"
            }});
          }}
        }});

        // Supplier payouts
        if (b.supplierPaid) {{
          cashOut += +b.cost;
          transactions.push({{
            date: "2026-11-17",
            type: "out",
            booking: b.id,
            party: b.dmcName || b.supplier || "Supplier",
            amount: +b.cost,
            mode: "Bank Transfer",
            ref: b.utr,
            status: "Completed Payout"
          }});
        }}
      }});

      // Sort by date descending
      transactions.sort((a, b) => b.date.localeCompare(a.date));

      container.innerHTML = `
        <div class="stats-row">
          <div class="stat-card">
            <span>Total Money In (Receipts)</span>
            <b style="color:var(--success);">${{formatINR(cashIn)}}</b>
          </div>
          <div class="stat-card">
            <span>Total Money Out (Payments)</span>
            <b style="color:var(--owed);">${{formatINR(cashOut)}}</b>
          </div>
          <div class="stat-card">
            <span>Net Balance in Accounts</span>
            <b style="color:var(--brand);">${{formatINR(cashIn - cashOut)}}</b>
          </div>
        </div>

        <div class="actionbar">
          <div class="actionbar-title">📒 Cash Book & Bank Transactions</div>
          <div class="actionbar-tools">
            <button class="btn btn-outline" onclick="exportCashBookExcel()">Export Cash Book (Excel)</button>
          </div>
        </div>

        <div class="tbl-wrapper">
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Type</th>
                <th>Booking ID</th>
                <th>Client / Supplier Party</th>
                <th class="num">Inflow (+)</th>
                <th class="num">Outflow (−)</th>
                <th>Payment Mode</th>
                <th>UTR / Ref</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              ${{transactions.length ? transactions.map(t => `
                <tr>
                  <td>${{t.date}}</td>
                  <td>${{t.type === "in" ? '<span class="badge badge-success">Receipt</span>' : '<span class="badge badge-owed">Payout</span>'}}</td>
                  <td><a class="btn-link" onclick="openBookingFile('${{t.booking}}')">${{t.booking}}</a></td>
                  <td><strong>${{t.party}}</strong></td>
                  <td class="num" style="color:var(--success); font-weight:700;">${{t.type === "in" ? "+" + formatINR(t.amount) : "—"}}</td>
                  <td class="num" style="color:var(--owed); font-weight:700;">${{t.type === "out" ? "−" + formatINR(t.amount) : "—"}}</td>
                  <td>${{t.mode}}</td>
                  <td class="mono">${{t.ref || "—"}}</td>
                  <td>${{t.status}}</td>
                </tr>
              `).join("") : '<tr><td colspan="9" style="text-align:center; padding:20px; color:var(--text-muted);">No transactions recorded yet.</td></tr>'}}
            </tbody>
          </table>
        </div>
      `;
    }}

    /* ========================================================
       PAGE 6: PROFIT & MARKUP (CONFIDENTIAL EXECUTIVE VIEW)
       ======================================================== */
    function renderProfitMarkupPage(container) {{
      const submittedFiles = DB.bookings.filter(b => b.submitted);
      const totalSold = submittedFiles.reduce((acc, f) => acc + (+f.sell || 0), 0);
      const totalCost = submittedFiles.reduce((acc, f) => acc + (+f.cost || 0), 0);
      const totalMarkup = totalSold - totalCost;
      const avgMarkupPct = totalSold > 0 ? ((totalMarkup / totalSold) * 100).toFixed(1) : "0.0";

      // Group markup by service
      const byService = {{}};
      submittedFiles.forEach(f => {{
        const s = f.service;
        if (!byService[s]) byService[s] = {{ count: 0, sell: 0, cost: 0, mk: 0 }};
        byService[s].count++;
        byService[s].sell += (+f.sell || 0);
        byService[s].cost += (+f.cost || 0);
        byService[s].mk += ((+f.sell || 0) - (+f.cost || 0));
      }});

      container.innerHTML = `
        <div class="sec-card conf">
          <div class="sec-body" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
            <div>
              <h2 style="font-size:18px; font-weight:800; color:var(--conf);">📊 Profit & Margin Executive Dashboard</h2>
              <p style="color:var(--text-muted); font-size:12px;">Confidential financial view visible only to Accounts and Super Admin.</p>
            </div>
            <span class="badge badge-purple" style="font-size:12px; padding:5px 12px;">CONFIDENTIAL</span>
          </div>
        </div>

        <div class="stats-row">
          <div class="stat-card conf">
            <span>Total Sold (Sales)</span>
            <b>${{formatINR(totalSold)}}</b>
          </div>
          <div class="stat-card conf">
            <span>Supplier Direct Cost</span>
            <b>${{formatINR(totalCost)}}</b>
          </div>
          <div class="stat-card conf">
            <span>Total Gross Profit (Markup)</span>
            <b style="color:var(--conf); font-size:26px;">${{formatINR(totalMarkup)}}</b>
          </div>
          <div class="stat-card conf">
            <span>Average Margin %</span>
            <b>${{avgMarkupPct}}%</b>
          </div>
        </div>

        <!-- SERVICE PROFITABILITY BREAKDOWN -->
        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">📈 Profitability by Service Category</div>
          </div>
          <div class="sec-body">
            <div class="tbl-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Service</th>
                    <th>Files</th>
                    <th class="num">Revenue (Sold)</th>
                    <th class="num">Supplier Cost</th>
                    <th class="num" style="color:var(--conf);">Markup Profit</th>
                    <th class="num">Margin %</th>
                  </tr>
                </thead>
                <tbody>
                  ${{Object.entries(byService).map(([svc, d]) => `
                    <tr>
                      <td><strong style="text-transform:uppercase;">${{svc}}</strong></td>
                      <td>${{d.count}}</td>
                      <td class="num">${{formatINR(d.sell)}}</td>
                      <td class="num">${{formatINR(d.cost)}}</td>
                      <td class="num font-weight-bold" style="color:var(--conf);">${{formatINR(d.mk)}}</td>
                      <td class="num">${{d.sell > 0 ? ((d.mk / d.sell) * 100).toFixed(1) + "%" : "—"}}</td>
                    </tr>
                  `).join("")}}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      `;
    }}

    /* ========================================================
       PAGE 7: DMCS & SUPPLIERS DIRECTORY
       ======================================================== */
    function renderSuppliersPage(container) {{
      container.innerHTML = `
        <div class="actionbar">
          <div class="actionbar-title">🏢 DMCs, Flight Portals & Hotel Suppliers</div>
          <button class="btn btn-primary" onclick="openAddSupplierPrompt()">+ Add New DMC / Supplier</button>
        </div>

        <div class="tbl-wrapper">
          <table>
            <thead>
              <tr>
                <th>Supplier Name</th>
                <th>Type</th>
                <th>Country</th>
                <th>How We Pay</th>
                <th>Contact Person & Mobile</th>
                <th>Bank / Account Details</th>
                <th>Payment Terms</th>
              </tr>
            </thead>
            <tbody>
              ${{DB.suppliers.map(s => `
                <tr>
                  <td><strong>${{s.name}}</strong></td>
                  <td><span class="badge badge-brand">${{s.type}}</span></td>
                  <td>${{s.country}}</td>
                  <td>${{s.payBy}}</td>
                  <td>${{s.contact}}<br><small class="mono text-muted">${{s.phone}}</small></td>
                  <td>
                    ${{s.accNo ? `
                      <small><b>${{s.bank}}</b></small><br>
                      <small class="mono">${{s.accNo}}</small><br>
                      <small class="mono text-muted">IFSC/SWIFT: ${{s.code}}</small>
                    ` : '<span class="badge badge-warning">No Bank Info</span>'}}
                  </td>
                  <td><small>${{s.notes || "—"}}</small></td>
                </tr>
              `).join("")}}
            </tbody>
          </table>
        </div>
      `;
    }}

    function openAddSupplierPrompt() {{
      const name = prompt("Enter Supplier / DMC Name:");
      if (!name) return;
      const type = prompt("Type (DMC / Flight portal / Hotel / Visa):", "DMC") || "DMC";
      const payBy = prompt("How we pay (Bank transfer / Portal wallet / Card):", "Bank transfer") || "Bank transfer";
      const bank = prompt("Bank Name:", "");
      const accNo = prompt("Account No / IBAN:", "");
      const code = prompt("IFSC / SWIFT Code:", "");

      DB.suppliers.push({{
        id: "sup-" + (DB.suppliers.length + 1),
        name,
        type,
        payBy,
        country: "India",
        contact: "",
        phone: "",
        email: "",
        notes: "",
        bank,
        accName: name,
        accNo,
        code
      }});

      addLog(currentUser, ROLES[currentRole].label, name, "Supplier created", type);
      saveData();
      renderMain();
      showToast("Supplier Added!");
    }}

    /* ========================================================
       PAGE 8: CHANGE AUDIT LOG
       ======================================================== */
    function renderChangeLogPage(container) {{
      container.innerHTML = `
        <div class="actionbar">
          <div class="actionbar-title">📜 Company Operations Audit Log</div>
          <span class="text-muted" style="font-size:12px;">Track who modified which booking file and when.</span>
        </div>

        <div class="tbl-wrapper">
          <table>
            <thead>
              <tr>
                <th>Date & Time</th>
                <th>Employee / Staff</th>
                <th>Role</th>
                <th>Booking / Target</th>
                <th>Action Taken</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              ${{DB.changeLog.map(l => `
                <tr>
                  <td class="mono">${{l.when}}</td>
                  <td><strong>${{l.who}}</strong></td>
                  <td><span class="badge badge-brand">${{l.role}}</span></td>
                  <td><strong class="mono" style="color:var(--brand);">${{l.file}}</strong></td>
                  <td>${{l.what}}</td>
                  <td class="text-muted">${{l.change || "—"}}</td>
                </tr>
              `).join("")}}
            </tbody>
          </table>
        </div>
      `;
    }}

    /* ========================================================
       PAGE 9: ACCESS RULES (SUPER ADMIN)
       ======================================================== */
    function renderAccessRulesPage(container) {{
      const r = DB.rules;
      container.innerHTML = `
        <div class="actionbar">
          <div class="actionbar-title">🔐 Staff Access Permissions & Rules</div>
          <button class="btn btn-primary" onclick="saveAccessRules()">Save Rule Changes</button>
        </div>

        <div class="sec-card">
          <div class="sec-head">
            <div class="sec-title">Sales Department Permissions</div>
          </div>
          <div class="sec-body">
            <label class="switch-label">
              <div class="switch-text">
                <b>See only their own bookings</b>
                <small>Off: Sales can view bookings made by other sales agents.</small>
              </div>
              <input type="checkbox" id="rule-ownOnly" class="switch-inp" ${{r.ownOnly ? "checked" : ""}}>
            </label>

            <label class="switch-label">
              <div class="switch-text">
                <b>Enter the DMC and Net Rate</b>
                <small>Allows sales to fill in DMC name and net price at package creation.</small>
              </div>
              <input type="checkbox" id="rule-enterDmc" class="switch-inp" ${{r.enterDmc ? "checked" : ""}}>
            </label>

            <label class="switch-label">
              <div class="switch-text">
                <b>Enter Portal, PNR and Net Fare on Portal Flights</b>
                <small>For tickets staff book directly on portals like Akbar, Riya, TBO.</small>
              </div>
              <input type="checkbox" id="rule-flightNet" class="switch-inp" ${{r.flightNet ? "checked" : ""}}>
            </label>

            <label class="switch-label">
              <div class="switch-text">
                <b>See the Supplier / DMC Name</b>
                <small>Read-only on submitted bookings.</small>
              </div>
              <input type="checkbox" id="rule-seeSupplier" class="switch-inp" ${{r.seeSupplier ? "checked" : ""}}>
            </label>

            <label class="switch-label">
              <div class="switch-text">
                <b>See the Supplier Cost (Net Rate)</b>
                <small>Read-only on submitted bookings.</small>
              </div>
              <input type="checkbox" id="rule-seeCost" class="switch-inp" ${{r.seeCost ? "checked" : ""}}>
            </label>

            <label class="switch-label">
              <div class="switch-text">
                <b>See the Markup (Profit Margin)</b>
                <small>Confidential: Usually reserved for Accounts and Admin.</small>
              </div>
              <input type="checkbox" id="rule-seeMarkup" class="switch-inp" ${{r.seeMarkup ? "checked" : ""}}>
            </label>

            <label class="switch-label">
              <div class="switch-text">
                <b>Edit Client and Trip Details After Submitting</b>
                <small>Off: Booking locks once submitted to Operations.</small>
              </div>
              <input type="checkbox" id="rule-editAfter" class="switch-inp" ${{r.editAfter ? "checked" : ""}}>
            </label>

            <label class="switch-label">
              <div class="switch-text">
                <b>Change the Price After Submitting</b>
                <small>Off: Only Accounts can edit pricing once submitted.</small>
              </div>
              <input type="checkbox" id="rule-editPriceAfter" class="switch-inp" ${{r.editPriceAfter ? "checked" : ""}}>
            </label>

            <label class="switch-label">
              <div class="switch-text">
                <b>Export Booking Lists to Excel or PDF</b>
                <small>Allow sales to download reports.</small>
              </div>
              <input type="checkbox" id="rule-canExport" class="switch-inp" ${{r.canExport ? "checked" : ""}}>
            </label>
          </div>
        </div>
      `;
    }}

    function saveAccessRules() {{
      DB.rules.ownOnly = document.getElementById("rule-ownOnly").checked;
      DB.rules.enterDmc = document.getElementById("rule-enterDmc").checked;
      DB.rules.flightNet = document.getElementById("rule-flightNet").checked;
      DB.rules.seeSupplier = document.getElementById("rule-seeSupplier").checked;
      DB.rules.seeCost = document.getElementById("rule-seeCost").checked;
      DB.rules.seeMarkup = document.getElementById("rule-seeMarkup").checked;
      DB.rules.editAfter = document.getElementById("rule-editAfter").checked;
      DB.rules.editPriceAfter = document.getElementById("rule-editPriceAfter").checked;
      DB.rules.canExport = document.getElementById("rule-canExport").checked;
      saveData();
      showToast("Access rules updated successfully!");
    }}

    /* ========================================================
       PAGE 10: SECURITY & LOGIN HISTORY (ADMIN)
       ======================================================== */
    function renderSecurityLogsPage(container) {{
      container.innerHTML = `
        <div class="actionbar">
          <div class="actionbar-title">🛡️ Employee Login History & Security Audit</div>
        </div>

        <div class="tbl-wrapper">
          <table>
            <thead>
              <tr>
                <th>Login Timestamp</th>
                <th>Employee / Username</th>
                <th>Role / Department</th>
                <th>Network Workstation</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              ${{DB.loginLog.map(l => `
                <tr>
                  <td class="mono font-weight-bold">${{l.time}}</td>
                  <td><strong>${{l.user}}</strong></td>
                  <td><span class="badge badge-brand">${{l.role}}</span></td>
                  <td>${{l.ip}}</td>
                  <td><span class="badge badge-success">✓ Authorized Session</span></td>
                </tr>
              `).join("")}}
            </tbody>
          </table>
        </div>
      `;
    }}

    /* ========================================================
       EXPORTS: EXCEL & PDF UTILITIES
       ======================================================== */
    function exportBookingsExcel() {{
      if (typeof XLSX === "undefined") {{
        alert("Export tool loading... please try again in a moment.");
        return;
      }}
      const data = DB.bookings.map(b => ({{
        "Booking ID": b.id,
        "Client Name": b.client,
        "Mobile": b.mobile,
        "Service": b.service.toUpperCase(),
        "Trip": b.dest || b.country || (b.from ? b.from + " - " + b.to : ""),
        "Selling Price": b.sell,
        "Supplier Cost": b.cost,
        "Markup": b.sell - b.cost,
        "Invoice No": b.invoiceNo || "Pending",
        "Submitted": b.submitted ? "Yes" : "Draft"
      }}));

      const ws = XLSX.utils.json_to_sheet(data);
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws, "Bookings");
      XLSX.writeFile(wb, `Romford_Bookings_${{new Date().toISOString().slice(0, 10)}}.xlsx`);
      showToast("Excel Export Downloaded!");
    }}

    function exportBookingsPDF() {{
      if (!window.jspdf || !window.jspdf.jsPDF) {{
        alert("PDF generator loading... please try again.");
        return;
      }}
      const {{ jsPDF }} = window.jspdf;
      const doc = new jsPDF({{ orientation: "landscape" }});

      doc.setFontSize(16);
      doc.setTextColor(21, 58, 104);
      doc.text("ROMFORD HOLIDAYS - BOOKINGS REPORT", 14, 18);
      doc.setFontSize(10);
      doc.setTextColor(100, 116, 139);
      doc.text(`Generated on ${{new Date().toLocaleDateString("en-IN")}} by ${{currentUser}}`, 14, 25);

      const headers = [["ID", "Client", "Mobile", "Service", "Trip", "Price", "Cost", "Markup", "Status"]];
      const rows = DB.bookings.map(b => [
        b.id,
        b.client,
        b.mobile,
        b.service.toUpperCase(),
        b.dest || b.country || (b.from ? b.from + "-" + b.to : ""),
        formatINR(b.sell),
        formatINR(b.cost),
        formatINR(b.sell - b.cost),
        b.submitted ? "Submitted" : "Draft"
      ]);

      doc.autoTable({{
        head: headers,
        body: rows,
        startY: 32,
        theme: "grid",
        headStyles: {{ fillColor: [21, 58, 104] }}
      }});

      doc.save(`Romford_Bookings_${{new Date().toISOString().slice(0, 10)}}.pdf`);
      showToast("PDF Export Downloaded!");
    }}

    function exportCashBookExcel() {{
      alert("Downloading Cash Book...");
    }}

    function exportSupplierPaymentsExcel() {{
      alert("Downloading Supplier Payments...");
    }}
  </script>
</body>
</html>
'''

with open('generated_legacy_full.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated legacy reference only; the maintained app is index.html.")
