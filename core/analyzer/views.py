from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
import requests
import json
import re
import os
from decouple import config
from django.http import HttpResponse
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

def my_view(request):
    secret_value = config('MY_SECRET_KEY')
    return HttpResponse(f"My secret is safely loaded: {'sk_d6a01095ad704a49b5956c604697d5174221a4a3193d47ac9e41ab9dcf80c224'}")

# ✅ Use environment variable for API key (more secure)
ASI_API_KEY = os.getenv("ASI_API_KEY", "sk_d6a01095ad704a49b5956c604697d5174221a4a3193d47ac9e41ab9dcf80c224")
ASI_URL = "https://api.asi1.ai/v1/chat/completions"


def call_asi(prompt):
    try:
        response = requests.post(
            ASI_URL,
            headers={
                "Authorization": f"Bearer {ASI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "asi1",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 500
            },
            timeout=10
        )
        if response.status_code != 200:
            return {"error": f"API Error {response.status_code}"}
        return response.json()
    except Exception as e:
        return {"error": str(e)}


def home(request):
    return render(request, 'index.html')


def basic_password_score(password):
    """Optional: basic rule-based password score"""
    score = 0
    if len(password) >= 8: score += 2
    if re.search(r"[A-Z]", password): score += 2
    if re.search(r"[0-9]", password): score += 2
    if re.search(r"[!@#$%^&*]", password): score += 2
    return min(score, 10)


@csrf_exempt
def analyze_password(request):
    if request.method != "POST":
        return JsonResponse({"response": "Only POST requests allowed"}, status=405)

    # ✅ get password safely
    password = request.POST.get("password")
    if not password:
        try:
            data = json.loads(request.body.decode('utf-8'))
            password = data.get("password", "")
        except Exception:
            password = ""

    if not password:
        return JsonResponse({"response": "Error: No password provided."}, status=400)

    # 🔥 structured AI prompt
    prompt = f"""
You are a cybersecurity expert.

Analyze this password: {password}

Return your answer in this JSON format:

{{
    "strength": "Weak/Medium/Strong",
    "score": number,
    "weaknesses": ["point1","point2"],
    "risk": "Explain how it can be hacked in simple terms",
    "improved": "Give a stronger version",
    "reason": "Why the new password is better"
}}
"""

    result = call_asi(prompt)

    try:
        output = result["choices"][0]["message"]["content"]
        # Try parsing JSON returned by AI
        parsed = json.loads(output)
        # Add rule-based score
        parsed["score"] = basic_password_score(password)
        return JsonResponse(parsed)
    except Exception:
        return JsonResponse({"response": output if "output" in locals() else result})


@csrf_exempt
def analyze_url(request):
    if request.method != "POST":
        return JsonResponse({"response": "Only POST requests allowed"}, status=405)

    url = request.POST.get("url")
    if not url:
        try:
            data = json.loads(request.body.decode('utf-8'))
            url = data.get("url", "")
        except Exception:
            url = ""

    if not url:
        return JsonResponse({"response": "Error: No URL provided."}, status=400)

    prompt = f"""
You are a cybersecurity expert.

Analyze this URL: {url}

Return your answer in this JSON format:

{{
    "safety": "Safe/Suspicious/Malicious",
    "risk": "Explain why this URL may be dangerous",
    "recommendations": ["Steps the user should take"]
}}
"""

    result = call_asi(prompt)

    try:
        output = result["choices"][0]["message"]["content"]
        parsed = json.loads(output)
        return JsonResponse(parsed)
    except Exception:
        return JsonResponse({"response": output if "output" in locals() else result})
