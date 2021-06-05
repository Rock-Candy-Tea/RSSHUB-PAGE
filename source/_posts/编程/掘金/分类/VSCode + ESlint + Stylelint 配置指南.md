
---
title: 'VSCode + ESlint + Stylelint 配置指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff488a0dc5ad4536906aa7117b893341~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 21:49:59 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff488a0dc5ad4536906aa7117b893341~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>从入坑开始接触了大大小小几十个项目了。在项目的切换中，总会碰到以下一些令人头疼的问题：</p>
<ol>
<li>编辑的时候标红，提示代码格式错误
<ul>
<li>保存的时候没有自动修复。</li>
<li>保存的时候修复了，但是还是报错。</li>
</ul>
</li>
<li>编辑的时候没有标红
<ul>
<li>保存的时候也不报错。</li>
<li>保存的时候报错了。</li>
</ul>
</li>
<li>写 <code>Vue</code> 项目时，只对 <code>script</code> 里的代码检测了语法，<code>template</code> 和 <code>style</code> 里的语法没有提示。保存时也不会自动按照规范修复。</li>
<li>....</li>
</ol>
<p>怀着实在忍不了了心情，我仔细阅读了</p>
<ol>
<li><code>VSCode defaultsetting.json</code> 配置</li>
<li>ESlint 配置规则</li>
<li>eslint-plugin-vue 文档</li>
<li>诸多网上的配置教程</li>
<li>...</li>
</ol>
<p>如果你曾遇到这样的困惑，不妨耐心往下看，相信你会有收获。如果你是前端工程化大佬，请忽略😄</p>
<p>以 <code>VSCode</code> + <code>Vue项目</code> 为例。</p>
<h2 data-id="heading-1">我们想要的效果</h2>
<ol>
<li>
<p>编辑的时候，按照我配置的规则 <code>A</code> 提示我语法有错误（标红）</p>
</li>
<li>
<p>保存的时候，按照规则 <code>A</code>，自动修复所有错误。</p>
</li>
</ol>
<h2 data-id="heading-2">配置VSCode</h2>
<p><code>保存时自动修复</code> 和 <code>文件使用哪套规则</code> 等都在 <code>VSCode</code> 配置。</p>
<p>首先，我们需要找到 <code>VSCode</code> 配置规则的地方。它有 <code>默认规则</code> 和 <code>用户自定义规则</code>。</p>
<p>按 <code>shift + cmd + P</code> 搜索 <code>deafult</code> 打开 <code>defaultSetting.json</code> 就是 <code>VSCode</code> 的默认配置。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff488a0dc5ad4536906aa7117b893341~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还是按 <code>shift + cmd + P</code> 搜索 <code>setting</code> 打开 <code>setting.json</code> 就是 <code>VSCode</code> 的用户自定义配置。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b1a933b5f014b83abd667890c9ac01b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>setting.json</code> 里的配置会覆盖默认设置。</p>
<p>我们需要在 <code>setting.json</code> 里写入以下配置。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-comment">// 保存时使用eslint格式进行修复</span>
    <span class="hljs-attr">"editor.codeActionsOnSave"</span>: &#123;
        <span class="hljs-attr">"source.fixAll"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">"source.fixAll.eslint"</span>: <span class="hljs-literal">true</span>,
    &#125;,
    
    <span class="hljs-comment">// 保存的时候自动格式化</span>
    <span class="hljs-attr">"editor.formatOnSave"</span>: <span class="hljs-literal">true</span>,
    
    <span class="hljs-comment">// 如果你的VSCode安装了Vetur插件，以下配置是需要的</span>
    <span class="hljs-comment">// 这能阻止Vetur对Vue代码进行检测，提高性能</span>
    <span class="hljs-attr">"vetur.format.enable"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"vetur.validation.template"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"vetur.validation.script"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"vetur.validation.style"</span>: <span class="hljs-literal">false</span>,
    
    <span class="hljs-comment">// 以下配置需要VSCode安装ESlint插件</span>
    <span class="hljs-comment">// 使用eslint规范 .Vue，.js</span>
    <span class="hljs-attr">"[vue]"</span>: &#123;
        <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"dbaeumer.vscode-eslint"</span>
    &#125;,
    <span class="hljs-attr">"[javascript]"</span>: &#123;
        <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"dbaeumer.vscode-eslint"</span>
    &#125;,
    
    <span class="hljs-comment">// 使用prettier规范JSON</span>
    <span class="hljs-attr">"[json]"</span>: &#123;
        <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
    &#125;,
    
    <span class="hljs-comment">// eslint设置</span>
    <span class="hljs-attr">"eslint.alwaysShowStatus"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"eslint.validate"</span>: [
        <span class="hljs-string">"javascript"</span>,
        <span class="hljs-string">"vue"</span>,
        <span class="hljs-string">"html"</span>
    ],
    <span class="hljs-attr">"eslint.options"</span>: &#123;
        <span class="hljs-attr">"extensions"</span>: [
            <span class="hljs-string">".js"</span>,
            <span class="hljs-string">".vue"</span>
        ]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们有了如下效果：</p>
<ol>
<li>保存的时候自动格式化代码并使用规则修复</li>
<li><code>.vue</code>,<code>.js</code>文件使用 <code>eslint</code> 规范</li>
<li><code>.json</code> 文件使用 <code>prettier</code> 规范</li>
</ol>
<p>我们上面配置的每一条规则，都可以在 <code>defaultSetting.json</code> 中找到。其中有对规则的作用详细的解释。有的还会有官方链接。想深入了解的同学可以自行查找。</p>
<p>别忘了安装 <code>ESlint</code> 插件哦～</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b02d4fdc465e4543ad6ae608172a3ddd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">配置 <code>ESLint</code> 规则</h2>
<p>配置方式有多种，可以在 <code>package.json</code>里配置，也可以单独配置 <code>.eslintrc.js</code>文件。这里我更推荐使用单独的文件配置。一目了然。</p>
<p>首先，我们在根目录下新建 <code>.eslintrc.js</code> 文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们自己一条条的配置规则，估计整个人都会不好了，还好我们可以直接使用业内推荐的规范。</p>
<p>当然了，如果你是使用脚手架创建的项目，在创建的时候，可以选择使用脚手架默认安装 <code>eslint</code>相关的包。可以打开 <code>package.json</code> 查看是否已经安装了。如果是，则没必要重复安装。</p>
<p>如果还没有安装，打开命令行工具</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm i --save-dev eslint eslint-plugin-vue babel-eslint
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们配置 <code>.eslintrc.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 如果是SSR项目，则需要配置node:true</span>
    <span class="hljs-attr">env</span>: &#123;
        <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-comment">// 为什么是这样的parser配置？</span>
    <span class="hljs-comment">// https://eslint.vuejs.org/user-guide/#how-to-use-a-custom-parser</span>
    <span class="hljs-attr">parser</span>: <span class="hljs-string">'vue-eslint-parser'</span>,
    <span class="hljs-attr">parserOptions</span>: &#123;
        <span class="hljs-attr">parser</span>: <span class="hljs-string">'babel-eslint'</span>
    &#125;,
    <span class="hljs-attr">extends</span>: [
        <span class="hljs-comment">// 如果是nuxt.js的脚手架项目，则需要安装对应的以来并做以下配置 </span>
        <span class="hljs-string">'@nuxtjs'</span>,
        <span class="hljs-string">'plugin:nuxt/recommended'</span>,
        
        <span class="hljs-comment">// 让eslint可以规范vue文件</span>
        <span class="hljs-string">'plugin:vue/base'</span>,
        <span class="hljs-comment">// vue3的项目需要使用，如果是vue2项目，使用 plugin:vue/recommended</span>
        <span class="hljs-string">'plugin:vue/vue3-recommended'</span>
    ],
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">// 注意这里不能配置 html 选项，原因：</span>
        <span class="hljs-comment">// https://eslint.vuejs.org/user-guide/#why-doesn-t-it-work-on-vue-files</span>
        <span class="hljs-string">'vue'</span>
    ],
    <span class="hljs-comment">// 配置自己的规则，覆盖上面继承的规则</span>
    <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-comment">// 配置js的缩进为 4，switch case 语句的 case 也使用4个空格缩进 </span>
        <span class="hljs-attr">indent</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-number">4</span>, &#123; <span class="hljs-attr">SwitchCase</span>: <span class="hljs-number">1</span> &#125;],
        <span class="hljs-comment">// 使用 eslint 检测 template里的代码，这里我配置 4 个空格缩进</span>
        <span class="hljs-string">'vue/html-indent'</span>: [
            <span class="hljs-string">'error'</span>,
            <span class="hljs-number">4</span>
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上配置，大家根据自己的项目特点，自行删减即可。比如，如果你的项目不是 <code>nuxt.js</code> 的，可以去掉 <code>extends</code> 里的 <code>'@nuxtjs</code> 和 <code>plugin:nuxt/recommended</code>。</p>
<p>现在我们基本已经实现了想要的效果。</p>
<ol>
<li>编辑的时候，对 <code>.js</code>,<code>.vue</code> 文件的 <code>template</code> 和 <code>script</code> 使用配置的 <code>eslint</code> 规范检查。</li>
<li>保存的时候，对以上文件使用相同的 <code>eslint</code> 规范进行自动修复。</li>
</ol>
<h2 data-id="heading-4">配置 <code>stylelint</code></h2>
<p>不过我们现在还不能对 <code>.css,.scss</code> 和 <code>vue</code> 文件里的 <code>style</code>  部分做规范检查和自动修复。这需要安装<code>stylelint</code>。</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm i --save-dev stylelint stylelint-config-standard stylelint-scss
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上安装了 <code>stylelint</code> 和 业内使用比较多的规范 <code> stylelint-config-standard</code> 和对 <code>scss</code> 语法的支持 <code>stylelint-scss</code>。</p>
<p>接下来我们需要配置它们。</p>
<p>在根目录下新增 <code>.stylelintrc.json</code> 文件。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-comment">// 使用规范</span>
    <span class="hljs-attr">"extends"</span>: <span class="hljs-string">"stylelint-config-standard"</span>,
    <span class="hljs-comment">// 自定义4个空格缩进</span>
    <span class="hljs-attr">"rules"</span>: &#123;
        <span class="hljs-attr">"indentation"</span>: <span class="hljs-number">4</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>VSCode</code> 安装 <code>stylelint</code> 插件。</p>
<p>大功告成！赶快试试吧～</p></div>  
</div>
            