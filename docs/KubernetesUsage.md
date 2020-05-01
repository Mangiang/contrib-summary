## Kubernetes

Requirements:

- Kunernetes
- Helm3

⚠ ⚠ ⚠

Replace:

- the repository name with whatever you want as your repository in [contrib-summary-chart/values.yaml](../contrib-summary-chart/values.yaml)

⚠ ⚠ ⚠

---

Usage

- `cd contrib-summary-chart`
- `helm dep build`
- `helm install <release name> .` you can uninstall using `helm install <release name>`

The whole Helm chart is located in the [contrib-summary-chart](../contrib-summary-chart) folder

The values are held by [contrib-summary-chart/values.yaml](../contrib-summary-chart/values.yaml)
