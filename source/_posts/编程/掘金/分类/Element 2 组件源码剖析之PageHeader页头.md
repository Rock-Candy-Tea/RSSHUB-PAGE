
---
title: 'Element 2 组件源码剖析之PageHeader页头'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d94054934bb2408292b1ef83be0229c5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 23:53:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d94054934bb2408292b1ef83be0229c5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h1 data-id="heading-0">0x00 简介</h1>
<p>组件 <code>PageHeader</code> 用于用户需要快速理解当前页是什么时。相较于面包屑组件，使用页头组件的页面的路径比较简单。本文将深入分析源码，剖析其实现原理，耐心读完，相信会对您有所帮助。组件源码实现详见<code>packages/page-header/src/main.vue</code> 。 🔗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Fpage-header" target="_blank" rel="nofollow noopener noreferrer" title="https://element.eleme.cn/#/zh-CN/component/page-header" ref="nofollow noopener noreferrer">组件文档 PageHeader</a>  🔗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FElemeFE%2Felement%2Fblob%2Fdev%2Fpackages%2Fpage-header%2Fsrc%2Fmain.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/ElemeFE/element/blob/dev/packages/page-header/src/main.vue" ref="nofollow noopener noreferrer">gitee源码 main.vue </a></p>
<p>更多组件剖析详见 👉  <a href="https://juejin.cn/post/6994721241194037255" target="_blank" title="https://juejin.cn/post/6994721241194037255"><strong>📚 Element 2 源码剖析组件总览</strong></a> 。</p>
<hr>
<h1 data-id="heading-1">0x01  组件源码</h1>
<h2 data-id="heading-2">template 模板内容</h2>
<p>组件模板创建一个class名为<code>el-page-header</code>的<code><div></code> 元素根节点，包含两个子节点 <code>左侧标题区域</code>、<code>右侧内容区域</code>。</p>
<p>两个子节点都提供了具名插槽，分发内容时需要指明 <code>slot#name</code>，否则内容会被丢弃。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-page-header"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-page-header__left"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$emit('back')"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-back"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-page-header__title"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"title"</span>></span>&#123;&#123; title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-page-header__content"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"content"</span>></span>&#123;&#123; content &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">左侧标题区域</h3>
<p>该节点是一个class 名为<code>el-page-header__left</code>的<code><div></code> 元素,并添加了<code>click</code>事件监听。<br>
当点击左侧区域后触发<code>click</code>事件，调用内建的 <code>$emit</code> 并传入事件名称<code>back</code> 来触发回调。</p>
<p>该节点区域内包含两个元素节点：</p>
<ol>
<li>一个名为<code>el-icon-back</code>的Icon图标 。</li>
<li>一个class 名为<code>el-page-header__title</code>的<code><div></code> 元素，提供了具名插槽<code>title</code>。</li>
</ol>
<p>具名插槽<code>title</code>提供后备内容，prop的 <code>title</code> 属性，<code>title</code> 默认值通过国际化方法设置  <code>t('el.pageHeader.title')</code> ，使用中文语言时值为<code>返回</code>。</p>
<h3 data-id="heading-4">右侧内容区域</h3>
<p>该节点是一个class 名为<code>el-page-header__content</code>的<code><div></code> 元素，提供了具名插槽<code>content</code>。具名插槽<code>title</code>提供后备内容，prop的 <code>content</code> 属性。</p>
<h2 data-id="heading-5">attributes 属性</h2>
<p>组件定义了2 个prop : <code>title</code>、<code>content</code>。</p>
<p>属性<code>title</code> 默认值使用工厂函数调用国际化方法获取翻译文本<code>t('el.pageHeader.title')</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入国际化处理方法</span>
<span class="hljs-keyword">import</span> &#123; t &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui/src/locale'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>, 
      <span class="hljs-function"><span class="hljs-title">default</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> t(<span class="hljs-string">'el.pageHeader.title'</span>);
      &#125;
    &#125;, 
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用中文语言时值为<code>返回</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 中文语言包  src\locale\lang\zh-CN.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">el</span>: &#123; 
    <span class="hljs-attr">pageHeader</span>: &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'返回'</span>
    &#125;, 
  &#125;
&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">样式设置</h2>
<p><code>el-page-header</code> <code>el-page-header__left</code> 元素使用 flex 默认布局。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.el-page-header</span> &#123; 
  <span class="hljs-attribute">display</span>: flex; 
&#125;
<span class="hljs-selector-class">.el-page-header__left</span> &#123; 
  <span class="hljs-attribute">display</span>: flex; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>左侧标题区域<code>el-page-header__left</code>和右侧内容区域<code>el-page-header__content</code>的分隔符通过CSS样式实现，通过设置 左侧标题区域的 伪类 <code>::after</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.el-page-header__left</span><span class="hljs-selector-pseudo">::after</span> &#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">1px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">16px</span>;
  <span class="hljs-attribute">right</span>: -<span class="hljs-number">20px</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>; 
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">50%</span>);
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#dcdfe6</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件渲染效果如下 👇：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d94054934bb2408292b1ef83be0229c5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-7">0x02 组件样式</h1>
<h2 data-id="heading-8">src/page-header.scss</h2>
<p>组件样式源码 <code>packages\theme-chalk\src\page-header.scss</code> 使用混合指令 <code>b</code>、<code>e</code>  嵌套生成组件样式。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-comment">// 生成 .el-page-header</span>
<span class="hljs-keyword">@include</span> b(page-header) &#123;
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-comment">// 生成 .el-page-header__left</span>
  <span class="hljs-keyword">@include</span> e(left) &#123;
    <span class="hljs-comment">// ...</span>
    
    <span class="hljs-comment">// 生成 .el-page-header__left::after</span>
    &<span class="hljs-selector-pseudo">::after</span> &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
    
    <span class="hljs-comment">// 生成 .el-page-header__left .el-icon-back </span>
    <span class="hljs-selector-class">.el-icon-back</span> &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
    
    <span class="hljs-comment">// 生成 .el-page-header__title</span>
    <span class="hljs-keyword">@include</span> e(title) &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
  &#125;
  <span class="hljs-comment">// 生成 .el-page-header__content</span>
  <span class="hljs-keyword">@include</span> e(content) &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">lib/page-header.css</h2>
<p>前文可知使用 <code>gulpfile.js</code>编译 <code>scss</code> 文件转换为<code>CSS</code>,经过浏览器兼容、格式压缩，最后生成 <code>packages\theme-chalk\lib\page-header.scss</code>，内容格式如下。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.el-page-header</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-page-header__left</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-page-header__left</span><span class="hljs-selector-pseudo">::after</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-page-header__left</span> <span class="hljs-selector-class">.el-icon-back</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-page-header__title</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-page-header__content</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-10">0x03 📚参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23vm-emit" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#vm-emit" ref="nofollow noopener noreferrer">“vm-emit”，vuejs.org </a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2F%3A%3Aafter" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/::after" ref="nofollow noopener noreferrer">“伪类 ::after”，MDN</a></p>
<h1 data-id="heading-11">0x04 关注专栏</h1>
<p>此文章已收录到专栏中 👇，可以直接关注。</p></div>  
</div>
            