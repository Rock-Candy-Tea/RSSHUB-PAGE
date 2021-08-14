
---
title: 'Element 2 组件源码剖析之Result结果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d6cd431061d400cb54547a6b2a2be6e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 06:55:59 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d6cd431061d400cb54547a6b2a2be6e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">0x00 简介</h1>
<p>组件 <code>Result</code> 用于对用户的操作结果或者异常状态做反馈。 本文将深入分析源码，剖析其实现原理，耐心读完，相信会对您有所帮助。组件源码实现详见<code>packages/result/src/</code> 文件夹下包含多个文件 <code>index.vue</code>、<code>icon-info.vue</code>、<code>icon-success.vue</code>、<code>icon-warning.vue</code>、<code>icon-error.vue</code>。 🔗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Fresult" target="_blank" rel="nofollow noopener noreferrer" title="https://element.eleme.cn/#/zh-CN/component/result" ref="nofollow noopener noreferrer">组件文档 Result</a>  🔗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub1s.com%2FElemeFE%2Felement%2Fblob%2Fdev%2Fpackages%2Fresult%2Fsrc%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github1s.com/ElemeFE/element/blob/dev/packages/result/src/" ref="nofollow noopener noreferrer">github源码 </a></p>
<p>更多组件剖析详见 👉  <a href="https://juejin.cn/post/6994721241194037255" target="_blank" title="https://juejin.cn/post/6994721241194037255"><strong>📚 Element 2 源码剖析组件总览</strong></a> 。</p>
<hr>
<h1 data-id="heading-1">0x01 svg 图标组件</h1>
<p>图标通过封装一个 <code><svg></code>元素，定义 <code>viewBox</code>属性，通过 <code><path></code> 元素是用来定义形状。</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 48 48"</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
      <span class="hljs-comment"><!--  创建图形形状元素 --></span>
      <span class="hljs-tag"><<span class="hljs-name">path</span>   <span class="hljs-attr">...</span>  /></span> 
  <span class="hljs-tag"></<span class="hljs-name">svg</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>封装 <code>icon-info.vue</code>、<code>icon-success.vue</code>、<code>icon-warning.vue</code>、<code>icon-error.vue</code> 等单独组件实现不同类型的<code>svg</code>图标。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d6cd431061d400cb54547a6b2a2be6e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图标颜色需要通过添加自定义的 class 样式修改。</p>
<h1 data-id="heading-2">0x02 组件源码</h1>
<h2 data-id="heading-3">template 模板内容</h2>
<p>模板创建一个 <code><div></code> 元素根节点，class 名为<code>el-result</code>，包含 4 个子节点 <code>自定义图标</code>、<code>自定义标题</code>、<code>自定义二级标题</code>、<code>自定义底部额外区域</code>。</p>
<p>每个节点都提供了各自具名<code>slot</code>, 在向具名插槽提供内容的时候需要指明 <code>slot#name</code>，否则内容无法正确分发，将被丢弃（未提供匿名插槽）。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-result"</span>></span>
    <span class="hljs-comment"><!-- 自定义图标 slot icon --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-result__icon"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"icon"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"iconElement"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"iconElement"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 自定义标题 slot title --></span> 
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"title || $slots.title"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-result__title"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"title"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 自定义二级标题 slot subTitle --></span> 
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"subTitle || $slots.subTitle"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-result__subtitle"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"subTitle"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; subTitle &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 自定义底部额外区域 slot extra --></span> 
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"$slots.extra"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-result__extra"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"extra"</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">自定义图标</h3>
<p>该节点是一个class 名为<code>el-result__icon</code>的<code><div></code> 元素包，裹着名为<code>icon</code>的具名<code>slot</code>。</p>
<p>插槽提供了后备内容，动态引用svg 图标组件。具体详见下文章节 <strong>动态组件</strong> 。</p>
<h3 data-id="heading-5">自定义标题</h3>
<p>该节点是一个class 名为<code>el-result__title</code>的<code><div></code> 元素包，裹着名为<code>title</code>的具名<code>slot</code>。</p>
<p>只有在 <code>title</code> 是 <code>truthy</code> 或者向该插槽提供内容时，该节点才会被渲染。若两者都设置了（传入<code>title</code>值而且向该插槽提供内容），展示内容为插槽分发内容优先级较高。因为 <code>title</code> 是做为插槽的<code>后备内容</code>。</p>
<blockquote>
<p><strong>truthy</strong>（真值）指的是在<strong>布尔值</strong>上下文中，转换后的值为真的值。所有值都是真值，除非它们被定义为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FGlossary%2FFalsy" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Glossary/Falsy" ref="nofollow noopener noreferrer">假值</a>（即除 <code>false</code>、<code>0</code>、<code>""</code>、<code>null</code>、<code>undefined</code> 和 <code>NaN</code> 以外皆为真值）</p>
</blockquote>
<h3 data-id="heading-6">自定义二级标题</h3>
<p>该节点是一个class 名为<code>el-result__subtitle</code>的<code><div></code> 元素包，裹着名为<code>title</code>的具名<code>subTitle</code>。</p>
<p>只有在 <code>subTitle</code> 是 <code>truthy</code> 或者向该插槽提供内容时，该节点才会被渲染。若两者都设置了（传入<code>subTitle</code>值而且向该插槽提供内容），展示内容为插槽分发内容优先级较高。因为 <code>subTitle</code> 是做为插槽的<code>后备内容</code>。</p>
<h3 data-id="heading-7">自定义底部额外区域</h3>
<p>该节点是一个class 名为<code>el-result__extra</code>的<code><div></code> 元素包，裹着名为<code>extra</code>的具名<code>slot</code>。只有向该插槽提供内容时<code> v-if="$slots.extra"</code>，该节点才会被渲染。</p>
<h2 data-id="heading-8">动态组件</h2>
<p>上文名为<code>icon</code>的具名<code>slot</code>的 <code>后备内容</code>使用了<code>动态组件</code> ,根据传入不同的图标类型<code>icon</code>，动态引入对应类型svg图标组件。</p>
<p>通过 Vue 的 <code><component></code> 元素加一个特殊的 <code>is</code> attribute 来实现在不同组件之间进行动态切换。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"iconElement"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"iconElement"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>svg 组件引入注册。</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">import</span> IconSuccess <span class="hljs-keyword">from</span> <span class="hljs-string">'./icon-success.vue'</span>;
<span class="hljs-keyword">import</span> IconError <span class="hljs-keyword">from</span> <span class="hljs-string">'./icon-error.vue'</span>;
<span class="hljs-keyword">import</span> IconWarning <span class="hljs-keyword">from</span> <span class="hljs-string">'./icon-warning.vue'</span>;
<span class="hljs-keyword">import</span> IconInfo <span class="hljs-keyword">from</span> <span class="hljs-string">'./icon-info.vue'</span>; 


<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
  <span class="hljs-attr">components</span>: &#123;
    [IconSuccess.name]: IconSuccess,
    [IconError.name]: IconError,
    [IconWarning.name]: IconWarning,
    [IconInfo.name]: IconInfo
  &#125;, 
&#125;;
</script> 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">计算属性</h3>
<p>计算属性 <code>iconElement</code>根据传入<code>icon</code>值动态生成 图标名称。用于组件引用和class添加。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> IconMap = &#123;
  <span class="hljs-attr">success</span>: <span class="hljs-string">'icon-success'</span>,
  <span class="hljs-attr">warning</span>: <span class="hljs-string">'icon-warning'</span>,
  <span class="hljs-attr">error</span>: <span class="hljs-string">'icon-error'</span>,
  <span class="hljs-attr">info</span>: <span class="hljs-string">'icon-info'</span>
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">iconElement</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> icon = <span class="hljs-built_in">this</span>.icon;
      <span class="hljs-keyword">return</span> icon && IconMap[icon] ? IconMap[icon] : <span class="hljs-string">'icon-info'</span>;
    &#125;
  &#125;
&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据 <code>IconMap</code> 定义，若传入的<code>icon</code>值不是<code>success / warning / info / error</code>其中一个，返回默认值<code>icon-info</code> 等同于 <code>icon</code>值为 <code>info</code>。</p>
<p><code>iconElement</code>值范围为  <code>icon-success</code>, <code>icon-warning</code>, <code>icon-error</code>, <code>icon-info</code>。</p>
<h3 data-id="heading-10">svg 样式</h3>
<p><code>iconElement</code>值  <code>icon-success</code>、 <code>icon-warning</code>、 <code>icon-error</code>、 <code>icon-info</code> 会用于svg图标颜色的自定义。不同类型的class定义了不同的颜色，效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5191e54899c24edf915f35a2b506d572~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">attributes 属性</h2>
<p>组件定义了3 个prop : <code>title</code> 、<code>subTitle</code> 、<code>icon</code> 。</p>
<pre><code class="hljs language-js copyable" lang="js">  props: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">subTitle</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">icon</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'info'</span>
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">title</h3>
<p>设置标题内容,默认值为 <code>''</code>。 具体功能详见上文章节  <strong>自定义标题</strong> 。</p>
<h3 data-id="heading-13">subTitle</h3>
<p>设置二级标题内容,默认值为 <code>''</code>。 具体功能详见上文章节 <strong>自定义二级标题</strong> 。</p>
<h3 data-id="heading-14">icon</h3>
<p>图标类型设置,用于引入指定类型的svg图标、设置图标颜色。 具体功能详见上文章节 <strong>计算属性</strong> 。</p>
<hr>
<h1 data-id="heading-15">0x03 组件样式</h1>
<h2 data-id="heading-16">src/result.scss</h2>
<p>组件样式源码 <code>packages\theme-chalk\src\result.scss</code> 使用混合指令 <code>b</code>、<code>e</code>  嵌套生成组件样式。</p>
<pre><code class="hljs language-scss copyable" lang="scss"> 
<span class="hljs-comment">// 生成 .el-result</span>
<span class="hljs-keyword">@include</span> b(result) &#123;
  <span class="hljs-comment">// ... </span>
  
  <span class="hljs-comment">// 生成 .el-result__icon svg</span>
  <span class="hljs-keyword">@include</span> e(icon) &#123;
    svg &#123;
      <span class="hljs-comment">// ... </span>
    &#125;
  &#125;
  
  <span class="hljs-comment">// 生成 .el-result__title</span>
  <span class="hljs-keyword">@include</span> e(title) &#123;
    <span class="hljs-comment">// ...  </span>
    
    <span class="hljs-comment">// 生成 .el-result__title  p</span>
    <span class="hljs-selector-tag">p</span> &#123;
      <span class="hljs-comment">// ... </span>
    &#125;
  &#125;
  
  <span class="hljs-comment">// 生成 .el-result__subtitle</span>
  <span class="hljs-keyword">@include</span> e(subtitle) &#123;
    <span class="hljs-comment">// ... </span>
    
    <span class="hljs-comment">// 生成 .el-result__subtitle  p</span>
    <span class="hljs-selector-tag">p</span> &#123;
      <span class="hljs-comment">// ... </span>
    &#125;
  &#125;
  
  <span class="hljs-comment">// 生成 .el-result__extra</span>
  <span class="hljs-keyword">@include</span> e(extra) &#123;
    <span class="hljs-comment">// ... </span>
  &#125;
  
  <span class="hljs-comment">// 生成 .el-result .icon-success</span>
  <span class="hljs-selector-class">.icon-success</span> &#123;
    <span class="hljs-comment">// ... </span>
  &#125;
  
  <span class="hljs-comment">// 生成 .el-result .icon-error</span>
  <span class="hljs-selector-class">.icon-error</span> &#123;
    <span class="hljs-comment">// ... </span>
  &#125;
  
  <span class="hljs-comment">// 生成 .el-result .icon-info</span>
  <span class="hljs-selector-class">.icon-info</span> &#123;
    <span class="hljs-comment">// ... </span>
  &#125;
  
  <span class="hljs-comment">// 生成 .el-result .icon-warning</span>
  <span class="hljs-selector-class">.icon-warning</span> &#123;
    <span class="hljs-comment">// ... </span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">lib/result.scss</h2>
<p>前文可知使用 <code>gulpfile.js</code>编译 <code>scss</code> 文件转换为<code>CSS</code>,经过浏览器兼容、格式压缩，最后生成 <code>packages\theme-chalk\lib\result.scss</code>，内容格式如下。</p>
<pre><code class="hljs language-css copyable" lang="css">
<span class="hljs-selector-class">.el-result</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result__icon</span> svg &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result__title</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result__title</span> <span class="hljs-selector-tag">p</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result__subtitle</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result__subtitle</span> <span class="hljs-selector-tag">p</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result__extra</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result</span> <span class="hljs-selector-class">.icon-success</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result</span> <span class="hljs-selector-class">.icon-error</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result</span> <span class="hljs-selector-class">.icon-info</span> &#123;
    // ... 
&#125;

<span class="hljs-selector-class">.el-result</span> <span class="hljs-selector-class">.icon-warning</span> &#123;
    // ... 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-18">0x04 📚参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents.html%23%25E5%258A%25A8%25E6%2580%2581%25E7%25BB%2584%25E4%25BB%25B6" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components.html#%E5%8A%A8%E6%80%81%E7%BB%84%E4%BB%B6" ref="nofollow noopener noreferrer">"动态组件",vuejs.org</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FSVG%2FAttribute%2FviewBox" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute/viewBox" ref="nofollow noopener noreferrer">"viewBox",MDN</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FGlossary%2FTruthy" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Glossary/Truthy" ref="nofollow noopener noreferrer">"Truthy",MDN</a></p>
<h1 data-id="heading-19">0x05 关注专栏</h1>
<p>此文章已收录到专栏中 👇，可以直接关注。</p></div>  
</div>
            