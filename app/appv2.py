# nano app.py 
# Version 2

import streamlit as st
import psycopg2
import os

db_host = "<db host>"
db_name = "postgres"
db_user = "<db user>"
db_password = "<password>"
db_port = 5000

def execute_query(query, data=None, fetch=False):
	with psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password, port=db_port) as connection:
		with connection.cursor() as cursor:
			cursor.execute(query, data)
			if fetch:
				return cursor.fetchall()

execute_query('''
	CREATE TABLE IF NOT EXISTS notes (
	id SERIAL PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	content TEXT NOT NULL,
	author VARCHAR(255) NOT NULL);
	''')

def main():
	st.title('Noteblog')

	menu = ['Add Note', 'View Notes', 'Delete']
	choice = st.sidebar.selectbox('Menu', menu)

	if choice == 'Add Note':
		st.subheader('Add a New Note')
		title = st.text_input('Title')
		content = st.text_area('Content')
		author = st.text_input('Author')
		
		if st.button('Add'):
			execute_query('INSERT INTO notes (title, content, author) VALUES (%s, %s, %s);', (title, content, author))
			st.success('Note added successfully!')

	elif choice == 'View Notes':
		st.subheader('All Notes')
		notes = execute_query('SELECT id, title, content, author FROM notes;', fetch=True)
		for note in notes:
			id, title, content, author = note
			st.markdown(f'# {title}')
			st.markdown(f'### {content}')
			st.info(f'By: {author}')
			st.text(f'ID Number: {id}')
			st.write("---")

	elif choice == 'Delete':
		st.subheader("Delete a Note")
		ID_Number = st.text_input('ID Number')
		if st.button('Delete'):
			execute_query(f'''
						DELETE FROM notes
						WHERE ID = {ID_Number}
						''')
			st.success('Successfully Delete')
	
if __name__ =='__main__':
	main()
