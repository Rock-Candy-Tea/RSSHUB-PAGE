
---
title: '基于element- plus 二次封装el-table'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec16d707c864a3bb08567f2ba24693e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 03:26:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec16d707c864a3bb08567f2ba24693e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr>
<p>一般在后台管理系统的开发中，都会遇到很多table，但每一次都去引入el-table就会导致代码十分冗余，代码效率也会低下，所以基于组件做一下二次封装成自己需要的组件就十分nice。</p>
<hr>
<p>拿element-plus官网举例：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">el-table</span>
      <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span>
      <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"date"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"日期"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"姓名"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"address"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"地址"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">components</span>: &#123;
  &#125;,
  setup () &#123;
  <span class="hljs-keyword">const</span> tableData = [&#123;
            <span class="hljs-attr">date</span>: <span class="hljs-string">'2016-05-02'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'王小虎'</span>,
            <span class="hljs-attr">address</span>: <span class="hljs-string">'上海市普陀区金沙江路 1518 弄'</span>
          &#125;, &#123;
            <span class="hljs-attr">date</span>: <span class="hljs-string">'2016-05-04'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'王小虎'</span>,
            <span class="hljs-attr">address</span>: <span class="hljs-string">'上海市普陀区金沙江路 1517 弄'</span>
          &#125;, &#123;
            <span class="hljs-attr">date</span>: <span class="hljs-string">'2016-05-01'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'王小虎'</span>,
            <span class="hljs-attr">address</span>: <span class="hljs-string">'上海市普陀区金沙江路 1519 弄'</span>
          &#125;, &#123;
            <span class="hljs-attr">date</span>: <span class="hljs-string">'2016-05-03'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'王小虎'</span>,
            <span class="hljs-attr">address</span>: <span class="hljs-string">'上海市普陀区金沙江路 1516 弄'</span>
          &#125;]
          <span class="hljs-keyword">return</span> &#123;
          tableData
          &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一个简单的表格就好了，我们只需要在对应的el-table-column中加上对应的prop和label即可。</p>
<p>基于上面的表格定义一个公共组件，我命名为list- table。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec16d707c864a3bb08567f2ba24693e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后在之前应用到的页面引入并使用</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a698a6fbd76e4e848e9ac6ae89aeb4a0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6644b3226ca3473abac179d339c2518c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/192130635a144beb9868b85a93ebcbfd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后来到我们的list.vue逐个封装。首先要考虑我们table的数据类型有哪些，文本，图片，标签，日期，操作按钮等等。代码中我的数据绑定在dataSourc中，通过fieldType来识别字段类型。</p>
<h3 data-id="heading-0">selection选择框：</h3>
<pre><code class="hljs language-js copyable" lang="js">        <el-table-column
          v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"dataSource.isSelection"</span>
          :selectable=<span class="hljs-string">"dataSource.selectable"</span>
          type=<span class="hljs-string">"selection"</span>
          :width=<span class="hljs-string">"dataSource.selectionWidth || 55"</span>>
        </el-table-column>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">序号</h3>
<pre><code class="hljs language-js copyable" lang="js">          <!-- 是否需要序号 -->
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
          <span class="hljs-attr">v-if</span>=<span class="hljs-string">"dataSource.isIndex"</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"index"</span>
          <span class="hljs-attr">label</span>=<span class="hljs-string">"序号"</span>
          <span class="hljs-attr">width</span>=<span class="hljs-string">"55"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">图片字段</h3>
<pre><code class="hljs language-js copyable" lang="js">        <el-table-column
          :min-width=<span class="hljs-string">"item.fieldType === 16 ? '50px' : '150px'"</span>
          v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"[7, 16].includes(item.fieldType)"</span>
          :key=<span class="hljs-string">"item.attr"</span>
          :label=<span class="hljs-string">"item.label"</span>>
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:header</span>=<span class="hljs-string">"scope"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-tooltip</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"tableHeadTooltipShow"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">effect</span>=<span class="hljs-string">"dark"</span> <span class="hljs-attr">:content</span>=<span class="hljs-string">"scope.column.label"</span> <span class="hljs-attr">placement</span>=<span class="hljs-string">"top-start"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"table-head-label"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> @<span class="hljs-attr">mouseenter</span>=<span class="hljs-string">"elementWidth"</span>></span>&#123;&#123;scope.column.label&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-tooltip</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"scope"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-image</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-table__table--header"</span>
              <span class="hljs-attr">:src</span>=<span class="hljs-string">"scope.row[item.attr]"</span>
              <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>
              <span class="hljs-attr">:preview-src-list</span>=<span class="hljs-string">"[scope.row[item.attr]]"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:error</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"image-error-slot"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-picture-outline"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-image</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
        </el-table-column>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">日期</h3>
<pre><code class="hljs language-js copyable" lang="js"> <el-table-column
          v-<span class="hljs-keyword">else</span>-<span class="hljs-keyword">if</span>=<span class="hljs-string">"[3, 13].includes(item.fieldType)"</span>
          min-width=<span class="hljs-string">"150px"</span>
          :show-overflow-tooltip=<span class="hljs-string">"true"</span>
          :key=<span class="hljs-string">"item.attr"</span>
          :label=<span class="hljs-string">"item.label"</span>>
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:header</span>=<span class="hljs-string">"scope"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-tooltip</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"tableHeadTooltipShow"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">effect</span>=<span class="hljs-string">"dark"</span> <span class="hljs-attr">:content</span>=<span class="hljs-string">"scope.column.label"</span> <span class="hljs-attr">placement</span>=<span class="hljs-string">"top-start"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"table-head-label"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> @<span class="hljs-attr">mouseenter</span>=<span class="hljs-string">"elementWidth"</span>></span>&#123;&#123;scope.column.label&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-tooltip</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"scope"</span>></span>
            &#123;&#123;formatDate(scope.row[item.attr], item.fieldType)&#125;&#125;
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
        </el-table-column>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以及日期格式化的方法，这里我引入了moment，感兴趣的可以了解一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> formatDate = <span class="hljs-function">(<span class="hljs-params">val, fieldType</span>) =></span> &#123;
      <span class="hljs-comment">// 如果该时间为空，后端不返回该属性【val = undefined】,页面直接渲染空字符</span>
      <span class="hljs-keyword">if</span> (val === <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
      &#125;
      <span class="hljs-keyword">if</span> (val === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'永久有效'</span>
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">String</span>(val).length === <span class="hljs-number">10</span>) &#123;
        val = val * <span class="hljs-number">1000</span>
      &#125;
      <span class="hljs-keyword">const</span> formatType = fieldType === <span class="hljs-number">3</span> ? <span class="hljs-string">'YYYY-MM-DD'</span> : <span class="hljs-string">'YYYY-MM-DD HH:mm:ss'</span>
      <span class="hljs-keyword">return</span> moment(val).format(formatType)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">操作按钮</h3>
<pre><code class="hljs language-js copyable" lang="js"> <el-table-column
         v-<span class="hljs-keyword">else</span>-<span class="hljs-keyword">if</span>=<span class="hljs-string">"item.fieldType === 99"</span>
         width=<span class="hljs-string">"150px"</span>
         :key=<span class="hljs-string">"item.attr"</span>
         :label=<span class="hljs-string">"item.label"</span>>
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:header</span>=<span class="hljs-string">"scope"</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">el-tooltip</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"tableHeadTooltipShow"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">effect</span>=<span class="hljs-string">"dark"</span> <span class="hljs-attr">:content</span>=<span class="hljs-string">"scope.column.label"</span> <span class="hljs-attr">placement</span>=<span class="hljs-string">"top-start"</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"table-head-label"</span>></span>
               <span class="hljs-tag"><<span class="hljs-name">span</span> @<span class="hljs-attr">mouseenter</span>=<span class="hljs-string">"elementWidth"</span>></span>&#123;&#123;scope.column.label&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
             <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
           <span class="hljs-tag"></<span class="hljs-name">el-tooltip</span>></span>
         <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"scope"</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">span</span>
             <span class="hljs-attr">class</span>=<span class="hljs-string">"cloum-operation"</span>
             <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(operation,index) in scope.row[item.attr]"</span>
             <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>
             @<span class="hljs-attr">click</span>=<span class="hljs-string">"operationRow(scope.row, operation.key)"</span>></span>
             &#123;&#123;operation.label&#125;&#125;
           <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
         <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
       </el-table-column>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>触发父组件中的方法</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> operationRow = <span class="hljs-function">(<span class="hljs-params">obj, operation</span>) =></span> &#123;
      <span class="hljs-comment">// console.log(obj)</span>
      context.emit(<span class="hljs-string">'operationRow'</span>, obj, operation)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">其他一些文本信息</h3>
<pre><code class="hljs language-js copyable" lang="js">        <el-table-column
          v-<span class="hljs-keyword">else</span>
          min-width=<span class="hljs-string">"150px"</span>
          :show-overflow-tooltip=<span class="hljs-string">"true"</span>
          :key=<span class="hljs-string">"item.attr"</span>
          :label=<span class="hljs-string">"item.label"</span>>
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:header</span>=<span class="hljs-string">"scope"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-tooltip</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"tableHeadTooltipShow"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">effect</span>=<span class="hljs-string">"dark"</span> <span class="hljs-attr">:content</span>=<span class="hljs-string">"scope.column.label"</span> <span class="hljs-attr">placement</span>=<span class="hljs-string">"top-start"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"table-head-label"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> @<span class="hljs-attr">mouseenter</span>=<span class="hljs-string">"elementWidth"</span>></span>&#123;&#123;scope.column.label&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-tooltip</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"scope"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"throughDetail(scope.row, item)"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;'can-through': item.detailThrough&#125;"</span>></span>
              &#123;&#123;scope.row[item.attr]&#125;&#125;
            <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
        </el-table-column>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上也就封装好了一个简单的table，然后到应用到的页面在setup中定义一下静态数据</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19bf0fa38ea04104ad778ede4cb3807f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92eeb402e5e94cefbb8e6748f785448c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就算简单的封装成功了。</p></div>  
</div>
            