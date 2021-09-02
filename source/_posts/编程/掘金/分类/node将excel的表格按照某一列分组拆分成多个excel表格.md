
---
title: 'node将excel的表格按照某一列分组拆分成多个excel表格'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1be1e9ee2834ebdb8eb13b321d61c94~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 01:14:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1be1e9ee2834ebdb8eb13b321d61c94~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ol>
<li>拿到所有班级的成绩按照班级生成表格发给每个老师</li>
<li>有了所有人工资后按照每个人生成工资表发放到个人</li>
<li>从数据中心拿到汇总数据后分发给各个单位</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1be1e9ee2834ebdb8eb13b321d61c94~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2b1dabc001740ffa2a205492a7587da~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> XLSXWriter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'xlsx-writestream'</span>);
<span class="hljs-keyword">const</span> powXLSX = <span class="hljs-built_in">require</span>(<span class="hljs-string">'xlsx-extract'</span>).XLSX;
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

<span class="hljs-keyword">const</span> fileName = <span class="hljs-string">'./test.xlsx'</span>;
<span class="hljs-keyword">const</span> groupName = <span class="hljs-string">"班级"</span>;

<span class="hljs-keyword">const</span> generateTable = <span class="hljs-function">(<span class="hljs-params">json, name</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> newFile = <span class="hljs-string">`./result/<span class="hljs-subst">$&#123;name&#125;</span>.xlsx`</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>.xlsx 有 <span class="hljs-subst">$&#123;json.length&#125;</span> 条数据`</span>)

  <span class="hljs-keyword">const</span> writer = <span class="hljs-keyword">new</span> XLSXWriter(newFile, &#123;&#125; <span class="hljs-comment">/* options */</span>);

  writer.getReadStream().pipe(fs.createWriteStream(newFile));
  json.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    writer.addRow(item)
  &#125;)
  writer.finalize();
&#125;

<span class="hljs-keyword">let</span> title = []
<span class="hljs-keyword">let</span> groupIndex = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> data = []
<span class="hljs-keyword">let</span> groupArr = [];
<span class="hljs-keyword">new</span> powXLSX().extract(fileName, &#123; <span class="hljs-attr">sheet_all</span>: <span class="hljs-literal">true</span> &#125;) <span class="hljs-comment">// 读取文件所有sheet，默认只读取第一张sheet，参数配置如下</span>
  .on(<span class="hljs-string">'sheet'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">sheet</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'sheet'</span>, sheet);  <span class="hljs-comment">// sheet is array [sheetname, sheetid, sheetnr]</span>
  &#125;)
  .on(<span class="hljs-string">'row'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">row</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!title.length) &#123;
      title = row
      groupIndex = row.findIndex(<span class="hljs-function"><span class="hljs-params">e</span> =></span> e === groupName)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.log(data.length + <span class="hljs-number">1</span>)
      <span class="hljs-keyword">const</span> value = &#123;&#125;
      title.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> value[item] = row[index])
      data.push(value);
      groupArr = [...new <span class="hljs-built_in">Set</span>([...groupArr, row[groupIndex]])]
    &#125;
  &#125;)
  .on(<span class="hljs-string">'cell'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">cell</span>) </span>&#123;
    <span class="hljs-comment">// console.log('cell', cell); //cell is a value or null</span>
  &#125;)
  .on(<span class="hljs-string">'error'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'error'</span>, err);
  &#125;)
  .on(<span class="hljs-string">'end'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`共 <span class="hljs-subst">$&#123;data.length&#125;</span> 条数据`</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`应生成 <span class="hljs-subst">$&#123;groupArr.length&#125;</span> 个表`</span>)
    groupArr.forEach(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
      generateTable(data.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item[groupName] === name), name)
    &#125;)
  &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e98da625ac6b4d218cca42478481756b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            