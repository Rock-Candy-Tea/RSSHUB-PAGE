
---
title: '狗尾续貂之Neutron网络部署架构的第N+1种方式'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc11e79caf34d739fdeb18f72787894~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 19:09:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc11e79caf34d739fdeb18f72787894~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><strong>前言</strong></h2>
<p>在前面的系列中，"牛"人总结了不同服务器配置、网络配置情况下Neutron的部署方式。这些年也偶尔兼职过部署运维的工作，对个中滋味深有体会，但是读过之后依然有醍醐灌顶，耳目一新的感觉，一句话，简单直接。</p>
<p>理想是美好的，现实是骨感的。去某客户现场做POC时，经过前期的沟通，现场的条件还不错，机器随便用，独立的二层交换机随便用，感觉不错呦。但，但是，唯一的三层网络是办公网络，DHCP方式获得，不可改！瞬间感觉血压有点高，懵了，好像跟想象的不一样啊，说好的提供连续的一段可访问地址呢？（再次证明，不到最后实施部署那一刻，神马都是浮云）没困难上，有困难更要上，作为焱融的男人，工作还要继续，不能说不的，让我们缓口气，理一理思绪。</p>
<p>其实事后想一想，这个问题的变种还是遇到过的，只不过大脑短路了，后面再提及。</p>
<h2 data-id="heading-1"><strong>分而治之</strong></h2>
<p>无图无真相，我们看看实际情况，当然真相不仅如此，还有路由、网关和远方。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc11e79caf34d739fdeb18f72787894~tplv-k3u1fbpfcp-watermark.image" alt="111.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们都知道，Neutron里面如果虚拟机需要外网流量进出，至少需要一个external网络，在这个网络中我们需要若干的IP地址，并且Neutron自行维护DHCP，当然也可以不启用DHCP，转而手动指定IP。但就上面的实际情况，我们既不能长久的获得连续的一段IP地址（可能晚上能ping出来一段，白天又自动分出去了），又不能在我们的Neutron网络内启动另外一个external的DHCP。混社区的，需要学会leverage，有问题第一时间要去抱大腿，到社区去找Neutron是否可以为external网络利用已经存在的DHCP，未果，只发现有提问题的，没有答的，哈哈。</p>
<p>好在现场硬件条件还不错，网口足够，交换机够用。那么我们就分而治之，不是没有连续的网络地址吗，但是有独立交换机啊，那我们就自己创造一个连续的IP地址池，只要与现有的不冲突即可，例如172.16.10.0/24, 这样安装OpenStack的时候，配置的br-ex选择该网段即可（其他网络不再详细描述，例如管理网也可以用其他的独立的私有网络，从现有的DHCP隔离出来）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28ded27e18e94bd68c150adbcf370146~tplv-k3u1fbpfcp-watermark.image" alt="222.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>OpenStack环境部署出来了，但是虚拟机还是隔离的。在当前拓扑下，办公网络和我们OpenStack的上联网络是不同的网段，两个交换机还不能直接连接，否则DHCP就乱了，那么就需要一个路由器做跨网段的通信。然而，答案肯定是没有了，:(。</p>
<p>好吧，没有什么是一台Linux操作系统不能搞定的，实在不够，就两台。我们可以用一台服务器，通过对操作系统做一些iptables的配置，达到路由器的目的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b143be8a5794ec9b11fff97228ad184~tplv-k3u1fbpfcp-watermark.image" alt="333.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>距离成功只有一步之遥了，其他台式机只要能路由到172.16.10.0/24的网络就能够访问到虚拟机了，如果可以修改DHCP Server，那么可以通过配置下发，将 172.16.10.0/24的路由设置为之前的那个Linux路由服务器，通过它进行转发。或者直接在办公网络台式机本地手动增加一条路由也能够完成同样的效果。</p>
<h2 data-id="heading-2"><strong>总结</strong></h2>
<p>文中试图在受限的情况下利用一些其他的方式来解决实际的问题，其实想来，这样的模式也是有迹可循的。例如在一个典型的机房中部署了私有云，在机房外需要访问虚拟机时，就有些类似，只不过那时需要利用防火墙做NAT等。受限于笔者在网络方面的有限了解，行文以及技术方面难免有遗漏，欢迎指正。</p></div>  
</div>
            