import pandas as pd

columns = ['product_title', 'team_member_count', 'categories', 'comments_count', 'up_votes', 'day_rank', 'hunter_badge']

def output(result: dict):
    df_output = pd.DataFrame(columns= columns)
    row_data = {key: None for key in columns}
    for key in columns:
        if key in result:
            row_data[key] = result[key]

    df_output = pd.DataFrame([row_data])
    df_output.to_csv('output.csv', index=False, mode = 'a', header = False)