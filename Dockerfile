FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG BASE_DIR="/app"
WORKDIR ${BASE_DIR}

# Create folder for dependencies
ARG DEPENDENCIES_DIR="/dependencies"
RUN mkdir -p ${DEPENDENCIES_DIR}

# User and group configuration to make volumes work.
ARG UID='10001'
ARG GID='10001'

# Create a group and user
RUN addgroup --gid "${GID}" kgroup
RUN adduser \
    --disabled-password \
    --gecos "" \
    --shell "/sbin/nologin" \
    --gid="${GID}" \
    --uid="${UID}" \
    rodion

# make "rodion" owner of BASE_DIR and DEPENDENCIES_DIR
RUN chown -R rodion:kgroup ${BASE_DIR}
RUN chown -R rodion:kgroup ${DEPENDENCIES_DIR}

# Tell docker that all future commands should run as the "rodion" user
USER rodion

COPY requirements.txt ${BASE_DIR}/
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt --target "${DEPENDENCIES_DIR}"

ENV PYTHONPATH="${DEPENDENCIES_DIR}:${PYTHONPATH}"
ENV PATH="${DEPENDENCIES_DIR}/bin:${PATH}"

COPY --chown=rodion:kgroup . ${BASE_DIR}/
