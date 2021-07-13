
---
title: 'Chrome插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74f3432c9ccc4b0da5131104e8c6c272~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 01:29:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74f3432c9ccc4b0da5131104e8c6c272~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​
1.什么是Chrome插件</p>
<pre><code class="copyable">  在我们的日常开发过程中，我们会在浏览器上安装很多有利于我们开发或者说更方便于使用chrome浏览器的插件，那么到底什么是chrome插件呢？ 其实Chrome插件就是一个用Web技术开发、用来增强浏览器功能的扩展程序，所以也许‘chrome扩展’比‘chrome插件’更贴切于它的意义。
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p>开发初体验</p>
<p>1.本地创建一个文件及：test</p>
<p>2.在test文件夹中，创建manifest.json。任何插件都必须要有这个文件，用来描述插件的配置信息</p>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"name"</span>: <span class="hljs-string">"test"</span>,
    <span class="hljs-string">"description"</span> : <span class="hljs-string">"this is test"</span>,
    <span class="hljs-string">"version"</span>: <span class="hljs-string">"0.0.1"</span>,
    <span class="hljs-string">"manifest_version"</span>: <span class="hljs-number">2</span>,
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义当前插件名，描述信息，以及版本号等</p>
<p>3.给插件加一个浏览器右上角的icon</p>
<pre><code class="copyable"> 这里可以自定义图标图片
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">
&#123;
     <span class="hljs-string">"name"</span>: <span class="hljs-string">"Hello Extensions"</span>,
    <span class="hljs-string">"description"</span> : <span class="hljs-string">"Hello world Extension"</span>,
    <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0"</span>,
    <span class="hljs-string">"manifest_version"</span>: <span class="hljs-number">2</span>，

     <span class="hljs-string">"browser_action"</span>:
      &#123;
      <span class="hljs-string">"default_icon"</span>: <span class="hljs-string">"./icons/16.png"</span>,
      <span class="hljs-string">"default_title"</span>: <span class="hljs-string">"这是一个示例Chrome插件"</span>,
      <span class="hljs-string">"default_popup"</span>: <span class="hljs-string">"index.html"</span>
      &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且还可以给它一个点击之后默认的弹出内容，如index.html中</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74f3432c9ccc4b0da5131104e8c6c272~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们就可以简单的来测试下我们刚刚写的小demo了</p>
<p>打开我们的chrome插件扩展，将我们写的test文件夹直接拖进来，然后你会发现在你的扩展器内多了一个名叫test的插件，如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55962b2a71d3417d91c699066afc5a19~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个时候，我们可以把该插件固定在我们浏览器的右上角，点击的时候会发现，弹框中的内容就是我们刚刚index中的写的内容哦，样式可以自行修改的。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f38d7f14e3a241e78b638ab215da00e8~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3.核心配置的介绍</p>
<p>1.manifest.json</p>
<pre><code class="copyable">  这是一个Chrome插件必不可少的文件，用来配置所有和插件相关的配置，必须放在根目录。

 下面是一些常见的配置：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">   

&#123;
 <span class="hljs-comment">// 清单文件的版本，这个必须写，而且必须是2</span>
 <span class="hljs-string">"manifest_version"</span>: <span class="hljs-number">2</span>,
 <span class="hljs-comment">// 插件的名称</span>
 <span class="hljs-string">"name"</span>: <span class="hljs-string">"demo"</span>,
 <span class="hljs-comment">// 插件的版本</span>
 <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
 <span class="hljs-comment">// 插件描述</span>
 <span class="hljs-string">"description"</span>: <span class="hljs-string">"简单的Chrome扩展demo"</span>,
 <span class="hljs-comment">// 图标，一般偷懒全部用一个尺寸的也没问题</span>
 <span class="hljs-string">"icons"</span>:
 &#123;
 <span class="hljs-string">"16"</span>: <span class="hljs-string">"img/icon.png"</span>,
 <span class="hljs-string">"48"</span>: <span class="hljs-string">"img/icon.png"</span>,
 <span class="hljs-string">"128"</span>: <span class="hljs-string">"img/icon.png"</span>
 &#125;,
 <span class="hljs-comment">// 会一直常驻的后台JS或后台页面</span>
 <span class="hljs-string">"background"</span>:
 &#123;
 <span class="hljs-comment">// 2种指定方式，如果指定JS，那么会自动生成一个背景页</span>
 <span class="hljs-string">"page"</span>: <span class="hljs-string">"background.html"</span>
 <span class="hljs-comment">//"scripts": ["js/background.js"]</span>
 &#125;,
 <span class="hljs-comment">// 浏览器右上角图标设置，browser_action、page_action、app必须三选一</span>
 <span class="hljs-string">"browser_action"</span>: 
 &#123;
 <span class="hljs-string">"default_icon"</span>: <span class="hljs-string">"img/icon.png"</span>,
 <span class="hljs-comment">// 图标悬停时的标题，可选</span>
 <span class="hljs-string">"default_title"</span>: <span class="hljs-string">"这是一个示例Chrome插件"</span>,
 <span class="hljs-string">"default_popup"</span>: <span class="hljs-string">"popup.html"</span>
 &#125;,
 <span class="hljs-comment">// 当某些特定页面打开才显示的图标</span>
 <span class="hljs-comment">/*"page_action":
 &#123;
 "default_icon": "img/icon.png",
 "default_title": "我是pageAction",
 "default_popup": "popup.html"
 &#125;,*/</span>
 <span class="hljs-comment">// 需要直接注入页面的JS</span>
 <span class="hljs-string">"content_scripts"</span>: 
 [
 &#123;
 <span class="hljs-comment">//"matches": ["http://*/*", "https://*/*"],</span>
 <span class="hljs-comment">// "<all_urls>" 表示匹配所有地址</span>
 <span class="hljs-string">"matches"</span>: [<span class="hljs-string">"<all_urls>"</span>],
 <span class="hljs-comment">// 多个JS按顺序注入</span>
 <span class="hljs-string">"js"</span>: [<span class="hljs-string">"js/jquery-1.8.3.js"</span>, <span class="hljs-string">"js/content-script.js"</span>],
 <span class="hljs-comment">// JS的注入可以随便一点，但是CSS的注意就要千万小心了，因为一不小心就可能影响全局样式</span>
 <span class="hljs-string">"css"</span>: [<span class="hljs-string">"css/custom.css"</span>],
 <span class="hljs-comment">// 代码注入的时间，可选值： "document_start", "document_end", or "document_idle"，最后一个表示页面空闲时，默认document_idle</span>
 <span class="hljs-string">"run_at"</span>: <span class="hljs-string">"document_start"</span>
 &#125;,
 <span class="hljs-comment">// 这里仅仅是为了演示content-script可以配置多个规则</span>
 &#123;
 <span class="hljs-string">"matches"</span>: [<span class="hljs-string">"*://*/*.png"</span>, <span class="hljs-string">"*://*/*.jpg"</span>, <span class="hljs-string">"*://*/*.gif"</span>, <span class="hljs-string">"*://*/*.bmp"</span>],
 <span class="hljs-string">"js"</span>: [<span class="hljs-string">"js/show-image-content-size.js"</span>]
 &#125;
 ],
 <span class="hljs-comment">// 权限申请</span>
 <span class="hljs-string">"permissions"</span>:
 [
 <span class="hljs-string">"contextMenus"</span>, <span class="hljs-comment">// 右键菜单</span>
 <span class="hljs-string">"tabs"</span>, <span class="hljs-comment">// 标签</span>
 <span class="hljs-string">"notifications"</span>, <span class="hljs-comment">// 通知</span>
 <span class="hljs-string">"webRequest"</span>, <span class="hljs-comment">// web请求</span>
 <span class="hljs-string">"webRequestBlocking"</span>,
 <span class="hljs-string">"storage"</span>, <span class="hljs-comment">// 插件本地存储</span>
 <span class="hljs-string">"http://*/*"</span>, <span class="hljs-comment">// 可以通过executeScript或者insertCSS访问的网站</span>
 <span class="hljs-string">"https://*/*"</span> <span class="hljs-comment">// 可以通过executeScript或者insertCSS访问的网站</span>
 ],
 <span class="hljs-comment">// 普通页面能够直接访问的插件资源列表，如果不设置是无法直接访问的</span>
 <span class="hljs-string">"web_accessible_resources"</span>: [<span class="hljs-string">"js/inject.js"</span>],
 <span class="hljs-comment">// 插件主页，这个很重要，不要浪费了这个免费广告位</span>
 <span class="hljs-string">"homepage_url"</span>: <span class="hljs-string">"https://www.baidu.com"</span>,
 <span class="hljs-comment">// 覆盖浏览器默认页面</span>
 <span class="hljs-string">"chrome_url_overrides"</span>:
 &#123;
 <span class="hljs-comment">// 覆盖浏览器默认的新标签页</span>
 <span class="hljs-string">"newtab"</span>: <span class="hljs-string">"newtab.html"</span>
 &#125;,
 <span class="hljs-comment">// Chrome40以前的插件配置页写法</span>
 <span class="hljs-string">"options_page"</span>: <span class="hljs-string">"options.html"</span>,
 <span class="hljs-comment">// Chrome40以后的插件配置页写法，如果2个都写，新版Chrome只认后面这一个</span>
 <span class="hljs-string">"options_ui"</span>:
 &#123;
 <span class="hljs-string">"page"</span>: <span class="hljs-string">"options.html"</span>,
 <span class="hljs-comment">// 添加一些默认的样式，推荐使用</span>
 <span class="hljs-string">"chrome_style"</span>: <span class="hljs-literal">true</span>
 &#125;,
 <span class="hljs-comment">// 向地址栏注册一个关键字以提供搜索建议，只能设置一个关键字</span>
 <span class="hljs-string">"omnibox"</span>: &#123; <span class="hljs-string">"keyword"</span> : <span class="hljs-string">"go"</span> &#125;,
 <span class="hljs-comment">// 默认语言</span>
 <span class="hljs-string">"default_locale"</span>: <span class="hljs-string">"zh_CN"</span>,
 <span class="hljs-comment">// devtools页面入口，注意只能指向一个HTML文件，不能是JS文件</span>
 <span class="hljs-string">"devtools_page"</span>: <span class="hljs-string">"devtools.html"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>content-scripts</li>
</ol>
<p>需要直接注入页面的文件，借助content-scripts我们可以实现通过配置的方式向指定的页面中注入JS和CSS</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
&#123;
 <span class="hljs-comment">// 需要直接注入页面的JS</span>
 <span class="hljs-string">"content_scripts"</span>: 
 [
 &#123;
 <span class="hljs-comment">//"matches": ["http://*/*", "https://*/*"],</span>
 <span class="hljs-string">"matches"</span>: [<span class="hljs-string">"<all_urls>"</span>],<span class="hljs-comment">// 表示匹配所有地址</span>
 <span class="hljs-comment">// 多个JS按顺序注入</span>
 <span class="hljs-string">"js"</span>: [<span class="hljs-string">"js/xxx.js"</span>, <span class="hljs-string">"js/xx.js"</span>],
 <span class="hljs-comment">// CSS要注意顺序，因为一不小心就可能影响全局样式</span>
 <span class="hljs-string">"css"</span>: [<span class="hljs-string">"css/xx.css"</span>],
 <span class="hljs-comment">// 代码注入的时间，可选值： "document_start", "document_end", or "document_idle"，最后一个表示页面空闲时，默认document_idle</span>
 <span class="hljs-string">"run_at"</span>: <span class="hljs-string">"document_start"</span>
 &#125;
 ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>background</li>
</ol>
<p>是一个常驻的页面，它的生命周期是插件中所有类型页面中最长的，它随着浏览器的打开而打开，随着浏览器的关闭而关闭，所以通常把需要一直运行的、启动就运行的、全局的代码放在background里面。</p>
<p>配置中，background可以通过page指定一张网页，也可以通过scripts直接指定一个JS，Chrome会自动为这个JS生成一个默认的网页：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
 <span class="hljs-comment">// 会一直常驻的后台JS或后台页面</span>
 <span class="hljs-string">"background"</span>:
 &#123;
 <span class="hljs-comment">// 如果指定JS，那么会自动生成一个背景页</span>
 <span class="hljs-string">"page"</span>: <span class="hljs-string">"background.html"</span>
 <span class="hljs-comment">//"scripts": ["js/background.js"]</span>
 &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>
<p>chrome的展示形式</p>
<p>这里给大家介绍几种较为常见的展示形式</p>
<p>1.浏览器右上角</p>
<pre><code class="copyable">    通过配置browser_action可以在浏览器的右上角增加一个图标，我们上面的小demo已经使用了，所以就不做详细说明了
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p>右键菜单</p>
<p>通过开发Chrome插件可以自定义浏览器的右键菜单，主要是通过chrome.contextMenusAPI实现</p>
</li>
</ol>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">     

<span class="hljs-comment">// manifest.json</span>
&#123;
<span class="hljs-string">"permissions"</span>: [<span class="hljs-string">"contextMenus"</span>， <span class="hljs-string">"tabs"</span>],
<span class="hljs-string">"background"</span>:&#123;
      <span class="hljs-string">"scripts"</span>: [<span class="hljs-string">"js/background.js"</span>]
      &#125;
&#125;
<span class="hljs-comment">// background.js</span>
chrome.contextMenus.create(&#123;
 <span class="hljs-attr">title</span>: <span class="hljs-string">'使用度娘搜索：%s'</span>, <span class="hljs-comment">// %s表示选中的文字</span>
 <span class="hljs-attr">contexts</span>: [<span class="hljs-string">'selection'</span>], <span class="hljs-comment">// 只有当选中文字时才会出现此右键菜单</span>
 <span class="hljs-attr">onclick</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>)
 </span>&#123;
 <span class="hljs-comment">// 注意不能使用location.href，因为location是属于background的window对象</span>
 chrome.tabs.create(&#123;<span class="hljs-attr">url</span>: <span class="hljs-string">'https://www.baidu.com/s?ie=utf-8&wd='</span> + <span class="hljs-built_in">encodeURI</span>(params.selectionText)&#125;);
 &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b453cc11cf34fc5be4046bebaa697d3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3.devtools(开发者工具)</p>
<p>我们应该在开发的过程中都用过这样的插件
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a92c0a8672e44e2ea7d3fb8d2b46c00a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们自己的插件其实也是可以插入到这个位置的，具体做法如下</p>
<p>在manifest.json中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
&#123;
 <span class="hljs-comment">// 只能指向一个HTML文件，不能是JS文件</span>
 <span class="hljs-string">"devtools_page"</span>: <span class="hljs-string">"devtools.html"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建文件devtools.html</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span><span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"js/devtools.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建devtools.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//MyTest 插件名，index.html 插件展示的内容</span>
chrome.devtools.panels.create(<span class="hljs-string">'MyTest'</span>, <span class="hljs-string">'icons/crm.png'</span>, <span class="hljs-string">'index.html'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">panel</span>)
</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'自定义面板创建成功！'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>获取当前窗口ID</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">     

chrome.windows.getCurrent(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">currentWindow</span>)
</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'当前窗口ID：'</span> + currentWindow.id);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.获取当前选项卡id</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">// 获取当前选项卡ID</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCurrentTabId</span>(<span class="hljs-params">callback</span>)
</span>&#123;
 chrome.tabs.query(&#123;<span class="hljs-attr">active</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">currentWindow</span>: <span class="hljs-literal">true</span>&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">tabs</span>)
 </span>&#123;
 <span class="hljs-keyword">if</span>(callback) callback(tabs.length ? tabs[<span class="hljs-number">0</span>].id: <span class="hljs-literal">null</span>);
 &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>7.本地存储</p>
<p>我们在开发中使用的本地存储一般都是sessionStorage或者localStorage等，在chrome的插件开发中，比较建议使用chrome.storage，理由如下：</p>
<p>chrome.storage是针对插件全局的，即使你在background中保存的数据，在content-script也能获取到
chrome.storage.sync可以跟随当前登录用户自动同步，这台电脑修改的设置会自动同步到其它电脑，很方便，如果没有登录或者未联网则先保存到本地，可以等登录了再同步至网络</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 读取数据，第一个参数是指定要读取的key以及设置默认值</span>
chrome.storage.sync.get(&#123;<span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">items</span>) </span>&#123;
 <span class="hljs-built_in">console</span>.log(items.color, items.age);
&#125;);
<span class="hljs-comment">// 保存数据</span>
chrome.storage.sync.set(&#123;<span class="hljs-attr">color</span>: <span class="hljs-string">'blue'</span>&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'保存成功！'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是此次分享的全部内容了，本次是入门级别的分享，仅仅用于了解chrome的开发，以及熟悉一些配置项。想要深入开发，还是需要参照官方文档哦～</p>
<p>本文参考了： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bookstack.cn%2Fread%2Fchrome-plugin-develop%2Fspilt.2.spilt.7.8bdb1aac68bbdc44.md" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bookstack.cn/read/chrome-plugin-develop/spilt.2.spilt.7.8bdb1aac68bbdc44.md" ref="nofollow noopener noreferrer">www.bookstack.cn/read/chrome…</a></p>
<p>参考的文档写的特别细致，里面有很多东西本文没有涉及到，比如通信，动态注入等等，感兴趣的话，可以自行查看哈</p>
<p>​</p></div>  
</div>
            