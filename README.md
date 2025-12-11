flowchart TD

    %% -------------------- DOCUMENT MANAGEMENT --------------------
    subgraph DOC [QMS Document Management]
        DOC1[Create Document (SOP / CRF / Protocol)]
        DOC2[Document Review]
        DOC3[Document Approval]
    end

    DOC1 --> DOC2 --> DOC3

    %% -------------------- PROTOCOL AUDIT --------------------
    subgraph AUDIT [Protocol Audit Workflow]
        A1[Plan Audit]
        A2[Execute Audit at Site]
        A3[Record Findings<br/>(Major / Minor)]
        A4[Submit Audit Report]
    end

    DOC3 --> A1 --> A2 --> A3 --> A4

    %% -------------------- CAPA PROCESS --------------------
    subgraph CAPA [Corrective & Preventive Action]
        C1[CAPA Triggered Automatically]
        C2[Root Cause Analysis]
        C3[Action Plan Assigned]
        C4[CAPA Review (QA)]
        C5[CAPA Approval]
        C6[Effectiveness Check]
        C7[CAPA Closure]
    end

    A4 --> C1 --> C2 --> C3 --> C4 --> C5 --> C6 --> C7
