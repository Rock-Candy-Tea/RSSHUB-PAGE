
---
title: '基于Vue实现Excel的解析与导出'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6828a2b8887a40f8987da3161a64979b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 01:22:07 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6828a2b8887a40f8987da3161a64979b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p>最近在整理日常开发中长涉及到的业务需求，正好想到了excel的解析与上传方面的事情，在开发中还是比较常见的，趁着周末做一下整理学习吧</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6828a2b8887a40f8987da3161a64979b~tplv-k3u1fbpfcp-watermark.image" alt="效果.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">基本介绍</h2>
<p>主要基于Vue+element实现文件的解析与导出，用的的插件是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fxlsx" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/xlsx" ref="nofollow noopener noreferrer">xlsx</a>,里面的具体方法，感兴趣的去研究一下，基本的样式，配置就不赘述了，也比较简单，我们直接上主食</p>
<h2 data-id="heading-2">代码实现</h2>
<h3 data-id="heading-3">基本结构</h3>
<p>用户点击文件上传，将excel的表格已json的格式显示在页面中，用户进行操作，检查数据后对服务进行提交，上传操作用的的element中的upload组件</p>
<pre><code class="hljs language-html copyable" lang="html">   <span class="hljs-comment"><!-- 上传文件按钮 --></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"buttonBox"</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">el-upload</span>
       <span class="hljs-attr">action</span>
       <span class="hljs-attr">accept</span>=<span class="hljs-string">".xlsx, .xls"</span>
       <span class="hljs-attr">:auto-upload</span>=<span class="hljs-string">"false"</span>
       <span class="hljs-attr">:show-file-list</span>=<span class="hljs-string">"false"</span>
       <span class="hljs-attr">:on-change</span>=<span class="hljs-string">"handle"</span>
     ></span>
       <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"trigger"</span>></span>选取EXCEL文件<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">el-upload</span>></span>

     <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"disable"</span>></span>采集数据提交<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

   <span class="hljs-comment"><!-- 解析出来的数据 --></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tableBox"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"show"</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>
       <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-info"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
       小主，以下是采集完成的数据，请您检查无误后，点击“采集数据提交”按钮上传至服务器哦！
     <span class="hljs-tag"></<span class="hljs-name">h3</span>></span>

     <span class="hljs-tag"><<span class="hljs-name">el-table</span> <span class="hljs-attr">:data</span>=<span class="hljs-string">"tempData"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span> <span class="hljs-attr">:height</span>=<span class="hljs-string">"height"</span> <span class="hljs-attr">border</span>></span>
       <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"姓名"</span> <span class="hljs-attr">min-width</span>=<span class="hljs-string">"50%"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
       <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"phone"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"电话"</span> <span class="hljs-attr">min-width</span>=<span class="hljs-string">"50%"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">上传解析</h3>
<ul>
<li>通过upload组件可以获取上传的文件流(下图)</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea25c5c4768d40a9b74740e13ca2d9d4~tplv-k3u1fbpfcp-watermark.image" alt="文件流.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>将文件流转为二进制，这里我们可以在utils文件中增加对应的方法(如下)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 把文件按照二进制进行读取</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readFile</span>(<span class="hljs-params">file</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
        <span class="hljs-keyword">let</span> reader = <span class="hljs-keyword">new</span> FileReader();
        reader.readAsBinaryString(file);
        reader.onload = <span class="hljs-function"><span class="hljs-params">ev</span> =></span> &#123;
             resolve(ev.target.result);
        &#125;;
    &#125;);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>通过xlsx将二进制六转为json,这样才能显示</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">//读取FILE中的数据（变为JSON格式）</span>
  <span class="hljs-keyword">let</span> data = <span class="hljs-keyword">await</span> readFile(file);
  <span class="hljs-keyword">let</span> workbook = xlsx.read(data, &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"binary"</span> &#125;),
    worksheet = workbook.Sheets[workbook.SheetNames[<span class="hljs-number">0</span>]];
  data = xlsx.utils.sheet_to_json(worksheet);
  <span class="hljs-comment">// 打印结果加下图</span>
  <span class="hljs-built_in">console</span>.log(workbook);

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb3c1f4c406649569655b128b5b2b385~tplv-k3u1fbpfcp-watermark.image" alt="完整的表.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>把读取出来的数据变为最后可以传递给服务器的数据,我们需要先封装一个映射表来对应传给后端的格式（如下）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 字段对应表</span>
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> character = &#123;
        <span class="hljs-attr">name</span>: &#123;
            <span class="hljs-attr">text</span>: <span class="hljs-string">"姓名"</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>
        &#125;,
        <span class="hljs-attr">phone</span>: &#123;
            <span class="hljs-attr">text</span>: <span class="hljs-string">"电话"</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>
        &#125;
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>转换数据格式</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">let</span> arr = [];
    data.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        <span class="hljs-keyword">let</span> obj = &#123;&#125;;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> character) &#123;
          <span class="hljs-keyword">if</span> (!character.hasOwnProperty(key)) <span class="hljs-keyword">break</span>;
          <span class="hljs-keyword">let</span> v = character[key],
            text = v.text,
            type = v.type;
          v = item[text] || <span class="hljs-string">""</span>;
          type === <span class="hljs-string">"string"</span> ? (v = <span class="hljs-built_in">String</span>(v)) : <span class="hljs-literal">null</span>;
          type === <span class="hljs-string">"number"</span> ? (v = <span class="hljs-built_in">Number</span>(v)) : <span class="hljs-literal">null</span>;
          obj[key] = v;
        &#125;
      arr.push(obj);
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>发送给服务器</p>
</li>
</ul>
<p><strong>这里要看服务器支持多条文件一起发送，如果不支持我们前端就可以采用递归逐条发送的方式进行发送，具体情况可以与后端进行沟通，我们这采用递归的方式进行传输</strong></p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 提交数据给服务器</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">submit</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.tempData.length <= <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
          <span class="hljs-attr">message</span>: <span class="hljs-string">"小主，请您先选择EXCEL文件！"</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">"warning"</span>,
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>
        &#125;);
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-built_in">this</span>.disable = <span class="hljs-literal">true</span>;
      <span class="hljs-keyword">let</span> loadingInstance = Loading.service(&#123;
        <span class="hljs-attr">text</span>: <span class="hljs-string">"小主，请您稍等片刻，奴家正在玩命处理中！"</span>,
        <span class="hljs-attr">background</span>: <span class="hljs-string">"rgba(0,0,0,.5)"</span>
      &#125;);

      <span class="hljs-comment">// 完成后处理的事情</span>
      <span class="hljs-keyword">let</span> complate = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
          <span class="hljs-attr">message</span>: <span class="hljs-string">"小主，奴家已经帮您把数据上传了！"</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">"success"</span>,
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>
        &#125;);
        <span class="hljs-built_in">this</span>.show = <span class="hljs-literal">false</span>;
        <span class="hljs-built_in">this</span>.disable = <span class="hljs-literal">false</span>;
        loadingInstance.close();
      &#125;;

      <span class="hljs-comment">// 需要把数据一条条传递给服务器</span>
      <span class="hljs-keyword">let</span> n = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">let</span> send = <span class="hljs-keyword">async</span> () => &#123;
        <span class="hljs-keyword">if</span> (n > <span class="hljs-built_in">this</span>.tempData.length - <span class="hljs-number">1</span>) &#123;
          <span class="hljs-comment">// 都传递完了</span>
          complate();
          <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">let</span> body = <span class="hljs-built_in">this</span>.tempData[n];
        <span class="hljs-comment">// 走接口</span>
        <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">await</span> createAPI(body);
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">parseInt</span>(result.code) === <span class="hljs-number">0</span>) &#123;
          <span class="hljs-comment">// 成功</span>
          n++;
        &#125;
        send();
      &#125;;
      send();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>以上就是对Excel文件的解析与上传的总结，其实并不是很难，都是日常开发常常涉及的业务，接下来一起看下Excel的导出吧</strong></p>
<h2 data-id="heading-5">Excel的导出</h2>
<h3 data-id="heading-6">基本结构</h3>
<p>一进来页面获取刚刚上传的文件，然后显示在表格中，然后做个分页.......这些就不说了，我们直接从点击导出excel按钮开始,先看下页面结构</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-comment"><!-- 上传按钮 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"buttonBox"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/upload"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-tooltip</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"EXCEL数据采集"</span> <span class="hljs-attr">placement</span>=<span class="hljs-string">"top"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-edit"</span> <span class="hljs-attr">circle</span>></span><span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-tooltip</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-comment"><!-- 搜索区域 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"searchBox"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"search"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"基于姓名、手机模糊搜索"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">"searchHandle"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"disabled"</span>></span>导出选中的数据<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-comment"><!-- 列表区域 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tableBox"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table</span>
        <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span>
        <span class="hljs-attr">:height</span>=<span class="hljs-string">"height"</span>
        <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>
        <span class="hljs-attr">v-loading</span>=<span class="hljs-string">"loading"</span>
        <span class="hljs-attr">element-loading-text</span>=<span class="hljs-string">"小主，奴家正在努力加载中..."</span>
        @<span class="hljs-attr">selection-change</span>=<span class="hljs-string">"selectionChange"</span>
      ></span>
        <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"selection"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"id"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"编号"</span> <span class="hljs-attr">min-width</span>=<span class="hljs-string">"10%"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"姓名"</span> <span class="hljs-attr">min-width</span>=<span class="hljs-string">"20%"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"phone"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"电话"</span> <span class="hljs-attr">min-width</span>=<span class="hljs-string">"20%"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"time"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"创建时间"</span> <span class="hljs-attr">min-width</span>=<span class="hljs-string">"25%"</span> <span class="hljs-attr">:formatter</span>=<span class="hljs-string">"formatter"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-comment"><!-- 分页区域 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pageBox"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-pagination</span>
        <span class="hljs-attr">background</span>
        <span class="hljs-attr">hide-on-single-page</span>
        <span class="hljs-attr">layout</span>=<span class="hljs-string">"total, sizes, prev, pager, next"</span>
        <span class="hljs-attr">:page-size</span>=<span class="hljs-string">"pageSize"</span>
        <span class="hljs-attr">:current-page</span>=<span class="hljs-string">"page"</span>
        <span class="hljs-attr">:total</span>=<span class="hljs-string">"total"</span>
        @<span class="hljs-attr">size-change</span>=<span class="hljs-string">"sizeChange"</span>
        @<span class="hljs-attr">current-change</span>=<span class="hljs-string">"prevNext"</span>
        @<span class="hljs-attr">prev-click</span>=<span class="hljs-string">"prevNext"</span>
        @<span class="hljs-attr">next-click</span>=<span class="hljs-string">"prevNext"</span>
      ></span><span class="hljs-tag"></<span class="hljs-name">el-pagination</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">导出Excel</h3>
<p>将json数据变为sheet数据，新建表格，在表格中插入一个sheet,通过xlsx的writeFile方法将文件写入</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 导出数据</span>
    <span class="hljs-function"><span class="hljs-title">submit</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.selectionList.length <= <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
          <span class="hljs-attr">message</span>: <span class="hljs-string">"小主，请您先选择要导出的数据哦！"</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">"warning"</span>,
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>
        &#125;);
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-built_in">this</span>.disabled = <span class="hljs-literal">true</span>;
      <span class="hljs-keyword">let</span> loadingInstance = Loading.service(&#123;
        <span class="hljs-attr">text</span>: <span class="hljs-string">"小主，请您稍等片刻，奴家正在玩命处理中..."</span>,
        <span class="hljs-attr">background</span>: <span class="hljs-string">"rgba(0,0,0,.5)"</span>
      &#125;);

      <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">this</span>.selectionList.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
          编号: item.id,
          姓名: item.name,
          电话: item.phone
        &#125;;
      &#125;);
      <span class="hljs-comment">// 将json数据变为sheet数据</span>
      <span class="hljs-keyword">let</span> sheet = xslx.utils.json_to_sheet(arr),
      <span class="hljs-comment">// 新建表格</span>
        book = xslx.utils.book_new();
      <span class="hljs-comment">// 在表格中插入一个sheet</span>
      xslx.utils.book_append_sheet(book, sheet, <span class="hljs-string">"sheet1"</span>);
      <span class="hljs-comment">// 通过xlsx的writeFile方法将文件写入</span>
      xslx.writeFile(book, <span class="hljs-string">`user<span class="hljs-subst">$&#123;<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()&#125;</span>.xls`</span>);

      loadingInstance.close();
      <span class="hljs-built_in">this</span>.disabled = <span class="hljs-literal">false</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**以上是对Excele的相关操作，文件上传解析是常见的需求，如果前端小伙伴们对大文件上传以及断电续传感兴趣的可以参考一下我的这篇文章<a href="https://juejin.cn/post/7000654161297539079" target="_blank" title="https://juejin.cn/post/7000654161297539079"><em>大文件上传与断点续传</em></a>，今天就到这了，最后送给前端小伙伴们一句话</p>
<blockquote>
<p>夫学须静也，才须学也，非学无以广才，非志无以成学。淫慢则不能励精，险躁则不能治性。年与时驰，意与日去，遂成枯落</p>
</blockquote></div>  
</div>
            