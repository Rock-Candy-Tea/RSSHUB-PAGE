
---
title: '基于Kubernetes的PaaS平台中细力度控制Pod方案的实现'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/322e0008095ca24baad59afc21716e52.png'
author: Dockone
comments: false
date: 2021-09-16 08:10:59
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/322e0008095ca24baad59afc21716e52.png'
---

<div>   
<br>之前的博客中介绍了<a href="http://dockone.io/article/2434589">细力度控制Pod的方案</a>，我们可以通过增加自定义资源的方式来针对性的调整Pod数目，但是这个一个基本的原语。如果将其作为平台的功能提供给用户呢？这篇博客将会介绍一下我们如何利用这个特性来精准的控制机器部署的Pod数目。<br>
<h3>简单回顾</h3>我们的PaaS平台中允许用户提供机器，由我们接入Kubernetes，而这部分用户自己的机器，他们希望这些机器的性能利用率能达到很优。无论怎么依靠程序的分配策略，总是不如自己手动调整的效果最佳，因此才会需要平台提供能够确定在每台机器部署确定Pod数目的功能。<br>
<br>上篇博客中我已经给出了可行的方案，具体的实现是增加新的资源限制。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/322e0008095ca24baad59afc21716e52.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/322e0008095ca24baad59afc21716e52.png" class="img-polaroid" title="01.png" alt="01.png" referrerpolicy="no-referrer"></a>
</div>
<br>
书写控制策略时配合CPU以及mem来使用：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/1d45a6538efd2ee0af25cfcf87367eea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/1d45a6538efd2ee0af25cfcf87367eea.png" class="img-polaroid" title="02.png" alt="02.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>系统设计与实现</h3><h4>用户交互部分</h4>在调研了实现方案之后，我就实现了一个可以修改自定义资源配置的功能，但是给用户之后，反馈是十分难用，修改起来工作量很大，几乎完全不可用。在组内讨论了方案之后，我们决定，对于每一个应用，如果用户想要指定每台机器部署多少个Pod，那么，最简化的配置应该是这样的：<br>
<pre class="prettyprint">应用1配置：<br>
机器1: 3,  <br>
机器2: 1,  <br>
机器3: 4,  <br>
</pre><br>
用户不应该关心底层的实现细节，也不用去管什么自定义的资源限制，只要给定node名称，就可以实现控制，这才是用户真正想要的功能。<br>
<h4>实现部分</h4>增加了自定义资源之后，程序部署时需要增加一步声明每台机器的资源数目，下面的代码就是声明机器的自定义资源。<br>
<pre class="prettyprint">def k8s_update_capacity(node, key, value=None):<br>
k8s_core_v1 = client.CoreV1Api()<br>
body = &#123;<br>
    "metadata": &#123;<br>
        'name': node,<br>
    &#125;,<br>
    "status": &#123;<br>
        "capacity": &#123;<br>
            key: value,<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
# 调用patch_node_status<br>
succ, err = apply_by_api(k8s_core_v1, 'node_status', config=body, action='http://weekly.dockone.io/patch')<br>
return succ, err<br>
</pre><br>
比如我们<code class="prettyprint">机器1</code>需要配置3个Pod，那么<code class="prettyprint">k8s_update_capacity('机器1', 'NS名称-app名称-版本名称', 3)</code>，在创建deployments时，将对应的资源请求设置为1，就可以实现在<code class="prettyprint">机器1</code>中部署3个Pod，当然，你需要针对指定的所有机器都做一样的操作。<br>
<h4>细节部分</h4>需要注意的是，我们的平台支持两种类型的发布，一种是滚动更新，另一种是版本更新，我简单描述下两者有什么区别：<br>
<ul><li>滚动更新：没有版本的概念，更新时，旧的Pod会被逐步删除，新的Pod逐步产生</li><li>版本更新：更新时，会创建一份新版本的Pod，然后用户可以选择是否丢弃或是上线这个新版本</li></ul><br>
<br>对于我们的实现中，使用版本更新的应用，资源标签就应该是<code class="prettyprint">NS-app_name-version_id</code>，对于滚动更新的应用，资源标签应该是<code class="prettyprint">NS-app_name</code>。<br>
<br>为什么滚动更新的应用拥有自己的版本号，但是不能加在标签中使用呢？<br>
<br>答：<br>
<ol><li>我们PaaS平台在设计之初，就是只有版本更新功能。结合了Kubernetes之后增加了滚动更新的功能，因此，即使是使用滚动更新的应用，依然是有版本号的，只是没给Kubernetes看到。</li><li>这个涉及到我们的资源使用情况，我们应用占用的资源很多。例如一台机器中，运行4个Pod已经是极限了，我们需要滚动更新策略，删除几个再新建几个，始终维持最大的Pod数目是4，否则可能会造成资源使用过度（报警或是机器挂掉）。如果对于这种应用使用了携带版本号的标签，也就是说，同一时刻，有可能存在一台机器上有两个标签<code class="prettyprint">NS-app_name-旧版本</code>，<code class="prettyprint">NS-app_name-新版本</code>，这样，很可能会在更新应用时机器中新旧版本的Pod数目加起来超过4，因此，滚动更新的应用，自定义资源一定不能携带版本号。</li></ol><br>
<br>这两种更新的方式标签名也就决定了我们在更新自定义资源时，需要采取不同的策略：<br>
<br>对于版本更新的应用：<br>
<br>部署时：我们需要给待部署的的机器增加自定义资源配置，因为携带了版本号，所以新版本一定能部署到正确的问题；更新结束后下线旧版本时需要删除旧版号本对应的资源设置。<br>
<br>对于滚动更新的应用：<br>
<br>部署时：我们需要更新所有可能会部署到的机器资源配置，因为用户可能此次更新修改了部署机器，例如，原有的host1部署了3个Pod，部署新的时指定host1不再部署应用，那么就必须在部署前就将host1上面的自定义资源删除，否则没有版本号的限制，Pod依然有可能部署到host1，更新结束后不需要进行其他处理。<br>
<h4>具体效果</h4>别的我也不说了，同事一句话表明了效果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/6c095e48afd79bffb2b8736bb0e73583.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/6c095e48afd79bffb2b8736bb0e73583.png" class="img-polaroid" title="03.png" alt="03.png" referrerpolicy="no-referrer"></a>
</div>
<br>
目前该功能已经稳定上线运行了2个月，程序按照预想行为进行。<br>
<h3>遇到的问题</h3><h4>扩缩容</h4>使用了自定义资源限制之后，一个比较麻烦的问题是扩缩容，原有的扩缩容可以简单的修改replica实现，但是现在，需要同步更新一下机器中对应的资源数目。<br>
<br>扩容可以简单的同步更新机器资源配置，然后修改replica数量来做到，但是缩容是不行的，具体的表现为，如果你调低了某台机器的自定义资源，然后减少replica数目时，Pod的删除不一定会出现在对应的机器，很可能误删其他机器的Pod，只有重新部署可以缩容。<br>
<br>具体的原因需要去看replicaset的代码，我下一篇博客会介绍下Kubernetes缩容的策略，顺便也能写写怎么调试control-manager的代码。<br>
<h4>maxunavailable的设置</h4>主要针对滚动更新的应用，当我们只有2个Pod，而maxunavailable为25%时，此时，只能容忍1/4容器不可用，因此，原有的2个Pod都不会被删除，而新的Pod也无法被创建，会出现死锁，具体的解决方案就是用户配置时确保<code class="prettyprint">maxunavailable * replica > 1</code>。<br>
<h3>总结</h3>这个细力度控制功能的实现，给我的最大感受就是，调研了解决方案之后，需要针对用户的需求，提供真正能用的上的功能，而不是草草实现（既花了时间，用户也用不上）。<br>
<br>另外就是针对不同的部署方案，需要考虑这种基础功能的实现策略，上面的实现中，我省略了cronjob以及job的实现，希望读者需要实现的时候自己考虑下，应该比较简单。<br>
<br>原文链接：<a href="https://corvo.myseu.cn/2021/04/30/2021-04-" rel="nofollow" target="_blank">https://corvo.myseu.cn/2021/04/30/2021-04-30-</a>基于kubernetes的PaaS平台中细力度控制pod/，作者：corvofeng
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            