import base64

with open('logo_b64.txt', 'r', encoding='utf-8') as f:
    b64_logo = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Romford Holidays - Office ERP & Booking Management</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #153A68;
      --primary-dark: #0e2747;
      --primary-light: #eaf1fa;
      --accent: #2563EB;
      --accent-soft: #EFF6FF;
      --bg: #F8FAFC;
      --card-bg: #FFFFFF;
      --text: #0F172A;
      --muted: #64748B;
      --border: #E2E8F0;
      --success: #16A34A;
      --success-soft: #DCFCE7;
      --warning: #D97706;
      --warning-soft: #FEF3C7;
      --danger: #DC2626;
      --danger-soft: #FEE2E2;
      --purple: #7C3AED;
      --purple-soft: #F3E8FF;
      --visa-color: #0D9488;
      --visa-soft: #CCFBF1;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --radius: 12px;
      --radius-sm: 8px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--text);
      font-size: 14px;
      line-height: 1.5;
      min-height: 100vh;
    }}
    input, select, textarea, button {{ font-family: inherit; font-size: inherit; }}
    .mono {{ font-family: 'JetBrains Mono', monospace; }}

    /* UTILITIES */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 600;
      white-space: nowrap;
    }}
    .badge-success {{ background: var(--success-soft); color: var(--success); }}
    .badge-warning {{ background: var(--warning-soft); color: var(--warning); }}
    .badge-danger {{ background: var(--danger-soft); color: var(--danger); }}
    .badge-purple {{ background: var(--purple-soft); color: var(--purple); }}
    .badge-primary {{ background: var(--primary-light); color: var(--primary); }}
    .badge-visa {{ background: var(--visa-soft); color: var(--visa-color); }}
    .badge-muted {{ background: #f1f5f9; color: var(--muted); }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 13px;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .btn-primary {{ background: var(--primary); color: #fff; }}
    .btn-primary:hover {{ background: var(--primary-dark); }}
    .btn-outline {{ background: #fff; border-color: var(--border); color: var(--text); }}
    .btn-outline:hover {{ background: #f8fafc; border-color: var(--muted); }}
    .btn-success {{ background: var(--success); color: #fff; }}
    .btn-danger {{ background: var(--danger); color: #fff; }}
    .btn-sm {{ padding: 5px 10px; font-size: 12px; }}

    /* LOGIN PAGE */
    #login-screen {{
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      background: radial-gradient(circle at top right, #e0ecfb, #f8fafc 60%);
    }}
    .login-card {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 20px;
      box-shadow: var(--shadow-lg);
      width: 100%;
      max-width: 440px;
      padding: 36px 32px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .login-brand {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 12px;
    }}
    .company-logo {{
      max-height: 64px;
      max-width: 220px;
      object-fit: contain;
    }}
    .login-brand h1 {{
      font-size: 22px;
      font-weight: 800;
      color: var(--primary);
      letter-spacing: -0.5px;
    }}
    .login-brand p {{
      font-size: 13px;
      color: var(--muted);
    }}
    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .form-group label {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text);
    }}
    .form-control {{
      width: 100%;
      padding: 10px 14px;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      outline: none;
      transition: border 0.15s;
      background: #fff;
    }}
    .form-control:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
    }}
    .role-select-box {{
      background: var(--primary-light);
      border: 1.5px solid #bdd6f5;
      border-radius: 12px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .role-select-box label {{
      color: var(--primary);
      font-weight: 700;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .role-select-box select {{
      border: 1px solid #94b9e6;
      border-radius: 8px;
      padding: 10px;
      font-size: 14px;
      font-weight: 600;
      color: var(--primary-dark);
      background: #fff;
      cursor: pointer;
    }}

    /* APP LAYOUT */
    #app-container {{
      display: none;
      min-height: 100vh;
      flex-direction: column;
    }}
    .topbar {{
      background: #fff;
      border-bottom: 1px solid var(--border);
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .topbar-logo {{
      height: 38px;
      max-width: 140px;
      object-fit: contain;
    }}
    .current-dept-badge {{
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .topbar-right {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .user-pill {{
      display: flex;
      align-items: center;
      gap: 10px;
      background: #f1f5f9;
      padding: 4px 12px 4px 6px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 600;
    }}
    .user-avatar {{
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--primary);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
    }}

    /* NAVIGATION TABS */
    .nav-tabs {{
      background: #fff;
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      display: flex;
      gap: 8px;
      overflow-x: auto;
    }}
    .nav-tab {{
      padding: 12px 16px;
      border: 0;
      background: transparent;
      font-weight: 600;
      font-size: 13px;
      color: var(--muted);
      cursor: pointer;
      border-bottom: 3px solid transparent;
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
    }}
    .nav-tab.active {{
      color: var(--primary);
      border-bottom-color: var(--primary);
    }}
    .nav-tab:hover:not(.active) {{
      color: var(--text);
    }}

    /* MAIN CONTENT */
    .main-body {{
      padding: 24px;
      max-width: 1400px;
      width: 100%;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
      flex: 1;
    }}

    /* METRIC STATS */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 16px;
    }}
    .stat-card {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      box-shadow: var(--shadow-sm);
    }}
    .stat-card.highlight {{
      border-left: 4px solid var(--primary);
    }}
    .stat-card.purple {{ border-left: 4px solid var(--purple); background: #faf7ff; }}
    .stat-card.warning {{ border-left: 4px solid var(--warning); }}
    .stat-card.success {{ border-left: 4px solid var(--success); }}
    .stat-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--muted);
    }}
    .stat-val {{
      font-size: 24px;
      font-weight: 800;
      color: var(--text);
    }}
    .stat-sub {{
      font-size: 12px;
      color: var(--muted);
    }}

    /* TABLES & PANELS */
    .panel {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
    }}
    .panel-header {{
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .panel-title {{
      font-size: 16px;
      font-weight: 700;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .table-container {{
      overflow-x: auto;
      width: 100%;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }}
    th {{
      background: #f8fafc;
      padding: 12px 16px;
      font-weight: 600;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--muted);
      border-bottom: 1px solid var(--border);
      white-space: nowrap;
    }}
    td {{
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
    }}
    tr:last-child td {{ border-bottom: none; }}
    tbody tr:hover {{
      background: #fbfcfe;
    }}
    .text-right {{ text-align: right; }}

    /* MODAL */
    .modal-overlay {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(4px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      z-index: 100;
    }}
    .modal-box {{
      background: #fff;
      border-radius: 16px;
      box-shadow: var(--shadow-lg);
      max-width: 650px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
    }}
    .modal-header {{
      padding: 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .modal-header h3 {{
      font-size: 18px;
      font-weight: 700;
      color: var(--primary);
    }}
    .modal-body {{
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .modal-footer {{
      padding: 16px 20px;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      background: #f8fafc;
    }}

    /* GRID FORM */
    .form-grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }}
    @media(max-width: 600px) {{
      .form-grid-2 {{ grid-template-columns: 1fr; }}
    }}

    /* TOAST */
    #toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0f172a;
      color: #fff;
      padding: 12px 20px;
      border-radius: 10px;
      font-weight: 600;
      font-size: 13px;
      box-shadow: var(--shadow-lg);
      display: none;
      z-index: 120;
    }}
  </style>
</head>
<body>

  <!-- LOGIN SCREEN -->
  <div id="login-screen">
    <div class="login-card">
      <div class="login-brand">
        <img class="company-logo" src="data:image/jpeg;base64,{b64_logo}" alt="Romford Holidays Logo">
        <h1>Office ERP & Operations</h1>
        <p>Romford Holidays Booking & Management System</p>
      </div>

      <div class="role-select-box">
        <label for="login-role">Step 1: Select Your Department / Role</label>
        <select id="login-role">
          <option value="sales">🟢 Sales Department</option>
          <option value="res">🔵 Reservations (Flight & Group Fare)</option>
          <option value="ops">🟠 Operations & Vendor Costing</option>
          <option value="accounts">🟣 Accounts & Management</option>
          <option value="visa">🟡 Visa Consultancy</option>
          <option value="admin">🔴 Super Admin</option>
        </select>
      </div>

      <form id="login-form" onsubmit="handleLogin(event)">
        <div style="display:flex; flex-direction:column; gap:14px;">
          <div class="form-group">
            <label>Username / Staff ID</label>
            <input type="text" id="login-user" class="form-control" placeholder="Enter username" value="admin" required>
          </div>
          <div class="form-group">
            <label>Password</label>
            <input type="password" id="login-pass" class="form-control" placeholder="••••••••" value="admin123" required>
          </div>
          <button type="submit" class="btn btn-primary" style="padding:12px; margin-top:8px; font-size:14px;">
            Login to Dashboard →
          </button>
        </div>
      </form>
      <div style="text-align:center; font-size:11px; color:var(--muted);">
        Secured Internal Office Portal · Romford Holidays
      </div>
    </div>
  </div>

  <!-- APPLICATION CONTAINER -->
  <div id="app-container">
    <!-- TOP BAR -->
    <header class="topbar">
      <div class="topbar-left">
        <img class="topbar-logo" src="data:image/jpeg;base64,{b64_logo}" alt="Romford Logo">
        <div id="dept-badge-header" class="current-dept-badge badge-primary">
          Sales Department
        </div>
      </div>
      <div class="topbar-right">
        <div class="user-pill">
          <div class="user-avatar" id="header-avatar">A</div>
          <span id="header-username">Arjun (Sales)</span>
        </div>
        <button class="btn btn-outline btn-sm" onclick="handleLogout()">Logout</button>
      </div>
    </header>

    <!-- NAVIGATION TABS -->
    <nav class="nav-tabs" id="app-tabs">
      <!-- Rendered dynamically depending on role -->
    </nav>

    <!-- MAIN BODY CONTENT -->
    <main class="main-body" id="main-content">
      <!-- Rendered dynamically -->
    </main>
  </div>

  <!-- MODALS -->
  <div class="modal-overlay" id="modal-overlay">
    <div class="modal-box" id="modal-box">
      <!-- Dynamic modal content -->
    </div>
  </div>

  <div id="toast"></div>

  <script>
    // CORE SYSTEM DATA & STORAGE
    const STORAGE_KEY = "romford_erp_data_v2";

    const DEFAULT_DATA = {{
      bookings: [
        {{
          id: "RH-2026-0001",
          client: "Muhammed Shafi",
          phone: "+91 98470 12345",
          service: "tour",
          dest: "Dubai 5D/4N Package",
          pax: 4,
          travelDate: "2026-12-10",
          sellPrice: 180000,
          received: 50000,
          verified: true,
          supplier: "Desert Rose DMC",
          cost: 142000,
          costPending: false,
          opsApproved: true,
          supplierPaid: false,
          utr: "",
          status: "In Progress",
          owner: "Arjun (Sales)",
          notes: "Family package with Burj Khalifa tickets",
          invoiceNo: "RH/26/0045",
          inVyapar: true
        }},
        {{
          id: "RH-2026-0002",
          client: "Anil Kumar & Family",
          phone: "+91 94471 55667",
          service: "flight",
          dest: "Cochin - London (Return)",
          pax: 2,
          travelDate: "2026-11-28",
          sellPrice: 165000,
          received: 165000,
          verified: true,
          supplier: "Akbar Travels Portal",
          cost: 152000,
          costPending: false,
          opsApproved: true,
          supplierPaid: true,
          utr: "HDFC9823471",
          ticketStatus: "Issued",
          ticketNo: "EK-512-882910",
          pnr: "W8Q2KP",
          fareType: "portal",
          status: "Completed",
          owner: "Arjun (Sales)",
          notes: "Emirates direct flight"
        }}
      ],
      visas: [
        {{
          id: "VISA-2026-001",
          client: "Faisal Rahman",
          phone: "+91 97450 99887",
          country: "United Kingdom",
          type: "Tourist Visa (6 Months)",
          pax: 1,
          fee: 14500,
          collected: 14500,
          vfsDate: "2026-11-25",
          status: "Under Process",
          docsChecked: true,
          submittedBy: "Visa Desk",
          notes: "Biometrics scheduled at VFS Kochi"
        }},
        {{
          id: "VISA-2026-002",
          client: "Dr. Sujatha Nair",
          phone: "+91 98462 33441",
          country: "Schengen (France)",
          type: "Conference Visa",
          pax: 1,
          fee: 12000,
          collected: 5000,
          vfsDate: "2026-12-05",
          status: "Document Collection",
          docsChecked: false,
          submittedBy: "Visa Desk",
          notes: "Awaiting bank statements and invitation letter"
        }}
      ],
      loginLogs: [
        {{ user: "admin", role: "Super Admin", time: "2026-11-17 10:15 AM", ip: "Office-PC-1" }}
      ]
    }};

    let DB = loadDB();

    function loadDB() {{
      try {{
        const stored = localStorage.getItem(STORAGE_KEY);
        return stored ? JSON.parse(stored) : DEFAULT_DATA;
      }} catch(e) {{
        return DEFAULT_DATA;
      }}
    }}

    function saveDB() {{
      try {{
        localStorage.setItem(STORAGE_KEY, JSON.stringify(DB));
      }} catch(e) {{
        console.error("Storage error", e);
      }}
    }}

    // STATE
    let currentRole = "admin";
    let currentUser = "Admin";
    let currentTab = "overview";

    const ROLES_INFO = {{
      sales: {{ name: "Sales Department", color: "var(--primary)", bg: "badge-primary", staff: "Arjun (Sales)" }},
      res: {{ name: "Reservations (Flights)", color: "var(--accent)", bg: "badge-primary", staff: "Reservation Head" }},
      ops: {{ name: "Operations & Costing", color: "var(--warning)", bg: "badge-warning", staff: "Salahu (Ops)" }},
      accounts: {{ name: "Accounts & Management", color: "var(--purple)", bg: "badge-purple", staff: "Accountant" }},
      visa: {{ name: "Visa Consultancy", color: "var(--visa-color)", bg: "badge-visa", staff: "Visa Consultant" }},
      admin: {{ name: "Super Admin", color: "var(--danger)", bg: "badge-danger", staff: "Shahinsha (Admin)" }}
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

    // LOGIN & AUTH
    function handleLogin(e) {{
      e.preventDefault();
      const role = document.getElementById("login-role").value;
      const username = document.getElementById("login-user").value.trim();

      currentRole = role;
      currentUser = username || ROLES_INFO[role].staff;

      // Log login event for Admin
      const now = new Date();
      const timeStr = now.toLocaleDateString("en-IN") + " " + now.toLocaleTimeString("en-IN", {{ hour: '2-digit', minute: '2-digit' }});
      DB.loginLogs.unshift({{
        user: currentUser,
        role: ROLES_INFO[role].name,
        time: timeStr,
        ip: "Office Local Network"
      }});
      saveDB();

      // Switch to app
      document.getElementById("login-screen").style.display = "none";
      document.getElementById("app-container").style.display = "flex";

      // Update header
      document.getElementById("dept-badge-header").innerText = ROLES_INFO[role].name;
      document.getElementById("dept-badge-header").className = "current-dept-badge " + ROLES_INFO[role].bg;
      document.getElementById("header-username").innerText = currentUser;
      document.getElementById("header-avatar").innerText = currentUser.charAt(0).toUpperCase();

      setupNavigation();
      showToast("Welcome! Logged in as " + ROLES_INFO[role].name);
    }}

    function handleLogout() {{
      document.getElementById("app-container").style.display = "none";
      document.getElementById("login-screen").style.display = "flex";
      showToast("Logged out successfully");
    }}

    // NAVIGATION TABS GENERATION
    function setupNavigation() {{
      const nav = document.getElementById("app-tabs");
      nav.innerHTML = "";

      let tabs = [];
      if (currentRole === "sales") {{
        tabs = [
          {{ id: "overview", label: "Sales Dashboard" }},
          {{ id: "bookings", label: "All Client Bookings" }},
          {{ id: "new_booking", label: "+ New Booking File" }}
        ];
      }} else if (currentRole === "res") {{
        tabs = [
          {{ id: "flights", label: "Flight Bookings" }},
          {{ id: "ticketing", label: "Ticketing Queue" }}
        ];
      }} else if (currentRole === "ops") {{
        tabs = [
          {{ id: "costing", label: "Vendor Costing & DMC" }},
          {{ id: "approvals", label: "Supplier Payment Approvals" }}
        ];
      }} else if (currentRole === "accounts") {{
        tabs = [
          {{ id: "receipts", label: "Client Receipts (Bank Check)" }},
          {{ id: "supplier_pays", label: "Supplier Payments to Send" }},
          {{ id: "pnl", label: "Profit & Margin Report" }}
        ];
      }} else if (currentRole === "visa") {{
        tabs = [
          {{ id: "visa_list", label: "Visa Applications" }},
          {{ id: "new_visa", label: "+ New Visa File" }}
        ];
      }} else {{ // admin
        tabs = [
          {{ id: "admin_overview", label: "Super Admin Dashboard" }},
          {{ id: "bookings", label: "All Bookings" }},
          {{ id: "visa_list", label: "Visa Desk" }},
          {{ id: "pnl", label: "Profit & Markups" }},
          {{ id: "login_logs", label: "Employee Login History" }}
        ];
      }}

      currentTab = tabs[0].id;

      tabs.forEach((tab, idx) => {{
        const btn = document.createElement("button");
        btn.className = "nav-tab" + (idx === 0 ? " active" : "");
        btn.innerText = tab.label;
        btn.onclick = () => {{
          document.querySelectorAll(".nav-tab").forEach(t => t.classList.remove("active"));
          btn.classList.add("active");
          currentTab = tab.id;
          renderView();
        }};
        nav.appendChild(btn);
      }});

      renderView();
    }}

    // MAIN VIEW ROUTER
    function renderView() {{
      const main = document.getElementById("main-content");

      if (currentTab === "overview" || currentTab === "admin_overview") {{
        renderOverview(main);
      }} else if (currentTab === "bookings") {{
        renderBookingsList(main);
      }} else if (currentTab === "new_booking") {{
        openNewBookingModal();
      }} else if (currentTab === "flights" || currentTab === "ticketing") {{
        renderReservations(main);
      }} else if (currentTab === "costing" || currentTab === "approvals") {{
        renderOperations(main);
      }} else if (currentTab === "receipts" || currentTab === "supplier_pays" || currentTab === "pnl") {{
        renderAccounts(main);
      }} else if (currentTab === "visa_list") {{
        renderVisa(main);
      }} else if (currentTab === "new_visa") {{
        openNewVisaModal();
      }} else if (currentTab === "login_logs") {{
        renderLoginLogs(main);
      }}
    }}

    // 1. OVERVIEW / DASHBOARD (SALES & ADMIN)
    function renderOverview(container) {{
      const bks = DB.bookings;
      const totalSell = bks.reduce((a, b) => a + (+b.sellPrice || 0), 0);
      const totalRec = bks.reduce((a, b) => a + (+b.received || 0), 0);
      const totalCost = bks.reduce((a, b) => a + (+b.cost || 0), 0);
      const margin = totalSell - totalCost;

      let html = `
        <div class="stats-grid">
          <div class="stat-card highlight">
            <span class="stat-title">Total Bookings</span>
            <div class="stat-val">${{bks.length}} Files</div>
            <span class="stat-sub">Active client files</span>
          </div>
          <div class="stat-card success">
            <span class="stat-title">Total Sales Value</span>
            <div class="stat-val">${{formatINR(totalSell)}}</div>
            <span class="stat-sub">Collected: ${{formatINR(totalRec)}}</span>
          </div>
          <div class="stat-card warning">
            <span class="stat-title">Pending Balance</span>
            <div class="stat-val">${{formatINR(Math.max(0, totalSell - totalRec))}}</div>
            <span class="stat-sub">To collect from clients</span>
          </div>
          ${{currentRole === 'admin' || currentRole === 'accounts' ? `
          <div class="stat-card purple">
            <span class="stat-title">Net Profit / Markup</span>
            <div class="stat-val" style="color:var(--purple);">${{formatINR(margin)}}</div>
            <span class="stat-sub">Gross margin</span>
          </div>` : ''}}
          <div class="stat-card">
            <span class="stat-title">Active Visas</span>
            <div class="stat-val">${{DB.visas.length}} Cases</div>
            <span class="stat-sub">Visa consultancy files</span>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <div class="panel-title">📋 Recent Client Bookings</div>
            <button class="btn btn-primary btn-sm" onclick="openNewBookingModal()">+ Add New Booking</button>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Booking ID</th>
                  <th>Client Name</th>
                  <th>Trip / Service</th>
                  <th>Travel Date</th>
                  <th class="text-right">Selling Price</th>
                  <th class="text-right">Received</th>
                  <th>Payment Status</th>
                  <th>Workflow Stage</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                ${{bks.map(b => `
                  <tr>
                    <td><span class="badge badge-primary mono">${{b.id}}</span></td>
                    <td><strong>${{b.client}}</strong><br><small class="text-muted">${{b.phone}}</small></td>
                    <td>${{b.dest}}<br><small class="badge badge-muted">${{b.service.toUpperCase()}}</small></td>
                    <td>${{b.travelDate || '—'}}</td>
                    <td class="text-right font-weight-bold">${{formatINR(b.sellPrice)}}</td>
                    <td class="text-right text-success">${{formatINR(b.received)}}</td>
                    <td>
                      ${{b.verified ? '<span class="badge badge-success">✓ Verified</span>' : '<span class="badge badge-warning">Pending Check</span>'}}
                    </td>
                    <td><span class="badge badge-primary">${{b.status}}</span></td>
                    <td>
                      <button class="btn btn-outline btn-sm" onclick="openBookingDetail('${{b.id}}')">View & Edit</button>
                    </td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
          </div>
        </div>
      `;
      container.innerHTML = html;
    }}

    // 2. BOOKINGS LIST
    function renderBookingsList(container) {{
      renderOverview(container);
    }}

    // 3. RESERVATIONS (FLIGHTS)
    function renderReservations(container) {{
      const flights = DB.bookings.filter(b => b.service === 'flight');
      container.innerHTML = `
        <div class="stats-grid">
          <div class="stat-card highlight">
            <span class="stat-title">Flight Files</span>
            <div class="stat-val">${{flights.length}}</div>
          </div>
          <div class="stat-card warning">
            <span class="stat-title">Pending Tickets</span>
            <div class="stat-val">${{flights.filter(f => f.ticketStatus !== 'Issued').length}}</div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <div class="panel-title">✈️ Flight Ticketing & PNR Queue</div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Booking ID</th>
                  <th>Passenger / Group</th>
                  <th>Sector & Travel</th>
                  <th>Fare Type</th>
                  <th>PNR</th>
                  <th>Ticket Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                ${{flights.length ? flights.map(f => `
                  <tr>
                    <td><span class="badge badge-primary mono">${{f.id}}</span></td>
                    <td><strong>${{f.client}}</strong> (${{f.pax}} Pax)</td>
                    <td>${{f.dest}}<br><small class="text-muted">Date: ${{f.travelDate}}</small></td>
                    <td><span class="badge badge-muted">${{(f.fareType || 'Portal').toUpperCase()}}</span></td>
                    <td><span class="mono font-weight-bold">${{f.pnr || '—'}}</span></td>
                    <td>
                      ${{f.ticketStatus === 'Issued' 
                        ? `<span class="badge badge-success">✓ Issued (${{f.ticketNo || 'Done'}})</span>`
                        : `<span class="badge badge-warning">Pending Issue</span>`}}
                    </td>
                    <td>
                      <button class="btn btn-primary btn-sm" onclick="promptIssueTicket('${{f.id}}')">
                        ${{f.ticketStatus === 'Issued' ? 'Update PNR' : 'Issue Ticket'}}
                      </button>
                    </td>
                  </tr>
                `).join('') : '<tr><td colspan="7" style="text-align:center; padding:20px;">No flight bookings found.</td></tr>'}}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }}

    function promptIssueTicket(id) {{
      const f = DB.bookings.find(b => b.id === id);
      const pnr = prompt("Enter PNR:", f.pnr || "");
      if (pnr === null) return;
      const tno = prompt("Enter Ticket No / Ref:", f.ticketNo || "");
      if (tno === null) return;

      f.pnr = pnr;
      f.ticketNo = tno;
      f.ticketStatus = "Issued";
      saveDB();
      renderView();
      showToast("Ticket details saved for " + f.id);
    }}

    // 4. OPERATIONS & COSTING
    function renderOperations(container) {{
      container.innerHTML = `
        <div class="panel">
          <div class="panel-header">
            <div class="panel-title">⚙️ Operations: Supplier Costing & Approvals</div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Booking ID</th>
                  <th>Client</th>
                  <th>Supplier / DMC</th>
                  <th class="text-right">Selling Price</th>
                  <th class="text-right">Supplier Cost (B2B)</th>
                  <th>Approval Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                ${{DB.bookings.map(b => `
                  <tr>
                    <td><span class="badge badge-primary mono">${{b.id}}</span></td>
                    <td><strong>${{b.client}}</strong></td>
                    <td>${{b.supplier || '<span class="text-muted">Not Assigned</span>'}}</td>
                    <td class="text-right">${{formatINR(b.sellPrice)}}</td>
                    <td class="text-right font-weight-bold">${{formatINR(b.cost)}}</td>
                    <td>
                      ${{b.opsApproved ? '<span class="badge badge-success">✓ Approved for Payment</span>' : '<span class="badge badge-warning">Pending Approval</span>'}}
                    </td>
                    <td>
                      <button class="btn btn-outline btn-sm" onclick="editCosting('${{b.id}}')">Set Cost / DMC</button>
                      ${{!b.opsApproved ? `<button class="btn btn-success btn-sm" onclick="approveOpsPayment('${{b.id}}')">Approve Payment</button>` : ''}}
                    </td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }}

    function editCosting(id) {{
      const b = DB.bookings.find(x => x.id === id);
      const sup = prompt("Enter DMC / Supplier Name:", b.supplier || "");
      if (sup === null) return;
      const cost = prompt("Enter Net Supplier Cost (₹):", b.cost || "");
      if (cost === null) return;

      b.supplier = sup;
      b.cost = +cost || 0;
      saveDB();
      renderView();
      showToast("Supplier cost updated for " + b.id);
    }}

    function approveOpsPayment(id) {{
      const b = DB.bookings.find(x => x.id === id);
      b.opsApproved = true;
      saveDB();
      renderView();
      showToast("Payment approved for Accounts desk!");
    }}

    // 5. ACCOUNTS & PNL
    function renderAccounts(container) {{
      const bks = DB.bookings;
      const pendingVerify = bks.filter(b => !b.verified);
      const toPay = bks.filter(b => b.opsApproved && !b.supplierPaid);

      container.innerHTML = `
        <div class="stats-grid">
          <div class="stat-card warning">
            <span class="stat-title">Client Receipts to Verify</span>
            <div class="stat-val">${{pendingVerify.length}}</div>
            <span class="stat-sub">Check bank transfer</span>
          </div>
          <div class="stat-card danger">
            <span class="stat-title">Supplier Payments Due</span>
            <div class="stat-val">${{toPay.length}}</div>
            <span class="stat-sub">Approved by Operations</span>
          </div>
          <div class="stat-card purple">
            <span class="stat-title">Total Profit (Markup)</span>
            <div class="stat-val">${{formatINR(bks.reduce((a, b) => a + ((b.sellPrice||0) - (b.cost||0)), 0))}}</div>
            <span class="stat-sub">Accounts visibility</span>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <div class="panel-title">🟣 Accounts: Payments & Invoicing</div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Booking</th>
                  <th>Client / Amount</th>
                  <th>Bank Verification</th>
                  <th>Supplier / Due</th>
                  <th>Supplier Payout</th>
                  <th>Invoice / Vyapar</th>
                </tr>
              </thead>
              <tbody>
                ${{bks.map(b => `
                  <tr>
                    <td><span class="badge badge-primary mono">${{b.id}}</span><br><strong>${{b.client}}</strong></td>
                    <td>Received: <strong class="text-success">${{formatINR(b.received)}}</strong><br><small>Total: ${{formatINR(b.sellPrice)}}</small></td>
                    <td>
                      ${{b.verified 
                        ? '<span class="badge badge-success">✓ Bank Verified</span>' 
                        : `<button class="btn btn-success btn-sm" onclick="verifyClientPayment('${{b.id}}')">Verify Bank Inflow</button>`}}
                    </td>
                    <td>${{b.supplier || '—'}}<br><strong class="text-danger">${{formatINR(b.cost)}}</strong></td>
                    <td>
                      ${{b.supplierPaid 
                        ? `<span class="badge badge-success">✓ Paid (UTR: ${{b.utr}})</span>`
                        : (b.opsApproved 
                            ? `<button class="btn btn-primary btn-sm" onclick="markSupplierPaid('${{b.id}}')">Send Payment & Add UTR</button>` 
                            : '<span class="badge badge-muted">Awaiting Ops Approval</span>')}}
                    </td>
                    <td>
                      <small>Inv: ${{b.invoiceNo || 'Pending'}}</small><br>
                      ${{b.inVyapar ? '<span class="badge badge-purple">In Vyapar</span>' : `<button class="btn btn-outline btn-sm" onclick="tagVyapar('${{b.id}}')">Enter Vyapar</button>`}}
                    </td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }}

    function verifyClientPayment(id) {{
      const b = DB.bookings.find(x => x.id === id);
      b.verified = true;
      saveDB();
      renderView();
      showToast("Client payment verified in bank!");
    }}

    function markSupplierPaid(id) {{
      const b = DB.bookings.find(x => x.id === id);
      const utr = prompt("Enter Bank Transfer UTR / Reference:");
      if (!utr) return;
      b.supplierPaid = true;
      b.utr = utr;
      saveDB();
      renderView();
      showToast("Supplier marked as paid!");
    }}

    function tagVyapar(id) {{
      const b = DB.bookings.find(x => x.id === id);
      const inv = prompt("Enter Invoice No:", b.invoiceNo || "RH/26/0001");
      if (!inv) return;
      b.invoiceNo = inv;
      b.inVyapar = true;
      saveDB();
      renderView();
      showToast("Invoice & Vyapar recorded!");
    }}

    // 6. VISA CONSULTANCY
    function renderVisa(container) {{
      const visas = DB.visas;
      container.innerHTML = `
        <div class="stats-grid">
          <div class="stat-card highlight">
            <span class="stat-title">Total Visa Files</span>
            <div class="stat-val">${{visas.length}}</div>
          </div>
          <div class="stat-card success">
            <span class="stat-title">Approved Visas</span>
            <div class="stat-val">${{visas.filter(v => v.status === 'Approved').length}}</div>
          </div>
          <div class="stat-card warning">
            <span class="stat-title">Under Process / VFS</span>
            <div class="stat-val">${{visas.filter(v => v.status === 'Under Process').length}}</div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <div class="panel-title">🟡 Visa Consultancy Desk</div>
            <button class="btn btn-primary btn-sm" onclick="openNewVisaModal()">+ Add New Visa Applicant</button>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Visa ID</th>
                  <th>Applicant Name</th>
                  <th>Country & Category</th>
                  <th>VFS / Appt Date</th>
                  <th>Documents</th>
                  <th>Visa Fee</th>
                  <th>Current Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                ${{visas.map(v => `
                  <tr>
                    <td><span class="badge badge-visa mono">${{v.id}}</span></td>
                    <td><strong>${{v.client}}</strong><br><small>${{v.phone}}</small></td>
                    <td><strong>${{v.country}}</strong><br><small class="text-muted">${{v.type}}</small></td>
                    <td>${{v.vfsDate || '—'}}</td>
                    <td>
                      ${{v.docsChecked ? '<span class="badge badge-success">✓ Docs Ready</span>' : '<span class="badge badge-warning">Pending Docs</span>'}}
                    </td>
                    <td>${{formatINR(v.fee)}}</td>
                    <td><span class="badge badge-visa">${{v.status}}</span></td>
                    <td>
                      <button class="btn btn-outline btn-sm" onclick="updateVisaStatus('${{v.id}}')">Update Status</button>
                    </td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }}

    function updateVisaStatus(id) {{
      const v = DB.visas.find(x => x.id === id);
      const statuses = ["Document Collection", "Under Process", "VFS Appointment Scheduled", "Approved", "Rejected", "Delivered"];
      const next = prompt("Select / Enter New Status:\\n" + statuses.join("\\n"), v.status);
      if (!next) return;
      v.status = next;
      if (next === "Approved" || next === "VFS Appointment Scheduled") {{
        v.docsChecked = true;
      }}
      saveDB();
      renderView();
      showToast("Visa status updated to: " + next);
    }}

    // 7. EMPLOYEE LOGIN HISTORY (ADMIN ONLY)
    function renderLoginLogs(container) {{
      container.innerHTML = `
        <div class="panel">
          <div class="panel-header">
            <div class="panel-title">🔒 Employee Login & Security Log (Admin Audit)</div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Date & Time</th>
                  <th>Username / Staff</th>
                  <th>Role / Department</th>
                  <th>Login Location / Network</th>
                  <th>Security Status</th>
                </tr>
              </thead>
              <tbody>
                ${{DB.loginLogs.map(l => `
                  <tr>
                    <td class="mono">${{l.time}}</td>
                    <td><strong>${{l.user}}</strong></td>
                    <td><span class="badge badge-primary">${{l.role}}</span></td>
                    <td>${{l.ip}}</td>
                    <td><span class="badge badge-success">✓ Authorized Session</span></td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }}

    // MODAL HANDLERS
    function closeModal() {{
      document.getElementById("modal-overlay").style.display = "none";
    }}

    function openNewBookingModal() {{
      const mbox = document.getElementById("modal-box");
      mbox.innerHTML = `
        <div class="modal-header">
          <h3>+ Create New Booking File</h3>
          <button class="btn btn-outline btn-sm" onclick="closeModal()">✕</button>
        </div>
        <div class="modal-body">
          <div class="form-grid-2">
            <div class="form-group">
              <label>Client Name *</label>
              <input type="text" id="nb-client" class="form-control" placeholder="Full client name" required>
            </div>
            <div class="form-group">
              <label>Mobile Number *</label>
              <input type="text" id="nb-phone" class="form-control" placeholder="+91 98470 00000" required>
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label>Service Category</label>
              <select id="nb-service" class="form-control">
                <option value="tour">Tour Package</option>
                <option value="flight">Flight Ticket</option>
                <option value="hotel">Hotel Booking</option>
                <option value="other">Other Service</option>
              </select>
            </div>
            <div class="form-group">
              <label>Destination / Sector *</label>
              <input type="text" id="nb-dest" class="form-control" placeholder="e.g. Dubai 5D/4N or COK-DXB">
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label>Number of Pax (People)</label>
              <input type="number" id="nb-pax" class="form-control" value="1" min="1">
            </div>
            <div class="form-group">
              <label>Travel Date</label>
              <input type="date" id="nb-date" class="form-control">
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label>Selling Price to Client (₹) *</label>
              <input type="number" id="nb-sell" class="form-control" placeholder="₹ 0">
            </div>
            <div class="form-group">
              <label>Advance Payment Collected (₹)</label>
              <input type="number" id="nb-rec" class="form-control" placeholder="₹ 0">
            </div>
          </div>

          <div class="form-group">
            <label>Notes / Requirements</label>
            <textarea id="nb-notes" class="form-control" rows="2" placeholder="Flight timings, hotel preferences..."></textarea>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-outline" onclick="closeModal()">Cancel</button>
          <button class="btn btn-primary" onclick="submitNewBooking()">Create & Submit Booking</button>
        </div>
      `;
      document.getElementById("modal-overlay").style.display = "flex";
    }}

    function submitNewBooking() {{
      const client = document.getElementById("nb-client").value.trim();
      const phone = document.getElementById("nb-phone").value.trim();
      const service = document.getElementById("nb-service").value;
      const dest = document.getElementById("nb-dest").value.trim();
      const pax = +document.getElementById("nb-pax").value || 1;
      const travelDate = document.getElementById("nb-date").value;
      const sellPrice = +document.getElementById("nb-sell").value || 0;
      const received = +document.getElementById("nb-rec").value || 0;
      const notes = document.getElementById("nb-notes").value.trim();

      if (!client || !phone || !dest) {{
        alert("Please fill in Client Name, Phone, and Destination.");
        return;
      }}

      const id = "RH-2026-" + String(DB.bookings.length + 1).padStart(4, '0');
      const newBk = {{
        id,
        client,
        phone,
        service,
        dest,
        pax,
        travelDate,
        sellPrice,
        received,
        verified: false,
        supplier: "",
        cost: 0,
        costPending: true,
        opsApproved: false,
        supplierPaid: false,
        utr: "",
        status: "Submitted",
        owner: currentUser,
        notes
      }};

      DB.bookings.unshift(newBk);
      saveDB();
      closeModal();
      renderView();
      showToast("New Booking Created: " + id);
    }}

    function openNewVisaModal() {{
      const mbox = document.getElementById("modal-box");
      mbox.innerHTML = `
        <div class="modal-header">
          <h3>+ Add Visa Applicant File</h3>
          <button class="btn btn-outline btn-sm" onclick="closeModal()">✕</button>
        </div>
        <div class="modal-body">
          <div class="form-grid-2">
            <div class="form-group">
              <label>Applicant Name *</label>
              <input type="text" id="nv-client" class="form-control" placeholder="Passport full name" required>
            </div>
            <div class="form-group">
              <label>Phone / WhatsApp *</label>
              <input type="text" id="nv-phone" class="form-control" placeholder="+91 00000 00000" required>
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label>Destination Country *</label>
              <input type="text" id="nv-country" class="form-control" placeholder="e.g. UK, Canada, Schengen, UAE">
            </div>
            <div class="form-group">
              <label>Visa Category</label>
              <input type="text" id="nv-type" class="form-control" placeholder="e.g. Tourist 6 Months, Student, Business">
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label>Visa & Service Fee (₹)</label>
              <input type="number" id="nv-fee" class="form-control" placeholder="₹ 12000">
            </div>
            <div class="form-group">
              <label>VFS / Biometric Appointment Date</label>
              <input type="date" id="nv-date" class="form-control">
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-outline" onclick="closeModal()">Cancel</button>
          <button class="btn btn-primary" onclick="submitNewVisa()">Save Visa Applicant</button>
        </div>
      `;
      document.getElementById("modal-overlay").style.display = "flex";
    }}

    function submitNewVisa() {{
      const client = document.getElementById("nv-client").value.trim();
      const phone = document.getElementById("nv-phone").value.trim();
      const country = document.getElementById("nv-country").value.trim();
      const type = document.getElementById("nv-type").value.trim() || "Tourist Visa";
      const fee = +document.getElementById("nv-fee").value || 0;
      const vfsDate = document.getElementById("nv-date").value;

      if (!client || !country) {{
        alert("Please provide applicant name and destination country.");
        return;
      }}

      const id = "VISA-2026-" + String(DB.visas.length + 1).padStart(3, '0');
      DB.visas.unshift({{
        id,
        client,
        phone,
        country,
        type,
        pax: 1,
        fee,
        collected: 0,
        vfsDate,
        status: "Document Collection",
        docsChecked: false,
        submittedBy: currentUser
      }});

      saveDB();
      closeModal();
      renderView();
      showToast("Visa File Created: " + id);
    }}

    function openBookingDetail(id) {{
      const b = DB.bookings.find(x => x.id === id);
      if (!b) return;

      const mbox = document.getElementById("modal-box");
      mbox.innerHTML = `
        <div class="modal-header">
          <h3>Booking Details · ${{b.id}}</h3>
          <button class="btn btn-outline btn-sm" onclick="closeModal()">✕</button>
        </div>
        <div class="modal-body">
          <div class="form-grid-2">
            <div><strong>Client:</strong> ${{b.client}}</div>
            <div><strong>Phone:</strong> ${{b.phone}}</div>
            <div><strong>Service:</strong> ${{b.service.toUpperCase()}}</div>
            <div><strong>Trip:</strong> ${{b.dest}}</div>
            <div><strong>Selling Price:</strong> ${{formatINR(b.sellPrice)}}</div>
            <div><strong>Received:</strong> ${{formatINR(b.received)}}</div>
            <div><strong>Supplier / DMC:</strong> ${{b.supplier || 'Not set'}}</div>
            <div><strong>Supplier Cost:</strong> ${{formatINR(b.cost)}}</div>
            <div><strong>Ops Approval:</strong> ${{b.opsApproved ? 'Approved' : 'Pending'}}</div>
            <div><strong>Supplier Payout:</strong> ${{b.supplierPaid ? 'Paid (UTR: ' + b.utr + ')' : 'Pending'}}</div>
          </div>
          <div style="margin-top:12px;">
            <strong>Notes:</strong> <p class="text-muted">${{b.notes || 'None'}}</p>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary" onclick="closeModal()">Close</button>
        </div>
      `;
      document.getElementById("modal-overlay").style.display = "flex";
    }}

  </script>
</body>
</html>
'''

with open('generated_legacy_basic.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated legacy reference only; the maintained app is index.html.")
