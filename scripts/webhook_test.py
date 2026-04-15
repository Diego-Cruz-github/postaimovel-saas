#!/usr/bin/env python3
"""
webhook_test.py - Teste de integracao com webhook Hotmart
Simula eventos de compra, cancelamento e reembolso.
"""

import requests
import json
import sys
from datetime import datetime


WEBHOOK_EVENTS = {
    "purchase_approved": {
        "event": "PURCHASE_APPROVED",
        "data": {
            "buyer": {"email": "test@example.com", "name": "Test User"},
            "purchase": {"status": "APPROVED", "transaction": "TEST-001"},
            "subscription": {"status": "ACTIVE"},
        }
    },
    "purchase_canceled": {
        "event": "PURCHASE_CANCELED",
        "data": {
            "buyer": {"email": "test@example.com", "name": "Test User"},
            "purchase": {"status": "CANCELED", "transaction": "TEST-001"},
            "subscription": {"status": "INACTIVE"},
        }
    },
    "purchase_refunded": {
        "event": "PURCHASE_REFUNDED",
        "data": {
            "buyer": {"email": "test@example.com", "name": "Test User"},
            "purchase": {"status": "REFUNDED", "transaction": "TEST-001"},
        }
    },
}


def send_test_event(webhook_url, event_type, timeout=15):
    """Envia evento de teste para o webhook."""
    if event_type not in WEBHOOK_EVENTS:
        print(f"  [FAIL] Unknown event type: {event_type}")
        return False

    payload = WEBHOOK_EVENTS[event_type]
    try:
        resp = requests.post(webhook_url, json=payload, timeout=timeout)
        status = "OK" if resp.status_code in [200, 201] else "WARN"
        print(f"  [{status}] {event_type}: HTTP {resp.status_code}")
        if resp.status_code == 200:
            try:
                data = resp.json()
                print(f"         Response: {json.dumps(data, indent=2)[:200]}")
            except ValueError:
                pass
        return resp.status_code in [200, 201]
    except Exception as e:
        print(f"  [FAIL] {event_type}: {e}")
        return False


def run_tests(webhook_url):
    """Executa todos os testes de webhook."""
    print(f"\n[{datetime.utcnow().isoformat()}] Hotmart Webhook Test")
    print(f"  Target: {webhook_url}")
    print("-" * 50)

    results = []
    for event_type in WEBHOOK_EVENTS:
        results.append(send_test_event(webhook_url, event_type))

    all_ok = all(results)
    print("-" * 50)
    print(f"  Result: {'ALL EVENTS OK' if all_ok else 'SOME EVENTS FAILED'}")
    return all_ok


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080/api/webhooks/hotmart"
    ok = run_tests(url)
    sys.exit(0 if ok else 1)
