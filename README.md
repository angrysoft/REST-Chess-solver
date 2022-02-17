# REST Chess solver


## Docker

Aplikacje można uruchomić używając dokera wystarczy wydać polecenie w katalogu aplikacji:

```
docker-compose up -d
```

Natomiast w systemie linux wystarczy:

```
make up
```

### Testy

Aby uruchomić test wydajemy polecenie

```
make test
```

## Venv

Alternatywnie można uruchomić aplikacje w wirtualnym środowisku pythona:

```
mkdir workdir
python -m venv workdir
```

Następnie kopiujemy katalog restchess do naszego workdir i wydajemy polecenia

```
cd workdir
source  bin/activate
pip install -r restchess/requirements.txt
python -m restchess.entrypoints.flask_app
```

### Testy

Testy uruchamiamy poleceniem

```
python -m pytest
```
