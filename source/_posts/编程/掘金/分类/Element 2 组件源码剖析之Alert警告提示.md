
---
title: 'Element 2 组件源码剖析之Alert警告提示'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31971bc1293d4e1194fdbb895e3ecb09~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:36:48 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31971bc1293d4e1194fdbb895e3ecb09~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h1 data-id="heading-0">0x00 简介</h1>
<p>组件 <code>Alert</code> 用于警告提示，展现需要关注的信息。本文将深入分析源码，剖析其实现原理，耐心读完，相信会对您有所帮助。组件源码实现详见<code>packages/alert/src/main.vue</code> 。 🔗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Falert" target="_blank" rel="nofollow noopener noreferrer" title="https://element.eleme.cn/#/zh-CN/component/alert" ref="nofollow noopener noreferrer">组件文档 Alert</a>  🔗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FElemeFE%2Felement%2Fblob%2Fdev%2Fpackages%2Falert%2Fsrc%2Fmain.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/ElemeFE/element/blob/dev/packages/alert/src/main.vue" ref="nofollow noopener noreferrer">gitee源码 main.vue </a></p>
<p>更多组件剖析详见 👉  <a href="https://juejin.cn/post/6994721241194037255" target="_blank" title="https://juejin.cn/post/6994721241194037255"><strong>📚 Element 2 源码剖析组件总览</strong></a> 。</p>
<hr>
<h1 data-id="heading-1">0x01  组件源码</h1>
<h2 data-id="heading-2">template 模板内容</h2>
<p>组件模板创建一个class名为<code>el-alert</code>的<code><div></code> 元素根节点 <code>1️⃣</code>，包含两个子节点 ：左侧的<code>Icon图标``2️⃣</code>、右侧的<code>文字内容区域</code> <code>3️⃣</code>。 组件使用内置 <code>transition</code> 实现<code>el-alert-fade</code> 淡入淡出效果。</p>
<p>组件DOM结构渲染如下 👇:
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31971bc1293d4e1194fdbb895e3ecb09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"el-alert-fade"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>
      <span class="hljs-attr">class</span>=<span class="hljs-string">"el-alert"</span>
      <span class="hljs-attr">:class</span>=<span class="hljs-string">"[typeClass, center ? 'is-center' : '', 'is-' + effect]"</span>
      <span class="hljs-attr">v-show</span>=<span class="hljs-string">"visible"</span>
      <span class="hljs-attr">role</span>=<span class="hljs-string">"alert"</span>
    ></span>
      <span class="hljs-comment"><!-- icon 图标 --></span>
      <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-alert__icon"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"[ iconClass, isBigIcon ]"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"showIcon"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
      <span class="hljs-comment"><!-- 文字内容 包含关闭按钮 --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-alert__content"</span>></span>
        <span class="hljs-comment"><!-- 标题 --></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-alert__title"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"[ isBoldTitle ]"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"title || $slots.title"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"title"</span>></span>&#123;&#123; title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-comment"><!-- 辅助性文字介绍 --></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-alert__description"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"$slots.default && !description"</span>></span><span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-alert__description"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"description && !$slots.default"</span>></span>&#123;&#123; description &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-comment"><!-- 关闭按钮 --></span>
        <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-alert__closebtn"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123; 'is-customed': closeText !== '', 
            'el-icon-close': closeText === '' &#125;"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"closable"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"close()"</span>></span>
          &#123;&#123;closeText&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">i</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1️⃣ 根节点</h3>
<ul>
<li>
<p>根据传入<em>prop</em>的属性值动态添加class。</p>
<ul>
<li>计算属性<code>typeClass</code> 根据 <code>type</code> 属性值生成不同类型样式 class ， <code>el-alert--[success/warning/info/error]</code>。</li>
<li>根据 <code>center</code> 属性值生成<code>is-center</code>，让图标文字水平居中。</li>
<li>根据 <code>effect</code> 属性值生成主题样式  <code>is-[light/dark]</code>。</li>
</ul>
</li>
<li>
<p><code>v-show="visible"</code> 使用 <em>Data Property</em> 的 <code>visible</code>属性控制组件显示隐藏。组件虽为页面中的非浮层元素不会自动消失，但支持手动关闭隐藏。</p>
</li>
<li>
<p><code>role="alert"</code> 表示当前元素的类型,用于 <code>ARIA</code> 无障碍访问设置。</p>
</li>
</ul>
<p>根节点元素内部使用flex布局。两个子节点交叉轴的中点对齐。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.el-alert</span> &#123; 
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-comment">/* 交叉轴的中点对齐 */</span>
    <span class="hljs-attribute">align-items</span>: center; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>is-center</code> 通过设定属性<code>justify-content </code> 定义了主轴上的对齐方式，实现两个子节点水平居中。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.is-center</span> &#123;
  <span class="hljs-attribute">justify-content</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2️⃣ Icon图标</h3>
<p>该节点是一个Icon 图标元素,表示某种状态时提升可读性，图标节点是否渲染可见根据 <code>showIcon</code>属性值决定 <code>v-if="showIcon"</code> 。</p>
<ul>
<li>静态样式 <code>el-alert__icon</code> 定义图标默认尺寸。</li>
<li>使用计算属性 <code>iconClass</code>  <code>isBigIcon</code> 动态添加样式。
<ul>
<li>计算属性<code>iconClass</code> 根据 <code>type</code> 属性值生成不同类型 icon  class ， <code>el-icon-[success/warning/info/error]</code>。</li>
<li>计算属性<code>isBigIcon</code> 根据 辅助性文字内容是否设置，生成图标大尺寸样式<code>is-big</code>。</li>
</ul>
</li>
</ul>
<p>Icon 不同大小尺寸效果 👇:
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ebdc46e2889462b836e1f18a259b417~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3️⃣ 文字内容区域</h3>
<p>该节点是一个class 名为<code>el-alert__content</code>的<code><div></code> 元素，内容包含三个节点：  <code>标题</code>  <code>4️⃣</code> 、 <code>辅助性文字</code> <code>5️⃣</code>、 <code>关闭按钮</code> <code>6️⃣</code> 。</p>
<p>文字内容区域 DOM 结构渲染如下 👇:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5add985891b244bc85ab05fc29f7642f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>标题</code>  、 <code>辅助性文字</code> 节点提供了具名插槽和匿名插槽，分发内容时需要指明 <code>slot#name</code>，否则内容都会分发给匿名插槽。</p>
</blockquote>
<h4 data-id="heading-6">4️⃣ 标题</h4>
<p>该节点是一个class 名为<code>el-alert__title</code>的<code><span></code> 元素,包裹着具名插槽 <code>title</code>。</p>
<p>只有在 <code>title</code>属性值是 <code>truthy</code> 或者向该插槽分发内容时，该节点才会被渲染。<code>title</code> 是插槽的<code>后备内容</code>。若两者都设置了（传入<code>title</code>值而且向该插槽提供内容），渲染展示内容为插槽分发内容。</p>
<p>使用计算属性 <code>isBoldTitle</code> 动态添加样式。 <code>isBoldTitle</code> 根据辅助性文字内容是否设置，生成样式<code>is-big</code> 加粗title字体,用于区分与辅助性文字的主次。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.is-bold</span> &#123;
  <span class="hljs-attribute">font-weight</span>: <span class="hljs-number">700</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">5️⃣ 辅助性文字</h4>
<p>该节点是一个class 名为<code>el-alert__description</code>的<code><p></code>段落元素。该节点提供了匿名插槽或 <code>description</code>属性值，但是两者只能同时设置一项，才能正常显示。</p>
<p>当然可以改成如下逻辑，默认显示<code>description</code>属性值，插槽分发内容后优先显示后者。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-alert__description"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"description || $slots.default"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span>></span> &#123;&#123; description &#125;&#125; <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>基于很多组件的逻辑实现： prop属性大多作为插槽的后备内容， 暂时还不知为啥提供这么对立条件，有他无我！</p>
</blockquote>
<h4 data-id="heading-8">6️⃣ 关闭按钮</h4>
<p>节点默认是一个名为<code>el-icon-close</code>的Icon 图标,提供<code>close</code>事件来设置关闭时的回调。通过 <code>closable</code>属性决定是否可关闭。</p>
<p>若设置<code>closeText</code>属性值自定义关闭按钮，此时节点为包裹文本的 <code><i></code>元素。</p>
<p>关闭按钮位置偏移至右上角，样式<code>el-alert__closebtn</code>定义如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.el-alert__closebtn</span> &#123; 
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">12px</span>;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">15px</span>; 
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">attributes 属性</h2>
<p>组件定义了8个prop 。</p>




































































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>可选值</th><th>默认值</th></tr></thead><tbody><tr><td>title</td><td>标题</td><td>string</td><td>—</td><td>—</td></tr><tr><td>type</td><td>类型</td><td>string</td><td>success/warning/info/error</td><td>info</td></tr><tr><td>description</td><td>辅助性文字</td><td>string</td><td>—</td><td>—</td></tr><tr><td>closable</td><td>是否可关闭</td><td>boolean</td><td>—</td><td>true</td></tr><tr><td>center</td><td>文字是否居中</td><td>boolean</td><td>—</td><td>true</td></tr><tr><td>close-text</td><td>关闭按钮自定义文本</td><td>string</td><td>—</td><td>—</td></tr><tr><td>show-icon</td><td>是否显示图标</td><td>boolean</td><td>—</td><td>false</td></tr><tr><td>effect</td><td>选择提供的主题</td><td>string</td><td>light/dark</td><td>light</td></tr></tbody></table>
<p><code>effect</code> 提供了自定义验证函数,提供了默认值<code>light</code>。 若传入<code>effect</code>值不是以下<code>light/dark</code>其中之一，会生成无效的样式<code>is-[effect]</code>，导致组件样式无法正常加载。</p>
<pre><code class="hljs language-js copyable" lang="js">props: &#123; 
  <span class="hljs-attr">effect</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-string">'light'</span>,
    <span class="hljs-attr">validator</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
      <span class="hljs-keyword">return</span> [<span class="hljs-string">'light'</span>, <span class="hljs-string">'dark'</span>].indexOf(value) !== -<span class="hljs-number">1</span>;
    &#125;
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">计算属性</h2>
<h3 data-id="heading-11">typeClass</h3>
<p>根据 <code>type</code> 属性值生成不同类型主题样式（背景颜色、文字颜色）  <code>el-alert-[success/warning/info/error]</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123;
  <span class="hljs-function"><span class="hljs-title">typeClass</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`el-alert--<span class="hljs-subst">$&#123; <span class="hljs-built_in">this</span>.type &#125;</span>`</span>;
  &#125;, 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">iconClass</h3>
<p>计算属性<code>iconClass</code> 根据 <code>type</code> 属性值生成不同类型 icon  class  <code>el-icon-[success/warning/info/error]</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> TYPE_CLASSES_MAP = &#123;
  <span class="hljs-string">'success'</span>: <span class="hljs-string">'el-icon-success'</span>,
  <span class="hljs-string">'warning'</span>: <span class="hljs-string">'el-icon-warning'</span>,
  <span class="hljs-string">'error'</span>: <span class="hljs-string">'el-icon-error'</span>
&#125;;

computed: &#123; 
  <span class="hljs-function"><span class="hljs-title">iconClass</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> TYPE_CLASSES_MAP[<span class="hljs-built_in">this</span>.type] || <span class="hljs-string">'el-icon-info'</span>;
  &#125;, 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若传入<code>type</code>值不是以下<code>success/warning/error</code>其中之一，都会生成<code>el-icon-info</code>，所以<code>type</code>默认值等于<code>info</code>。</p>
<h3 data-id="heading-13">isBigIcon</h3>
<p>根据辅助性文字内容是否设置，只有在 <code>title</code>属性值是 <code>truthy</code> 或者向该插槽分发内容时，生成样式<code>is-big</code> 加粗title字体,用于区分与辅助性文字的主次。</p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123; 
  <span class="hljs-function"><span class="hljs-title">isBigIcon</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.description || <span class="hljs-built_in">this</span>.$slots.default ? <span class="hljs-string">'is-big'</span> : <span class="hljs-string">''</span>;
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Icon 根据组件内容多少（高度也会调整），动态调整尺寸展示更加协调 👇:
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ebdc46e2889462b836e1f18a259b417~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">isBoldTitle</h3>
<p>根据辅助性文字内容是否设置，只有在 <code>title</code>属性值是 <code>truthy</code> 或者向该插槽分发内容时，生成图标大尺寸样式<code>is-big</code></p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123; 
  <span class="hljs-function"><span class="hljs-title">isBoldTitle</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.description || <span class="hljs-built_in">this</span>.$slots.default ? <span class="hljs-string">'is-bold'</span> : <span class="hljs-string">''</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-15">0x02 组件样式</h1>
<h2 data-id="heading-16">src/alert.scss</h2>
<p>组件样式源码 <code>packages\theme-chalk\src\alert.scss</code> 使用混合指令 <code>b</code>、<code>e</code> 、<code>m</code>、<code>when</code> 嵌套生成组件样式。</p>
<pre><code class="hljs language-scss copyable" lang="scss">
<span class="hljs-comment">//  .el-alert</span>
<span class="hljs-keyword">@include</span> b(alert) &#123;
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-keyword">@include</span> when(light) &#123;
    <span class="hljs-comment">//  .el-alert.is-light .el-alert__closebtn</span>
    <span class="hljs-selector-class">.el-alert__closebtn</span> &#123; <span class="hljs-comment">/* ... */</span> &#125;
  &#125;

  <span class="hljs-keyword">@include</span> when(dark) &#123;
    <span class="hljs-comment">//  .el-alert.is-dark .el-alert__closebtn</span>
    <span class="hljs-selector-class">.el-alert__closebtn</span> &#123; <span class="hljs-comment">/* ... */</span> &#125;
    
    <span class="hljs-comment">//  .el-alert.is-dark .el-alert__description</span>
    <span class="hljs-selector-class">.el-alert__description</span> &#123; <span class="hljs-comment">/* ... */</span> &#125;
  &#125;
  
  <span class="hljs-comment">//  .el-alert.is-center</span>
  <span class="hljs-keyword">@include</span> when(center) &#123; <span class="hljs-comment">/* ... */</span> &#125;

  <span class="hljs-comment">// success  warning  error 格式类似</span>
  <span class="hljs-keyword">@include</span> m(success) &#123;
  
    <span class="hljs-comment">// .el-alert--success.is-light</span>
    &<span class="hljs-selector-class">.is-light</span> &#123;
      <span class="hljs-comment">// ...</span>
      
      <span class="hljs-comment">//.el-alert--success.is-light .el-alert__description</span>
      <span class="hljs-selector-class">.el-alert__description</span> &#123; <span class="hljs-comment">/* ... */</span> &#125;
    &#125;
    <span class="hljs-comment">// .el-alert--success.is-dark</span>
    &<span class="hljs-selector-class">.is-dark</span> &#123; <span class="hljs-comment">/* ... */</span> &#125;
  &#125;
  
  <span class="hljs-comment">// info</span>
  <span class="hljs-keyword">@include</span> m(info) &#123;
    <span class="hljs-comment">//.el-alert--info.is-light</span>
    &<span class="hljs-selector-class">.is-light</span> &#123; <span class="hljs-comment">/* ... */</span> &#125;
    
    <span class="hljs-comment">// .el-alert--info.is-dark</span>
    &<span class="hljs-selector-class">.is-dark</span> &#123; <span class="hljs-comment">/* ... */</span> &#125;
    
    <span class="hljs-comment">// .el-alert--info .el-alert__description</span>
    <span class="hljs-selector-class">.el-alert__description</span> &#123; <span class="hljs-comment">/* ... */</span> &#125;
  &#125;
 

  <span class="hljs-comment">// .el-alert__content</span>
  <span class="hljs-keyword">@include</span> e(content)  &#123; <span class="hljs-comment">/* ... */</span> &#125;
  
  <span class="hljs-comment">// .el-alert__icon</span>
  <span class="hljs-keyword">@include</span> e(icon) &#123;
    <span class="hljs-comment">// ...</span>
   
    <span class="hljs-comment">// .el-alert__icon.is-big</span>
    <span class="hljs-keyword">@include</span> when(big)  &#123; <span class="hljs-comment">/* ... */</span> &#125;
  &#125;
  <span class="hljs-comment">// .el-alert__title</span>
  <span class="hljs-keyword">@include</span> e(title) &#123;
    <span class="hljs-comment">// ...</span>
    
    <span class="hljs-comment">// .el-alert__title.is-bold</span>
    <span class="hljs-keyword">@include</span> when(bold)  &#123; <span class="hljs-comment">/* ... */</span> &#125;
  &#125;
  
  <span class="hljs-comment">// .el-alert .el-alert__description</span>
  & <span class="hljs-selector-class">.el-alert__description</span>  &#123; <span class="hljs-comment">/* ... */</span> &#125;
  
  <span class="hljs-comment">// .el-alert__closebtn</span>
  <span class="hljs-keyword">@include</span> e(closebtn) &#123;
    <span class="hljs-comment">// ...</span>
    
    <span class="hljs-comment">// .el-alert__closebtn.is-customed</span>
    <span class="hljs-keyword">@include</span> when(customed)  &#123; <span class="hljs-comment">/* ... */</span> &#125;
  &#125;
&#125;

<span class="hljs-selector-class">.el-alert-fade-enter</span>, <span class="hljs-selector-class">.el-alert-fade-leave-active</span>  &#123; <span class="hljs-comment">/* ... */</span> &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">lib/alert.css</h2>
<p>前文可知使用 <code>gulpfile.js</code>编译 <code>scss</code> 文件转换为<code>CSS</code>,经过浏览器兼容、格式压缩，最后生成 <code>packages\theme-chalk\lib\alert.scss</code>，内容格式如下。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.el-alert</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert</span><span class="hljs-selector-class">.is-light</span> <span class="hljs-selector-class">.el-alert__closebtn</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert</span><span class="hljs-selector-class">.is-dark</span> <span class="hljs-selector-class">.el-alert__closebtn</span>,
<span class="hljs-selector-class">.el-alert</span><span class="hljs-selector-class">.is-dark</span> <span class="hljs-selector-class">.el-alert__description</span>  &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert</span><span class="hljs-selector-class">.is-center</span>  &#123; <span class="hljs-comment">/* ...  */</span> &#125; 

<span class="hljs-comment">/* ...success...  */</span> 
<span class="hljs-selector-class">.el-alert--success</span><span class="hljs-selector-class">.is-light</span>  &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert--success</span><span class="hljs-selector-class">.is-light</span> <span class="hljs-selector-class">.el-alert__description</span>  &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert--success</span><span class="hljs-selector-class">.is-dark</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-comment">/* ...warning...  */</span> 
<span class="hljs-comment">/* ...error...  */</span>  
<span class="hljs-comment">/* ...info...  */</span>  
<span class="hljs-selector-class">.el-alert--info</span><span class="hljs-selector-class">.is-light</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert--info</span><span class="hljs-selector-class">.is-dark</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert--info</span> <span class="hljs-selector-class">.el-alert__description</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 

<span class="hljs-selector-class">.el-alert__content</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert__icon</span>  &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert__icon</span><span class="hljs-selector-class">.is-big</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert__title</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert__title</span><span class="hljs-selector-class">.is-bold</span>  &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert</span> <span class="hljs-selector-class">.el-alert__description</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert__closebtn</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert__closebtn</span><span class="hljs-selector-class">.is-customed</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125; 
<span class="hljs-selector-class">.el-alert-fade-enter</span>, <span class="hljs-selector-class">.el-alert-fade-leave-active</span> &#123; <span class="hljs-comment">/* ...  */</span> &#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-18">0x03 📚参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAccessibility%2FARIA" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/Accessibility/ARIA" ref="nofollow noopener noreferrer">"ARIA",MDN</a></p>
<h1 data-id="heading-19">0x04 关注专栏</h1>
<p>此文章已收录到专栏中 👇，可以直接关注。</p></div>  
</div>
            