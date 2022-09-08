
---
title: '使用 Manifest V3 做一个简单 Chrome 页面右键菜单搜索扩展'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/095dc0e947fe4638832d3064b4eac1b8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 07:59:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/095dc0e947fe4638832d3064b4eac1b8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;font-family:-apple-system,system-ui,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial;color:#00325e&#125;.markdown-body ::selection&#123;background-color:#00325e;color:#fff&#125;.markdown-body blockquote&#123;padding:10px 20px;background-color:#fffaf0;box-shadow:0 3px 10px 0 rgba(255,172,194,.24);border:1px solid #f3ca8e;transition:all .2s;margin:1em 0;border-radius:5px&#125;.markdown-body blockquote p&#123;font-size:14px;line-height:25px;color:#795548&#125;.markdown-body blockquote p:last-child&#123;margin:0&#125;.markdown-body blockquote:hover&#123;border-color:#ff9800;background-color:#fff8e0;box-shadow:0 6px 10px -5px rgba(225,173,98,.3803921569)&#125;.markdown-body blockquote code&#123;color:#ff502c&#125;.markdown-body pre&#123;border:1px solid #8cc0f3;box-shadow:0 3px 10px 0 rgba(255,198,198,.28);border-radius:5px;transition:all .2s;overflow-x:auto;white-space:pre-wrap&#125;.markdown-body pre:hover&#123;border-color:#6d9dce&#125;.markdown-body pre>code&#123;padding:10px 20px;color:#00325e;background:#f0f8ff;font-size:12px;line-height:1.6;display:block&#125;.markdown-body code&#123;background:#f6fbff;color:#0b5393;padding:2px 4px;border-radius:4px;font-size:12px&#125;.markdown-body p&#123;font-size:14px;line-height:28px;text-align:justify;margin-bottom:17px;color:#595959&#125;.markdown-body a&#123;color:#00325e;text-decoration:none&#125;.markdown-body a:after&#123;content:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAQdJREFUKFNt0DtLA0EUBeBzZle0Eks7rcUfEfBRCha7NorYa6NmVJzgyi4smUgKtdZGCJktLMVH4Y8QeztLWyE7VyLEuNFbXj4Oh0P8c8mZm+uJrEN4BJFTeP/MUVe3bnocfALwkOlo1zS7iZAzf6Cx7oXgbaqjxiDEWCcVaGyxQ8pSWo9XhqhoQ/xUFbaKjhe5V+CmR7mnSplEEF6GSmJ+F/d0KHvbCIIJCLc85U6BC5mONgbJNM3uFag++sX7z8O8MzsWBucifMx0dDGE1kmm458KDVukAlnNdDz/exEeW3dNkbfsYC0xtmgDWP6ELLZ0/F6BJu/UoFQN5AkoeUjeJPvx6+i+X5Sjah4tA6gYAAAAAElFTkSuQmCC);margin-left:2px&#125;.markdown-body a:hover&#123;box-shadow:0 1px&#125;.markdown-body table&#123;max-width:100%;border-collapse:collapse;border-spacing:0;box-shadow:0 3px 10px 0 rgba(255,238,172,.24);transition:all .2s&#125;.markdown-body table:hover&#123;box-shadow:0 3px 10px 0 rgba(185,169,103,.24)&#125;.markdown-body table tr th&#123;border:1px solid #8cc0f3;background-color:#f0f8ff;padding:12px 15px&#125;.markdown-body table tr td&#123;border:1px solid rgba(243,202,142,.4);padding:12px 15px&#125;.markdown-body table tbody tr&#123;transition:all .2s&#125;.markdown-body table tbody tr:hover td&#123;border-color:#f3ca8e;background-color:#fff8e0;z-index:1&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body h1&#123;font-size:20px;margin-top:30px;margin-bottom:10px;padding-left:30px;position:relative&#125;.markdown-body h1>code&#123;font-size:20px&#125;.markdown-body h1:before&#123;content:"🍺";display:block;font-size:18px;width:18px;height:18px;left:0;position:absolute&#125;.markdown-body h2&#123;font-size:18px;margin-top:30px;margin-bottom:10px;padding-left:28px;position:relative&#125;.markdown-body h2>code&#123;font-size:18px&#125;.markdown-body h2:before&#123;content:"🍻";display:block;font-size:16px;width:16px;height:16px;left:0;position:absolute&#125;.markdown-body h3&#123;font-size:16px;margin-top:30px;margin-bottom:10px;padding-left:26px;position:relative&#125;.markdown-body h3>code&#123;font-size:16px&#125;.markdown-body h3:before&#123;content:"🥂";display:block;font-size:14px;width:14px;height:14px;left:0;position:absolute&#125;.markdown-body h4&#123;font-size:14px;margin-top:30px;margin-bottom:10px;padding-left:24px;position:relative&#125;.markdown-body h4>code&#123;font-size:14px&#125;.markdown-body h4:before&#123;content:"🥃";display:block;font-size:12px;width:12px;height:12px;left:0;position:absolute&#125;.markdown-body h5&#123;font-size:12px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h5>code&#123;font-size:12px&#125;.markdown-body h6&#123;font-size:10px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h6>code&#123;font-size:10px&#125;.markdown-body h1,.markdown-body h2&#123;color:#ff502c&#125;.markdown-body hr&#123;height:4px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#6d9dce,#8cc0f3 25%,transparent 50%)&#125;.markdown-body hr:nth-child(2n)&#123;background-image:linear-gradient(270deg,#ff9800,#fff8e0 25%,transparent 50%)&#125;.markdown-body ul&#123;padding-inline-start:20px&#125;.markdown-body ul li&#123;list-style-type:"🔸"&#125;.markdown-body ul li li&#123;list-style-type:"◻️"&#125;.markdown-body ul li li li&#123;list-style-type:"▫️"&#125;.markdown-body ol&#123;padding-inline-start:20px&#125;.markdown-body ol ::marker&#123;color:#ff9800&#125;.markdown-body ol,.markdown-body ul&#123;line-height:2em&#125;.markdown-body li&#123;padding-inline-start:1ch&#125;.markdown-body li.task-list-item&#123;list-style:none;padding-inline-start:0&#125;.markdown-body li input&#123;padding-right:2px&#125;.markdown-body li input[type=checkbox i]&#123;appearance:none&#125;.markdown-body li input:before&#123;content:"🟩";display:block;width:13px;height:13px&#125;.markdown-body li input:checked:before&#123;content:"✅"&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第6篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<h2 data-id="heading-0">介绍</h2>
<p>如果做一些简单的功能，油猴脚本就可以做到；要做一些复杂的带有界面的功能，就需要 Chrome 扩展来做了。</p>
<p>Chrome 扩展是基于 HTML、JavaScript 和 CSS 等 Web 技术构建的，在单独的沙盒执行环境中运行，并与 Chrome 浏览器交互。</p>
<p>Chrome 浏览器可以自定义地址栏搜索引擎，但是切换比较麻烦，如果有一个方便切换搜索引擎的扩展，就很方便我们搜索我们想要的东西了。下面介绍一下，如何做一个 Chrome 右键菜单搜索扩展。</p>
<p>因为 manifest_version2 会提示过时，所以本例使用的是 manifest_version3 来创建扩展程序。</p>
<h2 data-id="heading-1">创建清单</h2>
<p>每个扩展都要有一个名为 <code>manifest.json</code> 的 JSON 格式的清单文件，第一步要创建这个文件。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"搜索"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"description"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"百度 必应 360 搜狗 谷歌"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"1.0"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"manifest_version"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">3</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"icons"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"16"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"img/icon.png"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"48"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"img/icon.png"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"128"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"img/icon.png"</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"action"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"default_icon"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"img/icon.png"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"default_title"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"搜索"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"default_popup"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"index.html"</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"background"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"service_worker"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"background.js"</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"permissions"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-string">"notifications"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-string">"contextMenus"</span>
  <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"content_scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"matches"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"<all_urls>"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"js"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"content-script.js"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"run_at"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"document_idle"</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>manifest_version、name、version 字段是必须的。</li>
<li>action 定义扩展的图标、标题和用户界面。</li>
<li>manifest_version2 的 background.scripts 要替换为 manifest_version3 的 background.service_worker。</li>
<li>与 DOM 互动要使用 content_scripts 里面的 js 字段配置。matches 字段可使用通配符设置，例如 <code>*://*.juejin.cn/*</code>。</li>
<li>permissions 字段定义要使用的权限。这里使用了两个：通知和弹出菜单。</li>
</ol>
<blockquote>
<p>manifest_version3 不支持多个后台脚本，但可以将 service_worker 声明为 ES 模块来引入多个文件：</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// Manifest V2</span>
<span class="hljs-punctuation">&#123;</span>
  ...
  <span class="hljs-attr">"background"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
      <span class="hljs-string">"backgroundContextMenus.js"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-string">"backgroundOauth.js"</span>
    <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"persistent"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  ...
<span class="hljs-punctuation">&#125;</span>
<span class="hljs-comment">// Manifest V3</span>
<span class="hljs-punctuation">&#123;</span>
  ...
  <span class="hljs-attr">"background"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"service_worker"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"background.js"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"module"</span> <span class="hljs-comment">//optional</span>
  <span class="hljs-punctuation">&#125;</span>
  ...
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">交互逻辑</h2>
<p><code>manifest.json</code> 清单文件里面定义的文件都要保证不能缺少。不然会报错无法使用。</p>
<h3 data-id="heading-3">background.js</h3>
<p>这个是 service_worker，用来与浏览器互动，并与 content_scripts 通信。下面定义了两个事件监听，一个点击弹出菜单项的事件，一个点击扩展图标的事件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">sendData</span> = (<span class="hljs-params">data</span>) => &#123;
  chrome.<span class="hljs-property">tabs</span>.<span class="hljs-title function_">query</span>(&#123;
    <span class="hljs-attr">active</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">currentWindow</span>: <span class="hljs-literal">true</span>
  &#125;).<span class="hljs-title function_">then</span>(<span class="hljs-function"><span class="hljs-params">tabs</span> =></span> &#123;
    chrome.<span class="hljs-property">tabs</span>.<span class="hljs-title function_">sendMessage</span>(tabs[<span class="hljs-number">0</span>].<span class="hljs-property">id</span>, data)
  &#125;);
&#125;;
<span class="hljs-comment">// 点击弹出菜单</span>
chrome.<span class="hljs-property">contextMenus</span>.<span class="hljs-property">onClicked</span>.<span class="hljs-title function_">addListener</span>(<span class="hljs-keyword">function</span>(<span class="hljs-params">item, tab</span>) &#123;
  <span class="hljs-keyword">if</span> (!tab.<span class="hljs-property">url</span>.<span class="hljs-title function_">startsWith</span>(<span class="hljs-string">'chrome://'</span>)) <span class="hljs-title function_">sendData</span>(item);
&#125;);
<span class="hljs-comment">// 点击扩展图标</span>
chrome.<span class="hljs-property">runtime</span>.<span class="hljs-property">onMessage</span>.<span class="hljs-title function_">addListener</span>(<span class="hljs-keyword">function</span>(<span class="hljs-params">data, sender, sendResponse</span>) &#123;
  <span class="hljs-title function_">sendData</span>(data);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">content-script.js</h3>
<p>这个文件是与 background.js 通信，根据收到的数据，可对页面 DOM 进行操作。</p>
<pre><code class="hljs language-js copyable" lang="js">chrome.<span class="hljs-property">runtime</span>.<span class="hljs-property">onMessage</span>.<span class="hljs-title function_">addListener</span>(<span class="hljs-function">(<span class="hljs-params">data, sender, sendResponse</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (data.<span class="hljs-property">menuItemId</span>) &#123;
    <span class="hljs-keyword">switch</span> (data.<span class="hljs-property">menuItemId</span>) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'bing'</span>:
        url = <span class="hljs-string">'https://cn.bing.com/search?q='</span>;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'360'</span>:
        url = <span class="hljs-string">'https://www.so.com/s?q='</span>;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'sogou'</span>:
        url = <span class="hljs-string">'https://sogou.com/web?query='</span>;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'google'</span>:
        url = <span class="hljs-string">'https://www.google.com/search?q='</span>;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-attr">default</span>:
        url = <span class="hljs-string">'https://www.baidu.com/s?wd='</span>;
    &#125;
    <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">open</span>(data.<span class="hljs-property">selectionText</span> ? url + data.<span class="hljs-property">selectionText</span> : <span class="hljs-keyword">new</span> <span class="hljs-title function_">URL</span>(url).<span class="hljs-property">origin</span>);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">使用</h2>
<ol>
<li>git clone <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzkrisj%2Fchrome-search.git%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zkrisj/chrome-search.git%E3%80%82" ref="nofollow noopener noreferrer">github.com/zkrisj/chro…</a></li>
<li>打开扩展程序管理页面。</li>
<li>点击右上角开启开发者模式。</li>
<li>点击 加载已解压的扩展程序。选择第 1 步的文件夹。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/095dc0e947fe4638832d3064b4eac1b8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="捕获.PNG" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">效果</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2c56f301a334b4d85ce09f6f8fca64a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="微信截图_20220907234713.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5281b1a762347989ac0832f4fd224f6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="微信图片编辑_20220907235551.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">完整代码仓库地址</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzkrisj%2Fchrome-search" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zkrisj/chrome-search" ref="nofollow noopener noreferrer">github.com/zkrisj/chro…</a>，欢迎你的使用和 star。</p></div>  
</div>
            