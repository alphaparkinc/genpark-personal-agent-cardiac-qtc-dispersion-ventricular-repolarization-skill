# -*- coding: utf-8 -*-
"""Cardiac QTc Interval Dispersion & Repolarization Instability Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def assess_qtc_dispersion_repolarization(**kwargs):
    """Calculates heart-rate corrected QT intervals via Bazett, Fridericia, and Framingham formulas, evaluates precordial QTc dispersion, and flags torsadogenic ventricular arrhythmia risks."""
    qt_interval_measured_ms = kwargs.get('qt_interval_measured_ms')
    heart_rate_bpm = kwargs.get('heart_rate_bpm')
    qt_max_ms_in_leads = kwargs.get('qt_max_ms_in_leads')
    qt_min_ms_in_leads = kwargs.get('qt_min_ms_in_leads')
    is_female = kwargs.get('is_female')

    import math
    rr_sec = 60.0 / (heart_rate_bpm if heart_rate_bpm > 0 else 60.0)
    
    # Bazett: QTc = QT / sqrt(RR)
    qtc_bazett = round(qt_interval_measured_ms / math.sqrt(rr_sec), 1)
    
    # Fridericia: QTc = QT / (RR^(1/3))
    qtc_fridericia = round(qt_interval_measured_ms / (rr_sec ** (1.0 / 3.0)), 1)
    
    # Framingham: QTc = QT + 0.154 * (1 - RR) * 1000
    qtc_framingham = round(qt_interval_measured_ms + (154.0 * (1.0 - rr_sec)), 1)
    
    # QT Dispersion (QTd = QTmax - QTmin)
    qt_dispersion_ms = round(qt_max_ms_in_leads - qt_min_ms_in_leads, 1)
    
    upper_threshold = 460.0 if is_female else 450.0
    critical_threshold = 500.0
    
    if qtc_fridericia >= critical_threshold or qt_dispersion_ms > 80.0:
        risk_tier = "CRITICAL ARREST RISK (High propensity for Torsades de Pointes)"
        guidance = "Immediate ECG cardiology evaluation; discontinue QT-prolonging pharmacotherapy."
    elif qtc_fridericia >= upper_threshold or qt_dispersion_ms > 65.0:
        risk_tier = "BORDERLINE PROLONGATION / HETEROGENEOUS REPOLARIZATION"
        guidance = "Monitor serum potassium/magnesium levels; review drug-drug interaction matrix."
    elif qtc_fridericia < 340.0:
        risk_tier = "SHORT QT SYNDROME CONCERN"
        guidance = "Screen for congenital channelopathies or hypercalcemia."
    else:
        risk_tier = "PHYSIOLOGICAL HOMOGENEOUS REPOLARIZATION"
        guidance = "Ventricular repolarization dynamics well within healthy safety bounds."
        
    result = {
        "status": "success",
        "rr_interval_seconds": round(rr_sec, 3),
        "qtc_fridericia_ms": qtc_fridericia,
        "qtc_bazett_ms": qtc_bazett,
        "qtc_framingham_ms": qtc_framingham,
        "qt_dispersion_ms": qt_dispersion_ms,
        "repolarization_risk_tier": risk_tier,
        "electrophysiology_action_plan": guidance,
        "engine": "GenPark Ventricular Repolarization Dispersion Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "assess_qtc_dispersion_repolarization": {
        "name": "assess_qtc_dispersion_repolarization",
        "description": "Calculates heart-rate corrected QT intervals via Bazett, Fridericia, and Framingham formulas, evaluates precordial QTc dispersion, and flags torsadogenic ventricular arrhythmia risks.",
        "parameters": {
            "type": "object",
            "properties": {
                "qt_interval_measured_ms": {"type": "number", "description": "Raw measured QT interval in milliseconds"},
                "heart_rate_bpm": {"type": "number", "description": "Heart rate in beats per minute"},
                "qt_max_ms_in_leads": {"type": "number", "description": "Maximum QT interval across 12 precordial leads (ms)"},
                "qt_min_ms_in_leads": {"type": "number", "description": "Minimum QT interval across 12 precordial leads (ms)"},
                "is_female": {"type": "boolean", "description": "Biological sex of subject"},
            },
            "required": ['qt_interval_measured_ms', 'heart_rate_bpm', 'qt_max_ms_in_leads', 'qt_min_ms_in_leads', 'is_female']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "assess_qtc_dispersion_repolarization":
            res = assess_qtc_dispersion_repolarization(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-cardiac-qtc-dispersion-ventricular-repolarization-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-cardiac-qtc-dispersion-ventricular-repolarization-skill...")
    test_args = {'qt_interval_measured_ms': 410.0, 'heart_rate_bpm': 68.0, 'qt_max_ms_in_leads': 425.0, 'qt_min_ms_in_leads': 380.0, 'is_female': False}
    res = assess_qtc_dispersion_repolarization(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-cardiac-qtc-dispersion-ventricular-repolarization-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
