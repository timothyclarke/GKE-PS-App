# GKE-PS-app

Helm version of the app is in the `parser` directory. Install with `helm upgrade parser parser --install`. As the app itself is small it easily fits within a config map of the chart as such it was easier to run it there rather than building the container, pushing the container to a registry, then creating the deployment and pulling the container.

If you want to review some other heal charts please feel free to look at [my helm charts repo](https://github.com/timothyclarke/helm-charts/tree/master/charts)
If you want to test any of those charts them use `helm repo add timothyclarke https://timothyclarke.github.io/helm-charts/`

To deploy this using google cloud build create ithe following environmental variables
* `$_KUBE_CONFIG` and populate it with a base64 encoded version of your kube config
* `$_CLIENT_TOKENS` and populate with the base64 encoded client tokens

## Example kubeconfig

```
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: /workspace/.kube/ca.crt
    server: https://35.189.123.92
  name: gke-test-1
contexts:
- context:
    cluster: gke-test-1
    user: gke-test-1
  name: gke-test-1
current-context: gke-test-1
kind: Config
preferences: {}
users:
- name: gke-test-1
  user:
    token: /workspace/.kube/token
```
