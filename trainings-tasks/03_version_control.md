## 🎯 Module III: Version Control and Quality

### 📚 Goal: Integrate Copilot's contextual features into Git workflows.

Improve commit messages, code review, and branch documentation, while reinforcing the developer's ultimate responsibility for code integrity.

## Exercises

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **3.1** | **Code Review** | 1. **Stage** the file(s) containing the changes from the previous module.<br>2. Open the **Source Control** panel. <br>3. Click **"Review changes with Copilot"**. Review the feedback provided by Copilot on the staged code. |
| **3.2** | **Commit Message** | 1. In the **Source Control** panel, click the **Copilot Icon** next to the commit message box. Ensure you have staged changes.<br>2. Observe the quality of the commit message and understand the [limitations of the feature](https://docs.github.com/en/copilot/responsible-use/copilot-commit-message-generation). |
| **3.3** | **Challenge: PR Summary** | Leverage your knowledge from the previous chapters and create a concise summary for a Pull Request, avoiding the issue of getting an overly broad history. <br>**HINT:** You can craft a precise prompt and use the **`@workspace` agent** that forces Copilot to summarize only the specific changes for this PR (which likely involves the last few commits). You can use Git references (like commit hashes) or restrict the summary by file path to get the exact result you want. Feel free to research and apply any other approach. |

---

### 🧠 Lesson Learned: Git Workflow and Developer Responsibility

You can **embed GitHub Copilot directly into your Git workflow** to ensure cleaner branch history and detect issues ahead of your colleagues review. Remember that **developers are responsible for the code quality and integrity**.

---

#### 🛡️ Responsibility Boundaries

* **You are the Guardian:** 🧑‍💻 You are still fully responsible for the quality, correctness, and security of the code you commit. Copilot is an acceleration tool, not a replacement for human judgment.
* **Verification is Mandatory:** 🔬 Always review the output from Copilot's SCM review and manually test any changes it suggests before committing.
* **Meaningful Code:** ✅ Ensure you commit **correct and logical** code. Copilot accelerates the writing process, but **human validation and testing** is the non-negotiable final step.