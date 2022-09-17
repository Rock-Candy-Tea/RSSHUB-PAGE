
---
title: 'node.js的官方模块'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9463'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 23:23:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=9463'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>1、Globals模块：全局模块 - 全局变量在所有模块中均可使用。不需要引入，但是提供了一些全局变量给我们，我们可以直接使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  __dirname - 当前文件夹的绝对路径，
  __filename - 当前文件的完整的绝对路径
    <span class="hljs-built_in">exports</span> - 一个空&#123;&#125;，公开和暴露自己的成员
    <span class="hljs-variable language_">module</span> - 指代当前模块本身，包含了其他<span class="hljs-number">4</span>个变量
    <span class="hljs-built_in">require</span>()  - 一个函数，引入其他模块的
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、Querystring模块：查询字符串</p>
<pre><code class="hljs language-ini copyable" lang="ini">需要引入：let <span class="hljs-attr">qs</span> = require(<span class="hljs-string">'querystring'</span>)<span class="hljs-comment">;</span>
提供了解析url的查询字符串部分的功能
var  <span class="hljs-attr">obj</span>=qs.parse(<span class="hljs-string">"查询字符串部分"</span>)<span class="hljs-comment">;</span>
想要获取前端传来的某一个部分：obj.键名<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、Url模块：网址模块</p>
<pre><code class="hljs language-ini copyable" lang="ini">需要引入：let <span class="hljs-attr">url</span> = require(<span class="hljs-string">'url'</span>)<span class="hljs-comment">;</span>
提供了一些实用函数，用于 完整的URL 解析
var <span class="hljs-attr">objUrl</span>=url.parse(<span class="hljs-string">"完整的url网址"</span>,<span class="hljs-literal">true</span>)<span class="hljs-comment">;此方法会将url网址的各个部分全部解析出来，支持传入第二个参数，是一个布尔值，如果传入的是一个true，自动调用querystring的parse方法，顺便也解析了查询字符串（请求消息：前端->后端的东西）部分</span>
1、查询字符串：objUrl.query.键名 - 拿到前端传到后端的东西
2、路由：objUrl.pathname<span class="hljs-comment">; - 判断路由的不同，响应不同的网页给用户看</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、Buffer模块：缓冲区，可以将数组变成一个16进制的数字</p>
<p>5、fs模块：FileSystem - 文件系统</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">需要引入：<span class="hljs-keyword">let</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
提供了可以操作文件的<span class="hljs-variable constant_">API</span>
异步读取文件：
        fs.<span class="hljs-title function_">readFile</span>(<span class="hljs-string">"绝对路径|文件路径"</span>,<span class="hljs-function">(<span class="hljs-params">err,buf</span>)=></span>&#123;
拿到buf要干嘛？就需要写在这里
&#125;)

        异步写入文件：- 将原来的东西，替换掉
        fs.<span class="hljs-title function_">writeFile</span>(<span class="hljs-string">"绝对路径|文件路径"</span>,<span class="hljs-string">"写入的新内容"</span>,<span class="hljs-function">()=></span>&#123;
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"写入完毕了，以后要做什么"</span>)
&#125;)

        异步追加文件：- 保留原来的东西
fs.<span class="hljs-title function_">appendFile</span>(<span class="hljs-string">"绝对路径|文件路径"</span>,<span class="hljs-string">"写入的新内容"</span>,<span class="hljs-function">()=></span>&#123;
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"写入完毕了，以后要做什么"</span>)
&#125;)
                    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、http模块</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">固定步骤：
<span class="hljs-comment">//引入http、url、fs官方模块</span>
<span class="hljs-keyword">var</span> http=<span class="hljs-built_in">require</span>(<span class="hljs-string">"http"</span>);
<span class="hljs-keyword">var</span> url=<span class="hljs-built_in">require</span>(<span class="hljs-string">"url"</span>);
<span class="hljs-keyword">var</span> fs=<span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);
<span class="hljs-comment">//创建服务器</span>
<span class="hljs-keyword">var</span> app=http.<span class="hljs-title function_">createServer</span>();
<span class="hljs-comment">//为服务器设置监听的端口号</span>
app.<span class="hljs-title function_">listen</span>(<span class="hljs-number">80</span>);<span class="hljs-comment">//http默认端口为80，https默认端口为443</span>
<span class="hljs-comment">//为服务器绑定请求事件 - 请求？前端发到后端的，</span>
app.<span class="hljs-title function_">on</span>(<span class="hljs-string">"request"</span>,<span class="hljs-function">(<span class="hljs-params">req,res</span>)=></span>&#123;
        <span class="hljs-comment">//req - request:保存请求对象，请求对象，前端->后端，提供了一个属性req.url，解析此属性拿到自己需要的部分（路由|请求消息）</span>
<span class="hljs-keyword">var</span> objUrl=url.<span class="hljs-title function_">parse</span>(req.<span class="hljs-property">url</span>,<span class="hljs-literal">true</span>);
<span class="hljs-comment">//得到前端传来路由部分</span>
<span class="hljs-keyword">var</span> router=objUrl.<span class="hljs-property">pathname</span>;
<span class="hljs-comment">//判断前端的路由是什么，给他返回不同的页面</span>
<span class="hljs-keyword">if</span>(router==<span class="hljs-string">"/"</span> || router==<span class="hljs-string">"/index.html"</span>)&#123;
<span class="hljs-comment">//res - response：保存响应对象，后端->前端，提供了一个方法res.end(你想要响应的东西)</span>
fs.<span class="hljs-title function_">readFile</span>(<span class="hljs-string">"./public/index.html"</span>,<span class="hljs-function">(<span class="hljs-params">err,buf</span>)=></span>&#123;
res.<span class="hljs-title function_">end</span>(buf);
&#125;)
&#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(router.<span class="hljs-title function_">match</span>(<span class="hljs-regexp">/html/</span>)!=<span class="hljs-literal">null</span>)&#123;
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(router);
fs.<span class="hljs-title function_">readFile</span>(<span class="hljs-string">"./public"</span>+router,<span class="hljs-function">(<span class="hljs-params">err,buf</span>)=></span>&#123;
res.<span class="hljs-title function_">end</span>(buf);
&#125;)
&#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(router.<span class="hljs-title function_">match</span>(<span class="hljs-regexp">/css|js|jpg|png|gif|woff/</span>)!=<span class="hljs-literal">null</span>)&#123;
fs.<span class="hljs-title function_">readFile</span>(<span class="hljs-string">"./public"</span>+router,<span class="hljs-function">(<span class="hljs-params">err,buf</span>)=></span>&#123;
res.<span class="hljs-title function_">end</span>(buf);
&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;)</p>
<h1 data-id="heading-0">**      BOM对象**</h1>
<p>window对象介绍：扮演着两个角色</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-number">1</span>、代替了<span class="hljs-selector-tag">ES</span>中的<span class="hljs-selector-tag">global</span>，充当全局对象 <span class="hljs-selector-tag">-</span> 保存全局变量和全局函数
<span class="hljs-number">2</span>、自己也带有一些属性和方法，指代当前窗口本身

<span class="hljs-number">1</span>、网页打开新链接的方式：<span class="hljs-number">4</span>种 <span class="hljs-selector-tag">-</span> 目的：提升用户的体验感
<span class="hljs-number">1</span>、替换当前页面，可以后退
<span class="hljs-selector-tag">HTML</span>：<<span class="hljs-selector-tag">a</span> <span class="hljs-selector-tag">href</span>="<span class="hljs-selector-tag">url</span>">内容</<span class="hljs-selector-tag">a</span>>
     <span class="hljs-selector-tag">JS</span>：<span class="hljs-selector-tag">open</span>(<span class="hljs-string">"url"</span>,<span class="hljs-string">"_self"</span>);

<span class="hljs-number">2</span>、替换当前页面，禁止后退 <span class="hljs-selector-tag">-</span> 场景：电商网站，付款后不允许退回去再次付款
<span class="hljs-selector-tag">history</span>对象：记录着【当前窗口】的历史记录，只有有了历史才能前进后退
<span class="hljs-selector-tag">location</span>对象：记录着【当前窗口】正在打开的<span class="hljs-selector-tag">url</span>，而他又一个方法叫做替换，替换是不会产生任何历史记录的，但是<span class="hljs-selector-tag">url</span>替换后网页必然跳转
     <span class="hljs-selector-tag">JS</span>：<span class="hljs-selector-tag">location</span><span class="hljs-selector-class">.replace</span>(<span class="hljs-string">"新url"</span>)

<span class="hljs-number">3</span>、新窗口打开，可以打开多个
<span class="hljs-selector-tag">HTML</span>：<<span class="hljs-selector-tag">a</span> <span class="hljs-selector-tag">href</span>="<span class="hljs-selector-tag">url</span>" <span class="hljs-selector-tag">target</span>="<span class="hljs-selector-tag">_blank</span>">内容</<span class="hljs-selector-tag">a</span>>
     <span class="hljs-selector-tag">JS</span>：<span class="hljs-selector-tag">open</span>(<span class="hljs-string">"url"</span>,<span class="hljs-string">"_blank"</span>);

<span class="hljs-number">4</span>、新窗口打开，只能打开一个 <span class="hljs-selector-tag">-</span> 场景：电商网站，只允许用户打开一个付款页面
<span class="hljs-selector-tag">HTML</span>：<<span class="hljs-selector-tag">a</span> <span class="hljs-selector-tag">href</span>="<span class="hljs-selector-tag">url</span>" <span class="hljs-selector-tag">target</span>="自定义<span class="hljs-selector-tag">name</span>">内容</<span class="hljs-selector-tag">a</span>>
自定义<span class="hljs-selector-tag">name</span>的意思：每一个窗口底层都有一个名字，<span class="hljs-selector-tag">target</span>其实就是在设置名字，<span class="hljs-selector-tag">name</span>如果相同，新打开的窗口就会把旧窗口给替换掉（刷新）
     <span class="hljs-selector-tag">JS</span>：<span class="hljs-selector-tag">open</span>(<span class="hljs-string">"url"</span>,<span class="hljs-string">"自定义的name"</span>);

<span class="hljs-selector-tag">HTML</span>能做的，<span class="hljs-selector-tag">JS</span>都能做，<span class="hljs-selector-tag">JS</span>能做的，<span class="hljs-selector-tag">HTML</span>不一定可以
                    
                    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、window提供了属性和方法：</p>
<pre><code class="hljs language-ini copyable" lang="ini">属性：获取浏览器的完整大小：outerWidth/outerHeight<span class="hljs-comment">;</span>
 获取浏览器的文档显示区域的大小：innerWidth/innerHeight
获取屏幕的完整大小：screen.width/height<span class="hljs-comment">;</span>
每个人的电脑分辨率是不一样的

方法：1、打开窗口：var <span class="hljs-attr">newWindow</span>=open(<span class="hljs-string">"url"</span>,<span class="hljs-string">"自定义的name"</span>,<span class="hljs-string">"width=,height=,left=,top="</span>)<span class="hljs-comment">;</span>
注意：1、第三个配置参数没有传入时，窗口大小和浏览器一样，并且黏在浏览器上面（融为一体）
2、写入了第三个实参，则会脱离浏览器并且一个独立的小窗口，并且可以保存起来，设置为他绑定事件
3、宽高不能设置的太小了
          2、关闭窗口：window/newW.close()<span class="hljs-comment">;</span>
          3、修改窗口的大小：newW.resizeTo(new宽,new高)<span class="hljs-comment">;</span>
          4、修改窗口的位置：newW.moveTo(x,y)<span class="hljs-comment">;</span>
                              
                              
                              
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、周期性定时器</p>
<pre><code class="hljs language-scss copyable" lang="scss">             开启：timer=<span class="hljs-built_in">setInterval</span>(callback,间隔毫秒数);
                停止：<span class="hljs-built_in">clearInterval</span>(timer)

<span class="hljs-number">2</span>、一次性定时器
开启：timer=<span class="hljs-built_in">setTimeout</span>(callback,间隔毫秒数);
停止：<span class="hljs-built_in">clearTimeout</span>(timer)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            