# Cardiac QTc Interval Dispersion & Repolarization Instability Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `assess_qtc_dispersion_repolarization`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates heart-rate corrected QT intervals via Bazett, Fridericia, and Framingham formulas, evaluates precordial QTc dispersion, and flags torsadogenic ventricular arrhythmia risks.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Electrocardiology)`

## MCP Tool Specification
### `assess_qtc_dispersion_repolarization`
Parameters:
- `qt_interval_measured_ms` (float): Raw measured QT interval in milliseconds
- `heart_rate_bpm` (float): Heart rate in beats per minute
- `qt_max_ms_in_leads` (float): Maximum QT interval across 12 precordial leads (ms)
- `qt_min_ms_in_leads` (float): Minimum QT interval across 12 precordial leads (ms)
- `is_female` (bool): Biological sex of subject

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-cardiac-qtc-dispersion-ventricular-repolarization-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-cardiac-qtc-dispersion-ventricular-repolarization-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
