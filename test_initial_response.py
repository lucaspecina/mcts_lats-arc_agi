from mcts_lats.agent import initial_answer_chain

initial_response = initial_answer_chain.invoke(
    {"input": "Write a research report on lithium pollution."}
)
print(initial_response)