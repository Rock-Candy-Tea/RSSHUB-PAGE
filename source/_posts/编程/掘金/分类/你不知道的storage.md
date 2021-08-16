
---
title: '你不知道的storage'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9644'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 00:35:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=9644'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Storage 接口</h1>
<h2 data-id="heading-1">概述</h2>
<p>Storage 接口用于脚本在浏览器保存数据。两个对象部署了这个接口：<code>window.sessionStorage</code>和<code>window.localStorage</code>。</p>
<p><code>sessionStorage</code>保存的数据用于浏览器的一次会话（session），当会话结束（通常是窗口关闭），数据被清空；<code>localStorage</code>保存的数据长期存在，下一次访问该网站的时候，网页可以直接读取以前保存的数据。除了保存期限的长短不同，这两个对象的其他方面都一致。</p>
<p>保存的数据都以“键值对”的形式存在。也就是说，每一项数据都有一个键名和对应的值。所有的数据都是以文本格式保存。</p>
<p>这个接口很像 Cookie 的强化版，能够使用大得多的存储空间。目前，每个域名的存储上限视浏览器而定，Chrome 是 2.5MB，Firefox 和 Opera 是 5MB，IE 是 10MB。其中，Firefox 的存储空间由一级域名决定，而其他浏览器没有这个限制。也就是说，Firefox 中，<code>a.example.com</code>和<code>b.example.com</code>共享 5MB 的存储空间。另外，与 Cookie 一样，它们也受同域限制。某个网页存入的数据，只有同域下的网页才能读取，如果跨域操作会报错。</p>
<h2 data-id="heading-2">属性和方法</h2>
<p>Storage 接口只有一个属性。</p>
<ul>
<li><code>Storage.length</code>：返回保存的数据项个数。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'a'</span>);
<span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">'bar'</span>, <span class="hljs-string">'b'</span>);
<span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">'baz'</span>, <span class="hljs-string">'c'</span>);

<span class="hljs-built_in">window</span>.localStorage.length <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该接口提供5个方法。</p>
<h3 data-id="heading-3">Storage.setItem()</h3>
<p><code>Storage.setItem()</code>方法用于存入数据。它接受两个参数，第一个是键名，第二个是保存的数据。如果键名已经存在，该方法会更新已有的键值。该方法没有返回值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.sessionStorage.setItem(<span class="hljs-string">'key'</span>, <span class="hljs-string">'value'</span>);
<span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">'key'</span>, <span class="hljs-string">'value'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，<code>Storage.setItem()</code>两个参数都是字符串。如果不是字符串，会自动转成字符串，再存入浏览器。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.sessionStorage.setItem(<span class="hljs-number">3</span>, &#123; <span class="hljs-attr">foo</span>: <span class="hljs-number">1</span> &#125;);
<span class="hljs-built_in">window</span>.sessionStorage.getItem(<span class="hljs-string">'3'</span>) <span class="hljs-comment">// "[object Object]"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>setItem</code>方法的两个参数都不是字符串，但是存入的值都是字符串。</p>
<p>如果储存空间已满，该方法会抛错。</p>
<p>写入不一定要用这个方法，直接赋值也是可以的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 下面三种写法等价</span>
<span class="hljs-built_in">window</span>.localStorage.foo = <span class="hljs-string">'123'</span>;
<span class="hljs-built_in">window</span>.localStorage[<span class="hljs-string">'foo'</span>] = <span class="hljs-string">'123'</span>;
<span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'123'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Storage.getItem()</h3>
<p><code>Storage.getItem()</code>方法用于读取数据。它只有一个参数，就是键名。如果键名不存在，该方法返回<code>null</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.sessionStorage.getItem(<span class="hljs-string">'key'</span>)
<span class="hljs-built_in">window</span>.localStorage.getItem(<span class="hljs-string">'key'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>键名应该是一个字符串，否则会被自动转为字符串。</p>
<h3 data-id="heading-5">Storage.removeItem()</h3>
<p><code>Storage.removeItem()</code>方法用于清除某个键名对应的键值。它接受键名作为参数，如果键名不存在，该方法不会做任何事情。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">sessionStorage.removeItem(<span class="hljs-string">'key'</span>);
<span class="hljs-built_in">localStorage</span>.removeItem(<span class="hljs-string">'key'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Storage.clear()</h3>
<p><code>Storage.clear()</code>方法用于清除所有保存的数据。该方法的返回值是<code>undefined</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.sessionStorage.clear()
<span class="hljs-built_in">window</span>.localStorage.clear()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Storage.key()</h3>
<p><code>Storage.key()</code>方法接受一个整数作为参数（从零开始），返回该位置对应的键名。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.sessionStorage.setItem(<span class="hljs-string">'key'</span>, <span class="hljs-string">'value'</span>);
<span class="hljs-built_in">window</span>.sessionStorage.key(<span class="hljs-number">0</span>) <span class="hljs-comment">// "key"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合使用<code>Storage.length</code>属性和<code>Storage.key()</code>方法，可以遍历所有的键。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">window</span>.localStorage.length; i++) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">localStorage</span>.key(i));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">storage 事件</h2>
<p>Storage 接口储存的数据发生变化时，会触发 storage 事件，可以指定这个事件的监听函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'storage'</span>, onStorageChange);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监听函数接受一个<code>event</code>实例对象作为参数。这个实例对象继承了 StorageEvent 接口，有几个特有的属性，都是只读属性。</p>
<ul>
<li><code>StorageEvent.key</code>：字符串，表示发生变动的键名。如果 storage 事件是由<code>clear()</code>方法引起，该属性返回<code>null</code>。</li>
<li><code>StorageEvent.newValue</code>：字符串，表示新的键值。如果 storage 事件是由<code>clear()</code>方法或删除该键值对引发的，该属性返回<code>null</code>。</li>
<li><code>StorageEvent.oldValue</code>：字符串，表示旧的键值。如果该键值对是新增的，该属性返回<code>null</code>。</li>
<li><code>StorageEvent.storageArea</code>：对象，返回键值对所在的整个对象。也说是说，可以从这个属性上面拿到当前域名储存的所有键值对。</li>
<li><code>StorageEvent.url</code>：字符串，表示原始触发 storage 事件的那个网页的网址。</li>
</ul>
<p>下面是<code>StorageEvent.key</code>属性的例子。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onStorageChange</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(e.key);
&#125;

<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'storage'</span>, onStorageChange);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，该事件有一个很特别的地方，就是它不在导致数据变化的当前页面触发，而是在同一个域名的其他窗口触发。也就是说，如果浏览器只打开一个窗口，可能观察不到这个事件。比如同时打开多个窗口，当其中的一个窗口导致储存的数据发生改变时，只有在其他窗口才能观察到监听函数的执行。可以通过这种机制，实现多个窗口之间的通信。</p></div>  
</div>
            