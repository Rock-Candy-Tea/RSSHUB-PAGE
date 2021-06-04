
---
title: '基于Vue实现excel导入导出'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76d24ebe68b4daf90fa1ca6a834ace1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 20:58:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76d24ebe68b4daf90fa1ca6a834ace1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">导入excel表：</h1>
<h2 data-id="heading-1">导入excel导入功能vue-element-admin已经提供了，只要基于源码改造即可。</h2>
<h3 data-id="heading-2">（1）：excel导入功能需要使用npm包xlsx，所以需要安装xlsx插件， 使用 <code>npm i xlsx</code> 下载组件。</h3>
<h3 data-id="heading-3">（2）：将vue-element-admin提供的导入功能，新建成一个组件，组件源码地址（cv过去就好了）：</h3>
<p><code>https://github.com/PanJiaChen/vue-element-admin/blob/master/src/components/UploadExcel/index.vue</code></p>
<h3 data-id="heading-4">得到类似于这样的页面（多少会有点差异，我修改了一下样式）：</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76d24ebe68b4daf90fa1ca6a834ace1~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">（3）：使用Vue全局注册的方式注册并导入 excel 组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> UploadExcel <span class="hljs-keyword">from</span> <span class="hljs-string">'./UploadExcel'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
<span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span> &#123;
  Vue.component(<span class="hljs-string">'UploadExcel'</span>, UploadExcel) <span class="hljs-comment">// 注册导入excel组件</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">（4）：使用一个中间组件导入，注册在全局的excel组件（为什么要使用一个中间模块呢？因为在excel组件源码中需要传递两个props且为函数，需要使用一个中间组件传参，这是最方便以及简单的办法了）</h3>
<pre><code class="hljs language-js copyable" lang="js">props: &#123;
    <span class="hljs-attr">beforeUpload</span>: <span class="hljs-built_in">Function</span>, <span class="hljs-comment">// eslint-disable-line</span>
    <span class="hljs-attr">onSuccess</span>: <span class="hljs-built_in">Function</span><span class="hljs-comment">// eslint-disable-line</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">（5）：从源码中我们可以看到打开文件按钮其实打开的其实是隐藏域<code>input type 为 file</code>类型的文件域，其中 <code>@change="handleClick</code> 是用来判断文件域中有无数据，从而决定是否调用<code>upload</code> 函数， <code>upload</code> 函数中判断使用props传过来的参数 <code>beforeUpload</code> 函数是否有值，有值就直接执行并拿到返回值 <code>before</code> ，如果传递了函数 <code>beforeUpload</code>，并且没有 <code>return</code> 则结束导入，导入失败，如果函数 <code>beforeUpload</code> 有返回值，或者没有传 <code>beforeUpload</code> 则调用函数 <code>readerData</code> 并且把 excel 文件作为形参传递过去，在函数 <code>readerData</code> 中我们可以看到 读取文件是基于原生 <code>FileReader</code> 构造函数，并且返回值是一个Promise对象，在 <code>reader.onload</code> 事件中我们可以看到，<code>header 和 results</code> 这两个返回值被传入到 <code>generateData</code> 函数中，<code>generateData</code> 函数拿到结果后，判断我们是否传递参数 <code>onSuccess</code> ,如果传递，则调用函数传递结果 <code>header 和 results</code>。</h3>
<h3 data-id="heading-8">以上我们可以看到使用该组件非常的简单，只需要传递 <code>onSuccess</code> 函数， 如果在 <code>readerData</code> 读取excel表之前还需要做什么操作时就要传递 <code>beforeUpload</code> 函数（一定要有返回值， 否则上传文件失败）。</h3>
<pre><code class="hljs language-js copyable" lang="js"><input ref=<span class="hljs-string">"excel-upload-input"</span> <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"excel-upload-input"</span> type=<span class="hljs-string">"file"</span> accept=<span class="hljs-string">".xlsx, .xls"</span> @change=<span class="hljs-string">"handleClick"</span>>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"drop"</span> @<span class="hljs-attr">drop</span>=<span class="hljs-string">"handleDrop"</span> @<span class="hljs-attr">dragover</span>=<span class="hljs-string">"handleDragover"</span> @<span class="hljs-attr">dragenter</span>=<span class="hljs-string">"handleDragover"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">:loading</span>=<span class="hljs-string">"loading"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-left:16px;"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleUpload"</span>></span>打开文件<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">handleUpload</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$refs[<span class="hljs-string">'excel-upload-input'</span>].click();
    &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-keyword">const</span> files = e.target.files;
      <span class="hljs-keyword">const</span> rawFile = files[<span class="hljs-number">0</span>]; <span class="hljs-comment">// only use files[0]</span>
      <span class="hljs-keyword">if</span> (!rawFile) <span class="hljs-keyword">return</span>;
      <span class="hljs-built_in">this</span>.upload(rawFile);
    &#125;,
<span class="hljs-function"><span class="hljs-title">upload</span>(<span class="hljs-params">rawFile</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$refs[<span class="hljs-string">'excel-upload-input'</span>].value = <span class="hljs-literal">null</span>; <span class="hljs-comment">// fix can't select the same excel</span>
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.beforeUpload) &#123;
        <span class="hljs-built_in">this</span>.readerData(rawFile);
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-keyword">const</span> before = <span class="hljs-built_in">this</span>.beforeUpload(rawFile);
      <span class="hljs-keyword">if</span> (before) &#123;
        <span class="hljs-built_in">this</span>.readerData(rawFile);
      &#125;
    &#125;,
<span class="hljs-function"><span class="hljs-title">readerData</span>(<span class="hljs-params">rawFile</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> reader = <span class="hljs-keyword">new</span> FileReader();
        reader.onload = <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
          <span class="hljs-keyword">const</span> data = e.target.result;
          <span class="hljs-keyword">const</span> workbook = XLSX.read(data, &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'array'</span> &#125;);
          <span class="hljs-keyword">const</span> firstSheetName = workbook.SheetNames[<span class="hljs-number">0</span>];
          <span class="hljs-keyword">const</span> worksheet = workbook.Sheets[firstSheetName];
          <span class="hljs-keyword">const</span> header = <span class="hljs-built_in">this</span>.getHeaderRow(worksheet);
          <span class="hljs-keyword">const</span> results = XLSX.utils.sheet_to_json(worksheet);
          <span class="hljs-built_in">this</span>.generateData(&#123; header, results &#125;);
          <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">false</span>;
          resolve();
        &#125;;

        reader.readAsArrayBuffer(rawFile);
      &#125;);
    &#125;,
<span class="hljs-function"><span class="hljs-title">generateData</span>(<span class="hljs-params">&#123; header, results &#125;</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.excelData.header = header;
      <span class="hljs-built_in">this</span>.excelData.results = results;
      <span class="hljs-built_in">this</span>.onSuccess && <span class="hljs-built_in">this</span>.onSuccess(<span class="hljs-built_in">this</span>.excelData);
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">(6)：拿到 <code>header</code> 和 <code>results</code> 结果后结果类似于下图：</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80fd2dbfd38b4e04a7d45b2d3ed4a7d6~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">根据自己的需要的格式进行格式转换，然后调用后台接口就基本完成了，但是excel表中有一个时间问题需要自己转换一下时间格式，该函数我已经写出来并贴在代码区了（这里就不细说了）：</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">formatDate</span>(<span class="hljs-params">numb, format</span>)</span> &#123;
      <span class="hljs-keyword">const</span> time = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>((numb - <span class="hljs-number">1</span>) * <span class="hljs-number">24</span> * <span class="hljs-number">3600000</span> + <span class="hljs-number">1</span>)
      time.setYear(time.getFullYear() - <span class="hljs-number">70</span>)
      <span class="hljs-keyword">const</span> year = time.getFullYear() + <span class="hljs-string">''</span>
      <span class="hljs-keyword">const</span> month = time.getMonth() + <span class="hljs-number">1</span> + <span class="hljs-string">''</span>
      <span class="hljs-keyword">const</span> date = time.getDate() - <span class="hljs-number">1</span> + <span class="hljs-string">''</span>
      <span class="hljs-keyword">if</span> (format && format.length === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">return</span> year + format + month + format + date
      &#125;
      <span class="hljs-keyword">return</span> year + (month < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + month : month) + (date < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + date : date)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">导出excel表：</h1>
<h2 data-id="heading-12">1、Excel 的导入导出都是依赖于js-xlsx来实现的， 在 js-xlsx的基础上又封装了Export2Excel.js来方便导出数据。</h2>
<h2 data-id="heading-13">2、由于 Export2Excel不仅依赖js-xlsx还依赖file-saver和script-loader，所以开始前需要下载<code>xlsx file-saver</code> 和 <code>script-loader</code> 两个包：</h2>
<pre><code class="hljs language-js copyable" lang="js">npm install xlsx file-saver -S
npm install script-loader -S -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">(1)：由于js-xlsx体积还是很大的，导出功能也不是一个非常常用的功能，所以使用的时候建议使用懒加载。使用方法如下：</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span>(<span class="hljs-string">'@/vendor/Export2Excel'</span>).then(<span class="hljs-function"><span class="hljs-params">excel</span> =></span> &#123;
  excel.export_json_to_excel(&#123;
    <span class="hljs-attr">header</span>: tHeader, <span class="hljs-comment">//表头 必填</span>
    data, <span class="hljs-comment">//具体数据 必填</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'excel-list'</span>, <span class="hljs-comment">//非必填</span>
    <span class="hljs-attr">autoWidth</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">//非必填</span>
    <span class="hljs-attr">bookType</span>: <span class="hljs-string">'xlsx'</span> <span class="hljs-comment">//非必填</span>
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">（2）：excel导出参数的介绍：</h3>















































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>可选值</th><th>默认值</th></tr></thead><tbody><tr><td>header</td><td>导出数据的表头</td><td>Array</td><td>/</td><td>[]</td></tr><tr><td>data</td><td>导出的具体数据</td><td>Array</td><td>/</td><td>[[]]</td></tr><tr><td>filename</td><td>导出文件名</td><td>String</td><td>/</td><td>excel-list</td></tr><tr><td>autoWidth</td><td>单元格是否要自适应宽度</td><td>Boolean</td><td>true / false</td><td>true</td></tr><tr><td>bookType</td><td>导出文件类型</td><td>String</td><td>xlsx, csv, txt, more</td><td>xlsx</td></tr></tbody></table>
<h3 data-id="heading-16">（3）：我们最重要的一件事，就是把表头和数据进行相应的对应填上 <code>header</code> 和 <code>data</code> ，一个生成表头，一个生成表体，将数据转换好数据结构之后直接传入即可。</h3>
<h3 data-id="heading-17">（4）：我们从上文中说道excel表有时间问题，其excel时间与js时间对应不上，我们存入的时候做了时间转换，所以现在拿出也要做时间转换，代码如下：</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatDate</span>(<span class="hljs-params">date, fmt = <span class="hljs-string">'yyyy-MM-dd'</span></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!(date <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)) &#123;
    date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(date);
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/(y+)/</span>.test(fmt)) &#123;
    fmt = fmt.replace(<span class="hljs-built_in">RegExp</span>.$1, (date.getFullYear() + <span class="hljs-string">''</span>).substr(<span class="hljs-number">4</span> - <span class="hljs-built_in">RegExp</span>.$1.length));
  &#125;
  <span class="hljs-keyword">const</span> o = &#123;
    <span class="hljs-string">'M+'</span>: date.getMonth() + <span class="hljs-number">1</span>,
    <span class="hljs-string">'d+'</span>: date.getDate(),
    <span class="hljs-string">'h+'</span>: date.getHours(),
    <span class="hljs-string">'m+'</span>: date.getMinutes(),
    <span class="hljs-string">'s+'</span>: date.getSeconds()
  &#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> k <span class="hljs-keyword">in</span> o) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`(<span class="hljs-subst">$&#123;k&#125;</span>)`</span>).test(fmt)) &#123;
      <span class="hljs-keyword">const</span> str = o[k] + <span class="hljs-string">''</span>;
      fmt = fmt.replace(<span class="hljs-built_in">RegExp</span>.$1, (<span class="hljs-built_in">RegExp</span>.$1.length === <span class="hljs-number">1</span>) ? str : padLeftZero(str));
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> fmt;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">复杂表头的导出：</h2>
<h3 data-id="heading-19">excel中复杂表头的导出方法 主要是 <code>multiHeader</code> 和 <code>merges</code> 两个参数</h3>


























<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>可选值</th><th>默认值</th></tr></thead><tbody><tr><td>multiHeader</td><td>复杂表头的部分</td><td>Array</td><td>/</td><td>[[]]</td></tr><tr><td>merges</td><td>需要合并的部分</td><td>Array</td><td>/</td><td>[]]</td></tr></tbody></table>
<h3 data-id="heading-20">multiHeader里面是一个二维数组，里面的一个元素是一行表头，假设你想得到一个如图的结构mutiHeader应该这样定义：</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> multiHeader = [[<span class="hljs-string">'姓名'</span>, <span class="hljs-string">'主要信息'</span>, <span class="hljs-string">''</span>, <span class="hljs-string">''</span>, <span class="hljs-string">''</span>, <span class="hljs-string">''</span>, <span class="hljs-string">'部门'</span>]]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">multiHeader中的一行表头中的字段的个数需要和真正的列数相等，假设想要跨列，多余的空间需要定义成空串它主要对应的是标准的表头</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> header = [<span class="hljs-string">'姓名'</span>, <span class="hljs-string">'手机号'</span>, <span class="hljs-string">'入职日期'</span>, <span class="hljs-string">'聘用形式'</span>, <span class="hljs-string">'转正日期'</span>, <span class="hljs-string">'工号'</span>, <span class="hljs-string">'部门'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">如果，我们要实现其合并的效果， 需要设定merges选项</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> merges = [<span class="hljs-string">'A1:A2'</span>, <span class="hljs-string">'B1:F1'</span>, <span class="hljs-string">'G1:G2'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">merges的顺序是没关系的，只要配置这两个属性，就可以导出复杂表头的excel了</h3>
<h3 data-id="heading-24">最后配置项：</h3>
<pre><code class="hljs language-js copyable" lang="js"> excel.export_json_to_excel(&#123;
          <span class="hljs-attr">header</span>: <span class="hljs-built_in">Object</span>.keys(headers),
          data,
          <span class="hljs-attr">filename</span>: <span class="hljs-string">'员工资料表'</span>,
          multiHeader, <span class="hljs-comment">// 复杂表头</span>
          merges <span class="hljs-comment">// 合并选项</span>
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            