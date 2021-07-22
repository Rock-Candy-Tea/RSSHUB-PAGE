
---
title: 'vite2 + vue2 + tsx + pinia开发todo-list实战总结分享'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7030'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:23:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=7030'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">概述</h1>
<p>之前搞了<code>vue3+vite2</code>的实战，踩了不少坑，既然<code>vite2</code>也支持<code>vue2</code>并且原生支持ts，想尝试能否将vue2比较平滑过渡到vue3，看看两者之间的差异，尽量采用之前写vue3的方式来写vue2，踩踩坑，前两天给<code>vite-plugin-components </code>提了两个pr支持了vue2的组件库<code>view-ui</code>和<code>element-ui</code>,恰巧看看真实项目中使用会不会有什么问题</p>
<h1 data-id="heading-1">项目搭建</h1>
<h2 data-id="heading-2">vite2支持vue2</h2>
<h3 data-id="heading-3">安装依赖：</h3>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"vite-plugin-vue2"</span>: <span class="hljs-string">"^1.7.2"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">配置vite.config：</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createVuePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite-plugin-vue2"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [createVuePlugin()]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">安装模板编译器</h3>
<p>用于解析vue2文件，版本和vue2对应</p>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"vue-template-compiler"</span>: <span class="hljs-string">"^2.6.14"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">支持jsx/tsx</h2>
<h3 data-id="heading-7">插件支持</h3>
<p>只需要在<code>createVuePlugin</code>的插件中配置一下jsx开启</p>
<pre><code class="hljs language-ts copyable" lang="ts"> createVuePlugin(&#123;
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">使用时声明</h3>
<p><code>.vue</code>文件中使用的时候要声明为<code><script lang="tsx"></code></p>
<h3 data-id="heading-9">添加声明文件</h3>
<p>在src目录下 新建一个<code>shim-tsx.d.ts,</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// file: shim-tsx.d.ts</span>
<span class="hljs-keyword">import</span> Vue, &#123; VNode &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> &#123; ComponentRenderProxy &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/composition-api'</span>;

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">global</span> &#123;
  <span class="hljs-keyword">namespace</span> JSX &#123;
    <span class="hljs-keyword">interface</span> Element <span class="hljs-keyword">extends</span> VNode &#123;&#125;
    <span class="hljs-keyword">interface</span> ElementClass <span class="hljs-keyword">extends</span> ComponentRenderProxy &#123;&#125;
    <span class="hljs-keyword">interface</span> ElementAttributesProperty &#123;
      <span class="hljs-attr">$props</span>: <span class="hljs-built_in">any</span>; <span class="hljs-comment">// specify the property name to use</span>
    &#125;
    <span class="hljs-keyword">interface</span> IntrinsicElements &#123;
      [elem: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">支持ts</h2>
<h3 data-id="heading-11">安装依赖</h3>
<p>安装typescript依赖和vue编译器</p>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"typescript"</span>: <span class="hljs-string">"^4.1.3"</span>,
 <span class="hljs-string">"vue-tsc"</span>: <span class="hljs-string">"^0.1.7"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">文件名替换ts</h3>
<p>更改入口文件js为ts，<code>index.html</code>入口文件为<code>main.ts</code></p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/src/main.ts"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">添加类型声明文件</h3>
<ul>
<li>添加<code>.vue</code>文件<code>ts</code>声明，和<code>main.ts</code>同级目录新建<code>shims-vue.d.ts,</code></li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">"*.vue"</span> &#123;
  <span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
  <span class="hljs-comment">// eslint-disable-next-line prettier/prettier</span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Vue;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">支持vue3特性（引入compositionApi）</h2>
<h3 data-id="heading-15">安装依赖</h3>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"@vue/composition-api"</span>: <span class="hljs-string">"^1.0.3"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">主函数引入并使用</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> VueCompositionAPI <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/composition-api"</span>;
Vue.use(VueCompositionAPI);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">遇到的问题</h3>
<p>这个api需要在最前面引入，因为有的依赖库也使用了compositionApi如果顺序颠倒则会报错</p>
<h3 data-id="heading-18">配置组件库</h3>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"view-design"</span>: <span class="hljs-string">"^4.6.1"</span>,
 <span class="hljs-string">"element-ui"</span>: <span class="hljs-string">"^2.15.3"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">额外依赖</h3>
<p>由于<code>view-ui</code>中有用到<code>commonjs</code>的语法require，vite无法识别，需要安装一个插件解决</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"@originjs/vite-plugin-commonjs"</span>: <span class="hljs-string">"^1.0.0-beta6"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; viteCommonjs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@originjs/vite-plugin-commonjs"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
    <span class="hljs-attr">plugins</span>: [
         viteCommonjs(),
    ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">配置vite</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> ViteComponents, &#123;
  ElementUiResolver,
  ViewUiResolver,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite-plugin-components"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
    <span class="hljs-attr">plugins</span>: [
         ViteComponents(&#123;
               <span class="hljs-attr">dirs</span>: [<span class="hljs-string">"src/views"</span>],<span class="hljs-comment">//扫描自定义组件的路径，可配置为相对路径  ./</span>
               <span class="hljs-attr">customComponentResolvers</span>: [
                   ViewUiResolver(),
                   ElementUiResolver(),
               ]
         &#125;)
    ]
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">设置alias别名</h2>
<h3 data-id="heading-22">配置vite.config</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">"path"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-comment">// 配置别名</span>
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: [
      &#123;
        <span class="hljs-attr">find</span>: <span class="hljs-string">"@"</span>,
        <span class="hljs-attr">replacement</span>: path.resolve(__dirname, <span class="hljs-string">"src"</span>),
      &#125;,
    ],
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">更改tsconfig.json</h3>
<p>配置添加如下两个配置，避免ts文件中引入口提示如下错误</p>
<blockquote>
<p>Cannot find module '@/hooks/useForm' or its corresponding type declarations.Vetur(2307)</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-comment">//...略</span>
    <span class="hljs-attr">"baseUrl"</span>: <span class="hljs-string">"src"</span>,
    <span class="hljs-attr">"paths"</span>: &#123;
      <span class="hljs-attr">"@/*"</span>: [<span class="hljs-string">"./*"</span>]
    &#125;,
  &#125;,
  <span class="hljs-comment">//...略</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">遇到的问题</h3>
<p>开始配置好上述两项依旧不起作用，还是报错，重启vscode才好</p>
<h2 data-id="heading-25">vue-router</h2>
<p>vue2只能使用vue-router3</p>
<ul>
<li>安装依赖</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"vue-router"</span>: <span class="hljs-string">"^3.5.2"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>配置使用</li>
</ul>
<p>和以前使用一样</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
Vue.use(Router);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123;
  <span class="hljs-comment">// mode:'history',</span>
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">()=></span>  <span class="hljs-keyword">import</span>(<span class="hljs-string">"@/views/index.vue"</span>),
    &#125;,
  ],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">使用pinia</h2>
<h3 data-id="heading-27">安装依赖：</h3>
<p>vue2版本只能使用pinia1，官网是这样说的：</p>
<blockquote>
<p><code>pinia@next</code> install Pinia v2 for Vue 3. If your app is using Vue 2, you need to install Pinia v1: <code>pinia@latest</code> <strong>and</strong> <code>@vue/composition-api</code>. If you are using Nuxt, you should follow <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpinia.esm.dev%2Fssr%2Fnuxt.html" target="_blank" rel="nofollow noopener noreferrer" title="https://pinia.esm.dev/ssr/nuxt.html" ref="nofollow noopener noreferrer">these instructions</a>.</p>
</blockquote>
<p>但是我使用了<code>pinia@latest</code>这个让我选择版本，没有找到1.0的版本，应该指的就是0.x的版本吧，如果使用2.x版本就会报错</p>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"pinia"</span>: <span class="hljs-string">"^0.5.2"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">按需加载和引入组件库</h2>
<p>使用<code>vite-plugin-components</code>实现按需加载,在0.13.0这个版本支持了<code>view-ui</code>和<code>element-ui</code>,比较主流的两个组件库</p>
<h3 data-id="heading-29">安装依赖：</h3>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"vite-plugin-components"</span>: <span class="hljs-string">"^0.13.0"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">项目中使用</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//main.ts</span>
<span class="hljs-keyword">import</span> &#123; createPinia, PiniaPlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'pinia'</span>
Vue.use(PiniaPlugin)
<span class="hljs-keyword">const</span> store = createPinia();
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
  router,
  <span class="hljs-attr">pinia</span>:store,<span class="hljs-comment">//使用了插件才会有这个属性</span>
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App),
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">遇到的问题</h3>
<p>之前一般是新建一个store的文件夹然后新建一个index.ts导入后在main.ts中import后使用，但是总是提示没有引入compositionAPi，即使我在main.ts最上面已经引入了，还是报，无奈只能是将pinia也在main中引入了，不多也才一句话</p>
<h1 data-id="heading-32">项目开发中踩到的坑</h1>
<h2 data-id="heading-33">tsx的vetur报错</h2>
<p><strong>描述</strong>： 在view-ui的table使用tsx动态渲染列的时候给一个button设置时候设置了size属性，结果提示报错如下：</p>
<blockquote>
<p>Property 'size' does not exist on type 'ComponentOptions<Vue, DefaultData, DefaultMethods, DefaultComputed, PropsDefinition, DefaultProps>'.Vetur(2769)</p>
</blockquote>
<p>但是运行没有任何的报错，看ts的定义size属性也是定义的非必须属性</p>
<p><strong>解决</strong>： 今天更新了一下vscode发现就不报错了，挺坑的~</p>
<h2 data-id="heading-34">vue2在setup中定义tsx报错</h2>
<p><strong>描述</strong>： 报错信息如下：</p>
<blockquote>
<p>Cannot read property '$createElement' of undefined</p>
</blockquote>
<p><strong>解决</strong>：发现render函数在setup中应该是注入不进来,查看了setup传入参数的定义没有发现render函数的定义，无奈只能写在data函数中，render函数可以成功注入进来</p>
<h2 data-id="heading-35">动态添加的属性不会立即生效</h2>
<p>描述： 这是个老问题，只是vue3中解决了，退回到vue2就忽略了这个，向一个对象中添加一个之前没有的属性，不会响应变化
解决：使用<code>$set</code>添加响应式,  例如: <code>this.$set(item,'editing',!!item.editing)</code></p>
<h2 data-id="heading-36">在hooks中 使用共享数据不具备响应式</h2>
<p><strong>描述</strong>：类似<code>const data =  todoStore.total;</code>这种形式，然后再用data进行computed出其他的变量，此时在vue2中将失去响应式，但是vue3是正常的</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//vue3</span>
  <span class="hljs-keyword">const</span> data: UnwrapRef<DataItem[]> = todoStore.total;
  <span class="hljs-keyword">const</span> unfinish = computed(<span class="hljs-function">() =></span>
    data.filter(<span class="hljs-function">(<span class="hljs-params">item: DataItem</span>) =></span> item.finish != <span class="hljs-literal">true</span>)
  );

  <span class="hljs-keyword">const</span> finishes = computed(<span class="hljs-function">() =></span> data.filter(<span class="hljs-function">(<span class="hljs-params">item: DataItem</span>) =></span> item.finish));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解决</strong>：就是直接使用store的state变量属性进行computed</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//vue2</span>
  <span class="hljs-keyword">const</span> unfinish = computed(<span class="hljs-function">() =></span>
  todoStore.total.filter(<span class="hljs-function">(<span class="hljs-params">item: DataItem</span>) =></span> item.finish != <span class="hljs-literal">true</span>)
  );
  <span class="hljs-keyword">const</span> finishes = computed(<span class="hljs-function">() =></span>  todoStore.total.filter(<span class="hljs-function">(<span class="hljs-params">item: DataItem</span>) =></span> item.finish));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">pinia删除数据不触发拦截器</h2>
<p><strong>描述</strong>： 使用vue3的时候使用如下方式即可删除数组数据并且进入拦截器，但是在vue2的时候失效了</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//vue3</span>
  <span class="hljs-keyword">const</span> clearAll = <span class="hljs-function">() =></span> &#123;
    todoStore.$state.total.length = <span class="hljs-number">0</span>; <span class="hljs-comment">// 如果使用$reset  不触发拦截器</span>
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解决</strong>：经过测试发现只有调用splice才会触发pinia的拦截器
测试结果如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//vue2</span>
  <span class="hljs-keyword">const</span> clearAll = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// todoStore.$state.total=[]//可清空store 不走拦截器</span>
    <span class="hljs-comment">// todoStore.$state.total.length = 0//没有作用</span>
    <span class="hljs-comment">// Vue.set(todoStore.$state.total,'length',0)//没有作用</span>
    todoStore.$state.total.splice(<span class="hljs-number">0</span>,todoStore.$state.total.length)<span class="hljs-comment">//只能通过这种方式，触发全部删除，重置length为0 不管用</span>
  
  &#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-38">参考文档</h1>
<p><a href="https://juejin.cn/post/6973928601523585055" target="_blank" title="https://juejin.cn/post/6973928601523585055">vue2环境下成功使用vite的实践总结！！</a></p>
<h1 data-id="heading-39">代码地址</h1>
<p>主项目 github: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnabaonan%2Ftodos-action" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nabaonan/todos-action" ref="nofollow noopener noreferrer">github.com/nabaonan/to…</a></p>
<p>vue2项目目录是：vue2-vite-ts</p>
<p>欢迎star~</p>
<h1 data-id="heading-40">结语</h1>
<p>总的来说，vue2的ts版本如果配合<code>compositionApi</code>和<code>vue3</code>基本很接近了，<code>vue2</code>的<code>element</code>版本就是直接把vue3的代码粘贴过来，改动很少，由于使用了<code>hooks</code>的方式，所以逻辑基本不用动，然后页面的话，element-plus和element-ui也都是一个东西，页面都能复用，只是有个小bug是<code>popconfirm</code>中没有引入<code>popover</code>的样式，这个在<code>element-plus</code>中已经解决，<code>element-ui</code>没人管了，只能自己引入一下样式解决，其他都还好。
之前听说vue2.7应该会内置<code>compositionApi</code>，那样的话，vue3的代码直接复制过来连改都不用改了，但是<code>vue2</code>的<code>compositionApi</code>也有一些不被支持的功能，比如<code>emit</code>函数就不支持，需要从外部将emit传入到<code>hooks</code>函数中。</p>
<p>最近发现一个大佬在vue2里提了一个将vue2重构为ts的巨型pr，实在佩服这种十倍工程师的大佬，希望能早日并入，没准那时<code>template</code>的ts语法提示能更进一步了~</p></div>  
</div>
            