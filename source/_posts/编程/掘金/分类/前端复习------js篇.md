
---
title: '前端复习------js篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1f5ad831dc443e38b1aa99b10e3a4c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 06:28:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1f5ad831dc443e38b1aa99b10e3a4c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">javascript运行原理</h2>
<ul>
<li>Parse模块会将JavaScript代码转换成AST（抽象语法树），这是因为解释器并不直接认识JavaScript代码；</li>
<li>
<ul>
<li>如果函数没有被调用，那么是不会被转换成AST的；</li>
<li>Parse的V8官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Fscanner" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/scanner" ref="nofollow noopener noreferrer">v8.dev/blog/scanne…</a></li>
</ul>
</li>
<li>Ignition是一个解释器，会将AST转换成ByteCode（字节码）</li>
<li>
<ul>
<li>同时会收集TurboFan优化所需要的信息（比如函数参数的类型信息，有了类型才能进行真实的运算）；</li>
<li>如果函数只调用一次，Ignition会执行解释执行ByteCode；</li>
<li>Ignition的V8官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Fignition-interpreter" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/ignition-interpreter" ref="nofollow noopener noreferrer">v8.dev/blog/igniti…</a></li>
</ul>
</li>
<li>TurboFan是一个编译器，可以将字节码编译为CPU可以直接执行的机器码；</li>
<li>
<ul>
<li>如果一个函数被多次调用，那么就会被标记为热点函数，那么就会经过TurboFan转换成优化的机器码，提高代码的执行性能；</li>
<li>但是，机器码实际上也会被还原为ByteCode，这是因为如果后续执行函数的过程中，类型发生了变化（比如sum函数原来执行的是number类型，后来执行变成了string类型），之前优化的机器码并不能正确的处理运算，就会逆向的转换成字节码；</li>
<li>TurboFan的V8官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Fturbofan-jit" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/turbofan-jit" ref="nofollow noopener noreferrer">v8.dev/blog/turbof…</a></li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1f5ad831dc443e38b1aa99b10e3a4c6~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面是JavaScript代码的执行过程，事实上V8的内存回收也是其强大的另外一个原因，这里暂时先不展开讨论：</p>
<ul>
<li>Orinoco模块，负责垃圾回收，将程序中不需要的内存回收；</li>
<li>Orinoco的V8官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Ftrash-talk" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/trash-talk" ref="nofollow noopener noreferrer">v8.dev/blog/trash-…</a></li>
</ul>
<h2 data-id="heading-1">解释型语言和编译型语言</h2>
<p>编译型语言是代码在运行前编译器将人类可以理解的语言（编程语言）转换成机器可以理解的语言。</p>
<p>解释型语言也是人类可以理解的语言（编程语言），也需要转换成机器可以理解的语言才能执行，但是是在运行时转换的。所以执行前需要环境中安装了解释器；但是编译型语言编写的应用在编译后能直接运行。</p>
<h2 data-id="heading-2">跨域</h2>
<p>疑问： session和cookie的关系？并且后端通过ctx.session.名获取到的session是前端通过localStorage设置的还是后端通过this.ctx.session.名设置的？</p>
<ul>
<li>session是保存在服务端的。就是后端设置session，前端请求时，将<code>withCredentials</code>设置为true，就会发送cookie到服务端。</li>
<li>服务端执行session机制时候会生成session的id值，这个id值会发送给客户端，客户端每次请求都会把这个id值放到http请求的头部发送给服务端，而这个id值在客户端会保存下来，保存的容器就是cookie，因此当我们完全禁掉浏览器的cookie的时候，服务端的session也会不能正常使用。</li>
<li>Session是在服务端保存的一个数据结构，用来跟踪用户的状态，这个数据可以保存在集群、数据库、文件中；</li>
<li>Cookie是客户端保存用户信息的一种机制，用来记录用户的一些信息，也是实现Session的一种方式。</li>
</ul>
<h4 data-id="heading-3">cors设置</h4>
<p>在后端设置一些特定的响应头。</p>
<pre><code class="copyable">//设置哪个源可以访问
  ctx.set("Access-Control-Allow-Origin", ctx.headers.origin);
//允许携带cookie
  ctx.set("Access-Control-Allow-Credentials", true);
//允许那些方法访问我
  ctx.set("Access-Control-Request-Method", "PUT,POST,GET,DELETE,OPTIONS");  
//允许携带那个头部访问我
  ctx.set("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, cc");
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">关于 cors 的 cookie 问题</h5>
<p>想要传递 <code>cookie</code> 需要满足 3 个条件</p>
<p>1.web 请求设置<code>withCredentials</code></p>
<p>这里默认情况下在跨域请求，浏览器是不带 cookie 的。但是我们可以通过设置 <code>withCredentials</code> 来进行传递 <code>cookie</code>.</p>
<pre><code class="copyable">// 原生 xml 的设置方式
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
// axios 设置方式
axios.defaults.withCredentials = true;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.<code>Access-Control-Allow-Credentials</code> 为 <code>true</code></p>
<p>3.<code>Access-Control-Allow-Origin</code>为非 <code>*</code></p>
<p>这里请求的方式，在 <code>chrome</code> 中是能看到返回值的，但是只要不满足以上其一，浏览器会报错，获取不到返回值。</p>
<p><img src="https://juejin.cn/post/6990725554852855839" alt="image-20200812161453822" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">正向代理</h4>
<p>代理的思路为，利用服务端请求不会跨域的特性，让接口和当前站点同域。</p>
<p>就是在各个框架的json文件中，设置一个proxy选项。不同框架设置不同，所以用到时，自己搜索即可。 xxx proxy</p>
<h4 data-id="heading-6">JSONP</h4>
<p><code>JSONP</code> 主要就是利用了 <code>script</code> 标签没有跨域限制的这个特性来完成的。<strong>只支持get方法</strong>。</p>
<p>原理：JSONP 的理念就是，与服务端约定好一个回调函数名，服务端接收到请求后，将返回一段 Javascript，在这段 Javascript 代码中调用了约定好的回调函数，并且将数据作为参数进行传递。当网页接收到这段 Javascript 代码后，就会执行这个回调函数，这时数据已经成功传输到客户端了。</p>
<p>前端代码</p>
<p>前端定义一个回调函数，然后通过请求路径将该回调当成参数传递。</p>
<pre><code class="copyable">// 1. 创建回调函数callback
function Callback(res) &#123;
    alert(JSON.stringify(res, null , 2));
&#125;
document.getElementById('btn-4').addEventListener('click', function() &#123;
    // 2. 动态创建script标签，并设置src属性，注意参数cb=Callback
    var script = document.createElement('script');
    script.src = 'http://127.0.0.1:3000/api/jsonp?cb=Callback';
    document.getElementsByTagName('head')[0].appendChild(script);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后端代码</p>
<p>通过前端传过来的回调函数，我们将返回该函数的调用。</p>
<pre><code class="copyable">router.get('/api/jsonp', (req, res, next) => &#123;
    var str = JSON.stringify(data);
    // 3. 创建script脚本内容，用`callback`函数包裹住数据
    // 形式：callback(data)
    var script = `$&#123;req.query.cb&#125;($&#123;str&#125;)`;//这里就是callback(data),当前端请求接口时，就会回调该函数
    res.send(script);
&#125;);
// 4. 前端收到响应数据会自动执行该脚本
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">WebSocket</h4>
<p>这种方式本质没有使用了 HTTP 的响应头, 因此也没有跨域的限制，没有什么过多的解释直接上代码吧。</p>
<p>前端代码</p>
<pre><code class="copyable"><script>  
    let socket = new WebSocket("ws://localhost:80");  
    socket.onopen = function() &#123;    socket.send("返回的内容");  &#125;;  
    socket.onmessage = function(e) &#123;    console.log(e.data);  &#125;;
</script>
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">nginx反向代理</h4>
<p>以后再学，设计nginx知识。</p>
<blockquote>
<p>学习</p>
<p><a href="https://juejin.im/post/6844904126246027278#heading-28" target="_blank" title="https://juejin.im/post/6844904126246027278#heading-28">非常详细的跨域解决方案</a></p>
<p><a href="https://juejin.im/post/6844903767226351623" target="_blank" title="https://juejin.im/post/6844903767226351623">九种跨域方式实现原理（完整版）</a></p>
</blockquote>
<h2 data-id="heading-9">鉴权</h2>
<h4 data-id="heading-10">cookie</h4>
<p>服务端通过set-cookie设置cookie的信息。</p>
<p><img src="https://juejin.cn/post/6990725554852855839" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">Session</h4>
<blockquote>
<p>session 是另一种记录服务器和客户端会话状态的机制。session存储在服务器端，该会话对应的key即sessionId会被存储到客户端的cookie中。</p>
</blockquote>
<p><img src="https://juejin.cn/post/6990725554852855839" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据以上流程可知，session通过cookie来传递sessionId，达到用户鉴权的目的。除此之外，sessionId也可以不通过cookie传递，比如通过response返回客户端，再当作请求的参数传递给服务器去验证。</p>
<h4 data-id="heading-12">session-cookie</h4>
<p>当需要登录后才可以操作其他的。需要后端设置session, 前端请求时，将服务器返回的session id保存在cookie中。</p>
<h4 data-id="heading-13">token</h4>
<p>Token认证流程</p>
<ol start="0">
<li>客户端使用用户名跟密码请求登录</li>
<li>服务端收到请求，去验证用户名与密码</li>
<li>验证成功后，服务端会签发一个 <code>Token</code>，再把这个 <code>Token</code> 发送给客户端</li>
<li>客户端收到 <code>Token</code> 以后可以把它存储起来，比如放在 <code>Cookie</code> 里或者<code>Local Storage</code> 里</li>
<li>客户端每次向服务端请求资源的时候需要带着服务端签发的 <code>Token</code></li>
<li>服务端收到请求，然后去验证客户端请求里面带着的 <code>Token</code>（request头部添加Authorization），如果验证成功，就向客户端返回请求的数据 ，如果不成功返回401错误码，鉴权失败。</li>
</ol>
<pre><code class="copyable">//前端
​
axios.interceptors.request.use(config => &#123;
  config.headers.Authorization = window.sessionStorage.getItem("token")
  return config
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">jwt(基于token)</h4>
<p>基于 <code>token</code> 的解决方案有许多，常用的是<code>JWT</code>，<code>JWT</code> 的原理是，服务器认证以后，生成一个 <code>JSON</code> 对象，这个 <code>JSON</code> 对象肯定不能裸传给用户，那谁都可以篡改这个对象发送请求。因此这个 <code>JSON</code> 对象会被服务器端签名加密后返回给用户，返回的内容就是一张令牌，以后用户每次访问服务器端就带着这张令牌。</p>
<p>jwt的组成：Header（头部）、Payload（负载）、Signature（签名）。</p>
<ol start="0">
<li>Header部分是一个JSON对象，描述JWT的元数据。一般描述信息为该Token的加密算法以及Token的类型。&#123;"alg": "HS256","typ": "JWT"&#125;的意思就是，该token使用HS256加密，token类型是JWT。这个部分基本相当于明文，它将这个JSON对象做了一个Base64转码，变成一个字符串。Base64编码解码是有算法的，解码过程是可逆的。头部信息默认携带着两个字段。</li>
<li>Payload 部分也是一个 JSON 对象，用来存放实际需要传递的数据。有7个官方字段，还可以在这个部分定义私有字段。一般存放用户名、用户身份以及一些JWT的描述字段。它也只是做了一个Base64编码，因此肯定不能在其中存放秘密信息，比如说登录密码之类的。</li>
<li>Signature是对前面两个部分的签名，防止数据篡改，如果前面两段信息被人修改了发送给服务器端，此时服务器端是可利用签名来验证信息的正确性的。签名需要密钥，密钥是服务器端保存的，用户不知道。算出签名以后，把 Header、Payload、Signature 三个部分拼成一个字符串，每个部分之间用"点"（.）分隔，就可以返回给用户。</li>
</ol>
<pre><code class="copyable">//前端代码
//axios的请求拦截器，在每个request请求头上加JWT认证信息
axios.interceptors.request.use(
    config => &#123;
        const token = window.localStorage.getItem("token");
        if (token) &#123;
        // 判断是否存在token，如果存在的话，则每个http header都加上token
        // Bearer是JWT的认证头部信息
            config.headers.common["Authorization"] = "Bearer " + token;
        &#125;
        return config;
    &#125;,
    err => &#123;
        return Promise.reject(err);
    &#125;
);
//登录方法：在将后端返回的JWT存入localStorage
async login() &#123;
    const res = await axios.post("/login-token", &#123;
        username: this.username,
        password: this.password
    &#125;);
    localStorage.setItem("token", res.data.token);
&#125;,
//登出方法：删除JWT
async logout() &#123;
    localStorage.removeItem("token");
&#125;,
async getUser() &#123;
    await axios.get("/getUser-token");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//后端代码
const jwt = require("jsonwebtoken");
const jwtAuth = require("koa-jwt");
//用来签名的密钥
const secret = "it's a secret";
​
router.post("/login-token", async ctx => &#123;
  const &#123; body &#125; = ctx.request;
  //登录逻辑，略，即查找数据库，若该用户和密码合法，即将其信息生成一个JWT令牌传给用户
  const userinfo = body.username;
  ctx.body = &#123;
    message: "登录成功",
    user: userinfo,
    // 生成 token 返回给客户端
    token: jwt.sign(
      &#123;
        data: userinfo,
        // 设置 token 过期时间，一小时后，秒为单位
        exp: Math.floor(Date.now() / 1000) + 60 * 60
      &#125;,
      secret
    )
  &#125;;
&#125;);
​
//jwtAuth这个中间件会拿着密钥解析JWT是否合法。
//并且把JWT中的payload的信息解析后放到state中，ctx.state用于中间件的传值。
router.get(
  "/getUser-token",
  jwtAuth(&#123;
    secret
  &#125;),
  async ctx => &#123;
    // 验证通过，state.user
    console.log(ctx.state.user);
    ctx.body = &#123;
      message: "获取数据成功",
      userinfo: ctx.state.user.data 
    &#125;;
  &#125;
)
//这种密码学的方式使得token不需要存储，只要服务端能拿着密钥解析出用户信息，就说明该用户是合法的。
//若要更进一步的权限验证，需要判断解析出的用户身份是管理员还是普通用户。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>疑问：token后端生成后，放在哪里，是通过数据传递给前端，还是通过本地存储技术将其存储到本地，然后前端访问时，取出然后再通过authorization请求头传递给后端？</p>
<p>答: 是通过数据传递给前端，前端保存在本地，在以后需要权限才可以访问的时候，携带即可。</p>
<blockquote>
<p>学习自 <a href="https://juejin.im/post/6844903927100473357#heading-8" target="_blank" title="https://juejin.im/post/6844903927100473357#heading-8">掘金</a></p>
</blockquote>
<h2 data-id="heading-15">预编译*</h2>
<ul>
<li>
<h5 data-id="heading-16">找函数里面的变量声明和形参，此时赋值为undefined</h5>
</li>
<li>
<h5 data-id="heading-17">形参和实参相统一，就是给形参赋值</h5>
</li>
<li>
<h5 data-id="heading-18">找函数声明，如果有与函数同名的变量和函数，函数将覆盖变量</h5>
</li>
<li>
<h5 data-id="heading-19">然后再按照上下顺序执行代码，遇到相同的变量名和函数名，就相互覆盖</h5>
</li>
<li>
<h5 data-id="heading-20">然后再找赋值语句对相应变量赋值</h5>
</li>
</ul>
<p><strong>总之，变量的声明提升早与函数的声明提升</strong></p>
<pre><code class="copyable">var bar = [];        // 定义一个数组
for(var i = 0;i < 10;i++)&#123;
    bar[i] = function()&#123;   // 每个数组元素定义为一个函数
        console.log(i)   // 函数体
    &#125;
&#125;
bar[1](); // 10
bar[2](); // 10,都是输出10，深入理解需要掌握“预编译”和“作用域”的知识，
    // 思考方向 => 函数执行前,存在函数预编译AO(Activation Object)对象
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">如何验证<code>let,const</code>声明的变量也存在变量提升</h2>
<p><code>let,const</code>创建的过程被提升、初始化没有提升</p>
<p>其实他们声明的变量也是存在声明提升的，只是存在暂时性死区，不能在声明之前访问而已。如下面的例子，如果他不存在声明提升，那么这不会报错，会输出zh</p>
<pre><code class="copyable">let name = 'zh'
&#123;
  console.log(name) // Uncaught ReferenceError: name is not defined
  let name = 'hy'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">负载均衡</h2>
<p>当用户访问网站的时候，先访问一个中间服务器，再让这个中间服务器在服务器集群中选择一个压力较小的服务器，然后将该访问请求引入选择的服务器。这样保证服务器集群中的每个服务器压力趋于平衡。</p>
<h2 data-id="heading-23">执行上下文</h2>
<p>JavaScript 中有三种执行上下文类型。</p>
<ul>
<li><strong>全局执行上下文</strong> — 这是默认或者说基础的上下文，任何不在函数内部的代码都在全局上下文中。它会执行两件事：创建一个全局的 window 对象（浏览器的情况下），并且设置 <code>this</code> 的值等于这个全局对象。一个程序中只会有一个全局执行上下文。</li>
<li><strong>函数执行上下文</strong> — 每当一个函数被调用时, 都会为该函数创建一个新的上下文。每个函数都有它自己的执行上下文，不过是在<strong>函数被调用时创建的</strong>。函数上下文可以有任意多个。每当一个新的执行上下文被创建，它会按定义的顺序（将在后文讨论）执行一系列步骤。</li>
<li><strong>Eval 函数执行上下文</strong> — 执行在 <code>eval</code> 函数内部的代码也会有它属于自己的执行上下文，但由于 JavaScript 开发者并不经常使用 <code>eval</code>。</li>
</ul>
<h2 data-id="heading-24">执行栈</h2>
<p>就是当程序开始运行的时候，js引擎会创建一个栈结构，并且创建一个全局的执行上下文将其压入栈中，遇到函数调用时，会创建一个函数执行上下文，将其压入栈中，以此类推。函数执行完毕，将该函数的执行上下文从栈中弹出，将执行权交给栈顶元素。直到该程序执行完毕，将全局执行上下文从栈中弹出。</p>
<p>调用栈是一种数据结构。如果我们运行到一个函数，它就会将其放置到栈顶。当从这个函数返回的时候，就会将这个函数从栈顶弹出，这就是调用栈做的事情。</p>
<h2 data-id="heading-25">作用域</h2>
<p>作用域链是依靠执行上下文连接的，环境栈中的变量对象，从上到下就组成一条作用域链。他的用途就是保证对执行环境有权访问的所有变量和函数的有序访问。</p>
<p>词法作用域是指内部函数在定义的时候就决定了其外部作用域。</p>
<pre><code class="copyable">(function autorun()&#123;
    let x = 1;
    //这个函数中访问变量的时候，作用域是定义的时候决定的，而不是执行的时候。
    function log()&#123;
      console.log(x);
    &#125;;
    
    function run(fn)&#123;
      let x = 100;
      fn();
    &#125;
    
    run(log);//1
&#125;)();
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">词法环境</h2>
<p>包含<strong>环境记录器</strong>和<strong>外部环境的引用</strong></p>
<ol start="0">
<li><strong>环境记录器</strong>是存储变量和函数声明的实际位置。</li>
<li><strong>外部环境的引用</strong>意味着它可以访问其父级词法环境（作用域）。</li>
</ol>
<h2 data-id="heading-27">js的事件循环</h2>
<p><img src="https://juejin.cn/post/6990725554852855839" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>导图要表达的内容用文字来表述的话：</p>
<ul>
<li>同步和异步任务分别进入不同的执行"场所"，同步的进入主线程，异步的进入Event Table并注册函数。</li>
<li>当指定的事情完成时，Event Table会将这个函数移入Event Queue。</li>
<li>主线程内的任务执行完毕为空，会去Event Queue读取对应的函数，进入主线程执行。</li>
<li>上述过程会不断重复，也就是常说的Event Loop(事件循环)。</li>
</ul>
<p>MacroTask（宏任务）</p>
<ul>
<li><code>script</code>全部代码、<code>setTimeout</code>、<code>setInterval</code>、<code>setImmediate</code>（浏览器暂时不支持，只有IE10支持，具体可见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindow%2FsetImmediate" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Window/setImmediate" ref="nofollow noopener noreferrer"><code>MDN</code></a>）、<code>I/O</code>、<code>UI Rendering</code>。</li>
</ul>
<p>MicroTask（微任务）</p>
<ul>
<li><code>Process.nextTick（Node独有）</code>、<code>Promise</code>的then回调、<code>Object.observe(废弃)</code>、<code>MutationObserver</code>（具体使用方式查看<a href="https://link.juejin.cn/?target=http%3A%2F%2Fjavascript.ruanyifeng.com%2Fdom%2Fmutationobserver.html" target="_blank" rel="nofollow noopener noreferrer" title="http://javascript.ruanyifeng.com/dom/mutationobserver.html" ref="nofollow noopener noreferrer">这里</a>）</li>
</ul>
<p><code>setTimeout</code>这个函数，是经过指定时间后，把要执行的任务加入到Event Queue中。并不是到了指定的时间就执行，只有当主线程空闲出来后，才回去执行event queue中的等待事件。</p>
<p><code>setTimeout(fn,0)</code>的含义是，指定某个任务在主线程最早可得的空闲时间执行，意思就是不用再等多少秒了，只要主线程执行栈内的同步任务全部执行完成，栈为空就马上执行。</p>
<p>宏任务和微任务的执行顺序：</p>
<p>执行项目逻辑 ----> 将setTimeout，setInterval等定义的回调函数加入到宏任务队列，将promiese执行的回调加入到微任务队列 -------> 主逻辑执行完毕 -------> 执行微任务队列中的回调 --------> 执行宏任务队列中的回调</p>
<p>整段script代码是一个宏任务，在执行宏任务的过程中会不断的有微任务加入到微任务队列中，当执行完一个宏任务后先看微任务队列里有没有微任务，如果有先把整队的微任务执行完，然后在执行下一个宏任务，如此以往形成event loop。</p>
<p><strong><code>process.nextTick()</code>虽然它是异步API的一部分。<code>process.nextTick()</code>从技术上讲，它不是事件循环的一部分。</strong></p>
<ul>
<li><code>process.nextTick()</code>方法将 <code>callback</code> 添加到<code>next tick</code>队列。 一旦当前事件轮询队列的任务全部完成，在<code>next tick</code>队列中的所有<code>callbacks</code>会被依次调用。</li>
<li>process.nextTick应该是独立于Event Loop 之外的，它是微任务，但是它本身应该有一个自己的队列，这个队列中的回调函数会优先于微任务队列中的函数执行。比如，你把process.nextTick放在Promise.then的下方，他还是会优先执行。</li>
</ul>
<p><img src="https://juejin.cn/post/6990725554852855839" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">//注意promise改变状态之前，他是在主线程执行的，在then，和await中是在微任务中执行的。
​
console.log('1');
​
setTimeout(function () &#123;
  console.log('2');
  process.nextTick(function () &#123;
    console.log('3');
  &#125;)
  new Promise(function (resolve) &#123;
    console.log('4');
    resolve();
  &#125;).then(function () &#123;
    console.log('5')
  &#125;)
​
  // process.nextTick(function () &#123;
  //   console.log('3');
  // &#125;)
&#125;)
​
​
process.nextTick(function () &#123;
  console.log('6');
&#125;)
​
​
new Promise(function (resolve) &#123;
  console.log('7');
  resolve();
&#125;).then(function () &#123;
  console.log('8')
&#125;)
​
​
setTimeout(async function () &#123;
  console.log('9');
  // process.nextTick(function () &#123;
  //   console.log('10');
  // &#125;)
  // new Promise(function (resolve) &#123;
  //   console.log('11');
  //   resolve();
  // &#125;).then(function () &#123;
  //   console.log('12')
  // &#125;)
​
  let result = await Promise.resolve("11")
  console.log(result)
  console.log("12")
&#125;)
​
​
  ; (async () => &#123;
    console.log('13');
​
    let result = await Promise.resolve("14")
    console.log(result)
    console.log("15")
  &#125;)()
​
// 1 7 13 6 8 14 15 2 4 3 5 9 11 12。
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><a href="https://juejin.im/post/6844903512845860872" target="_blank" title="https://juejin.im/post/6844903512845860872">js执行机制</a></p>
<p><a href="https://juejin.im/entry/6844903444411580430" target="_blank" title="https://juejin.im/entry/6844903444411580430">深入 MutationObserver</a></p>
<p><a href="https://juejin.im/post/6844903764202094606#heading-37" target="_blank" title="https://juejin.im/post/6844903764202094606#heading-37">一次弄懂event loop</a></p>
</blockquote>
<h2 data-id="heading-28">mutationobserver</h2>
<p>Mutation Observer API 用来监视 DOM 变动。DOM 的任何变动，比如节点的增减、属性的变动、文本内容的变动，这个 API 都可以得到通知。</p>
<p>概念上，它很接近事件，可以理解为 DOM 发生变动就会触发 Mutation Observer 事件。但是，它与事件有一个本质不同：事件是同步触发，也就是说，DOM 的变动立刻会触发相应的事件；Mutation Observer 则是异步触发，DOM 的变动并不会马上触发，而是要等到当前所有 DOM 操作都结束才触发。</p>
<p>Mutation Observer 有以下特点。</p>
<ul>
<li>它等待所有脚本任务完成后，才会运行（即异步触发方式）。</li>
<li>它把 DOM 变动记录封装成一个数组进行处理，而不是一条条个别处理 DOM 变动。</li>
<li>它既可以观察 DOM 的所有类型变动，也可以指定只观察某一类变动。</li>
</ul>
<p>MutationObserver构造函数</p>
<p>通过new创建一个观察者对象，改构造函数需要传递一个回调函数。</p>
<pre><code class="copyable">var observer = new MutationObserver(callback);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该回调函数接收两个参数，参一：变动dom的数组，参二：观察者实例。</p>
<pre><code class="copyable">let callback = function (mutations, self) &#123;
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例方法：</p>
<p>1.observe(变动元素，观察选项)</p>
<pre><code class="copyable">let odiv = document.getElementById('#div');
​
let  options = &#123;
  'childList': true,
  'attributes':true
&#125; ;
​
observer.observe(odiv, options);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是 options对象的各属性及其描述：</p>













































<table><thead><tr><th>属性</th><th>类型</th><th>描述</th></tr></thead><tbody><tr><td>childList</td><td>Boolean</td><td>是否观察子节点的变动</td></tr><tr><td>attributes</td><td>Boolean</td><td>是否观察属性的变动</td></tr><tr><td>characterData</td><td>Boolean</td><td>是否节点内容或节点文本的变动</td></tr><tr><td>subtree</td><td>Boolean</td><td>是否观察所有后代节点的变动</td></tr><tr><td>attributeOldValue</td><td>Boolean</td><td>观察 attributes 变动时，是否记录变动前的属性值</td></tr><tr><td>characterDataOldValue</td><td>Boolean</td><td>观察 characterData 变动时，是否记录变动前的属性值</td></tr><tr><td>attributeFilter</td><td>Array</td><td>表示需要观察的特定属性（比如['class','src']），不在此数组中的属性变化时将被忽略</td></tr></tbody></table>
<p>注意：</p>
<ol start="0">
<li>
<p>对一个节点添加观察器，就像使用<code>addEventListener</code>方法一样，多次添加同一个观察器是无效的，回调函数依然只会触发一次。但是，如果指定不同的<code>options</code>对象，就会被当作两个不同的观察器。</p>
</li>
<li>
<p>监听选项中必须指定 childList、attributes 和 characterData 中的一种或多种。</p>
<pre><code class="copyable">Failed to execute 'observe' on 'MutationObserver': The options object must set at least one of 'attributes', 'characterData', or 'childList' to true.
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>2.disconnect()</p>
<p>该方法是停止监听dom变化的。</p>
<pre><code class="copyable">observer.disconnect();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.takeRecords()</p>
<p>用来清除变动记录，即不再处理未处理的变动。该方法返回变动记录的数组。</p>
<pre><code class="copyable">// 保存所有没有被观察器处理的变动
observer.takeRecords();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>MutationRecord 对象</p>
<p>即每次dom发生变化所产生的状态值。</p>























































<table><thead><tr><th>属性</th><th>类型</th><th>描述</th></tr></thead><tbody><tr><td>type</td><td>String</td><td>根据变动类型，值为 attributes， characterData 或 childList</td></tr><tr><td>target</td><td>Node</td><td>发生变动的DOM节点</td></tr><tr><td>addedNodes</td><td>NodeList</td><td>被添加的节点，或者为 null</td></tr><tr><td>removedNodes</td><td>NodeList</td><td>被删除的节点，或者为 null</td></tr><tr><td>previousSibling</td><td>Node</td><td>被添加或被删除的节点的前一个兄弟节点，或者为 null</td></tr><tr><td>nextSibling</td><td>Node</td><td>被添加或被删除的节点的后一个兄弟节点，或者为 null</td></tr><tr><td>attributeName</td><td>String</td><td>发生变更的属性的本地名称，或者为 null</td></tr><tr><td>attributeNamespace</td><td>String</td><td>发生变更的属性的命名空间，或者为 null</td></tr><tr><td>oldValue</td><td>String</td><td>如果 type 为 attributes，则返回该属性变化之前的属性值；如果 type 为 characterData，则返回该节点变化之前的文本数据；如果 type为 childList，则返回 null</td></tr></tbody></table>
<blockquote>
<p>参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjavascript.ruanyifeng.com%2Fdom%2Fmutationobserver.html" target="_blank" rel="nofollow noopener noreferrer" title="https://javascript.ruanyifeng.com/dom/mutationobserver.html" ref="nofollow noopener noreferrer">JavaScript 标准参考教程（alpha）)DOM模型Mutation Observer API</a></p>
</blockquote>
<h2 data-id="heading-29">优化js中的逻辑判断</h2>
<p>普通的写法：if-else if-else, switch-case</p>
<p>一元判断：Map, 对象</p>
<p>Map: [[条件， 逻辑参数]，[条件， 逻辑参数]，...]</p>
<p>对象: &#123;条件：逻辑参数&#125;</p>
<pre><code class="copyable">/**
 * 按钮点击事件
 * @param &#123;number&#125; status 活动状态：1 开团进行中 2 开团失败 3 商品售罄 4 开团成功 5 系统取消
 */
const onButtonClick = (status)=>&#123;
  if(status == 1)&#123;
    sendLog('processing')
    jumpTo('IndexPage')
  &#125;else if(status == 2)&#123;
    sendLog('fail')
    jumpTo('FailPage')
  &#125;else if(status == 3)&#123;
    sendLog('fail')
    jumpTo('FailPage')
  &#125;else if(status == 4)&#123;
    sendLog('success')
    jumpTo('SuccessPage')
  &#125;else if(status == 5)&#123;
    sendLog('cancel')
    jumpTo('CancelPage')
  &#125;else &#123;
    sendLog('other')
    jumpTo('Index')
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const actions = &#123;
  '1': ['processing','IndexPage'],
  '2': ['fail','FailPage'],
  '3': ['fail','FailPage'],
  '4': ['success','SuccessPage'],
  '5': ['cancel','CancelPage'],
  'default': ['other','Index'],
&#125;
/**
 * 按钮点击事件
 * @param &#123;number&#125; status 活动状态：1开团进行中 2开团失败 3 商品售罄 4 开团成功 5 系统取消
 */
const onButtonClick = (status)=>&#123;
  let action = actions[status] || actions['default'],
      logName = action[0],
      pageName = action[1]
  sendLog(logName)
  jumpTo(pageName)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const actions = new Map([
  [1, ['processing','IndexPage']],
  [2, ['fail','FailPage']],
  [3, ['fail','FailPage']],
  [4, ['success','SuccessPage']],
  [5, ['cancel','CancelPage']],
  ['default', ['other','Index']]
])
/**
 * 按钮点击事件
 * @param &#123;number&#125; status 活动状态：1 开团进行中 2 开团失败 3 商品售罄 4 开团成功 5 系统取消
 */
const onButtonClick = (status)=>&#123;
  let action = actions.get(status) || actions.get('default')
  sendLog(action[0])
  jumpTo(action[1])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多层判断：Map</p>
<p>Map: [[条件，() => &#123;&#125;], [条件，() => &#123;&#125;], ....]</p>
<ul>
<li>条件可以是多个条件合并的字符串</li>
<li>条件可以是一个对象</li>
<li>条件可以是正则，为了匹配更多相同逻辑不同条件的处理</li>
<li>.....</li>
</ul>
<p>对象：&#123;条件：() => &#123;&#125;, 条件：() => &#123;&#125;, ...&#125;</p>
<ul>
<li>条件可以是多个条件合并的字符串</li>
</ul>
<pre><code class="copyable">/**
 * 按钮点击事件
 * @param &#123;number&#125; status 活动状态：1开团进行中 2开团失败 3 开团成功 4 商品售罄 5 有库存未开团
 * @param &#123;string&#125; identity 身份标识：guest客态 master主态
 */
const onButtonClick = (status,identity)=>&#123;
  if(identity == 'guest')&#123;
    if(status == 1)&#123;
      //do sth
    &#125;else if(status == 2)&#123;
      //do sth
    &#125;else if(status == 3)&#123;
      //do sth
    &#125;else if(status == 4)&#123;
      //do sth
    &#125;else if(status == 5)&#123;
      //do sth
    &#125;else &#123;
      //do sth
    &#125;
  &#125;else if(identity == 'master') &#123;
    if(status == 1)&#123;
      //do sth
    &#125;else if(status == 2)&#123;
      //do sth
    &#125;else if(status == 3)&#123;
      //do sth
    &#125;else if(status == 4)&#123;
      //do sth
    &#125;else if(status == 5)&#123;
      //do sth
    &#125;else &#123;
      //do sth
    &#125;
  &#125;
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const actions = new Map([
  ['guest_1', ()=>&#123;/*do sth*/&#125;],
  ['guest_2', ()=>&#123;/*do sth*/&#125;],
  ['guest_3', ()=>&#123;/*do sth*/&#125;],
  ['guest_4', ()=>&#123;/*do sth*/&#125;],
  ['guest_5', ()=>&#123;/*do sth*/&#125;],
  ['master_1', ()=>&#123;/*do sth*/&#125;],
  ['master_2', ()=>&#123;/*do sth*/&#125;],
  ['master_3', ()=>&#123;/*do sth*/&#125;],
  ['master_4', ()=>&#123;/*do sth*/&#125;],
  ['master_5', ()=>&#123;/*do sth*/&#125;],
  ['default', ()=>&#123;/*do sth*/&#125;],
])
​
/**
 * 按钮点击事件
 * @param &#123;string&#125; identity 身份标识：guest客态 master主态
 * @param &#123;number&#125; status 活动状态：1 开团进行中 2 开团失败 3 开团成功 4 商品售罄 5 有库存未开团
 */
const onButtonClick = (identity,status)=>&#123;
  let action = actions.get(`$&#123;identity&#125;_$&#123;status&#125;`) || actions.get('default')
  action.call(this)
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const actions = &#123;
  'guest_1':()=>&#123;/*do sth*/&#125;,
  'guest_2':()=>&#123;/*do sth*/&#125;,
  //....
&#125;
​
const onButtonClick = (identity,status)=>&#123;
  let action = actions[`$&#123;identity&#125;_$&#123;status&#125;`] || actions['default']
  action.call(this)
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const actions = new Map([
  [&#123;identity:'guest',status:1&#125;,()=>&#123;/*do sth*/&#125;],
  [&#123;identity:'guest',status:2&#125;,()=>&#123;/*do sth*/&#125;],
  //...
])
​
const onButtonClick = (identity,status)=>&#123;
  // ...actions表示将[[],[],[]]内部的数组取出[],[],[]
  let action = [...actions].filter(([key,value])=>(key.identity == identity && key.status == status))
  action.forEach(([key,value])=>value.call(this))
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const actions = ()=>&#123;
  const functionA = ()=>&#123;/*do sth*/&#125;
  const functionB = ()=>&#123;/*do sth*/&#125;
  return new Map([
    [&#123;identity:'guest',status:1&#125;,functionA],
    [&#123;identity:'guest',status:2&#125;,functionA],
    [&#123;identity:'guest',status:3&#125;,functionA],
    [&#123;identity:'guest',status:4&#125;,functionA],
    [&#123;identity:'guest',status:5&#125;,functionB],
    //...
  ])
&#125;
​
const onButtonClick = (identity,status)=>&#123;
  let action = [...actions()].filter(([key,value])=>(key.identity == identity && key.status == status))
  action.forEach(([key,value])=>value.call(this))
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const actions = ()=>&#123;
  const functionA = ()=>&#123;/*do sth*/&#125;
  const functionB = ()=>&#123;/*do sth*/&#125;
  const functionC = ()=>&#123;/*send log*/&#125;
  return new Map([
    [/^guest_[1-4]$/,functionA],
    [/^guest_5$/,functionB],
    [/^guest_.*$/,functionC],
    //...
  ])
&#125;
​
const onButtonClick = (identity,status)=>&#123;
  let action = [...actions()].filter(([key,value])=>(key.test(`$&#123;identity&#125;_$&#123;status&#125;`)))
  action.forEach(([key,value])=>value.call(this))
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>学习自 <a href="https://juejin.im/post/6844903705058213896" target="_blank" title="https://juejin.im/post/6844903705058213896">掘金Think.大佬</a></p>
</blockquote>
<h2 data-id="heading-30">promise</h2>
<p>常用的静态方法：all，race，resolve, reject。</p>
<p>常用的实例方法：then, catch。</p>
<p>对于all方法来说，参数是一个若干个promise组成的数组，如果这些promise定义了自己的then,catch方法，并且有返回值，不管是成功还是失败，那么执行all方法的then就会执行，catch就不会执行。</p>
<pre><code class="copyable">const p1 = new Promise((resolve, reject) => &#123;
  resolve('hello');
&#125;)
.then(res => res)
.catch(e => e);
​
const p2 = new Promise((resolve, reject) => &#123;
  throw new Error('报错了');
&#125;)
.then(result => result)
.catch();//这里没有返回值，才会执行all的catch方法。
​
Promise.all([p1, p2])
.then(result => console.log(result))
.catch(e => console.log(e));
//执行结果
Error: 报错了
<span class="copy-code-btn">复制代码</span></code></pre>
<p>axios对其还做了一步简化。将接收到的请求参数封装成一个函数接收<code>spread()</code></p>
<pre><code class="copyable">function getUserAccount() &#123;
  return axios.get('/user/12345');
&#125;
​
function getUserPermissions() &#123;
  return axios.get('/user/12345/permissions');
&#125;
​
axios.all([getUserAccount(), getUserPermissions()])
  .then(axios.spread(function (acct, perms) &#123;
    // 两个请求现在都执行完成
  &#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>promise只执行一次，但是同一个promise的then,catch可以被执行多次。</p>
<pre><code class="copyable">const promise = new Promise((resolve, reject) => &#123;
  setTimeout(() => &#123;
    console.log('once')
    resolve('success')
  &#125;, 1000)
&#125;)
​
const start = Date.now()
promise.then((res) => &#123;
  console.log(res, Date.now() - start)
&#125;)
promise.then((res) => &#123;
  console.log(res, Date.now() - start)
&#125;)
//只会打印出一次once
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.then</code> 或者 <code>.catch</code> 的参数期望是函数，传入非函数则会发生值穿透。</p>
<pre><code class="copyable">Promise.resolve(1)
  .then(2)
  .then(Promise.resolve(3))
  .then(console.log)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.then</code>抛出的错误不会被第二个参数函数捕获，只能被后面的catch捕获。</p>
<pre><code class="copyable">Promise.resolve()
  .then(function success (res) &#123;
  //注意这里是抛出错误，而非返回错误。
    throw new Error('error')
  &#125;, function fail1 (e) &#123;
    console.error('fail1: ', e)
  &#125;)
  .catch(function fail2 (e) &#123;
    console.error('fail2: ', e)
  &#125;)
​
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">手写promise</h4>
<pre><code class="copyable">class Promise &#123;
  constructor(executor) &#123;//执行器函数
    let _this = this
    _this.status = 'pending'  //保存当前状态
    _this.value = undefined //执行成功时，传递的值
    _this.error = undefined//执行失败时，传递的值
    function resolve(value) &#123;
      if (_this.status === 'pending') &#123;
        _this.status = 'resolved'
        _this.value = value
      &#125;
    &#125;
​
    function reject(error) &#123;
      if (_this.status === 'pending') &#123;
        _this.status = 'rejected'
        _this.error = error
      &#125;
    &#125;
​
    executor(resolve, reject)//调用执行器函数
  &#125;
​
  then(onfulfilled, onRejected) &#123;
    let _this = this
    if (_this.status === 'resolved') &#123;
      onfulfilled(_this.value)
    &#125; else if (_this.status === 'rejected') &#123;
      onRejected(_this.error)
    &#125;
  &#125;
&#125;
​
//测试，此代码的问题是不能实现异步方法
let promise = new Promise((resolve, reject) => &#123;
  setTimeout(() => &#123;
    resolve('我是张昊')
    reject('我是李龙淼')
  &#125;, 1000)
&#125;).then(res => &#123;
  console.log(res)
&#125;, res => &#123;
  console.log(res)
&#125;)
//这里什么也不输出
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原因是我们在then函数中只对成功态和失败态进行了判断，而实例被new时，执行器中的代码会立即执行，但setTimeout中的代码将稍后执行，也就是说，then方法执行时，Promise的状态没有被改变依然是pending态，所以我们要对pending态也做判断，而由于代码可能是异步的，那么我们就要想办法把回调函数进行缓存，并且，<em><strong>then方法是可以多次使用的</strong></em>，所以要能存多个回调，那么这里我们用一个数组。</p>
<p>创建两个数组，为了存储成功的回调(resolve)和失败的回调(reject)</p>
<pre><code class="copyable">    _this.onResolvedCallbacks = []; // 存放then成功的回调,这里存的都是resolve()的函数
    _this.onRejectedCallbacks = []; // 存放then失败的回调，这里存的都是reject()的函数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在then中判断pending的判断,将then中的回调分别存入<code>onResolvedCallbacks</code>和<code>onRejectedCallbacks</code>数组中</p>
<pre><code class="copyable">if (_this.status === 'pending') &#123;
   // 每一次then时，如果是等待态，就把回调函数push进数组中，什么时候改变状态什么时候再执行
      //缓存成功时的回调函数，等到状态变为resolved的时候，在执行
      _this.onResolvedCallbacks.push(function () &#123;
        onfulfilled(_this.value)
      &#125;)
​
      //缓存失败时的回调函数，等到状态变为rejected的时候，在执行
      _this.onRejectedCallbacks.push(function () &#123;
        onRejectedCallbacks(_this.error)
      &#125;)
 &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在resolve方法中缓存异步执行的成功回调,在reject方法中缓存异步执行的失败的回调</p>
<pre><code class="copyable"> function resolve(value) &#123;
      if (_this.status === 'pending') &#123;
        _this.status = 'resolved'
        _this.value = value
        // 当成功的函数 (resolve()) 被调用时，之前缓存的回调函数会被一一调用
        _this.onResolvedCallbacks.map(callback => callback())
      &#125;
    &#125;
​
    function reject(error) &#123;
      if (_this.status === 'pending') &#123;
        _this.status = 'rejected'
        _this.error = error
        // 当失败的函数 (reject()) 被调用时，之前缓存的回调函数会被一一调用
        _this.onRejectedCallbacks.map(callback => callback())
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了防止promise在执行出现错误，我们需要做错误处理</p>
<pre><code class="copyable">    try &#123;
      executor(resolve, reject)
    &#125; catch (e) &#123;
      console.log(e)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>promise的链式调用。由于promise的状态会发生改变，所以then返回的promise是一个全新的。</p>
<p>有点复杂！！！
promise的其他原型方法</p>
<pre><code class="copyable">    // 捕获错误的方法，在原型上有catch方法，返回一个没有resolve的then结果即可
    Promise.prototype.catch = function (callback) &#123;
        return this.then(null, callback)
    &#125;
    // 解析全部方法，接收一个Promise数组promises,返回新的Promise，遍历数组，都完成再resolve
    Promise.all = function (promises) &#123;
        //promises是一个promise的数组
        return new Promise(function (resolve, reject) &#123;
            let arr = []; //arr是最终返回值的结果
            let i = 0; // 表示成功了多少次
            function processData(index, y) &#123;
                arr[index] = y;
                if (++i === promises.length) &#123;
                    resolve(arr);
                &#125;
            &#125;
            for (let i = 0; i < promises.length; i++) &#123;
                promises[i].then(function (y) &#123;
                    processData(i, y)
                &#125;, reject)
            &#125;
        &#125;)
    &#125;
    // 只要有一个promise成功了 就算成功。如果第一个失败了就失败了
    Promise.race = function (promises) &#123;
        return new Promise(function (resolve, reject) &#123;
            for (var i = 0; i < promises.length; i++) &#123;
                promises[i].then(resolve,reject)
            &#125;
        &#125;)
    &#125;
    // 生成一个成功的promise
    Promise.resolve = function(value)&#123;
        return new Promise(function(resolve,reject)&#123;
            resolve(value);
        &#125;)
    &#125;
    // 生成一个失败的promise
    Promise.reject = function(error)&#123;
        return new Promise(function(resolve,reject)&#123;
            reject(error);
        &#125;)
    &#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>学习自</p>
<p><a href="https://juejin.im/post/6844903509934997511#heading-0" target="_blank" title="https://juejin.im/post/6844903509934997511#heading-0">promise必知必会</a></p>
<p><a href="https://juejin.im/post/6844903583234834445#heading-6" target="_blank" title="https://juejin.im/post/6844903583234834445#heading-6">rocYoung对promise的分析</a></p>
</blockquote>
<h2 data-id="heading-32">前端的路由跳转</h2>
<p>Hash 方法是在路由中带有一个 <code>#</code>，主要原理是通过监听 <code>#</code> 后的 URL 路径标识符的更改而触发的浏览器 <code>hashchange</code> 事件，然后通过获取 <code>location.hash</code> 得到当前的路径标识符，再进行一些路由跳转的操作。</p>
<pre><code class="copyable">class RouterClass &#123;
  constructor() &#123;
    this.isBack = false
    this.routes = &#123;&#125;        // 记录路径标识符对应的cb
    this.currentUrl = ''    // 记录hash只为方便执行cb
    this.historyStack = []  // hash栈
    window.addEventListener('load', () => this.render())
    window.addEventListener('hashchange', () => this.render())
  &#125;
  
  /* 初始化 */
  static init() &#123;
    window.Router = new RouterClass()
  &#125;
  
  /* 记录path对应cb */
  route(path, cb) &#123;
    this.routes[path] = cb || function() &#123;&#125;
  &#125;
  
  /* 入栈当前hash，执行cb */
  render() &#123;
    if (this.isBack) &#123;      // 如果是由backoff进入，则置false之后return
      this.isBack = false   // 其他操作在backoff方法中已经做了
      return
    &#125;
    this.currentUrl = location.hash.slice(1) || '/'
    //将每一个路径都加入到栈中，为了back的判断
    this.historyStack.push(this.currentUrl)
    this.routes[this.currentUrl]()
  &#125;
  
  /* 路由后退 */
  back() &#123;
    this.isBack = true
    this.historyStack.pop()                   // 移除当前hash，回退到上一个
    const &#123; length &#125; = this.historyStack
    if (!length) return //如果栈中没有路径了，将直接结束
    let prev = this.historyStack[length - 1]  // 拿到要回退到的目标hash
    location.hash = `#$&#123; prev &#125;`   //为了使手动跳转正常进行，需要将当前路径加上一个#，来满足slice的分割
    this.currentUrl = prev
    this.routes[prev]()                       // 执行对应cb
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>history</p>
<ol start="0">
<li><code>history.go(n)</code>：路由跳转，比如n为 <code>2</code> 是往前移动2个页面，n为 <code>-2</code> 是向后移动2个页面，n为0是刷新页面</li>
<li><code>history.back()</code>：路由后退，相当于 <code>history.go(-1)</code></li>
<li><code>history.forward()</code>：路由前进，相当于 <code>history.go(1)</code></li>
<li><code>history.pushState()</code>：添加一条路由历史记录，如果设置跨域网址则报错，浏览器有记录。</li>
<li><code>history.replaceState()</code>：替换当前页在路由历史记录的信息，浏览器无记录。</li>
<li><code>popstate</code> 事件：当活动的历史记录发生变化，就会触发 <code>popstate</code> 事件，在点击浏览器的前进后退按钮或者调用上面前三个方法的时候也会触发，参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindow%2Fonpopstate" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Window/onpopstate" ref="nofollow noopener noreferrer">MDN</a></li>
</ol>
<h2 data-id="heading-33">何为闭包？</h2>
<p>闭包在实现上是一个结构体，它存储了一个函数（通常是其入口地址）和一个关联的环境（相当于一个符号查找表）。环境里是若干对符号和值的对应关系，它既要包括<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E7%25BA%25A6%25E6%259D%259F%25E5%258F%2598%25E9%2587%258F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E7%BA%A6%E6%9D%9F%E5%8F%98%E9%87%8F" ref="nofollow noopener noreferrer">约束变量</a>（<strong>该函数内部绑定的符号</strong>），也要包括<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E8%2587%25AA%25E7%2594%25B1%25E5%258F%2598%25E9%2587%258F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E5%8F%98%E9%87%8F" ref="nofollow noopener noreferrer">自由变量</a>（<strong>在函数外部定义但在函数内被引用</strong>），有些函数也可能没有自由变量。闭包跟函数最大的不同在于，当捕捉闭包的时候，它的自由变量会在捕捉时被确定，这样即便脱离了捕捉时的上下文，它也能照常运行。捕捉时对于值的处理可以是值拷贝，也可以是名称引用。</p>
<p>而闭包则意味着同时包括<strong>函数指针</strong>和<strong>环境</strong>两个关键元素。在编译优化当中，没有捕捉自由变量的闭包可以被优化成普通函数。</p>
<p><strong>闭包中引入的变量何时被销毁？</strong></p>
<p>闭包中访问的外部变量是存放在堆内存中的。</p>
<p>变量的生命周期取决于闭包的生命周期。被闭包引用的外部作用域中的变量将一直存活直到闭包函数被销毁。如果一个变量被多个闭包所引用，那么直到所有的闭包被垃圾回收后，该变量才会被销毁。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">维基百科</a></p>
</blockquote>
<h2 data-id="heading-34">数组方法(存在高阶函数)的返回值</h2>
<p>map：该方法的返回值就是回调函数的返回值组成的数组。</p>
<p>filter: 该方法的返回值就是回调函数符合条件的返回值组成的数组。</p>
<pre><code class="copyable">let arr = [1, 2, 3, 4]
​
let resArr = arr.filter(item => &#123;
  if (item > 2) &#123;
    return item
  &#125;
&#125;)
//等价于
arr.filter(item => item > 2)
console.log(resArr)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>forEach：该方法没有返回值。</p>
<p>reduce：该方法返回的值是累计器（回调函数的第一个参数）累计后的值。</p>
<pre><code class="copyable">let arr = [
  &#123; id: 1, name: 'zh', age: 20 &#125;,
  &#123; id: 2, name: 'hy', age: 19 &#125;,
  &#123; id: 3, name: 'llm', age: 19 &#125;
]
​
let reArr = arr.reduce((pre, next) => &#123;
  if (next.age === 19) &#123;
    return pre.concat(Object.assign(&#123;&#125;, next, &#123; sex: 'female' &#125;))
  &#125;
  return []//这里必须有返回值，不然会报错，因为每遍历一项都需要有返回值。如果上面用到了pre，下面没有返回就会报错，pre的值是每次回调函数返回的值。
&#125;, [])
​
console.log(reArr)
// &#123;id: 2, name: "hy", age: 19, sex: "female"&#125;
// &#123;id: 3, name: "llm", age: 19, sex: "female"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>every: 该方法的返回值是布尔值，只有数组中的元素都满足条件，才回返回true，否则返回false。</p>
<pre><code class="copyable">let arr = [1, 2, 3, 4]
​
let resArr = arr.every(item => item >= 1)
​
console.log(resArr)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>some：该方法返回的是布尔值，表示只要数组中有一个元素满足条件就返回true,否则返回false。</p>
<p>find：该方法返回的是第一个满足条件的值。</p>
<p>findIndex：该方法返回的是第一个满足条件的值的下标。</p>
<h2 data-id="heading-35">URLsearchParams</h2>
<p>URLsearchParams(url)用来解析url参数的。</p>
<pre><code class="copyable">//URLSearchParams用来解析参数的
let url = '?name=zh&age=20';
let searchParams = new URLSearchParams(url)
// console.log(searchParams)//map对象
let arr = [...searchParams]
​
console.log(arr) //[ [ 'name', 'zh' ], [ 'age', '20' ] ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取单个参数。</p>
<pre><code class="copyable">searchParams.get('name')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>校验参数是否存在。</p>
<pre><code class="copyable">searchParams.has('sex') // false
searchParams.has('age') // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加参数。</p>
<pre><code class="copyable">searchParams.append('sex', 'male')
console.log(searchParams)//URLSearchParams &#123; 'name' => 'zh', 'age' => '20', 'sex' => 'male' &#125;
console.log(url)//?name=zh&age=20,注意url并不会添加上该参数，但是解析后是有该参数的
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除参数。</p>
<pre><code class="copyable">searchParams.delete('sex');
searchParams.has('sex'); // false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改参数。</p>
<pre><code class="copyable">searchParams.set('age', 22)
console.log(searchParams)//URLSearchParams &#123; 'name' => 'zh', 'age' => '22', 'sex' => 'male' &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将解析后的参数，再转为查询字符串。</p>
<pre><code class="copyable">searchParams.toString() //name=zh&age=22&sex=male
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-36">重写数组方法</h2>
<h4 data-id="heading-37">重写map方法，利用for循环</h4>
<pre><code class="copyable">const selfMap = function (fn, context = this) &#123;
  //这里的context会被当做fn函数中的this,如果不传入context,那么this就是调用的数组。
  let arr = Array.prototype.slice.call(context)
  let mappedArr = Array()
  for (let i = 0; i < arr.length; i++) &#123;
    //判断稀疏数组的情况
    if (!arr.hasOwnProperty(i)) continue;
    mappedArr[i] = fn.call(context, arr[i], i, this)
    // console.log(context)
  &#125;
  return mappedArr
&#125;
​
Array.prototype.selfMap = selfMap
​
let resArr = [0, 0, 0, 1].selfMap(number => number * 2, [2, 3, 4])
​
console.log(resArr)//[4,6,8]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我对map方法的错误理解，context只是改变了this指向，然而并不是改变函数执行的数组。</p>
<p>作者大大，第二个方法，即map方法，我感觉应该把context初始为this,然后slice方法中传入context，这样传入第二个参数的时候，this的值才回改变。不然没有效果 let resArr = [0, 0, 0, 1].selfMap(number => number * 2, [2, 3, 4]) console.log(resArr)//这里仍然是[0,0,0,2]，而不是[4,6,8] //下面这样就是对的 const selfMap = function (fn, context = this) &#123; //这里的context会被当做fn函数中的this let arr = Array.prototype.slice.call(context) let mappedArr = Array() for (let i = 0; i number * 2, [2, 3, 4]) console.log(resArr)//[4,6,8] 如果不对，望告知。</p>
<p>这里是js原生的map测试</p>
<pre><code class="copyable">let resArr = [4, 5, 6].map(function (item, index, arr1) &#123;
​
  console.log(arr1)//[4,5,6]
  console.log('this', this)//[1,2,3]
  return item * 2//作用的是[4,5,6]
&#125;, [1, 2, 3])
​
console.log(resArr)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-38">重写map方法。利用reduce方法。</h4>
<pre><code class="copyable">const selfMap = function (fn, context) &#123;
  let arr = Array.prototype.slice.call(this)
  return arr.reduce((pre, cur, index) => &#123;
    //这个返回值就是pre,然后将完全处理后的元素，都返回给pre,然后展开pre即可。
    //也就是这里我有一个疑问，他每次都返回pre,每次都展开pre,每次展开都会重复上一次返回的pre中的元素呀，所以应该会重复很多呀。
    return [...pre, fn.call(context, cur, index, this)]
  &#125;, [])
&#125;
Array.prototype.selfMap = selfMap
let resArr = [1, 2, 3].selfMap(item => item * 2)
console.log(resArr)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决疑惑：因为数组的内存地址都是一样的，pre的内存地址一样的，只是展开了最后一次赋值的值。</p>
<pre><code class="copyable">let a = new Array(10)
let resArr = []
for (let i = 0; i <= a.length; i++) &#123;
  let arr = [i]
  resArr = [...arr, 2, 3, 4]
&#125;
​
console.log(resArr)//[ 10, 2, 3, 4 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">重写filter方法，利用for循环。</h4>
<pre><code class="copyable">const selfFilter = function (fn, context) &#123;
  //要处理的数组
  let arr = Array.prototype.slice.call(this)
  let resArr = Array()
  for (let i = 0; i < arr.length; i++) &#123;
    //判断返回的条件是否正确，并且加入到数组中。
    fn.call(context, arr[i], i, this) && resArr.push(arr[i])
  &#125;
  return resArr
&#125;
​
Array.prototype.selfFilter = selfFilter
​
let arr = [1, 2, 3]
​
let arr1 = arr.selfFilter(item => item > 2)
​
console.log(arr1)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-40">重写filter,利用reduce。</h4>
<pre><code class="copyable">const selfFilter = function (fn, context) &#123;
  let arr = Array.prototype.slice.call(this)
  let resArr = []
  return arr.reduce((pre, cur, index) => &#123;
    // if (fn.call(context, cur, index, this)) &#123;
    //   resArr.push(cur)
    //   return resArr
    // &#125;
    return fn.call(context, cur, index, this) ? [...pre, cur] : [...pre]
  &#125;, [])
&#125;
​
Array.prototype.selfFilter = selfFilter
​
let arr = [0, 2, 3]
​
let arr1 = arr.selfFilter(item => item > 2)
​
console.log(arr1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重写some，利用for循环。</p>
<pre><code class="copyable">const someFilter = function (fn, context) &#123;
  let arr = Array.prototype.slice.call(this)
  for (let i = 0; i < arr.length; i++) &#123;
    if (fn.call(context, arr[i], i, this))
      return true
  &#125;
  return false
&#125;
​
Array.prototype.someFilter = someFilter
​
let arr = [1, 2, 3]
​
let arr1 = arr.someFilter(item => item > 2)
console.log(arr1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重写flat方法，利用reduce。</p>
<pre><code class="copyable">const selfFlat = function (depth = 1) &#123;
  let arr = Array.prototype.slice.call(this)
  // let resArr = []
  if (depth === 0) return arr
  return reduce((pre, cur) => &#123;
    if (Array.isArray(cur)) &#123;
      //反正就是递归
      return [...pre, ...selfFlat.call(cur, depth - 1)]
    &#125; else &#123;
      return [...pre, cur]
    &#125;
  &#125;, [])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-41">es6的面向对象class语法</h2>
<h4 data-id="heading-42">ES6 的 class 内部是基于寄生组合式继承</h4>
<pre><code class="copyable">function inherit(subType, superType) &#123;
  subType.prototype = Object.create(superType.prototype, &#123;
    constructor: &#123;
      value: subType,
      enumerable: false,
      configurable: true,
      writable: true
    &#125;
  &#125;)
  // 让类的静态方法也可以被继承。
  Object.setPrototypeOf(subType, superType)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-43">函数的柯里化</h2>
<p>j就是通过以下调用的函数，可以实现分步调用。</p>
<p>他就是一个三阶函数。会后直接调用函数。</p>
<p>柯里化可是将一个多参数的函数转换成多个单参数的函数，但是现在我们不仅可以传入一个参数，还可以一次传入两个参数。</p>
<pre><code class="copyable">var curry = function (fn) &#123;
  //这一步是将传入的参数除了fn以外的参数抽选出来。
  var args = [].slice.call(arguments, 1);
  return function () &#123;
    //将传入的所有的参数连接在一起。
    var newArgs = args.concat([].slice.call(arguments));
    //其实我们分开调用函数，最后也是直接调用了最后一个函数。
    return fn.apply(this, newArgs);
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里修改了一些bug。既可以一次调用，也可以多次调用。</p>
<pre><code class="copyable">function curry(fn, args) &#123;
  //访问fn函数中参数的个数。
  let length = fn.length;
  args = args || []
  return function () &#123;
    let _args = args.slice(0), arg, i;
    for (i = 0; i < arguments.length; i++) &#123;
      //将第二个函数中的参数加入到第一个参数中去。
      arg = arguments[i];
      _args.push(arg)
    &#125;
    //比较总的参数和fn参数。直到函数参数满足被柯里化函数参数相同时调用。
    if (_args.length < length) &#123;
      return curry.call(this, fn, _args);
    &#125; else &#123;
      return fn.apply(this, _args)
    &#125;
  &#125;
&#125;
​
​
let fn = curry(function (a, b, c) &#123;
  console.log([a, b, c])
&#125;)
​
fn("a", "b", "c")
fn("a")("c", "b", "d")
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>参考自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmqyqingfeng%2FBlog%2Fissues%2F42%23" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mqyqingfeng/Blog/issues/42#" ref="nofollow noopener noreferrer">JavaScript专题之函数柯里化</a></p>
</blockquote>
<h2 data-id="heading-44">函数的length和arguments</h2>
<p><strong>注意：length表示的是形参的个数，而arguments表示的是实参的个数。</strong></p>
<h2 data-id="heading-45">Virtual Dom 的优势在哪里？</h2>
<p>「Virtual Dom 的优势」其实这道题目面试官更想听到的答案不是上来就说「直接操作/频繁操作 DOM 的性能差」，如果 DOM 操作的性能如此不堪，那么 jQuery 也不至于活到今天。所以面试官更想听到 VDOM 想解决的问题以及为什么频繁的 DOM 操作会性能差。</p>
<p>首先我们需要知道：</p>
<p>DOM 引擎、JS 引擎 相互独立，但又工作在同一线程（主线程） JS 代码调用 DOM API 必须 挂起 JS 引擎、转换传入参数数据、激活 DOM 引擎，DOM 重绘后再转换可能有的返回值，最后激活 JS 引擎并继续执行若有频繁的 DOM API 调用，且浏览器厂商不做“批量处理”优化， 引擎间切换的单位代价将迅速积累若其中有强制重绘的 DOM API 调用，重新计算布局、重新绘制图像会引起更大的性能消耗。</p>
<p>其次是 VDOM 和真实 DOM 的区别和优化：</p>
<ol start="0">
<li>虚拟 DOM 不会立马进行排版与重绘操作</li>
<li>虚拟 DOM 进行频繁修改，然后一次性比较并修改真实 DOM 中需要改的部分，最后在真实 DOM 中进行排版与重绘，减少过多DOM节点排版与重绘损耗</li>
<li>虚拟 DOM 有效降低大面积真实 DOM 的重绘与排版，因为最终与真实 DOM 比较差异，可以只渲染局部</li>
</ol>
<h2 data-id="heading-46">如何选择图片</h2>









































<table><thead><tr><th>名称</th><th>介绍</th><th>不适合</th><th>适合</th></tr></thead><tbody><tr><td>JPEG</td><td>在互联网上常被应用于存储和传输照片</td><td>线条图形，文字，图标图形，它不支持透明度</td><td>颜色丰富的照片，彩色图大焦点图，通栏bannr图，结构不规则的图形。</td></tr><tr><td>PNG</td><td>栅格图形，最初是为了代替gif设计的，文件比较大，支持半透明和透明的特性。</td><td>由于无损存储，彩色图像体积太大，所以不太适合</td><td>纯色，透明，线条绘图，图标。边缘清晰，有大块相同颜色区域。颜色数较少但是需要半透明。</td></tr><tr><td>Webp</td><td>可以插入多帧，实现动画效果，可以设置透明度，比gif有更好的动画。</td><td>最多处理256色，不适合于彩色图片</td><td>适用于图形和半透明图像</td></tr><tr><td>Gif</td><td>栅格图形，支持256色，仅支持完全透明和完全不透明，如果需要比较通用的动画，gif是唯一的选择。</td><td>每个像素只有8比特，不适合存储彩色图片。</td><td>动画和图标</td></tr><tr><td></td><td></td><td></td><td></td></tr></tbody></table>
<h2 data-id="heading-47">JSON.stringify()</h2>
<p>以下情况会出现失真。</p>
<p>如果对象含有 toJSON 方法会调用 toJSON。</p>
<pre><code class="copyable">const arr = [function () &#123; &#125;, undefined, NaN, 2]
arr.toJSON = () => &#123;
  return '你失真了'
&#125;
​
const tojson = JSON.stringify(arr)
​
console.log(tojson)//你失真了
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在数组中</strong>： 存在 Undefined/Symbol/Function 数据类型时会变为 null。 存在 Infinity/NaN 也会变成 null。</p>
<pre><code class="copyable">const arr = [function () &#123; &#125;, undefined, NaN, Infinity, Symbol(), 2]
​
const tojson = JSON.stringify(arr)
​
console.log(tojson)//[null,null,null,null,null,2]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在对象中</strong>: 属性值为 Undefined/Symbol/Function 数据类型时，属性和值都不会转为字符串。属性值为Infinity/NaN ，属性值会变为 null。</p>
<pre><code class="copyable">const obj = &#123;
  name: undefined,
  age: Symbol(),
  sex: function () &#123; &#125;,
  address: NaN,
  friend: Infinity,
  hobbit: 'llm'
&#125;
​
console.log(JSON.stringify(obj))//&#123;"address":null,"friend":null,"hobbit":"llm"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>日期数据类型的值会调用 toISOString。</p>
<pre><code class="copyable">//日期类型
const time = new Date()
​
const tojson1 = JSON.stringify(time)
const tojson = time.toISOString()
​
console.log(tojson1)//"2020-08-26T03:29:20.440Z"
console.log(tojson)//2020-08-26T03:29:20.440Z
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非数组/对象/函数/日期的复杂数据类型会变成一个空对象。</p>
<pre><code class="copyable">const reg = new RegExp("at", 'i')
​
const res = JSON.stringify(reg)
​
console.log(res)//&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JSON.stringify 有第二个参数 replacer，它可以是数组或者函数，用来指定对象序列化过程中哪些属性应该被处理，哪些应该被排除。</p>
<pre><code class="copyable">function replacer(key, value) &#123;
  if (typeof value === "string") &#123;
    return undefined;
  &#125;
  return value;
&#125;
​
var foo = &#123;foundation: "Mozilla", model: "box", week: 45, transport: "car", month: 7&#125;;
var jsonString = JSON.stringify(foo, replacer);
​
console.log(jsonString)// &#123;"week":45,"month":7&#125;
​
var foo = &#123;foundation: "Mozilla", model: "box", week: 45, transport: "car", month: 7&#125;;
console.log(JSON.stringify(foo, ['week', 'month']));// &#123;"week":45,"month":7&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>循环引用会抛出错误。</p>
<p>何为循环引用？</p>
<p>对象的属性值等于父级的引用。</p>
<pre><code class="copyable">const obj1 = &#123;
  a: null,
  name: 'zh'
&#125;
obj1.a = obj1
​
const res = JSON.stringify(obj1)
console.log(res)//TypeError: Converting circular structure to JSON
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">实现call方法</h2>
<p>核心思路就是把函数作为要绑定对象的一个方法,然后执行函数，最后从绑定对象上删除此方法。</p>
<pre><code class="copyable">const selfCall = function (context, ...args) &#123;
  //这一步等于this，但是this是一个对象呀。
  //又误会了这个this了，其实他表示的只是Function类的一个实例，即就是调用的函数而已。
  let func = this
  context || (context = window)
  if (typeof func !== 'function') throw new TypeError('this is not a function')
  let caller = Symbol('caller')
  context[caller] = func
  let res = context[caller](...args)
  delete context[caller]
  return res
&#125;
​
Function.prototype.selfCall = selfCall
let name = 'llm'
let obj = &#123;
  name: 'zh'
&#125;
​
function sayName() &#123;
  console.log(this.name)
&#125;
​
sayName.selfCall(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-49">实现apply方法</h2>
<p>主要是这里要判断有误参数，然后键传入的数组参数，展开在传入到函数中调用。</p>
<pre><code class="copyable">function selfApply(context, arr) &#123;
  let func = this;
  context = context || window;
  if (typeof func !== 'function') throw new TypeError('this is not a function')
  //唯一的键值
  let caller = Symbol('caller')
  context[caller] = func
  //函数返回值
  let res;
  if (!arr) &#123;
    res = context[caller]()
  &#125; else &#123;
    res = context[caller](...arr)
  &#125;
  //删除该函数
  delete context[caller]
  return res
&#125;
​
Function.prototype.selfApply = selfApply;
​
let name = 'llm'
let obj = &#123;
  name: 'zh'
&#125;
​
function sayName(a, b) &#123;
  console.log(this.name, a, b)
&#125;
​
sayName.selfApply(obj, [1, 2])
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-50">类型转换</h2>
<ol start="0">
<li>
<h4 data-id="heading-51">让原始值转化为布尔值。只要六种情况是转化为false。</h4>
<pre><code class="copyable">false , undefined , NaN , null , "" , 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，Boolean()不传入任何参数时，会返回false。</p>
</li>
<li>
<h4 data-id="heading-52">原始值转化为数字。</h4>
<p>如果 Number 函数不传参数，返回 +0，如果有参数，调用 <code>ToNumber(value)</code>。</p>
<p>注意这个 <code>ToNumber</code> 表示的是一个底层规范实现上的方法，并没有直接暴露出来。</p>
</li>
</ol>





























<table><thead><tr><th>参数类型</th><th>结果</th></tr></thead><tbody><tr><td>Undefined</td><td>NaN</td></tr><tr><td>Null</td><td>+0</td></tr><tr><td>Boolean</td><td>如果参数是 true，返回 1。参数为 false，返回 +0</td></tr><tr><td>Number</td><td>返回与之相等的值</td></tr><tr><td>String</td><td>这段比较复杂，看例子</td></tr></tbody></table>
<p>其实对于Number转化来说，就是将其传入的参数尽可能的转化为正数或者浮点数。忽略所有的前导0。如果参数中有非数字的字符，那么将会被转化为NaN。<strong>但是只有传入的都是空格除外。并且会忽略前导和后导的空格。</strong></p>
<pre><code class="copyable">Number("   ")//0
Number("123  123")//NaN
Number("123   ")//123
Number("   123")//123
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>
<h4 data-id="heading-53">原始值转化为字符串。</h4>
<p>直接调用String()方法，不传入参数，则返回一个空字符串。如果有参数，调用 <code>ToString(value)</code>。这个方法也是底层实现的，没有暴露出来。</p>





























<table><thead><tr><th>参数类型</th><th>结果</th></tr></thead><tbody><tr><td>Undefined</td><td>"undefined"</td></tr><tr><td>Null</td><td>"null"</td></tr><tr><td>Boolean</td><td>如果参数是 true，返回 "true"。参数为 false，返回 "false"</td></tr><tr><td>Number</td><td>又是比较复杂，可以看例子</td></tr><tr><td>String</td><td>返回与之相等的值</td></tr></tbody></table>
</li>
<li>
<h4 data-id="heading-54">对象转化为字符串和数字。</h4>
<p>toString()方法作用在于返回一个反映这个对象的字符串。</p>
<pre><code class="copyable">let arr = [1, 2]
let arr1 = []
console.log(arr.toString())//"1,2"
console.log(arr1.toString())//""
​
// console.log(null.toString())//报错
// console.log((undefined).toString())//报错
console.log((NaN).toString())//"NaN"
​
let str = ""
let str1 = " "
let str2 = "zh"
console.log(str.toString())//""
console.log(str1.toString())//""
console.log(str2.toString())//"zh"
​
console.log(true.toString())//true
console.log(false.toString())//false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而另一个转换对象的函数是 valueOf，表示对象的原始值。默认的 valueOf 方法返回这个对象本身，数组、函数、正则简单的继承了这个默认方法，也会返回对象本身。日期是一个例外，它会返回它的一个内容表示: 1970 年 1 月 1 日以来的毫秒数。</p>
<pre><code class="copyable">let date = new Date(2020, 8, 27);
console.log(date.valueOf()) // 1601136000000
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-55">ToPrimitive</h4>
<p><code>ToPrimitive(input[, PreferredType])</code> 第一个参数是 input，表示要处理的输入值。 第二个参数是 PreferredType，非必填，表示希望转换成的类型，有两个值可以选，Number 或者 String。</p>
<p>当不传入 PreferredType 时，如果 input 是日期类型，相当于传入 String，否则，都相当于传入 Number。 如果传入的 input 是 Undefined、Null、Boolean、Number、String 类型，直接返回该值。</p>
</li>
</ol>
<p><strong>如果是 ToPrimitive(obj, Number)</strong> ，处理步骤如下：</p>
<p>如果 obj 为 基本类型，直接返回 否则，调用 valueOf 方法，如果返回一个原始值，则 JavaScript 将其返回。 否则，调用 toString 方法，如果返回一个原始值，则 JavaScript 将其返回。 否则，JavaScript 抛出一个类型错误异常。</p>
<p><strong>如果是 ToPrimitive(obj, String)</strong> ，处理步骤如下：</p>
<p>如果 obj为 基本类型，直接返回 否则，调用 toString 方法，如果返回一个原始值，则 JavaScript 将其返回。 否则，调用 valueOf 方法，如果返回一个原始值，则 JavaScript 将其返回。 否则，JavaScript 抛出一个类型错误异常。</p>
<pre><code class="copyable">const toPrimitive = (obj, preferredType='Number') => &#123;
    let Utils = &#123;
        typeOf: function(obj) &#123;
            return Object.prototype.toString.call(obj).slice(8, -1);
        &#125;,
        isPrimitive: function(obj) &#123;
            let types = ['Null', 'String', 'Boolean', 'Undefined', 'Number'];
            return types.indexOf(this.typeOf(obj)) !== -1;
        &#125;
    &#125;;
   
    if (Utils.isPrimitive(obj)) &#123;
        return obj;
    &#125;
    
    preferredType = (preferredType === 'String' || Utils.typeOf(obj) === 'Date') ?
     'String' : 'Number';
​
    if (preferredType === 'Number') &#123;
        if (Utils.isPrimitive(obj.valueOf())) &#123;
            return obj.valueOf()
        &#125;;
        if (Utils.isPrimitive(obj.toString())) &#123;
            return obj.toString()
        &#125;;
    &#125; else &#123;
        if (Utils.isPrimitive(obj.toString())) &#123;
            return obj.toString()
        &#125;;
        if (Utils.isPrimitive(obj.valueOf())) &#123;
            return obj.valueOf()
        &#125;;
    &#125;
&#125;
​
var a=&#123;&#125;;
ToPrimitive(a);//"[object Object]",与上面文字分析的一致
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>学习自 <a href="https://juejin.im/post/6844904104402092039#heading-0" target="_blank" title="https://juejin.im/post/6844904104402092039#heading-0"><strong>冴羽大佬</strong></a></p>
</blockquote>
<h2 data-id="heading-56">隐式类型转换</h2>
<p>一元运算符(-,+)</p>
<p>他只会正确转换十六进制和十进制，但是不会转化八进制组成的字符串。</p>
<pre><code class="copyable">console.log(+"0xA")//10
console.log(+"071")//71
console.log(010)//8。这里还是可以转化8进制的数字的，但是不可以转化八进制的字符串
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比较(==)</p>
<p>如果两个值分别是<strong>数字</strong>和<strong>字符串</strong>/<strong>布尔值</strong>，其实都是转化为数字，再比较。</p>
<pre><code class="copyable">x是数字，y是字符串，判断x == ToNumber(y)
​
x是字符串，y是数字，判断ToNumber(x) == y
​
x是布尔值，判断ToNumber(x) == y
​
y是布尔值，判断x ==ToNumber(y)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当一方是布尔值的时候，会对布尔值进行转换，因为这种特性，所以尽量少使用 <code>xx == true</code> 和 <code>xx == false</code> 的写法。</p>
<p>比如:</p>
<pre><code class="copyable">// 不建议
if (a == true) &#123;&#125;
​
// 建议
if (a) &#123;&#125;
// 更好
if (!!a) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">console.log(false == undefined)//false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>false == undefined<code>相当于</code>0 == undefined<code>不符合上面的情形，执行最后一步 返回</code>false</p>
<pre><code class="copyable">console.log(false == [])//true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>false == []<code>相当于</code>0 == []<code>相当于</code>0 == ""<code>相当于</code>0 == 0<code>，结果返回</code>true</p>
<pre><code class="copyable">console.log([] == ![])//true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先会执行 <code>![]</code> 操作，转换成 false，相当于 <code>[] == false</code> 相当于 <code>[] == 0</code> 相当于 <code>'' == 0</code> 相当于 <code>0 == 0</code>，结果返回 <code>true</code></p>
<p>疑问：为什么![]表示的是false。</p>
<p>解答：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjawil%2Fblog%2Fissues%2F1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jawil/blog/issues/1" ref="nofollow noopener noreferrer">github</a>，[]表示的是对象，对象都是true，所以![]为false。</p>
<p>最后再举一些会让人踩坑的例子：</p>
<pre><code class="copyable">console.log(false == "0")
console.log(false == 0)
console.log(false == "")
​
console.log("" == 0)
console.log("" == [])
​
console.log([] == 0)
​
console.log("" == [null])
console.log(0 == "\n")
console.log([] == 0)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上均返回 true。</p>
<pre><code class="copyable">[[][0] + []][0][5]+[[][[[][0] + []][0][4]+[[][0] + []][0][5]+[[][0] + []][0][1]+[[][0] + []][0][2]] + []][0][8]+[[[] == []][0] + []][0][2]+[[][[[][0] + []][0][4]+[[][0] + []][0][5]+[[][0] + []][0][1]+[[][0] + []][0][2]] + []][0][6]+[[][[[][0] + []][0][4]+[[][0] + []][0][5]+[[][0] + []][0][1]+[[][0] + []][0][2]]+[]][0][23]+[[][0] + []][0][3]+[[][[[][0] + []][0][4]+[[][0] + []][0][5]+[[][0] + []][0][1]+[[][0] + []][0][2]] + []][0][8]+[+[1 + [[][0] + []][0][3] +309][0] + []][0][7]+[[][[[][0] + []][0][4]+[[][0] + []][0][5]+[[][0] + []][0][1]+[[][0] + []][0][2]] + []][0][6]+[[][0] + []][0][0]
//i love you
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<pre><code class="copyable">1. undefined == null，结果是true。且它俩与所有其他值比较的结果都是false。
​
2. String == Boolean，需要两个操作数同时转为Number。
​
3. String/Boolean == Number，需要String/Boolean转为Number。
​
4. Object == Primitive，需要Object转为Primitive(具体通过valueOf和toString方法)。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们用 Number() 等函数的时候，就是显式类型转换，其转换规则是当是基本类型时，参照规范中的对应表进行转换，当不是基本类型的时候，先参照规范中的 <code>ToPrimitive</code> 方法转换为基本类型，再按照对应表转换，当执行 ToPrimitive 的时候，又会根据情况不同，判断先执行对象的 valueOf 方法还是 toString 方法进行准换。</p>
<h2 data-id="heading-57">强弱类型的判断</h2>
<p>按照计算机语言的类型系统的设计方式,可以分为强类型和弱类型两种。二者之间的区别，就在于计算时是否可以不同类型之间对使用者透明地隐式转换。从使用者的角度来看，如果一个语言可以隐式转换它的所有类型，那么它的变量、表达式等在参与运算时，即使类型不正确，也能通过隐式转换来得到正确地类型，这对使用者而言，就好像所有类型都能进行所有运算一样，所以这样的语言被称作弱类型。与此相对，强类型语言的类型之间不一定有隐式转换。</p>
<h2 data-id="heading-58">js自动插入分号规则</h2>
<p>首先这些规则是基于两点：</p>
<ol start="0">
<li>以换行为基础；</li>
<li>解析器会尽量将新行并入当前行，当且仅当符合ASI规则时才会将新行视为独立的语句。</li>
</ol>
<p>ASI规则</p>
<p><strong>1. 新行并入当前行将构成非法语句，自动插入分号。</strong></p>
<pre><code class="copyable">if(1 < 10) a = 1
console.log(a)
// 等价于
if(1 < 10) a = 1;
console.log(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 在continue,return,break,throw后自动插入分号</strong>。</p>
<p><strong>3. ++、--后缀表达式作为新行的开始，在行首自动插入分号</strong>。</p>
<p><strong>4. 代码块的最后一个语句会自动插入分号</strong>。</p>
<p>No ASI规则：</p>
<p><strong>1. 新行以 ( 开始</strong></p>
<p><strong>2. 新行以 [ 开始</strong></p>
<p><strong>3. 新行以 / 开始</strong></p>
<p><strong>4. 新行以 + 、 - 、 % 和 * 开始</strong></p>
<p><strong>5. 新行以 , 或 . 开始</strong></p>
<h2 data-id="heading-59">&#123;&#125;的两种解读</h2>
<p>①当&#123;&#125;的前面有运算符号的时候，+，-，*，/,()等等，&#123;&#125;都会被解析成对象字面量，这无可争议。 ②当&#123;&#125;前面没有运算符时候但有;结尾的时候，或者浏览器的自动分号插入机制给&#123;&#125;后面插入分号(;)时候，此时&#123;&#125;都会被解析成代码块。 ③如果&#123;&#125;前面什么运算符都没有，&#123;&#125;后面也没有分号(;)结尾，Firefox会始终如一的解析为代码块，而chrome有细微的差别，chrome会解析为对象字面量。</p>
<h2 data-id="heading-60">运算符的优先级</h2>
<h4 data-id="heading-61">ECMAScript 运算符优先级</h4>





























































<table><thead><tr><th>运算符</th><th>描述</th></tr></thead><tbody><tr><td>. [] ()</td><td>字段访问、数组下标、函数调用以及表达式分组</td></tr><tr><td>++ -- - + ~ ! delete new typeof void</td><td>一元运算符、返回数据类型、对象创建、未定义值</td></tr><tr><td>* / %</td><td>乘法、除法、取模</td></tr><tr><td>+ - +</td><td>加法、减法、字符串连接</td></tr><tr><td><< >> >>></td><td>移位</td></tr><tr><td>< <= > >= instanceof</td><td>小于、小于等于、大于、大于等于、instanceof</td></tr><tr><td>== != === !==</td><td>等于、不等于、严格相等、非严格相等</td></tr><tr><td>&</td><td>按位与</td></tr><tr><td>^</td><td>按位异或</td></tr><tr><td>&&</td><td>逻辑与</td></tr><tr><td>?:</td><td>条件</td></tr><tr><td>= oP=</td><td>赋值、运算赋值</td></tr><tr><td>,</td><td>多重求值</td></tr></tbody></table>
<p>自增的是引用，而非值。</p>
<pre><code class="copyable">++[]//报错
​
let a = []
++a//1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析一些列子</p>
<pre><code class="copyable">1. &#123;&#125;+&#123;&#125;//chrome:"[object Object][object Object]"，Firfox:NaN
​
2. &#123;&#125;+[]//0
​
3. []+&#123;&#125;//"[object Object]"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是矛盾在于&#123;&#125;是看成<strong>代码块</strong>还是<strong>对象字面量</strong>。</p>
<p><strong>Firefox始终如一，第一个&#123;&#125;一直解析为代码块，运算符号后面&#123;&#125;解析为对象字面量</strong>。</p>
<p><strong>但是google有时候解析成代码块，有时候解析成对象字面量。</strong> 但是我们可以这样记住：<strong>Chrome对于首是"&#123;"尾是"&#125;"的表达式自动添加了括号。</strong></p>
<blockquote>
<p>学习自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjawil%2Fblog%2Fissues%2F5%23" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jawil/blog/issues/5#" ref="nofollow noopener noreferrer">从<code>++[[]][+[]]+[+[]]==10?</code>深入浅出弱类型JS的隐式转换</a></p>
</blockquote>
<h2 data-id="heading-62">为什么对象值放在堆中，基本数据类型放在栈中？</h2>
<p>能量是守衡的，无非是时间换空间，空间换时间的问题 堆比栈大，栈比堆的运算速度快,对象是一个复杂的结构，并且可以自由扩展，如：数组可以无限扩充，对象可以自由添加属性。将他们放在堆中是为了不影响栈的效率。而是通过引用的方式查找到堆中的实际对象再进行操作。相对于简单数据类型而言，简单数据类型就比较稳定，并且它只占据很小的内存。不将简单数据类型放在堆是因为通过引用到堆中查找实际对象是要花费时间的，而这个综合成本远大于直接从栈中取得实际值的成本。所以简单数据类型的值直接存放在栈中。</p>
<h2 data-id="heading-63">防抖和节流</h2>
<p><strong>apply第二个参数可以是一个数组也可以是一个类数组。</strong></p>
<h4 data-id="heading-64">函数防抖：</h4>
<ul>
<li>
<h5 data-id="heading-65">将几次操作合并为一次操作进行。原理是维护一个计时器，规定在delay时间后触发函数，但是在delay时间内再次触发的话，就会取消之前的计时器而重新设置。这样一来，只有最后一次操作能被触发。</h5>
</li>
</ul>
<pre><code class="copyable"> // 2、防抖功能函数，接受传参
    function debounce(fn, delay=1000) &#123;
      // 4、创建一个标记用来存放定时器的返回值
      let timeout = null;
      return function() &#123;
        // 5、每次当用户点击/输入的时候，把前一个定时器清除
        clearTimeout(timeout);
        // 6、然后创建一个新的 setTimeout，
        // 这样就能保证点击按钮后的 interval 间隔内
        // 如果用户还点击了的话，就不会执行 fn 函数
        timeout = setTimeout(() => &#123;
          fn.apply(this, arguments);
        &#125;, delay);
      &#125;;
    &#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-66">函数节流：</h4>
<ul>
<li>
<h5 data-id="heading-67">使得一定时间内只触发一次函数。原理是通过判断是否到达一定时间来触发函数。</h5>
</li>
</ul>
<pre><code class="copyable"> // 2、节流函数体
    function throttle(fn, delay=1000) &#123;
      // 4、通过闭包保存一个标记
      let canRun = true;
      return function() &#123;
        // 5、在函数开头判断标志是否为 true，不为 true 则中断函数
        if(!canRun) &#123;
          return;
        &#125;
        // 6、将 canRun 设置为 false，防止执行之前再被执行
        canRun = false;
        // 7、定时器
        setTimeout( () => &#123;
          fn.apply(this, arguments);
          // 8、执行完事件（比如调用完接口）之后，重新将这个标志设置为 true
          canRun = true;
        &#125;, delay);
      &#125;;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-68">区别：</h4>
<ul>
<li>
<h5 data-id="heading-69">函数节流不管事件触发有多频繁，都会保证在规定时间内一定会执行一次真正的事件处理函数，而函数防抖只是在最后一次事件后才触发一次函数。 比如在页面的无限加载场景下，我们需要用户在滚动页面时，每隔一段时间发一次 Ajax 请求，而不是在用户停下滚动页面操作时才去请求数据。这样的场景，就适合用节流技术来实现。</h5>
</li>
<li>
<h5 data-id="heading-70">主要是对返回函数的处理。节流是设置开关为false。如果执行到规定的时间。将开关设置为true。利用if函数判断开关。返回空值。不让其继续执行。等到规定时间后会继续执行。防抖是先清除延时器，然后再设置延时器调用函数。</h5>
</li>
</ul>
<h2 data-id="heading-71">浏览器的缓存机制</h2>
<p>强缓存和协商缓存最大也是最根本的区别是：<strong>强缓存命中的话不会发请求到服务器</strong>（比如chrome中的200 from memory cache），<strong>协商缓存一定会发请求到服务器</strong>，通过资源的请求首部字段验证资源是否命中协商缓存，如果协商缓存命中，服务器会将这个请求返回，但是不会返回这个资源的实体，而是通知客户端可以从缓存中加载这个资源（304 not modified）。</p>
<p>浏览器第一次向服务器发起该请求后拿到请求结果，会根据<strong>响应报文中HTTP头的缓存标识</strong>，决定是否缓存结果，是则将请求结果和缓存标识存入浏览器缓存中。</p>
<ul>
<li>浏览器每次发起请求，都会先在浏览器缓存中查找该请求的结果以及缓存标识</li>
<li>浏览器每次拿到返回的请求结果都会将该结果和缓存标识存入浏览器缓存中，用于更新上次缓存的结果。</li>
</ul>
<p>限制缓存时间</p>
<ul>
<li>Cache-Control： max-age， 单位是秒。是一个相对时间，用以表达自上次请求正确的资源之后的多少秒的时间段内缓存有效。</li>
<li>Expires(期满，终止)是一个绝对时间。用以表达在这个时间点之前发起请求可以直接从浏览器中读取数据，而无需发起请求</li>
<li>Cache-Control的优先级比Expires的优先级高。前者的出现是为了解决Expires在浏览器时间被手动更改导致缓存判断错误的问题。 如果同时存在则使用Cache-control。</li>
</ul>
<p>Cache-Control的优先级比expires高</p>
<h5 data-id="heading-72">强制缓存</h5>
<p>强制缓存就是向浏览器缓存查找该请求结果，并根据该结果的缓存规则来决定是否使用该缓存结果的过程。</p>
<p>缓存最后到达两个位置中。利用size做标识。</p>
<ul>
<li>from memory cache代表使用内存中的缓存，from disk cache则代表使用的是硬盘中的缓存，浏览器读取缓存的顺序为memory –> disk。</li>
</ul>
<p>在浏览器中，浏览器会在js和图片等文件解析执行后直接存入内存缓存中，那么当刷新页面时只需直接从内存缓存中读取(from memory cache)；而css文件则会存入硬盘文件中，所以每次渲染页面都需要从硬盘读取缓存(from disk cache)。</p>
<h4 data-id="heading-73">协商缓存</h4>
<p><strong>协商缓存就是强制缓存失效后，</strong> 浏览器携带缓存标识向服务器发起请求，由服务器根据缓存标识决定是否使用缓存的过程。</p>
<p>协商缓存的标识也是在响应报文的HTTP头中和请求结果一起返回给浏览器的，控制协商缓存的字段分别有：Last-Modified / If-Modified-Since和Etag / If-None-Match，其中Etag / If-None-Match的优先级比Last-Modified / If-Modified-Since高。</p>
<ul>
<li>Last-Modified是服务器响应请求时，返回该资源文件在服务器最后被修改的时间。</li>
<li>Last-Modified/If-Modified-since表示的是服务器的资源最后一次修改的时间；</li>
<li>Etag/If-None-match表示的<strong>是服务器资源的唯一标识</strong>，只要资源变化，Etag就会重新生成。</li>
</ul>
<p>If-Modified-Since则是客户端再次发起该请求时，携带上次请求返回的Last-Modified值，通过此字段值告诉服务器该资源上次请求返回的最后被修改时间。服务器收到该请求，发现请求头含有If-Modified-Since字段，则会根据If-Modified-Since的字段值与该资源在服务器的最后被修改时间做对比，若服务器的资源最后被修改时间大于If-Modified-Since的字段值，则重新返回资源，状态码为200；否则则返回304，代表资源无更新，可继续使用缓存文件。（<strong>就是当上次从服务器返回的最后修改时间小于再次请求时服务器对该文件的修改时间，就重新请求文件。</strong> ）</p>
<ul>
<li>Etag是服务器响应请求时，返回当前资源文件的一个唯一标识(由服务器生成)。<strong>这个可以解决Last-Modified 的时间精度和准确度问题</strong></li>
</ul>
<p>If-None-Match是客户端再次发起该请求时，携带上次请求返回的唯一标识Etag值，通过此字段值告诉服务器该资源上次请求返回的唯一标识值。服务器收到该请求后，发现该请求头中含有If-None-Match，则会根据If-None-Match的字段值与该资源在服务器的Etag值做对比，一致则返回304，代表资源无更新，继续使用缓存文件；不一致则重新返回资源文件，状态码为200。</p>
<p><strong>注：Etag / If-None-Match优先级高于Last-Modified / If-Modified-Since，同时存在则只有Etag / If-None-Match生效。</strong></p>
<p>总结：强制缓存优先于协商缓存。协商缓存成功则返回304状态码，继续使用缓存。否则返回200状态码，重新请求资源。HTTP 缓存可以分为强制缓存和协商缓存，强制缓存就是在缓存有效期内直接使用浏览器缓存；协商缓存则需要先询问服务端资源是否发生改变，如果未改变再使用浏览器缓存。</p>
<p><img src="https://juejin.cn/post/6990725554852855839" alt="image-20210301134157751" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-74">数组乱序</h2>
<pre><code class="copyable">​
// 方法一。该方法有缺陷，大多数元素的位置是不变的
function mixArr(arr) &#123;
  return arr.sort(() => Math.random() - 0.5)
&#125;
​
// 方法二。 洗牌算法
​
function shunflee(arr) &#123;
  const len = arr.length
  while(len > 1) &#123;
    const index = parsetInt(Math.random() * len--)
    [arr[index], arr[len]] = [arr[len], arr[index]]
  &#125;
  return arr
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-75">数组去重</h2>
<pre><code class="copyable">// 方法一。 利用对象的键不能重复的特点
function removeDup(arr) &#123;
  const obj = &#123;&#125;
  arr.forEach((item) => &#123;
    if(!obj[item]) &#123;
      obj[item] = true
    &#125;
  &#125;)
  return Object.keys(obj)
&#125;
​
// 方法二。 set数据结构
Array.from(new Set(arr))
[...new Set(arr)]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-76">new 操作符作用和实现</h2>
<p>1.创建一个对象</p>
<p>2.绑定prototype</p>
<p>3.改变this指向</p>
<p>4.返回新的对象</p>
<pre><code class="copyable">function MyNew(Constructor, ...arg) &#123;
  // 1.创建一个对象
  const newObj = &#123;&#125;
 // 2.绑定prototype
  newObj.__proto__ = Constructor.prototype
 // 3.改变this指向
  Constructor.call(newObj, ...arg)
 // 4.返回新的对象
  return newObj
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-77">数组的sort方法</h2>
<pre><code class="copyable"> let arr = [1, 22, 11, 332, 42, 12, 222]
 arr.sort((a, b) => &#123;
   //前一个参数是数组的后一项，第二个参数是数组的前一项
   // console.log(a, b)
   // 升序是按顺序相减，降序是反向相减。
   return a - b
 &#125;)
// 原数组被改变。
console.log(arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-78">字符串去重</h2>
<pre><code class="copyable">const str = [...new Set("zhhsajwnns")].join("");
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-79">闭包</h2>
<p>内部函数引用外部函数的变量，他会单独放在一个活动对象中，如果外部对象执行完毕，他的内存空间会被释放，但是内部函数所引用的那个活动对象不会被释放。</p>
<h4 data-id="heading-80">优点</h4>
<ol start="0">
<li>可以从内部函数访问外部函数的作用域中的变量，且访问到的变量长期驻扎在内存中，可供之后使用</li>
<li>避免变量污染全局</li>
<li>把变量存到独立的作用域，作为私有成员存在</li>
</ol>
<h4 data-id="heading-81">缺点</h4>
<ol start="0">
<li>对内存消耗有负面影响。因内部函数保存了对外部变量的引用，导致无法被垃圾回收，增大内存使用量，所以使用不当会导致内存泄漏</li>
<li>对处理速度具有负面影响。闭包的层级决定了引用的外部变量在查找时经过的作用域链长度</li>
<li>可能获取到意外的值(captured value)</li>
</ol>
<h2 data-id="heading-82">类数组和数组</h2>
<p>转化：转换后数组的长度会有length决定。索引不连续时转换结果是连续的，会自动补位。</p>
<ol start="0">
<li>
<p>Array.from()：不连续的索引，设置为undefined</p>
<pre><code class="copyable">// 代码示例
let al2 = &#123;
    length: 4,
    '-1': -1,
    '0': 0,
    a: 'a',
    1: 1
&#125;;
console.log(Array.from(al2)); // [0, 1, undefined, undefined]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Array.prototype.slice.call()：生成的是稀疏数组。</p>
<pre><code class="copyable">// 代码示例
let al2 = &#123;
    length: 4,
    '-1': -1,
    '0': 0,
    a: 'a',
    1: 1
&#125;;
console.log(Array.prototype.slice.call(al2)); //[0, 1, empty × 2]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-83">内存泄漏</h2>
<ol start="0">
<li>闭包使用不当引起内存泄漏</li>
<li>全局变量（js不会主动回收全局变量中的垃圾）</li>
<li>分离的DOM节点</li>
<li>控制台的打印</li>
<li>遗忘的定时器</li>
</ol>
<h2 data-id="heading-84">执行上下文对象</h2>
<p>变量对象</p>
<p>作用域链</p>
<p>this</p>
<h3 data-id="heading-85">通过底层思想判断this指向</h3>
<p>1.计算 MemberExpression （函数括号左边的部分）的结果赋值给 ref</p>
<p>2.判断 ref 是不是一个 Reference 类型</p>
<p>Reference 的构成，由三个组成部分，分别是：</p>
<ul>
<li>base value：属性所在的对象或者就是 EnvironmentRecord</li>
<li>referenced name： 变量名称</li>
<li>strict reference</li>
</ul>
<p>3.如果 ref 是 Reference，并且 IsPropertyReference(ref) 是 true, 那么 this 的值为 GetBase(ref)</p>
<ul>
<li>IsPropertyReference判断是否为true？如果base value为一个对象，他就是true。</li>
</ul>
<p>如果 ref 不是Reference，那么 this 的值为 undefined。在严格模式下，在非严格模式下是window</p></div>  
</div>
            