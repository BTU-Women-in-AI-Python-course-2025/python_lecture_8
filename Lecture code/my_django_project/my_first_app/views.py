from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone
from django.views import View


def home(request):
    return HttpResponse("Welcome to the Home Page!")

def not_found(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Page Not Found</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #ff6a00, #ee0979);
                color: white;
                text-align: center;
                padding: 50px;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
                display: inline-block;
                animation: fadeIn 1.2s ease-in-out;
            }
            h1 {
                font-size: 5rem;
                margin: 0;
            }
            h2 {
                margin: 20px 0;
                font-size: 2rem;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 30px;
            }
            a {
                color: #fff;
                background: rgba(255,255,255,0.2);
                text-decoration: none;
                padding: 12px 25px;
                border-radius: 10px;
                transition: 0.3s;
            }
            a:hover {
                background: rgba(255,255,255,0.35);
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>404</h1>
            <h2>Page Not Found</h2>
            <p>Oops! The page you’re looking for doesn’t exist.</p>
            <a href="/">Go Back Home</a>
        </div>
    </body>
    </html>
    """
    return HttpResponseNotFound(html, status=404)

def current_datetime(request):
    now = timezone.now()

    html_template = """<!doctype html>
<html lang="en" class="light">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Current Date & Time</title>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg1: #0ea5e9;
      --bg2: #7c3aed;
      --card: rgba(255,255,255,0.08);
      --border: rgba(255,255,255,0.15);
      --text: #0b1020;
      --muted: #5b647a;
      --accent: #111827;
    }
    .dark {
      --card: rgba(255,255,255,0.06);
      --border: rgba(255,255,255,0.12);
      --text: #e5e7eb;
      --muted: #9aa4b2;
      --accent: #f9fafb;
    }
    * { box-sizing: border-box; }
    html, body {
      height: 100%;
      margin: 0;
      font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
      color: var(--text);
    }
    body {
      background: linear-gradient(135deg, var(--bg1), var(--bg2)) fixed;
      display: grid;
      place-items: center;
      padding: 24px;
    }
    .wrap {
      width: 100%;
      max-width: 720px;
      backdrop-filter: blur(16px) saturate(150%);
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 24px;
      overflow: hidden;
      box-shadow:
        0 20px 40px rgba(0,0,0,0.20),
        inset 0 1px 0 rgba(255,255,255,0.07);
    }
    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 20px 24px;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0));
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 800;
      letter-spacing: 0.3px;
    }
    .badge {
      width: 36px; height: 36px;
      display: grid; place-items: center;
      border-radius: 12px;
      background: rgba(255,255,255,0.12);
      border: 1px solid var(--border);
    }
    .toggle {
      border: 1px solid var(--border);
      background: rgba(255,255,255,0.08);
      padding: 10px 14px;
      border-radius: 12px;
      cursor: pointer;
      font-weight: 600;
    }
    main { padding: 28px; }
    .grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
    }
    @media (min-width: 560px) {
      .grid { grid-template-columns: 1.2fr 0.8fr; }
    }
    .card {
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 20px;
      background: rgba(255,255,255,0.06);
    }
    .title {
      margin: 0 0 8px 0;
      font-size: 28px;
      line-height: 1.2;
      font-weight: 800;
      letter-spacing: 0.2px;
    }
    .muted { color: var(--muted); margin: 0; }
    .clock {
      font-size: 64px;
      line-height: 1;
      font-weight: 800;
      margin: 6px 0 12px 0;
      letter-spacing: 1px;
      word-spacing: 4px;
    }
    .row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }
    .pill {
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 10px 14px;
      font-weight: 600;
      background: rgba(255,255,255,0.05);
    }
    footer {
      padding: 20px 24px;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      color: var(--muted);
    }
    .sr-only {
      position: absolute;
      width: 1px; height: 1px;
      padding: 0; margin: -1px;
      overflow: hidden; clip: rect(0,0,0,0);
      white-space: nowrap; border: 0;
    }
  </style>
</head>
<body>
  <a class="sr-only" href="#content">Skip to content</a>
  <div class="wrap" role="region" aria-label="Current date and time">
    <header>
      <div class="brand" aria-label="App brand">
        <div class="badge" aria-hidden="true">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <path d="M12 7v5l3 3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <span>Now</span>
      </div>
      <button id="modeBtn" class="toggle" type="button" aria-pressed="false" aria-label="Toggle light and dark mode">Toggle Dark</button>
    </header>

    <main id="content" tabindex="-1">
      <div class="grid">
        <section class="card" aria-labelledby="live-time">
          <h2 id="live-time" class="title">Live Time</h2>
          <div id="clock" class="clock" data-iso="{{NOW_ISO}}">--:--:--</div>
          <p id="dateLine" class="muted">Loading date…</p>
          <div class="row" aria-label="Time details">
            <span id="tz" class="pill">Timezone: …</span>
            <span id="offset" class="pill">UTC offset: …</span>
            <span id="server" class="pill">Server ISO: {{NOW_ISO}}</span>
          </div>
        </section>

        <aside class="card" aria-labelledby="quick-facts">
          <h2 id="quick-facts" class="title">Quick Facts</h2>
          <p class="muted">This page shows the current time and date, updates every second, and adapts to your theme preference.</p>
          <ul>
            <li>Accessible semantics (ARIA, skip link)</li>
            <li>Responsive layout</li>
            <li>Glassmorphism styling</li>
            <li>Client-side live clock</li>
            <li>Light/Dark toggle</li>
          </ul>
        </aside>
      </div>
    </main>

    <footer>
      <span>Rendered by Django view</span>
      <span id="lastUpdated">Last updated: --:--:--</span>
    </footer>
  </div>

  <script>
    (function () {
      const root = document.documentElement;
      const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
      if (prefersDark) root.classList.replace("light", "dark");

      const btn = document.getElementById("modeBtn");
      btn.addEventListener("click", () => {
        const dark = root.classList.toggle("dark");
        btn.setAttribute("aria-pressed", String(dark));
      });

      const clockEl = document.getElementById("clock");
      const dateEl = document.getElementById("dateLine");
      const tzEl = document.getElementById("tz");
      const offsetEl = document.getElementById("offset");
      const updatedEl = document.getElementById("lastUpdated");

      // Use server ISO as an anchor; then tick on the client.
      const serverISO = clockEl.getAttribute("data-iso");
      let current = serverISO ? new Date(serverISO) : new Date();

      function pad(n) { return n.toString().padStart(2, "0"); }

      function render() {
        const d = current;
        const hh = pad(d.getHours());
        const mm = pad(d.getMinutes());
        const ss = pad(d.getSeconds());
        clockEl.textContent = `${hh}:${mm}:${ss}`;

        // Pretty date line using Intl
        try {
          const dateStr = new Intl.DateTimeFormat(undefined, {
            weekday: "long",
            year: "numeric",
            month: "long",
            day: "numeric"
          }).format(d);
          dateEl.textContent = dateStr;
        } catch {
          dateEl.textContent = d.toDateString();
        }

        // Timezone name & offset
        try {
          const tzName = Intl.DateTimeFormat().resolvedOptions().timeZone || "Local time";
          tzEl.textContent = `Timezone: ${tzName}`;
        } catch {
          tzEl.textContent = "Timezone: local";
        }
        const offsetMin = d.getTimezoneOffset();
        const sign = offsetMin > 0 ? "-" : "+";
        const abs = Math.abs(offsetMin);
        const oh = pad(Math.floor(abs / 60));
        const om = pad(abs % 60);
        offsetEl.textContent = `UTC offset: ${sign}${oh}:${om}`;

        updatedEl.textContent = `Last updated: ${hh}:${mm}:${ss}`;
      }

      render();
      setInterval(() => {
        current = new Date(current.getTime() + 1000);
        render();
      }, 1000);
    })();
  </script>
</body>
</html>"""

    html = html_template.replace("{{NOW_ISO}}", now.isoformat())
    return HttpResponse(html)



class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")


class NotFoundView(View):
    def get(self, request):
        return HttpResponse("404!")
