NEUROGUARD AI

Overview

NeuroGuard AI is an intelligent cybersecurity assistant powered by ASI-1 API. The checks passwords and URLs, detects vulnerabilities, stimulates cyber attacks and provides actionable recommendations. Detects the strength, length , patterns and reuse risks. Also follows the phishing patterns in URLs while checking suspicious domains.

DEFINATION NEUROGUARD

Neuro stands for brain and Guard stands for security.

Brains transmits information every minute and the information is encrypted until released. So your password should be information inside your brain secured.

&#x20;**Features of NeuroGuard AI.**

* Passwords strength analysis.
* URL phishing detection.
* Risk scoring system.
* Attack simulation.
* Security insights powered by AI.

TECH STACK

* Django framework
* python programming language(Backend)
* HTML, CSS, JavaScript (Frontend)
* ASI-1 API(AI Engine)

USAGE OF ASI-1

* Analyze the strength of the password.(weak, medium and strong).
* Detects phishing URLs.(URLs that personates other legal link to acquire user personal data.
* Stimulates hacking techniques such as substitution.
* provides recommendations. such as don't enter your details into this malicious link.

SETUP INSTRUCTIONS.

1. Clone repository: git clone.
2. Navigate: cd  NEUROGUARD-AI.
3. Create virtual environment: python -m venv venv.
4. Activate: venv\\Scripts\\activate.
5. Install dependencies: pip install -r requirements.txt.
6. Run server: python manage.py runserver.
7. Open browser:http://127.0.0.1.8000/

SYSTEM FLOW

1. User enters passwords or URL in browser.
2. Frontend(HTML AND JS) sends request via fetch().
3. Django backend receives request(view.py).
4. Backend formats prompt.
5. Backend calls ASI-1 API.
6. ASI-1 processes and returns AI response.
7. Django processes response(score, risk, text).
8. Response sent back as JSON.
9. Frontend displays the output(UI and score bar).

DEMO INPUTS

Weak passwords:12345678

Medium Passwords:#John\_123

Strong passwords:7\&Kk2#vP$mZ9!qR4@wN%3

phishing URL:equity-login-secure254.com

AUTHOR

NEUROGUARD-AI BY JERRYLE JILL.



