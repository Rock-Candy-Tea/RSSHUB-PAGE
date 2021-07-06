
---
title: 'Vue 2 系统如何快速迁移 Vite 作为开发工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 17:56:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image" alt="掘金引流终版.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://juejin.cn/post/6963056815420473357#heading-0" target="_blank">构建专栏系列目录入口</a></p>
</blockquote>
<blockquote>
<p>梁晓莹:  微医前端技术部 一只喜欢读书📚&&游泳🏊🏻的猪猪女孩～🤔</p>
</blockquote>
<h3 data-id="heading-0">当前版本 <a href="mailto:vite@2.3.7">vite@2.3.7</a></h3>
<h2 data-id="heading-1">一. 适合什么项目迁移</h2>
<ol>
<li>使用 vue2 的系统</li>
<li>内部系统 - 无需大型流量场景：因为 vite 更迭较快，导致系统需要定期改动基础功能，造成不稳定</li>
<li>非 ssr 系统 - ssr 还有很多问题，暂且等社区丰富起来</li>
<li>定期有人维护的系统</li>
<li>对开发有痛点而想要改进：比如打包慢，冷启动慢，HMR 更新慢。。。。</li>
<li>vite 生产环境用 rollup，但是改造成本大，提效不高，风险大，暂不建议使用。【本人愚见，大佬轻喷】</li>
</ol>
<h2 data-id="heading-2">二.迁移步骤</h2>
<p>将会以内部系统作为案例改造, 开发用 vite，生产依旧保持 webpack。</p>
<ol>
<li>简单了解 vite 特性。有问题优先看<a href="https://cn.vitejs.dev/guide/#index-html-and-project-root" target="_blank" rel="nofollow noopener noreferrer">vite 官网</a>排查是否有更新或解决方案！！</li>
<li>npm i <a href="mailto:vite@2.3.7">vite@2.3.7</a> <a href="mailto:vite-plugin-vue2@1.6.2">vite-plugin-vue2@1.6.2</a> <a href="mailto:vite-plugin-html@2.0.7">vite-plugin-html@2.0.7</a> -D</li>
<li>package.json 添加一个 script -- "vite": "NODE_ENV=development vite"</li>
<li>关键在于配置 vite.config.js【默认叫做这个文件名，你可配置成其他的。。】</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;

<span class="hljs-keyword">import</span> &#123; createVuePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-vue2'</span>;
<span class="hljs-keyword">import</span> &#123; injectHtml, minifyHtml &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-html'</span>;
<span class="hljs-keyword">import</span> &#123; cjs2esmVitePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'cjs2esmodule'</span>
<span class="hljs-keyword">import</span> dotenv <span class="hljs-keyword">from</span> <span class="hljs-string">'dotenv'</span>
<span class="hljs-keyword">const</span> config = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./config'</span>)

<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-comment">// 根据环境变量加载环境变量文件</span>
  <span class="hljs-keyword">const</span> file = dotenv.parse(fs.readFileSync(<span class="hljs-string">`./config/.env.<span class="hljs-subst">$&#123;process.env.NODE_ENV&#125;</span>`</span>), &#123;
    <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>
  &#125;)
  <span class="hljs-built_in">console</span>.log(file)
  <span class="hljs-comment">// 根据获取的 key 给对应的环境变量赋值</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> file) &#123;
    process.env[key] = file[key]
  &#125;
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-built_in">console</span>.error(e)
&#125;
<span class="hljs-keyword">const</span> API_LOCATION = process.env.API_LOCATION || <span class="hljs-string">'/api'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">dir</span>) </span>&#123;
  <span class="hljs-keyword">return</span> path.join(__dirname, <span class="hljs-string">'./'</span>, dir)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">root</span>: <span class="hljs-string">'./'</span>, <span class="hljs-comment">// 项目根目录（index.html 文件所在的位置）可以是一个绝对路径，或者一个相对于该配置文件本身的相对路径。</span>
  <span class="hljs-attr">publicDir</span>: <span class="hljs-string">'public'</span>, <span class="hljs-comment">// 作为静态资源服务的文件夹.该值可以是文件系统的绝对路径，也可以是相对于项目的根目录的相对路径。</span>
  <span class="hljs-attr">base</span>: <span class="hljs-string">'./'</span>, <span class="hljs-comment">// 公共基础路径。改值可以是绝对路径或空字符串</span>
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">optimizeDeps</span>: &#123; <span class="hljs-comment">// 要预构建的第三方依赖</span>
    <span class="hljs-attr">include</span>: []
  &#125;,
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-comment">// 'vue': 'vue/dist/vue.esm.js', // 如果是模板解析的 - 使用这个 vue：内部为正则表达式  vue 结尾的</span>
      <span class="hljs-string">'vendor'</span>: resolve(<span class="hljs-string">'src/vendor'</span>),
      <span class="hljs-string">'@'</span>: resolve(<span class="hljs-string">'src'</span>),
      <span class="hljs-string">'~@'</span>: resolve(<span class="hljs-string">'src'</span>),
      <span class="hljs-string">'~component'</span>: resolve(<span class="hljs-string">'src/components'</span>),
      <span class="hljs-string">'~config'</span>: resolve(<span class="hljs-string">'config'</span>),
    &#125;
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    cjs2esmVitePlugin(), <span class="hljs-comment">// 将 commonjs 转化为 es module： 有报错</span>
    createVuePlugin(&#123;
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">jsxOptions</span>: &#123;
        <span class="hljs-attr">injectH</span>: <span class="hljs-literal">false</span>,
      &#125;,
    &#125;),
    minifyHtml(), <span class="hljs-comment">// 压缩 HTML</span>
    injectHtml(&#123; <span class="hljs-comment">// 入口文件 index.html 的模板注入</span>
      <span class="hljs-attr">injectData</span>: &#123; <span class="hljs-comment">// 模板注入的数据</span>
        <span class="hljs-attr">htmlWebpackPlugin</span>: &#123;
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">isVite</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">shotcut</span>: <span class="hljs-string">'/static/img/favicon.png'</span>,
          &#125;
        &#125;,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'HMO 运营后台'</span>,
      &#125;,
    &#125;),
  ],
  <span class="hljs-attr">define</span>: &#123;
    <span class="hljs-string">'process.env'</span>: process.env
  &#125;,
  <span class="hljs-attr">server</span>: &#123;
    <span class="hljs-attr">host</span>: <span class="hljs-string">'liang.myweb.com'</span>,
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否自动打开浏览器</span>
    <span class="hljs-attr">port</span>: process.env.PORT || config.dev.port,
    <span class="hljs-attr">proxy</span>: &#123;
      [API_LOCATION]: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://127.0.0.1:8001'</span>,
        <span class="hljs-attr">rewrite</span>: <span class="hljs-function">(<span class="hljs-params">path</span>) =></span> path.replace(API_LOCATION, <span class="hljs-string">''</span>)
      &#125;
      
    &#125;
  &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">三.常用问题【踩坑日记😄】</h2>
<h4 data-id="heading-4">1. vite 目前要求入口文件必须是根目录下的 index.html，如果之前的 webpack 入口文件同名，需要更改。</h4>
<p>解决方案：
vite.config.js:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; injectHtml &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-html'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>:[
    injectHtml(&#123; <span class="hljs-comment">// 入口文件 index.html 的模板注入</span>
      <span class="hljs-attr">injectData</span>: &#123; <span class="hljs-comment">// 模板注入的数据</span>
        <span class="hljs-attr">htmlWebpackPlugin</span>: &#123; <span class="hljs-comment">// 取和 webpack 插件同名的对象 key，即可</span>
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">isVite</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">shotcut</span>: <span class="hljs-string">'/static/img/favicon.png'</span>,
          &#125;
        &#125;,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'HMO 运营后台'</span>
      &#125;,
    &#125;)
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack.xxx.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'index.html'</span>,
  <span class="hljs-attr">inject</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">isVite</span>: <span class="hljs-literal">false</span> <span class="hljs-comment">// 添加标识</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根目录入口文件 index.html - ejs 模板</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">      <% <span class="hljs-keyword">if</span> (htmlWebpackPlugin.options.isVite) &#123; %>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/src/main.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
      <%&#125;%>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2. 新版本报 xx 错： 可切换旧版本，如 <a href="mailto:vite@2.2.3">vite@2.2.3</a></h4>
<h4 data-id="heading-6">3.没有导出命名？</h4>
<blockquote>
<p>Uncaught SyntaxError: The requested module '/config/index.js' does not provide an export named 'default'Uncaught SyntaxError: The requested module '/config/index.js' does not provide an export named 'default'</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/245672025f8148cbb62a47737da6ee58~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
错误原因：浏览器仅支持 esm,不支持 cjs
vite.config.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; cjs2esmVitePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'cjs2esmodule'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
  cjs2esmVitePlugin(), <span class="hljs-comment">// 将 commonjs 转化为 es module</span>
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有 require.xx 的按需加载写法还可以修改成 import 的，案例如下：</p>
<pre><code class="hljs language-json copyable" lang="json">const subjectList = r => require.ensure( [], () => r(require('@/pages/xxx/subject/list.vue')), 'subject' );

<span class="hljs-comment">// 改为：Vue 动态组件 component: ()=>import()</span>

const subjectList = () => import(<span class="hljs-comment">/* webpackChunkName: "subject" */</span> '@/pages/xxx/subject/list.vue')
const arr = [
  &#123;
    path: '/subject/list',
    name: 'subject/list',
    component: subjectList
    meta: &#123;...&#125;
  &#125;
];
export default arr;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">4. proxy 使用 <a href="https://github.com/http-party/node-http-proxy" target="_blank" rel="nofollow noopener noreferrer">http-proxy</a>。完整选项详见 <a href="https://github.com/http-party/node-http-proxy#options" target="_blank" rel="nofollow noopener noreferrer">此处</a>.</h4>
<p>案例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">proxy: &#123;
      <span class="hljs-string">'/rest'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://my.web.com/'</span>,
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">bypass</span>: <span class="hljs-function">(<span class="hljs-params">req, res, proxyOption</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`当前请求代理：<span class="hljs-subst">$&#123;req.url&#125;</span> -> <span class="hljs-subst">$&#123;proxyOption.target&#125;</span>`</span>);
        &#125;,
      &#125;,
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">5. ts 文件报错？</h4>
<p>验证是否配置了 vite 的 ts 处理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"compilerOptions"</span>: &#123;
  <span class="hljs-string">"types"</span>: [<span class="hljs-string">"vite/client"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">6. 全局环境变量报错？</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// const isProd = ENV === 'production'; // webpack - dev 环境变量</span>
<span class="hljs-comment">// const isProd = import.meta.env.PROD; // vite - dev 环境变量</span>
<span class="hljs-comment">// 可以避开上面👆🏻的，采用 NODE_ENV 来区分：</span>
<span class="hljs-keyword">const</span> isProd = process.env.NODE_ENV === <span class="hljs-string">'production'</span>;

那么我们启动的时候：<span class="hljs-string">"dev"</span>: <span class="hljs-string">"NODE_ENV=development vite"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者可以探索一下社区的 babel 插件：
<a href="https://www.npmjs.com/package/babel-preset-vite" target="_blank" rel="nofollow noopener noreferrer">babel-preset-vite</a>【包含以下两个功能】
<a href="https://www.npmjs.com/package/babel-plugin-transform-vite-meta-env" target="_blank" rel="nofollow noopener noreferrer">babel-plugin-transform-vite-meta-env</a>
<a href="https://www.npmjs.com/package/babel-plugin-transform-vite-meta-glob" target="_blank" rel="nofollow noopener noreferrer">babel-plugin-transform-vite-meta-glob</a>
​</p>
<h4 data-id="heading-10">7. 看一些打印出来的日志&错误等？</h4>
<p>cli --debug，或者 vite.config.js 配置打印相关参数</p>
<h4 data-id="heading-11">8. 引入文件，比如.vue 的时候，不可以省略扩展名？</h4>
<p>是的！！！不是他们不会做，是他们不想做😭，就是这么设计的，具体请戳<a href="https://github.com/vitejs/vite/issues/178" target="_blank" rel="nofollow noopener noreferrer">这里</a>, <a href="https://twitter.com/youyuxi/status/1288859415878283264" target="_blank" rel="nofollow noopener noreferrer">尤大佬推特解释</a>
然后加上 resolve.extensions: ['.vue'] 直接在控制台报错：所以没用。。。</p>
<blockquote>
<p>error: No loader is configured for ".vue"</p>
</blockquote>
<p>害！老老实实加上扩展名！【在线🐶】
方便的全局加上扩展名方法如下：<a href="https://github.com/nuxt/vite/issues/18" target="_blank" rel="nofollow noopener noreferrer">链接</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17d08ea6609942b58b7a6357517198b0~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">9. less 文件找不到？</h4>
<blockquote>
<p>[vite] Internal server error: '~@/styles/var.less' wasn't found.</p>
</blockquote>
<p>（1）确定已经支持 less：<code> npm install -D less</code>
（2）别忘了 resolve.alias 也加上一个：<code> '~@': resolve('src')</code>
​</p>
<h4 data-id="heading-13">10. 如何支持 jsx?</h4>
<p>vite.config.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createVuePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-vue2'</span>;
createVuePlugin(&#123;
  <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 配置 jsx</span>
  <span class="hljs-attr">jsxOptions</span>: &#123;
    <span class="hljs-attr">injectH</span>: <span class="hljs-literal">false</span>,
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">'my-component'</span>,&#123;
render () &#123;
  <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>my template<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">11. 根据环境变量配置代理？</h4>
<p>（1）cross-env 来跨平台设置环境变量</p>
<blockquote>
<h3 data-id="heading-15">1. 安装 cross-env</h3>
<p>npm i cross-env -D</p>
</blockquote>
<p>（2）加载环境变量文件。它能将环境变量中的变量从 .env 文件加载到 process.env 中</p>
<blockquote>
<h3 data-id="heading-16">2. 安装 dotenv</h3>
<p>npm i dotenv -D</p>
</blockquote>
<p>（3）config/.env.development 配置变量</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">NODE_ENV = development
API_LOCATION = /api
LOGOUT_PC_LOCATION = http:<span class="hljs-comment">//user.myweb.com/login</span>
CRM_ADDRESS = http:<span class="hljs-comment">//crm.myweb.com</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）配置 vite.config.ts</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span> &#123;
  <span class="hljs-comment">// 根据环境变量加载环境变量文件</span>
  <span class="hljs-keyword">const</span> file = dotenv.parse(fs.readFileSync(<span class="hljs-string">`./config/.env.<span class="hljs-subst">$&#123;process.env.NODE_ENV&#125;</span>`</span>), &#123;
    <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>
  &#125;)
  <span class="hljs-built_in">console</span>.log(file)
  <span class="hljs-comment">// 根据获取的 key 给对应的环境变量赋值</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> file) &#123;
    process.env[key] = file[key]
  &#125;
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-built_in">console</span>.error(e)
&#125;
<span class="hljs-keyword">const</span> API_LOCATION = process.env.API_LOCATION || <span class="hljs-string">'/api'</span>
..... 此处省略

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">server</span>: &#123;
    <span class="hljs-attr">proxy</span>: &#123;
      [API_LOCATION]: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://127.0.0.1:8001'</span>,
        <span class="hljs-attr">rewrite</span>: <span class="hljs-function">(<span class="hljs-params">path</span>) =></span> path.replace(API_LOCATION, <span class="hljs-string">''</span>) <span class="hljs-comment">// 根据环境变量配置代理</span>
      &#125;

    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（5）package.json 启动 script</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"vite"</span>: <span class="hljs-string">"cross-env NODE_ENV=development vite"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">12. 环境变量报错？</h4>
<p>原来 webpack 使用的环境变量 process.env，vite 没有这个，所以报错</p>
<blockquote>
<p>Uncaught ReferenceError: process is not defined</p>
</blockquote>
<p>vite 使用的时候<code>import.meta.env</code>, 但是我们老的代码不想动怎么办？
其实 vite 也还是留了口子给我们定义全局变量[类型不能是 function]</p>
<pre><code class="hljs language-json copyable" lang="json">export default defineConfig(&#123;
  <span class="hljs-comment">// ...</span>
  define: &#123;
    'process.env': &#123;&#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">13. anything else?</h4>
<p>..... bug 无止境，很多都是非通用问题，都是引入 vite 后发现的系统本身的一些问题，这里就不一一举例了。后续会追踪更多通用问题</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7969cb6d54b94035b11c58b8e270d62d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            