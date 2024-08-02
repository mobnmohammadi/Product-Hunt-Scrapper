import pandas as pd

df_output = pd.DataFrame(columns=['product_title', 'team_member_count', 'categories', 'comments_count', 'up_votes', 'day_rank', 'hunter_badge'])
def output(result: dict):
    global df_output
    if result['product_title'] is not None:
        df_output = df_output._append({'product_title': result['product_title'], 'team_member_count': result['team_member_count'], 'categories': result['categories'], \
                                   'comments_count': result['comments_count'], 'up_votes': result['up_votes'], 'day_rank': result['day_rank'], 'hunter_badge': result['hunter_badge']}, ignore_index=True)
    
    df_output.to_csv('output.csv', index=False)