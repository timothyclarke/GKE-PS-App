# GKE-PS-app

Helm version of the app is in the `parser` directory. Install with `helm upgrade parser parser --install`. As the app itself is small it easily fits within a config map of the chart as such it was easier to run it there rather than building the container, pushing the container to a registry, then creating the deployment and pulling the container.

If you want to review some other heal charts please feel free to look at [my helm charts repo](https://github.com/timothyclarke/helm-charts/tree/master/charts)
If you want to test any of those charts them use `helm repo add timothyclarke https://timothyclarke.github.io/helm-charts/`

Using `gcr.io/cloud-builders/kubectl` to get kubectl config for deployment
