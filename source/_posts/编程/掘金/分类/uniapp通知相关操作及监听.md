
---
title: 'uniapp通知相关操作及监听'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3d7b643100d41f1a2a5676f2fcb7ccf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 00:17:50 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3d7b643100d41f1a2a5676f2fcb7ccf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">NotifyPlugin</h1>
<h3 data-id="heading-1">简介</h3>
<p>一个即可发送通知取消通知且还监听通知栏内容获取通知消息容的插件（相应权限获取判断插件内部都已处理好）</p>
<h3 data-id="heading-2">预览</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3d7b643100d41f1a2a5676f2fcb7ccf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">引用</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> notifyModule = uni.requireNativePlugin(<span class="hljs-string">"Chen-Notify"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">onStartNotifyListen(CACLLBACK)</h3>
<p>开启监听通知栏内容事件</p>
<h5 data-id="heading-5">CACLLBACK<strong>参数说明</strong></h5>

























<table><thead><tr><th><strong>参数</strong></th><th><strong>类型</strong></th><th><strong>说明</strong></th></tr></thead><tbody><tr><td>success</td><td>Boolean</td><td>操作状态</td></tr><tr><td>code</td><td>Int</td><td>状态码（200：操作成功，400：用户操作异常，500：插件内部操作异常）</td></tr><tr><td>msg</td><td>String</td><td>返回信息</td></tr></tbody></table>
<h5 data-id="heading-6"><strong>示例</strong></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title function_">onStartNotifyListen</span>(<span class="hljs-params"></span>)&#123;
  notifyModule.<span class="hljs-title function_">onStartNotifyListen</span>(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
    uni.<span class="hljs-title function_">showToast</span>(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'result：'</span> + <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(result),
      <span class="hljs-attr">icon</span>:<span class="hljs-string">"none"</span>
    &#125;)
  &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">onStopNotifyListen(CACLLBACK)</h3>
<p>停止监听通知内容事件</p>
<h5 data-id="heading-8">CACLLBACK<strong>参数说明</strong></h5>

























<table><thead><tr><th><strong>参数</strong></th><th><strong>类型</strong></th><th><strong>说明</strong></th></tr></thead><tbody><tr><td>success</td><td>Boolean</td><td>操作状态</td></tr><tr><td>code</td><td>Int</td><td>状态码（200：操作成功，400：用户操作异常，500：插件内部操作异常）</td></tr><tr><td>msg</td><td>String</td><td>返回信息</td></tr></tbody></table>
<h5 data-id="heading-9"><strong>示例</strong></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title function_">onStopNotifyListen</span>(<span class="hljs-params"></span>)&#123;
  notifyModule.<span class="hljs-title function_">onStopNotifyListen</span>(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
    uni.<span class="hljs-title function_">showToast</span>(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'result：'</span> + <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(result),
      <span class="hljs-attr">icon</span>:<span class="hljs-string">"none"</span>
    &#125;)
  &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">onNotify(CACLLBACK)</h3>
<p>通知栏内容获取全局事件</p>
<h5 data-id="heading-11">CACLLBACK<strong>参数说明</strong></h5>






























<table><thead><tr><th><strong>参数</strong></th><th><strong>类型</strong></th><th><strong>说明</strong></th></tr></thead><tbody><tr><td>success</td><td>Boolean</td><td>操作状态</td></tr><tr><td>data</td><td>String</td><td>通知栏内容信息（标题：title，内容：content）</td></tr><tr><td>code</td><td>Int</td><td>状态码（200：操作成功，400：用户操作异常，500：插件内部操作异常）</td></tr><tr><td>msg</td><td>String</td><td>返回信息</td></tr></tbody></table>
<h5 data-id="heading-12"><strong>示例</strong></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">plus.<span class="hljs-property">globalEvent</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'onNotify'</span>, <span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (result.<span class="hljs-property">success</span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">info</span> = result.<span class="hljs-property">data</span>
  &#125;
  uni.<span class="hljs-title function_">showToast</span>(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"result："</span> + <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(result),
    <span class="hljs-attr">icon</span>: <span class="hljs-string">"none"</span>
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">notify(OPTIONS，CACLLBACK)</h3>
<p>发送通知事件</p>
<h5 data-id="heading-14">OPTIONS<strong>参数说明</strong></h5>



































<table><thead><tr><th><strong>参数</strong></th><th><strong>类型</strong></th><th align="center">必填</th><th><strong>说明</strong></th></tr></thead><tbody><tr><td>id</td><td>Int</td><td align="center">是</td><td>通知ID，取消指定通知时需要</td></tr><tr><td>icon</td><td>String</td><td align="center">是</td><td>通知栏图标</td></tr><tr><td>title</td><td>String</td><td align="center">是</td><td>通知栏标题</td></tr><tr><td>content</td><td>String</td><td align="center">是</td><td>通知栏标内容</td></tr></tbody></table>
<h5 data-id="heading-15">CACLLBACK<strong>参数说明</strong></h5>

























<table><thead><tr><th><strong>参数</strong></th><th><strong>类型</strong></th><th><strong>说明</strong></th></tr></thead><tbody><tr><td>success</td><td>Boolean</td><td>操作状态</td></tr><tr><td>code</td><td>Int</td><td>状态码（200：操作成功，400：用户操作异常，500：插件内部操作异常）</td></tr><tr><td>msg</td><td>String</td><td>返回信息</td></tr></tbody></table>
<h5 data-id="heading-16"><strong>示例</strong></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">notifyModule.<span class="hljs-title function_">notify</span>(&#123;
  <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">icon</span>: <span class="hljs-string">"/static/logo.png"</span>,
  <span class="hljs-attr">title</span>: <span class="hljs-string">'通知标题'</span>,
  <span class="hljs-attr">content</span>: <span class="hljs-string">'这是通知内容'</span>
&#125;,<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  uni.<span class="hljs-title function_">showToast</span>(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'result：'</span> + <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(result),
    <span class="hljs-attr">icon</span>:<span class="hljs-string">"none"</span>
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">cancel(OPTIONS，CACLLBACK)</h3>
<p>取消指定通知事件</p>
<h5 data-id="heading-18">OPTIONS<strong>参数说明</strong></h5>

















<table><thead><tr><th><strong>参数</strong></th><th><strong>类型</strong></th><th align="center">必填</th><th><strong>说明</strong></th></tr></thead><tbody><tr><td>id</td><td>Int</td><td align="center">是</td><td>通知ID</td></tr></tbody></table>
<h5 data-id="heading-19">CACLLBACK<strong>参数说明</strong></h5>

























<table><thead><tr><th><strong>参数</strong></th><th><strong>类型</strong></th><th><strong>说明</strong></th></tr></thead><tbody><tr><td>success</td><td>Boolean</td><td>操作状态</td></tr><tr><td>code</td><td>Int</td><td>状态码（200：操作成功，400：用户操作异常，500：插件内部操作异常）</td></tr><tr><td>msg</td><td>String</td><td>返回信息</td></tr></tbody></table>
<h5 data-id="heading-20"><strong>示例</strong></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">notifyModule.<span class="hljs-title function_">cancel</span>(&#123;
  <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>
&#125;,<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  uni.<span class="hljs-title function_">showToast</span>(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'result：'</span> + <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(result),
    <span class="hljs-attr">icon</span>:<span class="hljs-string">"none"</span>
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">cancelAll(CACLLBACK)</h3>
<p>取消所有通知事件</p>
<h5 data-id="heading-22">CACLLBACK<strong>参数说明</strong></h5>

























<table><thead><tr><th><strong>参数</strong></th><th><strong>类型</strong></th><th><strong>说明</strong></th></tr></thead><tbody><tr><td>success</td><td>Boolean</td><td>操作状态</td></tr><tr><td>code</td><td>Int</td><td>状态码（200：操作成功，400：用户操作异常，500：插件内部操作异常）</td></tr><tr><td>msg</td><td>String</td><td>返回信息</td></tr></tbody></table>
<h5 data-id="heading-23"><strong>示例</strong></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">notifyModule.<span class="hljs-title function_">cancelAll</span>(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  uni.<span class="hljs-title function_">showToast</span>(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'result：'</span> + <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">stringify</span>(result),
    <span class="hljs-attr">icon</span>:<span class="hljs-string">"none"</span>
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D9393" target="_blank" rel="nofollow noopener noreferrer" title="https://ext.dcloud.net.cn/plugin?id=9393" ref="nofollow noopener noreferrer">插件地址</a></p></div>  
</div>
            