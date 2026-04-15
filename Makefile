.PHONY: help install test run docker-build docker-run docker-stop clean deploy-heroku

help:
	@echo "Walmart ESG Dashboard - Available Commands"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make install        - Install dependencies in virtual environment"
	@echo "  make test          - Run installation tests"
	@echo ""
	@echo "Running:"
	@echo "  make run           - Run dashboard locally"
	@echo "  make dev           - Run in development mode with auto-reload"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-run    - Run Docker container"
	@echo "  make docker-stop   - Stop Docker container"
	@echo "  make docker-compose - Run with docker-compose"
	@echo ""
	@echo "Deployment:"
	@echo "  make deploy-heroku - Deploy to Heroku"
	@echo "  make deploy-streamlit - Guide for Streamlit Cloud"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean         - Clean temporary files"
	@echo "  make update        - Update dependencies"
	@echo ""

install:
	@echo "Creating virtual environment..."
	python3 -m venv venv
	@echo "Installing dependencies..."
	./venv/bin/pip install -r requirements.txt
	@echo "✅ Installation complete!"

test:
	@echo "Running installation tests..."
	./venv/bin/python test_installation.py

run:
	@echo "Starting dashboard..."
	./venv/bin/streamlit run app.py

dev:
	@echo "Starting dashboard in development mode..."
	./venv/bin/streamlit run app.py --server.runOnSave true

docker-build:
	@echo "Building Docker image..."
	docker build -t walmart-esg-dashboard:latest .
	@echo "✅ Docker image built successfully!"

docker-run:
	@echo "Running Docker container..."
	docker run -d -p 8501:8501 --name walmart-esg-dashboard walmart-esg-dashboard:latest
	@echo "✅ Dashboard running at http://localhost:8501"

docker-stop:
	@echo "Stopping Docker container..."
	docker stop walmart-esg-dashboard
	docker rm walmart-esg-dashboard
	@echo "✅ Container stopped"

docker-compose:
	@echo "Starting with docker-compose..."
	docker-compose up -d
	@echo "✅ Dashboard running at http://localhost:8501"

docker-compose-stop:
	@echo "Stopping docker-compose..."
	docker-compose down
	@echo "✅ Services stopped"

deploy-heroku:
	@echo "Deploying to Heroku..."
	@if [ -z "$(APP_NAME)" ]; then \
		echo "Usage: make deploy-heroku APP_NAME=your-app-name"; \
		exit 1; \
	fi
	heroku create $(APP_NAME)
	git push heroku main
	heroku open
	@echo "✅ Deployed to Heroku!"

deploy-streamlit:
	@echo "To deploy to Streamlit Cloud:"
	@echo "1. Push code to GitHub"
	@echo "2. Go to https://share.streamlit.io"
	@echo "3. Sign in with GitHub"
	@echo "4. Click 'New app'"
	@echo "5. Select your repository and app.py"
	@echo "6. Click 'Deploy'"

clean:
	@echo "Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	@echo "✅ Cleaned!"

update:
	@echo "Updating dependencies..."
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt --upgrade
	@echo "✅ Dependencies updated!"

freeze:
	@echo "Freezing current dependencies..."
	./venv/bin/pip freeze > requirements.txt
	@echo "✅ requirements.txt updated!"

lint:
	@echo "Running code linter..."
	./venv/bin/pip install flake8 pylint
	./venv/bin/flake8 app.py --max-line-length=120
	@echo "✅ Linting complete!"

format:
	@echo "Formatting code..."
	./venv/bin/pip install black
	./venv/bin/black app.py
	@echo "✅ Code formatted!"
