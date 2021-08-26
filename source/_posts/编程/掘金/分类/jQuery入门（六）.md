
---
title: 'jQuery入门（六）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5574'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 18:15:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=5574'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第26天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a> Promise</p>
<h3 data-id="heading-0">ajaxError</h3>
<ul>
<li>
<p>任意一个请求在 <strong>失败</strong> 的时候就会触发这个函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$(<span class="hljs-built_in">window</span>).ajaxError(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'有一个请求失败了'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-1">ajaxComplete</h3>
<ul>
<li>
<p>任意一个请求在 <strong>完成</strong> 的时候就会触发这个函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$(<span class="hljs-built_in">window</span>).ajaxComplete(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'有一个请求完成了'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-2">ajaxStop</h3>
<ul>
<li>
<p>任意一个请求在 <strong>结束</strong> 的时候就会触发这个函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$(<span class="hljs-built_in">window</span>).ajaxStop(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'有一个请求结束了'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-3">jQuery 的多库共存</h2>
<ul>
<li>
<p>我们一直在使用 <code>jQuery</code>，都没有什么问题</p>
</li>
<li>
<p>但是如果有一天，我们需要引入一个别的插件或者库的时候</p>
</li>
<li>
<p>人家也向外暴露的是 <code>$</code> 获取 <code>jQuery</code></p>
</li>
<li>
<p>那么，我们的 <code>jQuery</code> 就不能用了</p>
</li>
<li>
<p>那么这个时候，<code>jQuery</code> 为我们提供了一个多库并存的方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这个方法可以交还 jQuery 命名的控制权</span>
jQuery.noConflict()

<span class="hljs-comment">// 上面代码执行完毕以后 $ 这个变量就不能用了</span>
<span class="hljs-comment">// 但是 jQuery 可以使用</span>
<span class="hljs-built_in">console</span>.log($) <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(jQuery) <span class="hljs-comment">// 可以使用</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>完全交出控制权</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这个方法可以交并且传递一个 true 的时候，会完全交出控制权</span>
jQuery.noConflict(<span class="hljs-literal">true</span>)

<span class="hljs-comment">// 上面代码执行完毕以后 $ 这个变量就不能用了</span>
<span class="hljs-comment">// jQuery 这个变量也不能用了</span>
<span class="hljs-built_in">console</span>.log($) <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(jQuery) <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>更换控制权</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 可以用一个变量来接受返回值，这个变量就是新的控制权</span>
<span class="hljs-keyword">var</span> aa = jQuery.noConflict(<span class="hljs-literal">true</span>)

<span class="hljs-comment">// 接下来就可以把 aa 当作 jQuery 向外暴露的接口使用了</span>
aa(<span class="hljs-string">'div'</span>).click(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我被点击了'</span>) &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-4">JQuery 的插件扩展</h2>
<ul>
<li><code>jQuery</code> 确实很好很强大</li>
<li>但是也有一些方法是他没有的，我们的业务需求中有的时候会遇到一些它里面没有的方法</li>
<li>那么我们就可以给他扩展一些方法</li>
</ul>
<h3 data-id="heading-5">扩展给他自己本身</h3>
<ul>
<li>
<p>扩展给自己本身使用 <code>jQuery.extend</code> 这个方法</p>
</li>
<li>
<p>扩展完后的内容只能用 <code>$</code> 或者 <code>jQuery</code> 来调用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// jQuery.extend 接受一个参数，是一个对象，对象里面是我们扩展的方法</span>
jQuery.extend(&#123;
    <span class="hljs-attr">max</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...n</span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.max.apply(<span class="hljs-literal">null</span>, n) &#125;,
    <span class="hljs-attr">min</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...n</span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.min.apply(<span class="hljs-literal">null</span>, n) &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>扩展完毕我们就可以使用了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> max = $.max(<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">6</span>, <span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.log(max) <span class="hljs-comment">// 6</span>
<span class="hljs-keyword">const</span> min = $.min(<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">6</span>, <span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.log(min) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-6">扩展给元素集</h3>
<ul>
<li>
<p>扩展完毕以后给元素的集合使用</p>
</li>
<li>
<p>也就是我们用 <code>$('li')</code> 这样的选择器获取到的元素集合来使用</p>
</li>
<li>
<p>使用 <code>jQuery.fn.extend()</code> 方法来扩展</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// jQuery.fn.extend() 接受一个参数，是一个对象，对象里面是我们扩展的方法</span>
jQuery.fn.extend(&#123;
    <span class="hljs-attr">checked</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// return 关键字是为了保证链式编程</span>
        <span class="hljs-comment">// 后面的代码才是业务逻辑</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.each(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">this</span>.checked = <span class="hljs-literal">true</span> &#125;)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>扩展完毕我们就可以使用了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 靠元素集合来调用</span>
$(<span class="hljs-string">'input[type=checkbox]'</span>).checked()
<span class="hljs-comment">// 执行完毕之后，所有的 复选框 就都是选中状态了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            