# Установка зависимостей
install:
	pip install -r requirements.txt

# Запуск тестов с использованием pytest
test:
	pytest tests/

# Запуск Streamlit приложения
run:
	streamlit run steps/5_streamlit_app.py

# Проверка зависимостей (дополнительно для форматирования и стиля)
lint:
	flake8 steps/ tests/

# Удаление скомпилированных файлов Python
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
