
---
title: '_wx-open-launch-app_ 微信开放标签 H5跳转App踩坑'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5279'
author: 掘金
comments: false
date: Tue, 04 May 2021 19:54:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=5279'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">背景</h3>
<p>业务需求中，经常有页面会供用户分享到微信<br>
其他用户在微信中打开H5后，点击相应按钮，此时若用户手机中已经安装了App，则直接唤起App并自动跳转到对应页面</p>
<p>这里就需要接入微信开放标签中的 <code><wx-open-launch-app></code> 标签，以向客户端传递 extinfo 来指定对应页面</p>
<p>使用步骤见官方文档：<a href="https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_Open_Tag.html" target="_blank" rel="nofollow noopener noreferrer">开放标签说明文档</a>，在此不赘述</p>
<p>但是文档除了接入步骤外，相关注意事项的信息量十分微薄，此中坑位就由我一一道来<br>
（都是一些小注意点，但是遇到了可能会花费些时间才能找到原因）</p>
<h3 data-id="heading-1">wx.config</h3>
<p>首先与使用 JS-SDK 一致，需要先引入 <code>jweixin.js</code>，后通过 <code>wx.config</code> 进行配置与申请</p>
<p>这里的一个注意点是，即使只需要引入开放标签而不需要使用任何 JsApi，也需要至少向 <code>jsApiList</code> 传递一项，不能为空数组，如</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">wx.config(&#123;
    ...
    <span class="hljs-attr">jsApiList</span>: [<span class="hljs-string">'onMenuShareWeibo'</span>],
    <span class="hljs-attr">openTagList</span>: [<span class="hljs-string">'wx-open-launch-app'</span>]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>否则会导致iOS配置的没问题，但安卓始终无法配置成功，触发 <code>wx.error</code><br>
（最坑的是在开发者工具上是没有问题的，真机验证时才会发现，而且 error 输出的内容也不相干）</p>
<h3 data-id="heading-2">标签引用</h3>
<p>官方文档中的引用示例如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">wx-open-launch-app</span> <span class="hljs-attr">xx</span>=<span class="hljs-string">'xx'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css"><span class="hljs-selector-class">.btn</span> &#123; <span class="hljs-attribute">padding</span>: <span class="hljs-number">12px</span> &#125;</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span>></span>App内查看<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">wx-open-launch-app</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而在 React 中不能使用 <code><template></code> 标签（React 会将小写字母开头的标签视为原生的 html 标签），因此需要改用微信提供的 <code><script type='text/wxtag-template'></code></p>
<p>并且 <code><style></code> 中的样式需要以字符串形式编写，或直接在 button 上写行内样式</p>
<p>所以准确的示例应该如下</p>
<pre><code class="hljs language-html copyable" lang="html">// @ts-ignore
<span class="hljs-tag"><<span class="hljs-name">wx-open-launch-app</span> <span class="hljs-attr">xx</span>=<span class="hljs-string">'xx'</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">'text/wxtag-template'</span>></span><span class="handlebars"><span class="xml">
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span>&#123;'.btn &#123; padding: 12px &#125;'&#125;<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'btn'</span> <span class="hljs-attr">style</span>=</span></span><span class="hljs-template-variable">&#123;&#123; ... &#125;&#125;</span><span class="xml"><span class="hljs-tag">></span>App内查看<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  </span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
&#123;/* @ts-ignore */&#125;
<span class="hljs-tag"></<span class="hljs-name">wx-open-launch-app</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">样式编写</h3>
<p>外部样式无法影响到标签内元素的样式<br>
（猜测是包裹着元素的 <code><script></code> 对外部样式进行了隔离）</p>
<p>编写单位时不能使用 <code>vw</code>、<code>vh</code>，因此需要 <code>getPx</code> 转化</p>
<p><code><wx-open-launch-app></code> 的父元素不能是 flex 布局，否则会被挤到宽度近乎为0</p>
<h3 data-id="heading-4">标签属性</h3>
<h5 data-id="heading-5">appid</h5>
<p>appid 是在微信公众平台中配置的<strong>关联应用</strong>的 appId（注意不是公众号的 appId）</p>
<p>当碰上 <code>"launch:fail_check fail"</code> 报错时，应该检查的可能性有两个</p>
<ul>
<li>上述的 appId 是否准确</li>
<li>wx.config 中的 appId 配置的公众号Id是否准确（业务有两个公众号，默认使用的是公众号A，而当时后台却配在公众号B，因此也被这个报错消磨了半天）</li>
</ul>
<h5 data-id="heading-6">extinfo</h5>
<p>extinfo 里放的是最重要的，即要给到客户端的需跳转到的对应路径信息</p>
<p>其格式是字符串，因此如果约定的数据是对象，不要忘了先 <code>JSON.stringify</code> 下，给到客户端自行解析</p>
<h3 data-id="heading-7">错误信息获取</h3>
<p>文档中写着 error 事件的返回值是 &#123; errMsg: string &#125;，但实际上应该是 <code>&#123; detail: string &#125;</code>，即</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">btn.addEventListener(<span class="hljs-string">'error'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fail'</span>, e.detail);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">兜底处理</h3>
<h5 data-id="heading-9">唤起失败</h5>
<p>用户手机中可能未装有对应 App，及其他不会成功唤起 App 的情况</p>
<p>因此需要在 <code>wx.error</code> 和 <code><wx-open-launch-app></code> 绑定的 <code>error</code> 事件中都进行兜底处理，如调起原有的跳转到 AppStore / 应用宝等的流程<br>
（wx.error 是针对微信版本、系统版本过低导致的配置失败的处理，开放标签的 error 则是针对应用尚未安装的处理）</p>
<h5 data-id="heading-10">初始化未完成</h5>
<p>在微信开放标签初始化完成之前（一般在1s内），按钮是不会显示的（只显示为一个小白圆圈👇）
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff0ac1e4f28c4d29b3d4bf661a3d7b14~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此可以写多一个 loading 状态的按钮展示，在开放标签的 <code>ready</code> 事件触发之后再进行替换</p></div>  
</div>
            