
---
title: 'vite原理的简单介，以及vite插件开发指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbcf41505b2d456abf64f62af6574f12~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:47:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbcf41505b2d456abf64f62af6574f12~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概念</h2>
<blockquote>
<p>基于esm（浏览器原生es Module的支持）</p>
</blockquote>
<ol>
<li>Vite，一个基于浏览器原生ES模块的开发服务器。利用浏览器去解析模块，在服务器端按需编译返回，完全跳过了打包这个概念，服务器随起随用。同时另有有Vue文件支持，还搞定了热更新，而且热更新的速度不会随着模块增加而变慢。</li>
<li>Vite要求项目完全由ES模块模块组成，common.js模块不能直接在Vite上使用。因此不能直接在生产环境中使用。在打包上依旧还是使用rollup等传统打包工具。</li>
<li>Vite的基本实现原理，就是启动一个koa服务器拦截浏览器请求ES模块的请求。通过路径查找目录下对应文件的文件做一定的处理最终以ES模块格式返回给客户端</li>
</ol>
<h2 data-id="heading-1">实现步骤</h2>
<p>首先启动一个koa服务器，对首页(index.html)、js文件、裸模块比如"vue"、vue文件等进行分别处理<br></p>
<ol>
<li>先返回index.html,然后再index.html中去加载main.js,在main.js中再去加载其它文件</li>
<li>加载main.js中的裸模块，比如"vue",vite会通过预打包，将vue模块的内容打包到node_modules中，然后替换路径 <br></li>
</ol>
<p>import &#123;createApp&#125; from 'vue' 转换成 import &#123;createApp&#125; from '/@modules/vue'<br>
通过 /@modules标识去node_module中查找并返回相对地址<br>
3. 加载vue文件，当Vite遇到一个.vue后缀的文件时使用vue中的compiler方法进行解析并返回。<br>
由于.vue模板文件的特殊性，它被分割成三个模块（template，css，脚本模块）进行分别处理。最后放入script，template，css发送多个请求获取。</p>
<h2 data-id="heading-2">在vue中的文件执行顺序</h2>
<p>localhost ==》 client(websocket) ==> main.js ==> env.js ==> vue.js(裸模块vue) ==> app.vue ==> 最后就是执行里面的路由，组件，ui库等</p>
<h2 data-id="heading-3">热更新原理</h2>
<p>Vite的热加载原理，实际上就是在客户端与服务端建立了一个websocket链接，当代码被修改时，服务端发送消息通知客户端去请求修改模块的代码，完成热更新。<br>
查看network,在localhost后会执行client文件，就是在这里建立webcocket实现热更新，然后再进入main.js</p>
<h2 data-id="heading-4">服务端原理</h2>
<p>服务端做的就是监听代码文件的更改，在适当的时机向客户端发送websocket信息通知客户端去请求新的模块代码。</p>
<h2 data-id="heading-5">客户端原理</h2>
<p>Vite的websocket相关代码在处理html中时被编写代码中</p>
<h2 data-id="heading-6">简单vite代码实现</h2>
<p>/src/app.vue</p>
<pre><code class="copyable"><template>
  <div>&#123;&#123; title &#125;&#125;</div>
</template>

<script>
import &#123; ref &#125; from "vue";
export default &#123;
  setup() &#123;
    const title = ref("hello, kvite!");
    return &#123; title &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src/main.js</p>
<pre><code class="copyable">import &#123;createApp&#125; from 'vue'
import App from "./app.vue"

createApp(App).mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.html</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>kvite</title>
</head>

<body>
    <div id="app"></div>
    <script>
        window.process = &#123;
            env:&#123;
                NODE_ENV:'dev'
            &#125;
        &#125;
    </script>
    <script type="module" src="/src/main.js"></script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>kvite.js</p>
<pre><code class="copyable">const Koa = require('koa')
const app = new Koa()

const opn = require('opn');
const fs = require("fs")
const path = require("path")
const complierSFC = require('@vue/compiler-sfc') //引入vue文件的解析
const complierDOM = require('@vue/compiler-dom') //引入template的解析

// 中间件配置
// 处理路由
app.use(async (ctx) => &#123;
  const &#123;
    url,
    query
  &#125; = ctx.request

  // 首页请求
  if (url === '/') &#123;
    //加载index.html
    ctx.type = "text/html";
    ctx.body = fs.readFileSync(path.join(__dirname, "./index.html"), "utf8");
  &#125; else if (url.endsWith('.js')) &#123;
    // js文件加载处理
    const p = path.join(__dirname, url)
    ctx.type = 'application/javascript'
    ctx.body = rewriteImport(fs.readFileSync(p, 'utf8'))
  &#125; else if (url.startsWith("/@modules/")) &#123;
    //裸模块名称
    const moduleName = url.replace("/@modules/", "");
    //去node_modules目录中找
    const prefix = path.join(__dirname, "./node_modules", moduleName);
    //package.json中获取module字段
    const module = require(prefix + "/package.json").module;
    const filePath = path.join(prefix, module);
    const ret = fs.readFileSync(filePath, "utf8");
    ctx.type = 'application/javascript'
    ctx.body = rewriteImport(ret)
  &#125; else if (url.indexOf('.vue') > -1) &#123;
    //获取加载文件路径
    const p = path.join(__dirname, url.split("?")[0]);
    const ret = complierSFC.parse(fs.readFileSync(p, 'utf8')); // console.log(ret)  可以看到是一颗ast树，可以在终端中查看
    if (!query.type) &#123;
      //SFC请求，读取vue文件，解析为js
      //获取脚本部分的内容
      const scriptContent = ret.descriptor.script.content;
      //替换默认导出为一个常量，方便后续修改
      const script = scriptContent.replace(
        "export default ",
        "const __script = "
      );
      ctx.type = 'application/javascript'
      ctx.body = `
        $&#123;rewriteImport(script)&#125;
        // 解析template
        import &#123;render as __render&#125; from '$&#123;url&#125;?type=template'
        __script.render = __render
        export default __script
        `;
    &#125; else if (query.type === "template") &#123;
      const tpl = ret.descriptor.template.content;
      //编译为render
      const render = complierDOM.compile(tpl, &#123;
        mode: "module"
      &#125;).code;
      ctx.type = 'application/javascript'
      ctx.body = rewriteImport(render)
    &#125;
  &#125;
&#125;)

// 裸模块地址的重写
//在vite中对于vue这种裸模块是无法识别的，它通过预编译把需要的模块打包到node_modules中，再通过相对地址找到并加载，
//这里我们通过识别 /@modules 这种地址标识，去找寻模块，进行地址的替换
//import xx from "vue"  ==> import xx from "/@modules/vue"
function rewriteImport(content) &#123;
  return content.replace(/ from ['"](.*)['"]/g, function (s1, s2) &#123;
    if (s2.startsWith("./") || s2.startsWith("/") || s2.startsWith("../")) &#123;
      return s1
    &#125; else &#123;
      //裸模块替换
      return ` from '/@modules/$&#123;s2&#125;'`
    &#125;
  &#125;)
&#125;

app.listen(6666, () => &#123;
  console.log('kvite start');
  opn(`http://localhost:6666/`);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FupJiang%2Fkvite" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/upJiang/kvite" ref="nofollow noopener noreferrer">代码地址</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1dh411S7Vz" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1dh411S7Vz" ref="nofollow noopener noreferrer">vite工作原理和手写实现视频地址</a></p>
<h2 data-id="heading-7">vite在使用中的问题</h2>
<p>qs对vite打包后好像不兼容 ，最后使用qs-stringfy</p>
<p>require模块不能使用，需要使用import.meta.glob</p>
<h2 data-id="heading-8">vite插件</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbcf41505b2d456abf64f62af6574f12~tplv-k3u1fbpfcp-watermark.image" alt="Image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db99c0f50eba4ace913abfc9a6070ddf~tplv-k3u1fbpfcp-watermark.image" alt="Image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>插件案例</p>
<pre><code class="copyable">/plugins/vite-plugin-my-example.ts

export default function myExample () &#123;
    // 返回的是插件对象
    return &#123;
      name: 'my-example', // 名称用于警告和错误展示
      // enforce: 'pre'|'post'
      // 初始化hooks，只走一次
      options(opts) &#123;
        console.log('options', opts);
      &#125;,
      buildStart() &#123;
        console.log('buildStart');
      &#125;,
      config(config) &#123;
        console.log('config', config);
        return &#123;&#125;
      &#125;,
      configResolved(resolvedCofnig) &#123;
        console.log('configResolved');
      &#125;,
      configureServer(server) &#123;
        console.log('configureServer');
        // server.app.use((req, res, next) => &#123;
        //   // custom handle request...
        // &#125;)
      &#125;,
      transformIndexHtml(html) &#123;
        console.log('transformIndexHtml');
        return html
        // return html.replace(
        //   /<title>(.*?)<\/title>/,
        //   `<title>Title replaced!</title>`
        // )
      &#125;,
      // id确认
      resolveId ( source ) &#123;
        if (source === 'virtual-module') &#123;
          console.log('resolvedId', source);
          return source; // 返回source表明命中，vite不再询问其他插件处理该id请求
        &#125;
        return null; // 返回null表明是其他id要继续处理
      &#125;,
      // 加载模块代码
      load ( id ) &#123;
        if (id === 'virtual-module') &#123;
          console.log('load');
          return 'export default "This is virtual!"'; // 返回"virtual-module"模块源码
        &#125;
        return null; // 其他id继续处理
      &#125;,
      // 转换
      transform(code, id) &#123;
        if (id === 'virtual-module') &#123;
          console.log('transform');
        &#125;
        return code
      &#125;,
    &#125;;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">vite.config.ts

import myExample from './plugins/vite-plugin-my-example'  //自定义插件

export default defineConfig(&#123;
  plugins: [vue(),
  myExample()
  ], //插件
&#125;)

//在项目运行时，可以看到插件钩子的执行
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1jb4y1R7UV" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1jb4y1R7UV" ref="nofollow noopener noreferrer">vite插件开发指南视频地址</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.dev/" ref="nofollow noopener noreferrer">vitejs官网地址</a></p></div>  
</div>
            