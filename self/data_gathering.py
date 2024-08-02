import pandas as pd

df_output = pd.DataFrame(columns=['product_title', 'team_member_count', 'categories', 'comments_count', 'up_votes', 'day_rank', 'hunter_badge'])
def output(result: dict):
    global df_output
    df_output = df_output._append({'product_title': None, 'team_member_count': None, 'categories': result['categories'], \
                                'comments_count': result['comments_count'], 'up_votes': result['up_votes'], 'day_rank': result['day_rank'], 'hunter_badge': result['hunter_badge']}, ignore_index=True)
    df_output.to_csv('output.csv', index=False)