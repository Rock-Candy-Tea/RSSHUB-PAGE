
---
title: 'Unity实用功能之实用Navigation(自动寻路系统)制作简易AI巡逻'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98fc06b2ff0543229463240554bc228f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 17:22:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98fc06b2ff0543229463240554bc228f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">概述</h2>
<p>AI巡逻功能一般在游戏开发中使用的比较多，最近做了一个打僵尸的项目，僵尸生成后要在城市中随机游走，当有玩家打僵尸的时候，僵尸会跑到玩家身前攻击玩家。这里就涉及到了AI的巡逻功能，所以就自己研究了一下。本片文章就简单的介绍一下实现过程</p>
<h2 data-id="heading-1">思路分析</h2>
<p>我这里使用的是Unity自带的寻路系统<code>Navigation</code>，整体思路就是，初始给AI一个目标点，让AI向着目标点移动，当AI走至目标点之后，再次以AI为中心，在半径为10-15米范围内随机取再取一个目标点让AI继续朝着目标点前进，直到有玩家攻击僵尸为止。</p>
<h2 data-id="heading-2">功能实现</h2>
<h3 data-id="heading-3">场景搭建</h3>
<p>首先我们在Unity中搭建一个简易的场景，一个地形，N多个Cube当障碍物，然后在放入AI资源（网上寻找就行，用方块代替也都行）。
最终场景如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98fc06b2ff0543229463240554bc228f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
半透明方块为障碍物，红球是为了看其中一个僵尸的目标点。</p>
<h3 data-id="heading-4">Nav Mesh Agent组件</h3>
<p>Nav Mesh Agent组件可以实现对指定对象寻路的代理，该组件自带了许多参数，可以通过修改Nav Mesh Agent组件的参数来实现对代理器大小，速度，加速度的控制，这里面就不做过多的讲解，只介绍一下参数。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf2c3c881f3a4ea482ad7781ec7da2eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Speed：移动速度</li>
<li>Angular Speed：角速度</li>
<li>Acceleration：加速度</li>
<li>Stopping Distance：到达时与目的地的路线</li>
<li>Auto Braking：是否自动停止无法到达目的地的路线</li>
<li>Radius：半径</li>
<li>Height：高度</li>
<li>Quality：障碍物躲避质量</li>
<li>Priority：回避优先等级</li>
<li>Auto Traverse Off Mesh Link：是否自动移动Off Mesh Link</li>
<li>Auto Repath：原有路径发现变化时是否重新寻路</li>
<li>Area Mask：在寻路径是将考虑的区域类型</li>
</ul>
<h3 data-id="heading-5">计算目标点开始寻路</h3>
<p>首先我们先随机取一个方向，作为下一个目标点的方向</p>
<pre><code class="copyable">//随机取一个方向
Vector3 dir = new Vector3(Random.Range(-10f, 10f), 0, Random.Range(-10f, 10f)).normalized;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，在这个方向的基础上随机取一个目标点，minDis为最小距离, maxDis为最大距离</p>
<pre><code class="copyable">//在这个方向的基础上取一个目标点
Vector3 pos = transform.position + transform.rotation * dir * Random.Range(minDis, maxDis);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置AI的目标点，并让目标进行移动。首先需要先获取AI身上的NavMeshAgent组件，然后通过方法SetDestination设置目标点即可</p>
<pre><code class="copyable">public NavMeshAgent NavMesh;
NavMesh = this.gameObject.GetComponent<NavMeshAgent>();
NavMesh.SetDestination(pos);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2990912b57fa4f7184758a0710e34ea4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这样AI就可以像目标点移动了。<br>
<strong>接下来要判断AI是否到达目标点。此方法即使目标点在一些不可能到达的目的地也可以计算</strong></p>
<pre><code class="copyable"> /// <summary>
 /// 判断是否到达目目标点
 /// </summary>
 /// <returns>true为未到达，false到达</returns>
 public bool IsMoving()
 &#123;
     if (!aidata.NavMesh.enabled)
         return false;
     bool r = aidata.NavMesh.pathPending ||
     aidata.NavMesh.remainingDistance > aidata.NavMesh.stoppingDistance ||
     idata.NavMesh.velocity != Vector3.zero;
     r = aidata.NavMesh.enabled ? r : false;
     return r;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在Update中实时判断是否到达，到达之后再次进行目标点获取与设置</p>
<pre><code class="copyable">if (!IsMoving())
&#123;
    //获取新目标点
    //设置AI新的目标点           
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ea6b6a0fc6d4b03be3a50e99ac6a3d0~tplv-k3u1fbpfcp-watermark.image" alt="454545.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">写在最后</h2>
<p>所有分享的内容均为作者在日常开发过程中使用过的各种小功能点，分享出来也变相的回顾一下，如有写的不好的地方还请多多指教。Demo源码会在之后整理好之后分享给大家。欢迎大家相互学习进步。</p></div>  
</div>
            