import numpy as np
from pandas import DataFrame

# 呼叫agg()做各種分組統計
def aggregate(df):
    # agg()可以分組統計一個(count)或多個(count, sum, mean, max, min)皆可
    print("計算每個區域的商店數量、營業額總和、平均營業額、最高營業額、最低營業額")
    region_stats = df.groupby('Region').agg(
        Count=('ID', 'count'),
        Total_Revenue=('Monthly_Revenue', 'sum'),
        Average_Revenue=('Monthly_Revenue', 'mean'),
        Max_Revenue=('Monthly_Revenue', 'max'),
        Min_Revenue=('Monthly_Revenue', 'min')
    ).reset_index()
    # 只格式化 Average_Revenue 到小數1位
    region_stats = region_stats.round({'Average_Revenue': 1})  
    # 格式化所有float類型column到小數1位，整數類型不影響
    # region_stats = region_stats.apply(lambda x: x.round(1))
    print(region_stats)

# 將分組統計結果合併
def aggregate_merge(df):
    print("計算每個區域的商店數量、營業額總和、平均營業額")
    region_stats = df.groupby('Region').agg(
        Count=('ID', 'count'),
        Total_Revenue=('Monthly_Revenue', 'sum'),
        Average_Revenue=('Monthly_Revenue', 'mean'),
    ).reset_index().round({'Average_Revenue': 1})  # 格式化 Average_Revenue 到小數1位
    print(region_stats)
    print("-----------------------------------")

    # agg()只能取得max, min的值，
    # 如果要max, min詳細資料，可以使用idxmax(), idxmin取得對應index後再搭配column取得
    # 如果有多筆資料的最高、最低值相同，則取第一筆
    region_max = df.loc[
        df.groupby('Region')['Monthly_Revenue'].idxmax(),
        ['Region', 'Name', 'Monthly_Revenue']]
    print(f"每個區域營業額最高的商店:\n{region_max}")
    print("-----------------------------------")

    region_min = df.loc[
        df.groupby('Region')['Monthly_Revenue'].idxmin(),
        ['Region', 'Name', 'Monthly_Revenue']]
    print(f"每個區域營業額最低的商店:\n{region_min}")
    print("-----------------------------------")

    # 當merge雙方的欄位名稱重複時才會加上suffix，否則不影響欄位名稱
    region_stats = region_stats.merge(
        region_max, on='Region', suffixes=('', '_Max'))
    region_stats = region_stats.merge(
        region_min, on='Region', suffixes=('', '_Min'))

    print(f"將所有結果合併:\n{region_stats}")


def main():
    # 建立10筆測試用的便利商店資料
    data = {
        'ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010'],
        'Name': ['FamilyMart Taipei', 'FamilyMart Taichung', 'FamilyMart Kaohsiung', 'FamilyMart Taitung',
                 'FamilyMart Taoyuan', 'FamilyMart Chiayi', 'FamilyMart Tainan', 'FamilyMart Hualien',
                 'FamilyMart Kaohsiung 2', 'FamilyMart Taipei 2'],
        'Region': ['North', 'Central', 'South', 'East', 'North', 'Central', 'South', 'East', 'South', 'North'],
        'Monthly_Revenue': [850000, 730000, 650000, 400000, 780000, 720000, 680000, 420000, 700000, 830000]
    }
    # 建立 DataFrame
    df = DataFrame(data)

    aggregate(df)
    print("===================================")
    aggregate_merge(df)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")