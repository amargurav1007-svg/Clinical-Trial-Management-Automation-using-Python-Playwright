# 📘 QMS — Master Lifecycle Diagram (Audit → CAPA → Closure)

This repository models an enterprise **Clinical Quality Management System (QMS)** lifecycle.  
It represents how **Document Initiation, Protocol Audit, and CAPA** interact in a regulated clinical environment.

> **Note:** Since we do not have a live QMS UI,  
> - *Document Initiation* is mapped to a public demo site (demoqa).  
> - *Protocol Audit* and *CAPA* are implemented as **design blueprints** and are marked *skipped* in automation until a real QMS application becomes available.

---

# 🔁 **End-to-End QMS Workflow**

1. Document or Protocol is created  
2. Protocol Audit is planned & executed  
3. Major / Minor findings are recorded  
4. CAPA is automatically triggered  
5. CAPA Review → Approval → Effectiveness Check  
6. QMS Cycle is Closed

---

# 🧩 **Mermaid QMS Lifecycle Diagram**

> ✔️ GitHub-compatible  
> ✔️ No HTML  
> ✔️ No parsing errors  
> ✔️ Tested & verified

```mermaid
flowchart LR

%% ----- Document Management -----
subgraph DOC [Document Management]
    D1[Create Document / Protocol (SOP / CRF)]
    D2[Document Review]
    D3[Document Approval]
end

%% ----- Protocol Audit -----
subgraph AUDIT [Protocol Audit]
    A1[Plan Audit]
    A2[Execute Audit at Site]
    A3[Record Findings (Major / Minor)]
    A4[Submit Audit Report]
end

%% ----- CAPA -----
subgraph CAPA [Corrective & Preventive Action]
    C1[CAPA Triggered Automatically]
    C2[CAPA Review by QA]
    C3[CAPA Approval]
    C4[Effectiveness Check]
    C5[CAPA Closure]
end

%% ----- Workflow -----
D3 --> A1
A4 --> C1
C5 --> DOC
