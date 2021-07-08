
---
title: '前端工程化实战 - 企业级 CLI 开发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3be397cabbf84ff1ada57b73ae30d643~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 08:03:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3be397cabbf84ff1ada57b73ae30d643~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️ 本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>去年同期写过一个基于 Node 的 <a href="https://juejin.cn/column/6960547897611911205" target="_blank" title="https://juejin.cn/column/6960547897611911205">DevOps 系列</a>，但是整个项目工程非常大，上手成本比较高，对于一些<strong>中小型团队或者新手</strong>参考的意义不算多，所以针对这些群体重启了一个新的工程化系列。</p>
<p>新的系列将从 <strong>0 到 1</strong> 逐步搭建一套完整工程化方案，所有文章将统一放在<a href="https://juejin.cn/column/6979802145801388039" target="_blank" title="https://juejin.cn/column/6979802145801388039">《前端工程化》</a>专栏中。</p>
<h3 data-id="heading-1">背景</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3be397cabbf84ff1ada57b73ae30d643~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先罗列一些小团队会大概率会遇到的问题：</p>
<ol>
<li>规范
<ul>
<li>代码没有规范，每个人的风格<strong>随心所欲</strong>，<strong>代码交付质量不可控</strong></li>
<li>提交 commit <strong>没有规范</strong>，无法从 commit 知晓提交开发内容</li>
</ul>
</li>
<li>流程
<ul>
<li>研发没有<strong>流程</strong>，没有 prd，没有迭代的需求管理，这个项目到底做了点啥也不知道</li>
</ul>
</li>
<li>效率
<ul>
<li>不断的<strong>重复工作</strong>，没有<strong>技术积累与沉淀</strong></li>
</ul>
</li>
<li>项目质量
<ul>
<li>项目没有规范就一定没有质量</li>
<li>测试功能全部靠<strong>人工</strong>发现与回归，费时费力</li>
</ul>
</li>
<li>部署
<ul>
<li>人工构建、部署，<strong>刀耕火种</strong>般的操作</li>
<li>依赖不统一、人为不可控</li>
<li>没有版本追踪、回滚等功能</li>
</ul>
</li>
</ol>
<p>除了上述比较常见的几点外，其余的一些人为环境因素就不一一列举了，总结出来其实就是<strong>混乱</strong> + <strong>不舒服</strong>。</p>
<p>同时处在这样的一个团队中，团队自身的规划就不明确，个人就更难对未来有一个清晰的规划与目标，容易全部陷于业务不可自拔、无限循环。</p>
<p>当你处在一个混乱的环境，遇事不要慌（<strong>乱世出英雄，为什么不能是你呢</strong>），先把事情捋顺，然后定个目标与规划，一步步走。</p>
<h3 data-id="heading-2">工程化</h3>
<p>上述列举的这些问题可以通过引入工程化体系来解决，那么什么是工程化呢？</p>
<p>广义上，一切以<strong>提高效率、降低成本、保障质量</strong>为目的的手段，都属于工程化的范畴。</p>
<p>通过一系列的规范、流程、工具达到<strong>研发提效、自动化、保障质量、服务稳定、预警监控</strong>等等。</p>
<p>对前端而言，在 Node 出现之后，可以借助于 Node 渗透到传统界面开发之外的领域，将研发链路延伸到整个 DevOps 中去，从而脱离“切图仔”成为前端工程师。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98c1f92c802545a3a92d9600e2779de1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是一套简单的 DevOps 流程，技术难度与成本都比较适中，作为小型团队搭建工程化的起点，性价比极高。</p>
<p>在团队没有制定规则，也没有基础建设的时候，通常可以先从最基础的 CLI 工具开始然后切入到整个工程化的搭建。</p>
<p><strong>所以先定一个小目标，完成一个团队、项目通用的 CLI 工具。</strong></p>
<h2 data-id="heading-3">CLI 工具分析</h2>
<p>小团队里面的业务一般迭代比较快，能抽出来提供开发基建的时间与机会都比较少，为了避免后期的重复工作，在做基础建设之前，一定要做好规划，思考一下当前最欠缺的核心与未来可能需要用到的功能是什么？</p>
<blockquote>
<p>Coding 永远不是最难的，最难的是不知道能使用 code 去做些什么有价值的事情。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2edf0eab40ba4fd5954e66021eee4921~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>参考上述的 DevOps 流程，本系列先简单规划出 CLI 的四个大模块，后续如果有需求变动再说。</p>
<blockquote>
<p>可以根据自己项目的实际情况去设计 CLI 工具，本系列仅提供一个技术架构参考。</p>
</blockquote>
<h3 data-id="heading-4">构建</h3>
<p>通常在小团队中，构建流程都是在一套或者多套模板里面准备多环境配置文件，再使用 Webpack Or Rollup 之类的构建工具，通过 Shell 脚本或者其他操作去使用模板中预设的配置来构建项目，最后再进行部署之类的。</p>
<p>这的确是一个简单、通用的 CI/CD 流程，但问题来了，只要最后一步的发布配置不在可控之内，任意团队的开发成员都可以对发布的配置项做修改。</p>
<p>即使构建成功，也有可能会有一些不可预见的问题，比如 Webpack 的 mode 选择的是 dev 模式、没有对构建代码压缩混淆、没有注入一些全局统一方法等等，此时对生产环境而言是<strong>存在一定隐患的</strong>。</p>
<p>所以需要将构建配置、过程从项目模板中抽离出来，<strong>统一使用 CLI 来接管</strong>构建流程，不再读取项目中的配置，而通过 CLI 使用统一配置（<code>每一类项目都可以自定义一套标准构建配置</code>）进行构建。</p>
<p>避免出现业务开发同学因为修改了错误配置而导致的生产问题。</p>
<h3 data-id="heading-5">质量</h3>
<p>与构建是一样的场景，业务开发的时候为了方便，很多时候一些通用的自动化测试以及一些常规的格式校验都会被忽略。比如每个人开发的习惯不同也会导致使用的 ESLINT 校验规则不同，会对 ESLINT 的配置做一些额外的修改，这也是不可控的一个点。一个团队还是使用同一套代码校验规则最好。</p>
<p>所以也可以将自动化测试、校验从项目中剥离，使用 CLI 接管，从而保证整个团队的某一类项目代码格式的<strong>统一</strong>性。</p>
<h3 data-id="heading-6">模板</h3>
<p>至于模板，基本上目前出现的博客中，只要是关于 CLI 的，就必然会有模板功能。</p>
<p>因为这个一个对团队来说，快速、便捷初始化一个项目或者拉取代码片段是非常重要的，也是作为 CLI 工具来说产出最高、收益最明显的功能模块，但本章就不做过多的介绍，放在后面模板的博文统一写。</p>
<h3 data-id="heading-7">工具合集</h3>
<p>既然是工具合集，那么可以放一些通用的工具类在里面，比如</p>
<ol>
<li>图片压缩（png 压缩的更小的那种）、上传 CDN 等</li>
<li>项目升级（比如通用配置更新了，CLI 提供一键升级模板的功能）</li>
<li>项目部署、发布 npm 包等操作。</li>
<li>等等其他一些重复性的操作，也都可以放在工具合集里面</li>
</ol>
<h2 data-id="heading-8">CLI 开发</h2>
<p>前面介绍了 CLI 的几个模块功能设计，接下来可以正式进入开发对应的 CLI 工具的环节。</p>
<h3 data-id="heading-9">搭建基础架构</h3>
<p>CLI 工具开发将使用 TS 作为开发语言，如果此时还没有接触过 TS 的同学，刚好可以借此项目来熟悉一下 TS 的开发模式。</p>
<pre><code class="hljs language-js copyable" lang="js">mkdir cli && cd cli <span class="hljs-comment">// 创建仓库目录</span>
npm init <span class="hljs-comment">// 初始化 package.json</span>
npm install -g typescript <span class="hljs-comment">// 安装全局 TypeScript</span>
tsc --init <span class="hljs-comment">// 初始化 tsconfig.json</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局安装完 TypeScript 之后，初始化 tsconfig.json 之后再进行修改配置，添加编译的文件夹与输出目录。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"target"</span>: <span class="hljs-string">"es5"</span>, <span class="hljs-comment">/* Specify ECMAScript target version: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', 'ES2018', 'ES2019', 'ES2020', 'ES2021', or 'ESNEXT'. */</span>
    <span class="hljs-attr">"module"</span>: <span class="hljs-string">"commonjs"</span>, <span class="hljs-comment">/* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', 'es2020', or 'ESNext'. */</span>
    <span class="hljs-attr">"outDir"</span>: <span class="hljs-string">"./lib"</span>, <span class="hljs-comment">/* Redirect output structure to the directory. */</span>
    <span class="hljs-attr">"strict"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">/* Enable all strict type-checking options. */</span>
    <span class="hljs-attr">"esModuleInterop"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">/* Enables emit interoperability between CommonJS and ES Modules via creation of namespace objects for all imports. Implies 'allowSyntheticDefaultImports'. */</span>
    <span class="hljs-attr">"skipLibCheck"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">/* Skip type checking of declaration files. */</span>
    <span class="hljs-attr">"forceConsistentCasingInFileNames"</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">/* Disallow inconsistently-cased references to the same file. */</span>
  &#125;,
  <span class="hljs-attr">"include"</span>: [
    <span class="hljs-string">"./src"</span>,
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述是一份已经简化过的配置，但应对当前的开发已经足够了，后续有需要可以修改 TypeScript 的配置项。</p>
<h3 data-id="heading-10">ESLINT</h3>
<p>因为是从 0 开发 CLI 工具，可以先从简单的功能入手，例如开发一个 Eslint 校验模块。</p>
<pre><code class="hljs language-js copyable" lang="js">npm install eslint --save-dev <span class="hljs-comment">// 安装 eslint 依赖</span>
npx eslint --init <span class="hljs-comment">// 初始化 eslint 配置</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接使用 <code>eslint --init</code> 可以快速定制出适合自己项目的 ESlint 配置文件 <code>.eslintrc.json</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"env"</span>: &#123;
        <span class="hljs-attr">"browser"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">"es2021"</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">"extends"</span>: [
        <span class="hljs-string">"plugin:react/recommended"</span>,
        <span class="hljs-string">"standard"</span>
    ],
    <span class="hljs-attr">"parser"</span>: <span class="hljs-string">"@typescript-eslint/parser"</span>,
    <span class="hljs-attr">"parserOptions"</span>: &#123;
        <span class="hljs-attr">"ecmaFeatures"</span>: &#123;
            <span class="hljs-attr">"jsx"</span>: <span class="hljs-literal">true</span>
        &#125;,
        <span class="hljs-attr">"ecmaVersion"</span>: <span class="hljs-number">12</span>,
        <span class="hljs-attr">"sourceType"</span>: <span class="hljs-string">"module"</span>
    &#125;,
    <span class="hljs-attr">"plugins"</span>: [
        <span class="hljs-string">"react"</span>,
        <span class="hljs-string">"@typescript-eslint"</span>
    ],
    <span class="hljs-attr">"rules"</span>: &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果项目中已经有定义好的 ESlint，可以直接使用自己的配置文件，或者根据项目需求对初始化的配置进行增改。</p>
<h4 data-id="heading-11">创建 ESlint 工具类</h4>
<p>第一步，对照文档 <a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.org%2Fdocs%2Fdeveloper-guide%2Fnodejs-api" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.org/docs/developer-guide/nodejs-api" ref="nofollow noopener noreferrer">ESlint Node.js API</a>，使用提供的 Node Api 直接调用 ESlint。</p>
<p>将前面生成的 .eslintrc.json 的配置项按需加入，同时使用 <code>useEslintrc:fase</code> 禁止使用项目本身的 .eslintrc 配置，仅使用 CLI 提供的规则去校验项目代码。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">import</span> &#123; ESLint &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'eslint'</span>
<span class="hljs-keyword">import</span> &#123; getCwdPath, countTime &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../util'</span>

<span class="hljs-comment">// 1. Create an instance.</span>
<span class="hljs-keyword">const</span> eslint = <span class="hljs-keyword">new</span> ESLint(&#123;
  <span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">extensions</span>: [<span class="hljs-string">".js"</span>, <span class="hljs-string">".ts"</span>],
  <span class="hljs-attr">useEslintrc</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">overrideConfig</span>: &#123;
    <span class="hljs-string">"env"</span>: &#123;
      <span class="hljs-string">"browser"</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-string">"es2021"</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-string">"parser"</span>: getRePath(<span class="hljs-string">"@typescript-eslint/parser"</span>),
    <span class="hljs-string">"parserOptions"</span>: &#123;
      <span class="hljs-string">"ecmaFeatures"</span>: &#123;
        <span class="hljs-string">"jsx"</span>: <span class="hljs-literal">true</span>
      &#125;,
      <span class="hljs-string">"ecmaVersion"</span>: <span class="hljs-number">12</span>,
      <span class="hljs-string">"sourceType"</span>: <span class="hljs-string">"module"</span>
    &#125;,
    <span class="hljs-string">"plugins"</span>: [
      <span class="hljs-string">"react"</span>,
      <span class="hljs-string">"@typescript-eslint"</span>,
    ],
  &#125;,
  <span class="hljs-attr">resolvePluginsRelativeTo</span>: getDirPath(<span class="hljs-string">'../../node_modules'</span>) <span class="hljs-comment">// 指定 loader 加载路径</span>
&#125;);


<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getEslint = <span class="hljs-keyword">async</span> (path: string = <span class="hljs-string">'src'</span>) => &#123;
  <span class="hljs-keyword">try</span> &#123;
    countTime(<span class="hljs-string">'Eslint 校验'</span>);
    <span class="hljs-comment">// 2. Lint files.</span>
    <span class="hljs-keyword">const</span> results = <span class="hljs-keyword">await</span> eslint.lintFiles([<span class="hljs-string">`<span class="hljs-subst">$&#123;getCwdPath()&#125;</span>/<span class="hljs-subst">$&#123;path&#125;</span>`</span>]);

    <span class="hljs-comment">// 3. Modify the files with the fixed code.</span>
    <span class="hljs-keyword">await</span> ESLint.outputFixes(results);

    <span class="hljs-comment">// 4. Format the results.</span>
    <span class="hljs-keyword">const</span> formatter = <span class="hljs-keyword">await</span> eslint.loadFormatter(<span class="hljs-string">"stylish"</span>);

    <span class="hljs-keyword">const</span> resultText = formatter.format(results);

    <span class="hljs-comment">// 5. Output it.</span>
    <span class="hljs-keyword">if</span> (resultText) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请检查===》'</span>, resultText);
    &#125;
    <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'完美！'</span>);
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;

    process.exitCode = <span class="hljs-number">1</span>;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'error===>'</span>, error);
  &#125; <span class="hljs-keyword">finally</span> &#123;
    countTime(<span class="hljs-string">'Eslint 校验'</span>, <span class="hljs-literal">false</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">创建测试项目</h4>
<pre><code class="copyable">npm install -g create-react-app // 全局安装 create-react-app
create-react-app test-cli // 创建测试 react 项目
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试项目使用的是 create-react-app，当然你也可以选择其他框架或者已有项目都行，这里只是作为一个 demo，并且后期也还会再用到这个项目做测试。</p>
<h4 data-id="heading-13">测试 CLI</h4>
<p>新建 <code>src/bin/index.ts</code>, demo 中使用 <code>commander</code> 来开发命令行工具。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-meta">#!/usr/bin/env node // 这个必须添加，指定 node 运行环境</span>
<span class="hljs-keyword">import</span> &#123; Command &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">const</span> program = <span class="hljs-keyword">new</span> Command();

<span class="hljs-keyword">import</span> &#123; getEslint &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../eslint'</span>

program
  .version(<span class="hljs-string">'0.1.0'</span>)
  .description(<span class="hljs-string">'start eslint and fix code'</span>)
  .command(<span class="hljs-string">'eslint'</span>)
  .action(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    getEslint()
  &#125;)
program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 pageage.json，指定 bin 的运行 js（每个命令所对应的可执行文件的位置）</p>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"bin"</span>: &#123;
    <span class="hljs-attr">"fe-cli"</span>: <span class="hljs-string">"/lib/bin/index.js"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先运行 <code>tsc</code> 将 TS 代码编译成 js，再使用 npm link 挂载到全局，即可正常使用。</p>
<blockquote>
<p>commander 的具体用法就不详细介绍了，基本上市面大部分的 CLI 工具都使用 commander 作为命令行工具开发，也都有这方面的介绍。</p>
</blockquote>
<p>命令行进入刚刚的测试项目，直接输入命令 <code>fe-cli eslint</code>，就可以正常使用 Eslint 插件，输出结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0750d38ecb84f5bb26da3662b7b4ae9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">美化输出</h4>
<p>可以看出这个时候，提示并没有那么显眼，可以使用 <code>chalk</code> 插件来美化一下输出。</p>
<p>先将测试工程故意改错一个地方，再运行命令 <code>fe-cli eslint</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd553aa1940c4e5caf0718289fd45133~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此，已经完成了一个简单的 CLI 工具，对于 ESlint 的模块，可以根据自己的想法与规划定制更多的功能。</p>
<h3 data-id="heading-15">构建模块</h3>
<h4 data-id="heading-16">配置通用 Webpack</h4>
<p>通常开发业务的时候，用的是 webpack 作为构建工具，那么 demo 也将使用 webpack 进行封装。</p>
<p>先命令行进入测试项目中执行命令 <code>npm run eject</code>，暴露 webpack 配置项。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44edec529d81462489b63a31800ea6b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图暴露出来的配置项可以看出，CRA 的 webpack 配置还是非常复杂的，毕竟是通用型的脚手架，针对各种优化配置都做了兼容，但目前 CRA 使用的还是 webpack 4 来构建。作为一个新的开发项目，CLI 可以不背技术债务，直接选择 webpack 5 来构建项目。</p>
<blockquote>
<p>一般来说，构建工具替换不会影响业务代码，如果业务代码被构建工具绑架，建议还是需要去优化一下代码了。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">"path"</span>

<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-keyword">const</span> postcssNormalize = <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-normalize'</span>);
<span class="hljs-keyword">import</span> &#123; getCwdPath, getDirPath &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../util'</span>

interface IWebpack &#123;
  mode?: <span class="hljs-string">"development"</span> | <span class="hljs-string">"production"</span> | <span class="hljs-string">"none"</span>;
  entry: any
  <span class="hljs-attr">output</span>: any
  <span class="hljs-attr">template</span>: string
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (&#123;
  mode,
  entry,
  output,
  template
&#125;: IWebpack) => &#123;
  <span class="hljs-keyword">return</span> &#123;
    mode,
    entry,
    <span class="hljs-attr">target</span>: <span class="hljs-string">'web'</span>,
    output,
    <span class="hljs-attr">module</span>: &#123;
      <span class="hljs-attr">rules</span>: [&#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx)$/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: getRePath(<span class="hljs-string">'babel-loader'</span>),
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">presets</span>: [
              <span class="hljs-string">''</span>@babel/preset-env<span class="hljs-string">',
            ],
          &#125;,
        &#125;,
        exclude: [
          getCwdPath('</span>./node_modules<span class="hljs-string">') // 由于 node_modules 都是编译过的文件，这里做过滤处理
        ]
      &#125;,
      &#123;
        test: /\.css$/,
        use: [
          '</span>style-loader<span class="hljs-string">',
          &#123;
            loader: '</span>css-loader<span class="hljs-string">',
            options: &#123;
              importLoaders: 1,
            &#125;,
          &#125;,
          &#123;
            loader: '</span>postcss-loader<span class="hljs-string">',
            options: &#123;
              postcssOptions: &#123;
                plugins: [
                  [
                    '</span>postcss-preset-env<span class="hljs-string">',
                    &#123;
                      ident: "postcss"
                    &#125;,
                  ],
                ],
              &#125;,
            &#125;
          &#125;
        ],
      &#125;,
      &#123;
        test: /\.(woff(2)?|eot|ttf|otf|svg|)$/,
        type: '</span>asset/inline<span class="hljs-string">',
      &#125;,
      &#123;
        test: [/\.bmp$/, /\.gif$/, /\.jpe?g$/, /\.png$/],
        loader: '</span>url-loader<span class="hljs-string">',
        options: &#123;
          limit: 10000,
          name: '</span><span class="hljs-keyword">static</span>/media/[name].[hash:<span class="hljs-number">8</span>].[ext]<span class="hljs-string">',
        &#125;,
      &#125;,
      ]
    &#125;,
    plugins: [
      new HtmlWebpackPlugin(&#123;
        template,
        filename: '</span>index.html<span class="hljs-string">',
      &#125;),
    ],
    resolve: &#123;
      extensions: [
        '</span><span class="hljs-string">',
        '</span>.js<span class="hljs-string">',
        '</span>.json<span class="hljs-string">',
        '</span>.sass<span class="hljs-string">'
      ]
    &#125;,
  &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>上述是一份简化版本的 webpack 5 配置，再添加对应的 commander 命令。</p>
<pre><code class="hljs language-js copyable" lang="js">program
  .version(<span class="hljs-string">'0.1.0'</span>)
  .description(<span class="hljs-string">'start eslint and fix code'</span>)
  .command(<span class="hljs-string">'webpack'</span>)
  .action(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    buildWebpack()
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在可以命令行进入测试工程执行 <code>fe-cli webpack</code> 即可得到下述构建产物</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97ffea55911d4cfa8f364937ec84a35e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbba5486d381410e9639dcd67870702a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下图是使用 CRA 构建出来的产物，跟上图的构建产物对一下，能明显看出使用简化版本的 webpack 5 配置还有很多可优化的地方，那么感兴趣的同学可以再自行优化一下，作为 demo 已经完成初步的技术预研，达到了预期目标。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3439050b0324f1089d17d816fe152bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，如果熟悉构建这块的同学应该会想到，除了 webpack 的配置项外，构建中<strong>绝大部分的依赖都是来自测试工程</strong>里面的，那么如何确定 React 版本或者其他的依赖统一呢？</p>
<p>常规操作还是通过模板来锁定版本，但是业务同学依然可以自行调整版本依赖导致不一致，并不能保证依赖一致性。</p>
<p>既然整个构建都由 CLI 接管，只需要考虑将全部的依赖转移到 CLI 所在的项目依赖即可。</p>
<h4 data-id="heading-17">解决依赖</h4>
<p>Webpack 配置项新增下述两项，指定依赖跟 loader 的加载路径，不从项目所在 node_modules 读取，而是读取 CLI 所在的 node_modules。</p>
<pre><code class="hljs language-js copyable" lang="js">resolveLoader: &#123;
  <span class="hljs-attr">modules</span>: [getDirPath(<span class="hljs-string">'../../node_modules'</span>)]
&#125;, <span class="hljs-comment">// 修改 loader 依赖路径</span>
<span class="hljs-attr">resolve</span>: &#123;
  <span class="hljs-attr">modules</span>: [getDirPath(<span class="hljs-string">'../../node_modules'</span>)],
&#125;, <span class="hljs-comment">// 修改正常模块依赖路径</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时将 babel 的 presets 模块路径修改为绝对路径，指向 CLI 的 node_modules（presets 会默认从启动路劲读取依赖）。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx)$/</span>,
    use: &#123;
      <span class="hljs-attr">loader</span>: getRePath(<span class="hljs-string">'babel-loader'</span>),
      <span class="hljs-attr">options</span>: &#123;
        <span class="hljs-attr">presets</span>: [
          getRePath(<span class="hljs-string">'@babel/preset-env'</span>),
          [
            getRePath(<span class="hljs-string">"@babel/preset-react"</span>),
            &#123;
              <span class="hljs-string">"runtime"</span>: <span class="hljs-string">"automatic"</span>
            &#125;
          ],
        ],
      &#125;,
    &#125;,
    <span class="hljs-attr">exclude</span>: [
      [getDirPath(<span class="hljs-string">'../../node_modules'</span>)]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成依赖修改之后，一起测试一下效果，先将测试工程的依赖 <code>node_modules</code> 全部删除</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db902fcc913b417fa5c030a6dd76d129~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再执行 <code>fe-cli webpack</code>，使用 CLI 依赖来构建此项目。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec8eb0fa8754bf9912a1cb1baa2fd14~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/418d20d0dd7a44189e45ad1b34534722~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，已经可以在项目不安装任何依赖的情况，使用 CLI 也可以正常构建项目了。</p>
<p>那么目前所有项目的依赖、构建已经全部由 CLI 接管，可以统一管理依赖与构建流程，如果需要升级依赖的话可以使用 CLI 统一进行升级，同时业务开发同学也无法对版本依赖进行改动。</p>
<blockquote>
<p>这个解决方案要根据自身的实际需求来实施，所有的依赖都来源于 CLI 工具的话，版本升级影响会非常大也会非常被动，要做好兼容措施。比如哪些依赖可以取自项目，哪些依赖需要强制通用，做好取舍。</p>
</blockquote>
<h2 data-id="heading-18">写给迷茫 Coder 们的一段话</h2>
<p>如果遇到最开始提到那些问题的同学们，应该会经常陷入到业务中无法自拔，而且写这种基础项目，是真的很花时间也很枯燥。容易对工作厌烦，对 coding 感觉无趣。</p>
<p>这是很正常的，绝大多数人都有这段经历与类似的想法，但还是希望你能去多想想，在<strong>枯燥、无味、重复</strong>的工作中去发现痛点、机会。只有接近业务、熟悉业务，才有机会去优化、革新、创造。</p>
<p><strong>所有的基建都是要依托业务才能发挥最大的作用</strong>。</p>
<p>每天抽个半小时思考一下今天的工作还能在哪些方面有所提高，提高效率的不仅仅是你的代码也可以是其他的工具或者是引入新的流程。</p>
<p>同时也不要仅仅限制在思考阶段，有想法就争取落地，再多抽半小时进行 coding 或者找工具什么的，但凡能够提高个几分钟的效率，即使是个小工具、多几行代码、换个流程这种也值得去尝试一下。</p>
<p>等你把这些零碎的小东西、想法一点点全部积累起来，到最后整合到一个体系中去，那么此时你会发现已经可以站在更高一层的台阶去思考、规划下一阶段需要做的事情，而这其中所有的经历都是你未来成长的基石。</p>
<p><strong>一直相信一句话：努力不会被辜负，付出终将有回报。此时敲下去的每一行代码在未来都将是你登高的一步步台阶。</strong></p>
<h2 data-id="heading-19">最后</h2>
<p>本章介绍的 CLI 工具还不够完善，作为工程化的一个起点，后续还需要对 CLI 做更多的功能迭代。</p>
<p>对工程化感兴趣的同学可以关注一下<a href="https://juejin.cn/column/6979802145801388039" target="_blank" title="https://juejin.cn/column/6979802145801388039">《前端工程化》</a>专栏，一起打造一个适合团队的 DevOps 体系。</p></div>  
</div>
            