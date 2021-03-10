import numpy as np
import pandas as pd
from tqdm import tqdm # 為程式加上進度條


def main():
    df = pd.read_json('contacts.json')
    npdata = df.values


    ## Trace
    """
    define memory (dictionary) 
    with value: set of ids, 
        and email/phone/order_id as key
    """
    memory = {}
    connections = {}

    def add_to_memory(user_id: int, value: str):
        if value != "":
            if value in memory:
                memory[value].add(user_id)
                return
            memory[value] = {user_id}

    for row in tqdm(npdata):
        user_id = row[0]
        add_to_memory(user_id, row[4])
        add_to_memory(user_id, row[1])
        add_to_memory(user_id, row[2])

    for ids in tqdm(memory.values(), total=len(memory.values())):
        current_connection = set(ids)

        for uid in ids:
            if uid in connections:
                current_connection.update(connections[uid])

            for uid in current_connection:
                connections[uid] = current_connection

    output = []
    for user_id, trace in tqdm(sorted(connections.items()), total=len(connections.items())):
        contacts = np.sum(npdata[list(trace), 3])
        trace = "-".join([str(_id) for _id in sorted(trace)])
        answer = "{}, {}".format(trace, contacts)
        output.append({"ticket_id": user_id, "ticket_trace/contact": answer})
    output_df = pd.DataFrame(output)
    filename = "output.csv"
    output_df.to_csv(filename, index=False)

if __name__ == '__main__':
    main()