from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
import datetime


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
    now = datetime.datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Current Date & Time</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-align: center;
                padding: 50px;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
                display: inline-block;
                animation: fadeIn 1.2s ease-in-out;
            }}
            h1 {{
                font-size: 2.5rem;
                margin-bottom: 20px;
            }}
            p {{
                font-size: 1.5rem;
                margin: 0;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Current Date & Time</h1>
            <p>{now}</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)



class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")


class NotFoundView(View):
    def get(self, request):
        return HttpResponse("404!")
