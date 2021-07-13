
---
title: 'webpack打包Vue后生成一个可修改的配置文件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76b50f1b59543c49ac69b3167f73561~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 02:50:19 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76b50f1b59543c49ac69b3167f73561~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">问题背景</h2>
<p>工作中两个场景都需要将stg和prod环境的前端代码中不同的接口url 以及各种外部引用的url等提取到静态变量中，并且更改静态变量的配置url就可以改变网站的访问接口</p>
<p>场景一：做docker自动部署平台的时候，当服务器的地址发生变化，后端接口迁移了，然后前端需要在平台上可以自动部署而不是手动部署的时候，就需要有一个配置文件可以在线上编辑更改。</p>
<p>场景二：前端是用工程化生成的，但是整体没有前后端分离部署。后端通过自动化部署的时候需要经过 获取代码---普通编译---stg部署----prd部署 步骤，后端部署stg的时候用的是前端生成的stg代码。prod的时候是prod的代码，为了在上平台上部署，需要后端编写shell脚本，区分stg和prod环境，然后将前端不同的包在不同的阶段放到服务器的根目录下。因为是整个项目的静态资源包，可能比较大，需要先zip压缩然后再解压。后端就提出，可不可以只是把不同的环境的不同的部分提取出来，然后只是移动这一个文件，就可以大大提升部署速度。</p>
<h2 data-id="heading-1">解决方案</h2>
<p>综上：寻找出两种方法来解决</p>
<ol>
<li>方法一：前端将不同环境的配置放到一个config.js中，然后通过用户访问的不同的url来区分是线上还是测试环境。每次服务器发生变化，只需要改变这个配置文件区分不同环境访问的url</li>
</ol>
<ul>
<li>首先在vue-cli静态文件夹 vuecli2是static文件下  vueCli3是public文件夹下新建config.js配置文件，包括不同环境的key对应的不同的接口地址等</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在public目录下新建一个config.js文件</span>
<span class="hljs-keyword">export</span> consst config=[
  <span class="hljs-comment">// 接口地址</span>
  targetAddress: &#123;
    <span class="hljs-attr">local</span>:<span class="hljs-string">"http://xxx.xxx.local.com"</span>,
    <span class="hljs-attr">stg</span>: <span class="hljs-string">"http://xxx.xxx.stg.com"</span>,
    <span class="hljs-attr">prod</span>:<span class="hljs-string">'http://xxx.xxx.prod.com'</span>,
  &#125;,
  <span class="hljs-attr">urlMap</span>: &#123;
<span class="hljs-attr">local</span>: [<span class="hljs-string">'10.118.120.41:8080'</span>,<span class="hljs-string">'localhost:8080'</span>, <span class="hljs-string">'10.118.120.43:8089'</span>],
<span class="hljs-attr">stg</span>: [<span class="hljs-string">'XXX.XXX.stg.com'</span>],
<span class="hljs-attr">prod</span>: [<span class="hljs-string">'XXX.XX.prod.com'</span>],
<span class="hljs-attr">cas</span>: &#123;
      <span class="hljs-attr">local</span>:<span class="hljs-string">"http://XXX.XXX.local/cas/#/"</span>,
      <span class="hljs-attr">stg</span>: <span class="hljs-string">"http://XXX.XXX.stg/cas/#/"</span>,
      <span class="hljs-attr">prod</span>:<span class="hljs-string">'http://XXX.XXX.prod/cas/#/'</span>,
&#125;
  &#125;,
  <span class="hljs-attr">developerUrl</span>: &#123;
    <span class="hljs-attr">local</span>:<span class="hljs-string">"http://XXX.XXX.local/subiectallmanage/"</span>,
    <span class="hljs-attr">stg</span>: <span class="hljs-string">"http://XXX.XXX.stg/subiectallmanage"</span>,
    <span class="hljs-attr">prod</span>:<span class="hljs-string">'http://XXX.XXX.prod/subiectallmanage'</span>, 
  &#125;
 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后在项目的api接口文件中引入config配置文件，并且根据用户输入的地址判断是哪一个环境（是local还是stg还是prod）,然后根据环境取出对应config中的url地址即可</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 在接口文件中 api/api.js下面写上如下代码</span>
 <span class="hljs-keyword">import</span> &#123; config &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../public/js/config.js'</span>
 <span class="hljs-keyword">let</span> targetUrl = <span class="hljs-string">''</span>; <span class="hljs-comment">// 后端接口Url</span>
 <span class="hljs-keyword">const</span> curUrl = <span class="hljs-built_in">window</span>.location.href; <span class="hljs-comment">// 用户输入的url</span>
 <span class="hljs-keyword">const</span> map = config.urlMap;
 <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> env <span class="hljs-keyword">in</span> map) &#123;
<span class="hljs-keyword">if</span> ( env != <span class="hljs-string">'cas'</span>) &#123;
<span class="hljs-keyword">let</span> hasUrl = map[env].some(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
<span class="hljs-keyword">return</span> curUrl.includes(e);
&#125;)
<span class="hljs-keyword">if</span> (hasUrl) &#123; targetUrl = config.targetAddress[env]; &#125;
&#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>方法二：利用插件generate-asset-webpack-plugin在打包的时候生成json文件，然后通过axios请求获取json中的配置。因为后端可以区分是生产还是测试环境，所以只需要有一个默认的json文件和一个生产的json 测试的json。然后后端通过shell脚本判断当前环境替换生产json到默认json目录下面。</li>
</ol>
<ul>
<li>安装插件 generate-asset-webpack-plugin</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">npm i generate-asset-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>vue.config.js中添加插件,使用插件生成json文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> GenerateAssetPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'generate-asset-webpack-plugin'</span>);
<span class="hljs-keyword">var</span> createServerConfig = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">compilation</span>) </span>&#123;
    <span class="hljs-comment">// 配置需要的api接口</span>
    <span class="hljs-keyword">let</span> cfgJson = &#123;
        <span class="hljs-attr">VUE_APP_SERVE_URL</span>: process.env.VUE_APP_PULIC_PATH,
        <span class="hljs-attr">VUE_APP_PULIC_ACTIVE</span>: process.env.VUE_APP_PULIC_ACTIVE
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.stringify(cfgJson);
&#125;
    <span class="hljs-built_in">module</span>.exports = &#123;
        <span class="hljs-attr">configureWebpack</span>: &#123;
            <span class="hljs-attr">plugins</span>: [
                <span class="hljs-keyword">new</span> GenerateAssetPlugin(&#123;
                    <span class="hljs-comment">// 不同的环境生成不同的json文件 stgConfig.json prdConfig.json</span>
                    <span class="hljs-attr">filename</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;process.env.VUE_APP_STATUS&#125;</span>Config.json`</span>,
                    <span class="hljs-attr">fn</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">compilation, cb</span>) </span>&#123;
                        cb(<span class="hljs-literal">null</span>, createConfig(compilation))
                    &#125;
                &#125;)
            ]
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>配置完成后，运行npm run test打测试包，生成stgConfig.json文件在测试目录下,如下图</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76b50f1b59543c49ac69b3167f73561~tplv-k3u1fbpfcp-watermark.image" alt="0001.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>然后将生成的stgConfig.json改名为serverconfig.json复制一份到public下面，在src目录下面新建一个getConfigUrl.js文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
Vue.prototype.getConfigJson = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        axios.get(<span class="hljs-string">"serverconfig.json"</span>).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
            <span class="hljs-comment">//挂载到vue原型上面，这样就可以在项目中调用了</span>
            Vue.prototype.$configApiUrl = result.data;
            <span class="hljs-built_in">console</span>.log(result.data);
        &#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'getConfigJson Error!'</span>, error)
        &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>最后将项目中用到</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">process.env.VUE_APP_SERVE_URL替换成 <span class="hljs-built_in">this</span>.$configApiUrl.VUE_APP_SERVE_URL 
process.env.VUE_APP_PULIC_ACTIVE替换<span class="hljs-built_in">this</span>.$configApiUrl.VUE_APP_PULIC_ACTIVE
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行npm run build打包生成prdConfig.json将两个配置文件都给到后端即可。</p></div>  
</div>
            