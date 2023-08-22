# Calibre Convert

Monitors a folder for .epub files and uses Calibre's ebook-convert to convert files from .epub to .mobi automatically.

This is a docker image on Ubuntu with Python and Calibre, and uses `watchdog` to monitor the directory.

## License

![GitHub License](https://img.shields.io/github/license/vkhurana/calibre-convert)  

## Build Status

[Code and Pipline is on GitHub](https://github.com/vkhurana/calibre-convert):  
![GitHub Last Commit](https://img.shields.io/github/last-commit/vkhurana/calibre-convert?logo=github)  
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vkhurana/calibre-convert/.github/workflows/BuildPublishPipeline.yml?logo=docker)
## Container Images

Docker container images are published on [Docker Hub](https://hub.docker.com/r/vkhurana/calibre-convert).  
Images are tagged using `latest`

![Docker Pulls](https://img.shields.io/docker/pulls/vkhurana/calibre-convert?logo=docker)  
![Docker Image Version](https://img.shields.io/docker/v/vkhurana/calibre-convert/latest?logo=docker)

## Usage
Sample usage with ephemeral container:
```
docker run -v /folder/to/watch:/target -it --rm vkhurana/calibre-convert:latest
```

## Background Info

This is a stateless container.

## Notes

- Runs on `Python 3`
- Pulls `Calibre` from apt

