FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Créer et placer le répertoire de travail
WORKDIR /app/

# Ajouter le répertoire au niveau du répertoire créé
ADD . /app/

# Installation des dépendences et updates
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
        && apk add gcc libc-dev linux-headers postgresql-dev \
        && pip install --upgrade pip \
        && pip install --no-cache-dir -r requirements.txt \
        && apk del .temp-build-deps

# Rendre le script exécutable
RUN chmod +x /app/autorun.sh

# Port d'exécution de l'application
EXPOSE 8000

# Démarrer l'application
ENTRYPOINT ["sh", "/app/autorun.sh"]