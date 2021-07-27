
---
title: '【VUE】在element-ui里面加参数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa116f2b23f4b229fcaf523d202d966~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 17:47:43 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa116f2b23f4b229fcaf523d202d966~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>前言</strong></p>
<blockquote>
<p>今天开发遇到了一个场景：循环里面放<code>el-upload</code>，在上传文件时需要获取到循环的<code>index</code>，但是<code>on-change</code>自带的参数<code>(file, fileList)</code>也需要用到，所以不能重写函数，只能新加<code>index</code></p>
</blockquote>
<p>原本是想根据vue文档里面的<code>$event</code>调用函数的原参
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa116f2b23f4b229fcaf523d202d966~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>刚开始是这么写的：</p>
<pre><code class="copyable"><div v-for="(item, index) in list" :key="index">
  <el-upload action="" :file-list="doc.fileList" 
  :show-file-list="false" 
  :auto-upload="false" 
  :on-change="fileChange($event, index)"
  :multiple="false"
  :limit="1">
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后发现报错<code>$event未定义</code>，看了半天才反应过来是<code>:on-change</code>而不是<code>@on-change</code>，<code>:on-change</code>是一个属性而不是绑定事件，所以需要传一个函数进去，最后改成：</p>
<pre><code class="copyable"><div v-for="(item, index) in list" :key="index">
  <el-upload action="" :file-list="doc.fileList" 
  :show-file-list="false" 
  :auto-upload="false" 
  :on-change="function (file, fileList) &#123;return fileChange(file, fileList, index)&#125;"
  :multiple="false"
  :limit="1">
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就可以啦~
希望各位可以互相交流，有问题麻烦指出一下哈~🥰</p></div>  
</div>
            