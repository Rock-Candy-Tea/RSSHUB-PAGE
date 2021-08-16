
---
title: 'Oasis 组件系统之脚本'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bc90a33134640a585814600ed0ee104~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 19:48:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bc90a33134640a585814600ed0ee104~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者 - <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fluzhuang" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/luzhuang" ref="nofollow noopener noreferrer">Oasis 团队 - 陆庄</a></p>
<h2 data-id="heading-0">引言</h2>
<p>Oasis是一款“组件式”渲染引擎，使用各种各样的组件给我们的实体添加丰富的能力。脚本是一种特殊的组件，并提供了多种生命周期回调函数，开发者可以重写这些回调函数用于能力扩展和业务逻辑编写。在实际开发中，不可避免的需要用到自定义扩展功能和业务逻辑的编写，所以了解、熟悉脚本的使用与运行机制，对想要使用Oasis开发需求的同学至关重要。</p>
<h2 data-id="heading-1">脚本系统介绍</h2>
<h3 data-id="heading-2">什么是脚本</h3>
<p>脚本系统是衔接引擎能力和游戏逻辑的纽带，脚本扩展自 <code>Script</code> 类，而 <code>Script</code> 用户可以通过它来扩展引擎的功能，也可以在脚本组件提供的生命周期钩子函数中编写自己的游戏逻辑代码。
​</p>
<h3 data-id="heading-3">脚本的生命周期</h3>
<p>Oasis 为用户提供了丰富的生命周期回调函数，用户只要重写指定的回调函数，Oasis 就会在特定的时期自动执行相关脚本，用户不需要手工调用它们。目前提供给用户的生命周期回调函数如下:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bc90a33134640a585814600ed0ee104~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
使用方式详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Foasisengine.cn%2F0.4%2Fdocs%2Fscript-cn%23%25E7%25BB%2584%25E4%25BB%25B6%25E7%2594%259F%25E5%2591%25BD%25E5%2591%25A8%25E6%259C%259F%25E5%2587%25BD%25E6%2595%25B0" target="_blank" rel="nofollow noopener noreferrer" title="https://oasisengine.cn/0.4/docs/script-cn#%E7%BB%84%E4%BB%B6%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%87%BD%E6%95%B0" ref="nofollow noopener noreferrer">官网文档</a></p>
<h2 data-id="heading-4">组件的运行机制</h2>
<p>脚本是组件的一种，所以脚本的运行机制遵循组件的运行机制，相对于其他内置组件，脚本只是拥有更多的生命周期而已，</p>
<h3 data-id="heading-5">组件的驱动</h3>
<p>脚本挂载在实体上，为了找到所有绑定在实体上的脚本并运行他们我们很自然的想到，遍历所有实体，然后发现如果实体上挂有脚本就执行它，如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b1dda42ec754bab9b4f0a5eceeb68d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
初看之下这个方法既简单又清晰，过去的Oasis也是以这种方式驱动组件执行的。但是细心的读者可能已经从图上发现“猫腻”了，就是我们使用引擎时不是所有的实体都会挂载脚本的，甚至可以说只有极少的实体我们需要挂载脚本去实现我们想要的功能。在复杂的场景中我们的实体数可能是几百，几千，甚至上万的（包含模型的实体数），而真正需要挂载的实体可能只有几个，那这种递归遍历就带来了极大的性能浪费。有的读者可能会好奇不就是多遍历了几个空实体么，能有多大损耗呢。大家很容易忽视的一点就是这个遍历是每帧都要执行的，在这种高频的执行下，这种损耗就会积少成多。<br>
随着我们的业务越来越复杂，同时也抱着对开源的敬畏之心，我们决定在开源之前想办法解决这个问题。解决办法其实也很简单，组件（脚本就是组件的一种）的执行从依赖实体的管理改为独立管理就好了，我们新建了一个名为
<code>ComponentsManager</code>的类用于管理所有的组件。新的组件运行执行机制如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a19695f16b549589d0d4639c16ac287~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>ComponentsManager</code>中有多个队列存储着组件的引用，在相应的时机按照生命周期顺序执行：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">if</span> (scene) &#123;
  componentsManager.callScriptOnStart();
  componentsManager.callScriptOnUpdate(deltaTime);
  componentsManager.callAnimationUpdate(deltaTime);
  componentsManager.callScriptOnLateUpdate(deltaTime);

  <span class="hljs-built_in">this</span>._render(scene);
&#125;

componentsManager.callComponentDestory();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">组件的管理</h3>
<p>上文中提到了<code>ComponentsManager</code>这个类，那在这部分我就详细的为大家介绍下他是如何对组件进行管理的</p>
<h4 data-id="heading-7">组件添加到组件队列</h4>
<p>组件添加到<code>ComponentsManager</code>对象中的组件队列中的时机是当组件为<code>enable</code>时，以脚本的父类 <code>Script</code> 为例：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">_onEnable(): <span class="hljs-built_in">void</span> &#123;
  <span class="hljs-keyword">const</span> componentsManager = <span class="hljs-built_in">this</span>.engine._componentsManager;
  <span class="hljs-keyword">const</span> prototype = Script.prototype;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>._started) &#123;
    componentsManager.addOnStartScript(<span class="hljs-built_in">this</span>);
  &#125;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.onUpdate !== prototype.onUpdate) &#123;
  componentsManager.addOnUpdateScript(<span class="hljs-built_in">this</span>);
&#125;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.onLateUpdate !== prototype.onLateUpdate) &#123;
 componentsManager.addOnLateUpdateScript(<span class="hljs-built_in">this</span>);
&#125;
<span class="hljs-built_in">this</span>.onEnable();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是并不是你在组件上设置 <code>enabled</code> 就可以了哦，<code>_onEnable</code> 的触发还依赖挂载实体是
<code>isActiveInHierarchy</code> 的（实体为非active时不会接收到任何回调）也就是挂载的实体是<code>isActive</code>的并且他的祖先实体们也是<code>isActive</code> 的。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">set</span> <span class="hljs-title">enabled</span>(<span class="hljs-params">value: <span class="hljs-built_in">boolean</span></span>) &#123;
  <span class="hljs-keyword">if</span> (value === <span class="hljs-built_in">this</span>._enabled) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-built_in">this</span>._enabled = value;
  <span class="hljs-keyword">if</span> (value) &#123;
    <span class="hljs-built_in">this</span>._entity.isActiveInHierarchy && <span class="hljs-built_in">this</span>._onEnable();
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">this</span>._entity.isActiveInHierarchy && <span class="hljs-built_in">this</span>._onDisable();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">组件从组件队列中移出</h4>
<p>组件从队列中移出的时机是组件状态为<code>disable</code>时，以 <code>Script</code> 类为例：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">_onDisable(): <span class="hljs-built_in">void</span> &#123;
  <span class="hljs-keyword">const</span> componentsManager = <span class="hljs-built_in">this</span>.engine._componentsManager;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._onStartIndex !== -<span class="hljs-number">1</span>) &#123;
    componentsManager.removeOnStartScript(<span class="hljs-built_in">this</span>);
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._onUpdateIndex !== -<span class="hljs-number">1</span>) &#123;
    componentsManager.removeOnUpdateScript(<span class="hljs-built_in">this</span>);
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._onLateUpdateIndex !== -<span class="hljs-number">1</span>) &#123;
    componentsManager.removeOnLateUpdateScript(<span class="hljs-built_in">this</span>);
  &#125;
  <span class="hljs-built_in">this</span>.onDisable();
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_onDisable</code> 的触发与<code>_onEnable</code> 同理也需要挂载实体是<code>isActiveInHierarchy</code> 的。
​</p>
<h4 data-id="heading-9">组件生命周期回调执行</h4>
<p>在《组件的执行》部分已经介绍过了组件的执行机制，这里再对几个特殊的生命周期进行补充。</p>
<h5 data-id="heading-10">onAwake</h5>
<p>与其他生命周期不同，<code>onAwake</code> 的回调触发是不在帧循环中的，而是组件第一次被这只为<code>active</code> 时。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">_setActive(value: <span class="hljs-built_in">boolean</span>): <span class="hljs-built_in">void</span> &#123;
  <span class="hljs-keyword">if</span> (value) &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>._awaked) &#123;
      <span class="hljs-built_in">this</span>._awaked = <span class="hljs-literal">true</span>;
      <span class="hljs-built_in">this</span>._onAwake();
    &#125;
    <span class="hljs-comment">// You can do isActive = false in onAwake function.</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._entity._isActiveInHierarchy) &#123;
      <span class="hljs-built_in">this</span>._onActive();
      <span class="hljs-built_in">this</span>._enabled && <span class="hljs-built_in">this</span>._onEnable();
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">this</span>._enabled && <span class="hljs-built_in">this</span>._onDisable();
<span class="hljs-built_in">this</span>._onInActive();
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">onStart</h5>
<p><code>onStart</code> 函数只需执行一次，执行过后我们就可以将其从队列中移出。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">callScriptOnStart(): <span class="hljs-built_in">void</span> &#123;
  <span class="hljs-keyword">const</span> onStartScripts = <span class="hljs-built_in">this</span>._onStartScripts;
  <span class="hljs-keyword">if</span> (onStartScripts.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">const</span> elements = onStartScripts._elements;
    <span class="hljs-comment">// The 'onStartScripts.length' maybe add if you add some Script with addComponent() in some Script's onStart()</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < onStartScripts.length; i++) &#123;
      <span class="hljs-keyword">const</span> script = elements[i];
      script._started = <span class="hljs-literal">true</span>;
      script._onStartIndex = -<span class="hljs-number">1</span>;
      script.onStart();
    &#125;
    onStartScripts.length = <span class="hljs-number">0</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">onBeginRender，onEndRender</h5>
<p>这两个生命周期的特殊之处在于他们是逐相机触发的。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">if</span> (cameras.length > <span class="hljs-number">0</span>) &#123;
  <span class="hljs-comment">// Sort on priority</span>
  <span class="hljs-comment">//@ts-ignore</span>
  cameras.sort(<span class="hljs-function">(<span class="hljs-params">camera1, camera2</span>) =></span> camera1.priority - camera2.priority);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = cameras.length; i < l; i++) &#123;
    <span class="hljs-keyword">const</span> camera = cameras[i];
    <span class="hljs-keyword">const</span> cameraEntity = camera.entity;
    <span class="hljs-keyword">if</span> (camera.enabled && cameraEntity.isActiveInHierarchy) &#123;
      componentsManager.callCameraOnBeginRender(camera);
      camera.render();
      componentsManager.callCameraOnEndRender(camera);
    &#125;
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  Logger.debug(<span class="hljs-string">"NO active camera."</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13"></h4>
<h4 data-id="heading-14">组件的销毁</h4>
<p>细心的读者可能会发现，销毁的生命周期回调为什么是在帧循环中触发的，不应该是调用销毁方法就马上触发么。在我们的引擎中销毁的生命周期回调是在帧循环的最后才触发的。
这样做的考虑是如果用户在销毁的生命周期回调中，设置了其他组件的 <code>enabled</code> 为 <code>false</code> ，设置实体的
<code>active</code> 为<code>false</code>，或者实体和组件的销毁，那就存在一个问题：组件在组件队列中是无序的，这样操作会导致在当前组件之前执行的组件执行完了自己的更新或渲染，在当前组件之后执行的组件会被移出组件队列将不会执行自己的更新渲染（如下图），而这个顺序对用户来说是未知的，就很可能出现不符合预期的情况。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a91d3b23ae6846a9834a2981254bf976~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">其他想说的</h3>
<p>还有一些零碎的点，我放在这部分跟大家分享。</p>
<h4 data-id="heading-16">ComponentsManager中的组件队列</h4>
<p>相信有的读者在看<code>ComponentsManager</code>类的代码时会有些疑惑:</p>
<ol>
<li>为什么脚本，动画，renderer的update要分成不同的队列，执行中通过判断组件的类型不就好了么。</li>
<li>为什么同一类型组件的不同生命周期要分成不同的队列，执行中直接执行组件的生命周期回调，或者通过判断他是否实现了对应的生命周期，再进行调用不就好了么。</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// Script</span>
<span class="hljs-keyword">private</span> _onStartScripts: DisorderedArray<Script> = <span class="hljs-keyword">new</span> DisorderedArray();
<span class="hljs-keyword">private</span> _onUpdateScripts: DisorderedArray<Script> = <span class="hljs-keyword">new</span> DisorderedArray();
<span class="hljs-keyword">private</span> _onLateUpdateScripts: DisorderedArray<Script> = <span class="hljs-keyword">new</span> DisorderedArray();
<span class="hljs-keyword">private</span> _destoryComponents: Script[] = [];

<span class="hljs-comment">// Animation</span>
<span class="hljs-keyword">private</span> _onUpdateAnimations: DisorderedArray<Component> = <span class="hljs-keyword">new</span> DisorderedArray();

<span class="hljs-comment">// Render</span>
<span class="hljs-keyword">private</span> _renderers: DisorderedArray<Renderer> = <span class="hljs-keyword">new</span> DisorderedArray();
<span class="hljs-keyword">private</span> _onUpdateRenderers: DisorderedArray<Renderer> = <span class="hljs-keyword">new</span> DisorderedArray();

<span class="hljs-comment">// Delay dispose active/inActive Pool</span>
<span class="hljs-keyword">private</span> _componentsContainerPool: Component[][] = [];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里就是我想和大家强调的一个点，希望大家在通过脚本实现功能时也能注意下。大家看上面两个问题，我对应的解决思路都有一个关键词：执行中。还记得我们优化组件执行机制的初衷么，就是不希望在执行中有太多性能损耗，因为生命周期的回调几乎都是每帧更新的，任何小的性能损耗在这样的叠加下都将放大进而影响我们的帧率。
组件的类型判断（instanceOf），空函数的调用，原型链属性的读取都是有一定的性能开销的。而且组件的类型和用户实现的生命周期都是在引擎启动前就决定了，执行的过程中并不会改变，没必要在执行的过程中每帧都做这样重复的判断。因此像上一部分（组件的管理）所写的，我们基本上在组件挂载时就将他分到了他应在的队列中。</p>
<h4 data-id="heading-17">帧循环中的性能优化：</h4>
<p>强调了很多次帧循环内要注意性能，这里分享一些我本人经常忽略的点：</p>
<ol>
<li>条件判断尽量用Enum或数字，不要用字符串：</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7aad9bf149e34ade8056c0c64d541c13~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>尽量用数组存储数据，用数字进行索引，字符串索引是性能杀手：</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1045b58eddb4f92824bcbd7eb56d52d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>for循环倒序最佳</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e98be6757d0547b88c8716a10390bed5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这是我平时开发代码最容易忽视的几个点，相信还有很多的优化手段我就不在这里班门弄斧了。</p>
<h4 data-id="heading-18">无序数组</h4>
<p>前面说了数据的存储建议使用数组，但是在帧循环中如果你的数据要频繁的插入，删除，那这个结论就不成立了。在组件的管理中业务逻辑可能会导致组件enable的频繁切换进而会导致组件队列的增删。我们既想享受到数组快速遍历的特性，又想减少队列增删带来的损耗。因为组件的顺序通常来讲是不重要的，所以我们使用了无序数组来作为组件队列的数据结构。</p>
<h4 data-id="heading-19">帧循环中的GC</h4>
<p>平时我们都强调要注意GC以免造成内存泄漏。在帧循环中也同样要注意GC，但是是尽量避免GC。因为JS的垃圾回收算法主要依赖于引用，当发现这个对象没人引用时浏览器内核就会将这块内存释放掉，但是释放的时机对我们来说是个黑盒。而频繁大量的GC会占用系统资源，这对我们的帧率来说就像是个不定时的炸弹，随时可能造成我们帧率的抖动。因此我们将帧循环中一些临时用到的数组空间采用“对象池”的方式获得，对象池会持有申请过的对象引用，有新的需求来时对其进行复用，这样就防止了这些临时数组的频繁创建销毁导致内存频繁的申请回收。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">getActiveChangedTempList(): Component[] &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._componentsContainerPool.length ? <span class="hljs-built_in">this</span>._componentsContainerPool.pop() : [];
&#125;

putActiveChangedTempList(componentContainer: Component[]): <span class="hljs-built_in">void</span> &#123;
componentContainer.length = <span class="hljs-number">0</span>;
  <span class="hljs-built_in">this</span>._componentsContainerPool.push(componentContainer);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">总结</h2>
<p>这篇文章介绍的内容其实挺简单的，但是对引擎使用者却非常重要，因为脚本真的太常用了，对项目性能的影响又很大。我们后续也会增加新的生命周期函数，比如用户点击以及物理相关的生命周期函数，使互动项目的开发更便捷。
​</p>
<p>希望这篇文章可以帮助大家更好的理解脚本/组件的运行机制同时如果大家有什么好的设计思路及性能优化思路，欢迎在我们的github上提issue讨论。最后欢迎对引擎设计感兴趣的同学和我们联系，一起交流。
​</p>
<p>欢迎大家 star 我们的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine" title="https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine" target="_blank">github 仓库</a>，也可以随时关注我们后续 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine%2Fmilestone%2F3" title="https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine%2Fmilestone%2F3" target="_blank">v0.5</a> 的规划，也可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine%2Fissues" title="https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine%2Fissues" target="_blank">issues</a> 里给我们提需求和问题。开发者可以加入到我们的钉钉群里来跟我们吐槽和探讨一些问题，钉钉搜索 31360432</p>
<p>无论你是渲染、TA 、Web 前端或是游戏方向，只要你和我们一样，渴望实现心中的绿洲，欢迎投递简历到 <a href="https://link.juejin.cn/?target=mailto%3Achenmo.gl%40antgroup.com" title="https://link.juejin.cn?target=mailto%3Achenmo.gl%40antgroup.com" target="_blank">chenmo.gl@antgroup.com</a>。岗位描述详见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Foasis-engine%2Fannouncement%2Fkdlpxt" title="https://link.juejin.cn?target=https%3A%2F%2Fwww.yuque.com%2Foasis-engine%2Fannouncement%2Fkdlpxt" target="_blank">www.yuque.com/oasis-engin…</a>。</p></div>  
</div>
            