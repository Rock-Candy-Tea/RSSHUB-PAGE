
---
title: 'Chrome 请求过滤扩展实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6d83ee2b8f040468bb82b4489149971~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 03 May 2021 03:24:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6d83ee2b8f040468bb82b4489149971~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a name="user-content-start" href="https://juejin.cn/post/undefined"></a> 引子</h2>
<p>接着 <a href="https://github.com/XXHolic/blog/issues/85" target="_blank" rel="nofollow noopener noreferrer">Chrome 扩展 : 入门</a>，接下来开始实现一开始自己的想法：网络请求过滤。简单的说就是监听某个网站的所有请求，把想要的请求在扩展插件中展示出来。扩展名为 Capture Request 。</p>
<ul>
<li><a href="https://github.com/XXHolic/blog/issues/86" target="_blank" rel="nofollow noopener noreferrer">Origin</a></li>
<li><a href="https://github.com/XXHolic" target="_blank" rel="nofollow noopener noreferrer">My GitHub</a></li>
</ul>
<h2 data-id="heading-1"><a name="user-content-detail" href="https://juejin.cn/post/undefined"></a> 需求具体化</h2>
<p>上面的想法比较模糊，为了达到这个目的，结合文档的示例，要做的有：</p>
<ol>
<li>扩展要有对应的图标及提示。</li>
<li>点击工具栏扩展图标，打开一个新的 Tab 页面，用来展示请求的相关信息。</li>
<li>扩展监听处于激活 Tab 的网站请求，可以配置过滤监听的网址。</li>
<li>对监听的请求，支持根据 url 筛选并导出。</li>
</ol>
<p>有些功能不方便直接在文档找到，这个时候，建议在 Chrome 商店找一个开源扩展，根据效果看里面用的一些 API ，然后找到对应文档。这里参考了 <a href="https://github.com/zxlie/FeHelper" target="_blank" rel="nofollow noopener noreferrer">FeHelper</a> 里面的一些实现。需要注意到是 FeHelper 开发基于 <code>manifest_version</code> 版本为 2 ，以下开发扩展基于的版本是推荐的版本为 3 ，完整代码见 <a href="https://github.com/XXHolic/extensions/tree/main/capture-request" target="_blank" rel="nofollow noopener noreferrer">Capture Request</a> 。</p>
<h2 data-id="heading-2"><a name="user-content-implement" href="https://juejin.cn/post/undefined"></a> 实现</h2>
<h3 data-id="heading-3"><a name="user-content-one" href="https://juejin.cn/post/undefined"></a> 图标相关信息配置</h3>
<p>按照<a href="https://github.com/XXHolic/blog/issues/85" target="_blank" rel="nofollow noopener noreferrer">入门</a>里面介绍的信息，图标可能出现的地方有工具栏、扩展管理页、权限警告和 favicon 上，在 <code>manifest.json</code> 中配置的下面相关字段：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"Capture Request"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">"Capture Request"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0"</span>,
  <span class="hljs-string">"manifest_version"</span>: <span class="hljs-number">3</span>,
  <span class="hljs-string">"action"</span>: &#123;
    <span class="hljs-string">"default_icon"</span>: &#123;
      <span class="hljs-string">"16"</span>: <span class="hljs-string">"xxx.png"</span>,
      <span class="hljs-string">"32"</span>: <span class="hljs-string">"xxx.png"</span>,
    &#125;
  &#125;,
  <span class="hljs-string">"icons"</span>:&#123;
    <span class="hljs-string">"16"</span>: <span class="hljs-string">"xxx.png"</span>,
    <span class="hljs-string">"32"</span>: <span class="hljs-string">"xxx.png"</span>,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>什么尺寸图标用在什么地方的详细说明在<a href="https://developer.chrome.com/docs/extensions/mv3/manifest/icons/" target="_blank" rel="nofollow noopener noreferrer">这里</a>，文档上推荐用 PNG 的图片格式。按照这个来，发现有的图标太小了会看起来明显模糊，也可以用比较大的尺寸，Chrome 会自己把图片压缩到需要的尺寸。</p>
<h3 data-id="heading-4"><a name="user-content-two" href="https://juejin.cn/post/undefined"></a> 点击扩展打开新 Tab 页面</h3>
<p>在<a href="https://github.com/XXHolic/blog/issues/85" target="_blank" rel="nofollow noopener noreferrer">入门</a>里面点击扩展的展现形式是打开了一个弹窗，在文档 <a href="https://developer.chrome.com/docs/extensions/mv3/user_interface/" target="_blank" rel="nofollow noopener noreferrer">Design the user interface</a> 中介绍的形式有 Popup 、Tooltip、Omnibox、Context menu、Override pages ，最有可能就是 Override pages ，但试了一下发现没有效果，于是去看别人的实现，发现可以通过监听<a href="https://developer.chrome.com/docs/extensions/reference/action/#event-onClicked" target="_blank" rel="nofollow noopener noreferrer">点击图标事件</a>打开新 Tab 。</p>
<p>但看似可以直接用的 API ，实际上还有下面几点要考虑：</p>
<ol>
<li>在哪里监听这事件？</li>
<li>什么时候监听这个事件？</li>
<li>怎么打开新 Tab ?</li>
<li>是否需要权限，如果需要，涉及那些权限？</li>
</ol>
<p>在<a href="https://github.com/XXHolic/blog/issues/85" target="_blank" rel="nofollow noopener noreferrer">入门</a>里面添加功能是通过<a href="https://developer.chrome.com/docs/extensions/mv3/background_pages/" target="_blank" rel="nofollow noopener noreferrer">后台脚本</a>，文档开头说的一句个人觉得很重要：</p>
<blockquote>
<p>扩展是通过基于事件编程来改变或增强 Chrome 浏览体验。</p>
</blockquote>
<p>从文档中可以发现，在后台脚本中可以解决上面提的第 1、2 两个问题，需要的权限是 <code>scripting</code> 。</p>
<p>打开 Tab 使用的 API 是 <a href="https://developer.chrome.com/docs/extensions/reference/tabs/" target="_blank" rel="nofollow noopener noreferrer">chrome.tabs</a> ，需要的权限是 <code>tabs</code> 。</p>
<p>主要做法是在 <code>manifest.json</code> 中添加下面配置：</p>
<pre><code class="hljs language-diff copyable" lang="diff">&#123;
  ...
<span class="hljs-addition">+ "permissions": [</span>
<span class="hljs-addition">+   "scripting",</span>
<span class="hljs-addition">+   "tabs",</span>
<span class="hljs-addition">+ ],</span>
<span class="hljs-addition">+ "background": &#123;</span>
<span class="hljs-addition">+   "service_worker": "background.js"</span>
<span class="hljs-addition">+ &#125;,</span>
  ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后新建后台脚本文件 <code>background.js</code> ，并添加下面主要逻辑代码：</p>
<pre><code class="hljs language-js copyable" lang="js">chrome.action.onClicked.addListener(<span class="hljs-function">() =></span> &#123;
  chrome.tabs.create(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">'page.html'</span>
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><a name="user-content-three" href="https://juejin.cn/post/undefined"></a> 监听请求及配置</h3>
<p>要把处于激活 Tab 网站上的请求显示到打开的扩展页面上，主要需要考虑的点有：</p>
<ol>
<li>怎么找到激活的 Tab ？</li>
<li>怎么截获网页请求？</li>
<li>截获的请求怎么同步到扩展自定义页面上？</li>
</ol>
<p>通过上面打开 Tab 的效果实现，可以联想到相关的 API 应该也在 <a href="https://developer.chrome.com/docs/extensions/reference/tabs/" target="_blank" rel="nofollow noopener noreferrer">chrome.tabs</a> 中，发现提供了 <code>query</code> 方法可以解决第 1 个问题。</p>
<p>截获请求的方法通过网上搜索，发现文档 <a href="https://developer.chrome.com/docs/extensions/reference/webRequest/" target="_blank" rel="nofollow noopener noreferrer">chrome.webRequest</a> ，里面详细的介绍了扩展中请求的生命周期及触发的事件，经过对比思考，个人最后决定监听 <code>onResponseStarted</code> 事件，需要的权限是 <code>webRequest</code> 。这样就解决了第 2 个问题。</p>
<p>参照<a href="https://github.com/XXHolic/blog/issues/85" target="_blank" rel="nofollow noopener noreferrer">入门</a>里面改变颜色的方式，类似的可以把请求缓存到 <a href="https://developer.chrome.com/docs/extensions/reference/storage/" target="_blank" rel="nofollow noopener noreferrer">chrome.storage</a> ，然后在扩展页面获取，需要的权限是 <code>storage</code> 。关于数据同步，可以通过监听 <code>chrome.storage.onChanged</code> 事件拿到变动的最新数据。这样就解决了第 3 个问题。</p>
<p>在调试的过程中，发现存在本地的数据使用 <code>chrome.storage.sync</code> 时，请求达到一定量后，会报错。看了文档发现这种方式的最大值有一定的限制，不太适合存储大量请求数据的场景，使用 <code>chrome.storage.local</code> 更加合适。</p>
<p>配置过滤请求的方式可直接按照<a href="https://github.com/XXHolic/blog/issues/85" target="_blank" rel="nofollow noopener noreferrer">入门</a>里面的配置方式处理，但有一点需要注意的是，每当配置更新的时候，需要重新监听 <code>onResponseStarted</code> 事件。</p>
<p>主要做法是在 <code>manifest.json</code> 的 <code>permissions</code> 字段中添加 <code>webRequest</code>、<code>storage</code> 。</p>
<p>在 <code>background.js</code> 中添加主要代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 储存请求数据默认值</span>
<span class="hljs-keyword">let</span> requestList = []
<span class="hljs-comment">// 网址过滤的默认值</span>
<span class="hljs-keyword">let</span> urlPattern = <span class="hljs-string">'<all_urls>'</span>

<span class="hljs-comment">// 监听请求事件的处理程序</span>
<span class="hljs-keyword">const</span> handlerResponseStarted = <span class="hljs-function">(<span class="hljs-params">details</span>) =></span> &#123;
  <span class="hljs-comment">// 找到处于激活状态的 Tab</span>
  chrome.tabs.query(&#123; <span class="hljs-attr">active</span>: <span class="hljs-literal">true</span> &#125;, <span class="hljs-function">(<span class="hljs-params">tab</span>) =></span> &#123;
    requestList.unshift(details)
    chrome.storage.local.set(&#123; requestList &#125;);
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">cancel</span>: <span class="hljs-literal">true</span> &#125;;
  &#125;)
&#125;

<span class="hljs-comment">// 监听 storage 改变事件</span>
chrome.storage.onChanged.addListener(<span class="hljs-function">(<span class="hljs-params">changeObj, areaName</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; urlPattern &#125; = changeObj
  <span class="hljs-comment">// 由于在 page.html 里面也监听了，所以要判断是不是 urlPattern 变动了</span>
  <span class="hljs-keyword">if</span> (areaName !== <span class="hljs-string">'local'</span> || !urlPattern) &#123;
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'urlPattern does not change'</span>)
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-keyword">const</span> &#123; newValue &#125; = urlPattern
  <span class="hljs-keyword">const</span> hasAddListen = chrome.webRequest.onResponseStarted.hasListener(handlerResponseStarted)
  <span class="hljs-keyword">if</span> (hasAddListen) &#123;
    chrome.webRequest.onResponseStarted.removeListener(handlerResponseStarted);
  &#125;
  chrome.webRequest.onResponseStarted.addListener(
    handlerResponseStarted,
    &#123; <span class="hljs-attr">urls</span>: [newValue] &#125;,
  );
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为扩展页面 <code>page.html</code> 添加脚本文件 <code>pages.js</code> ，添加关键逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js">  chrome.storage.onChanged.addListener(<span class="hljs-function">(<span class="hljs-params">changeObj, areaName</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; requestList &#125; = changeObj
    <span class="hljs-comment">// 由于在 background.js 里面也监听了，所以要判断是不是 requestList 变动了</span>
    <span class="hljs-keyword">if</span> (areaName !== <span class="hljs-string">'local'</span> || !requestList) &#123;
      <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'requestList does not change'</span>)
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">const</span> &#123; newValue &#125; = requestList || &#123; <span class="hljs-attr">newValue</span>: [] &#125;
    <span class="hljs-keyword">const</span> newItem = newValue[<span class="hljs-number">0</span>] || <span class="hljs-literal">null</span>
    <span class="hljs-keyword">if</span> (!newItem) &#123;
      <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'no data'</span>)
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">// 显示数据的逻辑</span>
    showData(newItem)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><a name="user-content-four" href="https://juejin.cn/post/undefined"></a> 导出数据</h3>
<p>截获了想要的数据，有需要导出到本地使用的场景，参考 <a href="https://github.com/zxlie/FeHelper" target="_blank" rel="nofollow noopener noreferrer">FeHelper</a> 里面的实现，找到了文档 <a href="https://developer.chrome.com/docs/extensions/reference/downloads/" target="_blank" rel="nofollow noopener noreferrer">chrome.downloads</a> ，需要的权限是 <code>downloads</code> 。</p>
<p>主要做法是在 <code>manifest.json</code> 的 <code>permissions</code> 字段中添加 <code>downloads</code> 。</p>
<p>在 <code>pages.js</code> 添加关键逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">let</span> localFilterList = []; <span class="hljs-comment">// 页面筛选后的数据</span>
  <span class="hljs-comment">// 点击导出的按钮</span>
  <span class="hljs-keyword">const</span> exportEle = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#operate-export'</span>)
  exportEle.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!localFilterList.length) &#123;
      alert(<span class="hljs-string">'无有效数据'</span>)
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">const</span> txt = <span class="hljs-built_in">JSON</span>.stringify(localFilterList)
    <span class="hljs-keyword">let</span> blob = <span class="hljs-keyword">new</span> Blob([txt], &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'application/octet-stream'</span> &#125;);
    <span class="hljs-comment">// 文件名称获取时间的秒数，可按照自己喜好定义</span>
    <span class="hljs-keyword">let</span> dt = (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()).getSeconds();
    chrome.downloads.download(&#123;
      <span class="hljs-attr">url</span>: URL.createObjectURL(blob),
      <span class="hljs-attr">saveAs</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">conflictAction</span>: <span class="hljs-string">'overwrite'</span>,
      <span class="hljs-attr">filename</span>: dt + <span class="hljs-string">'.json'</span>
    &#125;);
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7"><a name="user-content-reference" href="https://juejin.cn/post/undefined"></a> 参考资料</h2>
<ul>
<li><a href="https://github.com/XXHolic/blog/issues/85" target="_blank" rel="nofollow noopener noreferrer">Chrome 扩展 : 入门</a></li>
<li><a href="https://github.com/XXHolic/blog/issues/84" target="_blank" rel="nofollow noopener noreferrer">Chrome 扩展 : 扩展是什么?</a></li>
<li><a href="https://github.com/zxlie/FeHelper" target="_blank" rel="nofollow noopener noreferrer">FeHelper Github</a></li>
</ul>
<details>
<summary>wastebasket</summary>
<p>最近看了下电视剧<a href="https://movie.douban.com/subject/1478168/" target="_blank" rel="nofollow noopener noreferrer">《围城》</a>，虽然年代很早，但真是有趣，据说是完全按照原著拍的，没有任何改编。</p>
<p>在小说的最后一段才讲的是婚姻围城，不知道什么时候开始起，我一直以为整本书讲的是关于结婚的围城。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6d83ee2b8f040468bb82b4489149971~tplv-k3u1fbpfcp-zoom-1.image" alt="83-poster" loading="lazy" referrerpolicy="no-referrer"></p>
</details></div>  
</div>
            