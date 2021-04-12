
---
title: '移动端调试神器 Whistle'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5ba44d002f74efc92b8d1dc2a1e2a9b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 19:20:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5ba44d002f74efc92b8d1dc2a1e2a9b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">移动端调试神器 Whistle</h2>
<blockquote>
<p>在前端开发中移动端开发技能必不可少。当我们遇到类似于这样的问题：</p>
<ol>
<li>移动端Canvas渲染失败</li>
<li>微信获取openId回调页不匹配</li>
<li>微信浏览器文件上传失败</li>
<li>支付宝，微信H5支付域名校验不匹配</li>
<li>生产环境BUG，dev，test环境无法复现</li>
<li>当后端接口启用cors跨域时，本地环境无法访问</li>
<li>…</li>
</ol>
<p>Chrome模拟器和微信开发者工具等都无法完美复现我们遇到的问题，这时候我们需要用到whistle来实现真机调试</p>
</blockquote>
<h3 data-id="heading-1">Whistle原理</h3>
<p>​Whistle是一个Node实现的跨平台Web调试代理工具。它的作用可以理解为用Node开一个代理服务器，将我们需要调试的设备代理到whistle后，由whistle进行代理请求。同时whistle支持类似于hosts的转发规则，我们可以通过正则或者内置的一些指令对我们需要进行代理的域名进行转发，添加插件等。</p>
<h3 data-id="heading-2">安装whistle</h3>
<p><code>npm install -g whistle</code></p>
<h3 data-id="heading-3">启动whistle</h3>
<p><code>w2 start</code> or <code>w2 start -p 10086</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">➜  ~ w2 start
[!] whistle@2.5.23 is running
[i] 1. use your device to visit the following URL list, gets the IP of the URL you can access:
       http://127.0.0.1:8899/
       http://192.168.97.12:8899/
       Note: If all the above URLs are unable to access, check the firewall settings
             For <span class="hljs-built_in">help</span> see https://github.com/avwo/whistle
[i] 2. configure your device to use whistle as its HTTP and HTTPS proxy on IP:8899
[i] 3. use Chrome to visit http://local.whistlejs.com/ to get started
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们已经开启了whistle的代理，通过浏览器访问<code>http://127.0.0.1:8899/</code>即可看到 whistle控制台。</p>
<p><img alt="image-20210326215735158" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5ba44d002f74efc92b8d1dc2a1e2a9b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>接下来我将介绍在window、mac、iPhone、Android中分别如何利用whistle进行代理抓包。</p>
</blockquote>
<h3 data-id="heading-4">设置代理</h3>
<h4 data-id="heading-5">移动端设置代理</h4>
<p>连接到同一个WIFI下，iPhone及Android在wifi中设置代理，代理IP为：192.168.97.12（即是上面打印出来的局域网IP），端口号为：8899（也可以通过<code>-p 10086</code> ）指定自定义端口号。保存后我们的移动端设备就已经连接上了whistle。</p>
<p><img alt="image-20210326221102437" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19d08075acca4ec293999a3b415b56a8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">PC端设置代理</h4>
<p>因为我们在PC日常开发中，常用Chrome浏览器，所以这里只展示下Chrome浏览器下的代理设置。</p>
<p>PC端Chrome代理时，我这里推荐使用 Proxy switchyOmega（Chrome插件） 下载完成后，进入SwitchOmege配置。默认安装后，会有一个名为<code>proxy</code>的情景模式，我们将其改名为<code>Whistle</code>。</p>
<p><img alt="image-20210326221533231" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dccccfba4f0946c6a94d3d3c4b2ae77a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>修改完名字后，我们将我们的局域网IP及whistle的端口号填入到代理服务器中并应用选项。</p>
<p><img alt="image-20210326221755673" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36cf8d3e901144ffaa2d3a23cec6d505~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>此时，我们就可以进行whistle在PC端的代理，这里还推荐修改一个配置。默认代理模式为<code>系统代理</code>，因为众所周知的原因，基本上程序员都会进行科学上网，所以这里将默认配置改为<code>系统代理</code>，避免我们日常使用时被代理到whistle，无法科学上网的问题。</p>
<p><img alt="image-20210326222041688" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7048996e1be94965a7a4dd33214392bc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">安装HTTPS证书</h3>
<blockquote>
<p>现在基本上绝大多数域名都是走HTTPS协议，所以想要whistle进行HTTPS协议的代理我们还需要安装HTTPS证书。</p>
</blockquote>
<h4 data-id="heading-8">下载证书</h4>
<p>PC端：点击顶部工具栏中的<code>HTTPS</code>，打开whistle的HTTPS证书弹框，点击<code>Download RootCA</code>下载HTTPS证书。</p>
<p>移动端：连接上whistle代理后，通过浏览器扫码，会自动下载证书</p>
<p><img alt="image-20210410113710728" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d91b8196241436f8cbf80f0cc0001f0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">window安装证书</h4>
<p>下载完成后双击打开，将证书安装到<code>受信任的根证书颁发机构 </code> 完成安装即可。</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/547fe977b2bd40c2a64450f87c4c81bb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">Mac安装证书</h4>
<p>下载完成后双击打开，将证书安装到本地项目或者登录都可以，之后在你安装的地方搜索<code>whistle</code>，双击打开，选择<code>信任</code>，设置为<code>始终信任</code></p>
<p><img alt="image-20210322103214768" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27fe2c2f538f4c97a83a8e6d8bc1844e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">iPhone安装证书</h4>
<p>设置----通用-----关于本机------证书信任设置------>找到whistle证书打开信任</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ffbcf50c70b47cba81c1a750f3ffad5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12142d1a00cd49a28727f6761e0d7311~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h4 data-id="heading-12">Android安装证书</h4>
<p>视各个厂商系统而定，可以在具体扫码后根据提示设置。</p>
<h3 data-id="heading-13">Weinre调试</h3>
<blockquote>
<p>好了，至此我们完成了whistle的所有准备工作，接下来介绍whistle中给我们提供的功能</p>
</blockquote>
<h4 data-id="heading-14">redirect 重定向</h4>
<p>打开whistle控制台，我们可以看到左侧有个<code>Rules</code>，在这里面我们可以进行一些跳转规则的分组，配置。这里的配置类似于我们日常会修改的hosts文件的配置，前面的域名是需要代理的域名，后面的是需要指向的地址。这里我将<code>https://www.baidu.com</code> 重定向到 <code>https://www.bilibili.com</code>。</p>
<p>【！！注意！！ 这里在iPhone上有个坑，在iPhone上调试的时候，前面的域名一定要加上<code>https</code>，不然在iPhone中会出现证书验证不过的问题】</p>
<p><img alt="image-20210326233501378" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/762d30c54bbe4c20976b735680985c64~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后我们新开tab页，切换switchOmega到我们刚刚设置的<code>Whistle</code>情景模式，输入<code>https://www.baidu.com</code> 可以看到现在百度已经被成功跳转到B站了。</p>
<p><img alt="image-20210326233717709" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/640c8f502ed344318b21dfc5b54e19d5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>重定向在我们日常中的使用还是比较广阔的，举个例子：</p>
<ol>
<li>当我们需要在本地访问线上接口时，会有cors跨域问题，这时候可以通过伪装域名来绕过这个限制</li>
<li>当我们在开发微信或者支付宝相关功能时，此时微信或支付宝后台有安全域名限制，这时候也可以通过这个重定向来完成</li>
</ol>
</blockquote>
<h4 data-id="heading-15">log 日志打印</h4>
<p>移动端调试最痛苦的莫过于完全没办法看到log日志，特别是在生产环境下时我们也无法通过vconsole或者eruda等工具来辅助我们查看。所以这里我们可以通过在whistle中添加<code>log://</code>关键字来导出console日志。</p>
<p><img alt="image-20210326234340332" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d15c71b46427440582e94b85befcacbf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>配置好后，切换到<code>Network</code>选项中，我们可以在这里看到所有http请求，以此来排查接口或者资源请求等问题。选择到我们打开的域名所在的请求，例如我这里用<code>https://www.baidu.com</code> 举例。再通过右侧工具栏的<code>Tools</code>即可看到我们页面中使用到的<code>console</code></p>
<p><img alt="image-20210326234824802" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4729c6994c34420a82e93213ecd8e718~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这个功能适合我们在排查一些生产问题时，通过log日志去追踪问题所在，或者看到js中出现了那些错误。在一些机型兼容问题排查时有很大的帮助作用。</p>
</blockquote>
<h4 data-id="heading-16">jsPrepend js注入</h4>
<p>whistle支持让我们在加载网页时进行预制javascript代码的注入，点击左侧栏的<code>Values</code>，打开js脚本管理。这里我以注入<code>eruda</code>为例，首先我们去npm或者bootcdn等类似的网站上找到我们想要注入的一些工具库，例如我这里使用了<code>eruda.min.js</code>。通过<code>Create</code>创建一个新的脚本。将脚本文件拷贝进去。</p>
<p><img alt="image-20210326235356195" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b670b758955a40db813ab996cb0e18a8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后新建脚本<code>eruda.js</code>嵌入初始化代码</p>
<p><img alt="image-20210326235756498" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7699b684139e4810b5efc951b97c0c61~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>OK，做好准备工作。我们再回到<code>Rules</code>中进行js注入的配置，这里我们注入刚刚写的<code>eruda.min.js</code>和<code>eruda.js</code></p>
<p><img alt="image-20210327000604498" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c65bfcfb2d634b0093ba76658aeb13ca~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后我们再去打开下<code>https://m.baidu.com</code>查看下效果，可以看到eruda已经注入进来了</p>
<p><img alt="image-20210412173452901" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a25d440ecb9f40beba8dfe058a12dcec~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>因为移动端不像Chrome的devTool一样，可以自由的修改及运行js代码，所以这个功能给我们提供了这种可能。同时也让我们可以在测试生产环境代码时可以注入一些方便调试的工具库进来。</p>
</blockquote>
<h4 data-id="heading-17">weinre 移动端调试</h4>
<p>weinre是一个历史悠久的移动端调试工具，其界面仿照Chrome的DevTool设计，可以轻松的看到Dom树的结构，Network请求，Console等等，不过因为其历史悠久目前稳定性较差，有些时候并不一定百分百生效，而且配置起来相对麻烦。whistle中也内置了weinre，让我们能够轻松快捷的去使用weinre。</p>
<p>同样，我们打开<code>Rules</code>，然后加<code>https://www.baidu.com</code>中加上<code>weinew://baidu</code>这个指令（这里最后的baidu是指weinre的实例名，可以自由指定）</p>
<p><img alt="image-20210327001520630" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f753b1a3d95c4be69540776540ca52c4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>完成后，我们可以通过顶部工具栏的<code>Weinre</code>中可以看到我们添加的<code>baidu</code>实例，点击后即可进入weinre调试中。<img alt="image-20210327001746390" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa2301fb0b714685848b628133e3f7b1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在浏览器中打开<code>https://www.baidu.com</code>后，即可看到weinre中提示百度已经连接上来了。</p>
<p><img alt="image-20210327001904186" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95d894b389be41a7bb1a1868c5bde941~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>至此，whistle中常用的功能大概介绍完毕了。whistle中支持的功能还有很多，以上只是介绍了一些前端调试中经常用到功能，如果感兴趣的同学可以自行再去研究下<a href="http://wproxy.org/whistle/" target="_blank" rel="nofollow noopener noreferrer">whistle文档</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            