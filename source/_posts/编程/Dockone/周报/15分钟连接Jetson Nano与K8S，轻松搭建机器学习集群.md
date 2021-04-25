
---
title: '15分钟连接Jetson Nano与K8S，轻松搭建机器学习集群'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=8588'
author: Dockone
comments: false
date: 2021-04-25 08:08:09
thumbnail: 'https://picsum.photos/400/300?random=8588'
---

<div>   
<br>在本文中我将展示如何将Jetson Nano开发板连接到Kubernetes集群以作为一个GPU节点。我将介绍使用GPU运行容器所需的NVIDIA docker设置，以及将Jetson连接到Kubernetes集群。在成功将节点连接到集群后，我还将展示如何在Jetson Nano上使用GPU运行简单的TensorFlow 2训练会话。<br>
<br><h2>K3s还是K8s？</h2>K3s是一个轻量级Kubernetes发行版，其大小不超过100MB。在我看来，它是单板计算机的理想选择，因为它所需的资源明显减少。你可以查看我们的往期文章，了解更多关于K3s的教程和生态。在K3s生态中，有一款不得不提的开源工具K3sup，这是由Alex Ellis开发的，用于简化K3s集群安装。你可以访问Github了解这款工具：<br>
<a href="https://github.com/alexellis/k3sup"></a><a href="https://github.com/alexellis/k3sup" rel="nofollow" target="_blank">https://github.com/alexellis/k3sup</a><br>
<br><h2>我们需要准备什么？</h2><ul><li>一个K3s集群——只需要一个正确配置的主节点即可</li><li>NVIDIA Jetson Nano开发板，并安装好开发者套件</li></ul><br>
<br>如果你想了解如何在开发板上安装开发者套件，你可以查看以下文档：<br>
<a href="https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write"></a><a href="https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write" rel="nofollow" target="_blank">https://developer.nvidia.com/e ... write</a><br>
<ul><li>K3sup</li><li>15分钟的时间</li></ul><br>
<br><h2>计划步骤</h2><ol><li>设置NVIDIA docker</li><li>添加Jetson Nano到K3s集群</li><li>运行一个简单的MNIST例子来展示Kubernetes pod内GPU的使用</li></ol><br>
<br><h2>设置NVIDIA docker</h2>在我们配置Docker以使用nvidia-docker作为默认的运行时之前，我需要先解释一下为什么要这样做。默认情况下，当用户在Jetson Nano上运行容器时，运行方式与其他硬件设备相同，你不能从容器中访问GPU，至少在没有黑客攻击的情况下不能。如果你想自己测试一下，你可以运行以下命令，应该会看到类似的结果：<br>
<br><code class="prettyprint">1. root@jetson:~# echo &quot;python3 -c 'import tensorflow'&quot; | docker run -i<br>
    icetekio/jetson-nano-tensorflow /bin/bash<br>
 2. 2020-05-14 00:10:23.370761: W<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could<br>
    not load dynamic library 'libcudart.so.10.2'; dlerror:<br>
    libcudart.so.10.2: cannot open shared object file: No such file or<br>
    directory; LD_LIBRARY_PATH:<br>
    /usr/local/cuda-10.2/targets/aarch64-linux/lib:<br>
 3. 2020-05-14 00:10:23.370859: I<br>
    tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above<br>
    cudart dlerror if you do not have a GPU set up on your machine.<br>
 4. 2020-05-14 00:10:25.946896: W<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could<br>
    not load dynamic library 'libnvinfer.so.7'; dlerror:<br>
    libnvinfer.so.7: cannot open shared object file: No such file or<br>
    directory; LD_LIBRARY_PATH:<br>
    /usr/local/cuda-10.2/targets/aarch64-linux/lib:<br>
 5. 2020-05-14 00:10:25.947219: W<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could<br>
    not load dynamic library 'libnvinfer_plugin.so.7'; dlerror:<br>
    libnvinfer_plugin.so.7: cannot open shared object file: No such file<br>
    or directory; LD_LIBRARY_PATH:<br>
    /usr/local/cuda-10.2/targets/aarch64-linux/lib:<br>
 6. 2020-05-14 00:10:25.947273: W<br>
    tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:30] Cannot dlopen<br>
    some TensorRT libraries. If you would like to use Nvidia GPU with<br>
    TensorRT, please make sure the missing libraries mentioned above are<br>
    installed properly.<br>
 7. /usr/lib/python3/dist-packages/h5py/__init__.py:36: FutureWarning:<br>
    Conversion of the second argument of issubdtype from `float` to<br>
    `np.floating` is deprecated. In future, it will be treated as<br>
    `np.float64 == np.dtype(float).type`.<br>
 8. from ._conv import register_converters as _register_converters</code><br>
<br>如果你现在尝试运行相同的命令，但在docker命令中添<strong>--runtime=nvidia</strong>参数，你应该看到类似以下的内容：<br>
<br><code class="prettyprint">1. root@jetson:~# echo &quot;python3 -c 'import tensorflow'&quot; | docker run<br>
    --runtime=nvidia -i icetekio/jetson-nano-tensorflow /bin/bash<br>
 2. 2020-05-14 00:12:16.767624: I<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:48]<br>
    Successfully opened dynamic library libcudart.so.10.2<br>
 3. 2020-05-14 00:12:19.386354: I<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:48]<br>
    Successfully opened dynamic library libnvinfer.so.7<br>
 4. 2020-05-14 00:12:19.388700: I<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:48]<br>
    Successfully opened dynamic library libnvinfer_plugin.so.7<br>
 5. /usr/lib/python3/dist-packages/h5py/__init__.py:36: FutureWarning:<br>
    Conversion of the second argument of issubdtype from `float` to<br>
    `np.floating` is deprecated. In future, it will be treated as<br>
    `np.float64 == np.dtype(float).type`.<br>
 6. from ._conv import register_converters as _register_converters</code><br>
<br>nvidia-docker已经配置完成，但是默认情况下并没有启用。要启用docker运行nvidia-docker运行时作为默认值，需要将<strong>"default-runtime":"nvidia"</strong>添加到/etc/docker/daemon.json配置文件中，如下所示：<br>
<br><code class="prettyprint">&#123;<br>
    &quot;runtimes&quot;: &#123;<br>
        &quot;nvidia&quot;: &#123;<br>
            &quot;path&quot;: &quot;nvidia-container-runtime&quot;,<br>
            &quot;runtimeArgs&quot;: []<br>
        &#125;<br>
    &#125;,<br>
    &quot;default-runtime&quot;: &quot;nvidia&quot;<br>
&#125;</code><br>
<br>现在你可以跳过docker run命令中<strong>--runtime=nvidia</strong>参数，GPU将被默认初始化。这样K3s就会用nvidia-docker运行时来使用Docker，让Pod不需要任何特殊配置就能使用GPU。<br>
<br><h2>将Jetson作为K8S节点连接</h2>使用K3sup将Jetson作为Kubernetes节点连接只需要1个命令，然而要想成功连接Jetson和master节点，我们需要能够在没有密码的情况下同时连接到Jetson和master节点，并且在没有密码的情况下做sudo，或者以root用户的身份连接。<br>
<br>如果你需要生成SSH 密钥并复制它们，你需要运行以下命令：<br>
<br><code class="prettyprint">1. ssh-keygen -t rsa -b 4096 -f ~/.ssh/rpi -P &quot;&quot;<br>
 2. ssh-copy-id -i .ssh/rpi user@host</code><br>
<br>默认情况下，Ubuntu安装要求用户在使用sudo命令时输入密码，因此，更简单的方法是用root账户来使用K3sup。要使这个方法有效，需要将你的<strong>~/.ssh/authorized_keys</strong>复制到<strong>/root/.ssh/</strong>目录下。<br>
<br>在连接Jetson之前，我们查看一下想要连接到的集群：<br>
<br><code class="prettyprint">1. upgrade@ZeroOne:~$ kubectl get node -o wide<br>
 2. NAME      STATUS   ROLES    AGE   VERSION        INTERNAL-IP   <br>
    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     <br>
    CONTAINER-RUNTIME<br>
 3. nexus     Ready    master   32d   v1.17.2+k3s1   192.168.0.12  <br>
    &lt;none>        Ubuntu 18.04.4 LTS   4.15.0-96-generic  <br>
    containerd://1.3.3-k3s1<br>
 4. rpi3-32   Ready    &lt;none>   32d   v1.17.2+k3s1   192.168.0.30  <br>
    &lt;none>        Ubuntu 18.04.4 LTS   5.3.0-1022-raspi2  <br>
    containerd://1.3.3-k3s1<br>
 5. rpi3-64   Ready    &lt;none>   32d   v1.17.2+k3s1   192.168.0.32  <br>
    &lt;none>        Ubuntu 18.04.4 LTS   5.3.0-1022-raspi2  <br>
    containerd://1.3.3-k3s1</code><br>
<br>你可能会注意到，master节点是一台IP为<strong>192.168.0.12</strong>的<strong>nexus</strong>主机，它正在运行containerd。默认状态下，k3s会将containerd作为运行时，但这是可以修改的。由于我们设置了nvidia-docker与docker一起运行，我们需要修改containerd。无需担心，将containerd修改为Docker我们仅需传递一个额外的参数到k3sup命令即可。所以，运行以下命令即可连接Jetson到集群：<br>
<br><code class="prettyprint">1. k3sup join --ssh-key ~/.ssh/rpi  --server-ip 192.168.0.12  --ip<br>
    192.168.0.40   --k3s-extra-args '--docker'</code><br>
<br>IP <strong>192.168.0.40</strong>是我的Jetson Nano。正如你所看到的，我们传递了<strong>--k3s-extra-args'--docker'</strong>标志，在安装k3s agent 时，将<strong>--docker</strong>标志传递给它。多亏如此，我们使用的是nvidia-docker设置的docker，而不是containerd。<br>
<br>要检查节点是否正确连接，我们可以运行<strong>kubectl get node -o wide：</strong><br>
<br><code class="prettyprint">1. upgrade@ZeroOne:~$ kubectl get node -o wide<br>
 2. NAME      STATUS   ROLES    AGE   VERSION        INTERNAL-IP   <br>
    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     <br>
    CONTAINER-RUNTIME<br>
 3. nexus     Ready    master   32d   v1.17.2+k3s1   192.168.0.12  <br>
    &lt;none>        Ubuntu 18.04.4 LTS   4.15.0-96-generic  <br>
    containerd://1.3.3-k3s1<br>
 4. rpi3-32   Ready    &lt;none>   32d   v1.17.2+k3s1   192.168.0.30  <br>
    &lt;none>        Ubuntu 18.04.4 LTS   5.3.0-1022-raspi2  <br>
    containerd://1.3.3-k3s1<br>
 5. rpi3-64   Ready    &lt;none>   32d   v1.17.2+k3s1   192.168.0.32  <br>
    &lt;none>        Ubuntu 18.04.4 LTS   5.3.0-1022-raspi2  <br>
    containerd://1.3.3-k3s1<br>
 6. jetson    Ready    &lt;none>   11s   v1.17.2+k3s1   192.168.0.40  <br>
    &lt;none>        Ubuntu 18.04.4 LTS   4.9.140-tegra      <br>
    docker://19.3.6</code><br>
<br><h2>简易验证</h2>我们现在可以使用相同的docker镜像和命令来运行pod，以检查是否会有与本文开头在Jetson Nano上运行docker相同的结果。要做到这一点，我们可以应用这个pod规范：<br>
<br>&#123;&#123;&#123; 1. apiVersion: v1<br>
 2. kind: Pod<br>
 3. metadata:<br>
<ol><li>name: gpu-test</li><li><br>spec:</li><li><br>nodeSelector:</li><li><br>kubernetes.io/hostname: jetson</li><li><br>containers:</li><li><br>image: icetekio/jetson-nano-tensorflow</li><li><br> name: gpu-test</li><li><br> command:<br>
<ul><li></li></ul></li><li>"/bin/bash"<br>
- </li><li>"-c"<br>
- </li><li>"echo 'import tensorflow' | python3"</li><li>restartPolicy: Never&#125;&#125;&#125;</li></ol><br>
<br>等待docker镜像拉取，然后通过运行以下命令查看日志：<br>
<br>&#123;&#123;&#123;1. upgrade@ZeroOne:~$ kubectl logs gpu-test<br>
 2. 2020-05-14 10:01:51.341661: I<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:48]<br>
    Successfully opened dynamic library libcudart.so.10.2<br>
 3. 2020-05-14 10:01:53.996300: I<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:48]<br>
    Successfully opened dynamic library libnvinfer.so.7<br>
 4. 2020-05-14 10:01:53.998563: I<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:48]<br>
    Successfully opened dynamic library libnvinfer_plugin.so.7<br>
 5. /usr/lib/python3/dist-packages/h5py/__init__.py:36: FutureWarning:<br>
    Conversion of the second argument of issubdtype from <code class="prettyprint">float</code> to<br>
    <code class="prettyprint">np.floating</code> is deprecated. In future, it will be treated as<br>
    <code class="prettyprint">np.float64 == np.dtype(float).type</code>.<br>
<ol><li>from ._conv import register_converters as _register_converters&#125;&#125;&#125;</li></ol><br>
<br>如你所见，我们的日志信息与之前在Jetson上运行Docker相似。<br>
<br><h2>运行MNIST训练</h2>我们有一个支持GPU的运行节点，所以现在我们可以测试出机器学习的 "Hello world"，并使用MNIST数据集运行TensorFlow 2模型示例。<br>
<br>要运行一个简单的训练会话，以证明GPU的使用情况，应用下面的manifest：<br>
<br>&#123;&#123;&#123; 1. apiVersion: v1<br>
 2. kind: Pod<br>
 3. metadata:<br>
<ol><li>name: mnist-training</li><li>spec:</li><li><br>nodeSelector:</li><li><br>kubernetes.io/hostname: jetson</li><li><br>initContainers:<br>
<ul><li></li></ul></li><li><br>name: git-clone</li><li><br> image: iceci/utils</li><li><br> command:<br>
    - </li><li>"git"<br>
    - </li><li><br> "clone"</li><li><ul><li>"<<a href="https://github.com/IceCI/example-mnist-training.gi" rel="nofollow" target="_blank">https://github.com/IceCI/example-mnist-training.gi</a>t>"<br>
- </li></ul></li><li><br> "/workspace"</li><li><br> volumeMounts:<br>
    - </li><li><br> mountPath: /workspace</li><li><br> name: workspace</li><li>containers:<br>
- </li><li><br> image: icetekio/jetson-nano-tensorflow</li><li><br> name: mnist</li><li><br> command:<br>
<ul><li></li></ul></li><li>"python3"<br>
    - </li><li><br> "/workspace/mnist.py"</li><li><br> volumeMounts:<br>
    - </li><li><br> mountPath: /workspace</li><li><br> name: workspace</li><li><br> restartPolicy: Never</li><li>volumes:<br>
- </li><li><br> name: workspace</li><li><br> emptyDir: &#123;&#125;&#125;&#125;&#125;</li></ol><br>
<br>从下面的日志中可以看到，GPU正在运行：<br>
<br><code class="prettyprint">1. ...<br>
 2. 2020-05-14 11:30:02.846289: I<br>
    tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding<br>
    visible gpu devices: 0<br>
 3. 2020-05-14 11:30:02.846434: I<br>
    tensorflow/stream_executor/platform/default/dso_loader.cc:48]<br>
    Successfully opened dynamic library libcudart.so.10.2<br>
 4. ....</code><br>
<br>如果你在节点上，你可以通过运行tegrastats命令来测试CPU和GPU的使用情况：<br>
<br><code class="prettyprint">1. upgrade@jetson:~$ tegrastats --interval 5000<br>
 2. RAM 2462/3964MB (lfb 2x4MB) SWAP 362/1982MB (cached 6MB) CPU<br>
    [52%@1479,41%@1479,43%@1479,34%@1479] EMC_FREQ 0% GR3D_FREQ 9%<br>
    PLL@23.5C CPU@26C PMIC@100C GPU@24C AO@28.5C thermal@25C POM_5V_IN<br>
    3410/3410 POM_5V_GPU 451/451 POM_5V_CPU 1355/1355<br>
 3. RAM 2462/3964MB (lfb 2x4MB) SWAP 362/1982MB (cached 6MB) CPU<br>
    [53%@1479,42%@1479,45%@1479,35%@1479] EMC_FREQ 0% GR3D_FREQ 9%<br>
    PLL@23.5C CPU@26C PMIC@100C GPU@24C AO@28.5C thermal@24.75C<br>
    POM_5V_IN 3410/3410 POM_5V_GPU 451/451 POM_5V_CPU 1353/1354<br>
 4. RAM 2461/3964MB (lfb 2x4MB) SWAP 362/1982MB (cached 6MB) CPU<br>
    [52%@1479,38%@1479,43%@1479,33%@1479] EMC_FREQ 0% GR3D_FREQ 10%<br>
    PLL@24C CPU@26C PMIC@100C GPU@24C AO@29C thermal@25.25C POM_5V_IN<br>
    3410/3410 POM_5V_GPU 493/465 POM_5V_CPU 1314/1340</code><br>
<br><h2>总  结</h2>如你所见，将Jetson Nano连接到Kubernetes集群是一个非常简单的过程。只需几分钟，你就能利用Kubernetes来运行机器学习工作负载——同时也能利用NVIDIA袖珍GPU的强大功能。你将能够在Kubernetes上运行任何为Jetson Nano设计的GPU容器，这可以简化你的开发和测试。<br>
<blockquote><br>作者： Jakub Czapliński，Icetek编辑<br>
   原文链接：<br>
  <a href="https://medium.com/icetek/how-to-connect-jetson-nano-to-kubernetes-using-k3s-and-k3sup-c715cf2bf212"></a><a href="https://medium.com/icetek/how-to-connect-jetson-nano-to-kubernetes-using-k3s-and-k3sup-c715cf2bf212" rel="nofollow" target="_blank">https://medium.com/icetek/how- ... bf212</a></blockquote>
                                
                                                              
</div>
            