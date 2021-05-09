
---
title: 'Vue 3.x + Typescript + Vite 踩坑指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1675'
author: 掘金
comments: false
date: Sat, 08 May 2021 01:39:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=1675'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在迁移开源项目 <a href="https://github.com/Hansen-hjs/vue-admin/tree/next" target="_blank" rel="nofollow noopener noreferrer">vue-admin</a> 到最新技术上的时候，遇到了一些技术隐形的问题，毕竟是最新的技术点，难免有些疑难杂症，所以分享给有需要的朋友</p>
<p><a href="https://huangjingsheng.gitee.io/hjs/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">预览效果</a></p>
<h1 data-id="heading-0">Vite 与 webpack 使用注意点</h1>
<p><strong>node.js 文件系统</strong></p>
<p>以往在<code>webpack</code>环境中，是可以在任意地方使用<code>import path from "path"</code>或者<code>import fs from "fs"</code>来做一些文件处理的。现在<code>Vite</code>环境有些特殊的区分，就是在浏览器运行的文件，包括任何<code>.js</code>、<code>.vue</code>或者<code>.ts</code>，是不能正常使用<code>import path from "path"</code>或者<code>import fs from "fs"</code>等一些<code>node.js</code>模块的，必需要改用<code>Vite</code>环境特有的<code>import.meta.globEager</code>和<code>import.meta.glob</code>作为文件处理<code>api</code>使用。举个例子，当前项目需要读取<code>src/icons/svg/</code>目录下的所有<code>svg</code>名称，那么就要这样写：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item of svgIcons"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">svg-icon</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"item"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">const</span> svgFileReg = <span class="hljs-regexp">/(?<=(svg\/)).*?(?=(.svg))/</span>;

<span class="hljs-comment">/** 获取所有`svg`名称 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSvgNames</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> svgInfo = <span class="hljs-keyword">import</span>.meta.globEager(<span class="hljs-string">"../../icons/svg/*.svg"</span>);
    <span class="hljs-keyword">const</span> svgs = <span class="hljs-built_in">Object</span>.keys(svgInfo);
    <span class="hljs-keyword">const</span> names = svgs.map(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">const</span> res = value.match(svgFileReg)![<span class="hljs-number">0</span>];
        <span class="hljs-keyword">return</span> res;
    &#125;);
    <span class="hljs-keyword">return</span> names;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Icons"</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;

        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">svgIcons</span>: getSvgNames()
        &#125;
    &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说完浏览器运行文件，还有一个就是在<code>vite.config.ts</code>文件中，<code>import.meta.globEager</code>和<code>import.meta.glob</code>这个两个<code>api</code>就用不了了，只能用<code>node.js</code>的文件系统模块，也就是上说的那些<code>import fs from fs</code>。同样是当前项目的<code>svg</code>组件，这里要单独写一个<code>svg</code>的加载插件（vite插件），那么要像这样：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; readFileSync, readdirSync &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"fs"</span>;

<span class="hljs-comment">// svg-sprite-loader 这个貌似在 vite 中用不了</span>
<span class="hljs-comment">// 该文件只能作为`vite.config.ts`导入使用</span>
<span class="hljs-comment">// 其他地方导入会报错，因为浏览器环境不支持`fs`模块</span>

<span class="hljs-comment">/** `id`前缀 */</span>
<span class="hljs-keyword">let</span> idPerfix = <span class="hljs-string">""</span>;

<span class="hljs-keyword">const</span> svgTitle = <span class="hljs-regexp">/<svg([^>+].*?)>/</span>;

<span class="hljs-keyword">const</span> clearHeightWidth = <span class="hljs-regexp">/(width|height)="([^>+].*?)"/g</span>;

<span class="hljs-keyword">const</span> hasViewBox = <span class="hljs-regexp">/(viewBox="[^>+].*?")/g</span>;

<span class="hljs-keyword">const</span> clearReturn = <span class="hljs-regexp">/(\r)|(\n)/g</span>;

<span class="hljs-comment">/**
 * 查找`svg`文件
 * <span class="hljs-doctag">@param </span>dir 文件目录
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findSvgFile</span>(<span class="hljs-params">dir: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">Array</span><<span class="hljs-title">string</span>> </span>&#123;
    <span class="hljs-keyword">const</span> svgRes = []
    <span class="hljs-keyword">const</span> dirents = readdirSync(dir, &#123;
        <span class="hljs-attr">withFileTypes</span>: <span class="hljs-literal">true</span>
    &#125;)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> dirent <span class="hljs-keyword">of</span> dirents) &#123;
        <span class="hljs-keyword">if</span> (dirent.isDirectory()) &#123;
            svgRes.push(...findSvgFile(dir + dirent.name + <span class="hljs-string">"/"</span>));
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">const</span> svg = readFileSync(dir + dirent.name).toString().replace(clearReturn, <span class="hljs-string">""</span>).replace(svgTitle, <span class="hljs-function">(<span class="hljs-params">value, group</span>) =></span> &#123;
                <span class="hljs-comment">// console.log(++i)</span>
                <span class="hljs-comment">// console.log(dirent.name)</span>
                <span class="hljs-keyword">let</span> width = <span class="hljs-number">0</span>;
                <span class="hljs-keyword">let</span> height = <span class="hljs-number">0</span>;
                <span class="hljs-keyword">let</span> content = group.replace(clearHeightWidth, <span class="hljs-function">(<span class="hljs-params">val1: <span class="hljs-built_in">string</span>, val2: <span class="hljs-built_in">string</span>, val3: <span class="hljs-built_in">number</span></span>) =></span> &#123;
                        <span class="hljs-keyword">if</span> (val2 === <span class="hljs-string">"width"</span>) &#123;
                            width = val3;
                        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (val2 === <span class="hljs-string">"height"</span>) &#123;
                            height = val3;
                        &#125;
                        <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>;
                    &#125;
                )
                <span class="hljs-keyword">if</span> (!hasViewBox.test(group)) &#123;
                    content += <span class="hljs-string">`viewBox="0 0 <span class="hljs-subst">$&#123;width&#125;</span> <span class="hljs-subst">$&#123;height&#125;</span>"`</span>;
                &#125;
                <span class="hljs-keyword">return</span> <span class="hljs-string">`<symbol id="<span class="hljs-subst">$&#123;idPerfix&#125;</span>-<span class="hljs-subst">$&#123;dirent.name.replace(<span class="hljs-string">".svg"</span>, <span class="hljs-string">""</span>)&#125;</span>" <span class="hljs-subst">$&#123;content&#125;</span>>`</span>;
            &#125;).replace(<span class="hljs-string">"</svg>"</span>, <span class="hljs-string">"</symbol>"</span>);
            svgRes.push(svg);
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> svgRes;
&#125;

<span class="hljs-comment">/**
 * `svg`打包器
 * <span class="hljs-doctag">@param </span>path 资源路径
 * <span class="hljs-doctag">@param </span>perfix 后缀名（标签`id`前缀）
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">svgBuilder</span>(<span class="hljs-params">path: <span class="hljs-built_in">string</span>, perfix = <span class="hljs-string">"icon"</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (path.trim() === <span class="hljs-string">""</span>) <span class="hljs-keyword">return</span>;
    idPerfix = perfix;
    <span class="hljs-keyword">const</span> res = findSvgFile(path);
    <span class="hljs-comment">// console.log(res.length)</span>
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"svg-transform"</span>,
        <span class="hljs-function"><span class="hljs-title">transformIndexHtml</span>(<span class="hljs-params">html: <span class="hljs-built_in">string</span></span>)</span> &#123;
            <span class="hljs-keyword">return</span> html.replace(<span class="hljs-string">"<body>"</span>,
                <span class="hljs-string">`<body>
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="position: absolute; width: 0; height: 0">
                <span class="hljs-subst">$&#123;res.join(<span class="hljs-string">""</span>)&#125;</span>
                </svg>`</span>)
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后在<code>vite.config.ts</code>文件中使用：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite"</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">"@vitejs/plugin-vue"</span>
<span class="hljs-keyword">import</span> vueJsx <span class="hljs-keyword">from</span> <span class="hljs-string">"@vitejs/plugin-vue-jsx"</span>;
<span class="hljs-keyword">import</span> &#123; svgBuilder &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./src/icons/loader"</span>; <span class="hljs-comment">// 这里是上面写的`svg`加载插件</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
    <span class="hljs-attr">plugins</span>: [vue(), vueJsx(), svgBuilder(<span class="hljs-string">"./src/icons/svg/"</span>)],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>npm run build 报错</strong></p>
<p>这个问题比较诡异，<code>npm run dev</code>连警告都没有，<code>npm run build</code>打包居然报错了，后面摸索了一下，原来在<code>tsconfig.json</code>中，需要在<code>include</code>的所有路径前面加个<code>/</code>，我佛，<code>webpack</code>环境表示没有出现过这类问题。像这样：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    ...more,
    <span class="hljs-comment">// 这里所有的路径前面都要加上 / 猜测应该是 vite 在处理文件的时候，用的是严格路径校验</span>
    <span class="hljs-attr">"include"</span>: [<span class="hljs-string">"/src/**/*.ts"</span>, <span class="hljs-string">"/src/**/*.d.ts"</span>, <span class="hljs-string">"/src/**/*.tsx"</span>, <span class="hljs-string">"/src/**/*.vue"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是呢，在所有路径前面加上<code>/</code>之后又导致在开发中无法正常配置<code>ts</code>的一些类型检测，所以又得把前面的<code>/</code>给手动删掉，等<code>npm run build</code>的时候再加上去，不知道这是不是<code>vite</code>的一个<code>bug</code>，已经向作者提问了...</p>
<h1 data-id="heading-1">vue-router</h1>
<p><code>vue-router 4.x</code>之后剔除了路由路径匹配，什么意思呢？看个代码片段</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHashHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;

<span class="hljs-keyword">const</span> base = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"https://github.com/Hansen-hjs/vue-admin"</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">"baidu"</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../views/404.vue"</span>), <span class="hljs-comment">// 这里一定要给个组件（虽然不会显示），不然会卡死</span>
        <span class="hljs-attr">meta</span>: &#123;
            <span class="hljs-attr">icon</span>: <span class="hljs-string">"star"</span>,
            <span class="hljs-attr">title</span>: <span class="hljs-string">"跳转外部链接"</span>
        &#125;
    &#125;
]

<span class="hljs-keyword">const</span> router = createRouter(&#123;
    <span class="hljs-attr">history</span>: createWebHashHistory(),
    <span class="hljs-attr">routes</span>: base
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候会警告并卡死，因为现在不能匹配<code>path</code>为非<code>/</code>开头的路径了，这时候需要在外链前面加个<code>/</code>即可，然后对应的获取路由的时候做对应的的处理即可，像这样：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> base = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/https://github.com/Hansen-hjs/vue-admin"</span>,
        ...more
    &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时<code>vue-router 4.x</code>加入以往没有的新<code>api</code>：<code>removeRoute</code>现在可以轻松的做退出登陆删除之前动态拼接的路由了，不过这个<code>api</code>是以路由定义中<code>name</code>作为删除唯一键值的，所以我们在定义路由的时候最好写上，且唯一，删除路由操作可以看代码片段</p>
<p><a href="https://github.com/Hansen-hjs/vue-admin/blob/next/src/router/permission.ts" target="_blank" rel="nofollow noopener noreferrer">removeRoutes 方法</a></p>
<p>因为改用了<code>Composition API</code>，所以路由的使用方式变了，不过需要注意的是：<code>useRoute</code>和<code>useRouter</code>这两个<code>hooks</code>函数必选要写在顶层，如果是写在代码运行之后的函数中，是获取不到的，看下面代码：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; useRouter, useRoute &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> route = useRoute();
        <span class="hljs-keyword">const</span> router = useRouter();
        
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRouterInfo</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-comment">// const route = useRoute();    // 如果写在这里，是获取不到对象的</span>
            <span class="hljs-comment">// const router = useRouter();  // 如果写在这里，是获取不到对象的</span>

            <span class="hljs-built_in">console</span>.log(route, router);
            
        &#125;
        <span class="hljs-keyword">return</span> &#123;
            getRouterInfo
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">scss 变量无法在 js 或 ts 中使用</h1>
<p>之前在<code>webpack</code>中，<code>.scss</code>文件中导出的变量，是可以在对应的文件中作为<code>js</code>模块导入使用，现在换成<code>vite</code>之后就不行了，即使装了<code>sass-loader</code>，来看下之前能正确使用的代码片段：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-variable">$--color-primary</span>: <span class="hljs-number">#1890FF</span>;

<span class="hljs-comment">// The :export directive is the magic sauce for webpack</span>
<span class="hljs-comment">// https://mattferderer.com/use-sass-variables-in-typescript-and-javascript</span>
:export &#123;
    theme: <span class="hljs-variable">$--color-primary</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他非<code>.scss</code>文件导入使用</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> elementVariables <span class="hljs-keyword">from</span> <span class="hljs-string">"../styles/element-variables.scss"</span>;

<span class="hljs-built_in">console</span>.log(elementVariables) <span class="hljs-comment">// 输出 &#123; theme: "#1890FF" &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详细翻了 <a href="https://www.vitejs.net/guide/features.html#css-modules" target="_blank" rel="nofollow noopener noreferrer">vite文档</a> 也是没有找到相关的配置，所以暂时用不了该功能。</p>
<h1 data-id="heading-3">打包后依然是使用最新的ES模块</h1>
<p>最后需要注意的是，我们在开发环境使用的原生<code>ES模块</code>并不会因为打包后转成以往的兼容模式，意思就是只能用服务器形式来打开，并且不支持<code>IE</code>（好像是废话），仔细看下构建后的<code>index.html</code>引用的<code>js</code>标签就明白了，如果追求兼容、稳定，建议还是用<code>vue 2.x</code>+<code>vue-cli</code>...</p></div>  
</div>
            