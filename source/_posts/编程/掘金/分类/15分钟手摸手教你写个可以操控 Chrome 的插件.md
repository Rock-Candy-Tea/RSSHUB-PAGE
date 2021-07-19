
---
title: '15分钟手摸手教你写个可以操控 Chrome 的插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 17:07:55 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>翁佳瑞，微医前端技术部前端工程师。</p>
</blockquote>
<h2 data-id="heading-0">故事背景</h2>
<p>事情是这样的呢</p>
<p>友人 A: 能不能帮我整一个 chrome 插件？</p>
<p>我: 啥插件？</p>
<p>友人 A: 通过后端服务或者 python 脚本通信 chrome 插件能够操作浏览器</p>
<p>我: 你小子是想爬数据吧？直接用现成的 python 框架或者 谷歌的 puppeteer 就能操控浏览器吧</p>
<p>友人 A: 你说的路子我早就试过了，对于反爬检测高的的网站一下就能检测你的无头浏览器的相应特征，所以就用平时用的浏览器就能以真乱真</p>
<p>我: 老是整这些花里胡哨的，有啥用呀</p>
<p>友人 A: 10 斤小龙虾!</p>
<p>我:成交!!!</p>
<h2 data-id="heading-1">整体的思路</h2>
<p>根据朋友以上的要求，我们可以简单的得出一下的通信流程：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a95a2ec9a52640208a05d07e30256600~tplv-k3u1fbpfcp-watermark.image" alt="flow.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体有疑问没关系，我们只要知道大体的流程是这样通信的即可</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FDseekers%2Fextensions_control" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Dseekers/extensions_control" ref="nofollow noopener noreferrer">github 地址</a> 每个 commit 对应相应的步骤</p>
<h2 data-id="heading-2">第一步 创建一个 chrome 插件</h2>
<p>我们首先来创建一个啥功能都没有的 chrome 插件</p>
<p>目录如下所示</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87ef2ab1a8d144db88516f224a36e7c9~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">manifest.json</h3>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// manifest.json</span>
&#123;
    <span class="hljs-attr">"manifest_version"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 配置文件的版本</span>
    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"SocketEXController"</span>, <span class="hljs-comment">// 插件的名称</span>
    <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>, <span class="hljs-comment">// 插件的版本</span>
    <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Chrome SocketEXController"</span>,<span class="hljs-comment">// 插件描述</span>
    <span class="hljs-attr">"author"</span>: <span class="hljs-string">"wjryours"</span>, <span class="hljs-comment">// 作者</span>
    <span class="hljs-attr">"icons"</span>: &#123;
        <span class="hljs-attr">"48"</span>: <span class="hljs-string">"icon.png"</span>,<span class="hljs-comment">// 对应尺寸的图标路径 我这边全部用一个了</span>
        <span class="hljs-attr">"128"</span>: <span class="hljs-string">"icon.png"</span>
    &#125;,
    <span class="hljs-attr">"browser_action"</span>: &#123;
        <span class="hljs-attr">"default_icon"</span>: <span class="hljs-string">"icon.png"</span>, <span class="hljs-comment">// 图标</span>
        <span class="hljs-attr">"default_popup"</span>: <span class="hljs-string">"popup.html"</span> <span class="hljs-comment">// 点击右上角的图标的 popup 浮层 html 文件</span>
    &#125;,
    <span class="hljs-attr">"background"</span>: &#123;
        <span class="hljs-comment">// 会一直常驻的后台 JS 或后台页面</span>
        <span class="hljs-comment">// 2 种指定方式，如果指定 JS，那么会自动生成一个背景页</span>
        <span class="hljs-attr">"page"</span>: <span class="hljs-string">"background.html"</span>
    &#125;,
    <span class="hljs-attr">"content_scripts"</span>: [
        &#123;
            <span class="hljs-comment">// 允许哪些域名下加载 注入的 JS</span>
            <span class="hljs-comment">// "matches": ["http://*/*", "https://*/*"],</span>
            <span class="hljs-comment">// "<all_urls>" 表示匹配所有地址</span>
            <span class="hljs-attr">"matches"</span>: [
                <span class="hljs-string">"<all_urls>"</span>
            ],
            <span class="hljs-attr">"js"</span>: [
                <span class="hljs-string">"content-script.js"</span>
            ],
            <span class="hljs-attr">"run_at"</span>: <span class="hljs-string">"document_start"</span>
        &#125;
    ],
    <span class="hljs-attr">"permissions"</span>: [
        <span class="hljs-string">"contextMenus"</span>, <span class="hljs-comment">// 右键菜单</span>
        <span class="hljs-string">"tabs"</span>, <span class="hljs-comment">// 标签</span>
        <span class="hljs-string">"notifications"</span>, <span class="hljs-comment">// 通知</span>
        <span class="hljs-string">"webRequest"</span>, <span class="hljs-comment">// web 请求</span>
        <span class="hljs-string">"webRequestBlocking"</span>, <span class="hljs-comment">// 阻塞式 web 请求</span>
        <span class="hljs-string">"storage"</span>, <span class="hljs-comment">// 插件本地存储</span>
        <span class="hljs-string">"http://*/*"</span>, <span class="hljs-comment">// 可以通过 executeScript 或者 insertCSS 访问的网站</span>
        <span class="hljs-string">"https://*/*"</span> <span class="hljs-comment">// 可以通过 executeScript 或者 insertCSS 访问的网站</span>
    ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// background.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'background.js'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// popup.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'popup.js'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// content-script.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'content-script.js loaded'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">html</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- popup --></span>
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>SocketController Popup<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"./lib/css/popup.css"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./popup.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    popup
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- background --></span>
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>SocketController<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bg-container"</span>></span>
        bg-container
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 chrome 的扩展程序页加载我们的文件目录 即可</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/526d0a7b3aed4580bdfbe58d73de61f9~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们启用插件 随手打开一个页面就发现我们的插件已经生效了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b932b703aaae48198f99b14bd9c645e0~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/899480272ff6406fa06523974a149728~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">第二步 在本地创建 websocket 的服务</h2>
<p>正如上面的通信流程所示，我们还需要在本地创建一个可用的 websocket 来发送信息给 chrome 插件</p>
<p>为了方便起见，我这边就用 node 的 express 以及 socket.io 这个库来启用</p>
<p>目录结构和代码都很简单</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cae24db09d244be3ba9bd9d896c03f47~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js  用来创建 node 服务</span>
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-keyword">const</span> app = express()
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>)
<span class="hljs-keyword">const</span> server = http.createServer(app)
<span class="hljs-keyword">const</span> &#123; Server &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"socket.io"</span>)
<span class="hljs-keyword">const</span> io = <span class="hljs-keyword">new</span> Server(server)

app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    res.sendFile(__dirname + <span class="hljs-string">'/index.html'</span>)
&#125;)

io.on(<span class="hljs-string">'connection'</span>, <span class="hljs-function">(<span class="hljs-params">socket</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a user connected'</span>)
    socket.on(<span class="hljs-string">'disconnect'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'user disconnected'</span>);
    &#125;);
    socket.on(<span class="hljs-string">'webviewEvent'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'webviewEvent: '</span> + msg);
        io.emit(<span class="hljs-string">'webviewEvent'</span>, msg);
        <span class="hljs-comment">// socket.broadcast.emit('chat message', msg);</span>
    &#125;);
    socket.on(<span class="hljs-string">'webviewEventCallback'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'webviewEventCallback: '</span> + msg);
        io.emit(<span class="hljs-string">'webviewEventCallback'</span>, msg);
    &#125;);
&#125;)


server.listen(<span class="hljs-number">9527</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'listening on 9527'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- index.html --></span> 
<span class="hljs-comment"><!-- 点击事件传递的参数后续会用到，这里可以不去了解 --></span>
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Socket.IO Page<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="xml">
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"SendInput"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"SendInputevent"</span>></span>Send input event<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"SendClickevent"</span>></span>Send click event<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"SendGetTextevent"</span>></span>Send getText event<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/socket.io/socket.io.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> socket = io();

  <span class="hljs-keyword">var</span> form = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'form'</span>);
  <span class="hljs-keyword">var</span> input = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'input'</span>);

  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'SendClickevent'</span>).addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
    socket.emit(<span class="hljs-string">'webviewEvent'</span>, &#123; <span class="hljs-attr">event</span>: <span class="hljs-string">'click'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">delay</span>: <span class="hljs-number">300</span> &#125;, <span class="hljs-attr">element</span>: <span class="hljs-string">'#su'</span>, <span class="hljs-attr">operateTabIndex</span>: <span class="hljs-number">0</span> &#125;);
  &#125;)
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'SendInputevent'</span>).addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'SendInput'</span>).value
    socket.emit(<span class="hljs-string">'webviewEvent'</span>, &#123; <span class="hljs-attr">event</span>: <span class="hljs-string">'input'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">inputValue</span>: value &#125;, <span class="hljs-attr">element</span>: <span class="hljs-string">'#kw'</span>, <span class="hljs-attr">operateTabIndex</span>: <span class="hljs-number">0</span> &#125;);
  &#125;)
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'SendGetTextevent'</span>).addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
    socket.emit(<span class="hljs-string">'webviewEvent'</span>, &#123; <span class="hljs-attr">event</span>: <span class="hljs-string">'getElementText'</span>, <span class="hljs-attr">params</span>: &#123;&#125;, <span class="hljs-attr">element</span>: <span class="hljs-string">'.result.c-container.new-pmd .t a'</span>, <span class="hljs-attr">operateTabIndex</span>: <span class="hljs-number">0</span> &#125;);
  &#125;)

  socket.on(<span class="hljs-string">'webviewEventCallback'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(msg)
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"socket-service"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>,
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"nodemon index.js"</span>
  &#125;,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"express"</span>: <span class="hljs-string">"^4.17.1"</span>,
    <span class="hljs-attr">"nodemon"</span>: <span class="hljs-string">"^2.0.7"</span>,
    <span class="hljs-attr">"socket.io"</span>: <span class="hljs-string">"^4.1.2"</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的内容也很简单，就是使用 express 和 socket.io 创建了一个 node 服务支持长链接，对于 socket.io 想有更多的了解的可以参照 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsocket.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://socket.io/" ref="nofollow noopener noreferrer">官方文档</a></p>
<p>运行 npm run dev 即可</p>
<p>好的，这样我们的服务就跑起来了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2914a178841740a8a183b926090214dc~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A9527" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:9527" ref="nofollow noopener noreferrer">http://localhost:9527</a></p>
<p>并点击页面上的按钮在命令行上有 log 输出就说明连接成功啦!</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5c50111766c4281aa8f3267f39a04c7~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">第三步 开始使 chrome 插件 与 本地的 node 服务相互通信</h2>
<p>在开始与 node 服务通信前我们要了解下 chrome 插件的几种 js 的使用场景</p>
<h4 data-id="heading-8">content-scripts</h4>
<p>这个主要功能就是 Chrome 插件中向页面注入脚本
在第一步的操作中正是该文件在别的页面控制台中打印出了我们期望的 log
content-scripts 和 原始页面共享 DOM，但是不共享 JS
但是这个功能足以让我们去操作目标页面了</p>
<h4 data-id="heading-9">background.js</h4>
<p>是一个常驻的页面，它的生命周期是插件中所有类型页面中最长的，它随着浏览器的打开而打开，
随着浏览器的关闭而关闭，所以通常把需要一直运行的、启动就运行的、全局的代码放在 background 里面</p>
<h4 data-id="heading-10">popup.js</h4>
<p>这个就是点击浏览器右上角的插件图标展示的弹窗，生命周期很短，可以将临时的交互写在这里</p>
<p>对于我们这次要长时间驻存在浏览器后台与服务通信的要求得出 我们将相应的写在 background.js 中即可</p>
<p>我们这里将需要的 js 库 和 background.js 引入到 background.html 中</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./lib/js/lodash.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./lib/js/socket.io.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./background.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以使用两种方式来调试 这个常驻后台文件</p>
<p>1.直接在 chrome 拓展点击对应按钮即可弹出调试</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d6550af0ce54f2e9d04491c6e22611a~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01fd866ee3e44d85b6a8be30ab5c2d1c~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.直接在浏览器上输入对应的地址 即可</p>
<pre><code class="copyable">chrome-extension://$&#123;extensionID&#125;/background.html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次更新代码点击按钮刷新即可</p>
<p>为了调试方便起见我在 popup.js 中加入了以下代码
每次点击我们的插件图标即可新开一个后台页面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> extensionId = chrome.runtime.id
<span class="hljs-keyword">const</span> backgroundURL = <span class="hljs-string">`chrome-extension://<span class="hljs-subst">$&#123;extensionId&#125;</span>/background.html`</span>
<span class="hljs-built_in">window</span>.open(backgroundURL)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们只需要在 background.js 中编写相应代码，建立长链接就可以了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// background.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BackgroundService</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.socketIoURL = <span class="hljs-string">'http://localhost:9527'</span>
        <span class="hljs-built_in">this</span>.socketInstance = &#123;&#125;
        <span class="hljs-built_in">this</span>.socketRetryMax = <span class="hljs-number">5</span>
        <span class="hljs-built_in">this</span>.socketRetry = <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'background.js'</span>)   
        <span class="hljs-built_in">this</span>.connectSocket()
        <span class="hljs-built_in">this</span>.linstenSocketEvent()
    &#125;
    <span class="hljs-function"><span class="hljs-title">setSocketURL</span>(<span class="hljs-params">url</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.socketIoURL = url
    &#125;
    <span class="hljs-function"><span class="hljs-title">connectSocket</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (!_.isEmpty(<span class="hljs-built_in">this</span>.socketInstance) && _.isFunction(<span class="hljs-built_in">this</span>.socketInstance.disconnect)) &#123;
            <span class="hljs-built_in">this</span>.socketInstance.disconnect()
        &#125;
        <span class="hljs-built_in">this</span>.socketInstance = io(<span class="hljs-built_in">this</span>.socketIoURL);
        <span class="hljs-built_in">this</span>.socketRetry = <span class="hljs-number">0</span>
        <span class="hljs-built_in">this</span>.socketInstance.on(<span class="hljs-string">'connect_error'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'connect_error'</span>, e)
            <span class="hljs-built_in">this</span>.socketRetry++
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.socketRetryMax < <span class="hljs-built_in">this</span>.socketRetry) &#123;
                <span class="hljs-built_in">this</span>.socketInstance.close()
                alert(<span class="hljs-string">`以尝试连接<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.socketRetryMax&#125;</span>次，无法连接到 socket 服务，请排查服务是否可用`</span>)
            &#125;
        &#125;)
    &#125;
    <span class="hljs-function"><span class="hljs-title">linstenSocketEvent</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (!_.isEmpty(<span class="hljs-built_in">this</span>.socketInstance) && _.isFunction(<span class="hljs-built_in">this</span>.socketInstance.on)) &#123;
            <span class="hljs-built_in">this</span>.socketInstance.on(<span class="hljs-string">'webviewEvent'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`webviewEvent msg`</span>, msg)
            &#125;);
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> BackgroundService()
app.init()

<span class="copy-code-btn">复制代码</span></code></pre>
<p>刷新插件，打开插件后台页面 就可以看见链接建立成功，然后从 node 服务发送 msg 给 chrome 插件，我们就可以看到信息被成功接收了</p>
<p>(tips:之前的 node 服务别忘记启动)</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d272ce480ccb489e9bba2c84d51fc81d~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">第四步 开始使 chrome 插件 background.js 与 content-script.js 建立通信</h2>
<p>这一步也是相当简单，chrome 官方的文档也有很多介绍
我这边就写下实现步骤</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改 background.js 为如下代码</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">emitMessageToSocketService</span>(<span class="hljs-params">socketInstance, params = &#123;&#125;</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!_.isEmpty(socketInstance) && _.isFunction(socketInstance.emit)) &#123;
        <span class="hljs-built_in">console</span>.log(params)
        <span class="hljs-comment">// 将从 content-script.js 接收到的 msg 发送到 node 服务</span>
        socketInstance.emit(<span class="hljs-string">'webviewEventCallback'</span>, params);
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-title">linstenSocketEvent</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!_.isEmpty(<span class="hljs-built_in">this</span>.socketInstance) && _.isFunction(<span class="hljs-built_in">this</span>.socketInstance.on)) &#123;
        <span class="hljs-built_in">this</span>.socketInstance.on(<span class="hljs-string">'webviewEvent'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`webviewEvent msg`</span>, msg)
            <span class="hljs-comment">// 将从 node 服务接收到的 msg 发送到 content-script.js</span>
            <span class="hljs-built_in">this</span>.sendMessageToContentScript(msg, BackgroundService.emitMessageToSocketService)
        &#125;);
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-title">sendMessageToContentScript</span>(<span class="hljs-params">message, callback</span>)</span> &#123;
    <span class="hljs-keyword">const</span> operateTabIndex = message.operateTabIndex ? message.operateTabIndex : <span class="hljs-number">0</span>
    <span class="hljs-built_in">console</span>.log(message)
    chrome.tabs.query(&#123; <span class="hljs-attr">index</span>: operateTabIndex &#125;, <span class="hljs-function">(<span class="hljs-params">tabs</span>) =></span> &#123; <span class="hljs-comment">// 获取 索引的方式获取对应 tabs 实例以及 id</span>
        chrome.tabs.sendMessage(tabs[<span class="hljs-number">0</span>].id, message, <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123; <span class="hljs-comment">// 发送消息到对应 tab</span>
            <span class="hljs-built_in">console</span>.log(callback)
            <span class="hljs-keyword">if</span> (callback) callback(<span class="hljs-built_in">this</span>.socketInstance, response)
        &#125;);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// content-script.js</span>

chrome.runtime.onMessage.addListener(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">request, sender, sendResponse</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(request, sender, sendResponse)
    sendResponse(res)
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们这边将插件重新加载后关闭浏览器重新打开新浏览器，将需要测试的页面放置在第一个，
然后在我们的 localhost:9527 发送信息
这是我们就能在我们预期的页面接收到对应参数了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/908ff9e32fc941c29de79a47469a372c~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时你可能会看到 2 条 log,其实这个是正常现象,
因为如果你是通过打开了 chrome-extension://xxx/background.html 直接打开后台页 运行一个后台线程
但是真正在后台常驻的还有一个线程
所以相当是 2 个后台接收到了 socket 消息所以就发送 2 次 msg</p>
<h2 data-id="heading-12">第五步 尝试操控浏览器做对应操作</h2>
<p>好的，朋友们，我们终于来到了最后一步了</p>
<p>我们现在已经建立起了这 3 个模块间的联系了
现在无非就是要将从后端发送的消息通过一些判断做一些 js 操作</p>
<p>我们就来完成一个简单的任务，打开百度页面，搜索关键字，并将搜索到的各个 title 获取</p>
<p>我这边为了做演示方便点就直接引入了 jq 来操作 dom
在 js 文件夹下创建 operate.js 以及 jquery.min.js</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// 在 manifest.json 中加入 相应 js</span>
<span class="hljs-string">"content_scripts"</span>: [
    &#123;
        <span class="hljs-attr">"matches"</span>: [
            <span class="hljs-string">"<all_urls>"</span>
        ],
        <span class="hljs-attr">"js"</span>: [
            <span class="hljs-string">"lib/js/jquery.min.js"</span>,
            <span class="hljs-string">"lib/js/operate.js"</span>,
            <span class="hljs-string">"content-script.js"</span>
        ],
        <span class="hljs-attr">"run_at"</span>: <span class="hljs-string">"document_start"</span>
    &#125;
]

<span class="copy-code-btn">复制代码</span></code></pre>
<p>operate.js 主要用来定义一些操作</p>
<p>根据我们上面的小任务，我这边现在这里面加几个简单的事件定义，后续可以支持扩展</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// operate.js</span>
<span class="hljs-keyword">const</span> operateTypeMap = &#123;
    <span class="hljs-attr">CLICK</span>: <span class="hljs-string">'click'</span>,
    <span class="hljs-attr">INPUT</span>: <span class="hljs-string">'input'</span>,
    <span class="hljs-attr">GETELEMENTTEXT</span>: <span class="hljs-string">'getElementText'</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OperateConstant</span> </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">operateByEventType</span>(<span class="hljs-params">type, payload = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-keyword">let</span> res
        <span class="hljs-keyword">switch</span> (type) &#123;
            <span class="hljs-keyword">case</span> operateTypeMap.CLICK:
                res = OperateConstant.handleClickEvent(payload)
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> operateTypeMap.INPUT:
                res = OperateConstant.handleInputEvent(payload)
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> operateTypeMap.GETELEMENTTEXT:
                res = OperateConstant.handleGetElementTextEvent(payload)
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">default</span>:
                <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">return</span> res
    &#125;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">handleClickEvent</span>(<span class="hljs-params">payload</span>)</span> &#123;
        <span class="hljs-keyword">let</span> data = <span class="hljs-literal">null</span>
        <span class="hljs-keyword">if</span> (payload.element) &#123;
            $(payload.element).click()
        &#125;
        <span class="hljs-keyword">return</span> data
    &#125;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">handleInputEvent</span>(<span class="hljs-params">payload</span>)</span> &#123;
        <span class="hljs-keyword">let</span> data = <span class="hljs-literal">null</span>
        <span class="hljs-keyword">if</span> (payload.element) &#123;
            $(payload.element).val(payload.params.inputValue)
        &#125;
        <span class="hljs-keyword">return</span> data
    &#125;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">handleGetElementTextEvent</span>(<span class="hljs-params">payload</span>)</span> &#123;
        <span class="hljs-keyword">let</span> data = []
        <span class="hljs-keyword">if</span> (payload.element && $(payload.element)) &#123;
            <span class="hljs-built_in">Array</span>.from($(payload.element)).forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
                <span class="hljs-keyword">const</span> resItem = &#123;
                    <span class="hljs-attr">value</span>: $(item).text()
                &#125;
                data.push(resItem)
            &#125;)
        &#125;
        <span class="hljs-keyword">return</span> data
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 conent-script.js 使用</p>
<pre><code class="hljs language-js copyable" lang="js">chrome.runtime.onMessage.addListener(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">request, sender, sendResponse</span>) </span>&#123;
    <span class="hljs-keyword">const</span> operateRes =  OperateConstant.operateByEventType(request.event, request)
    <span class="hljs-built_in">console</span>.log(operateRes)
    <span class="hljs-keyword">const</span> res = &#123;
        <span class="hljs-attr">code</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">data</span>: operateRes,
        <span class="hljs-attr">message</span>: <span class="hljs-string">'操作成功'</span>
    &#125;
    sendResponse(res)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好的，我们来试下我们的功能吧
(tips: 请重新加载插件关闭所有 tab 以及确保你想要测试的 tabs 处于第一个)</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86a00012ccde48c1a16d05ed75f5ea5f~tplv-k3u1fbpfcp-watermark.image" alt="demo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以，非常完美</p>
<h2 data-id="heading-13">小结</h2>
<p>好的，朋友们，今天的分享就到这里了，
也许这个插件有许多不完善的地方，主要还是给大家分享个想法和思路，让没接触过 chrome 插件的朋友们也可以尝试下</p>
<h3 data-id="heading-14">参考资料</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fliuxianan%2Fp%2Fchrome-plugin-develop.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/liuxianan/p/chrome-plugin-develop.html" ref="nofollow noopener noreferrer">【干货】Chrome 插件(扩展)开发全攻略</a></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53cfdd9145b941ca84691c83e43a2297~tplv-k3u1fbpfcp-watermark.image" alt="未命名_自定义px_2021-07-18-0.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            