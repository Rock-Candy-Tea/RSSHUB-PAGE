
---
title: '避免将 JWT 存储在 localStorage 中 _  8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f2027086ea742ae8c0ceb2664061fcc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 04:08:31 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f2027086ea742ae8c0ceb2664061fcc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在文章中《<a href="https://juejin.cn/post/6991285683075678216" target="_blank" title="https://juejin.cn/post/6991285683075678216">Web 身份验证：Cookie 与 Token</a>》介绍过使用 <code>Token</code> 的好处，如无状态、自我存储等， 也提到过将 <code>Token</code> 存储在 <code>Cookie</code> 中的方式。可能有人会疑问，使用了 Token 为什么还用 <code>Cookie</code>，可以把 <code>Token</code> 存储在本地，如 <code>localStorage</code> 。</p>
<p>看到很多文章介绍将 JWT 存储在 <code>localStorage</code> 中，事实上，个人觉得建议最好不要。这就是将敏感信息存储在 <code>localStorage</code> 中，对于安全问题来说是个挑战，对于客户端的行为在安全问题上多数是不可靠的。</p>
<p>先简单介绍一下本地存储。</p>
<h3 data-id="heading-0">本地存储</h3>
<p><code>localStorage</code> 是 HTML5 的一项新特征，它基本上允许 Web 开发人员使用 JavaScript 在用户的浏览器中存储想要的任何信息，十分简单。</p>
<p>在操作上，<code>localStorage</code> 只是一个可以添加或删除数据的 JavaScript 对象，下面是一段 <code>localStorage</code> 操作的示例代码，该代码片段将创建一个指定 <code>Key</code> 的<code>localStorage</code> 数据，并可以为其更新、删除数据。</p>
<pre><code class="copyable">export const useStorage = (
    valKey = "authorization",
    keyPrefix = "DevPoint"
) => &#123;
    const localKey = `$&#123;valKey&#125;.$&#123;keyPrefix&#125;`;
    const save = (data) => &#123;
        window.localStorage.setItem(localKey, JSON.stringify(deepCopy(data)));
    &#125;;
    const get = () => &#123;
        const localData = window.localStorage.getItem(localKey);
        if (localData && localData !== "") &#123;
            return JSON.parse(localData);
        &#125; else &#123;
            return false;
        &#125;
    &#125;;
    /**
     * 清除 localStorage 中 valKey 的值
     */
    const clear = () => &#123;
        window.localStorage.setItem(localKey, "");
    &#125;;
    return &#123;
        save,
        get,
        clear,
    &#125;;
&#125;;
// 清除所有的 localStorage
export const cleanAll = () => &#123;
    window.localStorage.clear();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开浏览器开发工具，在控制台窗口的 <code>Application</code> 的标签页下看到，左侧的 <code>Storage</code> 可以看到，如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f2027086ea742ae8c0ceb2664061fcc~tplv-k3u1fbpfcp-watermark.image" alt="jwt1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>localStorage</code> 是一个纯 JavaScript 对象。如果正在构建一个单页面站点，使用 <code>localStorage</code> 之类的东西意味着网页可以独立于任何 Web 服务器运行，只需要浏览器存储空间，而无需在服务器中存储任何数据。</p>
<p>此外，<code>localStorage</code> 的好处是大小限制：像 <code>Cookie</code> 一般是 <code>4KB</code> 的大小限制，而 <code>localStorage</code> 在所有主流浏览器中至少<code> 5MB</code> 的数据存储。因此现在也越来越多的 Web 应用使用 <code>localStorage</code> 来存储一些数据。</p>
<h3 data-id="heading-1">安全问题</h3>
<p><code>localStorage</code> 尽管使用简单，但在安全问题上，没有任何的保护措施，这就意味着敏感信息存储在 <code>localStorage</code> 会带来安全问题。</p>
<p>将任何敏感信息存储在<code>localStorage</code> 中相当于在互联网中发布了这些信息。<code>localStorage</code> 设计的目的是为浏览器增加本地存储机制，被设计为简单的 <code>key/avalue</code> 存储，开发人员可以使用它来构建稍微复杂的单页应用程序。</p>
<blockquote>
<p>当将敏感信息存储在 <code>localStorage</code>  中时，实际上是在使用世界上最危险的东西 <code>JavaScript</code> 将最敏感的信息存储在有史以来最糟糕的保险库中，绝对不是一个好注意</p>
</blockquote>
<p>如果攻击者可以在您的网站上运行 JavaScript，他们就可以检索您存储在 <code>localStorage</code>  中的所有数据并将其发送到他们自己的域中。这意味着存储在 <code>localStorage</code> 中的敏感信息都有可能受到损害。</p>
<p>当然可能有足够的信息认为 Javascipt 无法在您的站点中运行，但是如果您的站点包含来自域外源的第三方 JavaScript 代码，例如一些第三方脚本库的CDN源：</p>
<ul>
<li>bootstrap 源</li>
<li>jQuery</li>
<li>广告脚本</li>
<li>谷歌分析链接</li>
<li>跟踪脚本</li>
<li>...</li>
</ul>
<p>一旦出现第三方脚本库被攻击了就会带来安全上的威胁，或许不曾使用第三方脚本库，又或者第三方脚本库绝对安全。</p>
<blockquote>
<p>如果需要考虑所有可能的场景，为了降低安全事故的风险，建议尽量不要在 <code>localStorage</code>  中存储任何重要的敏感信息。</p>
</blockquote>
<p>JWT 本质上与<code>用户名/密码</code> 在功能上相同，一旦知道 JWT 就相当于知道了用户名和密码。</p>
<p>如果攻击者可以获得 JWT 副本，就可以神不知鬼不觉的伪造请求向网站发出请求，因此建议不要将敏感信息存储在 <code>localStorage</code>  中。</p>
<h3 data-id="heading-2">JWT存储在 HttpOnly Cookie</h3>
<p>本文只是介绍了将 JWT 存储在 <code>localStorage</code> 的不好，不推荐这样使用。</p>
<p>建议的方式是将JWT存储在 <code>HttpOnly Cookie</code> 中，优点是不需要在 JavaScript 代码中处理 <code>Token</code> , 后续请求中都会自动跟上 Token 信息的 <code>Cookie</code>。</p>
<p>再者 Cookie 的 HttpOnly 标签是防御 <code>XSS</code> 的解决方案之一，因为 <code>HttpOnly</code> 在简单的条件下阻止客户端（JavaScript）访问 <code>Cookie</code>。如果再将 <code>secure</code> 标志设置为 <code>true</code>，则只会在安全或加密的网络中使用 <code>Cookie</code>，从而增加其安全性。</p>
<p>虽然上面的方式可以防御 <code>XSS</code> ，但还存在另一个威胁即跨站请求伪造（CSRF），可以采用 CORS 白名单机制，并且 CSRF 令牌（可以参阅《<a href="https://juejin.cn/post/6966887553588789262" target="_blank" title="https://juejin.cn/post/6966887553588789262">CSRF 攻击：解析、预防和 CSRF 令牌</a>》）与 JWT 一起使用。</p>
<p>但是在某些情况下，例如当 API 被移动应用程序使用并且它需要 <code>Authorization Bearer xxx</code> 标头而不是 <code>Cookie</code> 时，或者当需要使用同一个 JWT 向多个后端发出 HTTP 请求时，把 JWT 存在 <code>localStorage</code> 中的方案就更方便。</p>
<blockquote>
<p>还有一点 Cookie 存储的大小为 4KB ，因此在使用这个方案的时候需要注意 JWT 的大小。如果 JWT 超过了 <code>4KB</code> 就不适合使用 Cookie 存储 JWT的方案。</p>
</blockquote>
<h3 data-id="heading-3">总结</h3>
<p>JWT 是一个非常流行的标准，可以使用签名来信任请求，并在各方之间安全的交换信息。在实际项目开发中，建议避免将 JWT 存储在 <code>localStorage</code> 中，而是存储在 <code>HttpOnly Cookie</code>  。</p></div>  
</div>
            