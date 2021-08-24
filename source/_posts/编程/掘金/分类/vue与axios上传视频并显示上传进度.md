
---
title: 'vue与axios上传视频并显示上传进度'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ea62434178c4a48bcc4194c38a9a115~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 23:02:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ea62434178c4a48bcc4194c38a9a115~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>做项目难免会有各种各样的需求,这次是上传视频并显示上传进度,好的我们开始吧
首先先引入axios,我这里是单文件引入,没有使用封装</p>
<pre><code class="hljs language-php copyable" lang="php">import axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要用到的参数有</p>
<pre><code class="hljs language-c++ copyable" lang="c++">      exception: <span class="hljs-string">'-'</span>, <span class="hljs-comment">//进度条当前状态</span>
      videolist: [], <span class="hljs-comment">// 视频合集</span>
      progress: <span class="hljs-number">0</span>, <span class="hljs-comment">// 进度条</span>
      video: <span class="hljs-string">'',  // 保存预览地址
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>需要个触发选择文件上传的按钮
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ea62434178c4a48bcc4194c38a9a115~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
这里用的element做为布局</p>
<pre><code class="hljs language-php copyable" lang="php">   <el-form-item label=<span class="hljs-string">"视频"</span>>
        <div>
        <span class="hljs-comment">//限制上传完成才能上传下一个</span>
          <label v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"progress === 0"</span> <span class="hljs-class"><span class="hljs-keyword">class</span>="<span class="hljs-title">btn</span>" <span class="hljs-title">for</span>="<span class="hljs-title">uploadvideo</span>">上传视频</<span class="hljs-title">label</span>>
          <<span class="hljs-title">label</span> <span class="hljs-title">v</span>-<span class="hljs-title">else</span> <span class="hljs-title">class</span>="<span class="hljs-title">btn</span>" @<span class="hljs-title">click</span>="<span class="hljs-title">uploading</span>">上传视频</<span class="hljs-title">label</span>>
          <<span class="hljs-title">input</span>
            <span class="hljs-title">id</span>="<span class="hljs-title">uploadvideo</span>"
            <span class="hljs-title">style</span>="<span class="hljs-title">display</span>:<span class="hljs-title">none</span>;"
            <span class="hljs-title">type</span>="<span class="hljs-title">file</span>"
            <span class="hljs-title">accept</span>="<span class="hljs-title">video</span>/*"
            @<span class="hljs-title">change</span>="<span class="hljs-title">selectvideo</span>($<span class="hljs-title">event</span>)"
          >
        </<span class="hljs-title">div</span>>
      </<span class="hljs-title">el</span>-<span class="hljs-title">form</span>-<span class="hljs-title">item</span>>

</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift">  <span class="hljs-comment">// 未上传完成阻止</span>
    uploading() &#123;
      this.<span class="hljs-variable">$message</span>(&#123;
        message: '请等待上传完成',
        type: 'error'
      &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>accept(选择的文件格式),点击上传之后选择文件会触发事件回调,打印如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e208c2c5a0ed446db0ade970fc2d656d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
拿到之后就可以上传到服务器了</p>
<pre><code class="hljs language-php copyable" lang="php"> <span class="hljs-comment">// 上传视频</span>
    selectvideo(e) &#123;
      this.<span class="hljs-built_in">exception</span> = <span class="hljs-string">'-'</span>
      <span class="hljs-keyword">const</span> file = e.target.files[<span class="hljs-number">0</span>] <span class="hljs-comment">// 获取选中的文件</span>
      <span class="hljs-keyword">if</span> ([
        <span class="hljs-string">'video/mp4'</span>,
        <span class="hljs-string">'video/ogg'</span>,
        <span class="hljs-string">'video/flv'</span>,
        <span class="hljs-string">'video/avi'</span>,
        <span class="hljs-string">'video/wmv'</span>,
        <span class="hljs-string">'video/rmvb'</span>,
        <span class="hljs-string">'video/mov'</span>
      ].indexOf(file.type) === -<span class="hljs-number">1</span>
      ) &#123;
        <span class="hljs-comment">// layer.msg('请上传正确的视频格式')</span>
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      <span class="hljs-keyword">if</span> (!file.size) &#123;
        <span class="hljs-comment">// layer.msg('视频大小不能超过50MB')</span>
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      <span class="hljs-keyword">const</span> reader = <span class="hljs-keyword">new</span> FileReader()
      reader.onload = e => &#123;
        let data
        <span class="hljs-keyword">if</span> (typeof e.target.result === <span class="hljs-string">'object'</span>) &#123;
          data = window.URL.createObjectURL(<span class="hljs-keyword">new</span> Blob([e.target.result]))
        &#125; <span class="hljs-keyword">else</span> &#123;
          data = e.target.result
        &#125;
        this.videosrc = data
        <span class="hljs-comment">// 获取转换后的地址地址</span>
      &#125;
      <span class="hljs-comment">// 转化为base64</span>
      reader.readAsDataURL(file)
      <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData() <span class="hljs-comment">// 创建form对象</span>
      formData.append(<span class="hljs-string">'file'</span>, file) <span class="hljs-comment">// 通过append向form对象添加数据const res = await upLoadImage(formData);</span>
      axios(&#123;
        url: this.apiUrl + <span class="hljs-string">'/file'</span>,
        method: <span class="hljs-string">'post'</span>,
        data: formData,
        headers: &#123; <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'multipart/form-data'</span>, Authorization: `$&#123;this.uploadHeaders.Authorization&#125;` &#125;,
        <span class="hljs-comment">// 原生获取上传进度的事件</span>
        onUploadProgress: progressEvent => &#123;
          <span class="hljs-keyword">const</span> process = ((progressEvent.loaded / progressEvent.total) * <span class="hljs-number">100</span>) | <span class="hljs-number">0</span>
          this.progress = process
        &#125;
      &#125;).then(res => &#123;
        this.<span class="hljs-variable">$message</span>(&#123; message: `上传$&#123;res.data.msg&#125;`, type: <span class="hljs-string">'success'</span> &#125;)
        <span class="hljs-comment">// 进度条变成成功状态</span>
        this.<span class="hljs-built_in">exception</span> = <span class="hljs-string">'success'</span>
        <span class="hljs-comment">// 延时初始化进度条</span>
        setTimeout(() => &#123;
          this.progress = <span class="hljs-number">0</span>
          <span class="hljs-comment">// 数据填充 获取本地转化为base64的地址和上传成功地址</span>
          this.videolist.push(&#123; data: this.videosrc, src: this.apiUrl + <span class="hljs-string">'/file/getImgStream?idFile='</span> + res.data.data.realFileName &#125;)
        &#125;, <span class="hljs-number">500</span>)
      &#125;).<span class="hljs-keyword">catch</span>(_error => &#123;
        this.<span class="hljs-variable">$message</span>(&#123; message: `上传失败`, type: <span class="hljs-string">'error'</span> &#125;)
        <span class="hljs-comment">// 进度条变成失败状态</span>
        this.<span class="hljs-built_in">exception</span> = <span class="hljs-string">'exception'</span>
        <span class="hljs-comment">// 延时初始化进度条</span>
        setTimeout(() => &#123; this.progress = <span class="hljs-number">0</span> &#125;, <span class="hljs-number">2000</span>)
      &#125;)
      <span class="hljs-comment">//   防止第二次同一个文件不能选中</span>
      e.target.value = <span class="hljs-string">''</span>
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后上传完成之后就是展示区域</p>
<pre><code class="hljs language-php copyable" lang="php"> <el-form-item>
        <div <span class="hljs-class"><span class="hljs-keyword">class</span>="<span class="hljs-title">list</span>-<span class="hljs-title">image</span>">
          <<span class="hljs-title">div</span> <span class="hljs-title">v</span>-<span class="hljs-title">for</span>="(<span class="hljs-title">item</span>,<span class="hljs-title">index</span>) <span class="hljs-title">in</span> <span class="hljs-title">videolist</span>" :<span class="hljs-title">key</span>="<span class="hljs-title">index</span>">
            <<span class="hljs-title">video</span> <span class="hljs-title">class</span>="<span class="hljs-title">video</span>" :<span class="hljs-title">src</span>="<span class="hljs-title">item</span>.<span class="hljs-title">data</span>" <span class="hljs-title">alt</span>="" />
            <<span class="hljs-title">span</span>><<span class="hljs-title">i</span> <span class="hljs-title">class</span>="<span class="hljs-title">el</span>-<span class="hljs-title">icon</span>-<span class="hljs-title">delete</span>" @<span class="hljs-title">click</span>="<span class="hljs-title">deletevideo</span>(<span class="hljs-title">index</span>)" /><<span class="hljs-title">i</span>
              <span class="hljs-title">class</span>="<span class="hljs-title">el</span>-<span class="hljs-title">icon</span>-<span class="hljs-title">caret</span>-<span class="hljs-title">right</span>"
              <span class="hljs-title">style</span>="<span class="hljs-title">font</span>-<span class="hljs-title">size</span>: 23<span class="hljs-title">px</span>;<span class="hljs-title">margin</span>-<span class="hljs-title">left</span>: 5<span class="hljs-title">px</span>;"
              @<span class="hljs-title">click</span>="<span class="hljs-title">pay</span>(<span class="hljs-title">index</span>)"
            /></<span class="hljs-title">span</span>>
          </<span class="hljs-title">div</span>>
          <<span class="hljs-title">el</span>-<span class="hljs-title">progress</span>
            <span class="hljs-title">v</span>-<span class="hljs-title">if</span>="<span class="hljs-title">progress</span>"
            <span class="hljs-title">type</span>="<span class="hljs-title">circle</span>"
            :<span class="hljs-title">percentage</span>="<span class="hljs-title">progress</span>"
            <span class="hljs-title">style</span>="<span class="hljs-title">height</span>: 126<span class="hljs-title">px</span>; <span class="hljs-title">width</span>: 126<span class="hljs-title">px</span>;"
            :<span class="hljs-title">status</span>="<span class="hljs-title">exception</span>"
          />
        </<span class="hljs-title">div</span>>
      </<span class="hljs-title">el</span>-<span class="hljs-title">form</span>-<span class="hljs-title">item</span>>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c7a6cfe0b83491286acb90dbd782f44~tplv-k3u1fbpfcp-watermark.image" alt="上传中" loading="lazy" referrerpolicy="no-referrer">中间好像不显示，可以自行修改
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a47be724b83d4d8d848e5d3295f99d6d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53018deec71f4a8f848d7fb6511d44c6~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c29a482145484e1e9ebc9f5d088f14c7~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02ec785ecaf44a74b12a205ccf5e662c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
遮罩样式</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">.list-image &#123;
  <span class="hljs-attr">width</span>: 600px;
  display: flex;
  flex-wrap: wrap;
  div,
  .videolist &#123;
    <span class="hljs-attr">width</span>: 150px;
    height: 150px;
    display: inline-block;
    position: relative;
    margin-right: 30px;
    margin-bottom: 30px;
    border-radius: 6px;
    overflow: hidden;
    transition: opacity <span class="hljs-number">0.</span>3s;
    img,
    video &#123;
      <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
      height: <span class="hljs-number">100</span>%;
    &#125;
    span &#123;
      <span class="hljs-attr">position</span>: absolute;
      width: <span class="hljs-number">100</span>%;
      height: <span class="hljs-number">100</span>%;
      left: <span class="hljs-number">0</span>;
      top: <span class="hljs-number">0</span>;
      cursor: <span class="hljs-keyword">default</span>;
      text-align: center;
      color: #fff;
      opacity: <span class="hljs-number">0</span>;
      font-size: 20px;
      background-color: rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.5</span>);
      transition: opacity <span class="hljs-number">0.</span>3s;
      display: flex;
      align-items: center;
      justify-content: center;
      i:hover &#123;
        <span class="hljs-attr">cursor</span>: pointer;
      &#125;
    &#125;
  &#125;
  <span class="hljs-attr">div</span>:hover span &#123;
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
    box-shadow: <span class="hljs-number">0</span> 2px 12px <span class="hljs-number">0</span> rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.5</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>鼠标移上去的事件</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">    <span class="hljs-comment">// 删除</span>
    <span class="hljs-built_in">deletevideo</span>(e) &#123;
      <span class="hljs-keyword">this</span>.videolist.<span class="hljs-built_in">splice</span>(e, <span class="hljs-number">1</span>)
      <span class="hljs-keyword">this</span>.video = <span class="hljs-string">''
    &#125;,
    // 播放
    pay(index) &#123;
      this.video = this.videolist[index].data
      this.dialogTableVisible = true
    &#125;,
    // 弹窗消失清空地址
    close() &#123;
      this.dialogTableVisible = false
      this.video = '</span>'
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>播放区域</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">   <el-dialog :visible.sync=<span class="hljs-string">"dialogTableVisible"</span> style=<span class="hljs-string">"text-align: center"</span> :before-close=<span class="hljs-string">"close"</span>>
        <video :src=<span class="hljs-string">"video"</span> controls=<span class="hljs-string">"controls"</span> autoplay width=<span class="hljs-string">"500px"</span> />
      </el-dialog>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3cd916fa4a4568ab85c9e07960ef45~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
小白一个，请多多包涵</p></div>  
</div>
            