
---
title: '「项目 📝 」React实现导入导出Excel文件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bb0ec5dba4e4c6c8ee83e3617e83669~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 07:28:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bb0ec5dba4e4c6c8ee83e3617e83669~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">🌼 表示层</h1>
<p>这里我是使用的是antd的Upload上传组件</p>
<p>引用antd部分代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Button,Table,Upload &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Upload</span> &#123;<span class="hljs-attr">...props</span>&#125; <span class="hljs-attr">fileList</span>=<span class="hljs-string">&#123;state.fileList&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> ></span>Excel导入<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Upload</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleExport&#125;</span>></span>Excel导出<span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">🌴  业务层</h1>
<p>首先分析一下工作：</p>
<ul>
<li><strong>导入</strong>Excel工作：用户上传Excel表格，将表格内容转换为json对象方便后端处理，后端将数据存储数据库；</li>
<li><strong>导出</strong>Excel工作：获取后端json格式数据，前端将数据转换为sheet工作薄对象，生成的对象转换为Excel表格下载导出；</li>
</ul>
<p>下面就是技术层面的细节</p>
<h2 data-id="heading-2">✨ 核心插件xlsx</h2>
<p>安装xlsx：<code>npm install xlsx --save-dev</code></p>
<p>主要介绍用到的核心api：</p>
<ul class="contains-task-list">
<li class="task-list-item">
<p><input type="checkbox" disabled> XLSX.read(data,type) // 解析Excel数据</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> workbook.Sheets[workbook.SheetNames[0]] // 取到<strong>workbook</strong>对象中的第一个sheet表，<code>规定用户只有一个sheets</code>，不理解workbook的下面有解释</p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]], &#123;header:1,defval:’’&#125;）// 将工作簿对象转换为JSON对象数组，<code>注意defval不设置‘’则默认值为empty</code></p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled> XLSX.utils.json_to_sheet(json) // 将json对象转换为工作簿对象</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// workbook 理解：</span>
&#123;
    <span class="hljs-attr">SheetNames</span>: [<span class="hljs-string">'sheet1'</span>, <span class="hljs-string">'sheet2'</span>],
    <span class="hljs-attr">Sheets</span>: &#123;
        <span class="hljs-comment">// worksheet</span>
        <span class="hljs-string">'sheet1'</span>: &#123;
            <span class="hljs-comment">// cell</span>
            <span class="hljs-string">'A1'</span>: &#123; ... &#125;,
            <span class="hljs-comment">// cell</span>
            <span class="hljs-string">'A2'</span>: &#123; ... &#125;,
            ...
        &#125;,
        <span class="hljs-comment">// worksheet</span>
        <span class="hljs-string">'sheet2'</span>: &#123;
            <span class="hljs-comment">// cell</span>
            <span class="hljs-string">'A1'</span>: &#123; ... &#125;,
            <span class="hljs-comment">// cell</span>
            <span class="hljs-string">'A2'</span>: &#123; ... &#125;,
            ...
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">🍒 excel 导入</h2>
<p>核心代码 ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> f = file;
<span class="hljs-keyword">const</span> reader = <span class="hljs-keyword">new</span> FileReader();
reader.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">try</span>&#123;
        <span class="hljs-keyword">const</span> datas = e.target.result;
        <span class="hljs-keyword">const</span> workbook = XLSX.read(datas, &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">"binary"</span>,&#125;); <span class="hljs-comment">//解析datas</span>
        <span class="hljs-keyword">const</span> first_worksheet = workbook.Sheets[workbook.SheetNames[<span class="hljs-number">0</span>]]; <span class="hljs-comment">//是工作簿中的工作表的第一个sheet</span>
        <span class="hljs-keyword">const</span> jsonArr = XLSX.utils.sheet_to_json(first_worksheet, &#123;<span class="hljs-attr">header</span>: <span class="hljs-number">1</span>,<span class="hljs-attr">defval</span>:<span class="hljs-string">''</span>&#125;); <span class="hljs-comment">//将工作簿对象转换为JSON对象数组</span>
        handleImpotedJson(jsonArr)<span class="hljs-comment">// 数组处理</span>
        message.success(<span class="hljs-string">'Excel上传解析成功！'</span>)
    &#125;<span class="hljs-keyword">catch</span>(e)&#123;
      message.error(<span class="hljs-string">'文件类型不正确！或文件解析错误'</span>)
    &#125; 
&#125;;
reader.readAsBinaryString(f);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>理解：</p>
<ol>
<li>FileReader对象实例化<code>file</code>对象在<code>onload</code>事件里进行处理</li>
<li>XLSX.read 解析<code>data</code></li>
<li>XLSX.utils.sheet_to_json(first_worksheet, &#123;header: 1,defval:''&#125;) 将解析出的工作簿对象转化为<code>JSON</code>对象</li>
</ol>
<h2 data-id="heading-4">🍇 excel 导出</h2>
<p>核心代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> downloadExcel = <span class="hljs-function">() =></span>&#123;
    <span class="hljs-keyword">const</span> json = handleExportedJson(data)
    <span class="hljs-keyword">const</span> sheet = XLSX.utils.json_to_sheet(json);
    openDownloadDialog(sheet2blob(sheet,<span class="hljs-string">"Sheet1"</span>), <span class="hljs-string">"下载文件.xls"</span>)
&#125;
<span class="hljs-keyword">const</span> handleExportedJson = <span class="hljs-function">(<span class="hljs-params">array</span>) =></span>&#123;...&#125;  <span class="hljs-comment">// 处理Json数据</span>
<span class="hljs-keyword">const</span> openDownloadDialog = <span class="hljs-function">(<span class="hljs-params">url, saveName</span>) =></span>&#123;...&#125; <span class="hljs-comment">// 打开下载</span>
<span class="hljs-keyword">const</span> sheet2blob = <span class="hljs-function">(<span class="hljs-params">sheet, sheetName</span>) =></span>&#123;...&#125; <span class="hljs-comment">// 转成blob类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>理解：</p>
<ol>
<li>得到处理后的<code>json</code>格式数据</li>
<li>XLSX.utils.json_to_sheet(json) 转换成<code>sheet</code>工作簿对象</li>
<li>sheet2blob(sheet,saveName) 将工作簿对象转换成 <code>blob</code></li>
<li>openDownloadDialog 创建blob地址通过<code><a></code>标签实现下载动作</li>
</ol>
<h2 data-id="heading-5">🍑 excel 导出插件（js-export-excel）</h2>
<p>之前为啥没放自实现的代码，那不是因为发现有好用的插件嘛，代码很简单。</p>
<p>核心代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 直接导出文件</span>
<span class="hljs-keyword">let</span> dataTable = [];  <span class="hljs-comment">//excel文件中的数据内容</span>
<span class="hljs-keyword">let</span> option = &#123;&#125;;  <span class="hljs-comment">//option代表的就是excel文件</span>
dataTable  = data;  <span class="hljs-comment">//数据源</span>
option.fileName = <span class="hljs-string">"下载文件"</span>;  <span class="hljs-comment">//excel文件名称</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"data==="</span>,dataTable)
option.datas = [
    &#123;
        <span class="hljs-attr">sheetData</span>: dataTable,  <span class="hljs-comment">//excel文件中的数据源</span>
        <span class="hljs-attr">sheetName</span>: <span class="hljs-string">'Sheet1'</span>,  <span class="hljs-comment">//excel文件中sheet页名称</span>
        <span class="hljs-attr">sheetFilter</span>: [<span class="hljs-string">'id'</span>, <span class="hljs-string">'name'</span>, <span class="hljs-string">'belong'</span>, <span class="hljs-string">'step'</span>,<span class="hljs-string">'tag'</span>],  <span class="hljs-comment">//excel文件中需显示的列数据</span>
        <span class="hljs-attr">sheetHeader</span>: [<span class="hljs-string">'项目id'</span>, <span class="hljs-string">'项目名称'</span>, <span class="hljs-string">'所属公司'</span>, <span class="hljs-string">'项目阶段'</span>,<span class="hljs-string">'项目标签'</span>],  <span class="hljs-comment">//excel文件中每列的表头名称</span>
    &#125;
]
<span class="hljs-keyword">let</span> toExcel = <span class="hljs-keyword">new</span> ExportJsonExcel(option);  <span class="hljs-comment">//生成excel文件</span>
toExcel.saveExcel();  <span class="hljs-comment">//下载excel文件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上为这个插件的基本用法，还支持导出Blob，支持压缩等，详细见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fjs-export-excel" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/js-export-excel" ref="nofollow noopener noreferrer">官网</a></p>
<p>解释核心 <strong>option</strong>:</p>
<ul>
<li>
<p>fileName 下载文件名(默认：<code>download</code>)</p>
</li>
<li>
<p>datas 数据:</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*多个sheet*/</span>
<span class="hljs-comment">/*每个sheet为一个object */</span>
[&#123;
    <span class="hljs-attr">sheetData</span>:[], <span class="hljs-comment">// 数据</span>
    <span class="hljs-attr">sheetName</span>:<span class="hljs-string">''</span>, <span class="hljs-comment">// （非必需）sheet名字，默认为sheet1</span>
    <span class="hljs-attr">sheetFilter</span>:[], <span class="hljs-comment">//（非必需）列过滤(只有在 data 为 object 下起作用)</span>
    <span class="hljs-attr">sheetHeader</span>:[] <span class="hljs-comment">// 第一行，标题</span>
    <span class="hljs-attr">columnWidths</span>: [] <span class="hljs-comment">//（非必需）列宽，需与列顺序对应</span>
&#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器支持：ie 10+ 我测试下来demo在chrom、Safari、IE下都是能用的。</p>
<h1 data-id="heading-6">🌸  实现效果</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bb0ec5dba4e4c6c8ee83e3617e83669~tplv-k3u1fbpfcp-watermark.image" alt="2021-07-09 12.23.55 1 1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有不懂得可以看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHearLing%2Freact-excel-demo%2Ftree%2Fmaster%2Fdemo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/HearLing/react-excel-demo/tree/master/demo" ref="nofollow noopener noreferrer">GitHub demo源码</a></p>
<h1 data-id="heading-7">🍀 结语</h1>
<p>这是一个简单的业务实现，仔细的总结了一下。💗 感谢你看到这～💗 ，如果觉得不错麻烦点个赞 👍</p>
<p>刚忙完毕业的事儿，事情没有那么多了，又可以慢慢发文了，预告下一篇吧，关于我的「毕业设计」，给大家看个效果图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01bf489d1bfa4efe8eeaea5ab9e4d33d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我感觉这个可以到时候改成🌟博客啥的，毕竟开发了挺久的，想着有点用嘛 😂</p></div>  
</div>
            