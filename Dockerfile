FROM python:3.7-alpine

ENV FLASK_APP simpyinvoice.py
ENV APP_NAME simpyinvoice
ENV FLASK_CONFIG test
ENV SIMPYINVOICE_SECRET_KEY TA2l6XTGWtajkNjybhyRLdtSMaJweAph
ENV FLASK_ENV testing

WORKDIR /home

COPY Pipfile Pipfile
RUN pip install pipenv \
    && pipenv lock --requirements > requirements.txt \
    && pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY simpyinvoice.py config.py test_boot.sh ./

RUN flask db upgrade

EXPOSE 5000
CMD flask run
