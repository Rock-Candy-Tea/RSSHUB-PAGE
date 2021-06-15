
---
title: 'vue2环境下成功使用vite的实践总结！！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e956a8e0444acfa5d83fd9874079d8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 00:05:51 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e956a8e0444acfa5d83fd9874079d8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">vue2环境下成功使用vite的实践总结</h1>
<p>自从vite发布以来，社区赞誉无数，现在vite也更新到了2.0大版本，我也一直心水vite的极速编译的特性，特别是由于现在项目体积过大，已经严重拖慢了编译和热更新的速度，急需寻找一个解决方案。但无奈官方现在只有支持vue3的插件，而我的项目还是使用的vue2版本，于是我就一直在尝试如何将vite成功应用于vue2项目中，这是这段时间以来实践中总结出的一些问题解决方案，供大家参考。</p>
<p>说明： 按我设想的理想方案是：webpack作为打包工具，vite作为开发工具，所以我会考虑到在vite和webpack环境下尽量的维护一份共同配置。</p>
<h2 data-id="heading-1">如何正确的引入vue单文件</h2>
<p>在@vue/cli搭建的项目环境中，webpack配置中增加了对<code>.vue</code>文件扩展名的解析，以使我们导入时可以省略<code>.vue</code>后缀，但在vite文档中不建议忽略自定义导入类型的扩展名（例如：.vue），因为它会影响 IDE 和类型支持，所以需要将以前所有没有写明<code>.vue</code>后缀的模块引入都给补上。由于项目庞大，手动去每个文件中更改肯定是不现实的事情，所以我写了一个脚本，在node中执行，自动补全<code>.vue</code>后缀名</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// rewriteImportPath.js</span>

<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);
<span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">"chalk"</span>);

<span class="hljs-keyword">const</span> overridePaths = [];
<span class="hljs-keyword">const</span> r = <span class="hljs-regexp">/(?<!\/\/\s+|\*\s+)(?:im|ex)port (.*?) from "((?:\.&#123;0,2&#125;\/|[^.\s\r\n\t\\\/]+\/)*[^\s\r\n\t\\\/;]+)"|import\((?:\s*\/\*.*?\*\/\s*)?"((?:\.&#123;0,2&#125;\/|[^.\s\r\n\t\\\/]+\/)*[^\s\r\n\t\\\/;]+)"\)/g</span>;

<span class="hljs-keyword">const</span> baseDir = path.join(process.cwd(), <span class="hljs-string">"src"</span>);
<span class="hljs-keyword">const</span> defaultExtensions = [<span class="hljs-string">".mjs"</span>, <span class="hljs-string">".js"</span>, <span class="hljs-string">".ts"</span>, <span class="hljs-string">".jsx"</span>, <span class="hljs-string">".tsx"</span>, <span class="hljs-string">".json"</span>];

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">rewritePath</span>(<span class="hljs-params">baseDir, rootPath</span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> resolveAlias = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./resolveAlias"</span>);
    <span class="hljs-keyword">const</span> directory = fs.readdirSync(baseDir);
    directory.forEach(<span class="hljs-function"><span class="hljs-params">file</span> =></span> &#123;
      <span class="hljs-keyword">const</span> filePath = path.join(baseDir, file);
      <span class="hljs-keyword">const</span> stat = fs.statSync(filePath);
      <span class="hljs-keyword">if</span> (stat.isDirectory()) &#123;
        rewritePath(filePath);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/\.vue$|\.jsx?$/</span>.test(file)) &#123;
        <span class="hljs-keyword">const</span> fileContent = fs.readFileSync(filePath, <span class="hljs-string">"utf-8"</span>);
        <span class="hljs-keyword">const</span> newFileContent = fileContent.replace(r, <span class="hljs-function">(<span class="hljs-params">$$, $<span class="hljs-number">1</span>, $<span class="hljs-number">2</span>, $<span class="hljs-number">3</span></span>) =></span> &#123;
          <span class="hljs-keyword">let</span> importPath;
          <span class="hljs-keyword">const</span> isDynamicImport = !!$<span class="hljs-number">1</span>;
          <span class="hljs-keyword">const</span> modulePath = isDynamicImport ? $<span class="hljs-number">2</span> : $<span class="hljs-number">3</span>;
          <span class="hljs-keyword">if</span> (modulePath.startsWith(<span class="hljs-string">"."</span>)) &#123;
            importPath = path.join(baseDir, modulePath);
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span> (path.isAbsolute(modulePath)) &#123;
              importPath = path.join(rootPath, modulePath);
            &#125; <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-keyword">const</span> dirLevels = modulePath.split(<span class="hljs-string">"/"</span>);
              <span class="hljs-keyword">const</span> pathAlias = resolveAlias[dirLevels.shift()];
              <span class="hljs-keyword">if</span> (pathAlias) &#123;
                importPath = path.join(pathAlias, ...dirLevels);
              &#125;
            &#125;
          &#125;
          <span class="hljs-keyword">if</span> (!importPath) &#123;
            <span class="hljs-keyword">return</span> $$;
          &#125;
          <span class="hljs-keyword">let</span> suffix;
          <span class="hljs-keyword">const</span> files = fs.readdirSync(path.dirname(importPath));
          <span class="hljs-keyword">const</span> parsedImpPath = path.parse(importPath);
          files.some(<span class="hljs-function"><span class="hljs-params">file</span> =></span> &#123;
            <span class="hljs-keyword">const</span> parsedFilePath = path.parse(file);
            <span class="hljs-keyword">if</span> (
              defaultExtensions.includes(parsedFilePath.ext) &&
              parsedFilePath.name === parsedImpPath.name
            ) &#123;
              <span class="hljs-comment">// 修复模块导入的后缀错误</span>
              <span class="hljs-keyword">if</span> (
                parsedImpPath.ext === <span class="hljs-string">".js"</span> &&
                parsedFilePath.ext === <span class="hljs-string">".jsx"</span>
              ) &#123;
                suffix = parsedFilePath.ext;
              &#125;
              <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
            &#125;
            <span class="hljs-keyword">if</span> (
              !parsedImpPath.ext &&
              parsedFilePath.ext === <span class="hljs-string">".vue"</span> &&
              parsedFilePath.name === parsedImpPath.name
            ) &#123;
              suffix = <span class="hljs-string">".vue"</span>;
              <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
            &#125;
          &#125;);
          <span class="hljs-keyword">if</span> (suffix) &#123;
            <span class="hljs-keyword">const</span> &#123;dir,name&#125; = path.parse(modulePath)
            <span class="hljs-keyword">const</span> overridePath = $$.replace(
              modulePath,
              <span class="hljs-string">`<span class="hljs-subst">$&#123;dir&#125;</span>/<span class="hljs-subst">$&#123;name&#125;</span><span class="hljs-subst">$&#123;suffix&#125;</span>`</span>
            );
            overridePaths.push(<span class="hljs-string">"pathRewrite："</span> + $$ + <span class="hljs-string">"  >>>  "</span> + overridePath);
            <span class="hljs-keyword">return</span> overridePath;
          &#125;
          <span class="hljs-keyword">return</span> $$;
        &#125;);
        <span class="hljs-keyword">if</span> (fileContent !== newFileContent) &#123;
          fs.writeFileSync(filePath, newFileContent, <span class="hljs-string">"utf-8"</span>);
        &#125;
      &#125;
    &#125;);
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`error in <span class="hljs-subst">$&#123;baseDir&#125;</span>：\n`</span>, e);
  &#125;
&#125;
rewritePath(baseDir, process.cwd());
overridePaths.forEach(<span class="hljs-function"><span class="hljs-params">v</span> =></span> <span class="hljs-built_in">console</span>.log(v));
<span class="hljs-built_in">console</span>.log(
  <span class="hljs-string">"\n✔️ "</span>,
  chalk.green(<span class="hljs-string">"共成功改写"</span> + overridePaths.length + <span class="hljs-string">"条引用路径"</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">如何让vite能够解析vue2代码</h2>
<p>vite与vue2搭配使用，主要使用到的插件为<a href="https://github.com/underfin/vite-plugin-vue2" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-vue2</a>，这也是vite文档中推荐适配vue2开发的插件</p>
<h2 data-id="heading-3">如何启用jsx语法</h2>
<p>在vite中使用<code>jsx</code>还是稍微有点麻烦的，一是使用到<code>jsx</code>语法的js文件都必须改成使用<code>jsx</code>后缀名，二是在vue的<code>sfc</code>组件中还得加上<code>jsx</code>标识</p>
<ol>
<li>
<p>首先需要在<code>vite-plugin-vue2</code>中启用<code>jsx</code></p>
<p>vite.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite"</span>;
<span class="hljs-keyword">import</span> &#123; createVuePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite-plugin-vue2"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
    <span class="hljs-attr">plugins</span>: [createVuePlugin(&#123;<span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>&#125;)]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>sfc</code>组件中加上<code>jsx</code>标识</p>
<p>需要在<strong>script block</strong>中加上<code>lang=jsx</code>的标识</p>
<pre><code class="hljs language-vue copyable" lang="vue"><script lang="jsx">
    export default &#123;
        render()&#123;
            return <div>JSX Render</div>
        &#125;
    &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>另外，由于现在开发vue2项目中基本都是在IDE中使用vetur插件启用vue特性支持，然而当在vue文件中的script标签中加上lang="jsx"后，无法再使用vetur进行代码格式化，详见此<a href="https://github.com/vuejs/vetur/issues/2781" target="_blank" rel="nofollow noopener noreferrer">issue</a></strong></p>
</li>
<li>
<p>需要将所有使用到<code>jsx</code>语法的js文件后缀名改为<code>.jsx</code></p>
</li>
</ol>
<p>当<code>vite-plugin-vue2</code>发现有导入的资源是vue类型并且有<code>lang=jsx</code>的标识的时候，就会启用jsx转译，其核心依然是通过<code>babel</code>使用<code>@vue/babel-preset-jsx</code>进行转译,这里有一个坑点需要注意：</p>
<p><strong>当使用babel转译的时候，babel会默认搜寻当前项目目录中的babel配置文件，例如<code>babelrc</code>或者<code>babel.config.js</code>,如果当前项目存在着有babel的配置文件，则会在编译<code>jsx</code>语法代码的时候被启用,那么则需要确认配置文件中是否已经包含过@vue/babel-preset-jsx,不能重复添加同一个preset，否则编译会产生错误</strong></p>
<p>因为我项目中打算是开发环境使用<code>vite</code>，而生产环境则依然使用webpack进行打包，所以babel配置文件也是不能删除的，解决方案如下：</p>
<ol>
<li>
<p>如果是使用的babel.config.js文件，通过配置中<code>env</code>决定只在生产模式下才启用配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">production</span>: &#123;
      <span class="hljs-attr">presets</span>: [
        [
            <span class="hljs-string">'@vue/app'</span>,
            &#123;
                <span class="hljs-string">'useBuiltIns'</span>: <span class="hljs-string">'entry'</span>
            &#125;
        ]
      ]
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用<code>.babelrc</code>文件替换<code>babel.config.js</code>，因为<code>vite-plugin-vue2</code>中使用<code>babel</code>时指定了<code>babelrc:false</code>,也就是忽略<code>.babelrc</code>中的配置，避免使用到无关的<code>babel</code>配置。</p>
<p>vite-plugin-vue2中的jsxTransform.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformVueJsx</span>(<span class="hljs-params">code, id, jsxOptions</span>) </span>&#123;
    <span class="hljs-keyword">const</span> plugins = [];
    <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/\.tsx$/</span>.test(id)) &#123;
        plugins.push([
            <span class="hljs-built_in">require</span>.resolve(<span class="hljs-string">'@babel/plugin-transform-typescript'</span>),
            &#123; <span class="hljs-attr">isTSX</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">allowExtensions</span>: <span class="hljs-literal">true</span> &#125;,
        ]);
    &#125;
    <span class="hljs-keyword">const</span> result = core_1.transform(code, &#123;
        <span class="hljs-attr">presets</span>: [[<span class="hljs-built_in">require</span>.resolve(<span class="hljs-string">'@vue/babel-preset-jsx'</span>), jsxOptions]],
        <span class="hljs-attr">sourceFileName</span>: id,
        <span class="hljs-attr">sourceMaps</span>: <span class="hljs-literal">true</span>,
        plugins,
        <span class="hljs-attr">babelrc</span>: <span class="hljs-literal">false</span>,
    &#125;);
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">code</span>: result.code,
        <span class="hljs-attr">map</span>: result.map,
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>我给<code>vite-plugin-vue2</code>的作者发起了一个<a href="https://github.com/underfin/vite-plugin-vue2/pull/78" target="_blank" rel="nofollow noopener noreferrer">pr</a>,在<code>babel.transform</code>中加入<code>configFile:false</code>选项以解决此问题，但是还未被成功采纳。</p>
<h2 data-id="heading-4">问题实录</h2>
<h3 data-id="heading-5">一、不要在transition-group子元素上使用index作为key</h3>
<p>解决方案： 不要在<code>v-for</code>循环中使用<code>index</code>作为key,应替换为唯一值</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e956a8e0444acfa5d83fd9874079d8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210401094139124.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">二、scss无法使用:export导出变量</h3>
<p>目前<code>vite</code>不支持<code>:export</code>这种语法：</p>
<pre><code class="hljs language-sass copyable" lang="sass">$primary: #1890ff
:export &#123;
    primary: $primary
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查找过相应的<a href="https://github.com/vitejs/vite/issues/1279" target="_blank" rel="nofollow noopener noreferrer">issue</a>，尤大说的只会支持sass官方所支持的语法，建议使用<code>css-modules</code>替代。而:export实际并不是sass语法，webpack环境下支持<code>:export</code>这种写法实际是由<strong>css-loader</strong>提供的能力</p>
<p>解决方案：启用<strong>css-modules</strong>功能即可，开启<strong>css-modules</strong>功能也很简单，直接将scss文件后缀名改为 <strong>module.scss</strong>即可</p>
<h3 data-id="heading-7">三、 @ant-design/icons-vue导入报错</h3>
<p>在项目中，使用到了<code>ant-design-vue</code>中的几个组件，使用的按需导入方式（通过<a href="https://github.com/onebay/vite-plugin-imp" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-imp</a>插件），其内部的图标组件就依赖了<code>@ant-design/icons-vue</code>，报错如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b87a253d9d345a897f48c8f86cd5d2a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要原因为：
node_modules\ant-design-vue\es\icon\index.js</p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> allIcons <span class="hljs-keyword">from</span> <span class="hljs-string">'@ant-design/icons/lib/dist'</span>;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从<code>@ant-design/icons/lib/dist</code>中导入的<code>allIcons</code>多了一个<code>default</code>的导出项,这是由于vite的<strong>commonjs转es</strong>模块所导致的，所以遍历<code>allIcons</code>的时候遍历到<code>default</code>的时候报错</p>
<p>解决方案：</p>
<p>不再使用按需导入的方式，而是通过全量引入，直接引用打包编译过后的代码，需要配置路径别名，当遇到<code>imoprt &#123;xxx&#125; from 'antd-design-vue'</code>的时候，指向到 <code>import &#123;xxx&#125; from 'ant-design-vue/dist/antd.min.js</code></p>
<p>vite.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> defineConfig(&#123;
    <span class="hljs-attr">resolve</span>:&#123;
        <span class="hljs-attr">alias</span>: [
            &#123;<span class="hljs-attr">find</span>: <span class="hljs-regexp">/ant-design-vue$/</span>,replacement: <span class="hljs-string">'ant-design-vue/dist/antd.min'</span>&#125;
        ]
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意，当这样改了过后就不要再使用按需导入的插件了，只有引入编译后的代码才能解决这个错误，只能全量引入，在开发环境下，全量导入也是能接受的</strong></p>
<p>另外，全量引入后，记得手动引入<code>ant-design-vue</code>的样式文件</p>
<h3 data-id="heading-8">四、vue模版编译出现多余的空格字符</h3>
<p>此问题可能导致页面内容错位，因为Dom结构中会出现多余的空白字符，导致文本内容间出现分隔、行内标签间出现空格。而<code>vue-cli</code>中默认是对模版编译选项中配置了对空格的处理选项，而<code>vite-plugin-vue2</code>是没有默认配置的，就导致默认情况下与<code>webpack</code>版<code>vue-cli</code>环境下的配置有所差异。详见此<a href="https://github.com/underfin/vite-plugin-vue2/pull/62" target="_blank" rel="nofollow noopener noreferrer">issue</a>.</p>
<p>解决方案：</p>
<p>vite.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createVuePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite-plugin-vue2"</span>;
<span class="hljs-keyword">export</span> defineConfig(&#123;
      <span class="hljs-attr">plugins</span>: [
        createVuePlugin(&#123;
            <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">vueTemplateOptions</span>: &#123;
                <span class="hljs-attr">compilerOptions</span>: &#123;
                  <span class="hljs-attr">whitespace</span>: <span class="hljs-string">"condense"</span>
                &#125;
            &#125;
        &#125;)
     ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">五、require.context在vite环境下无法使用</h3>
<p><code>require.context</code>是webpack独有的语法，用于创建一个require上下文，通常用于批量导入模块。然而在<code>vite</code>中根本不支持<code>require</code>，所有的模块导入都必须使用<code>import</code>，所以<code>vite</code>中也提供了一个用于批量导入的<a href="https://cn.vitejs.dev/guide/features.html#glob-import" target="_blank" rel="nofollow noopener noreferrer">glob导入</a>功能</p>
<p><strong>import.meta.glob</strong></p>
<p>用于动态的导入多个模块（懒加载），且每个模块在构建时被分离为单独的chunk。例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> modules = <span class="hljs-keyword">import</span>.meta.glob(<span class="hljs-string">'./dir/*.js'</span>)

<span class="hljs-comment">// 以上语句会被转译为如下的样子：</span>

<span class="hljs-comment">// vite 生成的代码</span>
<span class="hljs-keyword">const</span> modules = &#123;
  <span class="hljs-string">'./dir/foo.js'</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./dir/foo.js'</span>),
  <span class="hljs-string">'./dir/bar.js'</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./dir/bar.js'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>import.meta.globEager</strong></p>
<p>用于静态的导入多个模块，例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> modules = <span class="hljs-keyword">import</span>.meta.glob(<span class="hljs-string">'./dir/*.js'</span>)

<span class="hljs-comment">// 以上语句会被转译为如下的样子：</span>

<span class="hljs-comment">// vite 生成的代码</span>
<span class="hljs-comment">// vite 生成的代码</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> __glob__0_0 <span class="hljs-keyword">from</span> <span class="hljs-string">'./dir/foo.js'</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> __glob__0_1 <span class="hljs-keyword">from</span> <span class="hljs-string">'./dir/bar.js'</span>
<span class="hljs-keyword">const</span> modules = &#123;
  <span class="hljs-string">'./dir/foo.js'</span>: __glob__0_0,
  <span class="hljs-string">'./dir/bar.js'</span>: __glob__0_1
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无论是批量动态导入还是批量静态导入，返回的都是一个对象，其中的<code>key</code>是该模块的所处路径，value是一个动态加载模块的函数或者直接就是一个导入的模块。而<code>require.context</code>返回的则是一个函数，所以在将<code>require.context</code>替换为<code>glob导入</code>时还需要注意获取获取导入的模块的方式改变。</p>
<p>由于与<code>require.context</code>的差异，所以在webpack环境中与在vite环境中无法使用通用的处理逻辑，最近我发现了一个<code>babel</code>插件<a href="https://www.npmjs.com/package/babel-plugin-transform-vite-meta-glob" target="_blank" rel="nofollow noopener noreferrer">babel-plugin-transform-vite-meta-glob</a>，可以直接在webpack环境中使用<code>glob导入</code>方式，此插件会将其转译为与vite中相同的处理方式，这样的话可保持vite环境与webpack环境下批量导入模块的代码一致，例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> modules = <span class="hljs-keyword">import</span>.meta.glob(<span class="hljs-string">'./path/to/files/**/*'</span>)

<span class="hljs-keyword">const</span> eagerModules = <span class="hljs-keyword">import</span>.meta.globEager(<span class="hljs-string">'./path/to/files/**/*'</span>)

<span class="hljs-comment">// 以上代码会转译为如下这样</span>

<span class="hljs-keyword">const</span> modules = &#123;
  <span class="hljs-string">'./path/to/files/file1.js'</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./path/to/files/file1.js'</span>),
  <span class="hljs-string">'./path/to/files/file2.js'</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>((<span class="hljs-string">'./path/to/files/file2.js'</span>),
  <span class="hljs-string">'./path/to/files/file3.js'</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>((<span class="hljs-string">'./path/to/files/file3.js'</span>)
&#125;

<span class="hljs-keyword">const</span> eagerModules = &#123;
  <span class="hljs-string">'./path/to/files/file1.js'</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'./path/to/files/file1.js'</span>),
  <span class="hljs-string">'./path/to/files/file2.js'</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'./path/to/files/file2.js'</span>),
  <span class="hljs-string">'./path/to/files/file3.js'</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'./path/to/files/file3.js'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">六、Svg Icon如何使用</h3>
<p>在webpack中使用svg icon,一般都是采用<a href="https://github.com/JetBrains/svg-sprite-loader" target="_blank" rel="nofollow noopener noreferrer">svg-sprite-loader</a>去做处理，方便直接在代码使用。而vite下也有一个类似的插件<a href="https://github.com/anncwb/vite-plugin-svg-icons/blob/main/README.zh_CN.md" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-svg-icons</a>,配置与<code>svg-sprite-loader</code>类似</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite"</span>;
<span class="hljs-keyword">import</span> &#123; createVuePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite-plugin-vue2"</span>;
<span class="hljs-keyword">import</span> viteSvgIcons <span class="hljs-keyword">from</span> <span class="hljs-string">"vite-plugin-svg-icons"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    createVuePlugin(&#123;
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">vueTemplateOptions</span>: &#123;
        <span class="hljs-attr">compilerOptions</span>: &#123;
          <span class="hljs-attr">whitespace</span>: <span class="hljs-string">"condense"</span>
        &#125;
      &#125;
    &#125;),
    viteSvgIcons(&#123;
      <span class="hljs-attr">iconDirs</span>: [resolve(__dirname, <span class="hljs-string">"src/icon/svg"</span>)],
      <span class="hljs-attr">symbolId</span>: <span class="hljs-string">"icon-[name]"</span>
    &#125;)
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在项目入口的js文件中，添加一个模块引入：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
...
<span class="hljs-keyword">import</span> <span class="hljs-string">"vite-plugin-svg-icons/register"</span>;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大功告成，接下来即可像在webpack环境中使用<strong>svg icon</strong>一样尽情享用了。</p>
<h3 data-id="heading-11">七、别名配置</h3>
<p>vite中同样支持与webpack类似的别名系统</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;defineConfig&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig &#123;
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">".mjs"</span>, <span class="hljs-string">".js"</span>, <span class="hljs-string">".ts"</span>, <span class="hljs-string">".jsx"</span>, <span class="hljs-string">".tsx"</span>, <span class="hljs-string">".json"</span>],
    <span class="hljs-attr">alias</span>: [
      ...Object.keys(aliasConfig).map(<span class="hljs-function"><span class="hljs-params">key</span> =></span> (&#123;
        <span class="hljs-attr">find</span>: key,
        <span class="hljs-attr">replacement</span>: aliasConfig[key]
      &#125;)),
      &#123; <span class="hljs-attr">find</span>: <span class="hljs-string">"timers"</span>, <span class="hljs-attr">replacement</span>: <span class="hljs-string">"timers-browserify"</span> &#125;,
      &#123; <span class="hljs-attr">find</span>: <span class="hljs-regexp">/ant-design-vue$/</span>, replacement: <span class="hljs-string">"ant-design-vue/dist/antd.min"</span> &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我是将别名配置抽出为一份公共的配置文件，以备webpack和vite使用一份相同的别名配置：</p>
<pre><code class="copyable">// aliasConfig

const &#123;resolve&#125; = require('path');
module.exports = &#123;
  "@": resolve(__dirname, "src"),
  static: resolve(__dirname, "public/static"),
  YZT: resolve(__dirname, "src/views/YZT"),
  FZSC: resolve(__dirname, "src/views/FZSC"),
  JCYJ: resolve(__dirname, "src/views/JCYJ"),
  GHSS: resolve(__dirname, "src/views/GHSS"),
  FZBZ: resolve(__dirname, "src/views/FZBZ"),
  ZBMX: resolve(__dirname, "src/views/ZBMX"),
  YWXT: resolve(__dirname, "src/views/YWXT"),
  MXXT: resolve(__dirname, "src/views/MXXT"),
  JDGL: resolve(__dirname, "src/views/JDGL"),
  JDTB: resolve(__dirname, "src/views/JDTB")
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">剩余待解决问题</h2>
<ol>
<li>vue中script标签中增加<code>lang="jsx"</code>标识后，更改代码无法实现热更新,关联<a href="https://github.com/vitejs/vite/issues/3008" target="_blank" rel="nofollow noopener noreferrer">issue</a></li>
<li>vue中script标签增加<code>lang="jsx"</code>标识后，无法使用vetur格式化，关联<a href="https://github.com/vuejs/vetur/issues/2781" target="_blank" rel="nofollow noopener noreferrer">issue</a></li>
<li>热更新状态丢失，关于这个问题，我搜了很多issue，但都没找到有类似问题的记录，并且我使用demo做测试时也并不能复现问题，但是实际应用在项目，就确实会出现这个问题，还没有找到头绪</li>
<li>某些依赖包由于内部使用了<code>require</code>导入的语法，导致vite不能成功将其转化为es模块，在运行时会报错。</li>
</ol>
<h2 data-id="heading-13">总结</h2>
<p>现在我的项目已经能成功使用vite启动起来了，但实际感受下来，在项目启动速度上并没有质的改变，因为项目过大，初次启动时通过网络请求加载模块的数量也非常非常多，导致速度并没有明显提升。但是在热更新方面，确实如尤大所说：速度快到惊人。</p>
<p>现在基于vite成功应用在生产环境中的案例也还比较少，遇到些问题都还得自己探索，但不可否认，vite提供了一种与webpack完全不同的方式，并且在编译和热更新速度上有较大的优势，期望能尽快完善vite相关的体系，能更加便捷的应用在项目中。</p>
<p>大家平时可以多关注下这个项目：<a href="https://github.com/vitejs/awesome-vite" target="_blank" rel="nofollow noopener noreferrer">awesome-vite</a>，里面有很多推荐的插件集合和各种不同技术栈使用vite的示例项目，遇到问题时可以提供一些解决思路。</p></div>  
</div>
            