
---
title: 'Fiddler高级用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c82786ac27a4f54850ecf80d155e277~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 03 May 2021 03:29:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c82786ac27a4f54850ecf80d155e277~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Fiddler高级用法</h2>
<h3 data-id="heading-1">1. 简单用法</h3>
<p>Fiddler作为一个基于http协议的抓包工具，一直在业界有广泛使用。很多测试或者前端在使用Fiddler时，仅仅用于查看前端和服务端之间的请求信息。包括我作为一个Fiddler的重度使用者，除了简单抓包分析外，最多也只是使用它的<code>Composer</code>功能，用来构建一个<code>POST</code>或者<code>GET</code>请求。总的来说，一般使用Fildder一般是使用以下几个功能</p>
<ol>
<li>抓包分析</li>
<li>通过配置代理，抓移动端请求信息</li>
<li>使用Composer快速测试后端接口</li>
</ol>
<p>然而功能强大且方便扩展的Fiddler远远不止这个简单的用法。</p>
<h3 data-id="heading-2">2. 高级用法--乱码处理</h3>
<p>前端开发中，调用后端一个接口。接口能正常访问，就是中文出现乱码。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c82786ac27a4f54850ecf80d155e277~tplv-k3u1fbpfcp-watermark.image" alt="乱码" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中左侧可以看到，不管是浏览器，还是在开发者工具中。后端返回的内容，都是乱码。并且乱码的内容还不同。从图中右侧，一般中文乱码的现象描述可以知道</p>
<ul>
<li>浏览器乱码原因推测是 <strong>以GBK的编码方式读取UTF8编码的中文</strong></li>
<li>开发者工具乱码原因推测是 <strong>以IOS8859-1的方式读取UTF8编码的中文</strong></li>
</ul>
<p>然而我后端接口代码刚好，只设置了响应内容是编码方式是UTF8，但并没有告诉浏览器。从显示结果来看，浏览器跟随系统默认编码猜测是<strong>GBK</strong>，而开发者工具默认编码猜测是<strong>IOS8859-1</strong>.为什么是猜测，因为，<strong>现在的chrome浏览器，实在找不到设置编码的地方</strong>，如果有知道的朋友，还麻烦留言告诉一下。</p>
<pre><code class="hljs language-java copyable" lang="java">  <span class="hljs-comment">//author:herbert 公众号:小院不小 Date:20210501 </span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">doGet</span><span class="hljs-params">(HttpServletRequest request, HttpServletResponse response)</span>
<span class="hljs-keyword">throws</span> ServletException, IOException </span>&#123;
String key = request.getParameter(<span class="hljs-string">"key"</span>);
String userName = request.getParameter(<span class="hljs-string">"u"</span>);
String password = request.getParameter(<span class="hljs-string">"p"</span>);
JSONObject user = findUserByNameAndPwd(userName, password);
JSONObject ret = <span class="hljs-keyword">new</span> JSONObject();
<span class="hljs-keyword">if</span> (user == <span class="hljs-keyword">null</span>) &#123;
ret.put(<span class="hljs-string">"errcode"</span>, <span class="hljs-number">99</span>);
ret.put(<span class="hljs-string">"errmsg"</span>, <span class="hljs-string">"未找到用户信息"</span>);
response.setCharacterEncoding(<span class="hljs-string">"utf8"</span>);<span class="hljs-comment">// 正常设置应该是设置Content-type</span>
response.getWriter().print(ret.toJSONString());
<span class="hljs-keyword">return</span>;
&#125;
    .....
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于后端代码没有加，但又必须马上解决。这个时候Fildder就派上用场了。</p>
<h4 data-id="heading-3">2.1 Fiddler断点</h4>
<p>在Fiddler左下角，有一行黑色的输入框。官方称之为<strong>QuickExec</strong>.在这里可以输入一些命令。比如我们现在要修改响应内容，就需要命令 <strong>bpafter</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e981f566a4a4761acf52afbc25e11a4~tplv-k3u1fbpfcp-watermark.image" alt="bpafer" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这里我们输入<code>bpafter weixin-server/weixinbind</code> 回车。然后会在状态栏看到这样一句话，<strong>RsponseURI breakpoint for weixin-server/weixinbind</strong>就表示启动成功了。这是我们在浏览器，重新访问这个链接，再回到Fildder会看到这样一个界面</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c9ad2cdebe340f79437f407de17c3e4~tplv-k3u1fbpfcp-watermark.image" alt="bpafterdebug" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在响应的页签中，我们选择<strong>raw</strong>页签，在Date下一样我们添加如下请求头<code>Content-Type: text/html;charset=utf-8</code>然后点击绿色的<strong>Run to Completion</strong> 按钮,回到浏览器。这时乱码就不在了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17b5b5c3738643cbad7ac2f6473883db~tplv-k3u1fbpfcp-watermark.image" alt="rightCharset" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">2.2 Fiddler规则</h4>
<p>聪明细心的一定发现了，使用<strong>bpater</strong>针对每次请求都需要手动添加header信息。能不能通过程序自动添加呢？答案是肯定的。
在Fiddler菜单中，选择Rules->Customize Rules...，弹出Fiddler的脚本编辑器。在脚本的<strong>OnBeforeResponse</strong>方法中添加如下代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">//author:herbert 公众号:小院不小 Date:20210501 </span>
 ...
<span class="hljs-keyword">if</span> (oSession.url.indexOf(<span class="hljs-string">"weixinbind"</span>)>-<span class="hljs-number">1</span>) &#123;
oSession.oResponse.headers.Add(<span class="hljs-string">"Customize"</span>,<span class="hljs-string">"add by Script"</span>)  
oSession.oResponse.headers.Add(<span class="hljs-string">"Content-Type"</span>,<span class="hljs-string">"text/html;charset=utf-8"</span>)  
&#125;
 ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存后退出，然后在状态栏看到<strong>CustomRules.js was loaded at 时间</strong>就表示我们当前修改的脚本已经生效了。回到浏览器重新访问改地址</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c1edc26ceb34e23a99175b6b70af9ae~tplv-k3u1fbpfcp-watermark.image" alt="rightCharsetByScript" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3. 高级用法--跨域处理</h3>
<p>构建跨域环境，我们在本地80端口下，添加index.html文件。文件内容如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--author:herbert 公众号:小院不小 Date:20210501 --></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">window</span>.onload = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-keyword">let</span> resutData = <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">"http://localhost:8080/weixin-server/weixinbind?u=1&p=2"</span>)
    <span class="hljs-keyword">let</span> jsonData = <span class="hljs-keyword">await</span> resutData.json();
    <span class="hljs-built_in">console</span>.log(jsonData)
    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#content"</span>).textContent = <span class="hljs-built_in">JSON</span>.stringify(jsonData)
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从代码中可以知道，访问了一个8080端口的GET请求。如果这个接口后端没有返回允许跨域标志，我们将请求不了数据。我们在浏览器会看到如下错误信息</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32b0e81fae73427d9ad089f99596b3cf~tplv-k3u1fbpfcp-watermark.image" alt="cros" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时，在后端不改代码的情况下，我们通过fiddler一样可以实现跨域请求。
在Fiddler菜单中，选择Rules->Customize Rules...，弹出Fiddler的脚本编辑器。在脚本的<strong>OnBeforeResponse</strong>方法中添加如下代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">//author:herbert 公众号:小院不小 Date:20210501 </span>
<span class="hljs-keyword">if</span>(oSession.host== <span class="hljs-string">"localhost:8080"</span>)&#123;
  oSession.oResponse.headers.Add(<span class="hljs-string">"Customize"</span>,<span class="hljs-string">"CROS add by Script"</span>);
  oSession.oResponse.headers.Add(<span class="hljs-string">"Content-Type"</span>,<span class="hljs-string">"application/json;charset=utf-8"</span>)  
  oSession.oResponse.headers.Add(<span class="hljs-string">"Access-Control-Allow-Origin"</span>,<span class="hljs-string">"*"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存退出后，刷新页面你会发现数据已经请求成功了.</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7bb5c4dfac54a909776169217ea6813~tplv-k3u1fbpfcp-watermark.image" alt="corsSuccess" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">4. 高级用法--响应替换</h3>
<p>修改线上内容，这个功能可想象的空间很大，可做的事情很多。为了说明他强大之处，我们依然上边的index.html说明。不过现在我们需要新建一个index2.html页面，具体内容如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--author:herbert 公众号:小院不小 Date:20210501 --></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">window</span>.onload = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-string">"警告！！！您的代码被修改啦"</span>)
    <span class="hljs-keyword">let</span> resutData = <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">"http://localhost:8080/weixin-server/weixinbind?u=1&p=2"</span>)
    <span class="hljs-keyword">let</span> jsonData = <span class="hljs-keyword">await</span> resutData.json();
    <span class="hljs-built_in">console</span>.log(jsonData)
    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#content"</span>).textContent = <span class="hljs-built_in">JSON</span>.stringify(jsonData)
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个文件仅仅是多加了一段代码<code>alert("警告！！！您的代码被修改啦")</code>,现在我们来实现访问index.html页面时，实际返回的index2.html的内容</p>
<p>在右侧找<strong>AutoResponse</strong>标签，点击添加规则，如下图设置</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72804a7284d7498ebe802d3c282c30fa~tplv-k3u1fbpfcp-watermark.image" alt="autoresponse" loading="lazy" referrerpolicy="no-referrer"></p>
<p>保存好以后，刷新刚才的index.html页面，你会看到如下结果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/515453da402a43aa8d9aad8e49c9e782~tplv-k3u1fbpfcp-watermark.image" alt="autoresponsesuccess" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里除了修改<code>HTML</code>页面外，还可以修改<code>css</code> <code>js</code>甚至<code>ajax</code>请求.这样可操作性就很多了，比如对别人的网站搞点小破坏啥的。特别是那些充分相信前端数据的网站，特别危险。
当然除了做响应替换外，还有其他很多命令，如用 *<strong>delay:1000</strong>实现延迟1秒响应，用于测试弱网环境</p>
<h3 data-id="heading-7">5. Fiddler4频繁弹出代理变化</h3>
<p>在很长一段时间，一直使用Fiddler2，每次打开都提示我升级，每次我都拒绝了。可是最近一次我升级了，问题就出现了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68f0f77d312049f3ab6c3bed59c0b23d~tplv-k3u1fbpfcp-watermark.image" alt="proxyChanged" loading="lazy" referrerpolicy="no-referrer"></p>
<p>抓包过程中出现了一条黄色的提示信息<strong>The system proxy was changed. click to reeable capturing</strong>.只要一出现这个信息，就不能愉快抓包了。后边从官方博客了解到改变代理服务最多可能有以下两个原因</p>
<ul>
<li>防火墙改变代理</li>
<li>VPN软件改变代理</li>
</ul>
<p>所以该怎么解决呢？这里有两个方法可以试下</p>
<h4 data-id="heading-8">5.1 重新启用代理</h4>
<p>在前边内容中，我们多次使用了自定义规则。这里我们一样可以通过自定义规则实现。
首先找到脚本的<code>main</code>方法,在里边注册一个事件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// author:herbert 公众号:小院不小 Date:20210502</span>
...
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Main</span>(<span class="hljs-params"></span>)</span>&#123;
  FiddlerObject.log(<span class="hljs-string">"注册函数DoReattach"</span>)
  FiddlerApplication.oProxy.add_DetachedUnexpectedly(DoReattach);
  <span class="hljs-keyword">var</span> today: <span class="hljs-built_in">Date</span> = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
  FiddlerObject.StatusText = <span class="hljs-string">" CustomRules.js was loaded at: "</span> + today;
&#125;
....   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后添加我们注册的方法<code>DoReattach</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// author:herbert 公众号:小院不小 Date:20210502</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">DoReattach</span>(<span class="hljs-params">o: <span class="hljs-built_in">Object</span>, ea: EventArgs</span>)</span>&#123;
  FiddlerObject.log(<span class="hljs-string">"DoReattach"</span>)
  ScheduledTasks.ScheduleWork(<span class="hljs-string">"reattach"</span>, <span class="hljs-number">1000</span>, innerReattach);
&#125;

<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">innerReattach</span>(<span class="hljs-params"></span>)</span>&#123;
  FiddlerObject.log(<span class="hljs-string">"innerReattach"</span>)
  FiddlerApplication.UI.actAttachProxy();
&#125;

<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">OnRetire</span>(<span class="hljs-params"></span>)</span>&#123;
  FiddlerObject.log(<span class="hljs-string">"执行函数OnRetire"</span>)
  FiddlerApplication.oProxy.remove_DetachedUnexpectedly(DoReattach);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里主要是通过检测到代理异常关闭时，启动一个任务，重新启动代理。就相当于程序帮我们完成了点击操作</p>
<h4 data-id="heading-9">5.2 从源头解决</h4>
<p>细心聪明的你，也许又发现了，上边的方法虽然解决了问题，但并不完美。会造成丢失某些请求。因为这里延迟了1秒重新启动代理。如果这个时间段刚好有一个请求过来，肯定就抓不到这个包。所以，还需要从源头抓起</p>
<p>首选关闭防火墙，如果确定已经关闭，但是问题还没有解决。这个时候就得检查你最近有没有安装vpn软件了。网上很多资料，都是让我们删除vpn的软件，这种杀鸡取卵的方式我是不敢苟同的。</p>
<p>其实我们只需要找到vpn相关的服务，然后关掉就可以了。这里不得不强调一下<strong>不要认为vpn没有运行就Ok，其实Vpn软件安装好以后，会在系统驻留服务，并开机启动</strong>。我们使用win+R启动运行窗口，输入<code>service.msc</code>回车，进入服务管理。按状态排序，让正在运行服务排列在最前边。然后一个个看是否有VPN相关文字介绍。这里没有搜索功能，比较麻烦。在我的电脑找到两个vpn相关的服务</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2c222d948084ce1904b851ec7e3abb5~tplv-k3u1fbpfcp-watermark.image" alt="SangforCSClient" loading="lazy" referrerpolicy="no-referrer"></p>
<p>![Dell]](<a href="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12dfb189a25e450296398c309223bb22~tplv-k3u1fbpfcp-watermark.image" target="_blank" rel="nofollow noopener noreferrer">p9-juejin.byteimg.com/tos-cn-i-k3…</a>)</p>
<p>这两个vpn工具，刚好都是我使用过的。选择停止这些服务，再回到Fildder工具，就再也么有出现那个黄色的警告条了。</p>
<p>彩蛋来了。附送一个小知识</p>
<p>在查找哪个程序修改了代理，我们可以使用ProcessMonitor工具。比如我们需要了解谁修改了我们代理，就可以添加如下两个过滤器实现</p>
<pre><code class="copyable">author:herbert 公众号:小院不小 Date:20210502

Operation  is RegSetValue
Path is HKCU\Software\Microsoft\Windows\CurrentVersion\InternetSettings\ProxyEnable
Path is HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyServer
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图所示</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcb54aa8928f42a580dcb7605ba3d8d5~tplv-k3u1fbpfcp-watermark.image" alt="processMonitorFilter" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样筛选以后，回到主界面，观察对应的额结果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/435222e3afb6423590d6ca65052a5945~tplv-k3u1fbpfcp-watermark.image" alt="processMonitorList" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从列表中结果中我们可了解到，除了Fiddler外还有其他程序在修改注册表<code>ProxyEnable</code>对应的值.</p>
<ul>
<li>20:27:50 这个时间段，是我启动Fiddler出现的结果。ProxyEnable变化 1->0->1,ProxyServer维持为127.0.0.1:8888</li>
<li>20:28:09 这个时间段，是Fidder出现那个黄色警告框出现的结果 ProxyEnable变化 1->0->1->0,ProxyServer维持为127.0.0.1:8888</li>
</ul>
<p>所以，最终<code>ProxyEnable</code>变成<code>0</code>了，就无法启动代理了。点击最后一条<code>ProxyEnable</code>为<code>0</code>的数据，查看明细，如下图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e27e38081354423ab8a1468274e9e69a~tplv-k3u1fbpfcp-watermark.image" alt="processMonitorDetail" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我对比<code>ProxyEnable</code>为<code>1</code>的那条数据，无论是<strong>进程id还是堆栈信息</strong>，都是一样的。所以我严重怀疑，这是<strong>Fiddler4的一个BUG</strong>。因为同样的环境，运行<strong>Fidder2</strong>并不会出现上边的那种情况。</p>
<h3 data-id="heading-10">6. 总结</h3>
<p>Fiddler这个软件基于插件的开发模式，可以扩展出很多功能。这个工具平时自己经常使用，很多时候只是抓个包发个请求而已。这次深挖了一下，主要是开发过程chrome开发者工具请求的中文出现了乱码。然而后端的代码又是我没权限修改的。所以就动了Fiddler的心思。这次就不放什么demo了。还是希望您多多支持下，写作不易。如果觉得还有点意思，您扫描下方的二维码,关注公众号[<strong>小院不小</strong>]，这里是我记录的技术地方，一直坚持原创，一直坚持是工作所积累。所以不会天天发文。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0c055ec1d3b4df2a8f295582a07799c~tplv-k3u1fbpfcp-watermark.image" alt="公众号" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            