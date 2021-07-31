
---
title: 'kindeditor使用_自定义工具栏_结合ThinkPHP使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7365'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 16:07:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=7365'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fkindeditor.net%2Fdoc.php" target="_blank" rel="nofollow noopener noreferrer" title="http://kindeditor.net/doc.php" ref="nofollow noopener noreferrer">官方文档</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdownload.csdn.net%2Fdownload%2Fsr_www%2F12581908" target="_blank" rel="nofollow noopener noreferrer" title="https://download.csdn.net/download/sr_www/12581908" ref="nofollow noopener noreferrer">自用版修改链接，放在/Public目录下</a></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">textarea</span>
<span class="hljs-attr">name</span>=<span class="hljs-string">"article_content"</span>
<span class="hljs-attr">id</span>=<span class="hljs-string">"editor"</span>
<span class="hljs-attr">style</span>=<span class="hljs-string">"width:100%;height:500px;"</span>
></span>&#123;$row[article_content]&#125;<span class="hljs-tag"></<span class="hljs-name">textarea</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/Public/kindeditor/kindeditor-all-min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/Public/kindeditor/lang/zh-CN.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> editorItems = [
<span class="hljs-string">'source'</span>
, <span class="hljs-string">'|'</span>
, <span class="hljs-string">'undo'</span>
, <span class="hljs-string">'redo'</span>
, <span class="hljs-string">'|'</span>
, <span class="hljs-string">'plainpaste'</span>
, <span class="hljs-string">'wordpaste'</span>
, <span class="hljs-string">'clearhtml'</span>
, <span class="hljs-string">'|'</span>
, <span class="hljs-string">'justifyleft'</span>
, <span class="hljs-string">'justifycenter'</span>
, <span class="hljs-string">'justifyright'</span>
, <span class="hljs-string">'|'</span>
, <span class="hljs-string">'fontsize'</span>
, <span class="hljs-string">'forecolor'</span>
, <span class="hljs-string">'hilitecolor'</span>
, <span class="hljs-string">'bold'</span>
, <span class="hljs-string">'italic'</span>
, <span class="hljs-string">'underline'</span>
, <span class="hljs-string">'strikethrough'</span>
, <span class="hljs-string">'removeformat'</span>
, <span class="hljs-string">'|'</span>
, <span class="hljs-string">'image'</span>
, <span class="hljs-string">'insertfile'</span>
, <span class="hljs-string">'|'</span>
, <span class="hljs-string">'link'</span>
, <span class="hljs-string">'unlink'</span>
, <span class="hljs-string">'|'</span>
, <span class="hljs-string">'preview'</span>
, <span class="hljs-string">'fullscreen'</span>
]
KindEditor.ready(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">K</span>) </span>&#123;
<span class="hljs-built_in">window</span>.editor = K.create(<span class="hljs-string">'#editor'</span>, &#123;
<span class="hljs-comment">// , uploadJson: '/Public/kindeditor/php/upload_json.php'</span>
<span class="hljs-attr">items</span>: editorItems
&#125;);
&#125;)
<span class="hljs-comment">//保存时获取更新后的数据</span>
form.on(<span class="hljs-string">'submit(*)'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
<span class="hljs-keyword">var</span> data = e.field
editor.sync()
data.article_content = $(<span class="hljs-string">'#editor'</span>).val()
<span class="hljs-keyword">if</span> (!data.article_content) &#123;
layer.msg(<span class="hljs-string">'文章内容不允许为空'</span>, &#123; <span class="hljs-attr">icon</span>: <span class="hljs-number">5</span> &#125;)
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;
<span class="hljs-built_in">console</span>.log(data)
$.post(<span class="hljs-string">'__CONTROLLER__/store'</span>, data, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(res)
<span class="hljs-keyword">if</span> (res.status == <span class="hljs-number">1</span>) &#123;
layer.msg(<span class="hljs-string">'保存成功'</span>, &#123;
<span class="hljs-attr">icon</span>: <span class="hljs-number">6</span>
, <span class="hljs-attr">time</span>: <span class="hljs-number">2000</span>
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
closeParentLayer()
&#125;)
&#125; <span class="hljs-keyword">else</span> &#123;
layer.msg(res.error, &#123; <span class="hljs-attr">icon</span>: <span class="hljs-number">5</span> &#125;)
&#125;
&#125;)

<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-comment">// /Root/Controller/BaseController.class.php</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">store</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-variable">$data</span>=\in_array(CONTROLLER_NAME,[<span class="hljs-string">'Site'</span>,<span class="hljs-string">'Article'</span>])?I(<span class="hljs-string">'post.'</span>,[],<span class="hljs-string">''</span>):I(<span class="hljs-string">'post.'</span>);
<span class="hljs-keyword">$this</span>->ajaxReturn(D(CONTROLLER_NAME)->store(<span class="hljs-variable">$data</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            