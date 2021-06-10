
---
title: 'Electron+Vue3 MAC 版日历开发记录(10)——env 使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 06:47:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于之前界面有点傻大个，所以在任务里，我加了一条：「整体缩小一倍」，但是伴随的问题也就出现了，我总不能每次调整界面大小，然后在所以有布局的地方都一遍一遍的找出来修改吧。</p>
<p>所以，今天我把关注点放在了变量上，也就是今天的记录主题：<code>env</code> 的使用。</p>
<p>其实在很多成熟的框架 (各种编程语言)，如 PHP 的 Laravel 框架，也是使用 <code>env</code> 来配置我们的静态和敏感变量。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e4974d55d064183919593960c4f317d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">环境变量说明</h2>
<p><code>Vite</code> 在一个特殊的 <code>import.meta.env</code> 对象上暴露环境变量。这里有一些普遍适用的内建变量：</p>
<blockquote>
<p><code>import.meta.env.MODE: &#123;string&#125;</code> 应用运行基于的 模式。</p>
<p><code>import.meta.env.BASE_URL: &#123;string&#125;</code> 应用正被部署在的 base URL。它由 base 配置项 决定。</p>
<p><code>import.meta.env.PROD: &#123;boolean&#125;</code> 应用是否运行在生产环境</p>
<p><code>import.meta.env.DEV: &#123;boolean&#125;</code> 应用是否运行在开发环境 (永远与 <code>import.meta.env.PROD</code> 相反)</p>
</blockquote>
<ol>
<li>在本项目里，我把常规的通用变量，如 <code>window</code> 长和宽放在 <code>.env</code> 下，如：</li>
</ol>
<pre><code class="copyable">VITE_APP_WIDTH=500
VITE_APP_HEIGHT=400
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：为了防止意外地将一些环境变量泄漏到客户端，只有以 <code>VITE_</code> 为前缀的变量才会暴露给经过 <code>vite</code> 处理的代码。</p>
</blockquote>
<p>在代码中，就可以直接使用了：</p>
<pre><code class="copyable">// main/src/App.ts
const window = new BrowserWindow(&#123;
  width: Number(this.env.VITE_APP_WIDTH),
  height: Number(this.env.VITE_APP_HEIGHT),
  resizable: false,
  alwaysOnTop: true,
  show: false,
  frame: false,
  webPreferences: &#123;
    webSecurity: false,
    preload: join(__dirname, '../../preload/dist/index.cjs'),
    contextIsolation: this.env.MODE !== 'test',   // Spectron tests can't work with contextIsolation: true
    enableRemoteModule: this.env.MODE === 'test', // Spectron tests can't work with enableRemoteModule: false
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>同样的，本项目用到的天气预报服务器 API 也可以放在 <code>.env</code> 中，在 <code>service</code> 中直接使用</li>
</ol>
<pre><code class="copyable">// .env
VITE_APP_WIDTH=700
VITE_APP_HEIGHT=600
VITE_WEATHER_API=***

// WeatherService.ts
const res = await http(&#123;
  url: import.meta.env.VITE_WEATHER_API,
  method: 'get',
  params: &#123;
    param: JSON.stringify(&#123;
      location: locationStr,
    &#125;),
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86f7107dc3a14ae1b08f9bb329c9341a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">智能提示</h2>
<p>根据 <a href="https://vitejs.dev/guide/env-and-mode.html" target="_blank" rel="nofollow noopener noreferrer">VITE 官方文档</a> 所说的：</p>
<blockquote>
<p><code>Vite</code> 会默认为 <code>import.meta.env</code> 提供类型定义。随着在 <code>.env[mode]</code> 文件中定义了越来越多自定义环境变量，你可能想要在代码中获取这些以 <code>VITE_ </code>为前缀的用户自定义环境变量的 <code>TypeScript</code> 智能提示。</p>
<p>要想做到这一点，你可以在 <code>src</code> 目录下创建一个 <code>env.d.ts</code>，接着按下面这样定义 <code>ImportMetaEnv</code>：</p>
</blockquote>
<pre><code class="copyable">interface ImportMetaEnv &#123;
  VITE_DEV_SERVER_URL: string,
  // 更多环境变量...
  VITE_APP_WIDTH: number,
  VITE_APP_HEIGHT: number,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而在本项目所引用的框架中，是采用「命令」生成以上文件的，见：<code>types/env.d.ts</code>:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff0e4c7fa93a45fb9fecb53a8bcc8571~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>生成该文件的代码如下：</p>
<pre><code class="copyable">#!/usr/bin/env node

const &#123;resolveConfig&#125; = require('vite');
const &#123;writeFileSync, mkdirSync, existsSync&#125; = require('fs');
const &#123;resolve, dirname&#125; = require('path');

const MODES = ['production', 'development', 'test'];

const typeDefinitionFile = resolve(process.cwd(), './types/env.d.ts');

/**
 *
 * @return &#123;string&#125;
 */
function getBaseInterface() &#123;
  return 'interface IBaseEnv &#123;[key: string]: string&#125;';
&#125;

/**
 *
 * @param &#123;string&#125; mode
 * @return &#123;Promise<&#123;name: string, declaration: string&#125;>&#125;
 */
async function getInterfaceByMode(mode) &#123;
  const interfaceName = `$&#123;mode&#125;Env`;
  const &#123;env: envForMode&#125; = await resolveConfig(&#123;mode&#125;, 'build');
  return &#123;
    name: interfaceName,
    declaration: `interface $&#123;interfaceName&#125; extends IBaseEnv $&#123;JSON.stringify(envForMode)&#125;`,
  &#125;;
&#125;

/**
 * @param &#123;string[]&#125; modes
 * @param &#123;string&#125; filePath
 */
async function buildMode(modes, filePath) &#123;

  const IBaseEnvDeclaration = getBaseInterface();

  const interfaces = await Promise.all(modes.map(getInterfaceByMode));

  const allDeclarations = interfaces.map(i => i.declaration);
  const allNames = interfaces.map(i => i.name);

  const ImportMetaEnvDeclaration = `type ImportMetaEnv = Readonly<$&#123;allNames.join(' | ')&#125;>`;

  const content = `
    $&#123;IBaseEnvDeclaration&#125;
    $&#123;allDeclarations.join('\n')&#125;
    $&#123;ImportMetaEnvDeclaration&#125;
  `;

  const dir = dirname(filePath);
  if (!existsSync(dir)) &#123;
    mkdirSync(dir);
  &#125;


  writeFileSync(filePath, content, &#123;encoding: 'utf-8', flag: 'w'&#125;);
&#125;

buildMode(MODES, typeDefinitionFile)
  .catch(err => &#123;
    console.error(err);
    process.exit(1);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码应该都能看得懂，不再解释了。命令写在 <code>package.json</code>：</p>
<pre><code class="copyable"> "buildEnvTypes": "node scripts/buildEnvTypes.js",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以每次更新静态变量，在运行之前，都需要执行一次该命令：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37c041ff95204a6b8099f6a6ecf573d2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">小结</h2>
<p>好了，今天总算了解了下有关 <code>Vite</code> 相关的知识，如何使用 <code>env</code> 来配置静态变量，如何在不同环境 (<code>development</code>、<code>production</code>、<code>test</code>、<code>local</code>) 下使用。最后剩下一个 <code>staging</code> 没用到，有待于以后使用的时候再做总结了。</p>
<p>未完待续！</p>
<blockquote>
<p>这个项目的所有记录基本放进专栏里了，欢迎查看：
<a href="https://juejin.cn/column/6968672386895839269" target="_blank">Electron+Vue3 MAC 版日历开发记录</a></p>
<p>最近有伙伴问代码链接：代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            