
---
title: 'ES 拾遗之赋值操作与原型链查找'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2b4c994d0844ae6b0a072259f701267~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 01:25:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2b4c994d0844ae6b0a072259f701267~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">问题</h2>
<p>这两天在排查一个 <a href="https://github.com/umijs/qiankun/issues/1121" target="_blank" rel="nofollow noopener noreferrer">qiankun 的 bug</a> 时，发现了一个我无法解释的 js 问题，这可要了我的命。<br>
<br>略去一切细枝末节，我们直接先来看问题。<br>假如有这么一段代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-string">'use strict'</span>;
  
  <span class="hljs-keyword">const</span> boundFn = <span class="hljs-built_in">Function</span>.prototype.bind.call(OfflineAudioContext, <span class="hljs-built_in">window</span>);
  <span class="hljs-built_in">console</span>.log(boundFn.hasOwnProperty(boundFn, <span class="hljs-string">'prototype'</span>));
  boundFn.prototype = OfflineAudioContext.prototype;
  <span class="hljs-built_in">console</span>.log(boundFn.hasOwnProperty(boundFn, <span class="hljs-string">'prototype'</span>));
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设我们已知，函数通过 bind 调用后，返回的新的 boundFn 是一定不会有 prototype 的。<br>
<br>那么打印结果就应该是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-literal">false</span>
<span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 boundFn 不具备自有属性 'prototype'，所以在经过 <code>boundFn.prototype = OfflineAudioContext.prototype</code> 的赋值操作后，会为其创建一个新的自有属性 'prototype'，其值为 <code>OfflineAudioContext.prototype</code>。一切都在情理之中。<br>
<br>但你真的把这段代码粘到 chrome 控制台跑一下就会发现，报错了😑<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2b4c994d0844ae6b0a072259f701267~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>从报错信息很容易判断，我们在尝试给一个 readonly 的属性做赋值，但关键是，prototype 这个属性在 boundFn 上压根不存在呀！<br>我们知道，对象的属性赋值操作的基本逻辑是这样的：</p>
<ol>
<li>如果对象上该属性不存在，则创建一个自有属性并赋值</li>
<li>如果对象上该属性已存在，则修改该属性的值，修改过程会触发该属性上的 data descriptor（writable 配置）检测或 accessor descriptor (setter 配置) 的调用。</li>
</ol>
<p>毫无疑问上面代码走的应该是第一个逻辑分支，完全不应该报错才对。<br>
<br>起初我还以为是浏览器兼容问题，然后尝试过几个浏览器之后，发现都是报错😑<br>
<br>排查的过程中发现，OfflineAudioContext.prototype 本身是 readonly 的<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0dba2b406ef444d8ed8b341816757fb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>但是这跟我们 boundFn.prototype 赋值有什么关系呢，即便我们把赋值操作改成：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">boundFn.prototype = <span class="hljs-number">123</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>报错还是会照旧。<br>继续查，发现 boundFn 的原型链上是有 prototype 的：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e31f34a03307498ca55003e24d549258~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>而且原型链上的这个 prototype 也是 readonly 的：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c61c2a2156e14064b2af505df6a2f45e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>但是我们一个写操作跟原型链有啥关系呢，不是读操作时才会按原型链查找吗？？？<br></p>
<h2 data-id="heading-1">ES Spec 追踪</h2>
<p>各种尝试之后无果，这时候只能祭出 ecmascript spec，看看能不能从里面找到蛛丝马迹了😑<br>
<br>搜索找到赋值操作(assignment)相关的 <a href="https://262.ecma-international.org/5.1/#sec-11.13.1" target="_blank" rel="nofollow noopener noreferrer">spec 说明</a>：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d91ffeff7064021beeb240ee9bdd614~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>如果有过读 ecmascript spec 经验的话，会找到关键步骤在第 5 步 <a href="https://262.ecma-international.org/5.1/#sec-8.7.2" target="_blank" rel="nofollow noopener noreferrer">PutValue</a>：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97d3ded95a8241928971f5ddc1acfd28~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>我们这个场景里，PutValue 的操作会沿着 4.a.false 的路径执行。即 put 对应的调用为 <code>base.[[Put]](reference name, W, true)</code>。<br>找到 <a href="https://262.ecma-international.org/5.1/#sec-8.12.5" target="_blank" rel="nofollow noopener noreferrer">[[Put]]</a> 的调用算法说明：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89cda5c3abb3415db83fb1a34c5d892f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>这里其实就能看到，如果我们走到了最后一步第6步的时候，实际上发生的事情就会是：<br><code>Object.defineProperty(O, P, &#123; writable: true, enumerable: true, configurable: true, value: V &#125;)</code>, 也就是我们会为对象创建一个新的属性并赋值，且这个属性是可枚举可修改的，符合我们之前的认知。<br>
<br>那其实我们就要看看，为什么流程没有走到第6步。<br>先看第一步里的 <a href="https://262.ecma-international.org/5.1/#sec-8.12.4" target="_blank" rel="nofollow noopener noreferrer">[[CanPut]]</a> 做了啥：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0087a5c00684d0d9359c700ee44b22e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>简单翻译下流程就是：</p>
<ol>
<li>查找自身属性的 descriptor</li>
<li>如果有则按照 descriptor 的规则判断</li>
<li>如果没有则看对象是否有原型</li>
<li>如果原型是 null 则直接根据对象是否可拓展返回结果</li>
<li>否则去原型链上查找属性</li>
<li>如果原型链上找不到，则直接根据对象是否可拓展返回结果</li>
<li>如果原型链上能找到，则记录查找后的值对应的 descriptor</li>
<li>如果记录的值是 accessor descriptor，那么就根据 setter 配置决定返回值</li>
<li>如果记录的值是 data descriptor，那么就根据是否和拓展或者是否 writable 来给出返回值</li>
</ol>
<p><br>其实到这里我们就能发现端倪了，关键点是这几步：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07798383cd25410f9500968866510952~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>这几步描述的实际就是，计算流程会一直去原型链上查找属性 P。<br>
<br>也就是说，即便我们是赋值操作，<strong>只要是对象属性的赋值，都会触发原型链的查找。</strong><br>
<br>那么回到上面那段代码，对应的计算流程就是：</p>
<ol>
<li>先触发了 boundFn 自身属性里查找 prototype 的操作</li>
<li>发现不存在 prototype，则去原型链上找</li>
<li>由于 boundFn 的原型指向了 BaseAudioContext，所以返回的实际是 BaseAudioContext.prototype</li>
<li>而 BaseAudioContext.prototype 的 writable 配置为 false</li>
<li>故 [[CanPut]] 操作返回了 false</li>
<li>返回 false 后就直接 throw 了一个 TypeError</li>
</ol>
<h2 data-id="heading-2">解法</h2>
<p>那么如果我们确实想给 boundFn 加一个自身属性 prototype 该怎么做呢？<br>其实我们只要找到不会触发原型链查找的修改方式就可以了：</p>
<pre><code class="hljs language-diff copyable" lang="diff"><span class="hljs-deletion">- boundFn.prototype = OfflineAudioContext.prototype;</span>
<span class="hljs-addition">+ Object.defineProperty(boundFn, 'prototype', &#123; value: OfflineAudioContext.prototype, enumerable: false, writable: true &#125;)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理就是 <a href="https://262.ecma-international.org/5.1/#sec-8.12.9" target="_blank" rel="nofollow noopener noreferrer">defineProperty API</a> 不会有 [[getProperty]] 这种触发原型链查找的调用：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/593824ad936340b583b8c5fa1942c72f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br></p>
<h2 data-id="heading-3">结论</h2>
<p>赋值（assignment）操作也会存在原型链查找逻辑，且是否可写也会遵循查找到的属性的 descriptor 规则。</p></div>  
</div>
            