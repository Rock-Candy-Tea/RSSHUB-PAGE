
---
title: 'React Diff 算法源码阅读笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/515393833b284f7288973a12a82dcb23~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 03:40:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/515393833b284f7288973a12a82dcb23~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文内容基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Ftree%2Fv17.0.0" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/tree/v17.0.0" ref="nofollow noopener noreferrer">React 17.0.0</a>，主要在 legacy mode 下针对 React-reconciler 来进行分析</p>
</blockquote>
<h2 data-id="heading-0">导读</h2>
<p>React Diff 的过程发生在 beginWork 内，每个节点被 Diff 的时机基本上都是在其父节点状态更新快结束后发生的，其关键函数是一个叫 reconcileChildren 的函数。所以下文均会使用 reconcileChildren 来代指 Diff 的发生。</p>
<p>reconcileChildren 不会直接涉及子节点的状态更新，只是 <strong>创建新 Fiber、复用旧 Fiber 、找到需要删除的无用旧 Fiber</strong>，然后生成一个得到一个最新状态的第一个子节点的 Fiber，然后在下一个 workLoop 中进行更细节的节点状态更新等。</p>
<h2 data-id="heading-1">ReconcileChildren</h2>
<blockquote>
<p>源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fv17.0.0%2Fpackages%2Freact-reconciler%2Fsrc%2FReactChildFiber.old.js%23L1274" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/v17.0.0/packages/react-reconciler/src/ReactChildFiber.old.js#L1274" ref="nofollow noopener noreferrer">github.com/facebook/re…</a></p>
</blockquote>
<h3 data-id="heading-2">函数签名</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildFibers</span>(<span class="hljs-params">
returnFiber: Fiber, <span class="hljs-comment">// WIP 的 Fiber 节点</span>
currentFirstChild: Fiber | <span class="hljs-literal">null</span>, <span class="hljs-comment">// Current 节点的第一个子节点的 Fiber</span>
newChild: <span class="hljs-built_in">any</span>, <span class="hljs-comment">// 最新的子节点的 ReactElement</span>
lanes: Lanes, <span class="hljs-comment">// 更新优先级，在本文中无需在意</span>
</span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">逻辑流程图</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/515393833b284f7288973a12a82dcb23~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">小节</h3>
<p>ReconcileChildren 主要会通过新的子节点的 ReactElement 类型来将逻辑分流，分别到其他自逻辑进行详细的 Diff，下面会进行一一的罗列。</p>
<h2 data-id="heading-5">reconcileSingleElement</h2>
<blockquote>
<p>源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fv17.0.0%2Fpackages%2Freact-reconciler%2Fsrc%2FReactChildFiber.old.js%23L1135" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/v17.0.0/packages/react-reconciler/src/ReactChildFiber.old.js#L1135" ref="nofollow noopener noreferrer">github.com/facebook/re…</a></p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bb31ff607bf41d19014ddab22047eef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">reconcileSinglePortal</h2>
<blockquote>
<p>源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fv17.0.0%2Fpackages%2Freact-reconciler%2Fsrc%2FReactChildFiber.old.js%23L1235" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/v17.0.0/packages/react-reconciler/src/ReactChildFiber.old.js#L1235" ref="nofollow noopener noreferrer">github.com/facebook/re…</a></p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2272661ca9004ce7b56c8dfc205ea84e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">reconcileSingleTextNode</h2>
<blockquote>
<p>源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fv17.0.0%2Fpackages%2Freact-reconciler%2Fsrc%2FReactChildFiber.old.js%23L1111" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/v17.0.0/packages/react-reconciler/src/ReactChildFiber.old.js#L1111" ref="nofollow noopener noreferrer">github.com/facebook/re…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cad482e50d840da9eb03f6c7468d05b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">reconcileChildrenArray</h2>
<blockquote>
<p>源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fv17.0.0%2Fpackages%2Freact-reconciler%2Fsrc%2FReactChildFiber.old.js%23L771" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/v17.0.0/packages/react-reconciler/src/ReactChildFiber.old.js#L771" ref="nofollow noopener noreferrer">github.com/facebook/re…</a></p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f525a2ab5fd34a0cb273a78a75843c3d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">reconcileChildrenIterator</h2>
<blockquote>
<p>源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fblob%2Fv17.0.0%2Fpackages%2Freact-reconciler%2Fsrc%2FReactChildFiber.old.js%23L926" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/react/blob/v17.0.0/packages/react-reconciler/src/ReactChildFiber.old.js#L926" ref="nofollow noopener noreferrer">github.com/facebook/re…</a></p>
</blockquote>
<p>迭代器的 reconciler 方式与 reconcileChildrenArray 基本一致，只不过遍历方式等做了一些区分，便不再赘述了。</p></div>  
</div>
            