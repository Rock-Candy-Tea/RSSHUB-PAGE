
---
title: '纯前端页面实现oss分片上传'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/931ea4fae0de4302b2023bf4c5a789c4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 06:02:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/931ea4fae0de4302b2023bf4c5a789c4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">1.原生的文件上传</h5>
<p>参考: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTML%2FElement%2FInput%2Ffile" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/Input/file" ref="nofollow noopener noreferrer">input type="file"</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/931ea4fae0de4302b2023bf4c5a789c4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><input id=<span class="hljs-string">"uploadValue"</span> type=<span class="hljs-string">"file"</span>  multiple=<span class="hljs-string">"multiple"</span> onchange=<span class="hljs-string">"fileChange()"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fileChange</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'uploadValue'</span>).value
  <span class="hljs-keyword">const</span> files = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'uploadValue'</span>).files
  <span class="hljs-built_in">console</span>.log(value, <span class="hljs-string">'value'</span>)  <span class="hljs-comment">// 表示选择文件的路径</span>
  <span class="hljs-built_in">console</span>.log(files, <span class="hljs-string">'files'</span>) <span class="hljs-comment">// 表示已选择文件的数组集合</span>
  <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData() 
  formData.append(<span class="hljs-string">"userfile"</span>, files[<span class="hljs-number">0</span>]) <span class="hljs-comment">//拿到第一个文件放到formData里面</span>
  <span class="hljs-built_in">console</span>.log(formData, <span class="hljs-string">'formData has file'</span>)
  <span class="hljs-keyword">const</span> res = formData.get(<span class="hljs-string">'userfile'</span>) <span class="hljs-comment">// 也能通过get去获取对应的文件,也能看到file里面有什么信息</span>
  <span class="hljs-built_in">console</span>.log(res, <span class="hljs-string">'res'</span>)
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e432d54b6994f30878c0494fe2c827e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
多文件上传,先选择,然后按住ctrl,可以选择多个,那么显示的就是已经选中n个文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5087d5f5f884506b0ad637e18aef3f4~tplv-k3u1fbpfcp-watermark.image" alt="你好呀4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">2.form表单以及formData的作用</h4>
<p>其实我们在做表单提交的时候,会用到FormData这个构造函数,那么为什么要用这个呢?</p>
<h5 data-id="heading-2">2.1 form表单</h5>
<p>参考: <br><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwangdoc.com%2Fjavascript%2Fbom%2Fform.html" target="_blank" rel="nofollow noopener noreferrer" title="https://wangdoc.com/javascript/bom/form.html" ref="nofollow noopener noreferrer">表单，FormData 对象</a> <br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Ftags%2Ftag_form.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/tags/tag_form.asp" ref="nofollow noopener noreferrer">form标签</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36883cb9c62b4a70bb7f6f8fbdb73bd4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><form action=<span class="hljs-string">"form_action.asp"</span> method=<span class="hljs-string">"get"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>First name: <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fname"</span> /></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Last name: <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"lname"</span> /></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"Submit"</span> /></span></span>
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c9f6846889480c9178133e7d354fe8~tplv-k3u1fbpfcp-watermark.image" alt="你好呀5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在点击提交的时候(type="submit")的时候,浏览器会自动将form表单里面的数据以键值对的方式,提交给服务器,但是我们平时提交,肯定不希望是浏览器自动去完成这个提交到服务器的操作,我们只需要获取到form表单里面的数据,就行了,什么时候提交到服务器,由我们自己决定,所以浏览器原生提供了 FormData 对象来完成这项工作,<code>FormData()</code>构造函数的参数是一个 DOM 的表单元素，构造函数会自动处理表单的键值对</p>
<h5 data-id="heading-3">2.2 FormData 构造函数</h5>
<p>参考定义:
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FFormData%2FFormData" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/FormData/FormData" ref="nofollow noopener noreferrer">FormData</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FFormData" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/FormData" ref="nofollow noopener noreferrer">FormData</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e91e984652b442b9be37f87c32bc21a1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在来实现,只获取表单中的数据,而不需要进行自动提交到服务器</p>
<pre><code class="hljs language-js copyable" lang="js">  <form id=<span class="hljs-string">"form"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>First name: <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fname"</span> /></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Last name: <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"lname"</span> /></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"Submit"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"getFormData()"</span> /></span></span>
  </form>
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFormData</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">const</span> data = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'form'</span>)
      <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData(data);
      <span class="hljs-built_in">console</span>.log(formData.get(<span class="hljs-string">'fname'</span>), <span class="hljs-string">'First name'</span>)
      <span class="hljs-built_in">console</span>.log(formData.get(<span class="hljs-string">'lname'</span>), <span class="hljs-string">'Last name'</span>)
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/912ecb4e49f64706a38b2227bba9fbd6~tplv-k3u1fbpfcp-watermark.image" alt="你好呀6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>FormData是一个构造函数,能够通过set去添加属性,能够通过get去获取属性</code></p>
<h4 data-id="heading-4">3.实现使用element ui两种上传方式</h4>
<h5 data-id="heading-5">3.1 利用action自动上传</h5>
<pre><code class="hljs language-js copyable" lang="js">  <el-upload
      ref=<span class="hljs-string">"upload"</span>
      <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"upload-demo"</span>
      :action=<span class="hljs-string">"getUrl()"</span>
      :headers=<span class="hljs-string">"uploadHeaders()"</span>
      :on-success=<span class="hljs-string">"uploadFile"</span>
      :on-remove=<span class="hljs-string">"handleRemove"</span>
      :before-remove=<span class="hljs-string">"beforeRemove"</span>
      :file-list=<span class="hljs-string">"fileList"</span>
      :on-exceed=<span class="hljs-string">"handleExceed"</span>
      :limit=<span class="hljs-string">"1"</span>
      accept=<span class="hljs-string">".so, .zip"</span>
    >
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>点击上传<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span></span>
    </el-upload>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getUrl</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;process.env.API_URL&#125;</span>接口名`</span>
&#125;,
<span class="hljs-function"><span class="hljs-title">uploadHeaders</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-string">'Authorization'</span>: <span class="hljs-string">`Bearer <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.token&#125;</span>`</span>,
  &#125;
&#125;,
<span class="hljs-function"><span class="hljs-title">uploadFile</span>(<span class="hljs-params">res, file, fileList</span>)</span> &#123;
  <span class="hljs-built_in">console</span>.log(res, <span class="hljs-string">'res'</span>)
  <span class="hljs-comment">//上传结果res,可以根据code判断</span>
&#125;,
<span class="hljs-function"><span class="hljs-title">beforeRemove</span>(<span class="hljs-params">file, fileList</span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$confirm(<span class="hljs-string">`确定移除 <span class="hljs-subst">$&#123;file.name&#125;</span>？`</span>)
&#125;,
<span class="hljs-function"><span class="hljs-title">handleExceed</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-built_in">this</span>.$message.warning(<span class="hljs-string">`当前限制选择1个文件，已经存在了1个文件`</span>)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要注意的是:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bd996b167aa4fb8accbcf55c8e8b6b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>前端用xhr.send(formData)上传，服务端接收body,然后后端去解析formData,所以使用post请求</code></p>
<p>服务端可以通过解析拿到对应上传的文件
我在项目中(node+sequelize)可以通过ctx.request.files拿到对应的数据
<a href="https://juejin.cn/post/6854573218679046157" target="_blank" title="https://juejin.cn/post/6854573218679046157">深入浅出 multipart/form-data</a></p>
<p>阿里云文件上传参考这篇:
<a href="https://juejin.cn/post/6844903907081060359#comment" target="_blank" title="https://juejin.cn/post/6844903907081060359#comment">vue文件上传至阿里云 ali-oss</a></p>
<h5 data-id="heading-6">3.2 自定义上传</h5>
<pre><code class="hljs language-js copyable" lang="js"> <el-upload
  ref=<span class="hljs-string">"upload"</span>
  <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"upload-demo"</span>
  action=<span class="hljs-string">""</span>
  :http-request=<span class="hljs-string">"customerHttp"</span>
  :on-remove=<span class="hljs-string">"handleRemove"</span>
  :before-remove=<span class="hljs-string">"beforeRemove"</span>
  :file-list=<span class="hljs-string">"fileList"</span>
  :on-exceed=<span class="hljs-string">"handleExceed"</span>
  :limit=<span class="hljs-string">"1"</span>
  accept=<span class="hljs-string">".so, .zip"</span>
>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>点击上传<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span></span>
</el-upload>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">packageFile</span>: <span class="hljs-string">''</span>,
    &#125;
&#125;
<span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">customerHttp</span>(<span class="hljs-params">item</span>)</span> &#123;
      <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData()
      formData.append(<span class="hljs-string">'file'</span>, item.file)
      <span class="hljs-comment">// 如果直接上传就不用存储,如果等按确定按钮,就需要存储</span>
      <span class="hljs-built_in">this</span>.packageFile = formData
      <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> uploadFile(<span class="hljs-built_in">this</span>.packageFile).catch(<span class="hljs-function">() =></span> <span class="hljs-literal">false</span>)
      <span class="hljs-built_in">console</span>.log(res)
    &#125;,
    <span class="hljs-comment">// 删除了之后 应该把this.packageFile进行清空</span>
    <span class="hljs-function"><span class="hljs-title">handleRemove</span>(<span class="hljs-params">file, fileList</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (fileList.length === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.packageFile = <span class="hljs-string">''</span>
      &#125;
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">4.大文件分片上传(element ui 纯前端实现)</h4>
<p><a href="https://juejin.cn/post/6956172874348986382" target="_blank" title="https://juejin.cn/post/6956172874348986382">知识点汇总</a> <br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fwujize%2Farticle%2Fdetails%2F107411243" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/wujize/article/details/107411243" ref="nofollow noopener noreferrer">VUE前端分片直传大文件到OSS方法</a><br>
<a href="https://juejin.cn/post/6844903991806197767" target="_blank" title="https://juejin.cn/post/6844903991806197767">阿里云OSS文件上传（分片上传、断点续传）前后端实现</a></p>
<p>一定要看api <a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument_detail%2F111268.html%3Fspm%3Da2c4g.11186623.6.1099.139926fdNt8n5M" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document_detail/111268.html?spm=a2c4g.11186623.6.1099.139926fdNt8n5M" ref="nofollow noopener noreferrer">分片上传官方案例(node.js)</a><br></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfead1c879014a8798eb7c1d6b313a9d~tplv-k3u1fbpfcp-watermark.image" alt="你好呀8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>模拟两个文件上传,都是205兆,为什么要分片上传?</p>
<p>之前我们上传的文件,是大概几十兆,所以上传虽然慢了点,也不是不能忍,但是后面兆数增加到400多兆,因为之前文件上传到oss,是在node端处理的,但是node.js有2分钟超时限制,所以为了减少node层转换,直接采用在前端进行oss上传</p>
<h5 data-id="heading-8">1.template</h5>
<pre><code class="hljs language-js copyable" lang="js"><el-upload
  ref=<span class="hljs-string">"upload"</span>
  <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"upload-demo"</span>
  action=<span class="hljs-string">""</span>
  :http-request=<span class="hljs-string">"customerHttp"</span>
  :on-remove=<span class="hljs-string">"handleRemove"</span>
  :before-remove=<span class="hljs-string">"beforeRemove"</span>
  :file-list=<span class="hljs-string">"fileList"</span>
  :on-exceed=<span class="hljs-string">"handleExceed"</span>
  :limit=<span class="hljs-string">"1"</span>
  accept=<span class="hljs-string">".so, .zip"</span>
>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>点击上传<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span></span>
</el-upload>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"padding: 10px 10px 10px 0px; width: 320px"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-progress</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"percentage"</span> <span class="hljs-attr">:text-inside</span>=<span class="hljs-string">"true"</span>
  <span class="hljs-attr">:stroke-width</span>=<span class="hljs-string">"24"</span> <span class="hljs-attr">:percentage</span>=<span class="hljs-string">"percentage"</span> <span class="hljs-attr">status</span>=<span class="hljs-string">"success"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">2. 数据定义</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> moment <span class="hljs-keyword">from</span> <span class="hljs-string">'moment'</span>
<span class="hljs-keyword">import</span> OSS <span class="hljs-keyword">from</span> <span class="hljs-string">'ali-oss'</span>
<span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> OSS(&#123;
  <span class="hljs-attr">region</span>: <span class="hljs-string">'xxxxx'</span>,
  <span class="hljs-attr">accessKeyId</span>: <span class="hljs-string">'xxxxx'</span>,
  <span class="hljs-attr">accessKeySecret</span>: <span class="hljs-string">'xxxxx'</span>,
  <span class="hljs-attr">endpoint</span>: <span class="hljs-string">'xxxxx'</span>,
  <span class="hljs-attr">bucket</span>: <span class="hljs-string">'xxxxxx'</span>,
&#125;)
<span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">percentage</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">savaData</span>: &#123;&#125;,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在node端去拿配置项,那么可以直接在config.local.js文件里面去定义ossConfig配置项,如果是纯前端实现的话,肯定不能直接定义(很不安全),要从接口拿,我是模拟,所以直接在页面写了</p>
<blockquote>
<p>const res = await this.sts.assumeRole(<code>acs:ram::$&#123;accountId&#125;:role/$&#123;roleName&#125;</code>, 'SessionTest')</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a826816b08845f9818e45b9ebc2eee5~tplv-k3u1fbpfcp-watermark.image" alt="1627215411(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-10">3.分片上传参数获取</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">customerHttp</span>(<span class="hljs-params">item</span>)</span> &#123;
  <span class="hljs-comment">// 拿到上传到的file</span>
  <span class="hljs-keyword">const</span> uploadFile = item.file
  <span class="hljs-comment">// 拿到上传的size</span>
  <span class="hljs-keyword">const</span> uploadFileSize = uploadFile.size <span class="hljs-comment">// 这里拿到的单位是字节(uploadFileSize/ 1024 / 1024</span>
  <span class="hljs-comment">// = 多少兆)</span>
  <span class="hljs-comment">// 设置每一片的大小,partSize 指定上传的每个分片的大小，范围为100 KB~5 GB。</span>
  <span class="hljs-keyword">const</span> partSize = <span class="hljs-built_in">Math</span>.ceil(uploadFileSize / <span class="hljs-number">1024</span> / <span class="hljs-number">1024</span> / <span class="hljs-number">1000</span>) * <span class="hljs-number">1024</span> * <span class="hljs-number">1024</span>
  <span class="hljs-comment">// 设置所有的文件上传所有的唯一的saveFileId</span>
  <span class="hljs-keyword">const</span> &#123; name, size, lastModified, type &#125; = uploadFile
  <span class="hljs-keyword">const</span> saveFileId = <span class="hljs-string">`<span class="hljs-subst">$&#123;lastModified&#125;</span>_<span class="hljs-subst">$&#123;size&#125;</span>_<span class="hljs-subst">$&#123;name&#125;</span>_<span class="hljs-subst">$&#123;type&#125;</span>`</span>
  <span class="hljs-built_in">this</span>.multipartUpload(partSize, saveFileId, uploadFile)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>partSize可以根据业务需求设定,最好就是设定一个最大的片数,看node的官方的例子是1000片,我这里设置最大的片数也是1000片,所以我的逻辑是如果超过1000片,我就将兆数放大,如果小于1000片,我就还是使用1兆,<code>Math.ceil(uploadFileSize / 1024 / 1024 / 1000)</code>是为了知道是不是大于1000片</p>
<p>为什么我要去创建一个<code>saveFileId</code>,可以叫做他文件的唯一的id,其实我看过很多例子,很多人的断点续传只做到了我传a文件,网页崩了,我再续传a文件,而我这里去创建saveFileId是为了,我传a文件,网页崩了,我又传b文件,网页崩了,过一会,我再传a文件或者b文件都要有续存的效果,所以我会将文件的信息形成唯一的id进行存储,然后放到内存里面,将所有的中断信息变成一个对象存储,对象的key是saveFileId(文件唯一的信息)</p>
<h5 data-id="heading-11">4.分片上传</h5>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">multipartUpload</span>(<span class="hljs-params">partSize, saveFileId, uploadFile</span>)</span> &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// object-name目前我是用的uploadFile.name,其实也是要根据你们的项目而定,</span>
        有没有具体的规定,要不要加项目名,要不要加对应的环境
        <span class="hljs-comment">// 上传的参数</span>
        <span class="hljs-keyword">const</span> uploadParams = &#123;
          partSize,
          <span class="hljs-attr">progress</span>: <span class="hljs-function">(<span class="hljs-params">percentage, checkpoint</span>) =></span> &#123;
            <span class="hljs-built_in">this</span>.savaData[saveFileId] = checkpoint
            <span class="hljs-built_in">console</span>.log(checkpoint)
            <span class="hljs-built_in">this</span>.savaData[<span class="hljs-string">'lastSaveTime'</span>] = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
            <span class="hljs-built_in">this</span>.percentage = <span class="hljs-built_in">parseInt</span>(percentage * <span class="hljs-number">100</span>)
            <span class="hljs-comment">// 在上传过程中,把已经上传的数据存储下来</span>
            <span class="hljs-built_in">this</span>.saveFinishedData(<span class="hljs-built_in">this</span>.savaData)
          &#125;,
        &#125;
        <span class="hljs-comment">// 断点续传</span>
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.resumeUpload(uploadParams, saveFileId)
        <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">res</span>: &#123; status &#125;&#125; = <span class="hljs-keyword">await</span> client.multipartUpload(uploadFile.name, 
        uploadFile, uploadParams)
        <span class="hljs-keyword">if</span> (status === <span class="hljs-number">200</span>) &#123;
          <span class="hljs-comment">// 重新去掉某个缓存进行设置</span>
          <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.savaData[saveFileId]
          <span class="hljs-built_in">this</span>.saveFinishedData(<span class="hljs-built_in">this</span>.savaData)
        &#125;
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-comment">// 捕获超时异常。</span>
        <span class="hljs-keyword">if</span> (e.code === <span class="hljs-string">'ConnectionTimeoutError'</span>) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'TimeoutError'</span>)
          <span class="hljs-comment">// do ConnectionTimeoutError operation</span>
        &#125;
      &#125;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很多人说进度条不能实时更新,其实是因为别人的例子,直接用的function,无法改变父级的this.percentage,所以这里应该用箭头函数<code>(percentage, checkpoint) =></code></p>
<h5 data-id="heading-12">5.断点续传</h5>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">resumeUpload</span>(<span class="hljs-params">uploadParams, saveFileId</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'upload-function-name'</span>)) &#123;
        <span class="hljs-keyword">const</span> obj = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'upload-function-name'</span>))
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.keys(obj).includes(saveFileId)) &#123;
          uploadParams.checkpoint = obj[saveFileId]
        &#125;
      &#125;
    &#125;,
    <span class="hljs-comment">// 存储到内存</span>
   <span class="hljs-function"><span class="hljs-title">saveFinishedData</span>(<span class="hljs-params">finishedData</span>)</span> &#123;
      <span class="hljs-built_in">localStorage</span>.setItem(
        <span class="hljs-string">'upload-function-name'</span>,
        <span class="hljs-built_in">JSON</span>.stringify(finishedData)
      )
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5e0aab25d2c492ba78f78c5e2d341cf~tplv-k3u1fbpfcp-watermark.image" alt="1627220519(1).png" loading="lazy" referrerpolicy="no-referrer">
主要是判断内存里面的文件和我现在上传文件是不是一致.是的话把对应的checkpoint传过去</p>
<p>upload-function-name这个名字,我觉得按照功能随便取个名字就好</p>
<h5 data-id="heading-13">6.初始化拿到内存里面的数据</h5>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.initPage()
 &#125;,
 <span class="hljs-attr">methods</span>: &#123;
  <span class="hljs-function"><span class="hljs-title">initPage</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 判断是不是有缓存</span>
      <span class="hljs-keyword">const</span> localData = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'upload-function-name'</span>)
      <span class="hljs-keyword">if</span> (!localData) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">this</span>.savaData = <span class="hljs-built_in">JSON</span>.parse(localData)
      <span class="hljs-comment">// 当前时间 > 存储时间(1000 * 60 * 60表示1h,意思就是这些数据你要存多久,</span>
      <span class="hljs-comment">// 可以是1h也可以是多少天,随意)</span>
      <span class="hljs-keyword">if</span> (moment(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()).diff(moment(<span class="hljs-built_in">this</span>.savaData.lastSaveTime)) > <span class="hljs-number">1000</span> * <span class="hljs-number">60</span> * <span class="hljs-number">60</span>) &#123;
        <span class="hljs-built_in">localStorage</span>.removeItem(<span class="hljs-string">'upload-function-name'</span>)
      &#125;
    &#125;,
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">7.知识点梳理</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> 分片上传,主要是把一个大文件,分成一小片上传,而按道理,后端应该把前端传的一片片合起来,这一步阿里云帮我们做了
<span class="hljs-number">2.</span> oss上传中,同一个文件,用saveFileId做文件的唯一标识
<span class="hljs-number">3.</span> 因为想要做到多个文件中断,都能够进行分别续存,所以将这些信息存到内存里面
<span class="hljs-number">4.</span> 只要上传成功了,应该将对应的内存中的信息删除
<span class="hljs-number">5.</span> 为了不让上传信息一直停留在内存,做了一个定期的删除
<span class="hljs-number">6.</span> doneParts 是已经上传的片数的集合
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">8.开发过程中一些思考(可不看)</h5>
<p>在做分片续存这里,<code>首先我在想checkpoint是什么?我靠什么信息知道哪些已经上传了,哪些没上传,是只用把中断的最后一片知道了就行了嘛,checkpoint是上传每一片的信息嘛?</code>我以为checkpoint每次打印出来,应该uploadId是不一样的,每个checkpoint表示的是已上传的那一片,结果我错了,或者我觉得至少每个checkpoint有个东西完全不一样,<code>结果每次上传完了</code>,我去看checkpoint,好像每个都一样(我查了后面几十个都一样)</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1dac27e9fba4654952d8e5825e442df~tplv-k3u1fbpfcp-watermark.image" alt="1627217629(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0444a0665fb1441eb9a0a0927557b004~tplv-k3u1fbpfcp-watermark.image" alt="04b02e2e68d0cb8890c6abcf64fd41b.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>于是我很困惑,这没有一个标志值怎么搞?看了看源码:
checkpoint 返回的数据:</p>
<blockquote>
<p>file 就是我们传的file <br> fileSize 也就是文件总大小 <br> name文件名  <br> partSize也就是我们传的portSize,没有就是1兆</p>
</blockquote>
<p>那么uploadId是不是唯一的呢?是代表了每一片的上传了的id还是说只要是这个文件上传,所有的uploadId是一样的呢?答案就是只要是同一个文件上传,uploadId是一致的,不是代表每一片</p>
<p>源码:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7450b82069a5417290c4494d2ef9095f~tplv-k3u1fbpfcp-watermark.image" alt="1627218644(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7e617c11bed440aba12ceca6ca679af~tplv-k3u1fbpfcp-watermark.image" alt="1627218810(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一次创建uploadId还是根据前端传的参数name和options,在上传调用时,这些参数都是不变的,所以不管request里面怎么写,uploadId应该是根据name和option出来的一个唯一值,所以我存储的断点以上提到的几个数都是固定的,那么唯一有可能变化的就是doneParts</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36b0c2cf12404c5ab94e05bf424e79d6~tplv-k3u1fbpfcp-watermark.image" alt="1627219147(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>源码证明,变化的应该是doneParts,而为什么我所有的数据doneParts都是206片呢???其实是因为我每次去分析数据都是全部上传完看最后的那些数据,只有在上传的过程中,整个doneParts的数量才是按照0->206从小到大数组在变化,而结束后的打印是没有规律的,大部分变成了206片,这里的原因还没有搞懂。。。。</p>
<p>因为doneParts上传中规律增加,中断时,我们把对应的checkpoint存储,oss解析到传过来的checkpoint.uploadId与当前传的一致就会进行续存.</p>
<p>开心每一天-_-</p></div>  
</div>
            