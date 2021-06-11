
---
title: 'SameSite 那些事'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/007e172a61bd4ef882b5bc6dcf0ad775~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 19:00:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/007e172a61bd4ef882b5bc6dcf0ad775~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在<a href="https://imnerd.org/web-security-vulnerability-csrf.html" target="_blank" rel="nofollow noopener noreferrer">《Web 安全漏洞之 CSRF》</a>中我们了解到，CSRF 的本质实际上是利用了 Cookie 会自动在请求中携带的特性，诱使用户在第三方站点发起请求的行为。除了文中说的一些解决方式之外，标准还专门为 Cookie 增加了 <code>SameSite</code> 属性，用来规避该问题。Chrome 于 2015 年 6 月支持了该属性，Firefox 和 Safari 紧随其后也增加了支持。<code>SameSite</code> 属性有以下几个值：</p>
<ul>
<li><code>SameSite=None</code>：无论是否跨站都会发送 Cookie</li>
<li><code>SameSite=Lax</code>：允许部分第三方请求携带 Cookie</li>
<li><code>SameSite=Strict</code>：仅允许同站请求携带 Cookie，即当前网页 URL 与请求目标 URL 完全一致</li>
</ul>
<p>该属性适合所有在网页下的请求，包括但不限于网页中的 JS 脚本、图片、iframe、接口等页面内的请求。可以看到 <code>None</code> 是最宽松的，和之前的行为无异。而 <code>Lax</code> 和 <code>Strict</code> 都针对跨站的情况下做了限制。其中 <code>Strict</code> 最为严格，不允许任何跨站情况下携带该 Cookie。<code>Lax</code> 则相对宽松一点，允许了一些显式跳转后的 GET 行为携带。以下是一个带有 <code>SameSite</code> 属性的标准 Cookie 响应示例：</p>
<pre><code class="copyable">Set-Cookie: name=lizheming; SameSite=None; Secure
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，浏览器做了仅针对 HTTPS 域名才支持 <code>SameSite=None</code> 配置。所以如果你要设置 <code>SameSite=None</code> 的话，则必须还要携带 <code>Secure</code> 属性才行。</p>
<h2 data-id="heading-0">Same Site</h2>
<p>Same Site 直译过来就是同站，它和我们之前说的同域 Same Origin 是不同的。两者的区别主要在于判断的标准是不一样的。一个 URL 主要有以下几个部分组成：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/007e172a61bd4ef882b5bc6dcf0ad775~tplv-k3u1fbpfcp-watermark.image" alt="url-object.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到同域的判断比较严格，需要 <code>protocol</code>, <code>hostname</code>, <code>port</code> 三部分完全一致。相对而言，Cookie 中的同站判断就比较宽松，主要是根据 Mozilla 维护的公共后缀表（<a href="https://publicsuffix.org/list/public_suffix_list.dat" target="_blank" rel="nofollow noopener noreferrer">Pulic Suffix List</a>）使用有效顶级域名(eTLD)+1的规则查找得到的一级域名是否相同来判断是否是同站请求。</p>
<p>例如 <code>.org</code> 是在 PSL 中记录的有效顶级域名，<code>imnerd.org</code> 则是一级域名。所以 <code>https://blog.imnerd.org</code> 和 <code>https://www.imnerd.org</code> 是同站域名。而 <code>.github.io</code> 也是在 PSL 中记录的有效顶级域名，所以 <code>https://lizheming.github.io</code> 和 <code>https://blog.github.io</code> 得到的一级域名是不一样的，他们两个是跨域请求。</p>
<p>在类似 GitHub/GitLab Pages, Netlify, Vercel 这种提供子域名给用户建站的第三方服务中，eTLD 的这种同站判断特性往往非常有用。通过将原本是一级域的域名添加到 eTLD 列表中，从而让浏览器认为配有用户名的完整域名才是一级域，有效解决了不同用户站点的 Cookie 共享的问题。</p>
<h3 data-id="heading-1">eTLD</h3>
<p>eTLD 的全称是 effective Top-Level Domain，它与我们往常理解的 Top-Level Domain 顶级域名有所区别。eTLD 记录在之前提到的 PSL 文件中。而 TLD 也有一个记录的列表，那就是 <a href="https://www.iana.org/domains/root/db" target="_blank" rel="nofollow noopener noreferrer">Root Zone Database</a>。RZD 中记录了所有的根域列表，其中不乏一些奇奇怪怪五花八门的后缀。</p>
<p>eTLD 的出现主要是为了解决 <code>.com.cn</code>, <code>.com.hk</code>, <code>.co.jp</code> 这种看起来像是一级域名的但其实需要作为顶级域名存在的场景。这里还可以分享一个有趣的事情，2020年5月份出现了一起阿里云所有 <code>ac.cn</code> 后缀网站解析全部挂掉的事件。原因就是 <code>ac.cn</code> 是中科院申请在册的 eTLD 域名。而阿里云的检测域名备案的脚本不了解规范，没有使用 PSL 列表去查找一级域名，而是使用了<code>.</code>分割的形式去查找的。最终所有 <code>*.ac.cn</code> 的域名由于 <code>ac.cn</code> 这个域名没有进行备案导致解析全部挂掉。而我们现在知道 <code>ac.cn</code> 这个域名是 eTLD 域名，它肯定是无法备案的。</p>
<h3 data-id="heading-2">Schemeful Same Site</h3>
<p>在 Chrome 86/Firefox 79 中，浏览器增加了一个 Schemeful Same Site 的选项，将协议也增加到了 Same Site 的判断规则中。但是并不是完全的不等判断，可以理解是否有 SSL 的区别。例如 <code>http://</code> 和 <code>https://</code> 跨站，但 <code>wss://</code> 和 <code>https://</code> 则是同站，<code>ws://</code> 和 <code>http:/</code> 也算是同站。</p>
<p>Chrome 可以浏览器输入 <code>chrome://flags/#schemeful-same-site</code> 找到配置并开启。</p>
<h2 data-id="heading-3">Lax</h2>
<p>我们知道互联网广告通过在固定域 Cookie 下标记用户 ID，记录用户的行为从何达到精准推荐的目的。随着全球隐私问题的整治，同时也是为了更好的规避 CSRF 问题，在 Chrome 80 中浏览器将默认的 SameSite 规则从 <code>SameSite=None</code> 修改为 <code>SameSite=Lax</code>。设置成 <code>SameSite=Lax</code> 之后页面内所有跨站情况下的资源请求都不会携带 Cookie。由于不会为跨站请求携带 Cookie，所以 CSRF 的跨站攻击也无从谈起，广告商也无法固定用户的 ID 来记录行为。</p>
<p>对用户来说这肯定是一件好事。但是对我们技术同学来说，这无疑是上游给我们设置的一个障碍。因为业务也确实会存在着多个域名的情况，并且需要在这些域名中进行 Cookie 传递。例如多站点使用 SSO 登录、接入统一的验证码服务、前端和服务端接口属于两个域名等等情况，都会因为这个修改受到影响。</p>
<p>这个修改影响面广泛，需要网站维护者花大量的时间去修改适配。而 Chrome 80 于 2020 年 2 月发布后全球就开始面临新冠疫情的影响。考虑到疫情问题后续的版本里又暂时先回退了这个特性（<a href="https://blog.chromium.org/2020/04/temporarily-rolling-back-samesite.html" target="_blank" rel="nofollow noopener noreferrer">相关链接</a>），最终是在 Chrome 86 进行了全量操作。</p>
<p>针对因为此次特性受到影响的网站，可以选择以下一些适配办法：</p>
<ol>
<li>使用 JWT 等其它非 Cookie 的通信方式</li>
<li>为 Cookie 增加 <code>SameSite=None;Secure</code> 属性配置</li>
<li>所有的跨域接口增加 Nginx 代理，使其和页面保持同域</li>
</ol>
<p>每一种方法都需要一些取舍。第一种更换 Cookie 的方式改造成本非常高，特别是在有外部业务对接的情况下基本不可能。第三种方式通过将跨域变为同域的转发方式可能会带来线上流量的成倍增加，也是需要考虑的因素。第二种设置成 <code>None</code> 看起来是比较简单的办法，不过也有着诸多的限制。</p>
<ol>
<li><code>SameSite=None;Secure</code> 由于仅支持 HTTPS 页面，所以如果有 HTTP 的场景需要考虑跳转至 HTTPS 或者选择其他方案；</li>
<li>由于 <code>SameSite</code> 属性是后来才加入的，一些老浏览器（其实就是 IE）会忽略带有这些属性的 Cookie，所以需要同时下发未配置 <code>SameSite</code> 属性和配置 <code>SameSite</code> 属性的两条 <code>Set-Cookie</code> 响应头，这样支持和不支持的会各取所需；</li>
<li>在 Safari 的某些版本中会将 <code>SamteSite=None</code> 等同于 <code>SameSite=Strict</code> 所以部分 Safari 场景需要特殊处理不进行下发（<a href="https://stackoverflow.com/questions/58525719/safari-not-sending-cookie-even-after-setting-samesite-none-secure" target="_blank" rel="nofollow noopener noreferrer">相关链接</a>）；</li>
</ol>
<p>综上使用代理转发的方式是我比较推荐的方式，除了不那么绿色之外兼容问题处理还是不错的。</p>
<h2 data-id="heading-4">SameParty</h2>
<p><code>SameSite=None</code> 断了我们跨站传递 Cookie 的念想，但实际业务上确实有这种场景。例如 Google 自己就有非常多的域名，这些域名如果都需要共享登录 Cookie 的话可能就会非常困难了。针对这种某个实体拥有多个域名需要共享 Cookie 的情况，就有人（那其实就是 Google 的同学）提出了 <a href="https://github.com/cfredric/sameparty" target="_blank" rel="nofollow noopener noreferrer">SameParty</a> 的概念。</p>
<p>该提案提出了 <code>SameParty</code> 新的 Cookie 属性，当标记了这个属性的 Cookie 可以在同一个主域下进行共享。那如何定义不同的域名属于同一主域呢？主要是依赖了另外一个特性 <a href="https://github.com/privacycg/first-party-sets" target="_blank" rel="nofollow noopener noreferrer">first-party-set</a> 第一方集合。它规定在每个域名下的该 URL <code>/.well-known/first-party-set</code>  可以返回一个第一方域名的配置文件。在这个文件中你可以定义当前域名从属于哪个第一方域名，该第一方域名下有哪些成员域名等配置。</p>
<p>当然使用固定 URL 会产生额外的请求，对页面的响应造成影响。也可以直接使用 <code>Sec-First-Party-Set</code> 响应头直接指定归属的第一方域名。</p>
<p>不过 W3C TAG 小组已经强烈拒绝了该提案（<a href="https://www.theregister.com/2021/04/08/w3c_google_multple_domains/" target="_blank" rel="nofollow noopener noreferrer">来源</a>）。W3C 认为该提案重新定义了网站沙箱的边界，带来的影响可能不仅仅只是 Cookie 共享这么简单，包括麦克风、摄像头、地理信息等隐私设置都需要去重新评估影响。</p>
<p>同时该提案可能会和用户的预期不一致，如果 Google 和 Youtube 被定义成第一方网站进行共享的话，那 Google 就能很轻松的获取到用户在 Youtube 上的行为，可能用户并不想要这样。</p>
<p>W3C TAG 小组全称是 Technical Architecture Group，即 W3C 技术架构组。TAG 是 W3C 专注于 Web 架构管理的特殊小组。其使命是为 Web 架构的设计原则寻求共识，且在必要时梳理并澄清这些设计原则，帮助协调 W3C 内部及外部跨越不同技术的架构定义与研发工作。基本可以认为它是 Web 基础规范定义的小组。另外万维网之父 Tim Berners-Lee 也在 TAG 小组中。</p>
<p>不过 W3C 说的有理没理，都阻挡不了 Chrome 去实现这个功能。在 Chrome 89 中已经增加了 SameParty 的相关逻辑，只是目前没有默认开启。目前在 DevTools 中是可以看到 Cookie 的 SameParty 属性列的。Edge 由于使用了 Chromium 也在同版本支持了该功能。只掌管了规范，没有掌管实现，当某一方浏览器实现了“霸权”的情况下，W3C 的处境就变得尴尬了起来。</p>
<h2 data-id="heading-5">FLoC</h2>
<p>SameSite 除了影响单实体多域名共享 Cookie 的情况，最大的问题其实就是互联网广告获取用户行为了。由于广告挂载页面和广告不在同域，所以广告无法获得用于标记用户 ID 从而对用户行为进行聚类。为了解决这个问题，有人（其实也是 Google 的同学）提出了 <a href="https://github.com/WICG/floc" target="_blank" rel="nofollow noopener noreferrer">Federated Learning of Cohorts</a> 同盟学习队列提案。</p>
<p>有别于之前使用 Cookie ID 标记直接将用户行为数据传递到广告商网站处理的方式。它提出了 <code>document.interestCohort()</code> 这个新的 API，将用户的行为在本地转换成了不带个人隐私的关键词，既规避了用户隐私问题，同时又解决了广告的精准投放问题。</p>
<p>不过这看似美好的东西却遭到了各大网站和浏览器的强力抵制，<a href="https://brave.com/why-brave-disables-floc/" target="_blank" rel="nofollow noopener noreferrer">brav</a>、<a href="https://vivaldi.com/blog/no-google-vivaldi-users-will-not-get-floced/" target="_blank" rel="nofollow noopener noreferrer">Vivaldi</a>、<a href="https://spreadprivacy.com/block-floc-with-duckduckgo/" target="_blank" rel="nofollow noopener noreferrer">duckduckgo</a>、<a href="https://github.blog/changelog/2021-04-27-github-pages-permissions-policy-interest-cohort-header-added-to-all-pages-sites/" target="_blank" rel="nofollow noopener noreferrer">GitHub</a> 以及 Edge，Firefox，Safari（<a href="https://www.theverge.com/2021/4/16/22387492/google-floc-ad-tech-privacy-browsers-brave-vivaldi-edge-mozilla-chrome-safari" target="_blank" rel="nofollow noopener noreferrer">来源</a>）都纷纷发表了拒绝支持的观点和行动。</p>
<p>社区主要的担心点在于，新的特性的增加可能会增加特征值为隐私嗅探提供了更广阔的入口。而且通过该 API 能获取到之前碍于权限无法程序获取的用户浏览数据。目前 Chrome 已经支持了这个功能，不过需要开启 Flag 才能支持。<a href="https://amifloced.org/" target="_blank" rel="nofollow noopener noreferrer">amIFLoCed</a> 是一个用来检测你的浏览器是否开启了 FLoC 追踪特性的网站，可以使用它检测你的浏览器是否应用该特性。</p>
<h2 data-id="heading-6">后记</h2>
<p>为了解决 CSRF 问题，Chrome 强推了 <code>SameSite=Lax</code> 作为默认配置。随之而来的，不仅是全球开发者的配合修改，还造成了已有场景的无法满足。而为了满足现有场景，又提出了 <code>SameParty</code> 和 <code>FLoC</code> 两个方案。这种行为不知能否成为浏览器的内卷行为？</p>
<p><code>SameSite</code> 属性本身是没有什么问题的，但个人认为它应该是一种 CSRF 问题的选择方案，浏览器将其默认修改成 <code>SameSite=Lax</code> 就有点难受了。大部分企业项目里都已经采用其他 CSRF 防范方式规避了该问题，而 Lax 配置又存在着兼容性问题，不能让我们完全免顾 CSRF 之忧。</p>
<p>随着全球隐私问题的白热化，不知道还有什么新的提案搞出来需要我们全球开发者为其买单。</p>
<p><strong>参考资料：</strong></p>
<ul>
<li><a href="https://blog.heroku.com/chrome-changes-samesite-cookie" target="_blank" rel="nofollow noopener noreferrer">封面图来源</a></li>
<li><a href="https://web.dev/samesite-cookies-explained/" target="_blank" rel="nofollow noopener noreferrer">《SameSite cookies explained》</a></li>
<li><a href="https://web.dev/samesite-cookie-recipes/" target="_blank" rel="nofollow noopener noreferrer">《SameSite cookie recipes》</a></li>
<li><a href="https://web.dev/schemeful-samesite/" target="_blank" rel="nofollow noopener noreferrer">《Schemeful Same-Site》</a></li>
<li><a href="https://web.dev/same-site-same-origin/" target="_blank" rel="nofollow noopener noreferrer">《Understanding "same-site" and "same-origin"》</a></li>
<li><a href="https://www.chromestatus.com/feature/5088147346030592" target="_blank" rel="nofollow noopener noreferrer">www.chromestatus.com/feature/508…</a></li>
<li><a href="https://www.chromium.org/updates/same-site" target="_blank" rel="nofollow noopener noreferrer">www.chromium.org/updates/sam…</a></li>
<li><a href="https://hacks.mozilla.org/2020/08/changes-to-samesite-cookie-behavior/" target="_blank" rel="nofollow noopener noreferrer">hacks.mozilla.org/2020/08/cha…</a></li>
</ul></div>  
</div>
            