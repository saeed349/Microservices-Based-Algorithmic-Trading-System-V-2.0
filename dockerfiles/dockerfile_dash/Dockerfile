# FROM python:3.7

# # ENV DASH_DEBUG_MODE True

# RUN set -ex && \
#     pip install dash dash-daq dash-bootstrap-components pandas

# EXPOSE 8050

# COPY ./app /app

# WORKDIR /app

# CMD ["python", "app.py"]


FROM python:3.7
ADD requirements.txt /app/requirements.txt
WORKDIR /app/
ENV PYTHONPATH "${PYTHONPATH}:/q_pack"

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["./index.py","--host=0.0.0.0"]