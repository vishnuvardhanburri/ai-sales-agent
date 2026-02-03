# AI Sales Agent - Prompt Engineering Library

This repository contains the production-grade prompt architecture for an autonomous AI Sales Agent. It follows senior SDE standards for versioning, testing, and validation of LLM logic.

## Project Overview
- **Objective**: Lead qualification (BANT/MEDDICC), objection handling, and meeting booking.
- **Models**: GPT-4, Claude 3.5 Sonnet.
- **Frameworks**: Chain-of-Thought (CoT), Few-Shot Prompting.

## Repository Structure
- `/prompts`: Versioned system and user prompt templates.
- `/evals`: Scripts for testing prompt performance against "Golden Sets."
- `/docs`: Detailed talk tracks and sales framework documentation.

## Engineering Standards
1. **No Hardcoded Logic**: All prompts use structured variables.
2. **Validation First**: Every prompt must pass a schema check.
3. **Auditability**: All iterations are tracked via Git history.
4. # ai-sales-agent
