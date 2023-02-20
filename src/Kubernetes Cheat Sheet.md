Kubernetes Cheat Sheet

Commands:
```bash
kubectl get: Retrieve information about resources in a cluster
kubectl get pods: List all pods in the cluster
kubectl get services: List all services in the cluster
kubectl get deployments: List all deployments in the cluster
kubectl describe: Describe the details of a specific resource
kubectl describe pod <pod-name>: Describe a specific pod
kubectl describe service <service-name>: Describe a specific service
kubectl describe deployment <deployment-name>: Describe a specific deployment
kubectl create: Create a new resource in the cluster
kubectl create -f <file.yaml>: Create a resource defined in a YAML file
kubectl create secret generic <secret-name> --from-literal=<key>=<value>: Create a new Secret with a specific key and value
kubectl delete: Delete a resource from the cluster
kubectl delete -f <file.yaml>: Delete a resource defined in a YAML file
kubectl delete pod <pod-name>: Delete a specific pod
kubectl apply: Update a resource in the cluster
kubectl apply -f <file.yaml>: Update a resource defined in a YAML file
kubectl exec: Execute a command in a container
kubectl exec -it <pod-name> <command>: Execute a command in an interactive terminal in a specific pod
kubectl scale: Scale the number of replicas in a Deployment
kubectl scale deployment <deployment-name> --replicas=<number>: Scale the number of replicas in a specific deployment
kubectl logs: Retrieve the logs of a container
kubectl logs <pod-name>: Retrieve the logs of a specific pod
```

## YAML Definitions:

* apiVersion: The version of the Kubernetes API used for the resource
* kind: The type of resource being defined (e.g. Pod, Service, Deployment)
* metadata: Information about the resource such as its name
* spec: The desired state of the resource, including details about replicas, containers, and ports

## Concepts:

* Pods: The smallest and simplest unit in the Kubernetes object model, a pod represents a single process running in a cluster
* Services: A way to expose a set of pods to the network, either within the cluster or externally
* Deployments: A higher-level resource that manages the scaling and rolling updates of pods
* ConfigMaps: A way to manage application configuration separate from the application's code
* Secrets: A way to manage sensitive information such as passwords and tokens.

## Interview questions on Kubernetes. 

## How would you troubleshoot a pod that is in a CrashLoopBackOff state?
* Answer: One way to troubleshoot a pod in a CrashLoopBackOff state is to check the pod's logs using the kubectl logs command. For example, if the pod is named "my-pod", you can check its logs using the following command:

```bash
  kubectl logs my-pod
```
This will display the logs of the pod, which can provide insights into the cause of the crash.

Another way to troubleshoot a pod in a CrashLoopBackOff state is to check the events related to the pod using the kubectl describe pod command. For example:

```bash
kubectl describe pod my-pod
```
This will provide information about the pod's status, including events that have occurred and the reason for the pod's current state.

## How would you deploy an application that requires a specific version of a certain package?

* Answer: One way to deploy an application that requires a specific version of a certain package is to use a Docker image that includes the required package version. For example, if the application requires version 1.2.3 of package "mypackage", you can use a Docker image that has mypackage version 1.2.3 installed.

Another way to deploy an application that requires a specific version of a certain package is to use a InitContainer in the pod definition that installs the package using a package manager such as apt-get or yum.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-image:latest
  initContainers:
  - name: install-mypackage
    image: busybox
    command:
      - sh
      - -c
      - "apk add --no-cache mypackage==1.2.3"

```
In this example, we use an InitContainer named "install-mypackage" that uses the busybox image and runs the command "apk add --no-cache mypackage==1.2.3" which installs mypackage version 1.2.3 before the container "my-container" is started.

## How would you configure a Kubernetes cluster to automatically roll out updates to a Deployment?
* Answer: One way to configure a Kubernetes cluster to automatically roll out updates to a Deployment is to use a Deployment strategy such as the RollingUpdate strategy.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
```

In this example, we set the strategy type to RollingUpdate and configure the rolling update strategy with the following options:

maxUnavailable: 1 which means that at most one pod will be unavailable during the update.
maxSurge: 1 which means that at most one additional pod will be created during the update.
This will automatically roll out updates to the pods in the deployment, ensuring that at least 2 replicas are available at all times during the update process.

## How would you scale a Deployment up and down based on CPU usage?

* Answer: One way to scale a Deployment up and down based on CPU usage is to use Kubernetes Horizontal Pod Autoscaler (HPA) which automatically scales the number of pods in a Deployment based on a specified metric.

```yaml
apiVersion: autoscaling/v2beta1
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
```
In this example, we create an HPA named "my-app-hpa" that targets the Deployment "my-app-deployment" and set the minimum replicas to 2 and the maximum replicas to 10. We also set the metric to be the CPU usage, and set the target average utilization to 50%, meaning that when the average CPU usage across all pods exceeds 50%, the HPA will scale the number of replicas up, and when it falls below 50%, it will scale the number of replicas down.

## How would you configure a Kubernetes cluster to automatically roll out updates to a StatefulSet?

* Answer: One way to configure a Kubernetes cluster to automatically roll out updates to a StatefulSet is to use a rolling update strategy. For example, the following StatefulSet definition includes a rolling update strategy that updates one pod at a time.
  

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: my-app-statefulset
spec:
  serviceName: my-app-service
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app-container
        image: my-app-image:latest
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 1
```
In this example, the StatefulSet named "my-app-statefulset" uses a rolling update strategy with a partition value of 1, meaning that the StatefulSet updates one pod at a time. This ensures that the pods are updated in a rolling fashion, maintaining the availability of the service during the update process.

## How would you configure a Kubernetes cluster to automatically roll out updates to a DaemonSet?

* Answer: One way to configure a Kubernetes cluster to automatically roll out updates to a DaemonSet is to use a rolling update strategy. For example, the following DaemonSet definition includes a rolling update strategy that updates one pod at a time.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: my-app-daemonset
spec:
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app-container
        image

```





## How would you create a Kubernetes deployment using a YAML file?
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myregistry/myapp:latest
        ports:
        - containerPort: 8080
```

This YAML file creates a Deployment named myapp-deployment with 3 replicas. It specifies the container image to use, the ports to expose and the labels to use. By using the command kubectl apply -f mydeployment.yaml this deployment will be created in the Kubernetes cluster.

## How would you scale a Deployment in Kubernetes?

```bash
kubectl scale deployment myapp-deployment --replicas=5
```
This command will scale the deployment myapp-deployment to have 5 replicas.

## How would you create a Kubernetes Service to expose a Deployment?

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
  - name: http
    port: 80
    targetPort: 8080
  type: LoadBalancer
```
This YAML file creates a Service named myapp-service that selects pods with the label app=myapp and exposes them on port 80 with the type LoadBalancer, which creates a load balancer and assigns it an external IP address.

## How would you use a ConfigMap to manage application configuration in Kubernetes?

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
data:
  app_setting_1: "value1"
  app_setting_2: "value2"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myregistry/myapp:latest
        ports:
        - containerPort: 8080
        envFrom:
        - configMapRef:
            name: myapp-config
```

This YAML file creates a ConfigMap named myapp-config that contains key-value pairs for application settings, and then it uses these ConfigMap to set the environment variables for the containers in the Deployment myapp-deployment.

## How would you use Kubernetes Secrets to manage sensitive information for your application?

```bash
kubectl create secret generic myapp-secret --from-literal=password=mysecretpassword
```
This command creates a Kubernetes Secret named myapp-secret with the key password and the value mysecretpassword. Then, to use this Secret in


## Examples

## Creating a Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app
          image: my-app:latest
          ports:
            - containerPort: 80
```

In this example, we are creating a Deployment named "my-app-deployment", with 3 replicas. The selector specifies that the pods that this deployment manages should have the label "app: my-app", and the template defines the pods' specification including the container name, image and port.

## Creating a Service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
    - name: http
      port: 80
      targetPort: 80
  type: ClusterIP
```

In this example, we are creating a Service named "my-app-service" that selects pods with the label "app: my-app" and expose port 80 as a ClusterIP service.

## Creating a ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-app-config
data:
  app.config: |-
    {
        "apiUrl": "http://localhost:3000",
        "logLevel": "debug"
    }
```
In this example, we are creating a ConfigMap named "my-app-config" that contains a key-value pair, where the key is "app.config" and the value is a JSON containing the configuration for the application.

## Creating a Secret:
```yaml 
apiVersion: v1
kind: Secret
metadata:
  name: my-app-secret
data:
  apiKey: cGFzc3dvcmQ=
```

In this example, we are creating a Secret named "my-app-secret" that contains a key-value pair where the key is "apiKey" and the value is "cGFzc3dvcmQ=" which is a base64 encoded string of the actual key value.

## Scaling a Deployment:
```bash
kubectl scale deployment my-app-deployment --replicas=5
```

In this example, we are scaling the "my-app-deployment" deployment to 5 replicas.

Note: These are just examples and may not work as expected in a real-world cluster. They also depend on the specific version of Kubernetes and may need to be adjusted accordingly.

