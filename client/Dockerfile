FROM python:3.11-slim

RUN pip install requests requests-ntlm

COPY ntlm_test.py /app/ntlm_test.py
WORKDIR /app

CMD ["python", "ntlm_test.py"]
