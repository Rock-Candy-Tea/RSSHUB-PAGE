
---
title: '自动化构建API模块'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1053'
author: 掘金
comments: false
date: Sun, 09 May 2021 01:38:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=1053'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前言:自动化构建api大大缩短了在api分类管理上浪费的时间</p>
</blockquote>
<h2 data-id="heading-0">1:引入所需的模块</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">'axios'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2:建立接口配置对象</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> configArray = [
  &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'biz'</span>, <span class="hljs-comment">// 接口类型</span>
    <span class="hljs-attr">apiUrl</span>: ***, <span class="hljs-comment">// 接口请求api</span>
    apiPath: <span class="hljs-string">'./src/api/'</span>, <span class="hljs-comment">// 接口生成文件夹路径</span>
    <span class="hljs-attr">headObj</span>: [
      &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'request'</span>, <span class="hljs-attr">path</span>: <span class="hljs-string">'@/utils/request'</span>&#125;
    ], <span class="hljs-comment">// 每个js文件头部写入内容import</span>
    <span class="hljs-attr">flag</span>: <span class="hljs-string">'w'</span>, <span class="hljs-comment">// a表示续写 w表示覆盖 //默认覆盖</span>
    <span class="hljs-attr">tags</span>: [],
    <span class="hljs-attr">nowDate</span>: getNowFormatDate()<span class="hljs-comment">//获取时间</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3:请求接口获取api路径并进行处理</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//约束好后端接口的格式,这里通过api/隔开,以下是处理方法,最终生成config对象</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">GenerateApi</span>(<span class="hljs-params">config</span>) </span>&#123;
  axios.get(config.apiUrl).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-keyword">let</span> data = res.data.paths
    config.tags = res.data.tags.map(<span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;
      <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">name</span>: v.name, <span class="hljs-attr">fileData</span>: <span class="hljs-string">''</span>,<span class="hljs-attr">fileName</span>: v.description.replace(<span class="hljs-regexp">/\s*/g</span>,<span class="hljs-string">''</span>).replace(<span class="hljs-regexp">/Controller$/g</span>,<span class="hljs-string">''</span>), <span class="hljs-attr">oldContent</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">isExistence</span>: <span class="hljs-literal">false</span>&#125; <span class="hljs-comment">// 每个生成文件头引入</span>
    &#125;)
    <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">Object</span>.entries(data)
    arr.forEach(<span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;
      <span class="hljs-keyword">let</span> msg = v[<span class="hljs-number">1</span>].post|| v[<span class="hljs-number">1</span>].get || v[<span class="hljs-number">1</span>].delete
      <span class="hljs-keyword">let</span> tag = msg.tags[<span class="hljs-number">0</span>]
      config.tags.forEach(<span class="hljs-function"><span class="hljs-params">k</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (tag === k.name) &#123;
          <span class="hljs-keyword">if</span> (!<span class="hljs-regexp">/api/g</span>.test(v[<span class="hljs-number">0</span>])) <span class="hljs-keyword">return</span>
          <span class="hljs-keyword">const</span> tmpUrl = v[<span class="hljs-number">0</span>].split(<span class="hljs-string">'/api/'</span>)[<span class="hljs-number">1</span>]
          k.desc = msg.description
          k.url = tmpUrl
          k.apiName = filterApiName(tmpUrl.split(<span class="hljs-string">'/'</span>))
          k.isExistence = readFileInfo(k.fileName, k.apiName, config)
          k.oldContent = k.isExistence.data
          k.fileData += getTemplate(k, config)
        &#125;
      &#125;)
    &#125;)
    createApiFileJs(config)
  &#125;).catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.error(e, <span class="hljs-string">'接口访问失败'</span>)
  &#125;)
&#125;

<span class="hljs-comment">//api格式化</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">filterApiName</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-keyword">let</span> name = <span class="hljs-string">''</span>
  arr.forEach(<span class="hljs-function">(<span class="hljs-params">k, i</span>) =></span> &#123;
    name += i > <span class="hljs-number">0</span> ? k.toLowerCase().replace(<span class="hljs-regexp">/( |^)[a-z]/g</span>, <span class="hljs-function">(<span class="hljs-params">L</span>) =></span> L.toUpperCase()) : k
  &#125;)
  <span class="hljs-keyword">return</span> name
&#125;
<span class="hljs-comment">//判断api文件是否存在</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readFileInfo</span>(<span class="hljs-params">path, params, config</span>) </span>&#123;
  <span class="hljs-keyword">let</span> result = &#123;
    <span class="hljs-attr">status</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">data</span>: <span class="hljs-string">''</span>
  &#125;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> data = fs.readFileSync(<span class="hljs-string">`<span class="hljs-subst">$&#123;config.apiPath&#125;</span><span class="hljs-subst">$&#123;path&#125;</span>.js`</span>).toString()
    result.status = data.indexOf(params) > <span class="hljs-number">0</span>
    result.data = data
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    result.status = <span class="hljs-literal">false</span>
  &#125;
  <span class="hljs-keyword">return</span> result
&#125;
<span class="hljs-comment">//生成接口模板</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTemplate</span>(<span class="hljs-params">data, config</span>) </span>&#123;
  <span class="hljs-keyword">let</span> template = <span class="hljs-string">''</span>
  <span class="hljs-keyword">if</span> (!readFileInfo(data.fileName, data.apiName).status) &#123;
    template = <span class="hljs-string">`
                /**
                 * <span class="hljs-subst">$&#123;data.desc&#125;</span>
                 * @author: zhangkang
                 * @createDate: <span class="hljs-subst">$&#123;config.nowDate&#125;</span>
                 * @param data &#123;Object&#125; 参数
                 */
                export function <span class="hljs-subst">$&#123;data.apiName&#125;</span>(data) &#123;
                  return request(&#123;
                    type: '<span class="hljs-subst">$&#123;config.type&#125;</span>',
                    url: '<span class="hljs-subst">$&#123;data.url&#125;</span>',
                    method: 'post',
                    data
                  &#125;)
                &#125;`</span>
  &#125;
  <span class="hljs-keyword">return</span> template
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4:node生成并写入文件</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//生成并写入文件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApiFileJs</span>(<span class="hljs-params">config</span>) </span>&#123;
  config.tags.forEach(<span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;
    <span class="hljs-keyword">let</span> path = <span class="hljs-string">`<span class="hljs-subst">$&#123;config.apiPath&#125;</span><span class="hljs-subst">$&#123;v.fileName&#125;</span>.js`</span>
    <span class="hljs-keyword">let</span> heade = createHeadTemplate(v.fileName, config)
    <span class="hljs-comment">// v.fileData = v.oldContent + v.fileData</span>
    v.fileData = heade + v.fileData
    v.fileData = createfileNotes(v, config) + v.fileData
    fs.writeFile(path, v.fileData, &#123;<span class="hljs-attr">flag</span>: config.flag, <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf-8'</span>&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (err) &#123;
        <span class="hljs-built_in">console</span>.error(err, <span class="hljs-string">'失败'</span>)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;v.fileName&#125;</span>文件生成成功`</span>)
      &#125;
    &#125;)
  &#125;)
&#125;

<span class="hljs-comment">//生成头部import模板</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createHeadTemplate</span>(<span class="hljs-params">p, config</span>) </span>&#123;
  <span class="hljs-keyword">let</span> template = <span class="hljs-string">''</span>
  config.headObj.forEach(<span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (!readFileInfo(p, v.path).status) &#123;
      template += <span class="hljs-string">`import <span class="hljs-subst">$&#123;v.name&#125;</span> from '<span class="hljs-subst">$&#123;v.path&#125;</span>'
`</span>
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> template
&#125;

<span class="hljs-comment">//生成相应api的文件注释</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createfileNotes</span>(<span class="hljs-params">data, config</span>) </span>&#123;
  <span class="hljs-keyword">let</span> template = <span class="hljs-string">''</span>
  <span class="hljs-keyword">if</span> (!readFileInfo(data.fileName, <span class="hljs-string">'@file'</span>, config).status) &#123;
    template = <span class="hljs-string">`/**
                 * @file: <span class="hljs-subst">$&#123;data.fileName&#125;</span>.
                 * @authors: yangj.
                 * @createDate: <span class="hljs-subst">$&#123;config.nowDate&#125;</span>.
                 * @Description: <span class="hljs-subst">$&#123;data.name&#125;</span>
               */
               `</span>
  &#125;
  <span class="hljs-keyword">return</span> template
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>每次接口更新通过node run一次就完成构建</p>
</blockquote></div>  
</div>
            