# Contributing to Adversarial ML Attack Lab

Thank you for your interest in contributing to ML security research!

## 🎯 How to Contribute

We welcome contributions in these areas:

- **New Attacks** - TextBugger, HotFlip, PWWS, Genetic Attack, prompt injection
- **Model Support** - RoBERTa, ALBERT, T5, GPT-2, domain-specific models
- **Defenses** - Adversarial training, input sanitization, detection methods
- **Documentation** - Attack guides, tutorials, benchmarks

## 🚀 Quick Start

```bash
# Fork and clone
git clone https://github.com/nand9lohot/llm-adversarial-attacks-textattack.git
cd llm-adversarial-attacks-textattack

# Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create feature branch
git checkout -b feature/your-feature
```

## 📝 Contribution Process

### 1. Create an Issue

Discuss your idea first:
- **Bugs:** Steps to reproduce, expected vs actual behavior
- **Features:** Motivation, implementation approach, references

### 2. Implement Changes

**Adding a new attack:**

```python
# attacks/new_attack.py

"""
Attack Name

Reference: Paper citation
MITRE ATLAS: AML.T0015
"""

from textattack.attack_recipes import AttackRecipe

class NewAttack(AttackRecipe):
    """Brief description."""
    
    @staticmethod
    def build(model_wrapper):
        # Implementation
        pass

def get_attack(model_wrapper):
    return NewAttack.build(model_wrapper)
```

**Register in attack engine:**
```python
# app/attack_engine.py
AVAILABLE_ATTACKS = {
    'new_attack': 'attacks.new_attack',
}
```

### 3. Add Tests

```python
# tests/test_new_attack.py

def test_attack_initialization(model_wrapper):
    attack = NewAttack.build(model_wrapper)
    assert attack is not None

def test_attack_success(model_wrapper, sample_text):
    attack = NewAttack.build(model_wrapper)
    result = attack.attack(sample_text)
    assert result.perturbed_result.output != result.original_result.output
```

### 4. Document

Create `docs/attacks/new_attack.md`:
```markdown
# Attack Name

## Overview
Brief description

## Methodology
How it works

## Usage
```python
# Code example
```

## Effectiveness
Success rates and metrics
```

### 5. Quality Checks

```bash
# Format code
black attacks/ app/ tests/
isort attacks/ app/ tests/

# Run tests
pytest tests/ -v --cov=attacks
```

### 6. Commit & Push

```bash
git add .
git commit -m "feat: add NewAttack implementation

- Implement NewAttack (Author et al., Conference Year)
- Add test suite and documentation
- Update attack engine

Closes #42"

git push origin feature/your-feature
```

### 7. Create Pull Request

Use this template:

```markdown
## Description
Brief description of changes

## Type
- [ ] New attack
- [ ] Bug fix
- [ ] Documentation

## Testing
- [ ] Tests added/updated
- [ ] All tests pass

## Checklist
- [ ] Code formatted
- [ ] Documentation updated
- [ ] Self-review completed
```

## 🎨 Code Style

**Follow PEP 8:**
- Line length: 100 characters
- Indentation: 4 spaces
- Docstrings: Google style

```python
def function_name(param1, param2):
    """
    Brief description.
    
    Args:
        param1 (str): Description
        param2 (int): Description
        
    Returns:
        Result: Description
    """
    pass
```

## 🧪 Testing Requirements

All contributions must include:
- **Unit tests** - Test individual components
- **Integration tests** - Test end-to-end flow
- **Coverage** - Maintain >80% coverage

## 📚 Documentation Standards

- Add docstrings to all public functions
- Include research paper references
- Provide usage examples
- Document parameters and return values

## 🏆 Recognition

Contributors are:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Acknowledged in citations

## 💡 Contribution Ideas

**Beginner:**
- Fix documentation typos
- Add usage examples
- Improve error messages

**Intermediate:**
- Implement documented attacks
- Add visualization features
- Create tutorial notebooks

**Advanced:**
- Novel attack research
- Defense mechanisms
- Transferability analysis

## 🤝 Review Process

1. Automated checks run on PR
2. Maintainer review (3-5 days)
3. Address feedback
4. Merge approval

## 📞 Getting Help

- **Issues** - Bug reports and features
- **Discussions** - Questions and ideas
- **Email** - Security concerns

---

**Branch Naming:**
- `feature/attack-name` - New attacks
- `fix/issue-description` - Bug fixes
- `docs/topic` - Documentation

**Commit Format:**
```
type: subject

body

footer
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`

---

Thank you for advancing ML security! 🚀