FROM python:3.11.3

WORKDIR /etl

# Copy the code
COPY etl/ .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the code
CMD [ "python", "etl.py" ]


