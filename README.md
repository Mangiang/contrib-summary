# contrib-summary
A small tool to generate a summary of a user contributions over a specific time period

---

## Usage
- [Local](#local)
- [Docker](#docker)
- [Kubernetes](#kubernetes)
- [Skaffold](#skaffold)

### Local
Requirements:
- Python3.6 or above
Usage
- `pip install -r requirements.txt`
- `python -m server.app`
- The server should be available at localhost:80

### Docker
Requirements:
- Docker Client

Usage
- `docker build .` alternatively you can choose a name using the `-t` option of `docker build`
- `docker run -it <image name>`
- The server should be available at localhost:80

### Kubernetes
Requirements:
- Kunernetes
- Helm3

Usage
- `cd contrib-summary-chart`
- `helm dep build`
- `helm install <release name> .` you can uninstall using `helm install <release name>`

### Skaffold dev
Requirements:
- Kunernetes
- Helm3

Usage
- `skaffold dev`
