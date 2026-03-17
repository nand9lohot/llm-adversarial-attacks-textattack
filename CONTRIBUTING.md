# Contributing to LLM Adversarial Attack Lab

Thank you for your interest in contributing. This project is designed as a practical AI security lab to explore adversarial attacks against NLP models. Contributions that improve realism, coverage, and research depth are highly encouraged.

---

## Scope of Contributions

We welcome contributions in the following areas:

### Adversarial Attacks
- Implement new attack techniques (e.g., TextBugger, HotFlip, Genetic Attacks)
- Extend existing attacks with improved constraints or search strategies
- Add LLM-specific attacks (prompt injection, jailbreaks, RAG poisoning)

### Model Coverage
- Support additional architectures (RoBERTa, LLaMA, Mistral, T5)
- Integrate open-source LLMs (via HuggingFace or local inference)

### Evaluation & Metrics
- Improve attack evaluation (robustness scoring, semantic similarity, perturbation metrics)
- Enhance reporting (visualizations, dashboards, comparative analysis)

### Engineering Improvements
- Performance optimizations (caching, parallel execution)
- CI/CD enhancements
- Docker/image optimization

---

## Getting Started

1. Fork the repository  
2. Create a feature branch:

```bash
git checkout -b feature/<your-feature-name>
```
3. Make your changes
4. Test locally:
```bash
docker build -t llm-adversarial-attack -f docker/Dockerfile .
docker run -v $(pwd)/reports:/app/reports llm-adversarial-attack
```
5. Submit a Pull Request

---

## Contribution Guidelines

- Follow the existing project structure (app/, attacks/, scripts/)
- Keep implementations modular and reusable
- Ensure Docker build and pipeline execution remain functional
- Avoid introducing unnecessary external dependencies
- Document any new attack clearly (method, assumptions, impact)

---

## Code Quality

- Use clear, readable Python code
- Add comments where logic is non-trivial
- Ensure compatibility with Python 3.10+
- Prefer deterministic and reproducible implementations

---

## Reporting Issues

**If you encounter issues:**
- Provide reproducible steps
- Include logs/output where relevant
- Clearly describe expected vs actual behavior

---

## Vision

This project aims to evolve into a practical AI red-teaming lab aligned with real-world adversarial ML threats and frameworks such as MITRE ATLAS.

Contributions that move the project toward this goal are especially valuable.

---

## Acknowledgement

All contributors will be recognized for their work.