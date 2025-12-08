## 🎯 Module II: Dynamic Interaction Modes

### 📚 Goal: Learn to switch between Copilot’s interaction modes and channels to maximize developer productivity.

Copilot provides several distinct interaction channels:

* **Code Completions** → Quick scaffolding and filling in code as you type.
* **Inline Chat (`Ctrl/Cmd + I`)** → Focused, in-place edits and actions on selected code.
* **Chat Panel** → Global reasoning, architectural questions, and multi-file context.
* **Quick Chat** → Transient questions and brief inquiries.
* **Copilot CLI** → Shell/Terminal Interaction for generating and executing commands.

Switching modes and channels intentionally improves speed, accuracy, and clarity.

## Exercises

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **2.1** | **Code Completions** | 1. In `app/main.py` **type:** `# Add a new GET route /task/1/status that accepts a task_id path parameter and returns the status of that task`. <br>2. Open `Copilot: Open Completions Panel` and iterate through suggestions. Once accepted ensure the comment is deleted. <br> **Hint:** If you don't know how to open the right tool use `@vscode` agent.|
| **2.2** | **Inline Chat (`/fix`)** | You notice that something seems to be off with the calculation of the `generate_productivity_report`. <br>1. **Select**  the entire `generate_productivity_report` function. <br>2. **Inline Chat**: `/fix calculation` <br>3. Evaluate the proposed fix. The function's name and internal docstring provide critical context. |
| **2.3** | **Chat Panel (`/explain`)** | 1. **Select**  the `generate_productivity_report` function. <br>2.**Chat: Ask:** `/explain the steps of the function` |
| **2.4** | **Inline Chat (Selection)** | 1. **Select** the `generate_productivity_report` function. <br>2. **Inline Chat**: `Explain this code in a single sentence.` Observe how it provides an in-place, focused explanation. |
| **2.5** | **Inline Chat (`/doc`)** | 1. **Select** in `app/main.py` the function `log_task`. <br>2. **Inline Chat**: `/doc` <br>3. You can enhance the internal prompt in case you want a specific format.|
| **2.6** | **Inline Terminal** | 1. **Open your terminal** and press **`Command/Ctrl + I`** to launch the inline chat. <br>2. **Inline Chat:** `I need to run my FastAPI application using uvicorn with hot-reloading`. Observe how it picks up the terminal agent natively. |
| **2.7** | **Custom Prompt** | 1. **Review** `security-audit.prompt.md`. **Select** `get_all_tasks` in `app/main.py` and run the prompt: `/security-audit`. <br>2. **Create** your own prompt. |
| **2.8** | **Challenge: Custom Prompt** | Think about a repetitive task in your daily coding; choose a prompting framework to craft a reusable prompt and integrate it seamlessly into your workflow, then validate the output and refine the prompt as needed. |

---

### 📚 Inspiration: Designing Custom Prompt Files
 
Prompt Files are how you turn repetitive workflow tasks into standard, reusable commands. This prevents lengthy, complex instructions from being typed repeatedly and ensures standardization for tasks like documentation or custom code audits across the entire codebase. <br> [GitHub Docs: Your First Prompt File](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file)

---

### 🧠 Lesson Learned: Dynamic Interaction and Agent Capabilities

The most effective way to use Copilot is by **choosing the right mode** and understanding how to provide and switch context.
**Change the mode → change the context → change the result.**

#### 💡 Core Thinking Modes

All interactions fall into one of following modes, dictating the AI's response style:

* **Ask Mode** → Reasoning, explanations, conceptual questions (e.g., asking `/explain`).
* **Edit Mode** → Rewriting, fixing, or refactoring existing, selected code (e.g., using `/fix`).
* **Agent Mode** → Multi-step workflows that coordinate actions or external tools.
* **Plan Mode** → Helps you generate a step‑by‑step plan before coding. [Plan Mode](https://github.blog/changelog/2025-11-18-plan-mode-in-github-copilot-now-in-public-preview-in-jetbrains-eclipse-and-xcode/?utm_source=chatgpt.com) is one of the latest features.

#### ⚡ Interaction Channels and Focus

Always choose the interaction channel that best fits your immediate need to ensure maximum velocity and the highest level of contextual awareness.

### ⭐ Key Insight: Context = Results
The ultimate insight is that **the input channel acts as the primary router** for your query, dictating which specialized agent or tool handles the request. Copilot is engineered to be a powerful problem-solver, adept at handling complex tasks and quickly grasping the right context, but the human must guide the interaction.

1.  **Channel is the Router:** The channel you use (Inline Chat, Terminal, or Chat Panel) is the first factor that determines the AI's scope and focus.
2.  **Implicit Routing:** The system automatically invokes the required agent based on context (e.g., Inline Chat inside the terminal automatically routes the request to the `@terminal` Agent). This means you don't always need to explicitly type the agent tag.
3.  **Efficiency:** The most effective workflow combines these factors efficiently. The ultimate goal is to find the fastest way to get a reliable result. If you prefer typing commands over clicking UI elements, sticking to Slash Commands and Context Variables is a great strategy.
4.  **Personal Preference:** Remember that finding the 'best' interaction channel is ultimately a matter of **personal workflow preference**; it's perfectly fine and even recommended to stick with the methods and settings that you find most efficient.

---

### 💡 References & Further Reading

* [VS Code: Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)