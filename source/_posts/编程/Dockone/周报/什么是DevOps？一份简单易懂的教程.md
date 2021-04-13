
---
title: '什么是DevOps？一份简单易懂的教程'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/f0ce732cd550ab16b082f35b27693242.png'
author: Dockone
comments: false
date: 2021-04-13 12:10:45
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/f0ce732cd550ab16b082f35b27693242.png'
---

<div>   
<br>【编者的话】DevOps是对已建立的IT流程的简化或者自动化。这里有一个简短的教程来帮助你理解和开始使用DevOps。<br>
<br>DevOps……CI/CD……Docker……Kubernetes……我敢肯定你在过去的一年里经常听人说这些词。好像全世界都在谈论这些技术，以至于你觉得即将到达NoOps阶段。<br>
<br>别担心，在工具和各种最佳实践的浩瀚海洋中感到迷失是正常的。是时候让我们来分析一下DevOps到底是什么了。<br>
<br>这篇文章的目的，就是为你建立一个坚实的基础。所以让我们从一个明显的问题开始。<br>
<h3>什么是DevOps？</h3><strong><a href="https://v.qq.com/x/page/d323986p1g4.html">视频</a></strong><br>
<br>DevOps是对已建立的 IT流程的简化或者自动化。<br>
<br>我见过很多人开始使用DevOps，最终却都迷失了。这似乎是一种魔咒。<br>
<br>通常从一段视频开始，讲述一家高科技初创公司是如何自动化整个产品发布流程的。一旦所有测试通过，部署就会自动进行。发生故障时，可以自动回滚。同时进行A/B测试，提高了客户参与度。<br>
<br>老实说吧，我们都想实现这样的DevOps。我们都厌倦了像坐过山车一样的发布新版本。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/f0ce732cd550ab16b082f35b27693242.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/f0ce732cd550ab16b082f35b27693242.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
不幸的是，DevOps不是这样工作的。DevOps并不是一根魔法棒，它能在一瞬间解决你所有的问题。<br>
<br>相反，这是一个系统性的工程，你应该使用合适的工具和技术来完成不同的任务。<br>
<h4>所有的一切都是为了流程</h4>具体是什么流程并不重要，只要它可以简化应用程序的部署或者自动化测试，让你的生活更轻松，那这就是DevOps的全部内容。<br>
<br>事实上，如果你的流程不能手动完成（针对较小的流程），你可能需要重新定义你的流程。<br>
<br>好了，让我们举一个真实的例子来更好地理解“流程”。<br>
<h3>一个真实的DevOps例子</h3>我们举一个，在云虚拟机上部署Nodejs应用程序的例子。<br>
<br>我们的流程如下：<br>
<ul><li>从源代码开始（Start with the source code）：只要我们能访问源代码，我们就可以在任何地方运行我们的代码。</li><li>构建制品（Build an Artifact）：然后我们打包源代码来构建一个制品。如果是Java语言，那么JAR文件就是我们的制品。但在我们Nodejs的例子中，源代码本身就是要发布的制品。</li><li>发布到制品仓库（Publish to an Artifact Repository）：接下来，我们将制品推送到制品仓库。然后我们的虚拟机就可以从制品仓库中提取制品。我们可以直接使用Github作为我们的制品仓库，因为我们的源代码即制品。</li><li>拉取并运行应用程序（Pull and run your app）：最后，我们将制品拉取到虚拟机上，并通过指令<code class="prettyprint">npm start</code>来启动Nodejs进程。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/96ad5a1e3040fcf1c0364c14e09c302d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/96ad5a1e3040fcf1c0364c14e09c302d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>我们的第一个DevOps项目</h3>我们不会在这里做任何花哨的事情。最简单的自动化的方式就是写一个shell脚本，按顺序顺序运行所有命令。恭喜你完成了我们的第一个DevOps项目！<br>
<br>我知道shell脚本听起来太简单了，不值得认真对待。我怀疑你曾经也写过这样的脚本。但相信我，这就是DevOps！<br>
<br>别担心，我们马上就可以看到那些花哨的东西了。但重要的是要理解DevOps就是这样工作的。<br>
<h3>“可重复”的重要性</h3>让我问你一个问题。你喜欢以下哪一个？<br>
<ul><li>一个在60%的时间内，能正常工作的自动化部署管道；</li><li>一个无聊的shell脚本，但是每次执行都能完成任务。</li></ul><br>
<br>如果你曾经在半夜处理过生产故障，那么你将选择shell脚本。<br>
<br>原因很简单。<strong>可靠性远比自动化程度更重要。</strong>换句话说，<strong>一个DevOps流程必须能够在每次运行时产生一致的结果。</strong><br>
<h4>使我们的过程可重复</h4>以我们的shell脚本为例。目前，我们的shell脚本依赖于安装在虚拟机上的Node.js。<br>
<br>如果没有在虚拟机上安装Node.js，会发生什么？一个错误的Node.js版本足以使我们的应用程序不能正常运行。当我们需要在虚拟机上安装多种语言运行时时，情况只会变得更糟。<br>
<br>一个简单的解决方案是将Node.js运行时与我们的源代码一起归档到zip文件中。然后可以将zip文件发送到虚拟机。这样，虚拟机就可以使用zip文件中的本地Node.js运行时来运行我们的应用程序。<br>
<br>幸运的是，有一种工具可以让我们的生活更轻松。<br>
<h3>Docker和容器</h3>如果你对Docker不熟悉，可以将Docker看作是一种将你的制品（artifact）及其所依赖的操作系统以及Node.js，一起打包进容器镜像中的方法。<br>
<br>使用容器，我们可以在安装了Docker的虚拟机上部署任何应用程序。<br>
<br>使用Docker，我们的流程将如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/824b0cbc82bb3a9dda1b3b2305ae387f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/824b0cbc82bb3a9dda1b3b2305ae387f.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
容器不仅仅能做到这些，但这却是容器能如此流行的重要原因之一。<br>
<h4>Docker  Vs.容器</h4>让我澄清一下，Docker和容器并不是同一个东西。<br>
<br><strong>Docker是一组实用工具，用于构建和运送容器镜像，以及使用容器运行时（如containerd）来运行容器。</strong><br>
<br>考虑到最近发生的事件，许多人对Docker的未来感到担忧。<br>
<br>重要的是要明白，Docker不会立马消失，在构建和运送容器镜像领域，将继续发挥重要作用。<br>
<h3>认真对待DevOps</h3>我们已经取得了一些重大进展。希望我们能理解Docker是如何融入DevOps流程中的。<br>
<br>是时候把事情推向下一个层次了。<br>
<h4>基于事件的触发部署</h4>我们的脚本看起来很稳定，但仍然是手动触发的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/12470d2b2f8357305efffbe6f585f3a1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/12470d2b2f8357305efffbe6f585f3a1.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果我们能，当有人往GitHub上推送代码时自动触发这个脚本，那不是更好吗？换句话说，我们希望基于事件的触发部署。<br>
<br>GitHub可以在一组特定的事件上调用webhook。为了实现这一点，我们需要创建一个简单的HTTP服务器，每当服务器接收到请求时，它就会执行shell脚本。我们可以将GitHub配置为，当发生Push事件时，触发HTTP请求。我们将这个过程称之为持续部署（Continuous Deployment）。<br>
<br>我们的新流程如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/dbbee2a98569e563fee77ed7b0d9fe96.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/dbbee2a98569e563fee77ed7b0d9fe96.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
恭喜你，你刚刚成功创建了一个<strong>CD pipeline</strong>。<br>
<br><strong>持续部署是一种软件，负责将应用程序从GitHub之类的东西一直带到最终部署的目标环境中。</strong><br>
<br>这基本上就是你经常听到的CI/CD。当人们谈论像Jenkins和CircleCI这样的工具时，他们通常指的是CI/CD。<br>
<h3>DevOps模式**</h3>我想你已经找到了一个模式。我们从一个流程开始，找到一个我们不满意的部分，然后引入一些软件来简化或自动化它。<br>
<br>用代码的方式来操作流程，这就是DevOps。<br>
<h3>引入容器编排</h3>最后让我们做一个小小的改进。到目前为止，我们一直将应用程序部署在单个虚拟机上。如果我们想将应用程序部署到多个虚拟机或者节点上呢？<br>
<br>实现这一点的最简单方法是让CD Server通过SSH连接到所有虚拟机，并将容器部署到每个虚拟机中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/d26778d9d2c93a86be0857413167c1a7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/d26778d9d2c93a86be0857413167c1a7.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
使用这种方式时，每当虚拟机的数量发生变化时，我们就需要更改脚本。但在真实世界中，我们希望我们的应用程序是可以自动扩缩容的。<br>
<br>更好的方法是创建另一个HTTP服务器来跟踪虚拟机数量的变化。我们可以称这个服务器为“飞行员（Pilot）”。<br>
<br>此服务器将负责对集群中的各个虚拟机执行健康检查，以维护活动的虚拟机列表。它甚至可以与云供应商进行通信，使事情变得更加健壮。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/4a58c055e0860b831561ebd96efb2a33.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/4a58c055e0860b831561ebd96efb2a33.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Pilot还将公开一个HTTP端点，以接受要生成的容器的详细信息。然后，它可以与各个虚拟机通信以完成任务。<br>
<br>现在，我们的CD Server可以简单地请求Pilot，而不是单独与每个虚拟机通信。<br>
<br>我们的新流程如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/93888b256ca86f89f55ad9f4fa1d19cd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/93888b256ca86f89f55ad9f4fa1d19cd.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们将Pilot称为容器编排器。其实这就是Kubernetes！你刚刚设计了一个迷你版的Kubernetes！<br>
<br>另外，Kubernetes在希腊语中就是Pilot的意思。这是不是巧合？<br>
<h3>从哪里开始？</h3>我们一起讨论了不少工具。这是我的最后一点。有没有想过为什么DevOps的空间如此分散？<br>
<br>如果你仔细想想，有这么多的工具，让你很难决定：什么是正确的选择，或者你应该从哪里开始？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/cea338dda2b01868b8e6a5bc5b5050dd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/cea338dda2b01868b8e6a5bc5b5050dd.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
每个组织都有自己的做事方式和流程，因而他们使用的工具也不同。你的工作不是找出哪种工具是最好的。你的工作就是找出最适合你的流程。一旦你明白了这一点，这些工具就只需要谷歌搜索了。<br>
<br>所以现在你知道从哪里开始了。不是工具。<strong>而是从了解你的公司和团队如何做事开始。</strong><br>
<br><strong>原文链接：<a href="https://dzone.com/articles/what-is-devops-a-devops-tutorial-in-plain-english#">What is DevOps? A DevOps Tutorial in Plain English</a>  （翻译：钟涛）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            