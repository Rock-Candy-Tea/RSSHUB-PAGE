
---
title: '从零开始的electron开发-文件处理-本地文件加载'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9889'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 17:12:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=9889'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">文件处理-本地文件加载</h1>
<p>我们在使用electron时，有时会涉及一些文件的处理，比如文件的下载，或者本地文件的加载（本地音乐，本地图片等），本章主要介绍electron本地文件的加载。<br>
其实这个功能还是比较常见的，比如我们下载了某某皮肤主题本地，想在本地加载，或者是做一个音乐播放器，加载本地音乐进行播放。<br>
目标：使用input file获取图片或者音乐文件的本地地址（当然你可以直接用已有文件的本地地址），进行展示和播放。</p>
<h2 data-id="heading-1">web本地文件加载</h2>
<p>浏览器为了安全考虑，在web页面进行文件加载时，是禁用了<code>file://</code>协议进行文件展示的，一般来说要想获取本地文件展示，得让用户进行input file选择，获取File对象，对这个File对象进行操作展示：</p>
<pre><code class="copyable"><a-upload
  :customRequest="customRequest"
  name="file"
  :showUploadList="false"
  :multiple="true"
>
  <a-button>
    <upload-outlined></upload-outlined>
    添加图片
  </a-button>
</a-upload>
<a-image
  :width="200"
  :height="200"
  :src="state.image"
  />


function customRequest(fileData) &#123;
  const file = fileData.file
  state.image = window.URL.createObjectURL(file)
  // 或者:
   if (file) &#123;
    var reader = new FileReader()
    reader.onload = function (evt) &#123;
      state.image = evt.target.result
    &#125;
    reader.onerror = function (evt) &#123;
      console.error(evt)
    &#125;
    reader.readAsDataURL(file)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如在进行图片的本地显示时，使用createObjectURL直接创建url对象进行展示或者使用readAsDataURL将其转化为base64进行展示。<br>
当然在electron中一切都变得简单起来，我们可以使用本地路径加载文件，当然得进行一些小处理。</p>
<h2 data-id="heading-2">electron本地文件加载</h2>
<p>比如说我们已知一个本地图片的路径，假设这个路径为下载文件夹中<code>C:\Users\Administrator\Downloads\1.png</code>，我们将这个地址赋值给img的src：</p>
<pre><code class="copyable"><a-upload
  :customRequest="customRequest"
  name="file"
  :showUploadList="false"
  :multiple="true"
>
  <a-button>
    <upload-outlined></upload-outlined>
    添加图片
  </a-button>
</a-upload>

<a-image
  :width="200"
  :height="200"
  :src="state.image"
  />

function customRequest(fileData) &#123;
  const path = fileData.file.path
  state.image = path
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的path就是本地文件的地址，当你赋值之后发现图片并不能加载，会报一个<code>net::ERR_UNKNOWN_URL_SCHEME</code>的错误，这是由于直接添加本地路径的话，加载文件实际上是通过<code>file://</code>协议进行加载的，默认情况下chromium并不能通过<code>file://</code>协议来读取文件，参考<a href="https://peter.sh/experiments/chromium-command-line-switches/#allow-file-access-from-files" target="_blank" rel="nofollow noopener noreferrer">链接</a>， 故并不能直接显示出来，本来可以设置chromium启动参数
(–-allow-file-access-from-files)来解决这个问题，但是比较遗憾electron并不吃这个一套：</p>
<pre><code class="copyable">// 无效
app.commandLine.appendSwitch('allow-file-access-from-files', true)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要对这个本地路径进行处理，让其不通过<code>file://</code>协议加载，那么如何实现呢？
我们可以通过<code>protocol</code>模块来注册自定义协议并拦截现有协议请求，比如我们实现一个<code>atom://</code>协议加载音乐文件进行播放：</p>
<pre><code class="copyable">主进程：
app.whenReady().then(() => &#123;
  // 这个需要在app.ready触发之后使用
  protocol.registerFileProtocol('atom', (request, callback) => &#123;
    const url = request.url.substr(7)
    callback(decodeURI(path.normalize(url)))
  &#125;)
&#125;)

渲染进程：
<a-upload
  :customRequest="customRequest"
  name="file"
  :showUploadList="false"
  :multiple="true"
>
  <a-button>
    <upload-outlined></upload-outlined>
    添加本地音乐
  </a-button>
</a-upload>
<audio :src="state.audio" controls>
</audio>


function customRequest(fileData) &#123;
  const path = 'atom:///' + fileData.file.path
  state.audio = path
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原来呢我们是直接赋值类似于<code>C:\Users\Administrator\Downloads\1.png</code>，我们在这个路径上加上<code>atom:///</code>变为<code>atom:///C:\Users\Administrator\Downloads\1.png</code>(mac同理，atom是一样的)，当匹配到atom时，就会拦截这个协议请求，返回一个本地路径。这里需要注意的一点是如果我们的路径有中文名，那么获取的<code>url</code>是encodeURI编码后的，我们在callback回调时需要用<code>decodeURI</code>进行解码。</p>
<p>注册了自定义协议之后，我们只需在加载本地路径时，在前面加上<code>atom:///</code>(其他名也可，自定义)即可。</p>
<p>本系列更新只有利用周末和下班时间整理，比较多的内容的话更新会比较慢，希望能对你有所帮助，请多多star或点赞收藏支持一下</p>
<p>本文地址：<a href="https://xuxin123.com/%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E7%9A%84electron%E5%BC%80%E5%8F%91-%E6%96%87%E4%BB%B6%E5%A4%84%E7%90%86-%E6%9C%AC%E5%9C%B0%E6%96%87%E4%BB%B6%E5%8A%A0%E8%BD%BD/" target="_blank" rel="nofollow noopener noreferrer">链接</a><br>
本文github地址：<a href="https://github.com/xuxingeren/vue-cli-electron" target="_blank" rel="nofollow noopener noreferrer">链接</a></p></div>  
</div>
            