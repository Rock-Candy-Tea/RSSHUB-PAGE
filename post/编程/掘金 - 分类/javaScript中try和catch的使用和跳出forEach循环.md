
---
title: javaScript中try和catch的使用和跳出forEach循环
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 17:21:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f85da1f89d24f2db3c627fa330e5473~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1，前言</h1>
<hr>
<p>有时项目中处理数据的时候，会存在数据有误，或者为空...等等问题而报错，由于<code>javaScript</code>是单线程，代码是自上而下放到执行栈中执行，如果某一段报错了，后面的代码全都不会执行。为了避免这种情况发生，我们的<code>try</code>和<code>catch</code>就派上用场了。</p>
<h1 data-id="heading-1">2，语法</h1>
<hr>
<p><strong>完整语法</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span> &#123;
    tryCode - 尝试执行的代码块
&#125;
<span class="hljs-keyword">catch</span>(error) &#123;
    catchCode - 捕获错误的代码块
&#125;
<span class="hljs-keyword">finally</span> &#123;
    finallyCode - 无论 <span class="hljs-keyword">try</span> / <span class="hljs-keyword">catch</span> 结果如何都会执行的代码块
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般我们只需要用到<code>try</code>和<code>catch</code>，下面是几个例子。</p>
<p><strong>demo数据</strong>（下面的例子都是用这个数据）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = [
  &#123;
    <span class="hljs-attr">id</span>:<span class="hljs-string">'001'</span>,
    <span class="hljs-attr">title</span>:<span class="hljs-string">'沙漠中怎么会有泥鳅'</span>,
    <span class="hljs-attr">array</span>:[
      &#123;
        <span class="hljs-attr">age</span>:<span class="hljs-number">18</span>
      &#125;
    ]
  &#125;,
  &#123;
    <span class="hljs-attr">id</span>:<span class="hljs-string">'002'</span>,
    <span class="hljs-attr">title</span>:<span class="hljs-string">'话说完飞过一只海鸥'</span>,
    <span class="hljs-attr">array</span>:[
      &#123;
        <span class="hljs-attr">age</span>:<span class="hljs-number">17</span>
      &#125;
    ]
  &#125;,
  &#123;
    <span class="hljs-attr">id</span>:<span class="hljs-string">'003'</span>,
    <span class="hljs-attr">title</span>:<span class="hljs-string">'大峡谷的风呼啸而过'</span>,
    <span class="hljs-attr">array</span>:[
      &#123;
        <span class="hljs-attr">age</span>:<span class="hljs-number">21</span>
      &#125;
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2.1，基本使用方法</h2>
<p>在这里我们没有定义过param变量，通过console.log打印时，javaScript会抛出一个错误。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span>&#123;
  <span class="hljs-built_in">console</span>.log(param)
&#125;
<span class="hljs-keyword">catch</span>(error)&#123;
  <span class="hljs-built_in">console</span>.error(error)
&#125;;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"如果看见了这段话说明代码没有被报错所阻塞"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="控制台" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f85da1f89d24f2db3c627fa330e5473~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">2.2，自定义报错信息</h2>
<p>配合<code>throw new Error</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span>&#123;
  obj.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">if</span>(item.id === <span class="hljs-string">'002'</span>)&#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'id不能等于002'</span>);
    &#125;
  &#125;);
&#125;
<span class="hljs-keyword">catch</span>(error)&#123;
  <span class="hljs-built_in">console</span>.error(error)
&#125;;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"如果看见了这段话说明代码没有被报错所阻塞"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="控制台" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa1abd91692b4dd4abe96bb84b1ccae4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">3，跳出forEach循环</h1>
<hr>
<p><code>forEach</code>不能使用<code>break</code>和<code>continue</code>这两个关键字，本身无法跳出循环，也不能像普通<code>for</code>循环一样使用<code>return</code>跳出，必须遍历所有的数据才能结束。</p>
<h2 data-id="heading-5">3.1，跳出forEach</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span>&#123;
  obj.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`当前id：<span class="hljs-subst">$&#123;item.id&#125;</span>`</span>)
    <span class="hljs-keyword">if</span>(item.id === <span class="hljs-string">'002'</span>)&#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'id等于002，跳出循环'</span>);
    &#125;
  &#125;);
&#125;
<span class="hljs-keyword">catch</span>(error)&#123;
  <span class="hljs-built_in">console</span>.error(error)
&#125;;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"如果看见了这段话说明代码没有被报错所阻塞"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="控制台" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26815c2321fa4f7d99167435158fad14~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">3.2，跳出双层forEach</h2>
<p>跳出了第二层循环，第一层循环继续执行；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span>&#123;
  obj.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`第一层forEach循环：<span class="hljs-subst">$&#123;item.id&#125;</span>`</span>);
    <span class="hljs-keyword">try</span>&#123;
      item.array.forEach(<span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
        <span class="hljs-keyword">if</span>(val.age < <span class="hljs-number">18</span>)&#123;
          <span class="hljs-keyword">throw</span>  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'年龄不能小于18岁'</span>);
        &#125;
      &#125;)
    &#125;<span class="hljs-keyword">catch</span>(error)&#123;
      <span class="hljs-built_in">console</span>.error(error)
    &#125;
  &#125;)
&#125;<span class="hljs-keyword">catch</span>(error)&#123;
  <span class="hljs-built_in">console</span>.log(error)
&#125;;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"如果看见了这段话说明代码没有被报错所阻塞"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="控制台" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e249f448a28476686fd8a135caca0db~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>如果看了觉得有帮助的，我是@鹏多多，欢迎 点赞 关注 评论；
END</strong></p>
<p><a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=Rik8--eP5pNr5CQawsb5PLXx1RiX205I&jump_from=webapi" rel="nofollow noopener noreferrer"><img border="0" alt="面向百度编程" title="面向百度编程" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01b0c5418e55455cb655aa27c3c9d20d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></a></p>
<p><code>往期文章</code></p>
<ul>
<li><a href="https://juejin.cn/post/6937175590302646308" target="_blank">微信小程序自定义Tabbar，附详细源码</a></li>
<li><a href="https://juejin.cn/post/6921527102273650695" target="_blank">细数JS中实用且强大的操作符&运算符</a></li>
<li><a href="https://juejin.cn/post/6918606560881033230" target="_blank">微信小程序API交互的自定义封装</a></li>
<li><a href="https://juejin.cn/post/6918983173770575880" target="_blank">微信小程序request请求的封装</a></li>
</ul>
<p><code>个人主页</code></p>
<ul>
<li><a href="https://blog.csdn.net/pdd11997110103?spm=1010.2135.3001.5421" target="_blank" rel="nofollow noopener noreferrer">CSDN</a></li>
<li><a href="https://github.com/pdd11997110103" target="_blank" rel="nofollow noopener noreferrer">GitHub</a></li>
<li><a href="https://www.jianshu.com/u/b7a8536bff06" target="_blank" rel="nofollow noopener noreferrer">简书</a></li>
<li><a href="https://www.cnblogs.com/-pdd/" target="_blank" rel="nofollow noopener noreferrer">博客园</a></li>
<li><a href="https://juejin.cn/user/747323639737191" target="_blank">掘金</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            