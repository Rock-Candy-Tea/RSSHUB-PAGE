
---
title: '既然 BGP 的前提是网络层是通的，那还需要 BGP 做什么用呢？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic3.zhimg.com/v2-0015463312f4f324f84cb4ed9d134853_1440w.jpg?source=b1748391'
author: 知乎
comments: false
date: Mon, 28 Mar 2022 15:15:22 GMT
thumbnail: 'https://pic3.zhimg.com/v2-0015463312f4f324f84cb4ed9d134853_1440w.jpg?source=b1748391'
---

<div>   
北极的回答<br><br><p data-pid="5iF2UPsR">大概十五年前，在福建某网络公司做过路由协议相关的东西，主要就是OSPF和BGP，我觉得目前的回答里，没有解释清楚一件事：设计BGP路由协议的目的是什么？</p><p data-pid="CySensJX">BGP主要用于AS（自治域）之间交换规模比较大的路由表，AS与AS之间相对独立。</p><p data-pid="rgM8pk04">划重点：<b>相对独立</b>、<b>大量路由</b></p><p data-pid="YWOcW638">1. 相对独立的<b>BGP协议是去中心化</b>的。</p><p data-pid="_pBAjP8v">因为BGP交换的数据是AS之间的路由表，AS通常都是一个国家或者一个大型的运营商，AS之间的地位是对等的。一个AS是否要接入到另外一个AS，不需要更高层次的网络管理者的授权。</p><p data-pid="400KC2Yi">而OSPF/ISIS就不行，OSPF/ISIS是中心化的，<b>OSPF需要area0交换数据，ISIS需要骨干区</b>，这些都是中心化的配置，如果国际互联网用OSPF/ISIS，那么就意味着很多数据流量就不得不通过某个中心区域，如果中心区域故障，那么全球互联网就瘫痪了。</p><p data-pid="yoyNZ1Mi">同时，<b>OSPF和ISIS在一个area里都需要一个核心路由器</b>，OSPF叫DR，ISIS叫DIS，尤其是在一个广播网络，DR/DIS非常重要，他们负责通告给其它路由器area里的路由表。有了核心路由器，OSPF/ISIS才能计算出当前arae的拓扑结构。</p><p data-pid="xq_kEZw3">但BGP不行，如果BGP里有类似DR/DIS的角色，那么这个网络就不再是去中心化的了，DR/DIS的选举和变化会导致网络波动，对于BGP这种拥有大规模路由表（上万条）的协议来说，这种波动的影响会非常巨大。</p><p data-pid="HKt0SOCY">去中心化意味着BGP的每个路由器，只能自己算自己的路由表，如果BGP也负责计算到peer端的路由，那么每个BGP路由器计算出来的结果是没办法统一的（没有DR/DIS），所以BGP为了去中心化，放弃了计算到peer路由的过程，把这个工作交给了IGP来实现。</p><p data-pid="__bG32Gg"><b>题主的疑问，用去中心化就可以解释了。</b></p><p data-pid="KG0kq6cl">2. <b>IGP协议报文开销太大</b></p><p data-pid="6gE2wXH_">BGP的报文格式中，是以属性为单位进行通告的，属性+路由条目*N的这种格式。</p><p data-pid="rsbS-J4I">OSPF的LSA和ISIS的LSP都是带有一定链接状态的数据，格式相当于（路由条目+属性）*N的格式，如果路由表数量巨大，那么OSPF/ISIS需要非常多的通信才能完成路由交换。如果是外部路由，那么为了描述一条路由信息，OSPF/ISIS需要更长的报文。同时OSPF/ISIS，<b>都存在老化时间</b>，需要周期性的刷新，BGP不需要。</p><p data-pid="Uu5qzVXk">我曾经在十几年前，抓过某高校内部的OSPF路由表，就有500多百条，而一个国家级别的网络，路由表的规模可能是上万条的，全球互联网的路由表可能是几十万甚至上百万条的，这种情况下，使用OSPF/ISIS的话，性能就不太好了。</p><p data-pid="BFLwN1Bo">3. <b>BGP不关注网络内部的可达性</b></p><p data-pid="nbC5tQQ3">这种设计主要是为了“过境流量”。举例：中国到美国的数据流量，主要走中美海底光缆。但如果这条光缆中断了，那么，还可以走中国-日本-美国；中国-欧洲-美国；中国-新加坡-美国……那么当数据流量在日本、欧洲、新加坡中转时，BGP协议不关注这些过境流量如何通过内部网络，换句话说，中国的路由器上，不需要知道日本、欧洲、新加坡的内部网络的路由，只需要知道边界在哪里，边界是否可达即可。</p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-0015463312f4f324f84cb4ed9d134853_1440w.jpg?source=b1748391" data-caption data-size="normal" data-rawwidth="639" data-rawheight="458" data-default-watermark-src="https://pic1.zhimg.com/v2-8e0d98dad8c913ff60c0851a80959447_720w.jpg?source=b1748391" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-0015463312f4f324f84cb4ed9d134853_r.jpg?source=b1748391" referrerpolicy="no-referrer"></figure><p><br></p><p data-pid="RQWqXbBX">BGP的这种特性还可以用来做网络调优。购买VPS/虚拟主机服务的时候，肯定听说过BGP机房的说法，所谓的BGP机房，就是在机房的出口处，配置一台运行IBGP的路由器，直接连通到EBGP的出口，那么对于跨AS的访问，只需要一跳就可以进入另外一个AS，不需要在运营商网络内部绕路。</p><p data-pid="TTicsDdk">所以，<b>用高速公路、主干道比喻都是不恰当的</b>，主要原因是BGP需要去中心化，去中心化意味着对端不可信，也就无法通过BGP peer去计算AS之间的拓扑了。</p>  
</div>
            