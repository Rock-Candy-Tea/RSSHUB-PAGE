
---
title: '前后端Excel处理篇——前端js-xlsx解析数据'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2485'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 07:18:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=2485'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>遇到一个excel数据上传的需求，查阅excel上传解析的资料，比较通用的有后端<code>POI</code>、<code>easyExcel</code>等，前端为<code>js-xlsx</code>，考虑到<strong>后端上传的方案数据直接解析到数据库中，用户无法对从excel上传的数据进行编辑</strong>，决定采用<code>js-xlsx</code>前端解析的方式，这样比较灵活。</p>
</blockquote>
<h2 data-id="heading-0">1、简介</h2>
<p>由<code>SheetJS</code>出品的<code>js-xlsx</code>是一款非常方便的只需要纯JS即可读取和导出excel的工具库，功能强大，支持格式众多，支持<code>xls</code>、<code>xlsx</code>、<code>ods</code>(一种OpenOffice专有表格文件格式)等十几种格式。本文全部都是以xlsx格式为例。</p>
<p>官方github：<a href="https://github.com/SheetJS/js-xlsx" target="_blank" rel="nofollow noopener noreferrer">github.com/SheetJS/js-…</a></p>
<hr>
<h2 data-id="heading-1">2、js-xlsx解析excel后的对象</h2>
<p>Excel名词：<code>js-xlsx</code>中的抽象类型</p>
<p>工作簿：<code>workBook</code></p>
<p>工作表：<code>Sheets</code></p>
<p><code>Excel</code>引用样式(单元格地址)：<code>cellAddress</code></p>
<p>单元格：<code>cell</code></p>
<h3 data-id="heading-2">单元格对象</h3>
<p>每一个单元格是一个对象（<code>Cell Object</code>）</p>





















































<table><thead><tr><th>key</th><th>value</th></tr></thead><tbody><tr><td>v</td><td>原始值</td></tr><tr><td>w</td><td>格式化文字</td></tr><tr><td>t</td><td>type: b Boolean, e Error, n Number, d Date, s Text, z Stub</td></tr><tr><td>f</td><td>cell formula encoded as an A1-style string (if applicable)</td></tr><tr><td>F</td><td>range of enclosing array if formula is array formula (if applicable)</td></tr><tr><td>r</td><td>rich text encoding (if applicable)</td></tr><tr><td>h</td><td>HTML rendering of the rich text (if applicable)</td></tr><tr><td>c</td><td>comments associated with the cell</td></tr><tr><td>z</td><td>number format string associated with the cell (if requested)</td></tr><tr><td>l</td><td>cell hyperlink object (.Target holds link, .Tooltip is tooltip)</td></tr><tr><td>s</td><td>the style/theme of the cell (if applicable)</td></tr></tbody></table>
<hr>
<h2 data-id="heading-3">3、主要Api</h2>
<p><code>js-xlsx</code>提供的接口非常清晰主要分为两类:</p>
<h3 data-id="heading-4">xlsx对象本身提供的功能</h3>
<ul>
<li>解析数据</li>
<li>导出数据</li>
</ul>
<h3 data-id="heading-5">utils工具类</h3>
<ul>
<li>将数据添加到数据表对象上</li>
<li>将二维数组以及符合格式的对象或者HTML转为工作表对象</li>
<li>将工作簿转为另外一种数据格式</li>
<li>行,列,范围之间的转码和解码</li>
<li>工作簿操作</li>
<li>单元格操作</li>
</ul>
<h2 data-id="heading-6">4、excel解析</h2>
<p>读取excel主要是通过<code>XLSX.read(data, &#123;type:type&#125;);</code>方法来实现，返回一个叫<code>WorkBook</code>的对象，<code>type</code>主要取值如下：
<code>base64</code>、<code>binary``、string</code>、<code>buffer</code>、<code>array</code>、<code>file</code>
这里我偷懒只用了<code>binary</code>，其他几种没有测试。。。</p>
<h3 data-id="heading-7">excel解析选项</h3>

































































<table><thead><tr><th>type</th><th>默认值</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td></td><td>excel编码，主要包括base64、binary、string、buffer、array、file等几种</td></tr><tr><td><strong>raw</strong></td><td>false</td><td>是否只解析原始值</td></tr><tr><td><strong>codepage</strong></td><td></td><td>If specified, use code page when appropriate **</td></tr><tr><td><strong>cellFormula</strong></td><td>true</td><td>存储格式化值在单元格对象f字段</td></tr><tr><td><strong>cellHTML</strong></td><td>true</td><td>Parse rich text and save HTML to the .h field</td></tr><tr><td><strong>cellNF</strong></td><td>false</td><td>Save number format string to the .z field</td></tr><tr><td><strong>cellStyles</strong></td><td>false</td><td>Save style/theme info to the .s field</td></tr><tr><td><strong>cellText</strong></td><td>true</td><td>Generated formatted text to the .w field</td></tr><tr><td><strong>cellDates</strong></td><td>false</td><td>Store dates as type d (default is n)</td></tr><tr><td><strong>dateNF</strong></td><td></td><td>If specified, use the string for date code 14 **</td></tr><tr><td>......</td><td>......</td><td>......</td></tr></tbody></table>
<h3 data-id="heading-8">excle解析代码</h3>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-comment">//1、解析出excel格式</span>
      <span class="hljs-built_in">this</span>.wb = XLSX.read(data, &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'binary'</span>,
        <span class="hljs-attr">cellNF</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">raw</span>: <span class="hljs-literal">true</span>
      &#125;)
     <span class="hljs-comment">//2、SheetNames以字符串数组的形式保存了所有的工作表的名称，通过XLSX.utils.sheet_to_json转化为json格式</span>
      <span class="hljs-built_in">this</span>.wb.SheetNames.forEach(<span class="hljs-function"><span class="hljs-params">sheetName</span> =></span> &#123;
        result.push(&#123;
          <span class="hljs-attr">sheetName</span>: sheetName,
          <span class="hljs-attr">sheet</span>: XLSX.utils.sheet_to_json(<span class="hljs-built_in">this</span>.wb.Sheets[sheetName], &#123; <span class="hljs-attr">raw</span>: <span class="hljs-literal">true</span> &#125;)
        &#125;)
      &#125;)
      <span class="hljs-comment">//3、中英文转换，将对应的中文key转化为自己想要的英文key</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dateTransition</span>(<span class="hljs-params">data, transitionJSON</span>) </span>&#123;
          <span class="hljs-keyword">const</span> list = []
          <span class="hljs-keyword">var</span> obj = &#123;&#125;
          <span class="hljs-keyword">var</span> outdata = <span class="hljs-built_in">JSON</span>.parse(data)
          <span class="hljs-comment">// 数组循环</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < outdata.length; i++) &#123;
            obj = &#123;&#125;
            <span class="hljs-comment">// 循环一行数据中每一个对象</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> outdata[i]) &#123;
              obj[transitionJSON[key]] = outdata[i][key]
            &#125;
            list.push(obj)
          &#125;
          <span class="hljs-keyword">return</span> list
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">5、日期格式转换</h2>
<p><code>js-xlsx</code>在解析excel日期格式时（excel单元格的格式为自定义日期格式），会自动转换为数字格式，尝试了解析选项中的<code>cellDates</code>，<code>dateNF</code>等选项，结果还是不尽如人意，最后考虑通用性问题，采用函数方式转换为时间戳,代码如下。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">formatDate</span>(<span class="hljs-params">numb</span>)</span> &#123;
      <span class="hljs-keyword">const</span> time = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>((numb - <span class="hljs-number">1</span>) * <span class="hljs-number">24</span> * <span class="hljs-number">3600000</span> + <span class="hljs-number">1</span>)
      time.setYear(time.getFullYear() - <span class="hljs-number">70</span>)
      time.setMonth(time.getMonth())
      time.setHours(time.getHours() - <span class="hljs-number">8</span>)
      time.setMinutes(time.getMinutes())
      time.setMilliseconds(time.getMilliseconds())
      <span class="hljs-keyword">return</span> time.valueOf()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">总结</h2>
<p>主要总结了使用<code>js-xlsx</code>解析excel的过程和一些关键点，excel导出等功能我使用的是<code>vxe-table</code>等库，就没有研究这方面。</p>
<h2 data-id="heading-11">参考：</h2>
<blockquote>
<p><a href="https://www.cnblogs.com/vicky-li/p/11469100.html" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/vicky-li/p/…</a>
<a href="https://www.cnblogs.com/liuxianan/p/js-excel.html" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/liuxianan/p…</a></p>
</blockquote></div>  
</div>
            