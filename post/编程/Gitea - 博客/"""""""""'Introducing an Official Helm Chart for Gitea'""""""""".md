
---
title: """""""""'Introducing an Official Helm Chart for Gitea'"""""""""
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Mon, 07 Sep 2020 00:00:00 GMT
thumbnail: ''
---

<div>   
<p> techknowlogick</p>
<h2>
<a href="https://blog.gitea.io/2020/09/introducing-an-official-helm-chart-for-gitea/">
Introducing an Official Helm Chart for Gitea
</a>
</h2>
<p>
<i>Mon Sep 7, 2020</i>
by
<b>
<a href="https://github.com/techknowlogick">
techknowlogick
</a>
</b>
</p>

<p>A question that we are often asked is “How can I run Gitea on Kubernetes”, previously we had pointed users to a YAML file with a fairly standard kubernetes deployment, however this required a lot of configuration effort by the user in terms of setting up a database, managing storage, and more. Thanks to the helm chart started by <a href="https://github.com/jfelten">@jfelten</a>, which was then continued by <a href="https://github.com/cdrage">@cdrage</a>, and <a href="https://github.com/novumrgi">NOVUM-RGI</a>, that work has now been transitioned over to official support status and is being maintained by some of the original authors, as well as other Gitea maintainers.</p>
<p>We are proud to release the <a href="https://gitea.com/gitea/helm-chart/">Official Gitea Helm Chart</a>.</p>
<p>To show you how quick it is to install Gitea using our helm chart is, here is a getting started guide that also includes creating the cluster from scratch.</p>
<p>First you’ll need to <a href="https://github.com/kubernetes-sigs/kind#installation-and-usage">install KinD</a>, and create a cluster with it using <code>kind create cluster</code> and tell your local tools where they can get the configuration to connect to your newly created cluster using <code>export KUBECONFIG="$(kind get kubeconfig-path --name="kind")</code></p>
<p>Now that your cluster has been created, you’ll need to tell helm where it can look for the helm chart using <code>helm repo add gitea-charts https://dl.gitea.io/charts/</code> and to ensure that helm has the latest updates you can have it pull down the latest repo changes with <code>helm repo update</code>.</p>
<p>Finally, you can install Gitea using the default configuration with <code>helm install gitea gitea-charts/gitea</code>. There are many <a href="https://gitea.com/gitea/helm-chart/#configuration">configuration options</a> available including setting up an ingress, using an external database, and much more!</p>





  
</div>
            