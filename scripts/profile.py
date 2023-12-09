from ydata_profiling import ProfileReport
import pandas as pd

df = pd.read_csv('data/car.data')

df.to_csv (r'data\car.csv', index=None)
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling/report.html")