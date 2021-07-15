
---
title: 'Vue Router 中实现在新窗口打开页面'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862bdd7fb31f4393b24c093d50a56232~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 06:03:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862bdd7fb31f4393b24c093d50a56232~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h4 data-id="heading-0">1. < router-link > 标签实现新窗口打开</h4>
<p>官方文档中说 v-link 指令被 < router-link > 组件指令替代，且 < router-link > 不支持 target="_blank"  属性，如果需要打开一个新窗口必须要用< a >标签，但事实上vue2版本的 < router-link > 是支持 target="_blank" 属性的 (tag="a")。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><router-link target=<span class="hljs-string">"_blank"</span> :to=<span class="hljs-string">"&#123;path:'/about',query:&#123;id:deviceId&#125;&#125;"</span>>关于</router-link>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span>&#123;
      <span class="hljs-attr">deviceId</span>:<span class="hljs-string">'123456'</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862bdd7fb31f4393b24c093d50a56232~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">2. 编程式导航</h4>
<p>有些时候需要在单击事件或者在函数中实现页面跳转，那么可以借助 router 的示例方法，通过编写代码实现。我们常用的是 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi mathvariant="normal">.</mi><mi>p</mi><mi>u</mi><mi>s</mi><mi>h</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">router.push 和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord">.</span><span class="mord mathnormal">p</span><span class="mord mathnormal">u</span><span class="mord mathnormal">s</span><span class="mord mathnormal">h</span><span class="mord cjk_fallback">和</span></span></span></span></span> router.go   但是 vue2.0 以后，这种方式就不支持新窗口打开的属性了，这个时候就需要使用this.$router.resolve。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><button @click=<span class="hljs-string">"gotest1"</span>>按钮</button>

<span class="hljs-function"><span class="hljs-title">gotest1</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-keyword">let</span> deviceId = <span class="hljs-string">'56789'</span>
   <span class="hljs-keyword">let</span> routeData = <span class="hljs-built_in">this</span>.$router.resolve(&#123;
      <span class="hljs-attr">query</span>: &#123;<span class="hljs-attr">id</span>:deviceId&#125;,
      <span class="hljs-attr">path</span>:<span class="hljs-string">'/test1'</span>
   &#125;);
   <span class="hljs-built_in">window</span>.open(routeData.href, <span class="hljs-string">'_blank'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f1bb92b8ccf4defb33e19a3b290b24c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            