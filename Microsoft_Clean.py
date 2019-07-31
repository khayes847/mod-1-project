import pandas as pd
import numpy as np
from Microsoft_Cleanup import *
import warnings

#we don't want any annoying warnings embarassing us here...
warnings.filterwarnings('ignore')

def Clean_Data(df1, df2, df3, df4, df5):

	# Switch variables from string to float:
	cast_to_float32(df1, 'production_budget')
	cast_to_float32(df1, 'worldwide_gross')
	
	# Create column for net profit (worldwide gross minus production budget):
	net_columns(df1, 'worldwide_gross', 'production_budget')
	
	# Create column for ratio (net profit divided by production budget):
	divide_columns(df1, 'net', 'production_budget')
	
	# Rename column 'movie' to 'title':
	rename_col(df1, 'movie', 'title')
	
	# Remove whitespace, potential extra words, punctuation, and case from titles:
	cleanup_text(df1, 'title')
	
	# Remove month and year from date:
	convert_year(df1, 'release_date')
	
	# Drop redundant columns:
	drop_cols(df1, 'id', 'domestic_gross', 'release_date')
	
	# Remove 'studio', 'domestic_gross', 'foreign_gross' column:
	drop_cols(df2, 'domestic_gross', 'foreign_gross')
	
	# Set 'year' to string:
	cast_to_str(df2, 'year')
	
	# Remove years, right whitespace, and superfluous verbiage from titles:
	cleanup_text(df2, 'title')
	
	# Merge df1 and df2:
	merged_df = left_merge(df1, df2, 'title', 'year')
	
	# Replace null studio values:
	fill_na(merged_df, 'studio')
	
	# Create 'year' string column from 'start_year':
	cast_to_str(df3, 'start_year')
	rename_col(df3, 'start_year', 'year')
	
	# Drop unused/confusing column:
	drop_cols(df3, 'original_title')
	
	# Rename column for easier merging:
	rename_col(df3, 'primary_title', 'title')
	
	# Remove years, right whitespace, and superfluous verbiage from titles:
	cleanup_text(df3, 'title')
	
	# Merge df3 with merged datafile:
	merged_df2 = left_merge(merged_df, df3, 'title', 'year')
	
	# Cast year to integer:
	cast_to_int(merged_df2, 'year')
	
	# Throw out all films made before 2010:
	cutoff_series_at(merged_df2, 'year', 2010)
	
	# Now cast year back to string:
	cast_to_str(merged_df2, 'year')
	
	# Merge df5 and df4:
	df4_prin = pd.merge(df5, df4,
        	                  on=["nconst"], how="left")
	
	# Remove extraneous columns:
	drop_cols(df4_prin, 'ordering',
        	                                      'nconst', 'job',
                	                              'characters', 'birth_year',
                        	                      'death_year',
                                	              'primary_profession',
                                        	      'known_for_titles')
	
	# Create list of directors from df4_prin:
	directors = subset_series(df4_prin, 'category', 'director')
	
	# Merge list of directors with previous merged document:= 
	merged_df3 = left_merge(merged_df2, directors, 'tconst')
	
	# Remove extra columns:
	drop_cols(merged_df3, 'category', 'runtime_minutes')
	
	#rename primary_name to, "director":
	rename_col(merged_df3, 'primary_name', 'director')
	
	# Fill in null director values:
	fill_na(merged_df3, 'director')
	
	# Now, create list of producers from df4_prin:
	producers = subset_series(df4_prin, 'category', 'producer')
	
	# Rename column primary_name to, "producer":
	rename_col(producers, 'primary_name', 'producer')
	
	# Drop column 'category':
	drop_cols(producers, 'category')
	
	# Merge list of producers with merged document:
	merged_df4 = pd.merge(merged_df3, producers, on=["tconst"], how="left")
	
	# Fill null producer values:
	fill_na(merged_df4, 'producer')
	
	# Remove duplicate titles:
	remove_duplicates(merged_df4, 'title')
	
	# Finally, drop the extra column:
	drop_cols(merged_df4, 'tconst')
	
	# And rename:
	md_clean = merged_df4
	return md_clean
