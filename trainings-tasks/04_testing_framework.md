## 🎯 Module IV: Testing Framework (Testing, Debugging, and Fixes)

### 📚 Goal: Integrate Copilot into the end-to-end development loop.
Generate tests, explore unit and integration coverage, and ensure code adheres to project standards.

Copilot can leverage **global instruction files** and **custom prompts** to understand project structure, naming conventions, and preferred frameworks. By refining instructions and prompts, you make Copilot smarter and reduce manual corrections when generating tests.

## Exercises

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **4.1** | **Test Generation** | 1. Select any function or endpoint. <br>2. Use **Inline Chat** and type: `/tests`. <br>3. Observe the initial suggestions and where Copilot proposes to place the test file. |
| **4.2** | **Enhance Instructions** | 1. Update the **global instruction file** to guide Copilot for test generation. Include the test framework (e.g., `pytest`),  naming conventions for test files and functions, preferred folder structure for tests, any required fixtures or templates. Use Copilot to enhance the instruction file!<br>2. Rerun `/tests` on a function and observe how your instructions influence the generated output. |
| **4.3** | **Challenge: Full Codebase Test Generation** | Generate unit and integration tests for the app using your updated instruction file. Ensure all tests follow your defined rules. |
| **4.4** | **Optional: Custom Prompt** | Create a `.prompt.md` file to automate the repetitive test-generation task. |

---

### 🧠 Lesson Learned: Context-Driven Test Generation
- **Enhancing instructions** ensures AI-generated tests are consistent, correctly placed, and follow naming conventions, fixtures, and framework standards.  
- **Prompt precision matters:** Even with instruction files, carefully worded prompts avoid scope creep or unintended outputs.  

