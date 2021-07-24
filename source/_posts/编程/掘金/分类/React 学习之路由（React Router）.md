
---
title: 'React 学习之路由（React Router）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6129'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 02:50:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=6129'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">React Router</h2>
<p><code>react-router</code>：路由核心库，包含诸多和路由功能相关的核心代码</p>
<p><code>react-router-dom</code>：利用核心库，结合实际的页面，实现跟页面路由相关的功能</p>
<p>所以我们一般都安装使用 <code>react-router-dom</code> 库</p>
<h3 data-id="heading-1">路由的两种模式</h3>
<p>我们都知道，url 地址 (如：<code>https://www.suressk.com:443/article?uid=sures&id=1008#hash</code>) 由以下几部分组成：</p>
<ol>
<li>网络协议 (<code>schema</code>)：<code>https</code> (<code>http</code> / <code>https</code> / <code>file</code>等)</li>
<li>主机名 (<code>host</code>)：<code>www.suressk.com</code> (一般有 <code>ip 地址</code>，<code>域名</code>，<code>预设值(如 localhost)</code>，<code>局域网中的电脑名</code>等)</li>
<li>端口号 (<code>port</code>)：<code>443</code> (<code>http 默认 80</code>，<code>https 默认 443</code>)</li>
<li>访问路径 (<code>path</code>)：<code>/article</code></li>
<li>查询参数 (<code>query</code> / <code>search</code>)：<code>?uid=sures&id=1008</code></li>
<li>哈希 (<code>hash</code> / <code>锚点</code>)：<code>#hash</code></li>
</ol>
<h4 data-id="heading-2">Hash Router</h4>
<p>根据 <code>url</code> 地址中的 <code>hash</code> 值来确定显示的组件</p>
<blockquote>
<p>因为 <code>hash</code> 值变化不会导致页面刷新 <br>
它的兼容性比较好，老版浏览器也支持</p>
</blockquote>
<h4 data-id="heading-3">Browser History Router</h4>
<p><code>HTML5</code> 出现后，新增 <code>History API</code>，从而使浏览器拥有了改变路径而不刷新页面的能力。<code>History</code> 表示浏览器的历史记录，它使用栈的方式存储，当我们每访问一个路径，它会将这个栈中加入一条路径记录</p>
<p><strong><code>history</code>：</strong></p>
<ol>
<li>
<p><code>history.length</code>：获取当前页历史记录条数</p>
</li>
<li>
<p><code>history.pushState(data, title, url)</code>：向当前历史记录栈中加入一条新记录</p>
<ul>
<li><code>data</code>：附加的数据信息</li>
<li><code>title</code>：页面标题 (大部分浏览器不支持)</li>
<li><code>url</code>：新的路径地址</li>
</ul>
</li>
<li>
<p><code>history.replaceState(data, title, url)</code>：替换历史记录栈当前的历史记录</p>
</li>
</ol>
<p>从而，我们可以根据路径来决定渲染哪个组件</p>
<h3 data-id="heading-4">路由组件</h3>
<p><code>react-router</code> 为我们提供了两个重要组件：<code>Router</code> 和 <code>Route</code> 以及一些其他的组件</p>
<h4 data-id="heading-5">Router 组件</h4>
<p>它本身不做任何展示，仅提供路由模式配置；此组件会产生一个上下文，上下文会提供一些实用的对象和方法，<code>react-router-dom</code> 提供下面两个组件：</p>
<ol>
<li>
<p><code>HashRouter</code>：实用 <code>hash 模式</code> 匹配</p>
</li>
<li>
<p><code>BrowserRouter</code>：实用 <code>BrowserHistory 模式</code> 匹配</p>
</li>
</ol>
<p>通常情况下，仅使用一个 <code>Router</code> 组件，而且用它来包裹整个页面</p>
<h4 data-id="heading-6">Route 组件</h4>
<p>根据不同的地址，展示不同的组件，它有两个重要属性：<code>path</code> 和 <code>component</code>：</p>
<ol>
<li>
<p><code>path</code>：匹配的路径规则 (地址匹配 <code>涉及后面的 "动态路径"</code>)，也可以是一个 <code>路径正则数组</code></p>
<ul>
<li>默认是不区分大小写的 (可以配合设置 <code>sensitive 属性为 true</code>，使路径匹配 <code>区分大小写</code>)</li>
<li>默认是模糊匹配，只要路径存在，则认为匹配成功 (可以配合设置 <code>exact 属性为 true</code> 来精确匹配)</li>
<li>如果不设置 <code>path</code>，则匹配任意路径</li>
</ul>
</li>
<li>
<p><code>component</code>：路径匹配成功后需显示的组件</p>
</li>
<li>
<p><code>Route</code> 的 <code>children (子元素)</code>：</p>
<ul>
<li>
<p>传递 <code>React 元素</code>，无论路径是否成功匹配，只要经过对此 <code>Route 组件</code> 的匹配，那么一定会显示 <code>children</code>，且会 <code>忽略 Route 组件的 component 属性</code></p>
</li>
<li>
<p>传递一个函数，该函数有多个参数 (来自 Router 组件产生的上下文)，改函数返回 React 元素，则一定会显示返回的元素，且会 <code>忽略 Route 组件的 component 属性</code></p>
</li>
</ul>
</li>
</ol>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123;BrowserRouter <span class="hljs-keyword">as</span> Router, Route&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompA</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>CompA<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompB</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>CompB<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompC</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>CompC<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/a'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;CompA&#125;</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/b'</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;CompB&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> "#<span class="hljs-attr">f40</span>" &#125;&#125;></span>Route Children Prop<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;CompC&#125;</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>Route</code> 组件可以写在任意位置，只要保证它是 <code>Router</code> 组件的后代元素即可</strong></p>
<h4 data-id="heading-7">Switch 组件</h4>
<p>它会依次进行路径匹配，若路径匹配成功，则不会继续往后匹配 (不加此组件的默认情况下会将 <code>Route</code> 组件的路径全部进行匹配渲染)</p>
<p>由于 <code>Switch</code> 组件会循环所有的子元素 (<code>按照书写 Route 组件</code> 的顺序去依次匹配)，若匹配成功，则渲染对应的组件，停止循环；因此，<code>Switch</code> 子组件不能是 <code>Route</code> 和 <code>Redirect</code> 组件以外的其他组件</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 比如，用法如下：</span>
<span class="hljs-keyword">import</span> React, &#123; memo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123;BrowserRouter <span class="hljs-keyword">as</span> Router, Route, Switch&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompA</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>CompA<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompB</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>CompB<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompC</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>CompC<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Task</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/a/b"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">CompB</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/a"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;CompA&#125;</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> "#<span class="hljs-attr">f40</span>" &#125;&#125;></span>Route Children Prop<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;CompC&#125;</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> memo(Task)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个示例，当我们访问 本地 server 地址 <code>/a/b</code> 路径时，你会发现页面渲染的内容是：<code>CompB</code>，虽然 <code>/a</code> 路径展示 <code>红色 Route Children Prop</code> 也满足路径匹配，但 <code>Switch组件</code> 匹配显示 <code>CompB组件</code> 后就停止了</p>
<h3 data-id="heading-8">路由信息</h3>
<p><code>Router</code> 组件会创建一个 <code>Context</code>，并且会向 <code>Context</code> 中注入一些信息。这个 <code>Context</code> 对开发者是隐藏的，<code>Route</code> 组件匹配到了 <code>path</code>，<code>Route</code> 组件会将这些 <code>Context</code> 中的信息作为属性传递给对应的组件：</p>
<h4 data-id="heading-9"><code>history</code></h4>
<ul>
<li>
<p><code>非 window.history</code> 对象，我们可以利用该对象进行无刷新跳转等操作</p>
</li>
<li>
<p><code>push(relativePath, data?)</code>：将某个新地址入栈 (历史记录栈)，第一个参数为跳转的相对路径；第二个参数即为跳转过去附加的状态数据 (后面可通过 <code>props.history.location.state</code> 获取，但这个状态数据依赖于跳转，若直接访问这个跳转的路径，状态数据就为空)</p>
</li>
<li>
<p><code>replace(relativePath, data?)</code>：将某个新地址替换历史记录栈的当前记录</p>
</li>
<li>
<p><code>go()</code> / <code>forward()</code> / <code>back()</code>：用法与 <code>window.history</code> 中的同名方法一样</p>
</li>
</ul>
<h4 data-id="heading-10"><code>location</code></h4>
<ul>
<li>
<p>与 <code>props.history.location</code> 是同一个对象，它里面记录了当前地址的相关信息 (<code>search</code> / <code>hash</code> / <code>pathname</code> / <code>state</code>)，我们通常会使用第三方库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fquery-string" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/query-string" ref="nofollow noopener noreferrer">【<strong>query-string</strong>】</a> 来解析参数数据 (<code>parse</code>)：</p>
</li>
<li>
<p>如 <code>location.search</code>：<code>?a=1&b=2&c=3</code> 解析为 <code>&#123;a: 1, b: 2, c: 3&#125;</code></p>
</li>
<li>
<p>如 <code>location.hash</code>：<code>#d=4&e=5</code> 解析为 <code>&#123;d: 4, e: 5&#125;</code></p>
</li>
</ul>
<h4 data-id="heading-11"><code>match</code></h4>
<ul>
<li>
<p>保存路由匹配的相关信息</p>
</li>
<li>
<p><code>isExact</code>：指当前路由路径与 <code>Route 组件</code> 配置的路径是否精确匹配，与 <code>Route 组件</code> 是否设置 <code>exact</code> 属性无关</p>
</li>
<li>
<p><code>params</code>：会根据 <code>Route 组件</code> 配置的动态参数，将地址栏参数对应位置的数据收集到这个对象中，如：</p>
<ul>
<li>
<p><code><Route path="/news/:year/:month?/:day?" component=&#123;News&#125; /></code>，访问路径是：<code>/news/2021/7</code>，那么 <code>params = &#123;year: '2021', month: '7', day: undefined&#125;</code></p>
</li>
<li>
<p><code><Route path="/news/:year(\d+)/:month?/:day?" component=&#123;News&#125; /></code>，加入正则表达式 (年份是数字)，若访问路径是：<code>/news/2021/7</code>，那么 <code>params = &#123;year: '2021', month: '7', day: undefined&#125;</code>；若访问路径是：<code>/news/suressk/7</code>，则此路径匹配失败</p>
</li>
</ul>
</li>
<li>
<p><code>path</code>：匹配上的路由路径使用的路径正则匹配规则 (如上面的示例：<code>"/news/:year(\d+)/:month?/:day?"</code>)</p>
</li>
<li>
<p><code>url</code>：实际匹配上的路由路径</p>
</li>
</ul>
<p><code>react-router</code> 使用了 <code>path-to-regexp</code> 来解析路径正则字符串，将它解析转换成一个真正的正则表达式</p>
<p>通常，向页面传递数据的方式有：</p>
<ol>
<li>
<p>使用 <code>state</code>：依赖于手动使用 <code>history 对象</code> 跳转时传递数据</p>
</li>
<li>
<p>使用 <code>search</code>：在地址栏通过查询参数携带 <code>/news?year=2021&month=7&day=21</code></p>
</li>
<li>
<p>使用 <code>hash</code>：将数据加到地址栏的 hash 值后 <code>/news#year=2021&month=7&day=21</code></p>
</li>
<li>
<p>使用 <code>params</code>：将数据填写到 <code>路径</code> 中 <code>/news/2021/7/21</code></p>
</li>
</ol></div>  
</div>
            