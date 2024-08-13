from mcts_lats.data_processing import load_tasks_from_file, task_sets, json_task_to_string
from mcts_lats.graph_workflow import setup_workflow
from mcts_lats.utils import init_prompt


def main(task_id, debug=False):
    # Load task
    challenges, solutions = load_tasks_from_file(task_sets['training'])
    task_string = json_task_to_string(challenges, task_id, 0)
    question = init_prompt + "\n" + task_string
    
    print(f"Prompt:\n{question}") if debug else None

    # setup graph workflow
    graph = setup_workflow()
    
    # invoke graph
    for step in graph.stream({"input": question}):
        last_step = step
        step_name, step_state = next(iter(step.items()))
        print(step_name)
        print("rolled out: ", step_state["root"].height)
        print("---")


    # Get best solution
    solution_node = last_step["expand"]["root"].get_best_solution()
    best_trajectory = solution_node.get_trajectory(include_reflections=False)
    print(best_trajectory[-1].content)


if __name__ == "__main__":
    main("0520fde7", debug=True)