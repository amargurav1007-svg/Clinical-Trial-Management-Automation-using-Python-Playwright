# QMS Module – Test Strategy (Document Initiation & CAPA)

## 1. Introduction
This document describes the test strategy for the Quality Management System (QMS) module, focused on:
- Document Initiation workflow
- CAPA (Corrective and Preventive Action) lifecycle (high level)

The goal is to validate that quality records are created, routed, and stored correctly with proper roles, statuses, and auditability.

## 2. In Scope
- QMS login and basic navigation
- Document Initiation:
  - Creating a new SOP document
  - Assigning approvers
  - Verifying status and record visibility
- CAPA workflow (high level validation)

## 3. Out of Scope
- Performance & load testing
- Deep database validation
- External integrations

## 4. Test Types
- Functional testing
- Regression testing
- Role-based access testing
- UI validation

## 5. Test Tools
- Manual Testing
- Automation: Python + Playwright + Pytest

## 6. Entry & Exit Criteria
Entry: Build deployed, test users ready  
Exit: All critical test cases pass

## 7. Risk & Mitigation
Risk: Metadata change  
Mitigation: Focus on critical workflows
