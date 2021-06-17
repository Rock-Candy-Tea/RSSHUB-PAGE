
---
title: 'Vue 之 More in js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf4525d6c011462690298fa5464d02a1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 23:01:01 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf4525d6c011462690298fa5464d02a1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>More in js，纵享丝滑开发体验！</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在说 <code>More in js</code> 之前，想必大家对 <code>React</code> 的 <code>All in js</code> 都不陌生，各位看官莫被干扰，本文与 <code>React</code> 无关。<code>More in js</code> 为笔者开发过程中的一些实例尝试，可能大家都有过类似的开发经历，但少有人思考这么做的价值。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf4525d6c011462690298fa5464d02a1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">SFC 组件结构</h2>
<p>讲到 Vue 的 SFC 组件结构，大家首先想到的一定是 <code>template</code> <code>script</code> <code>style</code> 三部曲。实际表现形式如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    ...
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span>
    ...
<span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>
    ...
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码就是 <code>Vue</code> 的 <code>SFC</code> 基础结构了，那这跟我们的 <code>More in js</code> 又有啥关系呢？</p>
<h2 data-id="heading-2">SFC 常见问题</h2>
<p>我们通常在业务组件开发时，避免不了出现复杂布局情况，组件嵌套（一层又一层，层层不一样），此时再加上业务逻辑的处理，代码行数轻轻松松破 <code>1000+</code>。</p>
<p>那么在维护或开发此类代码时，可能就是为了加一个属性导致我们在 <code>template</code> 和 <code>script</code> 之间反复横跳，开发体验较差，也带来了额外的时间成本。（此时某位暴躁老哥已经开始砸键盘了！）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02182816d5ab4f52bd743eb439a37090~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是笔者开发中的一个画布组件，其代码行数不算样式部分也突破了 <code>2000+</code>，对于正在修改业务逻辑的我突然需要给视图组件加个属性，直接促使肾上腺素飙升！</p>
<h2 data-id="heading-3">灵感来源</h2>
<p>对于上述问题的解决方案是在业务组件封装时产生的灵感。</p>
<p>通常 <code>UI</code> 组件库的基础组件并不能满足我们复杂的业务需求时，会对齐进行二次封装，那么对于源组件的 <code>props</code> 和 <code>events</code> 我们也是需要暴露给外界来降低上手成本，只针对该处的场景提供便利性，纵享丝滑体验。</p>
<p>例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"async-button"</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"main"</span>
    <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"mergeProps"</span>
    <span class="hljs-attr">:loading</span>=<span class="hljs-string">"loading"</span>
    @<span class="hljs-attr">click.prevent</span>=<span class="hljs-string">"onClick"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; omit, merge &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'AsyncButton'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">/**
     * 使用原始 Button 事件
     * <span class="hljs-doctag">@default <span class="hljs-variable">false</span></span>
     */</span>
    <span class="hljs-attr">useRaw</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>, <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span> &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">mergeProps</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> defaultProps = &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'primary'</span> &#125;
      <span class="hljs-keyword">return</span> omit(merge(defaultProps, <span class="hljs-built_in">this</span>.$attrs), <span class="hljs-string">'loading'</span>)
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">/**
     * 处理点击事件。
     */</span>
    <span class="hljs-function"><span class="hljs-title">onClick</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-comment">// useRaw: true 使用原始单击事件，false 使用异步单击事件</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.useRaw) &#123;
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'click'</span>, e)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> (<span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">false</span>), e)
      &#125;
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码是对 <code>Button</code> 组件做的一层简单封装，让使用者能够在点击时自动启动加载状态，在需要时通过回调函数来关闭加载状态。</p>
<p>对于源 <code>Button</code> 组件的 <code>props</code> 通过 <code>Vue</code> 提供的 <code>v-bind</code> 和 <code>$attrs</code> 实现属性穿透，那么反过来我们思考下是否可以把该方式应用到业务组件开发中？</p>
<p>答案是可以的。</p>
<h2 data-id="heading-4">More in js</h2>
<p>提出的 <code>More in js</code> 概念就是为了让 <code>Vue</code> 开发者能够更好地专注于业务逻辑部分的处理，配合 <code>IDE</code> 的定义跳转功能，可以相对的优化上述问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">SpecialTabs</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"data-point-tabs"</span> <span class="hljs-attr">left-label</span>=<span class="hljs-string">"上传文件"</span> <span class="hljs-attr">right-label</span>=<span class="hljs-string">"已上传的文件列表"</span>></span>
    <span class="hljs-comment"><!-- upload start --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"left"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">SingleUpload</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"singleUpload"</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"singleUpload"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-comment"><!-- upload end --></span>
    
    <span class="hljs-comment"><!-- table start --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"right"</span>></span>
      <span class="hljs-comment"><!-- table --></span>
      <span class="hljs-tag"><<span class="hljs-name">Table</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"file-table"</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"table"</span> @<span class="hljs-attr">hook:created</span>=<span class="hljs-string">"loadTableData"</span> /></span>

      <span class="hljs-comment"><!-- modal start --></span>
      <span class="hljs-tag"><<span class="hljs-name">Modal</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"modal"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"modal.show"</span> <span class="hljs-attr">transfer</span>></span>
        <span class="hljs-comment"><!-- modal footer --></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"toggleModal(false)"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"confirmBtn"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitForm"</span>></span>确定<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>

        <span class="hljs-comment"><!-- edit form --></span>
        <span class="hljs-tag"><<span class="hljs-name">EditForm</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">"editFormRef"</span>
          <span class="hljs-attr">:key</span>=<span class="hljs-string">"`edit-form_$&#123;updateFormFlag&#125;`"</span>
          <span class="hljs-attr">:info</span>=<span class="hljs-string">"table.singleSelected"</span>
          @<span class="hljs-attr">on-validated</span>=<span class="hljs-string">"handleValidated"</span>
          @<span class="hljs-attr">on-submitted</span>=<span class="hljs-string">"handleSubmitted"</span>
        ></span><span class="hljs-tag"></<span class="hljs-name">PointForm</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Modal</span>></span>
      <span class="hljs-comment"><!-- modal end --></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-comment"><!-- table end --></span>
  <span class="hljs-tag"></<span class="hljs-name">SpecialTabs</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> SpecialTabs <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/SpecialTabs'</span>
<span class="hljs-keyword">import</span> SingleUpload <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/SingleUpload'</span>
<span class="hljs-keyword">import</span> &#123; dataPointColumns &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./entity/data-point'</span>
<span class="hljs-keyword">import</span> DeleteMixin <span class="hljs-keyword">from</span> <span class="hljs-string">'@/mixins/delete'</span>
<span class="hljs-keyword">import</span> EditForm <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/edit-form.vue'</span>
<span class="hljs-keyword">import</span> &#123; showErrorMessage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/util/error'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'DataPoint'</span>,
  <span class="hljs-attr">mixins</span>: [DeleteMixin],
  <span class="hljs-attr">components</span>: &#123; SpecialTabs, SingleUpload, EditForm &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">singleUpload</span>: &#123;
        <span class="hljs-attr">autoUpload</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">uploadRequest</span>: <span class="hljs-built_in">this</span>.uploadRequest,
        <span class="hljs-attr">beforeUpload</span>: <span class="hljs-built_in">this</span>.handleBeforeUpload
      &#125;,
      <span class="hljs-attr">table</span>: &#123;
        <span class="hljs-attr">border</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">disabledHover</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">columns</span>: dataPointColumns.call(<span class="hljs-built_in">this</span>),
        <span class="hljs-attr">data</span>: [],
        <span class="hljs-attr">singleSelected</span>: &#123;&#125;,
        <span class="hljs-attr">actionOptions</span>: [...]
      &#125;,
      <span class="hljs-attr">modal</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'配置表单'</span>,
        <span class="hljs-attr">maskClosable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">show</span>: <span class="hljs-literal">false</span>
      &#125;,
      <span class="hljs-attr">confirmBtn</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'primary'</span>,
        <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>
      &#125;,
      <span class="hljs-attr">updateFormFlag</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-comment">/**
     * DeleteMixin
     */</span>
    <span class="hljs-function"><span class="hljs-title">deleteOption</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">deleteUrl</span>: <span class="hljs-string">'/db_table/delete'</span>,
        <span class="hljs-attr">method</span>: <span class="hljs-string">'delete'</span>,
        <span class="hljs-attr">loading</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">params</span>: <span class="hljs-function">(<span class="hljs-params">selection</span>) =></span> (&#123; <span class="hljs-attr">table_name</span>: selection[<span class="hljs-number">0</span>].table_name &#125;),
        <span class="hljs-attr">afterDelete</span>: <span class="hljs-function">(<span class="hljs-params">flag</span>) =></span> flag && <span class="hljs-built_in">this</span>.loadTableData()
      &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    ...
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码是对 <code>More in js</code> 的一次尝试，组件的属性对象显示声明在 <code>data</code> 中，通过 <code>v-bind</code> 来动态绑定到模板上，能够提升代码的阅读性，让开发者更加专注业务逻辑层，对于视图层只关注在布局即可。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d370e4c2e10f4bfe896cdc203479ba11~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>配合 <code>IDE</code> 的定义跳转功能，能够轻松实现对视图层组件的属性控制及添加，减少代码横跳次数，提升开发效率。</p>
<h2 data-id="heading-5">Vue3 更优体验</h2>
<p>在 <code>Vue2</code> 中由于 <code>options api</code> 的结构，我们的组件开发通常在单文件中，不会对内部业务逻辑过于聚合，所以 <code>More in js</code> 方式只会解决单文件内部的代码横跳问题。</p>
<p>但是在 <code>Vue3</code> 的 <code>hooks api</code> 中，我们可以通过抽离业务逻辑到 <code>@use/xxx</code> 后，让视图层与逻辑层的代码高度聚合，使用 <code>More in js</code> 可以更好的维护组件状态，不需要频繁的切换文件来更新属性信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// dp.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">SpecialTabs</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"data-point-tabs"</span> <span class="hljs-attr">left-label</span>=<span class="hljs-string">"上传文件"</span> <span class="hljs-attr">right-label</span>=<span class="hljs-string">"已上传的文件列表"</span>></span>
    <span class="hljs-comment"><!-- upload start --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"left"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">SingleUpload</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"singleUploadRef"</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"singleUploadAttrs"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-comment"><!-- upload end --></span>
    
    <span class="hljs-comment"><!-- table start --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"right"</span>></span>
      <span class="hljs-comment"><!-- table --></span>
      <span class="hljs-tag"><<span class="hljs-name">Table</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"file-table"</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"tableAttrs"</span> @<span class="hljs-attr">hook:created</span>=<span class="hljs-string">"loadTableData"</span> /></span>

      <span class="hljs-comment"><!-- modal start --></span>
      <span class="hljs-tag"><<span class="hljs-name">Modal</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"modal"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"modal.show"</span> <span class="hljs-attr">transfer</span>></span>
        <span class="hljs-comment"><!-- modal footer --></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"toggleModal(false)"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"confirmBtn"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitForm"</span>></span>确定<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>

        <span class="hljs-comment"><!-- edit form --></span>
        <span class="hljs-tag"><<span class="hljs-name">EditForm</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">"editFormRef"</span>
          <span class="hljs-attr">:key</span>=<span class="hljs-string">"`edit-form_$&#123;updateFormFlag&#125;`"</span>
          <span class="hljs-attr">:info</span>=<span class="hljs-string">"tableAttrs.singleSelected"</span>
          @<span class="hljs-attr">on-validated</span>=<span class="hljs-string">"handleValidated"</span>
          @<span class="hljs-attr">on-submitted</span>=<span class="hljs-string">"handleSubmitted"</span>
        ></span><span class="hljs-tag"></<span class="hljs-name">PointForm</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Modal</span>></span>
      <span class="hljs-comment"><!-- modal end --></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-comment"><!-- table end --></span>
  <span class="hljs-tag"></<span class="hljs-name">SpecialTabs</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
...

<span class="hljs-keyword">const</span> &#123; singleUploadAttrs, ... &#125; = useUpload()
<span class="hljs-keyword">const</span> &#123; tableAttrs, ... &#125; = useTable()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>


<span class="hljs-comment">// @use/upload.js</span>
...

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useUpload</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> singleUploadAttrs = reactive(&#123;
        <span class="hljs-attr">autoUpload</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">uploadRequest</span>: uploadRequest,
        <span class="hljs-attr">beforeUpload</span>: handleBeforeUpload
    &#125;)
    
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">uploadRequest</span>(<span class="hljs-params"></span>) </span>&#123;...&#125;
    
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleBeforeUpload</span>(<span class="hljs-params"></span>) </span>&#123;...&#125;
    
    ...
    
    <span class="hljs-keyword">return</span> &#123; singleUploadAttrs, ... &#125;
&#125;


<span class="hljs-comment">// @use/table.js</span>
...

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useTable</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> tableAttrs = reactive(&#123;
        <span class="hljs-attr">border</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">disabledHover</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">columns</span>: dataPointColumns(),
        <span class="hljs-attr">data</span>: [],
        <span class="hljs-attr">singleSelected</span>: &#123;&#125;,
        <span class="hljs-attr">actionsOptions</span>: [...]
    &#125;)
    
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadTableData</span>(<span class="hljs-params"></span>) </span>&#123;
        ...
        
        tableAttrs.data = [...]
    &#125;
    
    ...
    
    <span class="hljs-keyword">return</span> &#123; tableAttrs, ... &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Volar 体验提升</h2>
<p>随着 <code>Vue3</code> 的稳定，<code>IDE</code> 方面的插件也有了新的支持，官方维护的 <code>Volar</code> 脱颖而出，这里只重点说明 <code>Volar</code> 的编辑器拆分功能来让体验更加丝滑。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17638a2602244f0eb8b5666a70a0f3b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过拆分编辑器，配合 <code>More in js</code> 方式，只需要关注左侧 <code>hooks</code> 代码即可让开发体验上升一个台阶。</p>
<h2 data-id="heading-7">总结</h2>
<p>本次灵感主要解决开发时繁琐的代码横跳，从而找出更优的开发体验，但非最优体验，因人而异，请各位看官勿喷。有何问题，可评论区留言，谢谢！</p>
<p>相逢即是缘，挥一挥手指，留下一个赞吧！(<em>^▽^</em>)</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60721b6386e24d9baac4829b39cd4483~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            