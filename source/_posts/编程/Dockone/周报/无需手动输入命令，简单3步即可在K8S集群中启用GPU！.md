
---
title: '无需手动输入命令，简单3步即可在K8S集群中启用GPU！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/2021071222591960.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
author: Dockone
comments: false
date: 2021-07-16 00:22:00
thumbnail: 'https://img-blog.csdnimg.cn/2021071222591960.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
---

<div>   
<br>随着全球各大企业开始广泛采用Kubernetes，我们看到Kubernetes正在向新的阶段发展。一方面，Kubernetes被边缘的工作负载所采用并提供超越数据中心的价值。另一方面，Kubernetes正在驱动机器学习（ML）和高质量、高速的数据分析性能的发展。<br>
<br>我们现在所了解到的将Kubernetes应用于机器学习的案例主要源于Kubernetes 1.10中一个的功能，当时图形处理单元（GPUs）成为一个可调度的资源——现在这一功能处于beta版本。单独来看，这两个都是Kubernetes中令人兴奋的发展。更令人兴奋的是，可以使用Kubernetes在数据中心和边缘采用GPU。在数据中心，GPU是一种构建ML库的方式。那些训练过的库将被迁移到边缘Kubernetes集群作为机器学习的推理工具，在尽可能靠近数据收集的地方提供数据分析。<br>
<br>在早些时候，Kubernetes还是为分布式应用程序提供一个CPU和RAM资源的池。如果我们有CPU和RAM池，为什么不能有一个GPU池呢？这当然毫无问题，但不是所有的server都有GPU。所以，如何让我们的server在Kubernetes中可以装配GPU呢？<br>
<br>在本文中，我将阐述在Kubernetes集群中使用GPU的简单方法。在未来的文章中，我们还将GPU推向至边缘并向你展示如何完成这一步骤。为了真正地简化步骤，我将用Rancher UI来操作启用GPU的过程。Rancher UI只是Rancher RESTful APIs的一个客户端。你可以在GitOps、DevOps和其他自动化解决方案中使用其他API的客户端，比如Golang、Python和Terraform。不过，我们不会在此文中深入探讨这些。<br>
<br>本质上看，步骤十分简单：<br>
<ul><li>为Kubernetes集群构建基础架构</li><li>安装Kubernetes</li><li>从Helm中安装gpu-operator</li></ul><br>
<br><h2>使用Rancher和可用的GPU资源启动和运行</h2>Rancher是一个多集群管理解决方案并且是上述步骤的粘合剂。你可以在NVIDIA的博客中找到一个简化GPU管理的纯NVIDIA解决方案，以及一些关于gpu-operator与构建没有operator的GPU驱动堆栈有何区别的重要信息。<br>
<br>（<a href="https://developer.nvidia.com/blog/nvidia-gpu-operator-simplifying-gpu-management-in-kubernetes/"></a><a href="https://developer.nvidia.com/blog/nvidia-gpu-operator-simplifying-gpu-management-in-kubernetes/" rel="nofollow" target="_blank">https://developer.nvidia.com/b ... etes/</a>）<br>
<br><strong>前期准备</strong><br>
<br>以下是在Rancher中启动和运行GPU所需的材料清单（BOM）：<br>
<ol><li>Rancher</li><li>GPU Operator（<a href="https://nvidia.github.io/gpu-operator/" rel="nofollow" target="_blank">https://nvidia.github.io/gpu-operator/</a>）</li><li>基础架构——我们将在AWS上使用GPU节点</li></ol><br>
<br>在官方文档中，我们有专门的章节阐述如何高可用安装Rancher，所以我们假设你已经将Rancher安装完毕：<br>
<br><a href="https://docs.rancher.cn/docs/rancher2/installation/k8s-install/_index/"></a><a href="https://docs.rancher.cn/docs/rancher2/installation/k8s-install/_index/" rel="nofollow" target="_blank">https://docs.rancher.cn/docs/r ... ndex/</a><br>
<br><strong>流程步骤</strong><br>
<br><strong>使用GPUs安装Kubernetes集群</strong><br>
<br>Rancher安装之后，我们首先将构建和配置一个Kubernetes集群（你可以使用任何带有NVIDIA GPU的集群）。<br>
<br>使用Global上下文，我们选择Add Cluster<br>
<br><img src="https://img-blog.csdnimg.cn/2021071222591960.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>并在“来自云服务商提供的主机”部分，选择Amazon EC2。<br>
<br><img src="https://img-blog.csdnimg.cn/20210712225927688.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>我们是通过节点驱动来实现的—— 一组预配置的基础设施模板，其中一些模板有GPU资源。<br>
<br><img src="https://img-blog.csdnimg.cn/2021071222593625.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>注意到这里有3个节点池：一个是为master准备的，一个是为标准的worker节点准备的，另一个是为带GPU的worker准备的。GPU的模板基于p3.2xlarge机器类型，使用Ubuntu 18.04亚马逊机器镜像或AMI（ami-0ac80df6eff0e70b5）。当然，这些选择是根据每个基础设施提供商和企业需求而变化的。另外，我们将 “Add Cluster”表单中的Kubernetes选项设置为默认值。<br>
<br><strong>设置GPU Operator</strong><br>
<br>现在，我们将使用GPU Operator库（<a href="https://nvidia.github.io/gpu-operator"></a><a href="https://nvidia.github.io/gpu-operator" rel="nofollow" target="_blank">https://nvidia.github.io/gpu-operator</a>）在Rancher中设置一个catalog。（也有其他的解决方案可以暴露GPU，包括使用Linux for Tegra [L4T] Linux发行版或设备插件）在撰写本文时，GPU Operator已经通过NVIDIA Tesla Driver 440进行了测试和验证。<br>
<br>使用Rancher Global上下文菜单，我们选择要安装到的集群：<br>
<br><img src="https://img-blog.csdnimg.cn/20210712225953792.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>然后使用Tools菜单来查看catalog列表。<br>
<br><img src="https://img-blog.csdnimg.cn/20210712230357738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>点击Add Catalog按钮并且给其命名，然后添加url：<a href="https://nvidia.github.io/gpu-operator"></a><a href="https://nvidia.github.io/gpu-operator" rel="nofollow" target="_blank">https://nvidia.github.io/gpu-operator</a><br>
<br>我们选择了Helm v3和集群范围。我们点击Create以添加Catalog到Rancher。当使用自动化时，我们可以将这一步作为集群构建的一部分。根据企业策略，我们可以添加这个Catalog到每个集群中，即使它还没有GPU节点或节点池。这一步为我们提供了访问GPU Operator chart的机会，我们接下来将安装它。<br>
<br><img src="https://img-blog.csdnimg.cn/20210712230415864.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>现在我们想要使用左上角的Rancher上下文菜单以进入集群的“System”项目，我们在这里添加了GPU Operator功能。<br>
<br><img src="https://img-blog.csdnimg.cn/20210712230423838.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>在System项目中，选择Apps：<br>
<br><img src="https://img-blog.csdnimg.cn/20210712230431958.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>然后点击右上方的Launch按钮。<br>
<br><img src="https://img-blog.csdnimg.cn/20210712230440219.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>我们可以搜索“nvidia”或者向下滚动到我们刚刚创建的catalog。<br>
<br><img src="https://img-blog.csdnimg.cn/2021071223045036.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>点击gpu-operator app，然后在页面底部点击Launch。<br>
<br><img src="https://img-blog.csdnimg.cn/20210712230532997.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>在这种情况下，所有的默认值都应该没问题。同样，我们可以通过Rancher APIs将这一步骤添加到自动化中。<br>
<br><strong>利用GPU</strong><br>
<br>既然GPU已经可以访问，我们现在可以部署一个GPU-capable 工作负载。同时，我们可以通过在Rancher中查看Cluster -> Nodes的页面验证安装是否成功。我们看到GPU Operator已经安装了Node Feature Discovery (NFD)并且给我们的节点贴上了GPU使用的标签。<br>
<br><img src="https://img-blog.csdnimg.cn/20210712230546176.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><h2>总  结</h2>之所以能够采用如此简单的方法就能够让Kubernetes与GPU一起运行，离不开这3个重要部分：<br>
<ol><li>NVIDIA的GPU Operator</li><li>来自Kubernetes同名SIG的Node Feature Discovery（NFD）。</li></ol><br>
<br>Rancher的集群部署和catalog app集成<br>
<br>欢迎您根据本教程动手尝试，也请继续保持关注，在之后的教程中我们会尝试将GPU引用至边缘。
                                
                                                              
</div>
            