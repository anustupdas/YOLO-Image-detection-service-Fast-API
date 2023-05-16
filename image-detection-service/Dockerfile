FROM python:3.8-slim AS builder
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    python3 \
    gcc \
    wget
RUN apt install libgl1 -y
RUN apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx -y
RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*


ARG USERNAME=image-detection-service
ARG VERSION=0.5.0
RUN test -n "${VERSION}" || (echo "VERSION not set" && false)
RUN useradd -u 1001 -m -s /bin/bash ${USERNAME}
USER ${USERNAME}
COPY requirements.txt /
RUN pip install setuptools wheel --no-cache-dir \
 && pip install -r requirements.txt --user \
 && pip install image-detection-service==${VERSION} --user
RUN pip list

RUN pip uninstall opencv-python -y
RUN pip install opencv-python-headless
RUN pip list

FROM python:3.8-slim
ARG USERNAME=image-detection-service
RUN useradd -u 1001 -m -s /bin/bash ${USERNAME}
USER ${USERNAME}
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
COPY --from=builder --chown=1001 /home/${USERNAME}/.local /home/${USERNAME}/.local
USER root
RUN mkdir -p /etc/${USERNAME}/
RUN mkdir -p /etc/image_detection_service
RUN mkdir -p /etc/image_detection_service/data/ && mkdir -p /etc/image_detection_service/data/classes && mkdir -p /etc/image_detection_service/data/dataset
RUN chown ${USERNAME} /etc/${USERNAME}
COPY requirements.txt /
COPY default_config.yml /etc/${USERNAME}/config.yml
COPY data/classes/coco.names /etc/image_detection_service/data/classes/coco.names
COPY data/dataset/val2017.txt /etc/image_detection_service/data/dataset/val2017.txt
RUN chmod -R 777 /etc/image_detection_service/
USER ${USERNAME}
ENV REMOTE_CONFIG_URL=/etc/${USERNAME}/config.yml
EXPOSE 5000 8080
CMD ["run-cli"]
