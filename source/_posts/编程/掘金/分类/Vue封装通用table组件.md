
---
title: 'Vue封装通用table组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2943fc21b90f456c9fc564ae1bdde6b7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 21:52:16 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2943fc21b90f456c9fc564ae1bdde6b7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>对于大部分的后台管理系统，数据表格的展示大同小异，由于不想写重复的代码，所以我选择封装<code>通用table组件</code>，解放双手。如果你的表格有一列并不是简单dom元素，比如<code>switch按钮</code>，完全可以传入一个<code>render函数</code>，来达到目的。</p>
<h2 data-id="heading-1">第一步：定义通用组件</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- pro-table.vue --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table</span>
      <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span>
      <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>
      <span class="hljs-attr">:stripe</span>=<span class="hljs-string">"tableTitle.stripe"</span>
      <span class="hljs-attr">:border</span>=<span class="hljs-string">"tableTitle.border"</span>
      <span class="hljs-attr">:fit</span>=<span class="hljs-string">"tableTitle.fit"</span>
      <span class="hljs-attr">:highlight-current-row</span>=<span class="hljs-string">"tableTitle.highlightCurrentRow"</span>
      @<span class="hljs-attr">selection-change</span>=<span class="hljs-string">"handleSelectionChange"</span>></span>
      <span class="hljs-comment"><!--表格第一列--></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">:type</span>=<span class="hljs-string">"firstTableCol.type"</span>
        <span class="hljs-attr">:width</span>=<span class="hljs-string">"firstTableCol.width"</span>
        <span class="hljs-attr">v-if</span>=<span class="hljs-string">"firstTableCol.select"</span>
      ></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-comment"><!--表格其它列--></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(value,index) in tableCol"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>
                       <span class="hljs-attr">:prop</span>=<span class="hljs-string">"value.prop"</span>
                       <span class="hljs-attr">:label</span>=<span class="hljs-string">"value.label"</span>
                       <span class="hljs-attr">:width</span>=<span class="hljs-string">"value.width || 180"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!value.render"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"value.formatter"</span>></span>
              &#123;&#123; value.formatter(scope.row, value) &#125;&#125;
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"value.getImgurl"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-image</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"value.getImgurl(scope.row, value)"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 70px; height: 70px"</span>
                        <span class="hljs-attr">:preview-src-list</span>=<span class="hljs-string">"value.previewSrcList ? value.previewSrcList(scope.row, value) : value.getImgurl(scope.row, value).split(',')"</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-else</span>></span>
              &#123;&#123; scope.row[value.prop] &#125;&#125;
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-comment"><!--扩展dom--></span>
          <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-else</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Table</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"`cus$&#123;index&#125;`"</span> <span class="hljs-attr">:render</span>=<span class="hljs-string">"value.render"</span> <span class="hljs-attr">:param</span>=<span class="hljs-string">"scope.row"</span>></span><span class="hljs-tag"></<span class="hljs-name">Table</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-comment"><!--基础操作--></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"操作"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(value,index) in operator"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"value.click(scope.row, value)"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
            &#123;&#123; value.text &#125;&#125;
          <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
    <span class="hljs-comment"><!--分页插件--></span>
    <span class="hljs-tag"><<span class="hljs-name">el-pagination</span>
      <span class="hljs-attr">v-show</span>=<span class="hljs-string">"total>0"</span>
      <span class="hljs-attr">:total</span>=<span class="hljs-string">"total"</span>
      <span class="hljs-attr">:page-size.sync</span>=<span class="hljs-string">"pageSize"</span>
      <span class="hljs-attr">:current-page.sync</span>=<span class="hljs-string">"currentPage"</span>
      <span class="hljs-attr">:page-sizes</span>=<span class="hljs-string">"[10, 20, 30, 50]"</span>
      <span class="hljs-attr">layout</span>=<span class="hljs-string">"total, sizes, prev, pager, next, jumper"</span>
      @<span class="hljs-attr">current-change</span>=<span class="hljs-string">"handleCurrentChange"</span>
      @<span class="hljs-attr">size-change</span>=<span class="hljs-string">"handleSizeChange"</span>
      <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"$attrs"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-pagination</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-comment">// render函数</span>
<span class="hljs-keyword">import</span> Table <span class="hljs-keyword">from</span> <span class="hljs-string">'./table'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;Table&#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">tableTitle</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: &#123;
        <span class="hljs-attr">stripe</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">border</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">fit</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">highlightCurrentRow</span>: <span class="hljs-literal">false</span>
      &#125;
    &#125;,
    <span class="hljs-attr">firstTableCol</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: &#123;
        <span class="hljs-attr">select</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-number">55</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'selection'</span>
      &#125;
    &#125;,
    <span class="hljs-attr">tableCol</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: []
    &#125;,
    <span class="hljs-attr">tableData</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: []
    &#125;,
    <span class="hljs-attr">operator</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: []
    &#125;,
    <span class="hljs-attr">total</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">0</span>
    &#125;,
    <span class="hljs-attr">page</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">limit</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">10</span>
    &#125;,
    <span class="hljs-attr">autoScroll</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-attr">currentPage</span>: &#123;
      get () &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.page
      &#125;,
      set (val) &#123;
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'update:page'</span>, val)
      &#125;
    &#125;,
    <span class="hljs-attr">pageSize</span>: &#123;
      get () &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.limit
      &#125;,
      set (val) &#123;
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'update:limit'</span>, val)
      &#125;
    &#125;
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 监听table选择框</span>
    handleSelectionChange (selection) &#123;
      <span class="hljs-comment">// 调用父组件对应的方法 handleSelectionChange</span>
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'handleSelectionChange'</span>, selection)
    &#125;,
    <span class="hljs-comment">// 监听每页多少条数据（limit）</span>
    handleSizeChange (limit) &#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'pagination'</span>, &#123;<span class="hljs-attr">page</span>: <span class="hljs-built_in">this</span>.currentPage, <span class="hljs-attr">limit</span>: limit&#125;)
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.autoScroll) &#123;
        scrollTo(<span class="hljs-number">0</span>, <span class="hljs-number">800</span>)
      &#125;
    &#125;,
    <span class="hljs-comment">// 监听当前是第几页（page）</span>
    handleCurrentChange (page) &#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'pagination'</span>, &#123;<span class="hljs-attr">page</span>: page, <span class="hljs-attr">limit</span>: <span class="hljs-built_in">this</span>.pageSize&#125;)
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.autoScroll) &#123;
        scrollTo(<span class="hljs-number">0</span>, <span class="hljs-number">800</span>)
      &#125;
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">第二步：父组件与子组件进行render通信</h2>
<p>为了实现父组件render函数在子组件中生效，我们需要定义一个<code>render函数</code>，在<code>子组件中引用</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// table.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">render</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Function</span>
    &#125;,
    <span class="hljs-attr">param</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.render(h, <span class="hljs-built_in">this</span>.param)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">第三步：使用组件</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!--
        @自定义事件="父组件方法", 子组件中，this.$emit('自定义事件名称') 触发父组件事件。
        ref="proTable",标记在子组件上，指向子组件实例
    --></span>
    <span class="hljs-tag"><<span class="hljs-name">proTable</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"proTable"</span> <span class="hljs-attr">:tableTitle</span>=<span class="hljs-string">"tableTitle"</span> <span class="hljs-attr">:tableCol</span>=<span class="hljs-string">"tableCol"</span> <span class="hljs-attr">:tableData</span>=<span class="hljs-string">"tableData"</span> <span class="hljs-attr">:operator</span>=<span class="hljs-string">"operator"</span>
        <span class="hljs-attr">:firstTableCol</span>=<span class="hljs-string">"firstTableCol"</span>
        @<span class="hljs-attr">handleSelectionChange</span>=<span class="hljs-string">"handleSelectionChange"</span>
        <span class="hljs-attr">:total</span>=<span class="hljs-string">"total"</span> <span class="hljs-attr">:page.sync</span>=<span class="hljs-string">"queryParams.page"</span> <span class="hljs-attr">:limit.sync</span>=<span class="hljs-string">"queryParams.limit"</span> @<span class="hljs-attr">pagination</span>=<span class="hljs-string">"getList"</span>/></span>

  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> proTable <span class="hljs-keyword">from</span> <span class="hljs-string">'./pro-table'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    proTable
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">queryParams</span>: &#123;
        <span class="hljs-attr">page</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">limit</span>: <span class="hljs-number">10</span>,
      &#125;,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
      <span class="hljs-attr">total</span>: <span class="hljs-number">50</span>,
      <span class="hljs-comment">// element-ui中对table属性的设置</span>
      <span class="hljs-attr">tableTitle</span>: &#123;
        <span class="hljs-string">'stripe'</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-string">"highlightCurrentRow"</span>: <span class="hljs-literal">true</span>
      &#125;,
      <span class="hljs-comment">// 设置table的列</span>
      <span class="hljs-attr">tableCol</span>: [
        &#123; <span class="hljs-attr">prop</span>:<span class="hljs-string">'date'</span>,<span class="hljs-attr">label</span>:<span class="hljs-string">'日期'</span>&#125;,
        &#123; <span class="hljs-attr">prop</span>:<span class="hljs-string">'name'</span>,<span class="hljs-attr">label</span>:<span class="hljs-string">'姓名'</span>&#125;,
        &#123; <span class="hljs-attr">prop</span>:<span class="hljs-string">'address'</span>,<span class="hljs-attr">label</span>:<span class="hljs-string">'地址'</span>,<span class="hljs-attr">width</span>: <span class="hljs-number">300</span>&#125;,
        &#123; <span class="hljs-attr">prop</span>:<span class="hljs-string">'src'</span>,<span class="hljs-attr">label</span>:<span class="hljs-string">'图片'</span>,  
        <span class="hljs-attr">getImgurl</span>: <span class="hljs-function">(<span class="hljs-params">row, col, cellValue</span>) =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getImgurl(row)&#125;, 
        <span class="hljs-attr">previewSrcList</span>: <span class="hljs-function">(<span class="hljs-params">row, col, cellValue</span>) =></span> &#123;<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.listImgUrl(row)&#125;&#125;,
        &#123; <span class="hljs-attr">prop</span>:<span class="hljs-string">'sex'</span>,<span class="hljs-attr">label</span>:<span class="hljs-string">'性别'</span>,  
        <span class="hljs-attr">formatter</span>: <span class="hljs-function">(<span class="hljs-params">row, col, cellVaule</span>) =></span> &#123;<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.sexFormatter(row)&#125;&#125;,
        &#123; <span class="hljs-attr">prop</span>:<span class="hljs-string">'src'</span>,<span class="hljs-attr">label</span>:<span class="hljs-string">'图片'</span>,  
        <span class="hljs-attr">getImgurl</span>: <span class="hljs-function">(<span class="hljs-params">row, col, cellValue</span>) =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getImgurl(row)&#125;&#125;,
        &#123; <span class="hljs-attr">prop</span>:<span class="hljs-string">'text'</span>,<span class="hljs-attr">label</span>:<span class="hljs-string">'函数'</span>, <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h, params</span>) =></span> &#123;<span class="hljs-keyword">return</span>  <span class="hljs-built_in">this</span>.render(h, params)&#125;&#125;
      ],
      <span class="hljs-comment">// table的基本操作</span>
      <span class="hljs-attr">operator</span>: [
        &#123;<span class="hljs-string">'text'</span>:<span class="hljs-string">'详情'</span>, <span class="hljs-attr">click</span>: <span class="hljs-function">(<span class="hljs-params">row, col, cellValue</span>) =></span> &#123;<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getInfo(row)&#125;&#125;,
        &#123;<span class="hljs-string">'text'</span>:<span class="hljs-string">'删除'</span>, <span class="hljs-attr">click</span>: <span class="hljs-function">(<span class="hljs-params">row, col, cellValue</span>) =></span> &#123;<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.delInfo(row)&#125;&#125;,
        &#123;<span class="hljs-string">'text'</span>:<span class="hljs-string">'编辑'</span>, <span class="hljs-attr">click</span>: <span class="hljs-function">(<span class="hljs-params">row, col, cellValue</span>) =></span> &#123;<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.editInfo(row)&#125;&#125;,
      ],
      <span class="hljs-comment">// 模拟数据</span>
      <span class="hljs-attr">tableData</span>: [
        &#123;
          <span class="hljs-attr">date</span>: <span class="hljs-string">'2016-05-02'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'王小虎'</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">'上海市普陀区金沙江路 1518 弄'</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">img</span>:<span class="hljs-string">'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic2.zhimg.com%2F50%2Fv2-193cbb243dc14d3a016caaa54ba02837_hd.jpg&refer=http%3A%2F%2Fpic2.zhimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628435704&t=deb5584cb9ff53fe6977f14a5e0755bb'</span>
        &#125;, &#123;
          <span class="hljs-attr">date</span>: <span class="hljs-string">'2016-05-04'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'王小虎'</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">'上海市普陀区金沙江路 1517 弄'</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-number">1</span>,
          <span class="hljs-attr">img</span>:<span class="hljs-string">'https://pic1.zhimg.com/80/v2-894ab624807fd4cfa33dd4e42cc90ac8_720w.jpg?source=1940ef5c'</span>
        &#125;, &#123;
          <span class="hljs-attr">date</span>: <span class="hljs-string">'2016-05-01'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'王小虎'</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">'上海市普陀区金沙江路 1519 弄'</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">img</span>:<span class="hljs-string">'xx.jpg'</span>
        &#125;, &#123;
          <span class="hljs-attr">date</span>: <span class="hljs-string">'2016-05-03'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'王小虎'</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">'上海市普陀区金沙江路 1516 弄'</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-number">1</span>,
          <span class="hljs-attr">img</span>:<span class="hljs-string">'xx.jpg'</span>
        &#125;],
      <span class="hljs-attr">firstTableCol</span>: &#123;
        <span class="hljs-string">'select'</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-string">'type'</span>: <span class="hljs-string">'selection'</span>
      &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">getInfo</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-comment">// 触发父方法</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"获取详情"</span>,val)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">delInfo</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-comment">// 触发父方法</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"删除信息"</span>,val)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">editInfo</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-comment">// 触发父方法</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"编辑信息"</span>,val)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">getImgurl</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(val.img)
      <span class="hljs-keyword">return</span> val.img
    &#125;,
    <span class="hljs-function"><span class="hljs-title">sexFormatter</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-keyword">return</span> val.sex === <span class="hljs-number">0</span> ? <span class="hljs-string">'男'</span> : <span class="hljs-string">'女'</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">handleSelectionChange</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"监听选择框"</span>,val)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">getList</span>(<span class="hljs-params">queryParams</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"父级方法"</span>,queryParams)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">listImgUrl</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> array = [];
      array.push(<span class="hljs-string">"https://pic1.zhimg.com/80/v2-894ab624807fd4cfa33dd4e42cc90ac8_720w.jpg?source=1940ef5c"</span>);
      array.push(<span class="hljs-string">"https://cdn.pixabay.com/photo/2021/07/01/21/20/girl-6380331_960_720.jpg"</span>);
      <span class="hljs-keyword">return</span> array;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h, params</span>)</span> &#123;
      <span class="hljs-keyword">return</span> h(<span class="hljs-string">'span'</span>, <span class="hljs-literal">null</span> , <span class="hljs-string">'我是一个render组件'</span>)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">总结</h2>
<p>在引用组件的页面中，我们可以给每一个table列加方法，也可以给编辑、删除、详情添加自定义的方法，完全实现定制化。也可以自定义render函数。效果图如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2943fc21b90f456c9fc564ae1bdde6b7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            