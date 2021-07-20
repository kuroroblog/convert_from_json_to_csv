# @note ModuleNotFoundError: No module named 'pandas' と出ましたら、$ `pip install pandas`を実行。
import pandas as pd

# 参考 : https://qiita.com/yukiyoshimura/items/4c8d535ac79843d0fb0e
# 変換したいJSONファイルを読み込む
df = pd.read_json('./test.json')
df_json = pd.json_normalize(df['data'])
df_json.to_csv("./result.csv", encoding='utf-8')
