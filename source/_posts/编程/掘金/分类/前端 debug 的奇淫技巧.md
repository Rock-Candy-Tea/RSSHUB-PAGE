
---
title: '前端 debug 的奇淫技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cca396298d3642d69ce923502baa2420~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 18:25:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cca396298d3642d69ce923502baa2420~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>为什么要写这个文章呢？其实发现很多同学对一些很简单又有效的 debug 手段都不太了解，找 bug 的方式都不是很高效，导致最终 bug 找不到或者走了很多弯路。</p>
<h2 data-id="heading-0">Devtools</h2>
<p>作为前端开发，chrome 的 devtools 一定不陌生，下面讲一讲 devtools 里面 debug 的一些思路。</p>
<h2 data-id="heading-1">breakpoint</h2>
<p>其中断点是最最经常用到的，但很多同学都只用过默认的 breakpoint，其实还有其他两种。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cca396298d3642d69ce923502baa2420~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">breakpoint</h3>
<p>当代码执行到该行代码时暂停<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/152872883c9042f18ca427a0708760ae~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">conditional breakpoint</h3>
<p>条件断点，当表达式为 true 时才会暂停，下图是当变量<code>a === 1</code>时才暂停。经典应用场景是当 bug 是偶现时，你需要知道入参什么的正不正常，你可以打一个你认为不正常的条件断点，看看是谁调用的。PS：值得注意的是，如果你的表达式报错，那这个断点就会不生效，需要甄别到底是报错引起的断点没进入还是真的没进入。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2efc1e3d0354dd5972f56dec2529544~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">logpoint</h3>
<p>日志断点，当代码执行到这里时，会在控制台输出你的表达式，不会暂停代码执行，下图是将 a 输出到控制台的例子。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68edf4d9e3e3448bbbc9baeca91602f9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
值得注意的是，当你在调试带有 sroucemap 的压缩后的代码，可能会产生你看到的变量名和实际运行时拿到的变量名不一样，此时可以在右侧 scope 找到你想要的真实变量名或者在 source 面板 disable 掉 js 的 sourcemap 后再打断点。</p>
<h2 data-id="heading-5">Performance</h2>
<p>当你做了一些操作，不确定到底执行了什么代码时，可以利用 performance 来捕获到底什么样的代码被执行了，结合你的具体情况，有时候也会找到线索，有意想不到的收获。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1f865efe87e4fd5b08f3163c09de631~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">是谁动了我的代码</h1>
<p>经典面试题，如何找到是谁阻止了冒泡，直接在控制台输入下面的代码即可。经常用于寻找我绑定的事件为什么没有被触发。</p>
<pre><code class="hljs language-C copyable" lang="C">var tmpStopPropagation = MouseEvent.prototype.stopPropagation;

MouseEvent.prototype.stopPropagation = function(...args) &#123;
  console.trace(<span class="hljs-string">'stopPropagation'</span>);
  tmpStopPropagation.call(<span class="hljs-keyword">this</span>, ...args);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面这个例子是找到到底是谁对容器进行了滚动，比如我们遇到一些页面跳动或者抖动的场景，寻找到底是谁滚动了容器，当然滚动还有其他方法会触发，比如<code>scrollIntoView</code>，但思路都是一样的，代理这个方法即可。</p>
<pre><code class="hljs language-C copyable" lang="C">var tmpScrollTop = element.scrollTop;

Object.defineProperty(element, <span class="hljs-string">'scrollTop'</span>, &#123;
  get: function() &#123;
    <span class="hljs-keyword">return</span> tmpScrollTop;
  &#125;,
  <span class="hljs-built_in">set</span>: function(newVal) &#123;
    console.trace(<span class="hljs-string">'scrollTop'</span>);
    tmpScrollTop = newVal;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">setTimeout</h1>
<p>如果我们在想要打断点的时候依赖鼠标或者键盘操作，如果你去 source 面板去点击暂定，那我的现场就没有了，那下面的代码会帮你解决问题。</p>
<pre><code class="copyable">setTimeout(() => &#123;debugger;&#125;, 4000);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有这样一种 case，比如我期望在我鼠标移动时看看某个变量值是多少，此时不要再傻傻的在代码里面添加 console.log，直接运行下面的代码，可以实时看到你想要的变量。这个方法比较像 logpoint，不过不需要找源码去打断点，各有各的应用场景。</p>
<pre><code class="copyable">setTimeout(() => &#123;console.log(yourInstance.getSomeValue());&#125;, 100);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">SSR</h1>
<p>当你想要 debug 某个页面上 SSR 渲染的样式时，可以禁用掉 js 的执行，具体操作是打开 devtools 的 source 面板，然后 cmd+p，输入「>disable javascript」，按回车，然后刷新页面，你的页面就是纯 SSR 状态了。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fa042ac959c49bfa7f552af42ce43ef~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">二分法</h1>
<p>这个是终极 debug 方法，很少会用到，但也很通俗易懂，有一定应用场景。当你发现在某个版本之后你的代码出了问题，但又各种找不到思路，我只知道在 A 版本没问题，B 版本就有问题了，或者代码突然出了问题，又不知道是依赖了谁出的问题，就可以用这种方法。总的思路就是「控制变量」，你可以在代码中批量注释一些代码，然后验证问题还有没有，如果还就的话就继续注释，没有的话问题就出在被注释的代码里，比较像算法中的二分法。</p>
<h1 data-id="heading-10">总结</h1>
<p>如何 debug 还有更多的技巧，我这里写的也只是一部分，如果有其他更好的思路欢迎留言。</p>
<p>欢迎关注「 字节前端 ByteFE 」</p>
<p>简历投递联系邮箱「<a href="https://link.juejin.cn/?target=mailto%3Atech%40bytedance.com" target="_blank" title="mailto:tech@bytedance.com" ref="nofollow noopener noreferrer">tech@bytedance.com</a>」</p></div>  
</div>
            