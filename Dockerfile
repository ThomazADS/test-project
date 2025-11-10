FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir torch torchvision torchaudio \
--index-url https://download.pytorch.org/whl/cpu
COPY . .
CMD ["python", "run.py"]