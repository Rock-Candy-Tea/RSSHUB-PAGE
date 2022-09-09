
---
title: '让打卡小工具_智能一点_：添加请假过滤、token 自动刷新'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=301'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 18:29:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=301'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是杨成功。</p>
<p>前面写了一篇文章，介绍了如何用 Node.js + 钉钉 API 实现考勤打卡连续提醒的小工具。有的同学留言说为什么不直接调用钉钉 API 自动打卡（这个我也想过）。可惜我翻遍了钉钉的文档都没有找到这个 API。</p>
<p>再说了，怎么可能有这个 API 呢？想啥呢？</p>
<p>还有的同学严厉的指出了问题：“我请假了你还一直提醒？token 用几个小时就过期！”。针对这两个问题，我们在上次实现代码的基础上进行优化，添加两个逻辑：</p>
<ol>
<li>获取未打卡的人员时，过滤已请假人员</li>
<li>当 token 过期时，自动刷新 token</li>
</ol>
<p>如果没有看过上篇文章，请先看<a href="https://juejin.cn/post/7136108565986541598" target="_blank" title="https://juejin.cn/post/7136108565986541598">打卡小工具第一篇</a>，源代码在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fruidoc%2Fattend-robot" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ruidoc/attend-robot" ref="nofollow noopener noreferrer">GitHub</a>。</p>
<p>接下来我们一起实现新增的需求，优化打卡功能。</p>
<h2 data-id="heading-0">过滤已请假人员</h2>
<p>使用钉钉 API 可以获取一些人员的打卡状态。目前我们的做法是，将需要检测打卡状态的人员（我们全组人员）的 userid 维护在一个列表中，然后获取到这些人的打卡数据，从而筛选出未打卡的人员。</p>
<p>特殊情况是，假设我们组的一个组员今天请假了，他会被当做未打卡人员进行不断提醒。其实我们需要将已请假的人员排除在外，第一步是要获取今日已请假的人员。</p>
<p>获取请假状态的 API 如下：</p>
<blockquote>
<p>API 地址：$&#123;baseURL&#125;/topapi/attendance/getleavestatus<br>
请求方法：POST<br>
文档地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopen.dingtalk.com%2Fdocument%2Forgapp-server%2Fquery-status" target="_blank" rel="nofollow noopener noreferrer" title="https://open.dingtalk.com/document/orgapp-server/query-status" ref="nofollow noopener noreferrer">这里</a></p>
</blockquote>
<p>这个 API 的请求体是一个对象，对象的属性如下：</p>
<ul>
<li>userid_list：查询请假状态的 userid 列表</li>
<li>start_time：查询开始时间（当天上班时间）</li>
<li>end_time：查询结束时间（当天下班时间）</li>
<li>size：返回条数，最大 20</li>
<li>offset：分页，从 0 开始</li>
</ul>
<p>将获取请假状态写为一个单独的方法，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> dayjs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'dayjs'</span>);
<span class="hljs-keyword">const</span> access_token = <span class="hljs-keyword">new</span> <span class="hljs-title class_">DingToken</span>().<span class="hljs-title function_">get</span>();

<span class="hljs-comment">// 获取请假状态</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">getLeaveStatus</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params">userid_list</span>) => &#123;
  <span class="hljs-keyword">let</span> params = &#123;
    access_token,
  &#125;;
  <span class="hljs-keyword">let</span> body = &#123;
    <span class="hljs-attr">start_time</span>: <span class="hljs-title function_">dayjs</span>().<span class="hljs-title function_">startOf</span>(<span class="hljs-string">'day'</span>).<span class="hljs-title function_">valueOf</span>(),
    <span class="hljs-attr">end_time</span>: <span class="hljs-title function_">dayjs</span>().<span class="hljs-title function_">endOf</span>(<span class="hljs-string">'day'</span>).<span class="hljs-title function_">valueOf</span>(),
    <span class="hljs-attr">userid_list</span>: userid_list.<span class="hljs-title function_">join</span>(), <span class="hljs-comment">// userid 列表</span>
    <span class="hljs-attr">offset</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">size</span>: <span class="hljs-number">20</span>,
  &#125;;
  <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">await</span> axios.<span class="hljs-title function_">post</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;baseURL&#125;</span>/topapi/attendance/getleavestatus`</span>, body, &#123; params &#125;);
  <span class="hljs-keyword">if</span> (res.<span class="hljs-property">errcode</span> != <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> res;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> res.<span class="hljs-property">result</span>.<span class="hljs-property">leave_status</span>.<span class="hljs-title function_">map</span>(<span class="hljs-function">(<span class="hljs-params">row</span>) =></span> row.<span class="hljs-property">userid</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行以上方法后，就可以获取到当天已请假的用户。接着在所有需要检测打卡状态的用户列表中，过滤掉已请假的用户：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 需要检测打卡的 userid 数组</span>
<span class="hljs-keyword">let</span> alluids = [<span class="hljs-string">'xxx'</span>, <span class="hljs-string">'xxxx'</span>];
<span class="hljs-comment">// 获取请假状态</span>
<span class="hljs-keyword">let</span> leaveRes = <span class="hljs-keyword">await</span> <span class="hljs-title function_">getLeaveStatus</span>(alluids);
<span class="hljs-keyword">if</span> (leaveRes.<span class="hljs-property">errcode</span>) &#123;
  <span class="hljs-keyword">return</span> leaveRes;
&#125;
alluids = alluids.<span class="hljs-title function_">filter</span>(<span class="hljs-function">(<span class="hljs-params">uid</span>) =></span> !leaveRes.<span class="hljs-title function_">includes</span>(uid));
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(alluids); <span class="hljs-comment">// 过滤后的 userid 数组</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就不会对已请假的用户发出提醒了。</p>
<h2 data-id="heading-1">钉钉 token 自动刷新</h2>
<p>在获取钉钉 API 时，首先要获取接口调用凭证（也就是 access_token），每个 API 调用时都要携带这个凭证。但这个凭证是有期限的，有效期一过 API 就会被禁止调用。</p>
<p>因此，这里非常重要的一个优化点，就是自动刷新 access_token。</p>
<p>怎么做呢？其实和在前端项目中实现一样，在 <code>axios</code> 的拦截器中判断 access_token 是否过期，如果过期则重新获取，然后继续执行请求。</p>
<p>首先，将获取凭证写成一个单独的方法，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">fetchToken</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> params = &#123;
      <span class="hljs-attr">appkey</span>: <span class="hljs-string">'xxx'</span>,
      <span class="hljs-attr">appsecret</span>: <span class="hljs-string">'xxx'</span>,
    &#125;;
    <span class="hljs-keyword">let</span> url = <span class="hljs-string">'https://oapi.dingtalk.com/gettoken'</span>;
    <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">await</span> axios.<span class="hljs-title function_">get</span>(url, &#123; params &#125;);
    <span class="hljs-keyword">if</span> (result.<span class="hljs-property">data</span>.<span class="hljs-property">errcode</span> != <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">throw</span> result.<span class="hljs-property">data</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">let</span> token_str = <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(&#123;
        <span class="hljs-attr">token</span>: result.<span class="hljs-property">data</span>.<span class="hljs-property">access_token</span>,
        <span class="hljs-attr">expire</span>: <span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>() + result.<span class="hljs-property">data</span>.<span class="hljs-property">expires_in</span> * <span class="hljs-number">1000</span>,
      &#125;);
      <span class="hljs-keyword">new</span> <span class="hljs-title class_">DingToken</span>().<span class="hljs-title function_">set</span>(token_str);
      <span class="hljs-keyword">return</span> token_str;
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(error);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法主要是调用获取凭证的 API，调用成功后会返回 access_token 和有效时间。这里我们要设置一个过期时间，就是<code>当前时间+有效时间</code>，生成一个过期时间的时间戳：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>() + result.<span class="hljs-property">data</span>.<span class="hljs-property">expires_in</span> * <span class="hljs-number">1000</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里还有一个 <code>DingToken</code> 类是用于获取和存储 access_token 的，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">var</span> catch_dir = path.<span class="hljs-title function_">resolve</span>(__dirname, <span class="hljs-string">'../'</span>, <span class="hljs-string">'catch'</span>);
<span class="hljs-keyword">class</span> <span class="hljs-title class_">DingToken</span> &#123;
  <span class="hljs-title function_">get</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">let</span> res = fs.<span class="hljs-title function_">readFileSync</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;catch_dir&#125;</span>/ding_token.json`</span>);
    <span class="hljs-keyword">return</span> res.<span class="hljs-title function_">toString</span>() || <span class="hljs-literal">null</span>;
  &#125;
  <span class="hljs-title function_">set</span>(<span class="hljs-params">token</span>) &#123;
    fs.<span class="hljs-title function_">writeFileSync</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;catch_dir&#125;</span>/ding_token.json`</span>, token);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 access_token 和过期时间组成一个 JSON 字符串存储到文件中，接下来就可以在 <code>axios</code> 的请求拦截器中获取到这个 JSON 数据，然后判断当前时间是否大于过期时间。</p>
<p>如果是，则重新调用 <code>fetchToken()</code> 方法生成新 token，并继续执行请求。拦截器代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">'axios'</span>);
<span class="hljs-keyword">const</span> instance = axios.<span class="hljs-title function_">create</span>(&#123;
  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'https://oapi.dingtalk.com'</span>,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>,
&#125;);
<span class="hljs-keyword">const</span> dingToken = <span class="hljs-keyword">new</span> <span class="hljs-title class_">DingToken</span>();
<span class="hljs-comment">// 请求拦截器</span>
instance.<span class="hljs-property">interceptors</span>.<span class="hljs-property">request</span>.<span class="hljs-title function_">use</span>(<span class="hljs-keyword">async</span> (config) => &#123;
  <span class="hljs-keyword">if</span> (!config.<span class="hljs-property">params</span>.<span class="hljs-property">access_token</span>) &#123;
    <span class="hljs-keyword">let</span> catoken = &#123;&#125;;
    <span class="hljs-keyword">if</span> (dingToken.<span class="hljs-title function_">get</span>()) &#123;
      catoken = <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">parse</span>(dingToken.<span class="hljs-title function_">get</span>());
      <span class="hljs-comment">// 判断是否过期</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>() - catoken.<span class="hljs-property">expire</span> >= <span class="hljs-number">0</span>) &#123;
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'钉钉 token 过期'</span>);
        <span class="hljs-keyword">await</span> <span class="hljs-title function_">fetchToken</span>();
        catoken = <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">parse</span>(dingToken.<span class="hljs-title function_">get</span>());
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 第一次获取token</span>
      <span class="hljs-keyword">await</span> <span class="hljs-title function_">fetchToken</span>();
      catoken = <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">parse</span>(dingToken.<span class="hljs-title function_">get</span>());
    &#125;
    <span class="hljs-comment">// 将 token 携带至请求头</span>
    config.<span class="hljs-property">params</span>.<span class="hljs-property">access_token</span> = catoken.<span class="hljs-property">token</span>;
  &#125;
  <span class="hljs-keyword">return</span> config;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面在拦截器中编写的逻辑，我们就不需要关心 access_token 过期了。并且我们是在 token 过期之后才会重新请求，因此也不会触发调用频率限制。</p>
<h2 data-id="heading-2">总结</h2>
<p>本篇介绍了钉钉打卡小工具两个方面的优化，还有配置部分的代码我也做了精简，可以更快的接入自己的钉钉应用。</p>
<p>本次代码已经开源，地址在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fruidoc%2Fattend-robot" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ruidoc/attend-robot" ref="nofollow noopener noreferrer">GitHub</a>，欢迎大家尝试和 star。</p></div>  
</div>
            