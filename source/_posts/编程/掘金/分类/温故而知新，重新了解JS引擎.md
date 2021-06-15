
---
title: '温故而知新，重新了解JS引擎'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8ced7b3a8044b358736aded0df17051~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 07:24:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8ced7b3a8044b358736aded0df17051~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第14天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">前言</h1>
<p>前段时间在看小黄书，里头讲了<code>JS</code>的编译原理，并提到了<code>JS</code>引擎，出于好奇，我想去了解相关方面的知识。查阅了大量资料后，我将知识点归纳吸收，便有了此文</p>
<p>为了方便阅读，我将文章分成一下几部分</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8ced7b3a8044b358736aded0df17051~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">什么是JS引擎</h1>
<p>关于什么是JS引擎，我觉得结合生活中的例子会很好理解！</p>
<p>以生活中的汽车为例，汽车需要动，能让汽车动起来的那个东西就是引擎，如V8发动机。如果没有引擎，那仅仅是一堆废铜烂铁。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c61c8995e44a4631bc22f3d8a5091a61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而JS引擎也是一样，就是让JS动起来的东西。</p>
<p>为了体现我的专业，引入百度百科对它的定义</p>
<blockquote>
<p>JavaScript引擎是一个专门处理JavaScript脚本的虚拟机</p>
</blockquote>
<p>可以看到，<code>JS</code>引擎本质是一个虚拟机或者说是一个程序，只是这个程序能处理我们的JS代码，让我们写JS代码动起来，从而发挥代码的威力。</p>
<p>那引擎具体做了哪些工作呢？</p>
<p>简单总结，<code>JS</code>引擎可以将 <code>JS </code>代码编译为不同 <code>CPU</code>对应的汇编代码，而且还负责执行代码、分配内存以及垃圾回收等工作</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f41ab1248e004bea8a8967fffba2aebb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">常见的JS引擎有哪些</h1>
<p>其实这也是我最开始学写篇文章的初衷，我在网上查阅了很多资料，但是发现文章都比较陈旧，而且各个引擎出现的时间杂乱无章，于是我希望自己可以按照引擎出现的时间线进行整理</p>
<p>下面按照各大引擎大致出现的顺序进行排列</p>
<ol>
<li>
<p>Mozilla的<code>SpiderMonkey</code>引擎，是第一款JavaScript引擎，早期用于 Netscape Navigator，现时用于 Mozilla Firefox。是用C语言实现的，还有一个Java版本叫Rhino；<code>Rhino</code>引擎由Mozilla基金会管理，开放源代码，完全以Java编写，用于 HTMLUnit；而后<code>TraceMonkey</code>引擎是基于实时编译的引擎，用于Mozilla Firefox 3.5～3.6版本；<code>JaegerMonkey</code>：结合追踪和组合码技术大幅提高性能，用于Mozilla Firefox 4.0以上版本</p>
</li>
<li>
<p>Apple的<code>JavaScriptCore</code> ，简称JSC，开源，用于webkit内核浏览器，如 Safari ，2008 年实现了编译器和字节码解释器，升级为了 <code>SquirrelFish</code>。苹果内部代号为<code>Nitro</code>的 JavaScript 引擎也是基于 JSC引擎的。至于具体时间，JSC是WebKit默认内嵌的JS引擎，而WebKit诞生于1998年，<code>Nitro</code>是为Safari 4编写，Safari 4是2009年6月发布。</p>
</li>
<li>
<p>Opera的<code>LinearA</code>：用于Opera4.0到6.1，Opera4于2000年6月发布；<code>LinearB</code>：用于Opera7.0到9.2，Opera7于2003年6月发布；<code>Futhark</code>：用于Opera9.5到10.2，Opera9.5于2008年6月发布；<code>Carakan</code>：用于Opera10.5.及以上  2009年12月</p>
</li>
<li>
<p><code>Tamarin</code>引擎，由Adobe Labs编写，Flash Player 9所使用的引擎，大概时间2006年6月</p>
</li>
<li>
<p>2008年9月，Google的<code>V8</code>引擎第一个版本随着Chrome的第一个版本发布。<code>V8</code>引擎用 C++编写，由 Google 丹麦开发，开源。除了Chrome，还被运用于Node.js以及运用于Android操作系统等</p>
</li>
<li>
<p>Microsoft 的<code>Chakra</code>，译名查克拉，用于IE9、10、11和Microsoft Edge，IE9发布时间2011年3月</p>
</li>
<li>
<p><code>JerryScript</code>引擎 , 三星推出的适用于嵌入式设备的小型 JavaScript 引擎，2015年开源</p>
</li>
<li>
<p><code>Nashorn</code>引擎，从 JDK 1.8 开始，Nashorn取代Rhino(JDK 1.6, JDK1.7) 成为 Java 的嵌入式 JavaScript 引擎，JDK1.8发布于2014年</p>
</li>
<li>
<p><code>QuickJS </code>引擎， 2019 年 7 月发布</p>
</li>
<li>
<p><code>Hermes</code>引擎，Facebook在Chain React 2019 大会上发布的一个崭新JavaScript引擎，用于移动端React Native应用的集成，开源</p>
</li>
</ol>
<p>注：</p>
<ul>
<li>上述内容参考了大量资料所得，并不保证一定精准</li>
<li>由于有些引擎找不到何时发布的具体时间，于是我把该引擎最早被应用的时间表示其发布时间</li>
</ul>
<p>了解什么是JS引擎，也梳理常见的JS引擎，下面我们来看看引擎是如何运行JS代码的：以V8为例</p>
<h1 data-id="heading-3">V8引擎如何运行JS代码</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc2f0171041040f4b1cd32378106d6c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们简单来了解一下V8引擎</p>
<h2 data-id="heading-4">关于V8</h2>
<p><code>V8</code>引擎是使用<code>C++</code>编写的，由<code>Google</code>开源的<code>JavaScript</code>和<code>WebAssembly</code>引擎。<code>V8</code>第一个版本随着第一个版本的<code>Chrome</code>于<code>2008</code>年<code>9</code>月<code>2</code>日发布。</p>
<p>V8因为它的高性能被很多人青睐，于是常见的如</p>
<ol>
<li><code>Chrome</code>浏览器的<code>JS</code>引擎是<code>V8</code></li>
<li><code>Nodejs</code>的运行时环境是<code>V8</code></li>
<li><code>electron</code>的底层引擎也是<code>V8 </code></li>
</ol>
<p>那V8具体都做了哪些工作呢？</p>
<h2 data-id="heading-5">V8主要职责</h2>
<p>简单来说，<code>V8</code>是一个接收<code>JavaScript</code>代码，编译代码然后执行<code>C++</code>程序，编译后的代码可以在多种操作系统多种处理器上运行。其主要职责：</p>
<ol>
<li>编译和执行<code>JS</code>代码</li>
<li>处理调用栈</li>
<li>内存分配</li>
<li>垃圾回收等</li>
</ol>
<p>下面主要来看，V8如何编译和执行<code>JS</code></p>
<h2 data-id="heading-6">V8如何编译和执行JS代码</h2>
<p>一般来说，<code>JS</code>引擎在编译和执行代码都会用到三个重要的组件：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be8281f80d744587823635b7d960f1dc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">解析器parser</h3>
<p>负责将<code>JS</code>源代码解析成抽象语法树<code>AST</code>，如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffcaba81e34a41779a027cba5c437f46~tplv-k3u1fbpfcp-watermark.image" alt="动画11111111.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>JS代码变成AST的样子，你可以移步到ASTExplorer去看</p>
<h3 data-id="heading-8">解释器interpreter</h3>
<p>解释器负责将<code>AST</code>解析成字节码<code>bytecode</code>，并可以将解析成的<code>bytecode</code>解释执行</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4a3173b5e6547299280a55ccc8229e5~tplv-k3u1fbpfcp-watermark.image" alt="444.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">编译器compiler</h3>
<p>编译器负责编译出运行更加高效的机器代码</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4157ce3505de4163a1d90408f404f51e~tplv-k3u1fbpfcp-watermark.image" alt="5555.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是在<code>V8</code>早期，在<code>5.9</code>版本以前，是没有解释器，但有两个编译器，其编译流程如下</p>
<ol>
<li><code>parser</code>  解释器生成抽象语法树<code>AST</code></li>
<li><code>compiler</code>  编译器<code>Full-codegen </code> 基准编译器  直接生成机器码</li>
<li>运行一段时间后，由分析器线程优化<code>js</code>代码</li>
<li><code>compiler</code>  编译器<code>CrankShaft</code>   优化编译器   重新生成<code>AST</code>提升运行效率</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfb02b25d7a048acad20bb0be079e3a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样设计的缺点</p>
<ol>
<li>机器码会占用大量的内存</li>
<li>缺少中间层机器码，无法实现一些优化策略</li>
<li>无法很好的支持和优化<code>JS</code>的新语特性，无法拥抱未来</li>
</ol>
<p>正因为存在以上问题，新版本的V8流程上有所优化，流程如下</p>
<ol>
<li><code>parser</code>  解析器  生成<code>AST</code>抽象语法树</li>
<li><code>interpreter</code>   解释器  <code> Ignition</code>   生成<code>byteCode</code>字节码  并直接执行</li>
<li>清除<code>AST</code>释放内存空间</li>
<li>得到<code>25% - 50%</code>的等效机器代码大小</li>
<li><code>compiler </code> 运行过程中，解释器收集优化信息发送给编译器<code>TurboFan</code></li>
<li>重新生成机器码</li>
<li>有些热点函数变更会由优化后的机器码还原成字节码 也就是<code>deoptimization</code>  回退字节码操作执行</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/732ccd5315ea4c2180d00faf8d460929~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优化点：</p>
<ol>
<li>值声明未调用，不会被解析生成<code>AST</code></li>
<li>函数只被调用一次，<code>bytcode</code>直接被解释执行，不会进入到编译优化阶段</li>
<li>函数被调用多次，<code>Igniton</code>会收集函数类型信息，可能会被标记为热点函数，可能被编译成优化后的机器代码</li>
</ol>
<p>好处：</p>
<ol>
<li>由于一开始不需要直接编译成机器码，生成了中间层的字节码，从而节约了时间</li>
<li>优化编译阶段，不需要从源码重新解析,直接通过字节码进行优化，也可以<code>deoptimization</code>回退操作</li>
</ol>
<p>以上就是本次关于JS引擎的所有内容！如果有误，欢迎留言告知，也欢迎点赞支持！</p>
<h1 data-id="heading-10">end</h1></div>  
</div>
            