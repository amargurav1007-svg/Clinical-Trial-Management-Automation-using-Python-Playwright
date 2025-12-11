```mermaid
flowchart LR

%% ---------------------- QMS DOCUMENT MANAGEMENT ----------------------
subgraph QMS_DOC [QMS Document Management]
    DOC1[Create Document (SOP / CRF)]
    DOC2[Document Review]
    DOC3[Document Approval]
end

DOC1 --> DOC2 --> DOC3

%% ---------------------- PROTOCOL AUDIT ----------------------
subgraph AUDIT [Protocol Audit]
    A1[Plan Audit]
    A2[Execute Audit at Site]
    A3[Record Findings (Major / Minor)]
    A4[Submit Audit Report]
end

A1 --> A2 --> A3 --> A4

%% ---------------------- CAPA WORKFLOW ----------------------
subgraph CAPA [CAPA Workflow]
    C1[Initiate CAPA]
    C2[Root-Cause Analysis]
    C3[Implement Corrective Actions]
    C4[Effectiveness Check]
    C5[Close CAPA]
end

C1 --> C2 --> C3 --> C4 --> C5

%% ---------------------- AE / SAE REPORTING ----------------------
subgraph AE [AE / SAE Reporting]
    E1[Capture Patient AE Details]
    E2[Medical Evaluation]
    E3[Submit AE Report]
    E4[Regulatory Notification]
end

E1 --> E2 --> E3 --> E4

%% ---------------------- FLOW BETWEEN MODULES ----------------------
DOC3 --> A1   %% Approved documents → basis for audits
A4 --> C1     %% Audit findings → trigger CAPA
C5 --> E1     %% Closed CAPA improves AE reporting quality
```
