
---
title: '详解 Cookie 新增的 SameParty 属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6824dcf843a494eaa60c833139eb9c9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 16:22:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6824dcf843a494eaa60c833139eb9c9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>各大主流浏览器正在逐步禁用 <code>三方Cookie</code> ，之前笔者也在下面这篇文章中分析了全面禁用 <code>三方Cookie</code> 后对我们的网站带来的一些影响：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2NDAzMjE5NQ%3D%3D%26mid%3D2247485523%26idx%3D1%26sn%3De7f3989448f5ff1e8905fc6596268e33%26chksm%3Dce6eccfff91945e990e0b21e777f5a85f3f0699f7d51e45a1dd83d0bf36eaf926f7e90fbe3ff%26token%3D379611469%26lang%3Dzh_CN%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=Mzg2NDAzMjE5NQ==&mid=2247485523&idx=1&sn=e7f3989448f5ff1e8905fc6596268e33&chksm=ce6eccfff91945e990e0b21e777f5a85f3f0699f7d51e45a1dd83d0bf36eaf926f7e90fbe3ff&token=379611469&lang=zh_CN#rd" ref="nofollow noopener noreferrer">当浏览器全面禁用三方 Cookie</a></p>
<p>但是一个公司或组织往往在不同业务下会有多个不同的域名，例如 <code>taobao.com</code>、<code>tianmao.com</code>，所以很多正常的业务场景也许要借助 <code>三方Cookie</code>  来实现（比如 <code>单点登录 </code>和 <code>consent管理</code>），直接禁用后可能会给我们的业务带来很大影响，而且之前一直以来都没有很好的解决方案，这也是 Chrome 禁用 <code>三方Cookie</code> 进展非常缓慢的原因。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6824dcf843a494eaa60c833139eb9c9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>第一方Cookie</code> 和 <code>第三方Cookie</code> 被区别对待的情况下，Chrome 新推出了一个 <code>First-Party Sets</code> 策略，它可以允许由同一实体拥有的不同关域名都被视为第一方。</p>
<p>这意味着我们可以标记打算在同一方上下文共享 <code>Cookie</code> 的不同域名，目的是在防止第三方跨站点跟踪和仍然保持正常的业务场景下之间找到平衡。</p>
<blockquote>
<p>目前 <code>First-Party Sets</code> 策略还没有正式在稳定版推出，还在试用阶段。</p>
</blockquote>
<h2 data-id="heading-0">一方和三方 Cookie 的区别</h2>
<p>可能很多小伙伴对 <code>三方Cookie</code> 的概念还比较模糊，我们先来回顾一下：</p>
<p><code>Cookie</code> 本质上不区分第一方或第三方，它取决于包含 <code>Cookie</code> 的当前上下文。我们还用之前的老例子：</p>
<p>如果是你正常的正在逛着天猫，天猫会把你的信息写入一些 <code>Cookie</code> 到 <code>.tmall.com</code> 这个域下，然而打开控制台你会看到，并不是所有 <code>Cookie</code> 都是  <code>.tmall.com</code> 这个域下的，里面还有很多其他域下的  <code>Cookie</code> ，这些所有非当前域下的 <code>Cookie</code> 都属于第三方 <code>Cookie</code>，虽然你可能从来没访问过这些域，但是他们已经悄悄的通过这些第三方 <code>Cookie</code>来标识你的信息，然后把你的个人信息发送过去了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/726dc8ecd8184ae187b4f96b44a61a72~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而 <code>.tmall.com</code> 这个域下的 <code>Cookie</code> 都属于第一方 <code>Cookie</code>，那么为什么还需要第三方 <code>Cookie</code> 呢？再打开 <code>taobao.com</code>，你会发现你已经不需要再登录了，因为淘宝、天猫都属于阿里旗下的产品，阿里为他们提供统一的登录服务，同时，你的登录信息也会存到这个统一登录服务的域下，所以存到这个域下的 <code>Cookie</code> 就成了三方 <code>Cookie</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b01cfbe85796425284d64cb8dff64247~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">SameSite 的问题</h2>
<p><code>Chrome</code> 在之前的版本为 <code>Cookie</code> 新增了一个 <code>SameSite</code> 属性 来限制三方 <code>Cookie</code> 的访问，在 <code>Chrome 80</code> 版本后 <code>SameSite</code> 的默认值被设定为 <code>SameSite=Lax</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0829257206d940d3b6869b27cea05437~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>Strict</code> 模式下，将阻止所有三方 Cookie 携带，这种设置基本可以阻止所有 CSRF 攻击，然而，它的友好性太差，即使是普通的 GET 请求它也不允许通过。</p>
<p>在 <code>Lax</code> 模式下只会阻止在使用危险 <code>HTTP</code> 方法进行请求携带的三方 <code>Cookie</code>，例如 <code>POST</code> 方式。同时，使用 <code>JavaScript</code> 脚本发起的请求也无法携带三方 <code>Cookie</code>。</p>
<p>但是，试用上面两种模式，我们上面提到的一些正常的需求场景就无法实现了，对于这种 <code>Cookie</code> ，我们现在一般会手动设置 <code>SameSite=None</code> 。</p>
<p>这意味着这种 <code>Cookie</code> 又失去了跨站点请求伪造 (<code>CSRF</code>) 保护，例如在 <code>evil.site</code> 发送一个 <code>me.site</code> 的请求，也会带上我们的 <code>Cookie</code>。</p>
<h2 data-id="heading-2"><code>First-Party Sets</code> 策略</h2>
<p>在上面正常的业务场景中，所有不同的域名基本上都来自同一个组织或企业，我们希望在同一个运营主体下不同域名的 <code>Cookie</code> 也能共享。</p>
<p><code>First-Party Sets</code> 可以定义跨站点上下文仍然是 <code>first-party</code> 的情况。 <code>Cookie</code> 可以包含在第一方集合中，也可以排除在第三方上下文中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cabf7293fd3e4d8c977dd09d0e6d67b2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>First-Party Sets</code> 提出了一种明确定义在同一主体下拥有和运营的多个站点关系的方法。比如  <code>.tmall.com</code>、<code>taobao.com</code> 都可以被定义为同一主体运营 。</p>
<blockquote>
<p>这个策略来源于浏览器的隐私沙提案中对身份进行分区以防止跨站点跟踪的概念，在站点之间划定界限，限制对可用于识别用户的任何信息的访问。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bf47315e60345f7b1facb0a199042cd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器的默认行为是对同一站点进行分区，上面这个新的策略意味着分区被可以开放为多个站点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f578c87a40642f3a09e1b0f8cf6f82a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>First-Party Sets</code> 策略的一个重要部分是确保跨浏览器的政策防止滥用或误用。例如，<code>First-Party Sets</code> 策略不得在不相关的站点之间交换用户信息，或对不属于同一实体的站点进行分组。</p>
<p>所以单点登录这种场景可能是不能用这种方式解决了，因为这个场景属于交换用户信息，目前怎么界定哪些信息是用户信息官方还没有明确的描述，所以这个地方笔者也不是很确定。</p>
<blockquote>
<p><code>W3C</code> 目前正在讨论新的 <code>First-Party Sets</code> 的配置和验证，其中一个考虑的选项是由独立实体而非浏览器公司处理验证。</p>
</blockquote>
<p>目前 <code>First-Party Sets</code> 已经确定的原则如下：</p>
<ul>
<li><code>First-Party Sets</code> 中的域必须由同一组织拥有和运营。</li>
<li>所有域名应该作为一个组被用户识别。</li>
<li>所有域名应该共享一个共同的隐私政策。</li>
</ul>
<h2 data-id="heading-3">如何定义 <code>First-Party Sets</code></h2>
<p>每一个需要用到  <code>First-Party Sets</code> 策略的域名都应该把一个 <code>JSON</code> 配置托管在 <code>/.well-known/first-party-set</code> 路由下。</p>
<p>例如 <code>conardli.top</code> 的配置应该托管在 <code>https://conardli.top/.well-known/first-party-set</code> 下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"owner"</span>: <span class="hljs-string">"conardli.top"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">"members"</span>: [<span class="hljs-string">"conardli.com"</span>, <span class="hljs-string">"conardli.cn"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外 <code>conardli.com、 conardli.cn</code> 两个域名均需要增加所有者的配置：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"owner"</span>: <span class="hljs-string">"conardli.top"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>First-Party Sets</code> 还有一些限制：</p>
<ul>
<li>一个集合可能只有一个所有者。</li>
<li>一个成员只能属于一个集合，不能重叠或混合。</li>
<li>域名列表不要过大。</li>
</ul>
<h2 data-id="heading-4">SameParty 属性</h2>
<p>好了，上面介绍了一大堆，终于回到本文的主题 <code>Cookie SameParty</code> 属性了，这个属性就是为了配合 <code>First-Party Sets</code>  使用的。</p>
<p>所有开启了  <code>First-Party Sets</code> 域名下需要共享的 <code>Cookie</code> 都需要增加 <code>SameParty</code> 属性，例如，如果我在 <code>conardli.top</code> 下设置了下面的 <code>Cookie</code> ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Set</span>-Cookie: name=lishiqi; Secure; SameSite=Lax; SameParty
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时我在 <code>conardli.cn</code> 下发送 <code>conardli.top</code> 域名的请求，<code>Cookie</code> 也可以被携带了，但是如果我在另外一个网站，例如 <code>eval.site</code> 下发送这个请求， <code>Cookie</code> 就不会被携带。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb2c7d9fa26d464fbcb069e026eba8b8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>SameParty</code> 被广泛支持之前，你可以把它和 <code>SameSite</code> 属性一起定义来确保 <code>Cookie</code> 的行为降级，另外还有一些额外的要求：</p>
<ul>
<li>SameParty Cookie 必须包含 Secure.</li>
<li>SameParty Cookie 不得包含 SameSite=Strict.</li>
</ul>
<h2 data-id="heading-5">如何试用？</h2>
<p>在浏览器禁用三方 Cookie 后，这个新的提案应该会被大范围的使用，现在可以先试用起来啦！</p>
<p>你可以在下面两个地方参与提案的讨论：</p>
<ul>
<li>First-Party Sets 策略讨论：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprivacycg%2Ffirst-party-sets" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/privacycg/first-party-sets" ref="nofollow noopener noreferrer">github.com/privacycg/f…</a></li>
<li>SameParty 属性讨论： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcfredric%2Fsameparty" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cfredric/sameparty" ref="nofollow noopener noreferrer">github.com/cfredric/sa…</a></li>
</ul>
<p>现在提案还在试用阶段，你可以试用 <code>--use-first-party-set</code> 这个命令启动 <code>Chrome</code> ，就可以进行试用啦！</p>
<p>比如，在示例站 <code>https://fps-member1.glitch.me/</code> 添加如下配置：</p>
<pre><code class="hljs language-JS copyable" lang="JS">--use-first-party-set=https:<span class="hljs-comment">//fps-member1.glitch.me,https://fps-member2.glitch.me,https://fps-member3.glitch.me</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5280634094223360" target="_blank" rel="nofollow noopener noreferrer" title="https://www.chromestatus.com/feature/5280634094223360" ref="nofollow noopener noreferrer">www.chromestatus.com/feature/528…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcfredric%2Fsameparty" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cfredric/sameparty" ref="nofollow noopener noreferrer">github.com/cfredric/sa…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.chrome.com%2Fblog%2Ffirst-party-sets-sameparty%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.chrome.com/blog/first-party-sets-sameparty/" ref="nofollow noopener noreferrer">developer.chrome.com/blog/first-…</a></li>
</ul>
<blockquote>
<p>抖音前端正急缺人才，如果你想加入我们，欢迎加我微信和我联系。另外如果你想加入前端、面试、理财等交流群，或者你有任何其他事情想和我交流也可以添加我的个人微信 ConardLi 。</p>
</blockquote>
<blockquote>
<p>文中如有错误，欢迎在后台和我留言，如果这篇文章帮助到了你，欢迎点赞、在看和关注。你的点赞、在看和关注是对我最大的支持！</p>
</blockquote></div>  
</div>
            