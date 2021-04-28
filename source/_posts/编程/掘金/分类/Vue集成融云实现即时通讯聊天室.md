
---
title: 'Vue集成融云实现即时通讯聊天室'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f5cc075ec014549a0127789cad6e1b7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 17:31:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f5cc075ec014549a0127789cad6e1b7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近把<a href="https://juejin.cn/post/6951564460964347912" target="_blank">Vue+Element二次封装</a>持续完善了,然后开始着手处理即时通讯这一块了。</p>
<p>之前的老代码用的是融云2.x版本，现在4.x了，自然要更新下，融云4.x变化还是挺大的,很多API都换掉了，但是相对来讲还是比较简单上手的。</p>
<p>由于没有原型图，我直接边设计办coding，对于这种自己发挥的需求，我仍然保持微笑。（这应该是对我审美的肯定吧！）先整了个样图出来如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f5cc075ec014549a0127789cad6e1b7~tplv-k3u1fbpfcp-watermark.image" alt="融云2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>高处不胜寒，起舞弄清影。</p>
</blockquote>
<p>接下来咱们步入正题</p>
<h1 data-id="heading-1">分析需求</h1>
<p>项目是一个社交APP的后台管理项目，项目中有个模块是关于聊天室的，链接APP内的聊天大厅，如果有用户发布不良信息，可以禁言用户，同时也可以发布公告消息。</p>
<h2 data-id="heading-2">任务</h2>
<ol>
<li>获取token，链接融云</li>
<li>获取历史消息并模拟聊天展示出来</li>
<li>发送消息，这个是由后端完成，我发送消息就请求接口</li>
<li>可以禁言用户，这个也是由后端来统一完成</li>
</ol>
<h1 data-id="heading-3">关于融云</h1>
<p>融云提供的即时通讯服务，不需要在 App 之外建立并行的用户体系，不用同步 App 下用户信息到融云，不影响 App 现有的系统架构与帐号体系，与现有业务体系能够实现完美融合。</p>
<h2 data-id="heading-4">兼容说明</h2>

























<table><thead><tr><th>Chrome</th><th>Firefox</th><th>Safari</th><th>IE</th><th>Edge</th><th>QQ 浏览器</th><th>微信 浏览器</th><th>Android</th></tr></thead><tbody><tr><td>✔</td><td>✔</td><td>✔</td><td>9+</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td></tr></tbody></table>
<h2 data-id="heading-5">导入 SDK</h2>
<blockquote>
<p>融云 4.x 底层使用 Typescript 进行了重构，对 Typescript 的使用者提供了友好的类型化支持，推荐开发者使用 Typescript 进行业务开发以提升代码健壮性及可维护性。</p>
</blockquote>
<h3 data-id="heading-6">NPM 引入（推荐）</h3>
<ol>
<li>依赖安装</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm install @rongcloud/imlib-v4
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>代码集成</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 非 ESModule</span>
<span class="hljs-keyword">const</span> RongIMLib = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@rongcloud/imlib-v4'</span>)
<span class="hljs-comment">// ESModule</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> RongIMLib <span class="hljs-keyword">from</span> <span class="hljs-string">'@rongcloud/imlib-v4'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">CDN 引入</h2>
<ul>
<li>在<code>index.html</code></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.ronghub.com/RongIMLib-4.3.latest.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">App Key</h2>
<p><code>App Key</code> 是使用 IMLib 进行即时通讯功能开发的必要条件，也是应用的唯一性标识。在集成使用 <code>IMLib</code> 之前，请务必先通过 融云开发者后台  (opens new window)注册并获取开发者的专属 <code>App Key</code>。</p>
<p>只有在 App Key 相同的情况下，不同用户之间的消息才有可能互通。</p>
<h2 data-id="heading-9">初始化</h2>
<p>IMLib 提供的所有能力基于 IMLib 初始化后获取的实例对象，因此在使用 IMLib 的能力之前，<strong>必须先调用 IMLib 的初始化接口，且务必保证该接口在应用全生命周期内仅被调用一次。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 应用初始化以获取 RongIMLib 实例对象，请务必保证此过程只被执行一次</span>
<span class="hljs-keyword">const</span> im = RongIMLib.init(&#123; <span class="hljs-attr">appkey</span>: <span class="hljs-string">'<Your-App-Key>'</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>后续所有代码示例中的 im 均指通过初始化获取到的 RongIMLib 实例对象</p>
</blockquote>
<h2 data-id="heading-10">设置监听</h2>
<p>初始化完成后，<strong>应在建立连接之前对 im 对象添加事件监听器，及时获取相关事件通知。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 添加事件监听</span>
im.watch(&#123;
  <span class="hljs-comment">// 监听会话列表变更事件</span>
  conversation (event) &#123;
    <span class="hljs-comment">// 假定存在 getExistedConversationList 方法，以获取当前已存在的会话列表数据</span>
    <span class="hljs-keyword">const</span> conversationList = getExistedConversationList()
    <span class="hljs-comment">// 发生变更的会话列表</span>
    <span class="hljs-keyword">const</span> updatedConversationList = event.updatedConversationList;
    <span class="hljs-comment">// 通过 im.Conversation.merge 计算最新的会话列表</span>
    <span class="hljs-keyword">const</span> latestConversationList = im.Conversation.merge(&#123; conversationList, updatedConversationList &#125;)
  &#125;,
  <span class="hljs-comment">// 监听消息通知</span>
  message (event) &#123;
    <span class="hljs-comment">// 新接收到的消息内容</span>
    <span class="hljs-keyword">const</span> message = event.message;
  &#125;,
  <span class="hljs-comment">// 监听 IM 连接状态变化</span>
  status (event) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'connection status:'</span>, event.status);
  &#125;,
  <span class="hljs-comment">// 监听聊天室 KV 数据变更</span>
  chatroom (event) &#123;
    <span class="hljs-comment">/**
     * 聊天室 KV 存储数据更新
     * <span class="hljs-doctag">@example</span>
     * [
     *  &#123;
     *    "key": "name",
     *    "value": "我是小融融",
     *    "timestamp": 1597591258338, 
     *    "chatroomId": "z002", 
     *    "type": 1 // 1: 更新（ 含:修改和新增 ）、2: 删除
     *  &#125;,
     * ]
     */</span>
    <span class="hljs-keyword">const</span> updatedEntries = event.updatedEntries
  &#125;,
  expansion (event) &#123;
    <span class="hljs-comment">/**
     * 更新的消息拓展数据
     * <span class="hljs-doctag">@example <span class="hljs-type">&#123;
     *    expansion: &#123; key: 'value' &#125;</span></span>,      // 设置或更新的扩展值
     *    messageUId: 'URIT-URIT-ODMF-DURR' // 设置或更新扩展的消息 uid
     * &#125;
     */</span>
    <span class="hljs-keyword">const</span> updatedExpansion = event.updatedExpansion;
    <span class="hljs-comment">/**
     * 删除的消息拓展数据
     * <span class="hljs-doctag">@example <span class="hljs-type">&#123;
     *    deletedKeys: ['key1', 'key2'],    // 设置或更新的扩展值
     *    messageUId: 'URIT-URIT-ODMF-DURR' // 设置或更新扩展的消息 uid
     * &#125;</span></span>
     */</span>
    <span class="hljs-keyword">const</span> deletedExpansion = event.deletedExpansion;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">建立 IM 连接</h2>
<p><code>App Key</code> 是应用的唯一性标识，<code>Token</code> 则是用户的唯一性标识，是用户连接融云 <code>IM </code>服务所必需的身份凭证。<code>Token</code> 一般由开发者的应用服务器调用融云<code> Server API</code> 获取 Token 接口获取之后，由应用服务器下发到应用客户端。</p>
<p>我的这个token是从后端获取的，然后存储到本地，用的时候看看过期没，过期了就重新获取。相当于前端只进行部分交互。</p>
<ul>
<li>获取token</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 获取token</span>
    <span class="hljs-function"><span class="hljs-title">getIMToken</span>(<span class="hljs-params"></span>)</span> &#123;
      getIMToken().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">var</span> time = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
        res.time = time
        <span class="hljs-comment">// 将token保存下来</span>
        <span class="hljs-built_in">this</span>.gobalToken = res
        <span class="hljs-keyword">var</span> tokenStr = <span class="hljs-built_in">JSON</span>.stringify(res)
        <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'token'</span>, tokenStr)
        <span class="hljs-comment">// 初始化融云</span>
        <span class="hljs-built_in">this</span>.linkToRongs(res.data)
      &#125;)
    &#125;,
    <span class="hljs-comment">// 判断token是否过期</span>
    <span class="hljs-function"><span class="hljs-title">isToken</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">var</span> now = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
      <span class="hljs-comment">// 获取上一次存储的token</span>
      <span class="hljs-keyword">var</span> oldToken = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'token'</span>))
      <span class="hljs-comment">// 判断之前获取的token</span>
      <span class="hljs-keyword">if</span> (oldToken) &#123;
        <span class="hljs-keyword">var</span> tokenTime = oldToken.time
        <span class="hljs-comment">// 判断时间是否过期了</span>
        <span class="hljs-keyword">if</span> (now - tokenTime > <span class="hljs-number">29</span> * <span class="hljs-number">24</span> * <span class="hljs-number">60</span> * <span class="hljs-number">60</span> * <span class="hljs-number">1000</span>) &#123;
          <span class="hljs-built_in">this</span>.getIMToken()
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>.gobalToken = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'token'</span>))
          <span class="hljs-built_in">this</span>.linkToRongs(<span class="hljs-built_in">this</span>.gobalToken.data)
          <span class="hljs-keyword">return</span>
        &#125;
      &#125;
      <span class="hljs-built_in">this</span>.getIMToken()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>建立连接</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">im.connect(&#123; <span class="hljs-attr">token</span>: <span class="hljs-string">'<Your-Token>'</span> &#125;).then(<span class="hljs-function"><span class="hljs-params">user</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'链接成功, 链接用户 id 为: '</span>, user.id);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'链接失败: '</span>, error.code, error.msg);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">获取会话列表</h2>
<blockquote>
<p>Web 端不具备持久化的数据存储能力，需要开发者开启 IM 商用版 - 单群聊云存储  (opens new window)功能才能生效。 该功能需要在调用 <code>im.connect()</code> 并且建立连接成功之后执行。</p>
</blockquote>
<p><code>IMLib</code> 通过会话数据中的 <code>conversationType</code> 与 <code>targetId</code> 两个属性值来标识会话的唯一性，对于两个属性的定义如下：</p>
<ol>
<li><code>conversationType</code> 用来标识会话类型（如：单聊、群聊...），其值为 <code>RongIMLib.CONVERSATION_TYPE</code> 中的常量定义</li>
<li><code>targetId</code> 用来标识与本端进行对话的人员或群组 Id：</li>
</ol>
<ul>
<li>当 <code>conversationType</code> 值为 RongIMLib.CONVERSATION_TYPE.PRIVATE，targetId 为对方用户 Id</li>
<li>当 <code>conversationType</code> 值为 RongIMLib.CONVERSATION_TYPE.GROUP，targetId 为当前群组 Id</li>
<li>当 <code>conversationType</code> 值为 RongIMLib.CONVERSATION_TYPE.CHATROOM，targetId 为聊天室 Id</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取会话列表</span>
im.Conversation.getList().then(<span class="hljs-function"><span class="hljs-params">conversationList</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'获取会话列表成功'</span>, conversationList);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'获取会话列表失败: '</span>, error.code, error.msg);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">发送消息</h2>
<blockquote>
<p>该功能需要在调用 <code>im.connect() </code>并且建立连接成功之后执行。 IMLib 内置消息类型可通过 RongIMLib.MESSAGE_TYPE 获取其常量定义</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取指定会话的抽象实例，对于会话的操作基于此实例完成</span>
<span class="hljs-keyword">const</span> conversation = im.Conversation.get(&#123;
  <span class="hljs-comment">// targetId</span>
  <span class="hljs-attr">targetId</span>: <span class="hljs-string">'<TargetId>'</span>,
  <span class="hljs-comment">// 会话类型：RongIMLib.CONVERSATION_TYPE.PRIVATE | RongIMLib.CONVERSATION_TYPE.GROUP</span>
  <span class="hljs-attr">type</span>: <span class="hljs-string">'<Conversation-Type>'</span>
&#125;);
<span class="hljs-comment">// 向会话内发消息</span>
conversation.send(&#123;
  <span class="hljs-comment">// 消息类型，其中 RongIMLib.MESSAGE_TYPE 为 IMLib 内部的内置消息类型常量定义</span>
  <span class="hljs-attr">messageType</span>: RongIMLib.MESSAGE_TYPE.TEXT, <span class="hljs-comment">// 'RC:TxtMsg'</span>
  <span class="hljs-comment">// 消息内容</span>
  <span class="hljs-attr">content</span>: &#123;
    <span class="hljs-attr">content</span>: <span class="hljs-string">'Hello RongCloud'</span> <span class="hljs-comment">// 文本内容</span>
  &#125;
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">message</span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发送文字消息成功'</span>, message);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发送文字消息失败'</span>, error.code, error.msg);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">接收消息</h2>
<p>当本端作为消息接收的一方，所接收的消息将通过 <code>im.watch() </code>注册的消息监听向业务层抛出。具体可参考上述 设置监听 部分</p>
<h2 data-id="heading-15">获取历史消息</h2>
<blockquote>
<p>Web 端不具备持久化的数据存储能力，需要开发者开启 IM 商用版 - 单群聊云存储  (opens new window)功能才能生效。 该功能需要在调用 im.connect() 并且建立连接成功之后执行。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> conversation = im.Conversation.get(&#123;
  <span class="hljs-attr">targetId</span>: <span class="hljs-string">'<TargetId>'</span>,
  <span class="hljs-attr">type</span>: <span class="hljs-string">'<Conversation-Type>'</span>
&#125;);
<span class="hljs-keyword">const</span> option = &#123;
  <span class="hljs-comment">// 获取历史消息的时间戳，默认为 0，表示从当前时间获取</span>
  <span class="hljs-attr">timestamp</span>: +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
  <span class="hljs-comment">// 获取条数，有效值 1-20，默认为 20</span>
  <span class="hljs-attr">count</span>: <span class="hljs-number">20</span>,
&#125;;
conversation.getMessages(option).then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
  <span class="hljs-keyword">const</span> list = result.list;       <span class="hljs-comment">// 获取到的消息列表</span>
  <span class="hljs-keyword">const</span> hasMore = result.hasMore; <span class="hljs-comment">// 是否还有历史消息可获取</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'获取历史消息成功'</span>, list, hasMore);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发送文字消息失败'</span>, error.code, error.msg);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">断开连接</h2>
<blockquote>
<p>断开当前用户连接，连接断开后无法接收消息、发送消息、获取历史消息、获取会话列表... 在下次连接融云成功后，会收取上次离线后的消息，离线消息默认保存 7 天。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">im.disconnect().then(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'断开链接成功'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">实战运用</h1>
<h2 data-id="heading-18">token拿到手，往前走一走</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.isToken()
 &#125;
 <span class="hljs-attr">methods</span>:&#123;
<span class="hljs-comment">// 获取token</span>
    <span class="hljs-function"><span class="hljs-title">getIMToken</span>(<span class="hljs-params"></span>)</span> &#123;
      getIMToken().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">var</span> time = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
        res.time = time
        <span class="hljs-comment">// 将token保存下来</span>
        <span class="hljs-built_in">this</span>.gobalToken = res
        <span class="hljs-keyword">var</span> tokenStr = <span class="hljs-built_in">JSON</span>.stringify(res)
        <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'token'</span>, tokenStr)
        <span class="hljs-comment">// 初始化融云</span>
        <span class="hljs-built_in">this</span>.linkToRongs(res.data)
      &#125;)
    &#125;,
    <span class="hljs-comment">// 判断token是否过期</span>
    <span class="hljs-function"><span class="hljs-title">isToken</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">var</span> now = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
      <span class="hljs-comment">// 获取上一次存储的token</span>
      <span class="hljs-keyword">var</span> oldToken = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'token'</span>))
      <span class="hljs-comment">// 判断之前获取的token</span>
      <span class="hljs-keyword">if</span> (oldToken) &#123;
        <span class="hljs-keyword">var</span> tokenTime = oldToken.time
        <span class="hljs-comment">// 判断时间是否过期了</span>
        <span class="hljs-keyword">if</span> (now - tokenTime > <span class="hljs-number">29</span> * <span class="hljs-number">24</span> * <span class="hljs-number">60</span> * <span class="hljs-number">60</span> * <span class="hljs-number">1000</span>) &#123;
          <span class="hljs-built_in">this</span>.getIMToken()
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>.gobalToken = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'token'</span>))
          <span class="hljs-built_in">this</span>.linkToRongs(<span class="hljs-built_in">this</span>.gobalToken.data)
          <span class="hljs-keyword">return</span>
        &#125;
      &#125;
      <span class="hljs-built_in">this</span>.getIMToken()
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">init初始化，话话道心好好听</h2>
<p>一般测试服一个<code>appkey</code>,正式服一个<code>appkey</code>。这个<code>appkey</code>需要自己去申请</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 链接融云</span>
 <span class="hljs-function"><span class="hljs-title">linkToRongs</span>(<span class="hljs-params">token</span>)</span> &#123;
    <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">let</span> RongClientKey
    <span class="hljs-keyword">if</span> (process.env.VUE_APP_BASE_API2 === <span class="hljs-string">''</span>) &#123;<span class="hljs-comment">//测试服</span>
    RongClientKey = <span class="hljs-string">'4215151sadasas'</span>
    &#125; <span class="hljs-keyword">else</span> &#123;<span class="hljs-comment">//正式服</span>
    RongClientKey = <span class="hljs-string">'adsada12asda1a'</span>
    &#125;
    <span class="hljs-comment">// 应用初始化以获取 RongIMLib 实例对象，请务必保证此过程只被执行一次</span>
    <span class="hljs-comment">// eslint-disable-next-line no-undef</span>
    that.rongyun = RongIMLib.init(&#123; <span class="hljs-attr">appkey</span>: RongClientKey &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">监听先行开路，链接随后就到</h2>
<p>初始化完成后，应在建立连接之前对 im 对象添加事件监听器，及时获取相关事件通知。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 链接融云</span>
 <span class="hljs-function"><span class="hljs-title">linkToRongs</span>(<span class="hljs-params">token</span>)</span> &#123;
    <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">let</span> RongClientKey
    <span class="hljs-keyword">if</span> (process.env.VUE_APP_BASE_API2 === <span class="hljs-string">''</span>) &#123;<span class="hljs-comment">//测试服</span>
    RongClientKey = <span class="hljs-string">'4215151sadasas'</span>
    &#125; <span class="hljs-keyword">else</span> &#123;<span class="hljs-comment">//正式服</span>
    RongClientKey = <span class="hljs-string">'adsada12asda1a'</span>
    &#125;
    <span class="hljs-comment">// 应用初始化以获取 RongIMLib 实例对象，请务必保证此过程只被执行一次</span>
    <span class="hljs-comment">// eslint-disable-next-line no-undef</span>
    that.rongyun = RongIMLib.init(&#123; <span class="hljs-attr">appkey</span>: RongClientKey &#125;)
    <span class="hljs-keyword">const</span> im = that.rongyun
    <span class="hljs-comment">// 添加事件监听</span>
      im.watch(&#123;
        <span class="hljs-comment">// 监听会话列表变更事件</span>
        <span class="hljs-function"><span class="hljs-title">conversation</span>(<span class="hljs-params">event</span>)</span> &#123;
          <span class="hljs-comment">// 假定存在 getExistedConversationList 方法，以获取当前已存在的会话列表数据</span>
          <span class="hljs-keyword">const</span> conversationList = that.getExistedConversationList(im)
          <span class="hljs-comment">// 发生变更的会话列表</span>
          <span class="hljs-keyword">const</span> updatedConversationList = event.updatedConversationList
          <span class="hljs-comment">// 通过 im.Conversation.merge 计算最新的会话列表</span>
          <span class="hljs-keyword">const</span> latestConversationList = im.Conversation.merge(&#123; conversationList, updatedConversationList &#125;)
          <span class="hljs-built_in">console</span>.log(latestConversationList)
        &#125;,
        <span class="hljs-comment">// 监听消息通知</span>
        <span class="hljs-function"><span class="hljs-title">message</span>(<span class="hljs-params">event</span>)</span> &#123;
          <span class="hljs-comment">//初始化消息都在这</span>
          <span class="hljs-comment">// 新接收到的消息内容</span>
          <span class="hljs-keyword">const</span> message = event.message
          <span class="hljs-built_in">console</span>.log(message)
        &#125;,
        <span class="hljs-comment">// 监听 IM 连接状态变化</span>
        <span class="hljs-function"><span class="hljs-title">status</span>(<span class="hljs-params">event</span>)</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'connection status:'</span>, event.status)
        &#125;,
        <span class="hljs-comment">// 监听聊天室 KV 数据变更</span>
        <span class="hljs-function"><span class="hljs-title">chatroom</span>(<span class="hljs-params">event</span>)</span> &#123;
          <span class="hljs-keyword">const</span> updatedEntries = event.updatedEntries
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'聊天室 KV 存储数据更新'</span>, updatedEntries)
        &#125;
      &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">链接融云先用key，长驱直入无人拦</h2>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 链接融云</span>
 <span class="hljs-function"><span class="hljs-title">linkToRongs</span>(<span class="hljs-params">token</span>)</span> &#123;
    <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">let</span> RongClientKey
    <span class="hljs-keyword">if</span> (process.env.VUE_APP_BASE_API2 === <span class="hljs-string">''</span>) &#123;<span class="hljs-comment">//测试服</span>
    RongClientKey = <span class="hljs-string">'4215151sadasas'</span>
    &#125; <span class="hljs-keyword">else</span> &#123;<span class="hljs-comment">//正式服</span>
    RongClientKey = <span class="hljs-string">'adsada12asda1a'</span>
    &#125;
    <span class="hljs-comment">// 应用初始化以获取 RongIMLib 实例对象，请务必保证此过程只被执行一次</span>
    <span class="hljs-comment">// eslint-disable-next-line no-undef</span>
    that.rongyun = RongIMLib.init(&#123; <span class="hljs-attr">appkey</span>: RongClientKey &#125;)
    <span class="hljs-keyword">const</span> im = that.rongyun
    <span class="hljs-comment">// 添加事件监听</span>
      im.watch(&#123;
        <span class="hljs-comment">// 监听会话列表变更事件</span>
        <span class="hljs-function"><span class="hljs-title">conversation</span>(<span class="hljs-params">event</span>)</span> &#123;
          <span class="hljs-comment">// 假定存在 getExistedConversationList 方法，以获取当前已存在的会话列表数据</span>
          <span class="hljs-keyword">const</span> conversationList = that.getExistedConversationList(im)
          <span class="hljs-comment">// 发生变更的会话列表</span>
          <span class="hljs-keyword">const</span> updatedConversationList = event.updatedConversationList
          <span class="hljs-comment">// 通过 im.Conversation.merge 计算最新的会话列表</span>
          <span class="hljs-keyword">const</span> latestConversationList = im.Conversation.merge(&#123; conversationList, updatedConversationList &#125;)
          <span class="hljs-built_in">console</span>.log(latestConversationList)
        &#125;,
        <span class="hljs-comment">// 监听消息通知</span>
        <span class="hljs-function"><span class="hljs-title">message</span>(<span class="hljs-params">event</span>)</span> &#123;
          <span class="hljs-comment">//初始化消息都在这</span>
          <span class="hljs-comment">// 新接收到的消息内容</span>
          <span class="hljs-keyword">const</span> message = event.message
          <span class="hljs-built_in">console</span>.log(message)
        &#125;,
        <span class="hljs-comment">// 监听 IM 连接状态变化</span>
        <span class="hljs-function"><span class="hljs-title">status</span>(<span class="hljs-params">event</span>)</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'connection status:'</span>, event.status)
        &#125;,
        <span class="hljs-comment">// 监听聊天室 KV 数据变更</span>
        <span class="hljs-function"><span class="hljs-title">chatroom</span>(<span class="hljs-params">event</span>)</span> &#123;
          <span class="hljs-keyword">const</span> updatedEntries = event.updatedEntries
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'聊天室 KV 存储数据更新'</span>, updatedEntries)
        &#125;
      &#125;)
      <span class="hljs-comment">// 建立 IM 连接</span>
      <span class="hljs-keyword">const</span> chatRoomId = <span class="hljs-string">'627865222'</span>
      <span class="hljs-keyword">var</span> count = <span class="hljs-number">50</span> <span class="hljs-comment">// 数量</span>
      im.connect(&#123; <span class="hljs-attr">token</span>: token &#125;).then(<span class="hljs-function"><span class="hljs-params">user</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.$message.success(<span class="hljs-string">'加入聊天室成功'</span>)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'链接成功, 链接用户 id 为: '</span>, user.id)
        <span class="hljs-keyword">var</span> chatRoom = im.ChatRoom.get(&#123;
          <span class="hljs-attr">id</span>: chatRoomId
        &#125;)
        chatRoom.join(&#123;
          <span class="hljs-attr">count</span>: count <span class="hljs-comment">// 进入后, 自动拉取 20 条聊天室最新消息</span>
        &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'加入聊天室成功'</span>)
          chatRoom.getInfo().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>) </span>&#123;
            <span class="hljs-keyword">var</span> userCount = result.userCount
            <span class="hljs-keyword">var</span> user = that.uniq(that.messageList)
            <span class="hljs-comment">// 刷选用户</span>
            user.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
              that.list.push(item.user)
            &#125;)
            that.num = userCount
          &#125;)
        &#125;)
      &#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.$message.success(<span class="hljs-string">'加入聊天室失败'</span>)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'链接失败: '</span>, error.code, error.msg)
      &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">最后一步最重要，退出聊天要及时</h2>
<p>切换页面时，一定要退出聊天厅，不然下次加入聊天厅无法获取之前的消息。当然你也可以获取历史消息，我尝试获取历史消息一直报错，所以才选择打开页面加入，结束就离开。（不退出的话会一直保持连接）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">var</span> chatRoom = <span class="hljs-built_in">this</span>.rongyun.ChatRoom.get(&#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">'聊天室id'</span>
    &#125;)
    chatRoom.quit().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'退出聊天室成功'</span>)
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-23">结尾</h1>
<p>即时通讯这一块做起来还是蛮有意思的，总有一些意料之外的事情发生。</p>
<blockquote>
<p>生活中充满各种惊喜，代码世界亦是如此。</p>
</blockquote>
<p><a href="https://github.com/kinoaa/Vue-RongIMLib" target="_blank" rel="nofollow noopener noreferrer">最后把源码放在了github</a></p>
<p><a href="https://docs.rongcloud.cn/v4/" target="_blank" rel="nofollow noopener noreferrer">融云官方文档</a></p></div>  
</div>
            