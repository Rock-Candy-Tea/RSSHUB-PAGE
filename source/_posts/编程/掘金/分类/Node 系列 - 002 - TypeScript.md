
---
title: 'Node 系列 - 002 - TypeScript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad50caf8259349b096b603a3954fd201~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 01:20:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad50caf8259349b096b603a3954fd201~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>Create by <strong>jsliang</strong> on <strong>2021-05-12 11:00:03</strong><br>
Recently revised in <strong>2021-06-12 16:58:04</strong></p>
</blockquote>
<p>——————————☆☆☆——————————</p>
<p>Node 系列相应地址：</p>
<ul>
<li>代码仓库：<a href="https://github.com/LiangJunrong/all-for-one" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a></li>
<li>文章仓库：<a href="https://github.com/LiangJunrong/document-library/tree/master/%E7%B3%BB%E5%88%97-%E5%89%8D%E7%AB%AF%E8%B5%84%E6%96%99/Node" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a></li>
</ul>
<p>——————————☆☆☆——————————</p>
<p>TypeScript 是 JavaScript 的超集，为语言增加了新的功能（下面简称 TS）。</p>
<p><strong>jsliang</strong> 羡慕 TypeScript 很久了，一直没有自己去搭建过，都是用别人搭建好的，恰好这次要尝试，那就折腾个痛快。</p>
<p>这篇文章通过配置 <code>Node.js</code> 集成 TS，来快速讲解 TS 的使用。</p>

<h2 data-id="heading-0"><a name="user-content-chapter-one" id="user-content-chapter-one" href="https://juejin.cn/post/undefined"></a>一 目录</h2>
<p><strong>不折腾的前端，和咸鱼有什么区别</strong></p>












































<table><thead><tr><th>目录</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/post/6972834535167754270#chapter-one">一 目录</a></td></tr><tr><td><a name="user-content-catalog-chapter-two" id="user-content-catalog-chapter-two" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6972834535167754270#chapter-two">二 Node.js 快速集成 TS</a></td></tr><tr><td> <a href="https://juejin.cn/post/6972834535167754270#chapter-two-one">2.1 目录结构</a></td></tr><tr><td> <a href="https://juejin.cn/post/6972834535167754270#chapter-two-two">2.2 初始化步骤</a></td></tr><tr><td><a name="user-content-catalog-chapter-three" id="user-content-catalog-chapter-three" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6972834535167754270#chapter-three">三 tsconfig.json 讲解</a></td></tr><tr><td> <a href="https://juejin.cn/post/6972834535167754270#chapter-three-one">3.1 compilerOptions 可配置项</a></td></tr><tr><td> <a href="https://juejin.cn/post/6972834535167754270#chapter-three-two">3.2 files 可配置项</a></td></tr><tr><td> <a href="https://juejin.cn/post/6972834535167754270#chapter-three-three">3.3 include 和 exclude 可配置项</a></td></tr><tr><td><a name="user-content-catalog-chapter-four" id="user-content-catalog-chapter-four" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6972834535167754270#chapter-four">四 ESLint</a></td></tr><tr><td><a name="user-content-catalog-chapter-five" id="user-content-catalog-chapter-five" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6972834535167754270#chapter-five">五 总结</a></td></tr><tr><td><a name="user-content-catalog-chapter-six" id="user-content-catalog-chapter-six" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6972834535167754270#chapter-six">六 参考文献</a></td></tr><tr><td></td></tr></tbody></table>
<h2 data-id="heading-1"><a name="user-content-chapter-two" id="user-content-chapter-two" href="https://juejin.cn/post/undefined"></a>二 Node.js 快速集成 TS</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<h3 data-id="heading-2"><a name="user-content-chapter-two-one" id="user-content-chapter-two-one" href="https://juejin.cn/post/undefined"></a>2.1 目录结构</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<p>在这之前，我们先明白即将构建的目录：</p>
<pre><code class="copyable">util
 - src
  - index.ts
 - tsconfig.json
 - package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>util 就是仓库名称（文件夹名称），可以随意换个其他文件夹</p>
</blockquote>
<blockquote>
<p>除了 <code>index.ts</code> 是人工添加的，其他文件均有命令行生成，可以不理会</p>
</blockquote>
<p>那么，Here We go~</p>
<h3 data-id="heading-3"><a name="user-content-chapter-two-two" id="user-content-chapter-two-two" href="https://juejin.cn/post/undefined"></a>2.2 初始化步骤</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<p><strong>首先</strong>，初始化 <code>package.json</code>：</p>
<ul>
<li><code>npm init --yes</code></li>
</ul>
<blockquote>
<p>如果仓库名为中文名，需要 <code>npm init</code> 逐项填写</p>
</blockquote>
<p><strong>然后</strong>，如果在 <code>index.ts</code> 中，编写了以下代码：</p>
<blockquote>
<p>index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-built_in">console</span>.log(path);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时执行 <code>node src/index.ts</code>，会看到报错：</p>
<pre><code class="copyable">internal/modules/cjs/loader.js:883
  throw err;
  ^

Error: Cannot find module 'F:\jsliang\index.ts'
    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:880:15)
    at Function.Module._load (internal/modules/cjs/loader.js:725:27)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:72:12)   
    at internal/main/run_main_module.js:17:47 &#123;
  code: 'MODULE_NOT_FOUND',
  requireStack: []
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>也有可能不报错！</p>
</blockquote>
<p>如果你使用的是 VS Code 开发软件，会看到提示：</p>
<pre><code class="copyable">找不到名称 "require"。是否需要为节点安装类型定义? 请尝试使用 `npm i --save-dev @types/node`。ts(2580)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意思就是 <code>path</code> 和 <code>require</code> 模块都是 Node.js 的东西，使用它需要安装 Node.js 的声明文件，即安装 <code>@types/node</code> 这个包。</p>
<p><strong>接着</strong>，如果单单安装 <code>@types/node</code>，是还不够的，因为 <code>@types/node</code> 仅仅是 <code>TS</code> 文件做声明作用的，即 <code>xxx.d.ts</code>，所以还需要其他内容：</p>
<ul>
<li>安装 <code>@types/node</code>：<code>npm i @types/node -D</code></li>
<li>安装 <code>typescript</code>：<code>npm i typescript -D</code></li>
<li>安装 <code>ts-node</code>：<code>npm i ts-node -D</code></li>
</ul>
<blockquote>
<p>合在一块执行：<code>npm i @types/node typescript ts-node -D</code></p>
</blockquote>
<blockquote>
<p>【2021-06-12 16:42:05】发现一个漏点，照着自己这篇文章，安装这几个包之后，如果执行 <code>node src/index.ts</code> 还是会报：<code>SyntaxError: Unexpected identifier</code>，所以应该安装 <code>npm i ts-node -g</code>，然后再执行 <code>ts-node src/index.ts</code></p>
</blockquote>
<p>此时再执行 <code>node src/index.ts</code>，会发现 <code>path</code> 的信息打印出来了，可行，计划通~</p>
<blockquote>
<p>此时会生成 <code>node_modules</code> 和 <code>package-lock.json</code>，这 2 个详细不介绍，请自行 Google</p>
</blockquote>
<p><strong>最后</strong>，还可以深度配置 TS 内容：</p>
<ul>
<li>创建 <code>tsconfig.json</code>：<code>tsc --init</code></li>
</ul>
<blockquote>
<p>tsc 需要全局安装 <code>typescript</code>，所以需要先执行 <code>npm i typescript -g</code></p>
</blockquote>
<p>执行完命令之后，会自动创建 <code>tsconfig.json</code>，内容如下：</p>
<blockquote>
<p><strong>jsliang</strong> 于 <code>2021-05-11</code> 通过 <code>tsc --init</code> 获取到的 <code>tsconfig.json</code>，并通过机器翻译后开通了限制的几条（毕竟 <strong>jsliang</strong> 4 级都没过，想啥呢~）</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-comment">/* 访问 https://aka.ms/tsconfig.json 查看更多 */</span>

    <span class="hljs-comment">/* 基本选项 */</span>
    <span class="hljs-comment">// "incremental": true,                         /* 启用增量编译 */</span>
    <span class="hljs-string">"target"</span>: <span class="hljs-string">"es5"</span>,                                <span class="hljs-comment">/* 指定 ECMAScript 目标版本: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', 'ES2018', 'ES2019', 'ES2020', 或者 'ESNEXT'. */</span>
    <span class="hljs-string">"module"</span>: <span class="hljs-string">"commonjs"</span>,                           <span class="hljs-comment">/* 指定使用模块: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', 'es2020', 或者 'ESNext'. */</span>
    <span class="hljs-comment">// "lib": [],                                   /* 指定要包含在编译中的库文件 */</span>
    <span class="hljs-comment">// "allowJs": true,                             /* 允许编译 javascript 文件 */</span>
    <span class="hljs-comment">// "checkJs": true,                             /* 报告 javascript 文件中的错误 */</span>
    <span class="hljs-comment">// "jsx": "preserve",                           /* 指定 jsx 代码的生成: 'preserve', 'react-native', 'react', 'react-jsx' 或者 'react-jsxdev'. */</span>
    <span class="hljs-comment">// "declaration": true,                         /* 生成相应的 '.d.ts' 文件 */</span>
    <span class="hljs-comment">// "declarationMap": true,                      /* 对每个 '.d.ts' 文件进行遍历 */</span>
    <span class="hljs-comment">// "sourceMap": true,                           /* 生成相应的 '.map' 文件 */</span>
    <span class="hljs-comment">// "outFile": "./",                             /* 将输出文件合并为一个文件 */</span>
    <span class="hljs-string">"outDir"</span>: <span class="hljs-string">"./dist"</span>,                             <span class="hljs-comment">/* 指定输出目录 */</span>
    <span class="hljs-comment">// "rootDir": "./",                             /* 用来控制输出目录结构 --outDir */</span>
    <span class="hljs-comment">// "composite": true,                           /* 启用项目编译 */</span>
    <span class="hljs-comment">// "tsBuildInfoFile": "./",                     /* 指定文件来存储增量编译信息 */</span>
    <span class="hljs-string">"removeComments"</span>: <span class="hljs-literal">true</span>,                         <span class="hljs-comment">/* 删除编译后的所有的注释 */</span>
    <span class="hljs-comment">// "noEmit": true,                              /* 不生成输出文件 */</span>
    <span class="hljs-comment">// "importHelpers": true,                       /* 从 tslib 导入辅助工具函数 */</span>
    <span class="hljs-comment">// "downlevelIteration": true,                  /* 在 ES5 和 ES3 中全面支持 for-of */</span>
    <span class="hljs-comment">// "isolatedModules": true,                     /* 将每个文件作为单独的模块 （与 'ts.transpileModule' 类似） */</span>

    <span class="hljs-comment">/* 严格的类型检查选项 */</span>
    <span class="hljs-string">"strict"</span>: <span class="hljs-literal">true</span>,                                 <span class="hljs-comment">/* 启用所有严格类型检查选项 */</span>
    <span class="hljs-comment">// "noImplicitAny": true,                       /* 在表达式和声明上有隐含的 any 类型时报错 */</span>
    <span class="hljs-comment">// "strictNullChecks": true,                    /* 启用严格的 null 检查 */</span>
    <span class="hljs-comment">// "strictFunctionTypes": true,                 /* 启用严格的 function 类型检查 */</span>
    <span class="hljs-comment">// "strictBindCallApply": true,                 /* 启用严格的 bind、call、apply 方法参数检查 */</span>
    <span class="hljs-comment">// "strictPropertyInitialization": true,        /* 启用严格的类的属性初始化检查  */</span>
    <span class="hljs-comment">// "noImplicitThis": true,                      /* 当 this 表达式值为 any 类型的时候，生成一个错误 */</span>
    <span class="hljs-comment">// "alwaysStrict": true,                        /* 以严格模式检查每个模块，并在每个文件里加入 'use strict' */</span>

    <span class="hljs-comment">/* 额外的检查 */</span>
    <span class="hljs-string">"noUnusedLocals"</span>: <span class="hljs-literal">true</span>,                         <span class="hljs-comment">/* 有未使用的变量时，抛出错误 */</span>
    <span class="hljs-string">"noUnusedParameters"</span>: <span class="hljs-literal">true</span>,                     <span class="hljs-comment">/* 有未使用的参数时，抛出错误 */</span>
    <span class="hljs-comment">// "noImplicitReturns": true,                   /* 并不是所有函数里的代码都有返回值时，抛出错误 */</span>
    <span class="hljs-comment">// "noFallthroughCasesInSwitch": true,          /* 报告 switch 语句的 fallthrough 错误。（即，不允许 switch 的 case 语句贯穿） */</span>
    <span class="hljs-comment">// "noUncheckedIndexedAccess": true,            /* 在索引签名结果中包含 undefined */</span>
    <span class="hljs-comment">// "noPropertyAccessFromIndexSignature": true,  /* 需要索引签名中未声明的属性才能使用元素访问 */</span>

    <span class="hljs-comment">/* Module Resolution Options */</span>
    <span class="hljs-comment">// "moduleResolution": "node",                  /* 选择模块解析策略： 'node' (Node.js) or 'classic' (TypeScript pre-1.6) */</span>
    <span class="hljs-comment">// "baseUrl": "./",                             /* 用于解析非相对模块名称的基目录 */</span>
    <span class="hljs-comment">// "paths": &#123;&#125;,                                 /* 模块名到基于 baseUrl 的路径映射的列表 */</span>
    <span class="hljs-comment">// "rootDirs": [],                              /* 根文件夹列表，其组合内容表示项目运行时的结构内容 */</span>
    <span class="hljs-comment">// "typeRoots": [],                             /* 包含类型声明的文件列表 */</span>
    <span class="hljs-comment">// "types": [],                                 /* 需要包含的类型声明文件名列表 */</span>
    <span class="hljs-comment">// "allowSyntheticDefaultImports": true,        /* 允许从没有设置默认导出的模块中默认导入 */</span>
    <span class="hljs-string">"esModuleInterop"</span>: <span class="hljs-literal">true</span>,                        <span class="hljs-comment">/* 通过为所有导入创建名称空间对象，启用 CommonJS 和 ES 模块之间的的互动性 */</span>
    <span class="hljs-comment">// "preserveSymlinks": true,                    /* 不解析符号链接的真实路径 */</span>
    <span class="hljs-comment">// "allowUmdGlobalAccess": true,                /* 允许从模块访问 UMD 全局变量 */</span>

    <span class="hljs-comment">/* Source Map Options */</span>
    <span class="hljs-comment">// "sourceRoot": "",                            /* 指定调试器应该找到 TypeScript 文件而不是源文件的位置 */</span>
    <span class="hljs-comment">// "mapRoot": "",                               /* 指定调试器应该找到映射文件而不是生成文件的位置 */</span>
    <span class="hljs-comment">// "inlineSourceMap": true,                     /* 生成单个 soucemaps 文件，而不是将 sourcemaps 生成不同的文件 */</span>
    <span class="hljs-comment">// "inlineSources": true,                       /* E将代码与 sourcemaps 生成到一个文件中，要求同时设置了 --inlineSourceMap 或 --sourceMap 属性 */</span>

    <span class="hljs-comment">/* Experimental Options */</span>
    <span class="hljs-comment">// "experimentalDecorators": true,              /* 启用装饰器 */</span>
    <span class="hljs-comment">// "emitDecoratorMetadata": true,               /* 为装饰器提供元数据的支持 */</span>

    <span class="hljs-comment">/* Advanced Options */</span>
    <span class="hljs-string">"skipLibCheck"</span>: <span class="hljs-literal">true</span>,                           <span class="hljs-comment">/* 跳过声明文件的类型检查 */</span>
    <span class="hljs-string">"forceConsistentCasingInFileNames"</span>: <span class="hljs-literal">true</span>        <span class="hljs-comment">/* 进制对同一文件使用大小写不一致的引用 */</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个文件的作用，是让 TypeScript 将此目录和子目录下的 <code>.ts</code> 文件作为编译上下文的一部分，并且包含一部分默认的编译选项。</p>
<p>另外还有一些配置项可以查看下面的讲解内容。</p>
<h2 data-id="heading-4"><a name="user-content-chapter-three" id="user-content-chapter-three" href="https://juejin.cn/post/undefined"></a>三 tsconfig.json 讲解</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<p><code>tsconfig.json</code> 文件主要是为了养成一些良好的习惯，例如遵循不要通篇代码写 <code>any</code> 类型，不要 <code>import</code> 一些没用的包。</p>
<p>如果需要检验这个配置项，小伙伴们可以往 <code>index.ts</code> 写入下面代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'jsliang 的 Node 工具库'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>node src/index.ts</code> 就会报错：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad50caf8259349b096b603a3954fd201~tplv-k3u1fbpfcp-watermark.image" alt="tslint-config-01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就起到约束的作用。</p>
<p>下面讲解下一些配置项。</p>
<h3 data-id="heading-5"><a name="user-content-chapter-three-one" id="user-content-chapter-three-one" href="https://juejin.cn/post/undefined"></a>3.1 compilerOptions 可配置项</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<p>用来配置 TS 中的一些项：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"compilerOptions"</span>: &#123;

    <span class="hljs-comment">/* 基本选项 */</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><a name="user-content-chapter-three-two" id="user-content-chapter-three-two" href="https://juejin.cn/post/undefined"></a>3.2 files 可配置项</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<p>通过 <code>files</code> 指定需要编译的文件：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"files"</span>: [
    <span class="hljs-string">"./some/file.ts"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><a name="user-content-chapter-three-three" id="user-content-chapter-three-three" href="https://juejin.cn/post/undefined"></a>3.3 include 和 exclude 可配置项</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<p>通过 <code>include</code> 和 <code>exclude</code> 指定需要包含的文件和排除的文件：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"include"</span>: [
    <span class="hljs-string">"./folder"</span>
  ],
  <span class="hljs-string">"exclude"</span>: [
    <span class="hljs-string">"./folder/**/*.spec.ts"</span>,
    <span class="hljs-string">"./folder/someSubFolder"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8"><a name="user-content-chapter-four" id="user-content-chapter-four" href="https://juejin.cn/post/undefined"></a>四 ESLint</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<p>你可以通过 TSLint 或者 ESLint 来约束代码规范。</p>
<p>但是 TSLint 官网表示 2019 及以后它被抛弃了，改用 ESLint，所以这里咱们安装 ESLint 吧。</p>
<blockquote>
<p>参考文献：<a href="https://palantir.github.io/tslint/" target="_blank" rel="nofollow noopener noreferrer">palantir.github.io/tslint/</a></p>
</blockquote>
<p>执行命令：</p>
<ul>
<li><code>npm i eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin -D</code></li>
</ul>
<p>然后创建 <code>.eslintrc.js</code> 来存放下面内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 解析器</span>
  <span class="hljs-attr">parser</span>: <span class="hljs-string">"@typescript-eslint/parser"</span>, <span class="hljs-comment">// 把 TS 转换成 ESTree 兼容格式的解析器，这样就可以在 eslint 中使用了</span>
  
  <span class="hljs-comment">// 拓展：用来继承已有的 ESLint 配置</span>
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">"plugin:@typescript-eslint/recommended"</span>],

  <span class="hljs-comment">// 插件</span>
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">"@typescript-eslint"</span>],

  <span class="hljs-comment">// 环境：设置代码环境，eslint 能够自动识别对应环境所有的全局变量</span>
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">commonjs</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">amd</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es6</span>: <span class="hljs-literal">true</span>,
  &#125;,

  <span class="hljs-comment">/**
   * "off" 或 0 - 关闭规则
   * "warn" 或 1 - 开启规则，使用警告级别的错误：warn (不会导致程序退出),
   * "error" 或 2 - 开启规则，使用错误级别的错误：error (当被触发的时候，程序会退出)
   */</span>
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-comment">/* Possible Errors - 这些规则与 JavaScript 可能的错误或者逻辑错误有关 */</span>
    <span class="hljs-string">"no-dupe-args"</span>:            <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止 function 定义中出现重名参数</span>
    <span class="hljs-string">"no-dupe-keys"</span>:            <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止对象字面量中出现重复的 key</span>
    <span class="hljs-string">"no-empty"</span>:                <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止出现空语句块</span>
    <span class="hljs-string">"no-func-assign"</span>:          <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止对 function 声明重新赋值</span>
    <span class="hljs-string">"no-irregular-whitespace"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止不规则的空白</span>
    <span class="hljs-string">"no-unreachable"</span>:          <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在 return、throw、continue 和 break 语句之后出现不可达代码</span>

    <span class="hljs-comment">/* Best Practices - 这些规则是关于最佳实践的，帮助避免一些问题 */</span>
    <span class="hljs-string">"eqeqeq"</span>:                  <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求使用 === 和 !==</span>
    <span class="hljs-string">"curly"</span>:                   <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制所有控制语句使用一致的括号风格</span>

    <span class="hljs-comment">/* Variables - 这些规则与变量有关 */</span>
    <span class="hljs-string">"no-delete-var"</span>:           <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止删除变量</span>
    <span class="hljs-string">"no-unused-vars"</span>:          <span class="hljs-number">2</span>, <span class="hljs-comment">// 进制出现未使用过的变量</span>

    <span class="hljs-comment">/* Node.js and CommonJS - 关于 Node.js 相关的规则 */</span>
    <span class="hljs-string">"global-require"</span>:          <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求 require() 出现在顶层模块作用域中</span>
    <span class="hljs-string">"handle-callback-err"</span>:     <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求回调函数中有容错处理</span>
  &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置成功之后，我们可以在 <code>index.ts</code> 上看到：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18e5af729aad4c58859b5d97d745f11d~tplv-k3u1fbpfcp-watermark.image" alt="tslint-config-02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>图中这个配置项被关闭了，不能 <code>console</code> 也太奇葩了</p>
</blockquote>
<blockquote>
<p>小 Tips：配合 VS Code 的【ESlint】插件食用更香</p>
</blockquote>
<h2 data-id="heading-9"><a name="user-content-chapter-five" id="user-content-chapter-five" href="https://juejin.cn/post/undefined"></a>五 总结</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<p>当前目录结构如下：</p>
<pre><code class="copyable">+ src
  - index.ts
- .eslintrc.js
- package.json
- tsconfig.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相应的内容在上面我们也讲解过了，当前执行 <code>node src/index.ts</code> 也可以运行起来，TS 构造完毕。</p>
<p>最后贴一下 <code>package.json</code> 当前内容，避免小伙伴们走错路：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"jsliang"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">"Fe-util, Node 工具库"</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-string">"keywords"</span>: [
    <span class="hljs-string">"jsliang"</span>,
    <span class="hljs-string">"Node 工具库"</span>,
    <span class="hljs-string">"Node"</span>
  ],
  <span class="hljs-string">"author"</span>: <span class="hljs-string">"jsliang"</span>,
  <span class="hljs-string">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"@types/node"</span>: <span class="hljs-string">"^15.12.2"</span>,
    <span class="hljs-string">"@typescript-eslint/eslint-plugin"</span>: <span class="hljs-string">"^4.26.1"</span>,
    <span class="hljs-string">"@typescript-eslint/parser"</span>: <span class="hljs-string">"^4.26.1"</span>,
    <span class="hljs-string">"eslint"</span>: <span class="hljs-string">"^7.28.0"</span>,
    <span class="hljs-string">"ts-node"</span>: <span class="hljs-string">"^10.0.0"</span>,
    <span class="hljs-string">"typescript"</span>: <span class="hljs-string">"^4.3.2"</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们下期见~</p>
<h2 data-id="heading-10"><a name="user-content-chapter-six" id="user-content-chapter-six" href="https://juejin.cn/post/undefined"></a>六 参考文献</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6972834535167754270#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="https://palantir.github.io/tslint/" target="_blank" rel="nofollow noopener noreferrer">TSLint</a></li>
<li><a href="https://eslint.org/docs/user-guide/getting-started" target="_blank" rel="nofollow noopener noreferrer">ESLint</a></li>
<li><a href="https://cn.eslint.org/docs/user-guide/getting-started" target="_blank" rel="nofollow noopener noreferrer">ESLint 中文网</a></li>
<li><a href="https://cn.eslint.org/docs/rules/" target="_blank" rel="nofollow noopener noreferrer">ESLint: 配置规则</a></li>
<li><a href="https://blog.csdn.net/sxm666666/article/details/108064890" target="_blank" rel="nofollow noopener noreferrer">CSDN: eslint 简单配置</a></li>
<li><a href="https://note.xiexuefeng.cc/post/eslint-config/" target="_blank" rel="nofollow noopener noreferrer">snowdream: ESLint配置参数</a></li>
</ul>
<hr>
<blockquote>
<p>jsliang 的文档库由 <a href="https://github.com/LiangJunrong" target="_blank" rel="nofollow noopener noreferrer">梁峻荣</a> 采用 <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="nofollow noopener noreferrer">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a> 进行许可。<br>基于 <a href="https://github.com/LiangJunrong/document-library" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a> 上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" target="_blank" rel="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div>  
</div>
            