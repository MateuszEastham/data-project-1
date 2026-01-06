"""Main execution script.

This step adds the Analysis Module. We verify that we can perform
time series aggregation and statistical analysis on the loaded data.
"""
from config import( DATA_CSV_FILE, ENABLE_DATA_PROCESSING, ENABLE_TIME_SERIES, 
ENABLE_EXPLORATORY_ANALYSIS, ENABLE_STATIC_PLOTS, ENABLE_DASHBOARDS)

from utils import clean_outputs, print_section
import data
import analysis
import visualization

def test_analysis_module():
    print_section('VISUALIATION MODULE TEST')
    
    clean_outputs()
    
 # 1. Load Data and Analyze (Reusing previous steps)
    if ENABLE_DATA_PROCESSING and ENABLE_TIME_SERIES:
        data.download_required_files()
        df = data.load_and_explore_data(DATA_CSV_FILE)
        df_clean = data.preprocess_data(df)

        results = analysis.aggregate_time_series(df_clean)
        df_yearly, ts_data, ts_years, df_model_yearly, df_region_yearly = results
        
        # 2. Static Visualization
        if ENABLE_STATIC_PLOTS:
            print("\nTesting static visualization...")
            visualization.create_overview_visualizations(df_yearly, df_clean)
            visualization.create_heatmap(df_clean)

        # 3. Interactive Dashboards
        if ENABLE_DASHBOARDS:
            print("\nTesting interactive dashboards...")
            visualization.create_interactive_dashboard(ts_years, ts_data, df_yearly, df_clean)
            visualization.create_heatmap_interactive(df_model_yearly)
            
        print(f"\n✅ Step 4 Complete: Visualizations generated in 'outputs' directory.")

if __name__ == "__main__":
    test_analysis_module()

