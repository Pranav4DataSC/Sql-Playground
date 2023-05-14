## streamlit,pandas,sqlite3
## download sublime text
#core packages 
import streamlit as st
import pandas as pd
#db mgmt. 
import sqlite3
conn = sqlite3.connect('data/world.sqlite')
c = conn.cursor()

city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']

# fn execute sql
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data
def main():
	st.title("SQL Playground")
	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("HomePage")
		st.subheader("Tables Names : city ,country, countrylanguage ")
		# column layout
		col1,col2 = st.columns(2)
	
		with col1:
			with st.expander('Schema Info reference'):
				t_info = {'city':city,'country':country,'countrylanguage':countrylanguage}
				st.json(t_info)
			with st.form(key='query_form'):
				raw_code = st.text_area("Your SQL code here")
				submit_code = st.form_submit_button("Execute Code")
			# table of Info
			
		#Results layout
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)
				# Results
				query_results = sql_executor(raw_code)
				with st.expander("Results"):
					st.write(query_results)		
				with st.expander("Pretty Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)	
	else:
		st.subheader("About")

if __name__ == '__main__':
	main()
