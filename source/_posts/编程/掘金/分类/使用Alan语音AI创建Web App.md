
---
title: '使用Alan语音AI创建Web App'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50e450d8e8f9463a8c77092d352c33c4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 02:02:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50e450d8e8f9463a8c77092d352c33c4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>当前有很多语音助手：iOS有Siri，Windows有小娜，Android有Google Assistant，亚马逊的Alexa，国内安卓有灵犀。各大厂还推出了小度、小雅、小爱、天猫精灵等智能音箱产品，深受大家喜爱。这些语音助手或语音AI产品有一个基本上都是基于移动设备的。除了少有几个在线搜索、在线翻译App使用语音助手，很少看到使用了语音功能的Web App。主要还是因为移动场景下语音设备一般是标配，语音功能能解放双手，使用起来很方便。而电脑没有声卡没有麦克风一样跑得很溜，加上Web语音技术不是原生的，自行研发成本很高。随着Serverless（无服务器环境）和云计算云服务大行其道，我相信语音Web App会流行起来的。下面就会为大家推荐一个高级语音AI平台Alan。</p>
<h1 data-id="heading-0">一、Alan概述</h1>
<p>Alan提供了一个完整的无服务器环境来构建强大且可靠的应用内语音助手和聊天机器人。无需创建口语模型、训练语音识别软件、部署和托管语音组件——Alan AI后端完成了大部分工作。您的应用程序的语音体验可以由单个开发人员构建和开发，而不是由机器学习和 DevOps专家团队构建和开发，因此您无需额外开销即可向应用添加语音界面。</p>
<p>使用Alan，您可以超越触摸和键入界面的功能，并且语音可以在您的应用程序中启用任何复杂的工作流程或功能。Alan语音脚本是用JavaScript编写的，这使得它们具有高度的可定制性和灵活性。使用Alan创建的语音界面构建一次即可部署在任何地方——您无需为特定平台重建它们。</p>
<h1 data-id="heading-1">二、Alan起步</h1>
<p>想为您的应用创建语音助手吗？请按照以下步骤开始使用Alan。</p>
<h3 data-id="heading-2">1. 注册Alan Studio</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstudio.alan.app" target="_blank" rel="nofollow noopener noreferrer" title="https://studio.alan.app" ref="nofollow noopener noreferrer">注册</a>Alan Studio或登录（如果您已经注册）。</p>
<h3 data-id="heading-3">2. 创建语音脚本</h3>
<blockquote>
<p>选择模板</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50e450d8e8f9463a8c77092d352c33c4~tplv-k3u1fbpfcp-watermark.image" alt="select.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此处选择一个空白模板，如果对脚本不熟悉的话，也可以复制一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstudio.alan.app%2Fprojects" target="_blank" rel="nofollow noopener noreferrer" title="https://studio.alan.app/projects" ref="nofollow noopener noreferrer">语音脚本示例</a>模板来编辑。Alan Studio在线编辑器的界面如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28462c5886304a5e8f7265490d8fca1d~tplv-k3u1fbpfcp-watermark.image" alt="alan-studio.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>编写语音脚本</p>
</blockquote>
<p>在Alan Studio中，编写语音脚本。语音脚本描述了与用户对话的结构，或预期的对话场景。在脚本编辑区输入以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Use this sample to create your own voice commands</span>
intent(<span class="hljs-string">'(going| ) right'</span>, <span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
    p.play(<span class="hljs-string">'Right'</span>);
    p.play(&#123;<span class="hljs-attr">command</span>:<span class="hljs-string">'go-right'</span>&#125;);
&#125;);

intent(<span class="hljs-string">'(going| ) left'</span>, <span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
    p.play(<span class="hljs-string">'Left'</span>);
    p.play(&#123;<span class="hljs-attr">command</span>:<span class="hljs-string">'go-left'</span>&#125;);
&#125;);


intent(<span class="hljs-string">'(going| ) up'</span>, <span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
    p.play(<span class="hljs-string">'Up'</span>);
    p.play(&#123;<span class="hljs-attr">command</span>:<span class="hljs-string">'go-up'</span>&#125;);
&#125;);

intent(<span class="hljs-string">'(going| )down'</span>, <span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
    p.play(<span class="hljs-string">'Down'</span>);
    p.play(&#123;<span class="hljs-attr">command</span>:<span class="hljs-string">'go-down'</span>&#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要让用户与您的语音助手交互，您需要添加用户可以提供的语音脚本命令。 语音命令描述了用户想要完成的任务或操作。了解如何定义语音命令以及可以为这些命令触发哪些响应操作。</p>
<blockquote>
<p>意图</p>
</blockquote>
<p>您可以使用<code>intent()</code>函数在脚本中定义语音命令。该功能可用于完成用户要求的任务或回答用户的问题。</p>
<p>在<code>intent()</code>函数中，您必须指定一种或多种模式 — 调用命令的用户话语，以及调用命令时必须触发的一种或多种响应操作。命令和响应部分支持正则表达式、通配符。详细语法详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fserver-api%2Fpatterns" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/server-api/patterns" ref="nofollow noopener noreferrer">模式</a>。</p>
<p>编写命令时，您可以将预定义和用户定义的插槽添加到意图模式。插槽是用户话语中的“变量”，允许Alan识别和检索有用的信息。</p>
<blockquote>
<p>响应</p>
</blockquote>
<p>在Alan中，您可以通过以下功能触发语音命令的响应操作：</p>
<ul>
<li>play()</li>
<li>reply()</li>
</ul>
<p><code>play()</code>是用于响应操作的预定义函数。您可以使用它来响应用户或向客户端应用程序发送命令。</p>
<h5 data-id="heading-4">响应用户</h5>
<p>要向用户播放响应，您需要在<code>play()</code>函数中定义一个模式。Alan将使用这句话作为回应。在上面示例中，当用户说：<code>going right</code>或<code>right</code>会调用该命令。 作为响应操作，Alan向用户播放文本<code>Right</code>。</p>
<h5 data-id="heading-5">向App发送命令</h5>
<p><code>play()</code>函数可用于向与Alan集成的客户端应用程序发送命令。此类命令可让您在应用程序端执行特定活动，例如，导航到应用程序中的另一个页面、突出显示屏幕上的UI元素等。通过这种方式，您可以同步语音和视觉效果，并为您的应用创建多模式界面。</p>
<p>要发送命令，请将JSON传递给<code>play()</code>函数。在上面示例中，当用户说：<code>going right</code>或<code>right</code>会调用该命令。 作为响应操作，Alan向客户端App发送<code>go-right</code>命令。当然，更灵活的方式发送命令的同时</p>
<p>要在应用程序端处理命令，您必须为从 Alan 的语音脚本接收到的命令定义处理程序。有关详细信息，请参阅 <a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fmethods%2Fcommand-handler" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/methods/command-handler" ref="nofollow noopener noreferrer">onCommand</a>处理程序。</p>
<h5 data-id="heading-6">响应</h5>
<p><code>reply()</code>是一个预定义的函数，如果你只需要给用户一个响应，不需要做任何复杂的动作，就可以使用它。</p>
<pre><code class="hljs language-js copyable" lang="js">intent(<span class="hljs-string">'Say $(W hello|goodbye)'</span>,
  reply(<span class="hljs-string">'$(W)'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实就是<code>play(语音文本)</code>，在<code>reply()</code>函数中，您可以像在play()函数中一样使用模式和插槽。</p>
<blockquote>
<p>意图匹配</p>
</blockquote>
<p>您的项目可以有许多语音命令。当用户发出命令时，Alan会将命令与脚本中最合适的意图进行匹配。为此，Alan 分别评估每个意图，并为意图分配不同的权重或匹配分数。</p>
<p>匹配分值范围从1（最准确的匹配）到0（不匹配）。得分最高的命令被选为最佳匹配。</p>
<p>在下面的示例中，如果用户询问：天气如何？第一个意图将被选为最佳匹配。 第二个意图将不会被匹配，因为它包含的单词比用户的话语多。 反之亦然，如果用户问：今天的天气如何？第二个意图将获得更高的分数，因为它是最准确的匹配。</p>
<pre><code class="hljs language-js copyable" lang="js">intent(<span class="hljs-string">'What is the weather?'</span>, <span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
  p.play(<span class="hljs-string">'The weather is a word'</span>);
&#125;);

intent(<span class="hljs-string">'What is the weather today?'</span>, <span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
  p.play(<span class="hljs-string">'The weather today is great!'</span>)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详细语法<a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fserver-api%2Fscript-concepts" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/server-api/script-concepts" ref="nofollow noopener noreferrer">服务端API</a></p>
<h3 data-id="heading-7">3. 集成到应用程序中</h3>
<p>在Alan Studio工具栏中点击<code>Integrations</code>，首先要选择整合一样，开发阶段一般选择<code>Development</code>。最重要的复制Alan SDK Key，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e44bd5c5538e4dd38844b1218ef4b08b~tplv-k3u1fbpfcp-watermark.image" alt="sdk-key.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个在客户端调用云服务时会用到。我们还可以在该面板中配置Alan按钮。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3881975659ac4082bbcdd6cfc4459215~tplv-k3u1fbpfcp-watermark.image" alt="customize.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据配置生成相应的嵌入代码，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cae96800c6f44b928e3cba5743ea6f96~tplv-k3u1fbpfcp-watermark.image" alt="sample-code.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面的链接了解如何将不同的客户端平台上的应用程序与Alan集成。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fweb%2Fvanilla" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/web/vanilla" ref="nofollow noopener noreferrer">JavaScript</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fweb%2Freact" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/web/react" ref="nofollow noopener noreferrer">React</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fweb%2Fangular" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/web/angular" ref="nofollow noopener noreferrer">Angular</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fweb%2Fvue" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/web/vue" ref="nofollow noopener noreferrer">Vue</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fweb%2Fember" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/web/ember" ref="nofollow noopener noreferrer">Ember</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fweb%2Felectron" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/web/electron" ref="nofollow noopener noreferrer">Electron</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fweb%2Fionic" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/web/ionic" ref="nofollow noopener noreferrer">Ionic</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fios%2Fios-api" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/ios/ios-api" ref="nofollow noopener noreferrer">iOS</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fandroid%2Fandroid-ap" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/android/android-ap" ref="nofollow noopener noreferrer">Android</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fcross-platform%2Fcordova" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/cross-platform/cordova" ref="nofollow noopener noreferrer">Apache Cordova</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fcross-platform%2FFlutter" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/cross-platform/Flutter" ref="nofollow noopener noreferrer">Flutter</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fcross-platform%2Freact-native" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/cross-platform/react-native" ref="nofollow noopener noreferrer">React Native</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fcross-platform%2Fpowerapps" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/cross-platform/powerapps" ref="nofollow noopener noreferrer">Microsoft PowerApps</a></li>
</ul>
<p>下面将以JavaScript为例进行介绍。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> btn = alanBtn(&#123;
  <span class="hljs-attr">right</span>: <span class="hljs-number">24</span>,
  <span class="hljs-attr">top</span>: <span class="hljs-number">24</span>,
  <span class="hljs-attr">size</span>: <span class="hljs-number">48</span>,
  <span class="hljs-attr">key</span>: <span class="hljs-string">"8fc5f867070d9b45dbfb01d46106baf62e956eca572e1d8b807a3e2338fdd0dc/stage"</span>,
  <span class="hljs-attr">onCommand</span>: <span class="hljs-function">(<span class="hljs-params">commandData</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(commandData);
    <span class="hljs-keyword">let</span> style = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"circle"</span>).style;
    <span class="hljs-keyword">const</span> command = commandData.command;
    <span class="hljs-keyword">if</span> (command === <span class="hljs-string">"go-right"</span>) &#123;
      style.transform += <span class="hljs-string">"translateX(50px)"</span>;
    &#125;
    ...
  &#125;,
  <span class="hljs-attr">rootEl</span>: <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"alan-btn"</span>)
&#125;);
btn.activate();
btn.playText(<span class="hljs-string">"you are welcome"</span>);
btn.playCommand(&#123; <span class="hljs-attr">command</span>: <span class="hljs-string">"go-down"</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上面实例Alan按钮最主要的参数有：</p>
<blockquote>
<p>key</p>
</blockquote>
<p>Alan Studio项目的 Alan SDK 密钥。</p>
<blockquote>
<p>rootEl</p>
</blockquote>
<p>添加Alan按钮的元素。如果没有提供rootEl，则将Alan按钮添加到body中。</p>
<blockquote>
<p>onCommand</p>
</blockquote>
<p>用于处理来自Alan语音脚本的命令的回调。在此回调中，您可以设置有关应用程序对语音脚本接收到的命令做出反应的逻辑。</p>
<p>本实例中，我们在客户端应用中使用<code>activate()</code>方法以编程方式打开激活Alan按钮，调用<code>playText()</code>方法播放<code>you are welcome</code>，并使用<code>playCommand()</code>方法执行本地命令，由<code>go-right</code>命令处理程序处理将小球向右移动50px;</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Friafan%2Fpen%2Fwvzdywp" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/riafan/pen/wvzdywp" ref="nofollow noopener noreferrer">点击此处查看</a>完整实例代码。当用户说：<code>going left</code>或<code>left</code>，Alanw会向用户播放文本<code>Left</code>并将小球向左移动50px，其它方向亦然。如果免费语音次数已经使用完，会听到一个语音提示让用户充值。</p>
<h1 data-id="heading-8">三、注意</h1>
<blockquote>
<p>免费用户可以默认交互50次，如果绑定github并给Alan点赞，可以送交互（最多9次）。免费次数用完后，用户需要更改成付费方式并在线充值才能继续使用Alan语音云服务。</p>
</blockquote>
<blockquote>
<p>免费用户有很多功能限制：比如不能使用Alan Studio的测试功能，不能选择整合环境，不能添加编辑配置选项，不能选择多国语音支持等。</p>
</blockquote>
<h1 data-id="heading-9">四、展望</h1>
<p>语音AI会成为未来最主流的交互方式。根据贝恩公司此前的一份调研数据显示，未来人机交互方式中，语音交互将会占到30%左右。</p>
<p>首先，语音AI集成在硬件产品上，开门第一步必须是<strong>听得到听得清</strong>。这其实就是在硬件上考验拾音的问题。</p>
<p>其次，从AI的角度，我们和它产生对话，它听得清当然很重要，<strong>但更重要的是要能够听得懂</strong>。>这里就涉及到比如复杂语意解析、文本分析、自然语言理解等等算法。</p>
<p>最后，是语音AI在工作时的综合体验，比如说唤醒率，再比如说误触率，再比如说交互反馈。</p>
<p>参考：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstudio.alan.app" target="_blank" rel="nofollow noopener noreferrer" title="https://studio.alan.app" ref="nofollow noopener noreferrer">studio.alan.app</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fusage%2Fgetting-started" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/usage/getting-started" ref="nofollow noopener noreferrer">alan.app/docs/usage/…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Falan.app%2Fdocs%2Fclient-api%2Fweb%2Fvanilla" target="_blank" rel="nofollow noopener noreferrer" title="https://alan.app/docs/client-api/web/vanilla" ref="nofollow noopener noreferrer">alan.app/docs/client…</a></li>
</ul></div>  
</div>
            