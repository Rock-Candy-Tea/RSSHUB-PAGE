
---
title: 'Web History Api 记录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6502'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 05:27:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=6502'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、 常用方法</h2>
<h3 data-id="heading-1">1.1 history.back()</h3>
<p>在 <code>history</code> 中向后跳转，和点击浏览器回退按钮的效果相同。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.history.back();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 history.forward()</h3>
<p>在 <code>history</code> 中向前跳转，和点击浏览器前进按钮的效果相同。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.history.forward();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.3 history.go()</h3>
<p>在 <code>history</code> 中跳转到指定的一个点，点的位置通过与当前页面相对位置来标志 (当前页面的相对位置标志为0)，前进为正，后退为负。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 向后移动一个页面 ，等同于调用 back()</span>
<span class="hljs-built_in">window</span>.history.go(-<span class="hljs-number">1</span>);
<span class="hljs-comment">// 向前移动一个页面 ，等同于调用 forward()</span>
<span class="hljs-built_in">window</span>.history.go(<span class="hljs-number">1</span>);

<span class="hljs-comment">// 向后/前移动两个页面</span>
<span class="hljs-built_in">window</span>.history.go(-<span class="hljs-number">2</span>);
<span class="hljs-built_in">window</span>.history.go(<span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可以使用 <code>window.history.length</code> 来确定当前历史堆栈中页面的数量</p>
</blockquote>
<h2 data-id="heading-4">二、pushState 和 replaceState</h2>
<p><code>pushState()</code> 和 <code>replaceState()</code> 会修改浏览器的 URL，但是浏览器并不会立即加载这个 URL 对应的页面，即改变 URL 而不刷新页面。</p>
<h3 data-id="heading-5">2.1 history.pushState()</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.history.pushState(state, title, url);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数说明：</p>
<ul>
<li><code>state</code>: 一个与添加的记录相关联的状态对象，主要用于 <code>popstate</code> 事件。该事件触发时，该对象会传入回调函数。也就是说，浏览器会将这个对象序列化以后保留在本地，重新载入这个页面的时候，可以拿到这个对象。如果不需要这个对象，此处可以填 null。</li>
<li><code>title</code>: 新页面的标题。但是，现在所有浏览器都忽视这个参数，所以这里可以填空字符串。</li>
<li><code>url</code>: 新的网址，必须与当前页面处在同一个域。浏览器的地址栏将显示这个网址。</li>
</ul>
<p>假定当前网址是 <a href="http://localhost:8000/1.html" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8000/1.html</a>  使用 pushState() 方法在浏览记录（history 对象）中添加一个新记录。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> stateObj = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span> &#125;;
history.pushState(stateObj, <span class="hljs-string">'page 2'</span>, <span class="hljs-string">'2.html'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加新记录后，浏览器地址栏立刻显示 <a href="http://localhost:8000/2.html" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8000/2.html</a> ， 但并不会跳转到 <code>2.html</code>，甚至也不会检查 <code>2.html</code> 是否存在，它只是成为浏览历史中的最新记录。这时，在地址栏输入一个新的地址<code>( baidu.com )</code>，然后点击了倒退按钮，页面的 URL 将显示 <code>2.html</code>；你再点击一次倒退按钮，URL 将显示 <code>1.html</code>。</p>
<p>总之，<code>pushState()</code> 方法不会触发页面刷新，只是导致 history 对象发生变化，地址栏会有反应。</p>
<p>使用该方法之后，就可以用 <code>history.state</code> 属性读出状态对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> stateObj = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span> &#125;;
history.pushState(stateObj, <span class="hljs-string">'page 2'</span>, <span class="hljs-string">'2.html'</span>);
<span class="hljs-built_in">console</span>.log(history.state); <span class="hljs-comment">// &#123;foo: "bar"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.2 history.replaceState()</h3>
<p><code>replaceState()</code> 方法用来修改 history 对象的当前记录，其他都与 <code>pushState()</code> 方法一模一样。</p>
<h2 data-id="heading-7">三、popstate 事件</h2>
<p>每当同一个文档的浏览历史（即 <code>history</code> 对象）出现变化时，就会触发 <code>popstate</code> 事件。</p>
<blockquote>
<p>注意，仅仅调用 <code>pushState()</code> 方法或 <code>replaceState()</code> 方法 ，并不会触发该事件，只有用户点击浏览器倒退按钮和前进按钮，或者使用 JavaScript 调用 <code>history.back()</code>、<code>history.forward()</code>、<code>history.go()</code> 方法时才会触发。另外，该事件只针对同一个文档，如果浏览历史的切换，导致加载不同的文档，该事件也不会触发。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.onpopstate = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'location: '</span> + <span class="hljs-built_in">document</span>.location);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'state: '</span> + <span class="hljs-built_in">JSON</span>.stringify(event.state));
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回调函数的参数是一个 <code>event</code> 事件对象，它的 <code>state</code> 属性指向 <code>pushState</code> 和 <code>replaceState</code> 方法为当前 URL 所提供的状态对象（即这两个方法的第一个参数）。</p>
<h2 data-id="heading-8">四、参考</h2>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/History_API" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li><a href="http://javascript.ruanyifeng.com/bom/history.html" target="_blank" rel="nofollow noopener noreferrer">javascript.ruanyifeng.com/bom/history…</a></li>
</ul></div>  
</div>
            