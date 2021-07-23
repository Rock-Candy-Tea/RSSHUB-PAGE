
---
title: '实现一个vite（react版）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e35e55b9dfea405f8a739cf9bf1578f7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 05:14:26 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e35e55b9dfea405f8a739cf9bf1578f7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>本文参考了vite的0.x版本的源码，由于0.x版本只支持vue和esm依赖，react并没有esm包，所以这里并进行了一些react支持方面的改造，供学习和交流
阅读完本文，读者应该能够了解：</p>
<ul>
<li>es module相关的知识</li>
<li>koa的基本使用</li>
<li>vite的核心原理</li>
<li>dev-server自动更新的原理</li>
<li>esbuild的基础用法</li>
</ul>
</blockquote>
<p><a name="user-content-btB4v" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-0">预备知识</h3>
<p><a name="user-content-VcS33" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-1">es modules</h4>
<p>vite通过新版本浏览器支持的es modules来加载依赖<br>你需要把 type="module" 放到 script标签中, 来声明这个脚本是一个模块</p>
<pre><code class="copyable"><script type="module">
    // index.js可以通过export导出模块，也可以在其中继续使用import加载其他依赖 
    import App from './index.js'
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br>遇到import时，会自动发送一个http请求，来获取对应模块的内容，相应类型content-type=text/javascript
<a name="user-content-TGAry" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-2">基本架构</h3>
<p><a name="user-content-inAUK" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e35e55b9dfea405f8a739cf9bf1578f7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">vite原理</h3>
<p>首先我们创建一下vite项目跑一下</p>
<pre><code class="copyable">yarn create vite my-react-app --template react
yarn dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f50e3b34c35a4769bcbc198853c6f09f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>浏览器发出了一个请求，请求了main.jsx<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/672e493577c1412bba3e3327f3f7b98d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7750fefe827c463c8d53f155274d80c7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>查看main.jsx的内容，我们可以发现，vite启动的·服务器对引入模块的路径进行了处理，对jsx写法也进行了处理，转化成了浏览器可以运行的代码<br>继续看<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad304158eeb04d0589232958e4fc4ecb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abf1e1606ba14c5e8b8db68f74e69fd5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>在client中，我们看到了websocket的代码，所以可以理解为vite服务器注入客户端的websocket代码，用来获取服务器中代码的变化的通知，从而达到热更新的效果<br>综上，我们知道了vite服务器做的几件事：</p>
<ul>
<li>读取本地代码文件</li>
<li>解析引入模块的路径并重写</li>
<li>websocket代码注入客户端</li>
</ul>
<p><a name="user-content-NMujg" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-4">代码实现</h3>
<p>本文的完整代码在：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyklydxtt%2Fvite-react" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yklydxtt/vite-react" ref="nofollow noopener noreferrer">github.com/yklydxtt/vi…</a><br>这里我们分五步：</p>
<ol>
<li>创建服务</li>
<li>读取本地静态资源</li>
<li>并重写模块路径</li>
<li>解析模块路径</li>
<li>处理css文件</li>
<li>websocket代码注入客户端</li>
</ol>
<p><a name="user-content-lu7Qn" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-5">1.创建服务</h4>
<p>创建index.js</p>
<pre><code class="copyable">// index.js
const  Koa = require('koa');
const serveStaticPlugin = require('./plugins/server/serveStaticPlugin');
const rewriteModulePlugin=require('./plugins/server/rewriteModulePlugin');
const moduleResolvePlugin=require('./plugins/server/moduleResolvePlugin');

function createServer() &#123;
    const app = new Koa();
    const root = process.cwd();
    const context = &#123;
        app,
        root
    &#125;
    const resolvePlugins = [
        // 重写模块路径
        rewriteModulePlugin,
        // 解析模块内容
        moduleResolvePlugin,
        // 配置静态资源服务
        serveStaticPlugin,
    ]
    resolvePlugins.forEach(f => f(context));
    return app;
&#125;
module.exports = createServer;
createServer().listen(3001);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们使用koa创建了一个服务,<br>还注册了三个插件，分别用来配置静态资源，解析模块内容，重写模块里import其他模块路径<br>我们来分别实现这三个插件的功能
<a name="user-content-yGhck" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-6">2.配置静态资源,读取本地代码</h4>
<pre><code class="copyable">const  KoaStatic = require('koa-static');
const path = require('path');

module.exports = function(context) &#123;
    const &#123; app, root &#125; = context;
    app.use(KoaStatic(root));
    app.use(KoaStatic(path.join(root,'static')));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们创建一个static目录<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c5befd78e40405681433e25a24254b5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>我们用koa-static代理static目录下的静态资源<br>index.html中的内容如下：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7db2bd77c30344dbb5f85289c836dc4d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>执行</p>
<pre><code class="copyable">node index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>访问loaclhost:3001<br>可以到我们刚刚写的index.html的内容<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ba3be3009c444a3b5ad4ca1eef3c961~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-H5IEl" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-7">3.重写模块路径</h4>
<p>我们来实现rewriteModulePlugin.js,作用是重写import后的路径<br>把这样的路径<br>import  React,&#123;ReactDOM &#125; from 'es-react'<br>改为<br>import  React,&#123;ReactDOM &#125; from '/__module/es-react'</p>
<pre><code class="copyable">// plugins/server/rewriteModulePlugin.js

const &#123;readBody,rewriteImports&#125;=require('./utils');


module.exports=function(&#123;app,root&#125;)&#123;
    app.use(async (ctx,next)=>&#123;
        await next();

        if (ctx.url === '/index.html') &#123;
        // 修改script标签中的路径
            const html = await readBody(ctx.body)
            ctx.body = html.replace(
              /(<script\b[^>]*>)([\s\S]*?)<\/script>/gm,
              (_, openTag, script) => &#123;
                return `$&#123;openTag&#125;$&#123;rewriteImports(script)&#125;</script>`
              &#125;
            )
          &#125;

        if(ctx.body&&ctx.response.is('js'))&#123;
            //  修改js中的路径
            const content=await readBody(ctx.body);
            ctx.body=rewriteImports(content,ctx.path);
        &#125;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现一下rewriteImports函数和readBody</p>
<pre><code class="copyable">const path = require('path');
const &#123; parse &#125; = require('es-module-lexer');
const &#123;Readable&#125; =require('stream');
const resolve=require('resolve-from');
const MagicString = require('magic-string');

async function readBody(stream)&#123;
    if(stream instanceof Readable)&#123;
        return new Promise((resolve,reject)=>&#123;
            let res='';
            stream.on('data',(data)=>res+=data);
            stream.on('end',()=>resolve(res));
            stream.on('error',(e)=>reject(e));
        &#125;)
    &#125;else&#123;
        return stream.toString();
    &#125;
&#125;

function rewriteImports(source,modulePath)&#123;
    const imports=parse(source)[0];
    const magicString=new MagicString(source);
    imports.forEach(item=>&#123;
        const &#123;s,e&#125;=item;
        let id = source.substring(s,e);
        const reg = /^[^\/\.]/;
        const moduleReg=/^\/__module\//;
        if(moduleReg.test(modulePath))&#123;
        // 如果有/__module/前缀，就不用加了
            // 处理node_modules包中的js
            if(modulePath.endsWith('.js'))&#123;
                id=`$&#123;path.dirname(modulePath)&#125;/$&#123;id&#125;`
            &#125;else&#123;
                id=`$&#123;modulePath&#125;/$&#123;id&#125;`;
            &#125;
            magicString.overwrite(s,e,id);
            return;
        &#125;
        if(reg.test(id))&#123;
        // 对于前面没有/__module/前缀的node_modules模块的import，加上前缀
            id=`/__module/$&#123;id&#125;`;
            magicString.overwrite(s,e,id);
        &#125;
    &#125;);
    return magicString.toString();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​<br>
<a name="user-content-NGehn" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-8">4.读取node_modules模块内容</h4>
<p>我们来实现moduleResolvePlugin<br>因为我们只代理了static目录下的文件，所以需要读取node_modules的文件，就需要处理一下<br>主要功能是解析到/__module前缀，就去node_modules读取模块内容</p>
<pre><code class="copyable">// ./plugins/server/moduleResolvePlugin.js
const &#123; createReadStream &#125; = require('fs');
const &#123; Readable &#125; = require('stream');
const &#123; rewriteImports, resolveModule &#125; = require('./utils');


module.exports = function (&#123; app, root &#125;) &#123;
  app.use(async (ctx, next) => &#123;
    // koa的洋葱模型
    await next();

// 读取node_modules中的文件内容
    const moduleReg = /^\/__module\//;
    if (moduleReg.test(ctx.path)) &#123;
      const id = ctx.path.replace(moduleReg, '');
      ctx.type = 'js';
      const modulePath = resolveModule(root, id);
      if (id.endsWith('.js')) &#123;
        ctx.body = createReadStream(modulePath);
        return;
      &#125; else &#123;
        ctx.body = createReadStream(modulePath);
        return;
      &#125;
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取node模块的路径：</p>
<pre><code class="copyable">// ./plugins/server/utils.js
const path = require('path');
const &#123; parse &#125; = require('es-module-lexer');
const &#123;Readable&#125; =require('stream');
const resolve=require('resolve-from');  // 这个包的功能类似require，返回值是require的路径
const MagicString = require('magic-string');

// 返回node_modules依赖的绝对路径
function resolveModule(root,moduleName)&#123;
    let modulePath;
    if(moduleName.endsWith('.js'))&#123;
        modulePath=path.join(path.dirname(resolve(root,moduleName)),path.basename(moduleName));
        return modulePath;
    &#125;
    const userModulePkg=resolve(root,`$&#123;moduleName&#125;/package.json`);
    modulePath=path.join(path.dirname(userModulePkg),'index.js');
    return modulePath;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，基本功能完成<br>在static下添加代码：</p>
<pre><code class="copyable">// static/add.js
// 因为react没有esm格式的包，所以这里用es-react代替react
import  React,&#123;ReactDOM &#125; from 'es-react'
import LikeButton from './like_button.js';

const e = React.createElement;
const domContainer=document.getElementById("like_button_container");

ReactDOM.render(e(LikeButton), domContainer);

export default function add(a, b) &#123;
    return a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// static/like_button.js
import React from 'es-react'

const e = React.createElement;

export default class LikeButton extends React.Component &#123;
  constructor(props) &#123;
    super(props);
    this.state = &#123; liked: false &#125;;
  &#125;

  render() &#123;
    if (this.state.liked) &#123;
      return 'You liked this.';
    &#125;
    // 因为没有用babel解析，所以这里没有用jsx，使用createElement的写法
    return e(
      'button',
      &#123; onClick: () => this.setState(&#123; liked: true &#125;) &#125;,
      'Like'
    );
  &#125;
&#125;



<span class="copy-code-btn">复制代码</span></code></pre>
<p>试着执行</p>
<pre><code class="copyable">node index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到如下页面<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/843e7d8b274a4e519d7701f85d4d2489~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-yaNGI" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-9">5.处理css文件</h4>
<p>添加一个like_button.css</p>
<pre><code class="copyable">// ./static.like_button.css

h1&#123;
  color: #ff0
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在like_button.js中引入</p>
<pre><code class="copyable">// like_button.js

import './like_button.css';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刷新页面会看到这样的报错：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fed16ef707ea4fbdbf40b9ba485617d9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>es modules并不支持css，所以需要将css文件转为js.或者转为在link标签中引入<br>在rewriteModulePlugin.js中添加处理css的判断</p>
<pre><code class="copyable">const &#123;readBody,rewriteImports&#125;=require('./utils');


module.exports=function(&#123;app,root&#125;)&#123;
    app.use(async (ctx,next)=>&#123;
        await next();

        if (ctx.url === '/index.html') &#123;
            const html = await readBody(ctx.body)
            ctx.body = html.replace(
              /(<script\b[^>]*>)([\s\S]*?)<\/script>/gm,
              (_, openTag, script) => &#123;
                return `$&#123;openTag&#125;$&#123;rewriteImports(script)&#125;</script>`
              &#125;
            )
          &#125;

        if(ctx.body&&ctx.response.is('js'))&#123;
            const content=await readBody(ctx.body);
            ctx.body=rewriteImports(content,ctx.path);
        &#125;

// 处理css
        if(ctx.type==='text/css')&#123;
          ctx.type='js';
          const code=await readBody(ctx.body);
          ctx.body=`
          const style=document.createElement('style');
          style.type='text/css';
          style.innerHTML=$&#123;JSON.stringify(code)&#125;;
          document.head.appendChild(style)
          `
        &#125;
    &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新启动服务<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b76f4ba52c5425aab771dd3f89ccd4b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>样式就有了<br>like_button.css的请求body变成了如下的样子<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75bb743a99044bcf9d162d6408857f38~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-Y2g5F" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-10">6.实现热更新</h4>
<p>热更新借助websocket来实现<br>客户端代码</p>
<pre><code class="copyable">// ./plugins/client/hrmClient.js
const socket = new WebSocket(`ws://$&#123;location.host&#125;`)

socket.addEventListener('message',(&#123;data&#125;)=>&#123;
    const &#123;type&#125;=JSON.parse(data);
    switch(type)&#123;
        case 'update':
            location.reload();
            break;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>服务端添加一个中间件hmrWatcherPlugin.js<br>作用是将hrmClient.js的内容发送给客户端，并监听代码的变化，如果有变化，就通过ws发消息给客户端</p>
<pre><code class="copyable">// ./plugins/server/hmrWatcherPlugin.js
const fs = require('fs');
const path = require('path');
const chokidar =require('chokidar');

module.exports = function (&#123; app,root &#125;) &#123;
    const hmrClientCode = fs.readFileSync(path.resolve(__dirname, '../client/hmrClient.js'))
    app.use(async (ctx, next) => &#123;
        await next();
        将hrmClient.js的内容发送给客户端
        if (ctx.url === '/__hmrClient') &#123;
            ctx.type = 'js';
            ctx.body = hmrClientCode;
        &#125;
            if(ctx.ws)&#123;
            // 监听本地代码的变化
                const ws=await ctx.ws();
                const watcher = chokidar.watch(root, &#123;
                    ignored: [/node_modules/]
                &#125;);
                watcher.on('change',async ()=>&#123;
                        ws.send(JSON.stringify(&#123; type: 'update' &#125;));
                &#125;)
            &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对rewriteModulePlugin.js中对index.html的处理进行修改</p>
<pre><code class="copyable">// plugins/server/rewriteModulePlugin.js

...
app.use(async (ctx,next)=>&#123;
        await next();
        if (ctx.url === '/') &#123;
            const html = await readBody(ctx.body);

            ctx.body = html.replace(
              /(<script\b[^>]*>)([\s\S]*?)<\/script>/gm,
              (_, openTag, script) => &#123;
              // 添加对websock代码的请求
                return `$&#123;openTag&#125;import "/__hmrClient"\n$&#123;rewriteImports(script)&#125;</script>`
              &#125;
            )
          &#125;
 ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加完成后重启服务<br>对like_button.js进行修改，给button加一个感叹号，保存</p>
<pre><code class="copyable">...
return e(
      'button',
      &#123; onClick: () => this.setState(&#123; liked: true &#125;) &#125;,
      'Like!'
    );
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到页面有了更新，感叹号有了<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/966b4aae4c384134a9546b810fbc4bc0~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-OuuW8" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-11">7.对jsx代码处理</h4>
<p>vite中是通过esbuild来处理的<br>在对rewriteImports进行改造，使用esbuild把jsx转化成React.createElement的形式</p>
<pre><code class="copyable">// plugins/server/utils.js

function rewriteImports(source,modulePath)&#123;
 // ...
        const code=esbuild.transformSync(source, &#123;
        loader: 'jsx',
      &#125;).code;
    const imports=parse(code)[0];
    const magicString=new MagicString(code);
    imports.forEach(item=>&#123;
        const &#123;s,e&#125;=item;
        let id = code.substring(s,e);
        const reg = /^[^\/\.]/;
        const moduleReg=/^\/__module\//;
        if(moduleReg.test(modulePath))&#123;
            if(modulePath.endsWith('.js'))&#123;
                id=`$&#123;path.dirname(modulePath)&#125;/$&#123;id&#125;`
            &#125;else&#123;
                id=`$&#123;modulePath&#125;/$&#123;id&#125;`;
            &#125;
            magicString.overwrite(s,e,id);
            return;
        &#125;
    // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d455a14722534db9913e13dd65466774~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>jsx代码也渲染出来了
<a name="user-content-jD5uU" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-12">尾声</h3>
<p>本文是通过阅读vite源码并加上一点自己的理解写出来的，为了方便大家理解，只实现了核心功能，细节方便没有做过多说明，如果有错误希望得到指正。<br><strong>如果大家有收获，请给我点个赞Thanks♪(･ω･)ﾉ</strong><br>
<br>陌小路：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiaohanglin.site%2Fpages%2Fb632f1%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://xiaohanglin.site/pages/b632f1/" ref="nofollow noopener noreferrer">Vite原理分析</a><br></p></div>  
</div>
            