0. Big picture: what you’re building

You want VS Code + GitHub to mirror this mental model:
	•	Repo 1 – langgraph-playground
Tiny, self-contained experiments that map directly to your Heptabase pattern cards.
	•	Repo 2 – thesis-agent-system (later)
The “real” experimental system you’ll evaluate in the dissertation.

Right now, we’ll nail Repo 1 and structure VS Code so it’s super easy to live in.

⸻

1. Create your LangGraph playground repo locally

On your Mac terminal:

mkdir ~/dev
cd ~/dev
mkdir langgraph-playground
cd langgraph-playground
code .

VS Code should open in that folder.

Inside VS Code:
	1.	Make folders:

mkdir -p src
mkdir -p notebooks
mkdir -p notes


	2.	Create a basic layout:

mkdir -p src/00_hello_graph
mkdir -p src/01_state_basics
mkdir -p src/02_tools_and_functions
mkdir -p src/03_memory_checkpointer
mkdir -p src/04_multi_agent
mkdir -p src/05_router_patterns
mkdir -p src/06_evaluation



Now your repo structure matches the way you’re learning.

⸻

2. Set up Python & virtual environment (clean this time)

In VS Code’s Terminal (bottom panel):

# create venv
python3 -m venv .venv

# activate it
source .venv/bin/activate

You should see (.venv) appear at the start of your terminal prompt.

Now install base deps:

pip install langgraph langchain openai ipykernel
pip freeze > requirements.txt

Create a .gitignore in the root with:

.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.env

Set interpreter in VS Code (so it stops being weird)
	•	Open Command Palette: ⇧⌘P
	•	Type: Python: Select Interpreter
	•	Pick the one that says .venv inside langgraph-playground.

Now VS Code, the terminal, and your code all agree on the same Python environment.

⸻

3. Add your first “hello-graph” experiment

Create src/00_hello_graph/hello_graph.py:

from langgraph.graph import StateGraph, END

def node_fn(state: dict) -> dict:
    print("Hello from LangGraph! State:", state)
    return {"message": "done"}

graph = StateGraph(dict)
graph.add_node("start", node_fn)
graph.set_entry_point("start")
graph.add_edge("start", END)

app = graph.compile()

if __name__ == "__main__":
    result = app.invoke({"message": "start"})
    print("Result:", result)

Run it:

python src/00_hello_graph/hello_graph.py

This file now corresponds to one Pattern Card + one Code Gallery card in Heptabase.

You’ve officially got your “executable note”.

⸻

4. Initialize Git and push to GitHub

In the same folder:

git init
git add .
git commit -m "Initial LangGraph playground setup"

Now:
	1.	Go to GitHub → New Repository
	2.	Name it langgraph-playground
	3.	Don’t add a README (you already have one)
	4.	GitHub will show you commands like:

git remote add origin https://github.com/<your-username>/langgraph-playground.git
git branch -M main
git push -u origin main



Run those.

Now your repo is live, and every little pattern you add can be committed like:

git add src/04_multi_agent/supervisor_worker.py
git commit -m "Add supervisor-worker pattern demo"
git push

Low friction, high control.

⸻

5. Align VS Code workflow with your ADHD-friendly process

We want VS Code to encourage small, focused bursts that match your Heptabase boards.

Per new concept / course lesson:
	1.	Create a new file under the right folder, e.g.:

touch src/04_multi_agent/supervisor_worker.py


	2.	Paste in the code you’re following / adapting.
	3.	Run it from the terminal:

python src/04_multi_agent/supervisor_worker.py


	4.	Once it works:
	•	Add a Pattern Card in Heptabase
	•	Add a Code Gallery card that links to this file path
	5.	Commit with a very literal message:

git add src/04_multi_agent/supervisor_worker.py
git commit -m "Add basic supervisor-worker pattern"
git push



This gives you a tight loop:

VS Code file → GitHub → Heptabase card

No other systems. No duplication.

⸻

6. Optional: branches for “learning vs. thesis”

You can keep it simple for now and just use main.

Later, when you start building the real evaluation system, you can:
	•	Create a second repo: thesis-agent-system
or
	•	Add a branch to this repo:

git checkout -b thesis-experiments

Use:
	•	main = pure learning patterns
	•	thesis-experiments = graphs directly used in your experiments

You can merge good patterns back into main later.

⸻

7. Plugging AI into VS Code (lightweight)

Since Craft can’t take your own API key, VS Code is where your custom AI buddy lives.

Options (all follow the same pattern):
	•	Install an extension like Continue.dev, Cursor, or OpenAI Chat in VS Code
	•	Configure your OpenAI / Anthropic key in the extension
	•	Use it for:
	•	Refactoring your LangGraph code
	•	Explaining error messages
	•	Generating boilerplate nodes/graphs
	•	Drafting evaluation code

Crucially: this keeps heavy AI near your code, not near your notes.

Your loop becomes:
	•	Heptabase → concept & experiment idea
	•	VS Code + AI → actual LangGraph implementation
	•	Craft → writing up results in real sentences

Everyone has a job. No app overlaps.

⸻

8. Daily “how do I start?” checklist

When you sit down to work:
	1.	Open VS Code in langgraph-playground (code ~/dev/langgraph-playground)
	2.	Activate venv in the terminal:

source .venv/bin/activate


	3.	Pick one experiment / pattern from your Heptabase “Questions That Matter” or Experiments board.
	4.	Create or open the matching file in src/...
	5.	Write/run code for 25–30 minutes (one micro-sprint)
	6.	Commit + push if it works.
	7.	Update Heptabase: Pattern Card + Code Gallery card + any experiment results.

That’s it. No overthinking.
