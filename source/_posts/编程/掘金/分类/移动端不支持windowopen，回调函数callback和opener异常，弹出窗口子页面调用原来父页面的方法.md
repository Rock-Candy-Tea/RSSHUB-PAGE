
---
title: '移动端不支持window.open，回调函数callback和opener异常，弹出窗口子页面调用原来父页面的方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4077ab1bbb5464ba88d30044cc624d6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 01:53:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4077ab1bbb5464ba88d30044cc624d6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.移动端不支持window.open</h2>
<p><strong>移动端是不支持window.open打开小窗口的，会自动转成打开一个新页面</strong>，你可以<strong>使用第三方插件layer.open</strong>实现打开小窗口的功能。</p>
<p>第三方插件layer.open的使用可以<strong>参考官方API</strong>地址如下
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.layui.com%2Fdoc%2Fmodules%2Flayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.layui.com/doc/modules/layer.html" ref="nofollow noopener noreferrer">layer.open官方API</a></p>
<p><strong>分享一个我的代码和效果图：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    $(<span class="hljs-string">'#gyslb'</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> gslbs = $(<span class="hljs-string">"#gslb"</span>).val();
 layer.config(&#123;
      <span class="hljs-attr">extend</span>: <span class="hljs-string">'../../../layer.css'</span> <span class="hljs-comment">//自定义定义手机端弹窗皮肤，可以省略</span>
   &#125;);
 layer.open(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">area</span>: [<span class="hljs-string">'90%'</span>, <span class="hljs-string">'90%'</span>],
      <span class="hljs-attr">title</span>: <span class="hljs-string">'选择经营品目'</span>,
      <span class="hljs-attr">shadeClose</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">//点击遮罩关闭</span>
      <span class="hljs-comment">//maxmin: true, //最大、最小按钮</span>
      <span class="hljs-attr">content</span>: <span class="hljs-string">'../../****.html,//小窗口页面的地址
    &#125;);
  &#125;);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4077ab1bbb5464ba88d30044cc624d6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2.移动端不支持opener，导致回调函数异常</h2>
<p>使用了layer.open后，<strong>可以把opener换成parent</strong>，即可解决这个问题</p>
<h2 data-id="heading-2">3. layer弹出层父子页面事件相互调用方法</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jb51.net%2Farticle%2F145817.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jb51.net/article/145817.htm" ref="nofollow noopener noreferrer">原文</a>
父页面</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><body>
 
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">data-url</span>=<span class="hljs-string">"bbbb.html"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"parentIframe"</span>></span>小小提示层<span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"shuzhi"</span> /></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"but_par"</span>></span>父页面<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</body>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../jquery-1.9.1.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"layer/layer.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<script>
$(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
$(<span class="hljs-string">"#parentIframe"</span>).click(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">var</span> a = $(<span class="hljs-built_in">this</span>).attr(<span class="hljs-string">"data-url"</span>);
layer.open(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">content</span>: a,
  <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">layero, index</span>)</span>&#123;
    <span class="hljs-keyword">var</span> body = layer.getChildFrame(<span class="hljs-string">'body'</span>, index);<span class="hljs-comment">//获取子页面内容</span>
    <span class="hljs-keyword">var</span> iframeWin = <span class="hljs-built_in">window</span>[layero.find(<span class="hljs-string">'iframe'</span>)[<span class="hljs-number">0</span>][<span class="hljs-string">'name'</span>]]; <span class="hljs-comment">//得到iframe页的窗口对象，执行iframe页的方法：iframeWin.method();</span>
   body.find(<span class="hljs-string">"#transmit"</span>).click();<span class="hljs-comment">//执行子页面的方法</span>
    body.find(<span class="hljs-string">'input'</span>).val(<span class="hljs-string">'Hi，我是从父页来的'</span>)
    $(<span class="hljs-string">".but_par"</span>).click(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    alert(<span class="hljs-number">222</span>);
    &#125;)
  &#125;
&#125;); 
&#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子页面</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><body>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"不满意"</span> /></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"transmit"</span>></span>给父层传值<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</div>
</body>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
$(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
$(<span class="hljs-built_in">document</span>).on(<span class="hljs-string">"click"</span>,<span class="hljs-string">"#transmit"</span>).click(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
parent.$(<span class="hljs-string">"#shuzhi"</span>).val($(<span class="hljs-string">"#name"</span>).val());
parent.location.reload(); 刷新父页面
<span class="hljs-comment">//关闭layer弹出层</span>
<span class="hljs-keyword">var</span> index = parent.layer.getFrameIndex(<span class="hljs-built_in">window</span>.name); <span class="hljs-comment">//获取窗口索引</span>
parent.layer.close(index);
&#125;)
<span class="hljs-built_in">window</span>.parent.$(<span class="hljs-string">".but_par"</span>).click();<span class="hljs-comment">//执行父页面的事件</span>
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            