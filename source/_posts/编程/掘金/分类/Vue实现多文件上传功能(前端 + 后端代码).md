
---
title: 'Vue实现多文件上传功能(前端 + 后端代码)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3b5d7827c014ec9b0b0f733904efdfb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 19:23:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3b5d7827c014ec9b0b0f733904efdfb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<p><strong>本人业余前端开发，因为公司(很坑)觉得我很牛逼，所以让我前后端一起玩，无奈的我只能磕磕碰碰的研究起了vue</strong>。</p>
<p>开发项目的时候，用到文件上传的功能很常见，包括单文件上传和多文件上传，上传各种类型的文件。在vue里面要实现多文件上传功能，还是很方便的。</p>
<p>本文就一起来学习一下，如何把多文件上传功能封装成一个组件，后面需要使用的时候，直接两三行代码就能搞定。</p>
<h3 data-id="heading-0">1、前端代码</h3>
<p>首先我们先看前端，如何把它封装成一个组件。我们在调用它的时候，可能需要从外部传入一些参数给它，所以我们需要定义一些传入参数。这些参数我们可以放到props里面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 值</span>
    <span class="hljs-attr">value</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Object</span>, <span class="hljs-built_in">Array</span>],
    <span class="hljs-comment">// 大小限制(MB)</span>
    <span class="hljs-attr">fileSize</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-number">2</span>,
    &#125;,
    <span class="hljs-comment">// 文件类型, 例如['png', 'jpg', 'jpeg']</span>
    <span class="hljs-attr">fileType</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> [<span class="hljs-string">".jpg"</span>, <span class="hljs-string">".jpeg"</span>, <span class="hljs-string">".png"</span>, <span class="hljs-string">".doc"</span>, <span class="hljs-string">".xls"</span>, <span class="hljs-string">".xlsx"</span>, <span class="hljs-string">".ppt"</span>, <span class="hljs-string">".txt"</span>, <span class="hljs-string">".pdf"</span>],
    &#125;,
    <span class="hljs-comment">// 是否显示提示</span>
    <span class="hljs-attr">isShowTip</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-comment">// 单据id</span>
    <span class="hljs-attr">billId</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">require</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-comment">// 单据类型</span>
    <span class="hljs-attr">billType</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面定义了一些文件大小，文件类型等，如果没有传入，则为默认值。单据类型和单据id是必须要传入的，这里可以依照实际开发需要进行定义即可。</p>
<p>文件上传组件，我们可以使用element的<code>el-upload</code>，在页面引入，我们点击后一般唤醒的是一个文件上传弹窗，可以使用<code>el-dialog</code>标签包围。完整代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-dialog</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"附件上传"</span> <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"visible"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"800px"</span> <span class="hljs-attr">:close-on-click-modal</span>=<span class="hljs-string">"false"</span> @<span class="hljs-attr">close</span>=<span class="hljs-string">"cancel"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"upload-file"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-upload</span>
        <span class="hljs-attr">:action</span>=<span class="hljs-string">"action"</span>
        <span class="hljs-attr">:before-upload</span>=<span class="hljs-string">"handleBeforeUpload"</span>
        <span class="hljs-attr">:file-list</span>=<span class="hljs-string">"fileList"</span>
        <span class="hljs-attr">:limit</span>=<span class="hljs-string">"3"</span>
        <span class="hljs-attr">multiple</span>
        <span class="hljs-attr">:accept</span>=<span class="hljs-string">"accept"</span>
        <span class="hljs-attr">:on-error</span>=<span class="hljs-string">"handleUploadError"</span>
        <span class="hljs-attr">:on-exceed</span>=<span class="hljs-string">"handleExceed"</span>
        <span class="hljs-attr">:on-success</span>=<span class="hljs-string">"handleUploadSuccess"</span>
        <span class="hljs-attr">:on-change</span>=<span class="hljs-string">"handChange"</span>
        <span class="hljs-attr">:http-request</span>=<span class="hljs-string">"httpRequest"</span>
        <span class="hljs-attr">:show-file-list</span>=<span class="hljs-string">"true"</span>
        <span class="hljs-attr">:auto-upload</span>=<span class="hljs-string">"false"</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"upload-file-uploader"</span>
        <span class="hljs-attr">ref</span>=<span class="hljs-string">"upload"</span>
      ></span>
        <span class="hljs-comment"><!-- 上传按钮 --></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"trigger"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>选取文件<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-left: 10px;"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"fileList.length < 1"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitUpload"</span>></span>上传到服务器<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-comment"><!-- 上传提示 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-upload__tip"</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"tip"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"showTip"</span>></span>
          请上传
          <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"fileSize"</span>></span> 大小不超过 <span class="hljs-tag"><<span class="hljs-name">b</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: #f56c6c"</span>></span>&#123;&#123; fileSize &#125;&#125;MB<span class="hljs-tag"></<span class="hljs-name">b</span>></span> <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"fileType"</span>></span> 格式为 <span class="hljs-tag"><<span class="hljs-name">b</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: #f56c6c"</span>></span>&#123;&#123; fileType.join("/") &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">b</span>></span> <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          的文件
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-upload</span>></span>

      <span class="hljs-comment"><!-- 文件列表 --></span>
      <span class="hljs-tag"><<span class="hljs-name">transition-group</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"upload-file-list el-upload-list el-upload-list--text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"el-fade-in-linear"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"ul"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"file.uid"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-upload-list__item ele-upload-list__item-content"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(file, index) in list"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-link</span> <span class="hljs-attr">:href</span>=<span class="hljs-string">"file.url"</span> <span class="hljs-attr">:underline</span>=<span class="hljs-string">"false"</span> <span class="hljs-attr">target</span>=<span class="hljs-string">"_blank"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-document"</span>></span> &#123;&#123; getFileName(file.name) &#125;&#125; <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-link</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ele-upload-list__item-content-action"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-link</span> <span class="hljs-attr">:underline</span>=<span class="hljs-string">"false"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleDelete(index)"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">el-link</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">transition-group</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面用到的几个变量，我们需要在data里面定义</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 已选择文件列表</span>
      <span class="hljs-attr">fileList</span>: [],
      <span class="hljs-comment">// 是否显示文件上传弹窗</span>
      <span class="hljs-attr">visible</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-comment">// 可上传的文件类型</span>
      <span class="hljs-attr">accept</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">action</span>: <span class="hljs-string">'action'</span>
    &#125;;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>accept</code>字段需要在页面创建后，通过传入或默认的<code>fileType</code>字段进行拼接得到</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.fileList = <span class="hljs-built_in">this</span>.list
    <span class="hljs-comment">// 拼接</span>
    <span class="hljs-built_in">this</span>.fileType.forEach(<span class="hljs-function"><span class="hljs-params">el</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.accept += el
      <span class="hljs-built_in">this</span>.accept += <span class="hljs-string">','</span>
    &#125;)
    <span class="hljs-built_in">this</span>.fileType.slice(<span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.fileList.length - <span class="hljs-number">2</span>)
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就是文件上传相关的方法，这里我们使用选择文件后手动上传的方式，请看下面的代码</p>
<pre><code class="hljs language-js copyable" lang="js"><el-upload
        :action=<span class="hljs-string">"action"</span>  <span class="hljs-comment">// 手动上传，这个参数没有用，但因为是必填的，所以随便填一个值就行</span>
        :before-upload=<span class="hljs-string">"handleBeforeUpload"</span>  <span class="hljs-comment">// 文件上传之前进行的操作</span>
        :file-list=<span class="hljs-string">"fileList"</span>   <span class="hljs-comment">// 已选择文件列表</span>
        :limit=<span class="hljs-string">"3"</span>   <span class="hljs-comment">// 一次最多上传几个文件</span>
        multiple   <span class="hljs-comment">// 可以多选</span>
        :accept=<span class="hljs-string">"accept"</span>   <span class="hljs-comment">// 可以上传的文件类型</span>
        :on-error=<span class="hljs-string">"handleUploadError"</span>   <span class="hljs-comment">// 上传出错时调用</span>
        :on-exceed=<span class="hljs-string">"handleExceed"</span>   <span class="hljs-comment">// 文件数量超过限制时调用</span>
        :on-success=<span class="hljs-string">"handleUploadSuccess"</span>   <span class="hljs-comment">// 上传成功时调用</span>
        :on-change=<span class="hljs-string">"handChange"</span>   <span class="hljs-comment">// 文件发生变化时调用</span>
        :http-request=<span class="hljs-string">"httpRequest"</span>   <span class="hljs-comment">// 自定义的文件上传方法，我们手动点击上传按钮后会调用</span>
        :show-file-list=<span class="hljs-string">"true"</span>   <span class="hljs-comment">// 是否显示文件列表</span>
        :auto-upload=<span class="hljs-string">"false"</span>   <span class="hljs-comment">// 关闭自动上传</span>
        <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"upload-file-uploader"</span> 
        ref=<span class="hljs-string">"upload"</span>
      >

<!-- 上传按钮 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"trigger"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>选取文件<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-left: 10px;"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"fileList.length < 1"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitUpload"</span>></span>上传到服务器<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击上传到服务器后，就触发<code>submitUpload</code>调用我们自定义的方法。</p>
<p>注意这里选取文件的按钮需要加上<code>slot="trigger"</code>属性，不然点击上传到服务器按钮后，也会触发选择文件弹框。</p>
<p>接下来看相关的方法</p>
<pre><code class="hljs language-js copyable" lang="js">methods: &#123;
<span class="hljs-comment">// 外部调用这个方法，显示文件上传弹窗</span>
    <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.visible = <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-comment">// 上传前校检格式和大小</span>
    <span class="hljs-function"><span class="hljs-title">handleBeforeUpload</span>(<span class="hljs-params">file</span>)</span> &#123;
      <span class="hljs-comment">// 校检文件类型</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.fileType) &#123;
        <span class="hljs-keyword">let</span> fileExtension = <span class="hljs-string">""</span>;
        <span class="hljs-keyword">if</span> (file.name.lastIndexOf(<span class="hljs-string">"."</span>) > -<span class="hljs-number">1</span>) &#123;
          fileExtension = file.name.slice(file.name.lastIndexOf(<span class="hljs-string">"."</span>));
        &#125;
        <span class="hljs-keyword">const</span> isTypeOk = <span class="hljs-built_in">this</span>.fileType.some(<span class="hljs-function">(<span class="hljs-params">type</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (file.type.indexOf(type) > -<span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
          <span class="hljs-keyword">if</span> (fileExtension && fileExtension.indexOf(type) > -<span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;);
        <span class="hljs-keyword">if</span> (!isTypeOk) &#123;
          <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">`文件格式不正确, 请上传<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.fileType.join(<span class="hljs-string">"/"</span>)&#125;</span>格式文件!`</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;
      &#125;
      <span class="hljs-comment">// 校检文件大小</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.fileSize) &#123;
        <span class="hljs-keyword">const</span> isLt = file.size / <span class="hljs-number">1024</span> / <span class="hljs-number">1024</span> < <span class="hljs-built_in">this</span>.fileSize;
        <span class="hljs-keyword">if</span> (!isLt) &#123;
          <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">`上传文件大小不能超过 <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.fileSize&#125;</span> MB!`</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;,
    <span class="hljs-comment">// 文件个数超出</span>
    <span class="hljs-function"><span class="hljs-title">handleExceed</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">`只允许上传3个文件`</span>);
    &#125;,
    <span class="hljs-comment">// 上传失败</span>
    <span class="hljs-function"><span class="hljs-title">handleUploadError</span>(<span class="hljs-params">err</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">"上传失败, 请重试"</span>);
    &#125;,
    <span class="hljs-comment">// 上传成功回调</span>
    <span class="hljs-function"><span class="hljs-title">handleUploadSuccess</span>(<span class="hljs-params">res, file</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$message.success(<span class="hljs-string">"上传成功"</span>);
      <span class="hljs-built_in">this</span>.cancel()
    &#125;,
    <span class="hljs-comment">/** 文件状态改变时调用 */</span>
    <span class="hljs-function"><span class="hljs-title">handChange</span>(<span class="hljs-params">file, fileList</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.fileList = fileList
    &#125;,
    <span class="hljs-comment">// 删除文件</span>
    <span class="hljs-function"><span class="hljs-title">handleDelete</span>(<span class="hljs-params">index</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.fileList.splice(index, <span class="hljs-number">1</span>);
    &#125;,
    <span class="hljs-comment">// 获取文件名称</span>
    <span class="hljs-function"><span class="hljs-title">getFileName</span>(<span class="hljs-params">name</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (name.lastIndexOf(<span class="hljs-string">"/"</span>) > -<span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">return</span> name.slice(name.lastIndexOf(<span class="hljs-string">"/"</span>) + <span class="hljs-number">1</span>).toLowerCase();
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>;
      &#125;
    &#125;,
    <span class="hljs-comment">/** 手动提交上传 */</span>
    <span class="hljs-function"><span class="hljs-title">submitUpload</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.fileList.length <= <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      <span class="hljs-built_in">this</span>.$refs.upload.submit()
    &#125;,
    <span class="hljs-comment">/** 关闭上传弹框 */</span>
    <span class="hljs-function"><span class="hljs-title">cancel</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.fileList = []
      <span class="hljs-built_in">this</span>.visible = <span class="hljs-literal">false</span>
    &#125;,
    <span class="hljs-comment">/** 调用接口上传 */</span>
    <span class="hljs-function"><span class="hljs-title">httpRequest</span>(<span class="hljs-params">param</span>)</span> &#123;
      <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData()
      formData.append(<span class="hljs-string">"billId"</span>, <span class="hljs-built_in">this</span>.billId)
      formData.append(<span class="hljs-string">"formType"</span>, <span class="hljs-built_in">this</span>.billType)
      formData.append(<span class="hljs-string">'file'</span>, param.file)
      uploadFormFile(formData).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">if</span>(res.code === <span class="hljs-number">200</span>)&#123;
          <span class="hljs-comment">// 自定义上传时，需自己执行成功回调函数</span>
          param.onSuccess()
          <span class="hljs-built_in">this</span>.$refs.upload.clearFiles()
          <span class="hljs-built_in">this</span>.msgSuccess(<span class="hljs-string">"上传成功"</span>)
          <span class="hljs-comment">// 回调方法，文件上传成功后，会调用`input`指定的方法，在调用方定义</span>
          <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"input"</span>, res.data)
        &#125;
      &#125;).catch(<span class="hljs-function">(<span class="hljs-params">err</span>)=></span>&#123;&#125;)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他方法都还好，主要看看这个<code>httpRequest</code>方法，如果直接使用url的方式进行调用，会出现跨域问题，你需要把token放到请求头里。我这里是通过封装后的api接口进行调用的，已经做了全局的token验证，所以只需要把相关的参数带上即可。</p>
<p>使用<code>formData </code>带上需要的参数。上传成功后，使用<code>this.$emit("input", res.data)</code>执行上传成功后的逻辑。</p>
<p>这就封装好了一个文件上传的组件，接下来看看怎么使用。</p>
<h3 data-id="heading-1">2、使用组件</h3>
<p>在使用的页面，首先需要引入组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> FileUpload <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/FileUpload'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再页面内进行调用</p>
<pre><code class="hljs language-js copyable" lang="js"><file-upload ref=<span class="hljs-string">"fileUploadDialog"</span> :billId=<span class="hljs-string">"this.form.noticeId"</span> :billType=<span class="hljs-string">"10"</span> @input=<span class="hljs-string">"getAttachList"</span>></file-upload>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>billId</code>和<code>billType</code>是我们动态传入的参数，其他的参数使用默认值，<code>getAttachList</code>方法在文件上传成功后执行。</p>
<p>我们需要一个按钮唤醒文件上传框</p>
<pre><code class="hljs language-js copyable" lang="js"><el-button
       type=<span class="hljs-string">"primary"</span>
       plain
       icon=<span class="hljs-string">"el-icon-plus"</span>
       size=<span class="hljs-string">"mini"</span>
       @click=<span class="hljs-string">"handleAdd"</span>
       :disabled=<span class="hljs-string">"notEdit"</span>
     >上传</el-button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义<code>hangAdd</code>方法，直接调用组件里定义的<code>show</code>方法即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">handleAdd</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-built_in">this</span>.$refs.fileUploadDialog.show()
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后定义文件上传成功后的方法，获取已上传文件列表即可。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-title">getAttachList</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>
   <span class="hljs-built_in">this</span>.attachQuery.billId = <span class="hljs-built_in">this</span>.form.noticeId
   <span class="hljs-built_in">this</span>.attachQuery.billType = <span class="hljs-number">10</span>
   listAttachment(<span class="hljs-built_in">this</span>.attachQuery).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
     <span class="hljs-built_in">this</span>.attachList = response.rows
     <span class="hljs-built_in">this</span>.attachList.forEach(<span class="hljs-function"><span class="hljs-params">el</span> =></span> &#123;
       <span class="hljs-comment">// 转为kb，取小数点后2位</span>
       el.fileSize = <span class="hljs-built_in">parseFloat</span>(el.fileSize / <span class="hljs-number">1024</span>).toFixed(<span class="hljs-number">2</span>)
     &#125;)
     <span class="hljs-built_in">this</span>.attachTotal = response.total
     <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">false</span>
   &#125;).catch(<span class="hljs-function">() =></span> &#123;&#125;)
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里前端代码就大功告成了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3b5d7827c014ec9b0b0f733904efdfb~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">3、后端代码</h3>
<p>我这里选择上传图片到阿里云服务器，上传到哪里不重要</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 单据附件上传
 * <span class="hljs-doctag">@param</span> billId 单据id
 * <span class="hljs-doctag">@param</span> formType 单据类型
 * <span class="hljs-doctag">@param</span> file 上传的文件
 * <span class="hljs-doctag">@return</span>
 * <span class="hljs-doctag">@throws</span> Exception
 */</span>
<span class="hljs-meta">@PostMapping("/form/attachment/upload")</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> AjaxResult <span class="hljs-title">uploadFormFile</span><span class="hljs-params">(<span class="hljs-meta">@RequestParam(value = "billId")</span> Long billId,
                             <span class="hljs-meta">@RequestParam(value = "formType")</span> Integer formType,
                             <span class="hljs-meta">@RequestParam("file")</span> MultipartFile[] file)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 文件上传后的路径</span>
        List<String> pathList = <span class="hljs-keyword">new</span> ArrayList<>();

        <span class="hljs-keyword">for</span> (MultipartFile f : file) &#123;
            <span class="hljs-keyword">if</span> (!f.isEmpty()) &#123;
                <span class="hljs-comment">// 调用接口上传照片</span>
                AjaxResult result = uploadService.uploadFormFile(f, billId, formType);
                <span class="hljs-keyword">if</span> (!result.get(<span class="hljs-string">"code"</span>).toString().equals(<span class="hljs-string">"200"</span>)) &#123;
                    <span class="hljs-keyword">return</span> AjaxResult.error(<span class="hljs-string">"上传文件异常，请联系管理员"</span>);
                &#125;
                pathList.add(result.get(<span class="hljs-string">"data"</span>).toString());
            &#125;
        &#125;

        <span class="hljs-comment">// 返回图片路径</span>
        <span class="hljs-keyword">return</span> AjaxResult.success(pathList);
    &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
        <span class="hljs-keyword">return</span> AjaxResult.error(e.getMessage());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们使用一个<code>MultipartFile</code>数组接受文件，然后调用方法判断文件的一些属性上传文件即可，具体的上传方法这里就不贴了，各有不同，具体情况具体分析。</p>
<p>到这里，本文就ok了。关于MIME 类型列表，可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Fmedia%2Fmedia_mimeref.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/media/media_mimeref.asp" ref="nofollow noopener noreferrer">点击这里</a>查看。如果过程中遇到什么问题，可以在下方留言，我会回复的。</p>
<h5 data-id="heading-3">觉得好的可以帮忙点个赞啊，也可以关注我的公众号【秃头哥编程】</h5></div>  
</div>
            