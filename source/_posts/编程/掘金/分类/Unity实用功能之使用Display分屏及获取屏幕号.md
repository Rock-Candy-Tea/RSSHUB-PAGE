
---
title: 'Unity实用功能之使用Display分屏及获取屏幕号'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/986ddbe42cab43fc814b8d638e43f74e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 01:58:11 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/986ddbe42cab43fc814b8d638e43f74e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第9天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">概述</h2>
<p>在日常开发中，经常会遇到多屏幕开发，就是所谓的分屏。本片文章就主要介绍一下，在Unity中如何使用分屏功能，以及如何获取当前鼠标点击的是哪一个屏幕。</p>
<h2 data-id="heading-1">功能实现</h2>
<p>在Unity中使用分屏功能方法有很多种，这个需要根据项目需求具体分析，本篇文章主要使用的是多摄像机分屏，共分为五个屏幕。</p>
<h3 data-id="heading-2">分屏场景搭建</h3>
<p>在Unity中创建五个摄像机，五个Canvas</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/986ddbe42cab43fc814b8d638e43f74e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后修改相机和Canvas参数,这里面都是修改Target Display,只有修改成对应的Display，canvas上的内容才会显示在UI应的相机屏幕中</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4844c58ab6c4da0a2918818365fd9bd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">  <img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c09165299f04e658cedea1315d74f26~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来就是修改Game视图中的Dispay，只有Game视图中的Display也修改了才能显示对应的摄像机画面</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/868fd043422140d69c26d9d00d290f87~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">Display详解</h3>
<p>Unity官方文档<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.unity3d.com%2FManual%2FMultiDisplay.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.unity3d.com/Manual/MultiDisplay.html" ref="nofollow noopener noreferrer">地址</a><br>
官方文档中叫 Multi-display，其解释为可以使用多显示器同时在最多八个不同的监视器上显示最多八个不同的应用程序视图。可以将其用于 PC 游戏、街机游戏机或公共显示装置等设置。
Unity 支持多显示器：</p>
<ul>
<li>独立平台（Windows、macOS X 和 Linux）</li>
<li>Android（OpenGL ES 和 Vulkan）</li>
<li>IOS</li>
</ul>
<p>UnityDisplay分屏目前最多支持8个屏幕</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba48b348c43f4b6ea4331deee23875f2~tplv-k3u1fbpfcp-watermark.image" alt="捕获.PNG" loading="lazy" referrerpolicy="no-referrer">
具体的场景搭建已经在上面写过了，但是场景搭建完成还不行，还需要将屏幕激活，才可以使用，因为Unity的默认显示模式是仅一台显示，所以运行应用程序时，需要使用<code>Display.Activate()</code>显式激活其他显示。<br>
<strong>一旦激活显示器，就无法将其停用。</strong></p>
<pre><code class="copyable">for (int i = 0; i < Display.displays.Length; i++)
&#123;
    Display.displays[i].Activate();
    Screen.SetResolution(Display.displays[i].renderingWidth, Display.displays[i].renderingHeight, true);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多有关Display的方法请查看光放API</p>
<h3 data-id="heading-4">获取屏幕号</h3>
<p>这里有一点需要注意的就是 Display.displays.Length这个属性，在Editor下，无论你的主机连接了多少个显示器，Display.displays.Length的值都是1。只有打包运行的时候，返回值才是真的连接的显示器个数。<br>
我们获取屏幕号的方法主要的思路就是。通过鼠标在屏幕中的位置，然后除以分辨率的宽度进行获取。但是这里面有点坑的是，在Editor模式下和打包出来的模式下，不太一样。<br>
我们用到的是鼠标的<code>Input.mousePosition</code>,而这个是以屏幕的左下角为（0,0），右上角为顶点。在打包出来的时候鼠标的范围应该是（0,0）-（9600,1080）。这里我的电脑屏幕是1920*1080的分辨率，所以五个屏幕连起来鼠标的最大坐标为（9600,1080）。<br>
其实写到这里，都很好计算屏幕序号，鼠标的x轴的值/单个屏幕的宽度+1就是当前的屏幕序号，但是有时候会有小数出现，所以我们要向下取整。代码如下</p>
<pre><code class="copyable">sceneNumber = (int)Mathf.Floor(mousePosition.x / (float)SceneWidth) + 1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，屏幕序号就获取到了（打包之后的程序），那么该如何获取鼠标在该屏幕上的位置呢，其实也很简单，只要知道了是第几个屏幕，鼠标的横坐标减去相对应个屏幕宽度即可。</p>
<pre><code class="copyable">Vector3 pos =new Vector3(mousePosition.x- (SceneWidth*(sceneNumber-1)), mousePosition.y, mousePosition.z);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">坑来了</h4>
<p>上面打包状态下屏幕号获取非常容易，那么在Editor下呢？是否也一样？答案是否定的。。。<br>
当你使用上述代码的时候你会发现，计算到的屏幕号就不一定是多少了，负数都有可能。那是因为，在编辑器状态下，会默认一个屏幕（Game视图）为主屏幕，鼠标位置是以该屏幕的左下角为（0，0），右上角为（1920,1080）所以超出的部分有可能是正有可能是特别大。比如下图，鼠标位置已经负1000多了，显然不对</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dccee76f1364d379e4ab69556de53b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
通过测试发现，当鼠标点在哪个屏幕，哪个屏幕就不会被默认为主屏幕，而当我们点击鼠标想要计算的时候，就会发现，鼠标的位置始终是当前位置，经过探索发现，当我们点击鼠标的时候，程序会在点击的同时更改当前屏幕为主屏幕，我们在Update中使用如下代码测试，会发现，在鼠标点击拍断执行之前，鼠标位置已经发生了改变。</p>
<pre><code class="copyable">Debug.Log(Input.mousePosition);
if (Input.GetMouseButtonDown(0))
&#123;
    Debug.Log("鼠标点击");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/796132b1baac4a0bbb560ba00372d502~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
那么我们也不能每次测试都打一个包吧，所以就自己研究了个解决办法</p>
<ol>
<li>运行时先点击屏幕一，确定一号屏幕</li>
<li>创建 private float[] positions = &#123; 1, 1 &#125;;数组，存储上一次鼠标的横轴坐标和当前的横轴坐标</li>
<li>通过上一次点击的屏幕号和鼠标位置计算当前的屏幕号</li>
</ol>
<p>首先确定屏幕一</p>
<pre><code class="copyable">if (Input.GetMouseButtonDown(0))
&#123;
    if (!isSureScene1)
    &#123;
        isSureScene1 = true;
        sceneNumber = 1;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后记录鼠标的位置，上一次和当前的</p>
<pre><code class="copyable"> //记录鼠标位置（横坐标X值，用于计算屏幕号）
 positions[0] = positions[1];
 positions[1] = Input.mousePosition.x;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后计算屏幕号，比打包的能复杂点，也仅仅是一点，仅仅就是变为了在当前屏幕号的基础上加上计算的屏幕号</p>
<pre><code class="copyable">/// <summary>
/// 通过鼠标位置计算屏幕号
/// </summary>
/// <returns></returns>
void GetSceneNumberFromMousePosition()
&#123;
        sceneNumber += (int)Mathf.Floor(positions[0] / (float)SceneWidth);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就能够完美的解决了在编辑器状态下无法获取屏幕号的问题了，就能够直接通过屏幕号获取摄像机，然后就可以用来发射射线等功能了。
效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d2b052b9e87430fa554bcdc7f938f03~tplv-k3u1fbpfcp-watermark.image" alt="4545.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">总结</h2>
<p>此方法还不是很完善，但是在Unity这个使用已经是足够了，缺点就是对分辨率有要求，分辨率要相同才行，其次就是，在Editor下，game视图要保证大小差不多，并别摆放，就上上图那样，的否则会计算错误。</p>
<h2 data-id="heading-7">写在最后</h2>
<p>所有分享的内容均为作者在日常开发过程中使用过的各种小功能点，分享出来也变相的回顾一下，如有写的不好的地方还请多多指教。Demo源码会在之后整理好之后分享给大家。欢迎大家相互学习进步。</p></div>  
</div>
            