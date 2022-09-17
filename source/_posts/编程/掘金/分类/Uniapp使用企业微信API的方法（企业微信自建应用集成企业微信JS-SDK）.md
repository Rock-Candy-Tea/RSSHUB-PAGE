
---
title: 'Uniapp使用企业微信API的方法（企业微信自建应用集成企业微信JS-SDK）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3386'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 23:24:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=3386'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1、业务需求</h4>
<p>使用uniapp打包的H5应用，要集成企业微信的js-sdk。在用户点击分享的时候，自定义分享的内容。</p>
<h4 data-id="heading-1">2、需求难点分析</h4>
<ul>
<li>uniapp关于企业微信<code>jweixin</code>全局对象的引入。</li>
<li><code>wx.config</code>获取对应配置的数据需要后端高度配合。</li>
<li><code>wx.config</code>注册后使用对应企业微信API的调用方法。</li>
<li>api和代码的修改需要实时部署，不然无法调试。</li>
</ul>
<p>上述难点主要集中在全局注册企业微信<code>jweixin</code>对象和后端签名算法。</p>
<h4 data-id="heading-2">3、实现需求：自定义企业微信转发</h4>
<p>参考企业微信文档： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.work.weixin.qq.com%2Fdocument%2Fpath%2F90514" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.work.weixin.qq.com/document/path/90514" ref="nofollow noopener noreferrer">developer.work.weixin.qq.com/document/pa…</a></p>
<ol start="0">
<li>
<p><strong>引入js-sdk</strong></p>
<ul>
<li>
<pre><code class="hljs language-lua copyable" lang="lua">npm install jweixin-<span class="hljs-built_in">module</span> <span class="hljs-comment">--save </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局下载<code>jweixin</code>模块。因为只在自建应用中使用，所以要使用条件编译引入。</p>
</li>
<li>
<pre><code class="hljs language-ini copyable" lang="ini">// <span class="hljs-comment">#ifdef H5</span>
const <span class="hljs-attr">jweixin</span> = require(<span class="hljs-string">"jweixin-module"</span>)<span class="hljs-comment">;</span>
const <span class="hljs-attr">env</span> = uni.getSystemInfoSync().platform<span class="hljs-comment">;</span>
console.log("env, 当前环境", env)
if (<span class="hljs-attr">env</span> === <span class="hljs-string">"ios"</span>) &#123;
  <span class="hljs-attr">Vue.prototype.wx</span> = jweixin<span class="hljs-comment">;</span>
//   <span class="hljs-attr">Vue.prototype.jweixin</span> = wx<span class="hljs-comment">;</span>
&#125; else &#123;
  <span class="hljs-attr">Vue.prototype.jweixin</span> = jweixin<span class="hljs-comment">;</span>
&#125;
// <span class="hljs-comment">#endif</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在H5环境下动态引入<code>jweixin</code>对象。因为IOS端全局对象自带wx对象，所以要用<code>jweixin</code>覆盖。</p>
</li>
<li>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://open.work.weixin.qq.com/wwopen/js/jwxwork-1.0.0.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>index.html</code>中引入企业微信相关依赖；</p>
</li>
</ul>
<p>2、<strong>通过config接口注入权限验证配置</strong></p>
<ul>
<li>
<pre><code class="hljs language-csharp copyable" lang="csharp">wx.config(&#123;
    beta: <span class="hljs-literal">true</span>,<span class="hljs-comment">// 必须这么写，否则wx.invoke调用形式的jsapi会有问题</span>
    debug: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。</span>
    appId: <span class="hljs-string">''</span>, <span class="hljs-comment">// 必填，企业微信的corpID</span>
    timestamp: , <span class="hljs-comment">// 必填，生成签名的时间戳</span>
    nonceStr: <span class="hljs-string">''</span>, <span class="hljs-comment">// 必填，生成签名的随机串</span>
    signature: <span class="hljs-string">''</span>,<span class="hljs-comment">// 必填，签名，见 附录-JS-SDK使用权限签名算法</span>
    jsApiList: [] <span class="hljs-comment">// 必填，需要使用的JS接口列表，凡是要调用的接口都需要传进来</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面appId后面的参数都是由后端包装后通过接口返回。特别注意<code>signature</code>签名的生成需要使用企业的<strong>corpID</strong>生成，而且<code>timestamp</code>时间戳必须是<strong>数字类型</strong>。</p>
</li>
</ul>
<p>3、<strong>通过ready接口处理成功验证</strong></p>
<ul>
<li>
<pre><code class="hljs language-lua copyable" lang="lua">wx.ready(<span class="hljs-function"><span class="hljs-keyword">function</span><span class="hljs-params">()</span></span>&#123;
    // <span class="hljs-built_in">config</span>信息验证后会执行ready方法，所有接口调用都必须在<span class="hljs-built_in">config</span>接口获得结果之后，<span class="hljs-built_in">config</span>是一个客户端的异步操作，所以如果需要在页面加载时就调用相关接口，则须把相关接口放在ready函数中调用来确保正确执行。对于用户触发时才调用的接口，则可以直接调用，不需要放在ready函数中。
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在config信息验证成功后，就在ready方法里面调用相关的接口。</p>
</li>
</ul>
<p>4、<strong>通过error接口处理失败验证</strong></p>
<ul>
<li>
<pre><code class="hljs language-lua copyable" lang="lua">wx.<span class="hljs-built_in">error</span>(<span class="hljs-function"><span class="hljs-keyword">function</span><span class="hljs-params">(res)</span></span>&#123;
    // <span class="hljs-built_in">config</span>信息验证失败会执行<span class="hljs-built_in">error</span>函数，如签名过期导致验证失败，具体错误信息可以打开<span class="hljs-built_in">config</span>的<span class="hljs-built_in">debug</span>模式查看，也可以在返回的res参数中查看，对于SPA可以在这里更新签名。
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ol>
<h4 data-id="heading-3">4、接口封装，接口调用</h4>
<ol start="0">
<li>
<p>封装一个请求接口，因为每一个页面调用的API都用时效性，出了这个页面就没法调用。所以需要封装一个灵活的方法来在不同的页面动态引入注入权限验证配置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qyGetUserTag <span class="hljs-keyword">from</span> <span class="hljs-string">"../api/user.js"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">getWxConfig</span>(<span class="hljs-params">qyApi, params</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-title function_">qyGetUserTag</span>(&#123;
      <span class="hljs-attr">pageUrl</span>: <span class="hljs-variable language_">window</span>.<span class="hljs-property">location</span>.<span class="hljs-property">href</span>.<span class="hljs-title function_">split</span>(<span class="hljs-string">"#"</span>)[<span class="hljs-number">0</span>],
    &#125;).<span class="hljs-title function_">then</span>(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: data &#125; = res.<span class="hljs-property">data</span>;
      <span class="hljs-keyword">const</span> wxConfig = data
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-variable language_">window</span>.<span class="hljs-property">location</span>.<span class="hljs-property">href</span>, <span class="hljs-string">"当前调用的页面"</span>);
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(wxConfig, <span class="hljs-string">"wxConfig内容"</span>);
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">jweixin</span>.<span class="hljs-title function_">config</span>(&#123; <span class="hljs-comment">// jweixin是全局注册的企业微信api对象</span>
        <span class="hljs-attr">beta</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 必须这么写，否则wx.invoke调用形式的jsapi会有问题</span>
        <span class="hljs-attr">debug</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。</span>
        <span class="hljs-attr">appId</span>: wxConfig.<span class="hljs-property">corpid</span>, <span class="hljs-comment">// 必填，企业微信的corpID</span>
        <span class="hljs-attr">timestamp</span>: wxConfig.<span class="hljs-property">timestamp</span>, <span class="hljs-comment">// 必填，生成签名的时间戳</span>
        <span class="hljs-attr">nonceStr</span>: wxConfig.<span class="hljs-property">noncestr</span>, <span class="hljs-comment">// 必填，生成签名的随机串</span>
        <span class="hljs-attr">signature</span>: wxConfig.<span class="hljs-property">signature</span>, <span class="hljs-comment">// 必填，签名，见 附录-JS-SDK使用权限签名算法</span>
        <span class="hljs-attr">jsApiList</span>: [qyApi], <span class="hljs-comment">// 必填，需要使用的JS接口列表，凡是要调用的接口都需要传进来</span>
      &#125;);
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">jweixin</span>.<span class="hljs-title function_">ready</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"ready初始化完成"</span>);
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">jweixin</span>[qyApi](params);
        <span class="hljs-title function_">resolve</span>(data);
      &#125;);
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">jweixin</span>.<span class="hljs-title function_">error</span>(<span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) &#123;
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(error, <span class="hljs-string">"打印错误信息"</span>);
        <span class="hljs-title function_">reject</span>(error);
      &#125;);
    &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>调用接口的时候，传入两个参数，需要调用的方法，和方法传入的参数。我这里使用了企业微信分享功能：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">wx.<span class="hljs-title function_">onMenuShareAppMessage</span>(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">''</span>, <span class="hljs-comment">// 分享标题</span>
    <span class="hljs-attr">desc</span>: <span class="hljs-string">''</span>, <span class="hljs-comment">// 分享描述</span>
    <span class="hljs-attr">link</span>: <span class="hljs-string">''</span>, <span class="hljs-comment">// 分享链接；在微信上分享时，该链接的域名必须与企业某个应用的可信域名一致</span>
    <span class="hljs-attr">imgUrl</span>: <span class="hljs-string">''</span>, <span class="hljs-comment">// 分享图标</span>
    <span class="hljs-attr">success</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
        <span class="hljs-comment">// 用户确认分享后执行的回调函数</span>
    &#125;,
    <span class="hljs-attr">cancel</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
        <span class="hljs-comment">// 用户取消分享后执行的回调函数</span>
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法引入和调用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; getWxConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../../utils/wx_init.js"</span>; <span class="hljs-comment">// 方法引入</span>
​
<span class="hljs-keyword">async</span> <span class="hljs-title function_">getWxData</span>(<span class="hljs-params"></span>) &#123; <span class="hljs-comment">// 方法定义</span>
    <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">await</span> getWxConfig.<span class="hljs-title function_">call</span>(<span class="hljs-variable language_">this</span>, <span class="hljs-string">"onMenuShareAppMessage"</span>, &#123; <span class="hljs-comment">// 绑定到当前页面</span>
        <span class="hljs-attr">title</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">qy_postMessage</span>.<span class="hljs-property">title</span>, <span class="hljs-comment">// 分享标题</span>
        <span class="hljs-attr">desc</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">qy_postMessage</span>.<span class="hljs-property">summary</span>, <span class="hljs-comment">// 分享描述</span>
        <span class="hljs-attr">link</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">qy_postMessage</span>.<span class="hljs-property">href</span>, <span class="hljs-comment">// 分享链接；在微信上分享时，该链接的域名必须与企业某个应用的可信域名一致</span>
        <span class="hljs-attr">imgUrl</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">qy_postMessage</span>.<span class="hljs-property">imageUrl</span>, <span class="hljs-comment">// 分享图标</span>
        <span class="hljs-attr">success</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"分享成功"</span>);
            <span class="hljs-comment">// 用户确认分享后执行的回调函数</span>
        &#125;,
        <span class="hljs-attr">cancel</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"分享失败"</span>);
            <span class="hljs-comment">// 用户取消分享后执行的回调函数</span>
        &#125;,
    &#125;);
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(res, <span class="hljs-string">"微信返回的值。webview 测试"</span>);
&#125;,
 <span class="hljs-title function_">mounted</span>(<span class="hljs-params"></span>) &#123; <span class="hljs-comment">// 方法调用</span>
      <span class="hljs-comment">// #ifdef H5</span>
     <span class="hljs-keyword">const</span> origin = <span class="hljs-string">"https://qyhtest.citic.com"</span>;
     <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">addEventListener</span>(
          <span class="hljs-string">"message"</span>,
          <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
              <span class="hljs-keyword">if</span> (e.<span class="hljs-property">origin</span> === origin) &#123;
                  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">arg</span>: data &#125; = e.<span class="hljs-property">data</span>.<span class="hljs-property">data</span>;
                  <span class="hljs-variable language_">this</span>.<span class="hljs-property">qy_postMessage</span> = data;
                  <span class="hljs-variable language_">this</span>.<span class="hljs-property">qy_postMessage</span> && <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">getWxData</span>();
              &#125;
          &#125;,
          <span class="hljs-literal">false</span>
      );
      <span class="hljs-comment">// #endif</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol></div>  
</div>
            