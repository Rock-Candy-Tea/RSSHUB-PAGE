
---
title: '从 TypeScript 到 VSCode —— 语言服务插件导引'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Sun, 21 Mar 2021 23:43:20 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>众所周知，在如今的开发者中 TypeScript 日渐流行。TypeScript 提供了强劲的类型检查能力，除此之外，比较不为人知的是，它还以 <code>language service</code> 的形式提供了针对 TypeScript 和 JavaScript 开发体验的编辑器支持能力，例如重构，快速修复，自动补全等。并且 TypeScript 提供了基础的针对 <code>language service</code> 的扩展能力。<br>
VSCode 也是当下非常流行的一款 editor。VSCode 提供了丰富的扩展能力，同时, VSCode 作为同属 Microsoft 维护的开源项目，也与 TypeScript 进行了深度的集成和整合。</p>
<p>本文以作者的一款 TypeScript/VSCode 插件 <a href="https://github.com/HearTao/ts-string-literal-enum-plugin" target="_blank" rel="nofollow noopener noreferrer">ts-string-literal-enum-plugin</a> (将 Enum 转换为字符串字面量 Enum的插件) 为线索，进行了对 TypeScript/VSCode/Language Service 生态的一次探索。</p>
<h3 data-id="heading-1">背景</h3>
<p>在 TypeScript 众多的 issue 中，有这样一个 <a href="https://github.com/microsoft/TypeScript/issues/16464" target="_blank" rel="nofollow noopener noreferrer">#16464</a> 希望可以扩展 Enum 语法的提案，这个提案的目的在于提供一种简便方法，以允许大家快捷方便的定义 “字符串字面量枚举”，即如下形式：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Action &#123;
   LOAD_PROFILE = <span class="hljs-string">"LOAD_PROFILE"</span>,
   ADD_TASK = <span class="hljs-string">"ADD_TASK"</span>,
   REMOVE_TASK = <span class="hljs-string">"REMOVE_TASK"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于经常会用到字符串字面量枚举的开发者来说，可能需要很多恼人的 “复制-粘贴” 或多行编辑操作，而这会降低开发者的体验。因此提案提议支持如下语法，当做上面定义的语法糖：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Action: <span class="hljs-built_in">string</span> &#123;
   LOAD_PROFILE,
   ADD_TASK,
   REMOVE_TASK
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>作者对此持支持的观点，但由于种种原因，TypeScript 团队目前并没有接受这个提案，并且提出了一些解决方案，例如提供重构动作以允许用户方便的转换 Enum 的形式。<br>
而作者则实现了 TypeScript 团队所提出的解决方案，并与大家分享相关的经验。</p>
<h3 data-id="heading-2">实现</h3>
<h5 data-id="heading-3">TypeScript language service plugin</h5>
<p>TypeScript 提供了对于 <code>language service plugin</code> 的支持，允许用户扩展 <code>language service</code> 的能力，并且有<a href="https://github.com/microsoft/TypeScript/wiki/Writing-a-Language-Service-Plugin" target="_blank" rel="nofollow noopener noreferrer">相关文档</a>，本文不再赘述。</p>
<h6 data-id="heading-4">API</h6>
<p>首先，我们需要扩展 TypeScript <code>language service</code> 提供的功能。而我们首先要知道 <code>language service</code> 提供了哪些功能，以及这些功能对外暴露出的接口定义，这些信息可以在 <a href="https://github.com/microsoft/TypeScript/blob/master/src/services/types.ts#L333" target="_blank" rel="nofollow noopener noreferrer">TypeScript 类型定义中</a> 找到。由于我们的目的是增加重构动作，根据上方提到的类型定义可知，我们需要扩展 <code>language service</code> 中的 <code>getApplicableRefactors</code> 和 <code>getEditsForRefactor</code> 两个接口。</p>
<p>顾名思义，<code>getApplicableRefactors</code> 代表根据提供的信息，获取可以在当前上下文使用的重构动作。而 <code>getEditsForRefactor</code> 则是在当前上下文中，获取使用重构所需的文本编辑操作。</p>
<h6 data-id="heading-5">Plugin</h6>
<p>简单来说，TypeScript 期望得到并加载 <code>export = (mod: &#123; typescript: ts &#125;) => &#123; create(info: ts.server.PluginCreateInfo): ts.LanguageService &#125;</code> 形式的 plugin，即 TypeScript 会将运行时使用的 TypeScript 与一些运行时信息 (例如当前所使用的 <code>language service</code> 实例) 注入 plugin 中。<br>
值得注意的是，我们需要使用 <code>mod.typescript</code> - 即被注入至 plugin 中的 TypeScript 库来作为我们 plugin 中使用到的 TypeScript 库，这样做有两个原因:</p>
<ul>
<li>不同版本的 TypeScript 可能有很多名字相同但值不同的定义，若不使用被注入 plugin 的 TypeScript 库可能会造成兼容性问题。</li>
<li>可以减少打包 plugin 时对 TypeScript 的依赖，减小 plugin 体积。</li>
</ul>
<p>我们的目的是扩展原有的 <code>language service</code>，也就是说需要保留原有的功能，在此基础上增加我们自定义的操作，即类似 decoration/proxy 的行为。</p>
<p>实现 plugin 所需的基础代码不再赘述，可以在 <a href="https://github.com/HearTao/ts-string-literal-enum-plugin/blob/main/src/plugin.ts" target="_blank" rel="nofollow noopener noreferrer">src/plugin.ts</a>, <a href="https://github.com/HearTao/ts-string-literal-enum-plugin/blob/main/src/decorator.ts" target="_blank" rel="nofollow noopener noreferrer">src/decorator.ts</a> 和 <a href="https://github.com/HearTao/ts-string-literal-enum-plugin/blob/main/src/index.ts" target="_blank" rel="nofollow noopener noreferrer">src/index.ts</a> 中查看。</p>
<h6 data-id="heading-6">Service</h6>
<p>Service 也是 plugin 的核心功能由, 即提供可用重构动作和与之对应的文本编辑操作。、</p>
<p>由上文提到的类型定义中可知，<code>getApplicableRefactors</code> 有 <code>fileName, positionOrRange</code> 等参数，其中我们只关注这 2 个参数。<code>getEditsForRefactor</code> 则有
<code>fileName, positionOrRange, refactor, actionName</code> 等参数，其中我们只关注这 4 个参数。</p>
<p>整体实现有很多细节，本文不再赘述，仅简述主要逻辑：</p>
<ul>
<li>实现 <code>getApplicableRefactors</code>
<ol>
<li>根据 <code>fileName</code> 与 <code>positionOrRange</code> 获取触发重构动作的位置与与之对应的 AST Node。</li>
<li>判断当前 AST Node 是否符合我们的预期。 plugin 中提供了 <code>将 Enum 或 Enum member 转换为“字符串字面量枚举”</code> 两个功能，也就是判断是 Node 否为 <code>EnumDeclaration</code> 或 <code>EnumMember</code>，并且若为 <code>EnumMember</code>，则不能有初始化表达式（称之为 <code>可转换的</code>）；若为 <code>EnumDeclaration</code>, 则至少有一个 member 为<code>可转换的</code>。</li>
<li>若符合预期，则根据当前节点信息返回对应的重构动作信息，用于在 VSCode 中展示。</li>
</ol>
</li>
<li>实现 <code>getEditsForRefactor</code>
<ol>
<li>根据 <code>fileName</code> 与 <code>positionOrRange</code> 获取要使用重构动作的位置与与之对应的 AST Node。</li>
<li>进行语法转换，为 Enum member 生成初始化表达式。其中使用到的 <code>TextChanges API</code> 与 <code>TypeScript Internal API</code> 可以在 <a href="https://juejin.cn/post/6942338521541640223" target="_blank">一种编辑 TypeScript 代码的方式</a> 与 <a href="https://www.npmjs.com/package/open-typescript" target="_blank" rel="nofollow noopener noreferrer">open-typescript</a> 中找到。</li>
<li>返回要使用的重构动作对应的文本操作。</li>
</ol>
</li>
</ul>
<h6 data-id="heading-7">构建与使用</h6>
<p>在 <code>package.json</code> 中指定 <code>main</code> 为 <code>tsc</code> build 指定的目录后，即可以 TypeScript <code>language service plugin</code> 的形式测试与使用。
我们可以以 <code>file:</code> 或 <code>yarn pack</code> 的形式将其安装到项目中，在 <code>tsconfig.json</code> 中指定 <code>&#123; "compilerOptions": &#123; "plugins": [&#123; "name": "《plugin package》" &#125;] &#125;&#125;</code>，并在 VSCode 中选择使用 <code>node_modules</code> 中的 TypeScript 即可。</p>
<h5 data-id="heading-8">VSCode extensions</h5>
<p>上文提到，VSCode 与 TypeScript 有深度的集成和整合（TypeScript Extensions 也由 VSCode 团队在维护），拜此所赐，我们可以非常方便快捷的将一个 TypeScript plugin 集成为 VSCode extensions。</p>
<h6 data-id="heading-9">Contribution Points</h6>
<p>如果你熟悉 VSCode 开发，那你一定知道 VSCode 有许多 <code>Contribution Points</code>，我们可以通过这些 <code>Contribution Points</code> 来一定程度上影响到 VSCode 的行为。</p>
<p>而幸运的是，VSCode 提供了 <a href="https://code.visualstudio.com/api/references/contribution-points#contributes.typescriptServerPlugins" target="_blank" rel="nofollow noopener noreferrer">Contribution Point</a> 这样一个 contribution point。我们可以利用这个 contribution point 来直接将 TypeScript <code>language service plugin</code> 加载到 VSCode 中。</p>
<h6 data-id="heading-10">实现</h6>
<p>对于我们实现的 plugin 来说，目前并不需要一些额外的交互（例如：VSCode 中的配置项等），因此我们只需要在 <code>package.json</code> 中补充需要的信息（如 <code>name</code>，<code>icon</code> 等）即可完成 extension 的开发。<a href="https://github.com/HearTao/ts-string-literal-enum-plugin/blob/main/extension/package.json" target="_blank" rel="nofollow noopener noreferrer">可以在这里看到完整配置</a>。</p>
<p>构建与发布则可以参考官方文档: <a href="https://code.visualstudio.com/api/working-with-extensions/publishing-extension" target="_blank" rel="nofollow noopener noreferrer">publishing-extension</a>，为了更好的体验，我们还可以指定 <code>vscodeignore</code> 以忽略不必要的文件，增加 README 等。在本地构建出 <code>.vsix</code> 文件后，便可在 VSCode 中安装和使用 extension。</p>
<h5 data-id="heading-11">自动化</h5>
<p>我们还可以实现对于 PR 进行 <a href="https://github.com/HearTao/ts-string-literal-enum-plugin/blob/main/.github/workflows/build.yml" target="_blank" rel="nofollow noopener noreferrer">gated build</a>， 或对于 release 自动 publish 到 <a href="https://github.com/HearTao/ts-string-literal-enum-plugin/blob/main/.github/workflows/publish.yml" target="_blank" rel="nofollow noopener noreferrer">npm 以及 vscode marketplace</a>。这部分与其他项目大同小异，不再赘述。</p>
<h3 data-id="heading-12">结语</h3>
<p>TypeScript 和 VSCode 都是当前最火热最流行的项目之一，本文由一个 TypeScript issue 出发，将 TypeScript，TypeScript plugin 及 VSCode extension 串联起来。揭开了 TypeScript/VSCode 生态的冰山一角。希望可以帮助到大家。</p>
<p>感谢阅读。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            