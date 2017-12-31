# pymd-wiki

## with Docker
```docker
docker-compose build
docker-compose up -d
docker-compose exec pymd-wiki /bin/bash
```

```bash
cd workspace/pymd-wiki
python3.6 -m venv venv
source venv/bin/activate
pip install --upgrade pip wheel
pip install -r requirements.txt
python -m unittest tests/test_*.py
```