
---
title: 'webpack原理-webpack5内部分包原理解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db2950ad4aba4fb29764d45225a4b30f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 10:56:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db2950ad4aba4fb29764d45225a4b30f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:30px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:60px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:24px 0 12px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#a862ea&#125;.markdown-body ol li.task-list-item,.markdown-body ul li.task-list-item&#123;list-style:none&#125;.markdown-body ol li.task-list-item ol,.markdown-body ol li.task-list-item ul,.markdown-body ul li.task-list-item ol,.markdown-body ul li.task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body a,.markdown-body code,.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6,.markdown-body li,.markdown-body p&#123;opacity:.85;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body a:hover,.markdown-body code:hover,.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover,.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:1px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;transition:transform .2s ease 0s;background-color:#f8f5ff;box-shadow:0 0 10px #e7daff&#125;.markdown-body img:hover&#123;opacity:1;box-shadow:0 0 20px #e7daff;transform:translateY(-1px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:12px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:3px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body .math&#123;font-style:italic;margin:12px 0;padding:.5em 1em;background-color:#f8f5ff&#125;.markdown-body .math>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:18px;color:#383838;border-radius:2px;scroll-behavior:smooth;box-shadow:0 0 10px #e7daff&#125;.markdown-body pre>code:hover&#123;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;width:100%;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:.5em;border:1px solid #e7daff&#125;.markdown-body tr&#123;background-color:#f8f5ff&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h1 data-id="heading-0">开场白</h1>
<blockquote>
<p>大家好，我是Webpack，AKA打包老炮，我的slogan是："打天下的包，让Rollup无包可打"。 <br></p>
</blockquote>
<pre><code class="hljs copyable">今天我要带来的才艺是：解析webpack5内部的分包规则,也就是ChunkGraph    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果还没看过这篇文章的话，建议先读完再看这里。</p>
<p><a href="https://juejin.cn/post/7125696644435148831" target="_blank" title="https://juejin.cn/post/7125696644435148831">webpack原理解析【长文万字】</a></p>
<p><a href="https://juejin.cn/post/7138285996500025352" target="_blank" title="https://juejin.cn/post/7138285996500025352">webpack原理 - ModuleGraph原理</a></p>
<p>本文从以下几个问题依次解答剖析webpack内部的分包规则：</p>
<ul>
<li>1：webpack分包规则与ChunkGraph的关系</li>
<li>2：ChunGraph长什么样子？</li>
<li>3：ChunkGraph构建的过程？</li>
</ul>
<h1 data-id="heading-1">webpack分包规则与ChunkGraph的关系</h1>
<p>   你可以简单的认为ChunkGraph就等于webpack的分包规则！
   这句话有点简单，但这么理解完全没问题。</p>
<p>   我们都知道chunk往往都是一一对应产物【bundle】，那么一个程序往往不是只有一个chunk，一般来说我们配置多个入口文件，就会产生多个chunk；多个异步引入模块，也会产生多个chunk。那么问题就来了，你知道这些逻辑在webpack的内部是如何实现的吗？webpack又是如何设计这些对象的？</p>
<p>   如果你看过往期文章，知道了ModuleGraph是以module为中心描绘module之间关系的对象。那么对应的：ChunkGraph就是以chunk为中心描绘chunk与module关系对象。</p>
<p>   在讨论ChunkGraph之前，希望能够先想象一下这样一个场景：</p>
<pre><code class="hljs language-css copyable" lang="css">入口文件<span class="hljs-number">1in</span>dex<span class="hljs-selector-class">.js</span>，引用了<span class="hljs-selector-tag">a</span><span class="hljs-selector-class">.js</span>、<span class="hljs-selector-tag">b</span><span class="hljs-selector-class">.js</span>；入口文件<span class="hljs-number">2</span>main<span class="hljs-selector-class">.js</span>，引用了<span class="hljs-selector-tag">b</span><span class="hljs-selector-class">.js</span>。
这样的结构打包出来的chunk会是什么样的呢？
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据你的经验，你可能马上想到了，这样打包出来的chunk有两个：</p>
<ul>
<li>chunk-index[a.js, b.js]</li>
<li>chunk-main[b.js]
没有错，事实也是如此。但是你理解webpack构建出来这两个chunk的原理吗？
另外，这个b.js被两个chunk引用你可能马上也想到了通过配置SplitChunkPlugin将b.js打包到新的chunk以减小包体积的问题。</li>
<li>chunk-b[b.js]
那SplitChunkGraph又是如何去完成上述这个功能的呢？【SplitChunkPlugin的原理我们留到以后再出文章去解析】
这里我们可以简单理解为SplitChunkPlugin也是通过改写ChunkGraph对象内部数据来实现的。</li>
</ul>
<p>所以学习ChunkGraph的原理除了面试时跟面试官battle外，也有助于你更加好的去优化你的项目构建速度、减小包体积的问题。</p>
<h1 data-id="heading-2">ChunkGraph长什么样子？</h1>
<p>在想webpack怎么实现之前先思考如果是我们来实现ChunkGraph的话，我们该如何设计呢？
在开始阅读webpack5的源码之前我也问过自己这个问题。我的想法是ChunkGraph核心记录的信息应该是：</p>
<ul>
<li>有哪些chunk，chunk里面有哪些module</li>
<li>有哪些module，module属于哪些chunk
有了这样的信息就能够清楚的表达chunk与module的关系了。也方便分包优化的操作。</li>
</ul>
<p>所以必然的，要有一个放chunk列表的变量【chunks】；也要有一个放module列表的变量【modules】。</p>
<p>事实上当我打开webpack内部源码的时候，也发现了这样的变量。但不同的是，chunks不是一个数组而是一个Map<chunk, ChunkGraphChunk>；modules也不是一个数组，而是Map<modules, ChunkGraphModule>。</p>
<p>但问题不大</p>
<ul>
<li>chunks：Map<chunk, ChunkGraphChunk>中的ChunkGraphChunk依然用来记录当前chunk中有哪些modules的</li>
<li>modules：Map<modules, ChunkGraphModule>中的ChunkGraphModule是用来记录当前module属于哪些chunk的</li>
</ul>
<p>所以，带着这样的思路去有助于阅读webpack的源码</p>
<p>ChunkGraph的核心：</p>
<ul>
<li>有哪些chunk，chunk里面有哪些module</li>
<li>有哪些module，module属于哪些chunk</li>
</ul>
<h2 data-id="heading-3">ChunkGraph的庐山真面目</h2>
<p>至此，正式揭开ChunkGraph的真实面目：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db2950ad4aba4fb29764d45225a4b30f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
这里面除了ChunGraph对象，还有
ChunkGraphChunk：记录一个chunk有哪些module
ChunkGraphModule：记录一个module属于哪些chunk。就好像b.js 既属于chunk-index, 又属于chunk-main。</p>
<p>接下来我们剖析源码分析，上图的数据是如何收集构建出来的【主要是关注ChunkGraph的_modules、_chunks是如何添加进来数据的】。</p>
<h1 data-id="heading-4">ChunkGraph构建的过程？</h1>
<p>ChunkGraph构建发生在webpack的seal函数内；
大致可以分为两个阶段：</p>
<ul>
<li>初始化入口ChunkGraph</li>
<li>构建完整chunkGraph</li>
</ul>
<h2 data-id="heading-5">初始化入口ChunkGraph</h2>
<p>这个阶段的代码比较简单。可以总结为以下步骤</p>
<ul>
<li>遍历入口</li>
<li>创建入口chunk，<em>关联chunk和chunkGrorup关系</em></li>
<li>遍历入口的module</li>
<li>设置chunkGraph的_modules,_chunks值【收集ChunkGraph的_modules中的entryModules, _chunks中的entryInChunks】</li>
<li>设置chunkGraphInit值</li>
</ul>
<p>tips: 简单一句话总结：创建入口chunk，绑定入口module与chunk的关系，设置chunkGraphInit值。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3d07aa0bdc64fba8997e800929af2de~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对应源码也贴一下。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c5964e4d2b246489b9d5cb6d8bfe7b6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
细心地你可能已经找到了一个入口对应一个chunk的原因了。</p>
<p>在上述的流程中仅仅是入口chunk，入口module做了处理。
所以说这个阶段叫：初始化入口ChunkGraph。
chunkGraphInit数据是为了构建完整chunkGraph提供一个起点数据，在下一阶段会从这个起点不断摸索其他module与chunk的关系。</p>
<p><strong>看看真实数据长什么样子，来帮助下我们更好的理解该阶段</strong>
假设当前的module依赖关系：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fd530518fdc420784b7e0fb9fecd4d1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么此时chunkGraphInit的数据设置成了这个样子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">chunkGraphInit： <span class="hljs-title class_">Map</span>&#123;
&#123;chunkGroup-index, [<span class="hljs-variable language_">module</span>-index]&#125;,
&#123;chunkGroup-main,  [<span class="hljs-variable language_">module</span>-main] &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时chunkGraph内部_modules、_chunks内部数据是这个样子的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">_modules： <span class="hljs-title class_">Map</span>&#123;
<
<span class="hljs-variable language_">module</span>-index, 
<span class="hljs-attr">chunkGraphModule</span>:&#123;
<span class="hljs-attr">chunks</span>: [],
<span class="hljs-attr">entryInChunks</span>: [chunk-index]
&#125;
>,
<
<span class="hljs-variable language_">module</span>-main, 
<span class="hljs-attr">chunkGraphModule</span>:&#123;
<span class="hljs-attr">chunks</span>: [],
<span class="hljs-attr">entryInChunks</span>: [chunk-main]
&#125;
>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">_chunks： <span class="hljs-title class_">Map</span>&#123;
<
chunk-index, 
<span class="hljs-attr">chunkGraphChunk</span>:&#123;
modules： [],
<span class="hljs-attr">entreyModules</span>: [<span class="hljs-variable language_">module</span>-index]
&#125;
>,
<
chunk-main, 
<span class="hljs-attr">chunkGraphChunk</span>:&#123;
modules： [],
<span class="hljs-attr">entreyModules</span>: [<span class="hljs-variable language_">module</span>-main]
&#125;
>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再补充一个知识：chunkGroup【给chunk分组的对象。为什么要给chunk分组这是一个值得思考的问题？以后有机会再出个文章分析一下】
此时的Compilation中chunkGroups的数据</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">chunkGroups</span>: [
chunkGroup-index：&#123;
<span class="hljs-attr">chunks</span>: [chunk-index],
<span class="hljs-attr">_children</span>: [],
<span class="hljs-attr">_parents</span>: [],
&#125;,
chunkGroup-<span class="hljs-attr">main</span>: &#123;
<span class="hljs-attr">chunks</span>: [chunk-main],
<span class="hljs-attr">_children</span>: [],
<span class="hljs-attr">_parents</span>: [],
&#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了起点数据后，此时将进入下一个阶段...</p>
<h1 data-id="heading-6">构建完整chunkGraph</h1>
<p>这个阶段也可以叫：通过入口拓展来完善ChunkGraph。</p>
<p>前面我们已经得到了两个非常重要的数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">chunkGraphInit： <span class="hljs-title class_">Map</span>&#123;
<chunkGroup-index, [<span class="hljs-variable language_">module</span>-index]>,
<chunkGroup-main,  [<span class="hljs-variable language_">module</span>-main]>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">``</span><span class="hljs-string">`javascript
// ChunkGraph的属性
_modules： Map&#123;
<
module-index, 
chunkGraphModule:&#123;
chunks: [],
entryInChunks: [chunk-index]
&#125;
>,
<
module-main, 
chunkGraphModule:&#123;
chunks: [],
entryInChunks: [chunk-main]
&#125;
>,
&#125;

_chunks： Map&#123;
<
chunk-index, 
chunkGraphChunk:&#123;
modules： [],
entreyModules: [module-index]
&#125;
>,
<
chunk-main, 
chunkGraphChunk:&#123;
modules： [],
entreyModules: [module-main]
&#125;
>,
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>聪明伶俐的你，已经想到接下来就是通过入口module顺藤摸瓜找到其他module添加进chunk中，并且module也记录着他属于哪些chunk的信息收集过程。也就是ChunkGraph的信息不断在完善的过程。</p>
<p>接下来从源码的角度来解析这一过程的实现原理，完成该功能的核心函数buildChunGraph(Compilation, chunkGraphInit)。一起来看看buildChunkGraph函数都干了些啥吧。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cc957ddbe974706b21401a12309ee0f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
内部调用visitModules()函数开始对module顺藤摸瓜：</p>
<p>visitModules()函数内部定义了queue队列，遍历chunkGraphInit中的入口modules，将moduel转换为queueItem压入到队列中【此时的queueItem的action=1，action控制着queueItem的处理流程】。</p>
<p>此时的queueItem是有了module与chunk等关键信息的了。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/825190c017b147d0a33ace710abbffcc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时遍历queue队列，弹出queueItem处理，处理queueItem的过程相对繁琐。大致可总结为：</p>
<ul>
<li>调用chunkGraph.connectChunkAndModule(chunk, module)【构建ChunkGraph的_modules、_chunks信息（即确定了module属于哪些chunk，chunk有哪些module）】</li>
<li>将queueItem的action改为5，重新压回到queueItem</li>
<li>找到module引入了哪些module，转化为queueItem【action=1】，再压入到queue队列中</li>
</ul>
<p>简单总结：从入口module开始，找到依赖的modules不断压入到队列中去处理。直到最后没有了新的依赖module压入队列。</p>
<p>用一个流程图来更好的理解这一过程：</p>
<p><em>tips: 当有异步依赖的时候才会走action=4</em>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d085cbd6250400b809e8d0ad624b8bb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>处理queueItem的那块代码也贴出来看看，非常值得学习的一种控制逻辑设计：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96bcb0c317154a9491a14ad24283aae7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
上面这部分逻辑很难消化，因为确实看的时候感到有点吃力。但是当我们去描绘出queue队列在处理过程中如何变化的时候，感觉又好理解了许多。
下面以这个依赖结构为例子，我们来看看queue的数据变化情况：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a129a55f8c864601bd60daa75b64e4ea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
来看看queue一开始只以入口module转化为queueItem【此时的queueItem的action=1】的情况吧：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c252f1780a16446d897364be0bda5364~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
此时的queue只有两个消息：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">queue</span>: [
queue-app：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
queue-index：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后弹出queue-index，此时queue只剩下queue-app：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">queue</span>: [
queue-app：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后开始处理queue-index:</p>
<ul>
<li>将module-index, chunk-index添加进chunkGraph的_modules,_chunks</li>
<li>将弹出的queue-index的action设为5，然后重新压入queue</li>
</ul>
<p>此时queue队列的数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">queue</span>: [
queue-app：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
queue-index：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">5</span> ...&#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继续处理queue-index:</p>
<ul>
<li>找到module-index的依赖 module-a 、 module-b。转化为queueItem【action=1】并压入队列</li>
</ul>
<p>此时queue队列的数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">queue</span>: [
queue-app：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
queue-index：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">5</span> ...&#125;,
queue-b：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
queue-a：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里对queue-index的处理已经完成。
接着回到循环，弹出队列queue-a，
然后开始处理queue-a:</p>
<ul>
<li>将module-a, chunk-a添加进chunkGraph的_modules,_chunks</li>
<li>将弹出的queue-a的action设为5，然后重新压入queue</li>
</ul>
<p>此时queue队列的数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">queue</span>: [
queue-app：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
queue-index：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">5</span> ...&#125;,
queue-b：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">1</span> ...&#125;,
queue-a：&#123;<span class="hljs-attr">action</span>:<span class="hljs-number">5</span> ...&#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>...这里就不凑字数了，queue-a又找到了module-a1,又压入队列........</p>
<p>action等于5的时候就有给队列添加的可能了，所以queue最终会被全部消费掉。</p>
<p>这里直接放一张整理过程中的笔记，略显凌乱。但还是有用的：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23d7b09d45b64602a245dc9ed50aa26e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
时光飞逝，到这一步ChunkGraph已经将所有的module都分配到对应的chunk。但关于分包的逻辑此时还没结束，因为还有个令人又爱又恨的SplitChunkPlugin插件，它会对目前的ChunkGraph再进一步优化，这个分包插件在webpack4开始内置支持！</p>
<p>配置好SplitChunkPlugin一定能让你的项目更上一层楼。</p>
<p>下一篇文章准备写关于SplitChunkPlugin插件优化分包的原理。又是难啃的一篇文章。</p>
<pre><code class="hljs language-handlebars copyable" lang="handlebars">文章结尾分享一下关于阅读源码的一些心得：
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>抓住重点，别被带偏：</strong> 源码中会有很对属性函数会让你看的一头雾水，切记分清主次，把时间集中在核心代码中。可以去参考其他优秀的文章提到的流程、函数。帮助自己找到核心代码！</li>
<li><strong>画流程图，整理流程：</strong> 边看边画，有效避免看了东忘了西的尴尬场面，浪费时间回头再看</li>
<li><strong>看数据源：</strong> 有些关键的对象/属性如ChunkGraph、ChunkModule、Compilation、Module等，在调试的时候可以查看这些对象真实记录的数据，有助于理解该对象，并且能够反推一些复杂的函数的逻辑作用。</li>
</ul>
<p>感谢阅读~ 能坚持看到这里的看官点赞支持一下吧！❤❤❤❤❤</p></div>  
</div>
            