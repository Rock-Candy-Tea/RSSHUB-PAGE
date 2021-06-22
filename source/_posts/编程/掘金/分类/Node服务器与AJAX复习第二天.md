
---
title: 'Node服务器与AJAX复习第二天'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e59cda88d09c4a09baa0a80c9aba54c4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 16:36:50 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e59cda88d09c4a09baa0a80c9aba54c4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>这是我参与更文挑战的第21天，活动详情查看：</code><a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">FS模块</h3>
<p>File system 文件系统</p>
<p>当前这个模块用于操作文件与文件夹</p>
<h4 data-id="heading-1">创建文件</h4>
<pre><code class="hljs language-js copyable" lang="js">fs.appendFile(filePath, content, callback);
filePath: 文件路径
<span class="hljs-attr">content</span>: 文件内容
<span class="hljs-attr">callback</span>: 回调函数
回调函数中有err 表示创建过程中可能出现的异常
该方法有两种用法，第一种创建文件（当文件不存在时），第二种追加内容（当文件已经存在时）
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入FS模块</span>
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

<span class="hljs-comment">// 创建文件</span>
fs.appendFile(<span class="hljs-string">"./a.txt"</span>, <span class="hljs-string">"这是一个txt文件"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
<span class="hljs-comment">// 当前函数就是创建文件完毕之后的回调函数</span>
<span class="hljs-comment">// err 表示 创建过程中可能出现的异常</span>
<span class="hljs-built_in">console</span>.log(err);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"创建完毕"</span>);
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e59cda88d09c4a09baa0a80c9aba54c4~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">读取文件</h4>
<pre><code class="hljs language-js copyable" lang="js">fs.readFile(filePath, callback);
filePath: 文件路径
<span class="hljs-attr">callback</span>: 回调函数
<span class="hljs-attr">err</span>: 读取过程中可能发生的错误 没错误时 err是<span class="hljs-literal">null</span> 有错误时 err时错误对象
<span class="hljs-attr">data</span>: 读取到的文件内容 它的类型时buffer
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo:</p>
<pre><code class="hljs language-js copyable" lang="js">fs.readFile(<span class="hljs-string">"index.html"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, data</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(err);
<span class="hljs-built_in">console</span>.log(data);
<span class="hljs-built_in">console</span>.log(data.toString());
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8252ab4e484b4db19c13c64dd1ea8b67~tplv-k3u1fbpfcp-watermark.image" alt="图片3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">删除文件</h4>
<pre><code class="hljs language-js copyable" lang="js">fs.unlink(filePath, callback);
filePath: 被删除的文件的地址
<span class="hljs-attr">callback</span>: 回调函数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入fs</span>
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

<span class="hljs-comment">// 调用unlink方法删除文件</span>
fs.unlink(<span class="hljs-string">"./index.html"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"删除"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">重命名</h4>
<pre><code class="hljs language-js copyable" lang="js">fs.rename(oldPath, newPath, callback);
oldPath: 原路径
<span class="hljs-attr">newPath</span>: 新路径
<span class="hljs-attr">callback</span>: 回调函数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);
fs.rename(<span class="hljs-string">"a.js"</span>, <span class="hljs-string">"b.js"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"重命名"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">创建文件夹</h4>
<pre><code class="hljs language-js copyable" lang="js">fs.mkdir(dirPath, callback);
dirPath: 文件夹路径
<span class="hljs-attr">callback</span>: 回调函数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);
fs.mkdir(<span class="hljs-string">"a"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">删除文件夹</h4>
<pre><code class="hljs language-js copyable" lang="js">fs.rmdir(dirPath, callback);
dirPath: 被删除的文件夹
<span class="hljs-attr">callback</span>: 回调函数
注：该方法只可以删除空目录
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

fs.rmdir(<span class="hljs-string">"abc"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">如果删除非空目录:</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0ee242b06784f77a0522312eb34ac85~tplv-k3u1fbpfcp-watermark.image" alt="23.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">读取文件夹</h4>
<pre><code class="hljs language-js copyable" lang="js">fs.readdir(dirPath, callback);
dirPath: 被读取的文件夹
<span class="hljs-attr">callback</span>: 回调函数
<span class="hljs-attr">err</span>: 错误对象
<span class="hljs-attr">arr</span>: 被读取的文件夹中所有文件与文件夹名组成的数组
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

fs.readdir(<span class="hljs-string">"./新建文件夹"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, arr</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(err);
<span class="hljs-built_in">console</span>.log(arr);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1de80cec84646ab802bd0ff29d6badd~tplv-k3u1fbpfcp-watermark.image" alt="图片4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">判断一个目标是文件还是文件夹</h4>
<pre><code class="hljs language-js copyable" lang="js">fs.stat(path, callback);
path: 目标路径
<span class="hljs-attr">callback</span>: 回调函数
<span class="hljs-attr">err</span>: 错误对象
<span class="hljs-attr">state</span>: 根据目标生成的一个对象 该对象有一个方法 isDirectory() 返回布尔值 如果是<span class="hljs-literal">true</span> 说明是文件夹 否则 说明是文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

fs.stat(<span class="hljs-string">"./新建文件夹/aaa.txt"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, state</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"aaa.txt"</span> + (state.isDirectory() ? <span class="hljs-string">"是"</span> : <span class="hljs-string">"不是"</span>) + <span class="hljs-string">"一个文件夹"</span>);
&#125;)

fs.stat(<span class="hljs-string">"./新建文件夹/aaaa"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, state</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"aaaa"</span> + (state.isDirectory() ? <span class="hljs-string">"是"</span> : <span class="hljs-string">"不是"</span>)+ <span class="hljs-string">"一个文件夹"</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ece2a06023d046739048b74a5043bbca~tplv-k3u1fbpfcp-watermark.image" alt="21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">删除非空目录</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">del</span>(<span class="hljs-params">dirPath</span>) </span>&#123;
<span class="hljs-comment">// 读取该文件夹</span>
<span class="hljs-keyword">var</span> arr = fs.readdirSync(dirPath)
<span class="hljs-comment">// 循环</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;<span class="hljs-keyword">var</span> state = fs.statSync(dirPath + <span class="hljs-string">"/"</span> + arr[i]);
<span class="hljs-comment">// console.log(dirPath + "/" + arr[i] + (state.isDirectory() ? "是":"不是") + "一个文件夹");</span>
<span class="hljs-keyword">if</span> (state.isDirectory()) &#123;
del(dirPath + <span class="hljs-string">"/"</span> + arr[i]);
&#125; <span class="hljs-keyword">else</span> &#123;
fs.unlinkSync(dirPath + <span class="hljs-string">"/"</span> + arr[i])
&#125;
&#125;
<span class="hljs-comment">// 最后删除文件夹 </span>
fs.rmdirSync(dirPath);
&#125;

<span class="hljs-built_in">module</span>.exports = del;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">URL模块</h3>
<p>该模块用于处理URL字符串和URL对象</p>
<h4 data-id="heading-12">URL.parse</h4>
<p>parse方法用于将URL字符串解析成URL对象</p>
<p>Demo:</p>
<pre><code class="hljs language-js copyable" lang="js">有如下字符串: 
   <span class="hljs-keyword">var</span> str = http:<span class="hljs-comment">//www.icketang.com/pc/index.html?username=laosi&password=123#ccc</span>
想要获取url中的某一个部分:
引入url模块
<span class="hljs-keyword">var</span> url = <span class="hljs-built_in">require</span>(<span class="hljs-string">"url"</span>);
调用parse方法解析字符串
url.parse(str); 返回值是一个对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象如下:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f23713cac678401093af55637f66442e~tplv-k3u1fbpfcp-watermark.image" alt="04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">静态服务器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入http模块</span>
<span class="hljs-keyword">var</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">"http"</span>);
<span class="hljs-comment">// 引入fs模块</span>
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);
<span class="hljs-comment">// 引入url模块</span>
<span class="hljs-keyword">var</span> url = <span class="hljs-built_in">require</span>(<span class="hljs-string">"url"</span>);

<span class="hljs-comment">// MIMEType大全</span>
<span class="hljs-keyword">var</span> MIMEType = &#123;  
<span class="hljs-string">"*"</span>      :<span class="hljs-string">"application/octet-stream"</span>,
<span class="hljs-string">"323"</span>    :<span class="hljs-string">"text/h323"</span>,
<span class="hljs-string">"acx"</span>    :<span class="hljs-string">"application/internet-property-stream"</span>,
<span class="hljs-string">"ai"</span>    :<span class="hljs-string">"application/postscript"</span>,
    ……
 &#125;

<span class="hljs-comment">// 创建服务器</span>
<span class="hljs-keyword">var</span> server = http.createServer(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res</span>) </span>&#123;
<span class="hljs-comment">// if (req.url === "/index.html") &#123;</span>
<span class="hljs-comment">// fs.readFile("./index.html", function(err, data) &#123;</span>
<span class="hljs-comment">// res.end(data);</span>
<span class="hljs-comment">// &#125;)</span>
<span class="hljs-comment">// return;</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-comment">// if (req.url === "/second.html") &#123;</span>
<span class="hljs-comment">// fs.readFile("./second.html", function(err, data) &#123;</span>
<span class="hljs-comment">// res.end(data);</span>
<span class="hljs-comment">// &#125;)</span>
<span class="hljs-comment">// return;</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// 我们发现 当访问的是/index.html时，读取的是./index.html 访问的是/second.html时 读取的是./second.html 我们可以直接强行读取 不管发送的是什么请求 全部前面加.后读取</span>
<span class="hljs-comment">// console.log(req.url);</span>
<span class="hljs-comment">// 定义变量 接受格式化之后的对象</span>
<span class="hljs-keyword">var</span> url_obj = url.parse(req.url);
<span class="hljs-comment">// console.log(url_obj);</span>
<span class="hljs-keyword">var</span> pathName = url_obj.pathname;
fs.readFile(<span class="hljs-string">"."</span> + pathName, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, data</span>) </span>&#123;
<span class="hljs-keyword">if</span> (err) &#123;
res.setHeader(<span class="hljs-string">"content-type"</span>, <span class="hljs-string">"text/plain;charset=utf-8"</span>);
res.end(<span class="hljs-string">"抱歉, 您读取的  ."</span> + pathName + <span class="hljs-string">"不存在"</span>);
<span class="hljs-keyword">return</span>;
&#125;
<span class="hljs-comment">// 获取拓展名  index.html</span>
<span class="hljs-keyword">var</span> extName =  pathName.slice(pathName.indexOf(<span class="hljs-string">"."</span>) + <span class="hljs-number">1</span>);
res.setHeader(<span class="hljs-string">"content-type"</span>, MIMEType[extName] + <span class="hljs-string">";charset=utf-8"</span>)
res.end(data);
&#125;)
&#125;)

<span class="hljs-comment">// 监听端口号</span>
server.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">HTTP请求方式</h3>
<h4 data-id="heading-15">GET请求</h4>
<pre><code class="hljs language-js copyable" lang="js">HTTP请求根据目的可以划分成不同的种类。
get请求表示“从服务器上获取内容”
特点: 触发方式多 
地址栏输入
img标签发出的请求
link标签发出的请求
script标签发出的请求
表单发出的请求
ajax
    没有请求正文
携带的数据就是query
  便于分享
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">POST请求</h4>
<pre><code class="hljs language-js copyable" lang="js">post请求表示“往服务器上放置内容”
特点：触发方式少
表单
ajax
  保密性高
因为请求时携带的数据都放在请求正文内
  不便于分享
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">NodeJS处理GET请求</h3>
<p>前端发送的请求：</p>
<pre><code class="hljs language-js copyable" lang="js">http:<span class="hljs-comment">//localhost:3000/login?username=%E7%8E%8B%E8%80%81%E4%BA%94&psd=123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后端处理:</p>
<p>所谓的后端处理，其实就是将前端发送过来的数据或者保存，或者查询等处理方式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> url_obj = url.parse(req.url, <span class="hljs-literal">true</span>); 
<span class="hljs-comment">// 定义接口处理/login</span>
<span class="hljs-keyword">if</span> (pathName === <span class="hljs-string">"/login"</span> && req.method.toLowerCase() === <span class="hljs-string">"get"</span>) &#123;
<span class="hljs-built_in">console</span>.log(url_obj.query.username);
<span class="hljs-built_in">console</span>.log(url_obj.query.psd);
res.end(<span class="hljs-string">"hello"</span>);
<span class="hljs-keyword">return</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>url.parse的第二个参数为true时，表示将解析出来的query也转化成对象。</p>
<p>为false时:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94073528d38147cda7a49454bb4e25f7~tplv-k3u1fbpfcp-watermark.image" alt="图片5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为true时:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c0503b69f6b451ebb7a9281eb355fc6~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            