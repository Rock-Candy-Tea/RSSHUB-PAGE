
---
title: '从0开始撸React源码-03ReactDom.render'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7c6d0143044d369655cc171dc55bb9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 20:06:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7c6d0143044d369655cc171dc55bb9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>声明 : 当前react源码版本为16.8.6</p>
<h1 data-id="heading-0">1.ReactDom</h1>
<p>在源码中找到ReactDom的定义</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7c6d0143044d369655cc171dc55bb9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们熟悉的render方法的入口就在这里</p>
<h1 data-id="heading-1">2.ReactDom.render(<App / > , root , callback)</h1>
<p>我们进入render方法，发现这个方法接收三个参数。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1608727799b9428d9a1ded7804016eff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>render 方法调用了 legacyRenderSubtreeIntoContainer</p>
<h2 data-id="heading-2">2.1 legacyRenderSubtreeIntoContainer</h2>
<p>这个方法会检验我们的容器上是否存在_reactRootContainer这个属性，初次渲染的时候 我们的容器上不会存在这个属性。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/482a1340a58a49b4987a4e50e601fb41~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们会走入这段逻辑</p>
<pre><code class="hljs language-javaScript copyable" lang="javaScript"> <span class="hljs-keyword">if</span> (!root) &#123;
    <span class="hljs-comment">// Initial mount</span>
    root = container._reactRootContainer = legacyCreateRootFromDOMContainer(
      container,
      forceHydrate,
    );
    ...
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看一下 legacyCreateRootFromDOMContainer 这个方法</p>
<h2 data-id="heading-3">2.2 legacyCreateRootFromDOMContainer</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb02d3f751e54b4b8c19c274e9a4d2f7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里需要解释一下参数里的forceHydrate.这里的forceHydrate的值是在 legacyRenderSubtreeIntoContainer 这个方法的第四个参数</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c412b28cf6c84f4783a8be86cd1e22e7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到,他手动传入false.</p>
<p>这个参数的作用是,是否复用容器中的DOM.主要用于服务端渲染.</p>
<p>由于这个值是false,所以我们会走到 shouldHydrateDueToLegacyHeuristic 这个方法</p>
<h3 data-id="heading-4">2.2.1 shouldHydrateDueToLegacyHeuristic</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b61fd4919958474aa5c6ae2da864f036~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个方法的目的是判断是不是一个合法的挂载目标节点.这里检验了挂载目标节点中是否存在ROOT_ATTRIBUTE_NAME(data-reactroot).老版本react是用这个标识判断是否需要对容器内元素进行合并(ssr相关)</p>
<p>由于我们的运行时是clint,所以 shouldHydrate 这个变量值是false.</p>
<p>之后react把container中节点都给移除掉</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47e11d00dce040e8bff6a2a6dad49776~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之后返回了一个ReactRoot</p>
<h2 data-id="heading-5">2.3 ReactRoot</h2>
<p>执行了 createContainer 方法 并且在原型上声明了几个方法.(记住render方法是在这里注册的)</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0c3d141f8c5426f8320e54543cef31a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">2.3.1 createContainer</h3>
<p>这个方法的核心是创建一个FiberRoot</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e295ecbcc6484fbda69877714e82d9d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们先记住这里创建了一个FiberRoot即可.</p>
<p>到这里我们获得了 legacyCreateRootFromDOMContainer 方法的执行结果.我们可以回到 legacyRenderSubtreeIntoContainer 这个方法</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3c581215bc4491296310f578069082d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们的root现在已经有值了.之后判断了一下用户有没有callback,这里不过多解释.接下来这里涉及到了一个新的概念:batchedUpdates(批量更新).这部分需要我们在讲解更新流程时才能看到.你可以当做这里无事发生(其实就是改了个更新需要的全局变量.).所以我们直接看他的回调函数.</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">if</span> (parentComponent != <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">// ...</span>
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 最终调用</span>
    root.render(children, callback);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">2.4 render</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d24874bf9c9b4a77a7fa0d5a2b789427~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7fa177a6d5b4f758b113749bef468a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里又有一个概念,ExpirationTime.可以根据任务优先级进行更新.</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> expirationTime = computeExpirationForFiber(currentTime, current);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后他执行了 updateContainerAtExpirationTime 这个方法</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6c206ab41894f91b6fbc487293452e6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">2.5 scheduleRootUpdate</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae1af946118147fd943fc308b78d2cb5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">总结</h1>
<p>我们先熟悉流程,再去看每个方法具体实现细节.否则分支太多,很容易钻牛角尖.</p>
<p>在ReactDom.render的过程中,我们创建了一个reactRoot,同时创建了一个FiberRoot.在FiberRoot创建的过程中,会创建一个Fiber对象.</p>
<p>在root上我们创建了一个ExpirationTime和update更新对象,然后把这个更新对象加入到Fiber对象中.此过程为创建更新.</p>
<p>然后我们开始进行任务调度,开始调度更新scheduleWork</p>
<p>下一篇 : React-Fiber-Root</p></div>  
</div>
            