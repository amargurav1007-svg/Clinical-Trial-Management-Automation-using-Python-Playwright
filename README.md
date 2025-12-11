---

# 🔁 QMS — Master Lifecycle Diagram (Audit → CAPA → Closure)

This repository models an enterprise Clinical Quality Management System (QMS) lifecycle.  
Below is a high-level flowchart (Mermaid) that shows how Document Initiation, Protocol Audit, and CAPA interact in a regulated clinical environment.

> **Note:** For live demo we map Document Initiation to a demo site (demoqa). Protocol Audit and CAPA are implemented as design blueprints and are skipped until a real QMS UI is available.

### Mermaid diagram (paste into README.md as-is — GitHub renders Mermaid in supported views)

```mermaid
flowchart LR
    subgraph DOC [Document Management]
        D1[Create Document / Protocol<br/>(SOP / Protocol / CRF)]
        D2[Document Review]
        D3[Document Approval]
    end

    subgraph AUDIT [Protocol Audit]
        A1[Plan Audit]
        A2[Execute Audit at Site]
        A3[Record Findings<br/>(Major / Minor)]
    end

    subgraph CAPA [CAPA Lifecycle]
        C1[Auto-trigger CAPA from Findings]
        C2[Root Cause Analysis]
        C3[Corrective Action Plan]
        C4[Preventive Action Plan]
        C5[Review & Approval]
        C6[Effectiveness Check]
        C7[Close CAPA]
    end

    subgraph QMS_CLOSURE [QMS Closure]
        Q1[Audit Follow-up]
        Q2[Management Review]
        Q3[Archive Records]
    end

    %% flows
    D1 --> D2 --> D3
    D3 --> A1
    A1 --> A2 --> A3
    A3 --> C1
    C1 --> C2 --> C3 --> C4 --> C5 --> C6 --> C7
    C7 --> Q1 --> Q2 --> Q3

    %% annotations
    classDef blue fill:#E8F0FF,stroke:#0366d6;
    class DOC blue;
    class AUDIT blue;
    class CAPA blue;
    class QMS_CLOSURE blue;
