
---
title: 'web项目对接钉钉扫码登录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/072cbeba0e244423a42b447dfb69511a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:44:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/072cbeba0e244423a42b447dfb69511a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0"><a href="https://juejin.cn/post/6943478980972380168"></a>写在前面</h4>
<p>今天我们记录一下关于vue进行web开发的过程中对接钉钉的H5微应用的时候扫码登录的功能，你说他难吧，其实不难，很简单，你说他简单吧，看文档可能真的有点乱，不然您也不会来看我的帖子，我也看了别的大佬们写的关于这个的记录，不是说写的有问题，只是说很少有人站在别人开发的角度看待问题，导致很多人觉得还是不明白，所以今天就我写的过程中出现的问题进行描述一下大家可能迷茫的地方，尽量让每个开发者都看得懂！<br>
感谢以下提供支持的博主：<br>
<a href="https://blog.csdn.net/weixin_43788115/article/details/103560146" target="_blank" rel="nofollow noopener noreferrer">填了个大空</a><br>
<a href="https://blog.csdn.net/qq_24510455/article/details/97146126" target="_blank" rel="nofollow noopener noreferrer">易-水寒</a></p>
<h4 data-id="heading-1"><a href="https://juejin.cn/post/6943478980972380168"></a>官方文档地址</h4>
<p><a href="https://ding-doc.dingtalk.com/doc#/serverapi2/kymkv6" target="_blank" rel="nofollow noopener noreferrer">官方地址</a></p>
<ul>
<li>官方呢提供了两种实现的思路，也是不同的形式，具体使用哪一种呢，你们自己视情况而定</li>
</ul>
<h4 data-id="heading-2"><a href="https://juejin.cn/post/6943478980972380168"></a>方案一</h4>
<ul>
<li>方案一呢是不需要我们进行写二维码的实现过程的，这里直接使用官方的一个链接，也就是这个链接</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">https:<span class="hljs-comment">//oapi.dingtalk.com/connect/qrconnect?appid=APPID&response_type=code&scope=snsapi_login&state=STATE&redirect_uri=REDIRECT_URI</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3"><a href="https://juejin.cn/post/6943478980972380168"></a>redirect_uri</h5>
<ul>
<li>这个链接两个点需要注意，第一个是redirect_uri参数，是通过后台配置的，具体什么位置配置的呢？看截图：</li>
<li><img alt="回调地址" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/072cbeba0e244423a42b447dfb69511a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
这个需要你们的管理员进去，然后按照图示找到配置的地方，这里有人就问了，这个地址写什么？一般的话写的是您的web的登录入口的地址，比如说我的是https://csdn.clearlove/#login,那么你们就写自己的登录地址就好了。</li>
</ul>
<h5 data-id="heading-4"><a href="https://juejin.cn/post/6943478980972380168"></a>appid</h5>
<ul>
<li>这个参数同上，只要点击了创建扫码登录应用授权以后这个会自动生成的。</li>
</ul>
<blockquote>
<p>有了以上两个参数，就基本ok了，很多博主也是写到这里就不写了，所以很多人就迷茫了，这也不行啊，怎么登录的啊，下面的步骤是登录的部分，如果您使用了方案一，会发现点击扫码登录的时候会直接跳到一个新的页面，然后生成一个二维码，就像这样：<br>
<img alt="类似这样的二维码" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23e2e96cbb464c069877f5c1650ba39e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
有人说这个二维码怎么跳转过来的，很简单，就一个href，写一个span或者按钮的东西，事件绑定到下面的这个函数，点击执行函数就可以了，代码如下：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//扫码登录</span>
            <span class="hljs-function"><span class="hljs-title">sweep_code</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">window</span>.location.href = <span class="hljs-string">"https://oapi.dingtalk.com/connect/qrconnect?appid=*******************&response_type=code&scope=snsapi_login&state=STATE&redirect_uri=https://csdn.clearlove/#/login"</span>
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后我们需要做的就是扫码，扫码之后会发现，他会回调到你地址上的redirect_uri这个参数的值的地址，也就是login的页面，这个时候我们需要做的就是将回调地址里面的code和state获取到，怎么获取呢？<br>
如图：<br>
<img alt="回调url" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f0d584802b44e1a51f257db0808de4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
-我们使用下面的代码进行获取url中的code 和state</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@aim </span>get code from url
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@data </span>19-09
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">getUrlKey</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">decodeURIComponent</span>((<span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'[?|&]'</span>+name+<span class="hljs-string">'='</span>+<span class="hljs-string">'([^&;]+?)(&|#|;|$)'</span>).exec(location.href)||[,<span class="hljs-string">""</span>])[<span class="hljs-number">1</span>].replace(<span class="hljs-regexp">/\+/g</span>,<span class="hljs-string">'%20'</span>))||<span class="hljs-literal">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将这段js放到您的工具分类中，然后在login页面导入（您直接写到login页面也可以，只是这个js偏工具类，所以个人建议单独拿出来比较好,如果您是直接写到login的话，就不要写export了，直接当作一个函数使用就好了，真的是为你们操碎了心），然后直接使用getUrlKey方法进行获取code，我们在我们的login.vue文件（你的登录页面也就是你的回调地址指向的页面）在created的生命周期中进行如下代码操作，具体代码如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.code = <span class="hljs-built_in">this</span>.$utils.getUrlKey(<span class="hljs-string">'code'</span>) <span class="hljs-comment">//这个是用来给后端获取用户信息的</span>
<span class="hljs-built_in">this</span>.state = <span class="hljs-built_in">this</span>.$utils.getUrlKey(<span class="hljs-string">'state'</span>) <span class="hljs-comment">//这个只是为了防止攻击的， 没有这个参数也可以，看后端要不要这个参数了，具体情况来定</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>下面就是将code作为参数给到后端，他返回登录信息给您，然后您判断成功以后进如系统就可以了，为了让你们明白，我简单的画一个流程：<br>
<img alt="流程" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dbecbbd9d17463c8c69e1439c26cccb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
以上是第一种方案，我这么写估计都明白了，还不明白的话，就下面留言吧！</li>
</ul>
<h4 data-id="heading-5"><a href="https://juejin.cn/post/6943478980972380168"></a>方案二</h4>
<blockquote>
<p>很多人迷茫的更多的是使用方案2进行实现的过程，那其实方案2和方案一的区别就是一个体验稍微好点，因为不用跳转页面了，就比如我做的这个：<br>
<img alt="扫码登录" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d837f6a54c8403bb174331d2b66c0c9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
这种的实现过程其实差不多的，下面分两种情况，第一种是使用vue2.0版本的，第二种是vue3.0版本的</p>
</blockquote>
<h5 data-id="heading-6"><a href="https://juejin.cn/post/6943478980972380168"></a>vue2.0</h5>
<p>直接在您的index.html中引入如下的代码</p>
<pre><code class="hljs language-js copyable" lang="js"><script src=<span class="hljs-string">"https://g.alicdn.com/dingding/dinglogin/0.0.5/ddLogin.js"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在登录的页面进行二维码的生成，这里说一点，就是二维码的生成以后的操作和方案一是一摸一样的，所以方案二我写的时候就写到如何生成二维码，有了二维码以后 ，扫码、回调、获取code、根据code获取用户信息、登录这一系列就和方案一一模一样了，这也是为什么方案一写的那么详细的原因，废话不多话，引入上面的钉钉的js以后呢，接着在页面上找一块你需要生成二维码的div，比如这样：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"height: 310px;background: #ffffff"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ding-login"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"isShow === 'ding'"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这里说明一下，要不要这个v-show都可以，我是提供了账号登录和扫码登录的功能，所以我需要切换，用到了v-show,您如果只有扫码登录，就完全不用，明白吧！<br>
接着我们需要在页面上直接在methods中使用如下代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">dingLogin</span>(<span class="hljs-params"></span>)</span> &#123;
                    <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
                        <span class="hljs-keyword">var</span> obj = DDLogin(&#123;
                            <span class="hljs-attr">id</span>: <span class="hljs-string">"ding-login"</span>,
                            <span class="hljs-attr">goto</span>: <span class="hljs-built_in">this</span>.http_url,
                            <span class="hljs-attr">style</span>: <span class="hljs-string">"border:none;background-color:#FFFFFF;"</span>,
                            <span class="hljs-attr">width</span>: <span class="hljs-string">"300"</span>, <span class="hljs-comment">// 二维码的宽度</span>
                            <span class="hljs-attr">height</span>: <span class="hljs-string">"300"</span> <span class="hljs-comment">// 二维码的高度</span>
                        &#125;)
                        <span class="hljs-comment">// 重置扫码登录框的样式，让登录框居中</span>
                        <span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'ding-login'</span>)
                        box.querySelector(<span class="hljs-string">'iframe'</span>).style.top = <span class="hljs-string">'0'</span>
                        box.querySelector(<span class="hljs-string">'iframe'</span>).style.bottom = <span class="hljs-string">'0'</span>
                        box.querySelector(<span class="hljs-string">'iframe'</span>).style.left = <span class="hljs-string">'0'</span>
                        box.querySelector(<span class="hljs-string">'iframe'</span>).style.right = <span class="hljs-string">'0'</span>
                        box.querySelector(<span class="hljs-string">'iframe'</span>).style.margin = <span class="hljs-string">'auto'</span>
                    &#125;)
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>说明：dingLogin这个函数就是点击扫码登录的时候调用的函数</p>
</blockquote>
<ul>
<li>然后我们在created里实现如下代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">scansettings().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                <span class="hljs-built_in">this</span>.appid = res.data.appkey
                <span class="hljs-built_in">this</span>.appSecret = res.data.appsecret
                <span class="hljs-built_in">this</span>.redirect_uri = res.data.redirect_uri
                <span class="hljs-built_in">this</span>.redirects = <span class="hljs-built_in">encodeURIComponent</span>(<span class="hljs-built_in">this</span>.redirect_uri)
                <span class="hljs-built_in">this</span>.http_url = <span class="hljs-built_in">encodeURIComponent</span>(<span class="hljs-string">"https://oapi.dingtalk.com/connect/oauth2/sns_authorize?appid="</span> + <span class="hljs-built_in">this</span>.appid + <span class="hljs-string">"&response_type=code&scope=snsapi_login&state=STATE&redirect_uri="</span> + <span class="hljs-built_in">this</span>.redirects + <span class="hljs-string">""</span>)
                <span class="hljs-comment">// 获取到扫码结果，并且跳转获取临时登录码</span>
                <span class="hljs-keyword">var</span> handleMessage = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
                    <span class="hljs-keyword">var</span> origin = event.origin;
                    <span class="hljs-keyword">if</span> (origin == <span class="hljs-string">"https://login.dingtalk.com"</span>) &#123;
                        <span class="hljs-keyword">var</span> loginTmpCode = event.data;
                        <span class="hljs-keyword">let</span> url = <span class="hljs-string">"https://oapi.dingtalk.com/connect/oauth2/sns_authorize?appid="</span> + <span class="hljs-built_in">this</span>.appid + <span class="hljs-string">"&response_type=code&scope=snsapi_login&state=STATE&redirect_uri="</span> + <span class="hljs-built_in">this</span>.http_url + <span class="hljs-string">"&loginTmpCode="</span> + loginTmpCode + <span class="hljs-string">""</span>
                        location.href = url
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        <span class="hljs-built_in">console</span>.info(event)
                    &#125;
                &#125;;
                <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span>.addEventListener != <span class="hljs-string">'undefined'</span>) &#123;
                    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, handleMessage, <span class="hljs-literal">false</span>);
                &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span>.attachEvent != <span class="hljs-string">'undefined'</span>) &#123;
                    <span class="hljs-built_in">window</span>.attachEvent(<span class="hljs-string">'onmessage'</span>, handleMessage);
                &#125;
            &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
                <span class="hljs-built_in">console</span>.error(err)
            &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里很多人看完以后就迷茫了，我简单的解释一下，官方给的源代码是这样的，<a href="https://ding-doc.dingtalk.com/doc#/serverapi2/kymkv6" target="_blank" rel="nofollow noopener noreferrer">官方源代码</a>，区别在哪呢？其实就是参数获取的问题，因为这里我的appid和appSecret和回调的地址redirect_uri都是后端接口((scansettings)返回的，所以我页面加载的时候就直接请求接口，进行参数的获取，这里如果您这三个参数都是您自己写死的，那么您完全可以直接使用官方的代码，不过要加一行，也就是 location.href = url这点代码，不然没办法回调回来，官方说的原话是“获取到loginTmpCode后就可以在这里构造跳转链接进行跳转了”，具体怎么跳转，就是这点代码，然后你会发现二维码扫码以后就可以直接回调了，然后和方案一就一样了，这里还有一个点需要注意，就是回调的地址需要encodeURIComponent进行转码，这步是为了解决浏览器对特殊参数强制转码导致的url错乱的问题。</p>
</blockquote>
<h4 data-id="heading-7"><a href="https://juejin.cn/post/6943478980972380168"></a>vue3.0</h4>
<ul>
<li>如果您使用的是vue3.0的版本，会发现有的时候index.html这个文件没有了，怎么办呢？那2.0和3.0的代码写法是一样，区别在于怎么引入钉钉的js的问题，这里直接在export中引入如下代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">components: &#123;
            <span class="hljs-string">'dingtalk'</span>: &#123;
                <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">createElement</span>)</span> &#123;
                    <span class="hljs-keyword">return</span> createElement(
                        <span class="hljs-string">'script'</span>,
                        &#123;
                            <span class="hljs-attr">attrs</span>: &#123;
                                <span class="hljs-attr">type</span>: <span class="hljs-string">'text/javascript'</span>,
                                <span class="hljs-attr">src</span>: <span class="hljs-string">'https://g.alicdn.com/dingding/dinglogin/0.0.5/ddLogin.js'</span>,
                            &#125;,
                        &#125;,
                    );
                &#125;,
            &#125;,
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后我们在页面上直接使用</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">   <span class="hljs-tag"><<span class="hljs-name">dingtalk</span>></span><span class="hljs-tag"></<span class="hljs-name">dingtalk</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就引入了 ，下面的写法就和2.0一样了！</p>
<h5 data-id="heading-8"><a href="https://juejin.cn/post/6943478980972380168"></a>不用vue怎么实现钉钉扫码登录呢？</h5>
<p>这个就比较简单了，上面的函数一样的写，区别在于vue存在生命周期，所以我们可以在created中实现code的获取，那一般的web项目我们只需要写到windows.onload的时候就可以了，有人就觉得，那么如果是两种方式（账号登录和扫码登录）都支持的话，是不是每次进来的时候就会报错呢？提示什么code不存在什么的，这个问题很好解决，只要我们获取code之前if判断一下code是不是存在，不存在再进行code的获取就好了！</p>
<blockquote>
<p>如果对这个扫码登录还有什么问题的话，可以留言，我看到的会及时回复的，我追求的是博客不写就不写了，既然写了，就追求每个开发者都看得懂！</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            