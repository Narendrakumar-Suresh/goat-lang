***If youre really goingv to contribute or just thought of it ping me or create an issue. I was sleep while creating this file and gpitty made it .....***

# Contributing to GoatLang Compiler (GLC)

Thank you for your interest in contributing! 🎉
GoatLang (GLC) is a toy programming language that transpiles to C. Contributions are welcome in the form of bug fixes, new features, documentation, or examples.

---

## 🛠 Getting Started

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:

   ```bash
   git clone https://github.com/<your-username>/glc.git
   cd glc
   ```
3. **Install dependencies**:

   ```bash
   pip install -e .
   ```

   This installs `glc` in editable mode so you can run it as:

   ```bash
   glc examples/hello.g
   ```

---

## 🚀 Development Workflow

1. **Create a branch** for your work:

   ```bash
   git checkout -b feature/new-thing
   ```

2. **Make your changes** in `glc/` source code or `examples/`.

3. **Test locally** by running:

   ```bash
   pytest
   ```

   (Tests coming soon — for now, run some `.g` programs to verify.)

4. **Commit with clear messages**:

   ```bash
   git commit -m "Add while loop support"
   ```

5. **Push your branch**:

   ```bash
   git push origin feature/new-thing
   ```

6. **Open a Pull Request** on GitHub.

---

## 📖 Code Style Guidelines

* Follow **PEP8** for Python code.
* Keep functions **small and focused**.
* Add **comments** for parsing/lexer rules or tricky logic.
* Place example `.g` files under the `examples/` directory.

---

## 🧪 Adding Examples

If you add a new language feature, please also add an example in the `examples/` folder, like:

```go
fn greet() {
    string msg = "Hello"
    print(msg)
}
```

---

## 🐛 Reporting Issues

* Use the [GitHub Issues](https://github.com/Narendrakumar-Suresh/glc/issues) page.
* Include steps to reproduce, expected behavior, and actual behavior.
* Share the `.g` code snippet if possible.

---

## 📦 Releasing

* Update `pyproject.toml` version before a release.
* Run:

  ```bash
  rm -rf dist build *.egg-info
  python -m build
  python -m twine upload dist/*
  ```

---

## 🙌 Code of Conduct

Please be respectful and constructive in all discussions.
We want a welcoming and beginner-friendly environment.
