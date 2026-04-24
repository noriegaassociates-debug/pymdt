# GNES-PyMDT Execution Layer

**Status:** Layer 1 Semantic-Authoritative · ALL SIM · NO CLAIM  
**Authority:** HiC_ONLY  
**AI Engines:** ADVISORY_ONLY  
**Repository:** `noriegaassociates-debug/pymdt`

This directory instruments PyMDT as the GNES digital-twin execution layer for microgrid simulation, SDS calculation, MIMO return-difference stability screening, OSCAL component-definition export, and NERC/NRC control-boundary mapping.

The upstream README states that PyMDT is a Python interface for Sandia's Microgrid Design Toolkit, requires a compliant MDT installation, is Windows x64-bound, and points users to `minimal.py` for a starter example. This GNES extension therefore treats PyMDT as a simulation wrapper, not as validated field-control software.

## Generated artifacts

| Path | Purpose |
|---|---|
| `gnes/colab/GNES_PyMDT_Instrumented_Kernel.py` | Colab-compatible GNES kernel with SDS, MIMO, PRM-lite, hash manifest, and telemetry audit records |
| `gnes/oscal/gnes_pymdt_oscal_component_definition.json` | OSCAL 1.1.2 component-definition stub for PyMDT as digital-twin simulation layer |
| `gnes/compliance/nerc_nrc_control_mapping.yaml` | NERC/NRC readiness map with explicit SIM-only caveats |
| `gnes/dashboard/gnes_sds_mimo_dashboard.py` | Streamlit dashboard for live SDS/MIMO review from PyMDT-style JSONL telemetry |

## Governing rule

PyMDT may generate V4 simulation state and support V4/V9 comparison, but it cannot elevate outputs into operational authority. Any Layer 2 elevation requires site-specific validation, real telemetry binding, MDT parity testing, NERC/NRC applicability review, and HiC authorization.

## Final label

```text
GNES-PYMDT-EXECUTION-LAYER
Digital Twin + Microgrid Simulation Core
ALL SIM · NO CLAIM
FAIL-CLOSED ON SDS OR MIMO ROBUSTNESS DEGRADATION
```
