FROM ubuntu:20.04
MAINTAINER vkhurana@users.noreply.github.com

ARG LABEL_VERSION="python3"

LABEL name="calibre-convert" \
    version=${LABEL_VERSION} \
    description="Monitors a folder for .epub files and uses Calibre's ebook-convert to convert to .mobi automatically" \
    maintainer="Vivek Khurana <vkhurana@users.noreply.github.com>"

ENV TZ=Etc/UTC
ARG DEBIAN_FRONTEND=noninteractive
VOLUME /target

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    calibre

RUN apt-get clean \
  && rm -rf /var/cache/apt/* /var/lib/apt/lists/*

WORKDIR /calibre-convert

COPY requirements.txt ./
COPY convert.py ./

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Run the script when the image is run
ENTRYPOINT ["python3", "/calibre-convert/convert.py"]