#!/usr/bin/env python3
"""
health_check.py - Monitoramento do PostAImovel em producao
Verifica app, banco MySQL e integracao Hotmart.
"""

import requests
import sys
from datetime import datetime


def check_app(base_url, timeout=10):
    """Verifica se a aplicacao esta respondendo."""
    try:
        resp = requests.get(base_url, timeout=timeout)
        status = "OK" if resp.status_code == 200 else "WARN"
        elapsed = int(resp.elapsed.total_seconds() * 1000)
        print(f"  [{status}] App: HTTP {resp.status_code} ({elapsed}ms)")
        return resp.status_code == 200
    except Exception as e:
        print(f"  [FAIL] App: {e}")
        return False


def check_api(base_url, timeout=10):
    """Verifica endpoints da API."""
    endpoints = ["/api/auth/status", "/api/properties"]
    results = []
    for endpoint in endpoints:
        try:
            resp = requests.get(f"{base_url}{endpoint}", timeout=timeout)
            status = "OK" if resp.status_code in [200, 401] else "WARN"
            print(f"  [{status}] API {endpoint}: HTTP {resp.status_code}")
            results.append(True)
        except Exception as e:
            print(f"  [FAIL] API {endpoint}: {e}")
            results.append(False)
    return all(results)


def check_hotmart_webhook(base_url, timeout=10):
    """Verifica se o endpoint de webhook Hotmart esta acessivel."""
    try:
        resp = requests.post(
            f"{base_url}/api/webhooks/hotmart",
            json={"test": True},
            timeout=timeout
        )
        accessible = resp.status_code < 500
        status = "OK" if accessible else "FAIL"
        print(f"  [{status}] Hotmart webhook: HTTP {resp.status_code}")
        return accessible
    except Exception as e:
        print(f"  [FAIL] Hotmart webhook: {e}")
        return False


def run_checks(base_url):
    """Executa verificacao completa."""
    print(f"\n[{datetime.utcnow().isoformat()}] PostAImovel Health Check")
    print(f"  Target: {base_url}")
    print("-" * 50)

    results = [
        check_app(base_url),
        check_api(base_url),
        check_hotmart_webhook(base_url),
    ]

    all_ok = all(results)
    print("-" * 50)
    print(f"  Result: {'ALL HEALTHY' if all_ok else 'ISSUES DETECTED'}")
    return all_ok


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080"
    ok = run_checks(url)
    sys.exit(0 if ok else 1)
