
---
title: 'Chrome Extension MV3迁移checklist'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3894'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 07:10:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=3894'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>目前，Chrome商店中大部分扩展程序都是基于MV2版本开发的。</p>
<p>Chrome浏览器从88版本开始支持MV3啦（即Manifest Version 3），目前查看官方文档时默认已经是MV3版本，Chrome商店在2021年1月也已经开始接收MV3的扩展提交。</p>
<p>本文是一份Chrome扩展开发从<strong>MV2</strong>向<strong>MV3</strong>迁移的备忘清单。</p>
<h2 data-id="heading-1">为什么需要迁移</h2>
<p>两个原因：</p>
<ul>
<li>使用MV3的扩展，在安全性、隐私性和性能方面将会得到增强;</li>
<li>和MV1一样，MV2会被逐步废弃。</li>
</ul>
<p>不过到目前为止，对于MV2的废弃官方还没有给出具体的时间线，但会在MV3稳定支持后，留给开发者至少一年的时间来进行迁移。原文如下：</p>
<blockquote>
<p>While there is not an exact date for removing support for Manifest V2 extensions, developers can expect the migration period to last at least a year from when Manifest V3 lands in the stable channel.</p>
</blockquote>
<p>MV3虽然还没有完全稳定，但我们可以先了解两个版本之间的差异，在开发时尽量避免使用MV3不再支持的特性，减少未来迁移时的工作量。</p>
<h2 data-id="heading-2">修改项·checklist</h2>
<p>以下是迁移至MV3时的一些修改项，目前开发接触到的部分中，<strong>background向service worker的转变</strong>以及<strong>使用webRequest对web请求进行监听修改</strong>这两个部分，相对变更较大，需要调整一定量的代码来完成迁移，其它的部分大多是配置上的变更，配合少量的代码修改即可。</p>
<h3 data-id="heading-3">manifest版本号</h3>
<p>升级第一步，把配置文件中的版本号设置为<code>3</code>。</p>
<pre><code class="copyable">// Manifest V3
"manifest_version": 3 // 版本号由2修改为3

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">从background pages到service workers</h3>
<p>MV3中使用Service Worker替换了原来的背景页，这也是升级时变化比较大的部分。</p>
<p>关于Service Worker的详细内容可以参考<a href="https://developers.google.com/web/fundamentals/primers/service-workers/" target="_blank" rel="nofollow noopener noreferrer">Service Worker简介</a>，这里只讨论扩展升级到MV3时需要做的变更。</p>
<p><strong>首先，在manifest.json中的变化：</strong></p>
<ul>
<li>使用<code>background.service_worker</code>替换原来的<code>background.page</code>或<code>background.scripts</code></li>
<li>文件路径配置由数组变为单字符串；</li>
<li>service worker文件需置于扩展程序文件夹的根目录下，如果仍使用MV2中的相对路径就会报错，service worker无法成功注册。（留心官方文档提示：Service workers must be registered at root level: they cannot be in a nested directory.）</li>
<li>移除<code>background.persistent</code>字段</li>
</ul>
<pre><code class="copyable">  // Manifest V2
  "background": &#123;
   "scripts": ["js/pages/background.js"]
   &#125;,



  // Manifest V3
  "background": &#123;
    // Required
    "service_worker": 'background.js'
  &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>其次，要调整代码以保证能够在service worker中正常运行：</strong></p>
<p>两者最大的区别：MV2中的background scrips被成功注册后是一直运行着的，而MV3中的Service Worker 在不用时会被中止，并在下次有需要时重启。还需要注意的是Service Worker没有直接访问DOM的能力。</p>
<h4 data-id="heading-5">用缓存替换全局变量</h4>
<p>因为Service Worker并不是长期存在的，而是在浏览器会话中重复“启动-执行某些操作-终止”这样的过程，只有在需要的时候才会处于可用的状态，因此如果仍然使用全局变量存储某些数据，程序在重新启动时就会丢失。</p>
<p>在MV3中，可以利用storage API将需要的数据存储在缓存中，需要时从缓存中获取。</p>
<pre><code class="copyable">// MV2
let name = undefined;

chrome.runtime.onMessage.addListener((&#123; type, name &#125;) => &#123;
  if (msg.type === "set-name") &#123;
    name = msg.name;
  &#125;
&#125;);

chrome.browserAction.onClicked.addListener((tab) => &#123;
  chrome.tabs.sendMessage(tab.id, &#123; name &#125;);
&#125;);



// MV3
chrome.runtime.onMessage.addListener((&#123; type, name &#125;) => &#123;
  if (type === "set-name") &#123;
    chrome.storage.local.set(&#123; name &#125;);
  &#125;
&#125;);

chrome.action.onClicked.addListener((tab) => &#123;
  chrome.storage.local.get(["name"], (&#123; name &#125;) => &#123;
    chrome.tabs.sendMessage(tab.id, &#123; name &#125;);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">用alarms替换timers</h4>
<p>setTimeout和setInterval在service worker中可能会失效，因为调度程序在service worker处于终止状态时会取消定时器的执行。</p>
<p>可以用扩展程序中的alarms API来代替定时器，以避免出现定时器失效的问题。</p>
<pre><code class="copyable">// MV2 timers
const TIMEOUT = 3 * 60 * 1000; // 3 minutes
window.setTimeout(() => &#123;
  chrome.action.setIcon(&#123;
    path: getRandomIconPath(),
  &#125;);
&#125;, TIMEOUT);



// MV3 => alarms
chrome.alarms.create(&#123; delayInMinutes: 3.0 &#125;);

chrome.alarms.onAlarm.addListener(() => &#123;
  chrome.action.setIcon(&#123;
    path: getRandomIconPath(),
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">绘制canvas</h4>
<p>如果在背景页中有绘制canvas的场景（例如：用于展示或缓存资源），不要忘记service worker没有直接访问DOM的能力，但可以使用<code> OffscreenCanvas API</code>来做替换。</p>
<p>写法上使用<code>new OffscreenCanvas(width, height)</code>来代替 <code>document.createElement('canvas')</code></p>
<pre><code class="copyable">// MV2
function buildCanvas(width, height) &#123;
  const canvas = document.createElement("canvas");
  canvas.width = width;
  canvas.height = height;
  return canvas;
&#125;



// MV3
function buildCanvas(width, height) &#123;
  const canvas = new OffscreenCanvas(width, height);
  return canvas;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">修改网络请求</h3>
<p>在MV2中，我们使用<code>chrome.webRequest</code>相关的API来拦截和修改web请求；</p>
<p>在MV3中，需要使用新的<code>chrome.declarativeNetRequest</code>来代替。</p>
<p>新的API有以下区别：</p>
<ul>
<li>由Chrome浏览器本身去计算和修改请求，而非像MV2中一样是javascript程序上的拦截和修改。</li>
<li>需要通过指定rules来实现请求的修改，浏览器会在匹配到符合规则的请求和操作时，按照rules中定义好的规则进行修改，程序中不再能直接查看请求的实际内容。</li>
</ul>
<p>以修改web请求中的headers为例，</p>
<p>在MV2中我们可能会在请求发出之前，在监听事件中对headers做一些修改：</p>
<pre><code class="copyable">// MV2

chrome.webRequest.onBeforeSendHeaders.addListener(
details => &#123;
  
  // some modify logic...
  
  return &#123; requestHeaders: details.requestHeaders &#125;;
&#125;,
&#123; urls: ['<all_urls>'] &#125;,
['blocking', 'requestHeaders', 'extraHeaders']
);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在MV3中，首先要在manifest.json中指定rules文件，声明<code>declarativeNetRequest</code>权限：</p>
<pre><code class="copyable">// MV3

&#123;
  "name": "My extension",
  ...

  "declarative_net_request" : &#123;
    "rule_resources" : [&#123;
      "id": "ruleset_1",
      "enabled": true,
      "path": "rules.json"
    &#125;]
  &#125;,
  "permissions": [
    "declarativeNetRequest",
    "declarativeNetRequestFeedback", // 只在需要时声明即可
  ],
  "host_permissions": [ 
    "http://www.blogger.com/",
    "http://*.headers.com/" // 需要重定向或修改headers时需要声明对应的hosts，否则不需要
  ],
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在rules.json文件中，定义修改规则，示例文件：</p>
<pre><code class="copyable">  &#123;
    "id": 1,
    "priority": 1,
    "action": &#123;
      "type": "modifyHeaders",
      "requestHeaders": [
        &#123; "header": "token", "operation": "set", "value": "token value" &#125;,
      ]
      "responseHeaders": [
        &#123; "header": "h1", "operation": "remove" &#125;,
        &#123; "header": "h2", "operation": "set", "value": "v2" &#125;,
        &#123; "header": "h3", "operation": "append", "value": "v3" &#125;
      ]
    &#125;,
    "condition": &#123; "urlFilter": "headers.com/123", "resourceTypes": ["main_frame"] &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，一条规则由以下四个部分组成：</p>
<ul>
<li>id：规则的唯一id</li>
<li>priority：规则的优先级</li>
<li>condition：规则被触发的条件</li>
<li>action：匹配到该条规则时进行的操作</li>
</ul>
<p><code>action</code>指定修改web请求的操作类型：</p>
<ul>
<li>block：阻塞请求</li>
<li>redirect：重定向请求</li>
<li>upgradeScheme</li>
<li>allow</li>
<li>allowAllRequests</li>
<li>modifyHeaders：修改请求头</li>
</ul>
<p>在处理请求时会根据rules里指定的优先级来，具体可以参考<a href="https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest/#matching-algorithm" target="_blank" rel="nofollow noopener noreferrer">Matching algorithm</a>这一节。</p>
<p><code>rules.json</code>静态文件中已经启用(enabled)的规则可以通过<code>updateEnabledRulesets</code>API来更新，但rules在数量上有一定的限制，更新时需要注意，限制相关内容可以参考文档 <a href="https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest/#global-static-rule-limit" target="_blank" rel="nofollow noopener noreferrer">Global Static Rule Limit</a> 一节。</p>
<p>总的来说，新的API这种形式感觉相比MV2来说会更加复杂一些，这里只列出了我开发中用到的一部分内容，在迁移时根据业务场景，可以再仔细阅读下官方文档。</p>
<h3 data-id="heading-9">Host permissions</h3>
<p>MV3对权限声明进行了拆分，新增<code>host_permissions</code>字段单独声明host访问权限，其他权限的声明仍然在<code>permissions</code>字段下。</p>
<pre><code class="copyable">// Manifest V2
"permissions": [
  "tabs",
  "bookmarks",
  "http://www.blogger.com/",
],



// Manifest V3
"permissions": [
  "tabs",
  "bookmarks"
],
"host_permissions": [
  "http://www.blogger.com/",
  "*://*/*"
],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">合并Action API</h3>
<p>MV2中的<code>browser_action</code>和<code>page_action</code>，到MV3中被合并到了单独的<code>action</code> API中，涉及到两个场景的修改：</p>
<p>一、manifest.json中配置的修改</p>
<pre><code class="copyable">// manifest.json

// Manifest V2
&#123;
  "browser_action": &#123; … &#125;,
  "page_action": &#123; … &#125;
&#125;


// Manifest V3
&#123;
  "action": &#123; … &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、在javascript中使用API时的修改：</p>
<pre><code class="copyable">// background.js

// Manifest V2
chrome.browserAction.onClicked.addListener(tab => &#123; … &#125;);
chrome.pageAction.onClicked.addListener(tab => &#123; … &#125;);

// Manifest V3
chrome.action.onClicked.addListener(tab => &#123; … &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">Content security policy</h3>
<p>扩展程序的内容安全策略(CSP)声明方式变更，由字符串改为对象。</p>
<pre><code class="copyable">// Manifest v2
"content_security_policy": "..."


// Manifest v3
"content_security_policy": &#123;
  "extension_pages": "...",
  "sandbox": "..."
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">其它变更</h2>
<ul>
<li>远程托管的代码(Remotely hosted code)：MV3中不再支持非扩展包内的js代码的执行，包括从远程服务器获取的js文件，和程序运行时传给<code>eval</code>的代码字符串，因此所有代码都需要打包在程序包中。</li>
<li>剩下的我这里没太常用，可以参考文档过一下，升级的时候如果有问题，在开发者工具中也会有对应的错误提示，再对照文档修改即可。</li>
</ul>
<h2 data-id="heading-13">参考资料</h2>
<ul>
<li><a href="https://blog.chromium.org/2020/12/manifest-v3-now-available-on-m88-beta.html" target="_blank" rel="nofollow noopener noreferrer">Chromium Blog</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/mv3/intro/mv3-migration/" target="_blank" rel="nofollow noopener noreferrer">Migrating to Manifest V3</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/mv3/mv3-migration-checklist/" target="_blank" rel="nofollow noopener noreferrer">Manifest V3 migration checklist</a></li>
<li><a href="https://developers.google.com/web/fundamentals/primers/service-workers/" target="_blank" rel="nofollow noopener noreferrer">Service Worker简介</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/mv3/migrating_to_service_workers/" target="_blank" rel="nofollow noopener noreferrer">Migrating from background pages to service workers</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest/#method-setExtensionActionOptions" target="_blank" rel="nofollow noopener noreferrer">chrome.declarativeNetRequest API</a></li>
</ul></div>  
</div>
            