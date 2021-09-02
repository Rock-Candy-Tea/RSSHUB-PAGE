
---
title: 'express中使用node-xlsx插件下载excel表格'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78236dc6f2c447579f4364df54a2c870~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 01:07:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78236dc6f2c447579f4364df54a2c870~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>node-xlsx是一个轻量级的excel插件，下载导出excel基本的功能这个插件都能实现，本文记录一下express框架中使用node-xlsx插件下载excel表格的步骤。</p>
</blockquote>
<h2 data-id="heading-0">情况一、读取本地文件并返回前端excel流文件</h2>
<blockquote>
<p>这种情况适用于下载excel模板场景，毕竟模板是固定的内容，我们在代码的文件夹中存放一个固定的excel模板，读取并返回即可。</p>
</blockquote>
<ul>
<li>第一步，肯定是要下载安装这个插件<code>npm i node-xlsx</code></li>
<li>第二步，在对应代码中引入这个插件<code>const xlsx = require('node-xlsx')</code></li>
<li>第三步，就是在对应的路由url中写对应代码，代码如下:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// excel导出下载模板接口</span>
route.get(<span class="hljs-string">"/exportExcel"</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;

  <span class="hljs-comment">// 首先，读取本地excel模板文件，并解析成node-xlsx插件需要的数据格式，</span>
  <span class="hljs-comment">// （比如我的表格文件在代码中的excel文件夹下）要引入fs文件模块才能读取哦</span>
  <span class="hljs-keyword">const</span> dataByParse = xlsx.parse(fs.readFileSync(<span class="hljs-string">'./excel/统计模板.xlsx'</span>));

  <span class="hljs-comment">/* 
     打印出来的数据是一个数组，数组中的每一项（每一个对象）都是一个sheet数据，name属性指定的是每一个sheet的名字
     data属性是一个数组，数组中存放的是表格对应每个sheet的数据，data数组中的第一项是“表头”的数据，也可以理解为是
     第一行的数据，后面的每一项就是对应每一行“表体”的数据，具体格式，后续也会举例。
  */</span> 
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"解析数据格式"</span>,dataByParse);

  <span class="hljs-comment">// 最后一步，使用xlsx插件自带的build方法将解析后的数据转换成为excel表格（buffer形式的流文件）</span>
  <span class="hljs-comment">// 以流文件的形式返回给前端，前端接收解析下载即可</span>
  res.send(xlsx.build(dataByParse))

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">node-xlsx需要的数据格式举例子</h3>
<p>比如这样的数据格式，我们看一下数据结构</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> excelData = [
    <span class="hljs-comment">// 第一个sheet内容</span>
    &#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">"我是sheet1"</span>, <span class="hljs-comment">// 给第一个sheet指名字 </span>
      <span class="hljs-attr">data</span>:[  <span class="hljs-comment">// 注意，这里是一个二维数组</span>
        [<span class="hljs-string">"姓名"</span>,<span class="hljs-string">"年龄"</span>,<span class="hljs-string">"家乡"</span>,<span class="hljs-string">"备注"</span>], <span class="hljs-comment">// 第一行</span>
        [<span class="hljs-string">"孙悟空"</span>,<span class="hljs-string">"500"</span>,<span class="hljs-string">"花果山"</span>,<span class="hljs-string">"人送外号斗战胜佛"</span>], <span class="hljs-comment">// 第二行</span>
        [<span class="hljs-string">"猪八戒"</span>,<span class="hljs-string">"88"</span>,<span class="hljs-string">"高老庄"</span>,<span class="hljs-string">"天蓬元帅"</span>], <span class="hljs-comment">// 第三行</span>
      ]
    &#125;,
    <span class="hljs-comment">// 第二个sheet内容</span>
    &#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">"我是sheet2"</span>, <span class="hljs-comment">// 给第二个sheet指名字 </span>
      <span class="hljs-attr">data</span>:[
        [<span class="hljs-string">"城市"</span>,<span class="hljs-string">"国家"</span>,<span class="hljs-string">"人口"</span>,<span class="hljs-string">"经济水平"</span>], <span class="hljs-comment">// 同上</span>
        [<span class="hljs-string">"上海"</span>,<span class="hljs-string">"中国"</span>,<span class="hljs-string">"14亿"</span>,<span class="hljs-string">"越来越好"</span>],
        [<span class="hljs-string">"伦敦"</span>,<span class="hljs-string">"英国"</span>,<span class="hljs-string">"7000万"</span>,<span class="hljs-string">"还行"</span>],
        [<span class="hljs-string">"华盛顿"</span>,<span class="hljs-string">"美国"</span>,<span class="hljs-string">"3.4亿"</span>,<span class="hljs-string">"凑活"</span>]
      ]
    &#125;
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">上述数据格式对应效果图</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78236dc6f2c447579f4364df54a2c870~tplv-k3u1fbpfcp-watermark.image" alt="852.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很显然，数据结构和对应导出的excel结果都是对应的</p>
<h2 data-id="heading-3">情况二、根据前端传递参数，查询mysql数据并返回前端流文件</h2>
<blockquote>
<p>这种情况适用于，一次性的表格文件下载。不会占用后端磁盘文件。就是接收前端传递来的参数，然后把参数拼接sql语句。最终把数据结构组装成node-xlsx插件需要的数据格式即可</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// excel导出下载模板接口</span>
route.post(<span class="hljs-string">"/exportExcel"</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-comment">// 假设我们mysql数据库查询得到了excelData这个数据结果</span>
  <span class="hljs-keyword">let</span> excelData = [
    <span class="hljs-comment">// 第一个sheet内容</span>
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"我是sheet1"</span>, <span class="hljs-comment">// 给第一个sheet指名字 </span>
      <span class="hljs-attr">data</span>: [
        [<span class="hljs-string">"姓名"</span>, <span class="hljs-string">"年龄"</span>, <span class="hljs-string">"家乡"</span>, <span class="hljs-string">"备注"</span>], <span class="hljs-comment">// 第一行</span>
        [<span class="hljs-string">"孙悟空"</span>, <span class="hljs-string">"500"</span>, <span class="hljs-string">"花果山"</span>, <span class="hljs-string">"人送外号斗战胜佛"</span>], <span class="hljs-comment">// 第二行</span>
        [<span class="hljs-string">"猪八戒"</span>, <span class="hljs-string">"88"</span>, <span class="hljs-string">"高老庄"</span>, <span class="hljs-string">"天蓬元帅"</span>], <span class="hljs-comment">// 第三行</span>
      ]
    &#125;,
    <span class="hljs-comment">// 第二个sheet内容</span>
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"我是sheet2"</span>, <span class="hljs-comment">// 给第二个sheet指名字 </span>
      <span class="hljs-attr">data</span>: [
        [<span class="hljs-string">"城市"</span>, <span class="hljs-string">"国家"</span>, <span class="hljs-string">"人口"</span>, <span class="hljs-string">"经济水平"</span>], <span class="hljs-comment">// 同上</span>
        [<span class="hljs-string">"上海"</span>, <span class="hljs-string">"中国"</span>, <span class="hljs-string">"14亿"</span>, <span class="hljs-string">"越来越好"</span>],
        [<span class="hljs-string">"伦敦"</span>, <span class="hljs-string">"英国"</span>, <span class="hljs-string">"7000万"</span>, <span class="hljs-string">"还行"</span>],
        [<span class="hljs-string">"华盛顿"</span>, <span class="hljs-string">"美国"</span>, <span class="hljs-string">"3.4亿"</span>, <span class="hljs-string">"凑活"</span>]
      ]
    &#125;
  ]

  <span class="hljs-comment">// excel表格内容配置单元格宽度</span>
  <span class="hljs-keyword">let</span> optionArr = &#123; 
    <span class="hljs-comment">// 指定sheet1相应宽度</span>
    <span class="hljs-string">"!cols"</span>: [
      &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">15</span> &#125;,
      &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">15</span> &#125;,
      &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">10</span> &#125;,
      &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">50</span> &#125;,
    ],
    <span class="hljs-comment">// 指定sheet2相应宽度</span>
    <span class="hljs-string">"cols"</span>: [
      &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">15</span> &#125;,
      &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">15</span> &#125;,
      &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">10</span> &#125;,
      &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">50</span> &#125;,
    ],
  &#125;

  <span class="hljs-comment">// xlsx.build方法第二个参数接收的是单元格的配置参数</span>
  res.send(xlsx.build(excelData,optionArr))
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">总结</h2>
<p>本文记录的主要是后端方面的代码写法，至于前端的下载excel表格的写法和注意事项常见问题，可以参考我的另外一篇文章，传送门如下：<a href="https://juejin.cn/post/6926880294062522375" target="_blank" title="https://juejin.cn/post/6926880294062522375">juejin.cn/post/692688…</a></p>
<blockquote>
<p>最后附上npmjs官方网站的文档实例介绍，更加齐全哟： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fnode-xlsx" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/node-xlsx" ref="nofollow noopener noreferrer">www.npmjs.com/package/nod…</a></p>
</blockquote></div>  
</div>
            