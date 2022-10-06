---
title: "How to Restart All Pods in a Kubernetes Namespace"
author: Lane Wagner
date: "2020-10-26"
categories: 
  - "open-source"
images:
  - /img/800/restart-k8s.webp
---

Where I work, we use a repo-per-namespace setup and so it often happens that I want to restart all pods and deployments in a single Kubernetes namespace.

Maybe I want to see the startup logs, maybe I want to shut down production for a few seconds, don't question my motives.

Anyway, what matters is that bouncing all deployments one after another is really inconvenient and I don't like typing.

## The best way to bounce (kubectl >= 1.15)

I recently found out from a friend there is an easier way as of `kubectl` 1.15+. Restarting all the pods in a namespace is as easy as running the following `kubectl` command.

```bash
kubectl -n {NAMESPACE} rollout restart deploy
```

## The old way (kubectl <= 1.14)

In older versions of `kubectl` you needed to run a command for each deployment in the namespace. In true lazy-developer-fashion I wrote a little script that will do it for me:

```bash
deploys=`kubectl -n $1 get deployments | tail -n +2 | cut -d ' ' -f 1`
for deploy in $deploys; do
  kubectl -n $1 rollout restart deployments/$deploy
done
```

It's fairly simple to use. Assuming I named the script `kubebounce.sh`:

```bash
./kubebounce.sh {NAMESPACE}
```

I made a little [open-source repo](https://github.com/lane-c-wagner/kubebounce) with installation instructions if you want to add it to your $PATH. Be sure to star the repo if you find it useful.

## How It Works

Bash isn't exactly the easiest language to read. Let's go over each portion of the script.

```bash
deploys=`kubectl -n $1 get deployments | tail -n +2 | cut -d ' ' -f 1`
```

In bash, `$1` refers to the first command-line argument, the namespace in our case. In essence, this line gets all the deployments in the target namespaces and saves them into a `deploys` variable. We pipe the output of the `kubectl get deployments` command into a `tail -n +2` command, which just strips of the first line of the output. Then we run that output through a `cut` command which leaves us with a nice list of all the deployment names.

That's actually the trickier part, next we just loop over all the deployments and restart them one-by-one:

```bash
for deploy in $deploys; do
  kubectl -n $1 rollout restart deployments/$deploy
done
```
