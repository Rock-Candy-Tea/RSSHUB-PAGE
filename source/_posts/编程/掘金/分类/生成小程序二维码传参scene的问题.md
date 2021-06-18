
---
title: '生成小程序二维码传参scene的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b7006d6e8be466b95a6951e15e761f8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 01:08:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b7006d6e8be466b95a6951e15e761f8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、报错提示</h1>
<pre><code class="copyable">'&#123;"errcode":40169,"errmsg":"invalid length for scene, or the data is not json string hint: [MHecNHnre-dcD9Wa]"&#125;'
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>原因：参数 scene 超过了32位</li>
</ul>
<h1 data-id="heading-1">二、官方文档，如图</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b7006d6e8be466b95a6951e15e761f8~tplv-k3u1fbpfcp-zoom-1.image" alt="avatar" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">三、解决方法（有些方法不治本）</h1>
<h2 data-id="heading-3">（1）、请求接口方式</h2>
<ul>
<li>把scene数据md5加密；</li>
<li>后端  redis:key-value（md5加密后的scene:scene原文） 或 数据表 存scene的数据；</li>
<li>小程序获取到scene之后，请求后端接口根据md5后的值获取加密前的数据。</li>
</ul>
<h2 data-id="heading-4">（2）、缩短参数名</h2>
<ul>
<li>比如：</li>
</ul>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-variable">$param</span>[<span class="hljs-string">'user_id'</span>] = <span class="hljs-number">999</span>;
<span class="hljs-variable">$param</span>[<span class="hljs-string">'shopper'</span>] = <span class="hljs-number">3</span>;
<span class="hljs-variable">$data</span>[<span class="hljs-string">'scene'</span>] = http_build_query(<span class="hljs-variable">$param</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>缩短为：</li>
</ul>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-variable">$param</span>[<span class="hljs-string">'u'</span>] = <span class="hljs-number">999</span>;
<span class="hljs-variable">$param</span>[<span class="hljs-string">'s'</span>] = <span class="hljs-number">3</span>;
<span class="hljs-variable">$data</span>[<span class="hljs-string">'scene'</span>] = http_build_query(<span class="hljs-variable">$param</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">（3）、英文字符隔开参数，和前端约定每个位置的值代表的含义（推荐这个）</h2>
<ul>
<li>比如：</li>
</ul>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-variable">$param</span>[<span class="hljs-string">'user_id'</span>] = <span class="hljs-number">999</span>;
<span class="hljs-variable">$param</span>[<span class="hljs-string">'shopper'</span>] = <span class="hljs-number">3</span>;
<span class="hljs-variable">$data</span>[<span class="hljs-string">'scene'</span>] = http_build_query(<span class="hljs-variable">$param</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以用英文字符 ,;_等隔开，如下</li>
</ul>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-variable">$userId</span> = <span class="hljs-number">999</span>;
<span class="hljs-variable">$shopper</span> = <span class="hljs-number">3</span>;
<span class="hljs-variable">$data</span>[<span class="hljs-string">'scene'</span>] =  <span class="hljs-variable">$userId</span> . <span class="hljs-string">';'</span> . <span class="hljs-variable">$shopper</span>;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            