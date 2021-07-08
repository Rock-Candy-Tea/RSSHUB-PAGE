
---
title: '手摸手教你使用最新版husky(v7.0.1)让代码更优雅规范'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e452c75dcd4453d9f09d48ce4528c61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 06:36:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e452c75dcd4453d9f09d48ce4528c61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767/" target="_blank" title="https://juejin.cn/post/6978685539985653767/">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
</blockquote>
<blockquote>
<p><strong>hello，大家好，我是小憨憨，一个持续性学习，不间断写bug的前端工程师</strong></p>
</blockquote>
<h2 data-id="heading-0">写在前面</h2>
<p>日常工作中，几乎每个项目都是由多个人进行维护，每个人的代码书写习惯和风格又不尽相同，在这种情况下，如果没有统一的规范，你就会发现提交到代码仓库的代码格式五花八门，并且<code>commit log</code>也是乱七八糟，更严重点可能有的小伙伴在提交代码的时候为了省事<code>commit message</code>直接就是两个点点，总之，可能就是怎么省事怎么来。最终导致的结果就是，当你某一天需要<code>cherry-pick</code>某个<code>commit</code>到另外的分支的时，看着<code>commmit log</code>一脸懵逼。所以，规范和约束在多人协作下，就显得尤为重要。</p>
<h2 data-id="heading-1">githooks</h2>
<p>类似于前端框架中的生命周期钩子，git在某些特定事件发生前或后也会有某些执行特定功能的钩子，githooks就是在git执行特定事件（如commit、push、receive等）时触发运行的脚本。</p>
<p>githooks 保存在 .git 文件夹中</p>
<p>具体钩子如下表所示：</p>






















































































































































<table><thead><tr><th>git hook</th><th>执行时机</th><th>说明</th></tr></thead><tbody><tr><td>applypatch-msg</td><td>git am 执行前</td><td>默认情况下，如果commit-msg启用的话，applpatch-msg钩子在启用时会运行commit-msg钩子</td></tr><tr><td>pre-applypatc</td><td>git am 执行前</td><td>默认的pre-applypatch钩子在启用时运行pre-commit钩子（如果后者已启用）</td></tr><tr><td>post-applypatch</td><td>git am 执行后</td><td>这个钩子主要用于通知，不能影响git-am的结果</td></tr><tr><td>pre-commit</td><td>git commit 执行前</td><td>可以使用 git commit --no verify 命令绕过该钩子</td></tr><tr><td>pre-merge-commit</td><td>git merge 执行前</td><td>可以使用 git merge --no verify 命令绕过该钩子</td></tr><tr><td>prepare-commit-msg</td><td>git commit执行之后，编辑器打开之前</td><td></td></tr><tr><td>commit-msg</td><td>git commit 执行前</td><td>可以使用 git commit --no verify 命令绕过该钩子</td></tr><tr><td>post-commit</td><td>git commit 执行后</td><td>不影响git commit的结果</td></tr><tr><td>pre-rebase</td><td>git rebase执行前</td><td></td></tr><tr><td>post-checkout</td><td>git checkout 或 git switch执行后</td><td>如果不使用 --no-checkout 参数，则在 git clone 之后也会执行</td></tr><tr><td>post-merge</td><td>git merge 执行后</td><td>在执行git pull 时也会被调用</td></tr><tr><td>pre-push</td><td></td><td>git push 执行前</td></tr><tr><td>pre-receive</td><td>git receive pack 执行前</td><td></td></tr><tr><td>update</td><td></td><td></td></tr><tr><td>proc-receive</td><td></td><td></td></tr><tr><td>post-receive</td><td>git receive pack 执行前</td><td>不影响 git receive pack 的执行结果</td></tr><tr><td>post-update</td><td>当git receive pack对 git push 作出反应并更新仓库中的引用时</td><td></td></tr><tr><td>reference-transaction</td><td></td><td></td></tr><tr><td>push-to-checkout</td><td>当git receive pack对 git push 作出反应并更新仓库中的引用时，以及当推送试图更新当前被签出的分支且 receive.denyCurrentBranch配置被updateInstead时</td><td></td></tr><tr><td>pre-auto-gc</td><td>git gc --auto 执行前</td><td></td></tr><tr><td>post-rewrite</td><td>执行 git commit --amend 或 git rebase 时</td><td></td></tr><tr><td>sendemail-validate</td><td>git send-email 执行前</td><td></td></tr><tr><td>fsmonitor-watchman</td><td>配置core.fsmonitor被设置为.git/hooks/fsmonitor-watchman 或.git/hooks/fsmonitor-watchmanv2时</td><td></td></tr><tr><td>p4-changelist</td><td>git-p4 submit 执行并编辑完changelist message 之后</td><td>可以使用 git-p4 submit --no-verify绕过该钩子</td></tr><tr><td>p4-prepare-changelist</td><td>git-p4 submit 执行后，编辑器启动前</td><td>可以使用 git-p4 submit --no-verify绕过该钩子</td></tr><tr><td>p4-post-changelist</td><td>git-p4 submit 执行后</td><td></td></tr><tr><td>p4-pre-submit</td><td>git-p4 submit 执行前</td><td>可以使用 git-p4 submit --no-verify绕过该钩子</td></tr><tr><td>post-index-change</td><td>索引被写入 read-cache.c do_write_locked_index后</td><td></td></tr></tbody></table>
<h2 data-id="heading-2">husky(v7.0.1)</h2>
<p>husky 是一个让配置 git 钩子变得更简单的工具。支持所有的git钩子。</p>
<h3 data-id="heading-3">使用husky</h3>
<ul>
<li>首先执行安装命令  <code>npm install husky --save-dev</code></li>
<li>要在安装后自动启用钩子，我们需要执行<code>npm set-script prepare "husky install"</code></li>
<li>执行完上一步的命令之后可以在package.json 文件的scripts配置项中看到如下代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"prepare"</span>: <span class="hljs-string">"husky install"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>创建钩子，比如我们创建一个commit-msg钩子：<code>yarn husky add .husky/commit-msg 'yarn commitlint --edit "$1"'</code></p>
</li>
<li>
<p>将上一步创建的 commit-msg 钩子添加到git中：<code>git add .husky/commit-msg</code></p>
</li>
<li>
<p>此外还有 <code>husky-init</code>命令， 执行之后可以在项目中快速的初始化一个husky。</p>
</li>
</ul>
<h2 data-id="heading-4">lint-staged(v11.0.0)</h2>
<p><strong>lint-staged 是一个在git暂存区上运行linters的工具。</strong>（Run linters against staged git files and don't let 💩 slip into your code base!）</p>
<p>它将根据package.json依赖项中的代码质量工具来安装和配置 husky 和 lint-staged ，因此请确保在此之前安装（npm install --save-dev）并配置所有代码质量工具，比如Prettier和ESlint。</p>
<ul>
<li>安装：执行 <code>yarn add lint-staged -D</code> 命令</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">执行 npx lint-staged --help 命令可以看到相关的所有参数如下：
用法: lint-staged [options]

<span class="hljs-attr">Options</span>:
  -V, --version                      输出版本号
  --allow-empty                      当任务撤消所有分阶段的更改时允许空提交（默认值：<span class="hljs-literal">false</span>）
  -c, --config [path]                配置文件的路径
  -d, --debug                        打印其他调试信息（默认值：<span class="hljs-literal">false</span>）
  -p, --concurrent <parallel tasks>  要同时运行的任务数，或者为<span class="hljs-literal">false</span>则要连续运行任务（默认值：<span class="hljs-literal">true</span>）
  -q, --quiet                        自己的控制台输出（默认值：<span class="hljs-literal">false</span>）
  -r, --relative                     将相对文件路径传递给任务（默认值：<span class="hljs-literal">false</span>）
  -x, --shell                        跳过任务解析以更好地支持shell（默认值：<span class="hljs-literal">false</span>）
  -h, --help                         输出用法信息
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>--allow-empty</strong>：使用此参数允许创建空的git提交。默认情况下，当LITER任务撤消所有阶段性的更改时，LITET阶段将抛出一个错误，并中止提交。</li>
</ul>
<h2 data-id="heading-5">git commit提交规范</h2>
<p>通常使用 Google AnguarJS 规范的要求。
格式要求：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">type</span>></span>(<span class="hljs-tag"><<span class="hljs-name">scope</span>></span>): <span class="hljs-tag"><<span class="hljs-name">subject</span>></span>
<span class="hljs-tag"><<span class="hljs-name">BLANK</span> <span class="hljs-attr">LINE</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">BLANK</span> <span class="hljs-attr">LINE</span>></span>
<span class="hljs-tag"><<span class="hljs-name">footer</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code><type></code>代表某次提交的类型，比如是修复一个 bug 或是增加一个 feature，具体类型如下：</li>
</ul>













































<table><thead><tr><th>类型</th><th>描述</th></tr></thead><tbody><tr><td>feat</td><td>新增feature</td></tr><tr><td>fix</td><td>修复bug</td></tr><tr><td>docs</td><td>仅仅修改了文档，比如README, CHANGELOG, CONTRIBUTE等等;</td></tr><tr><td>style</td><td>仅仅修改了空格、格式缩进、逗号等等，不改变代码逻辑;</td></tr><tr><td>refactor</td><td>代码重构，没有加新功能或者修复bug</td></tr><tr><td>perf</td><td>优化相关，比如提升性能、体验</td></tr><tr><td>test</td><td>测试用例，包括单元测试、集成测试等</td></tr><tr><td>chore</td><td>改变构建流程、或者增加依赖库、工具等</td></tr><tr><td>revert</td><td>回滚到上一个版本</td></tr></tbody></table>
<ul>
<li><code>scope</code>：说明commit影响的范围。scope依据项目而定，例如在业务项目中可以依据菜单或者功能模块划分，如果是组件库开发，则可以依据组件划分。</li>
<li><code>subject</code>:是commit的简短描述；</li>
<li><code>body</code>:提交代码的详细描述；</li>
<li><code>footer</code>:如果代码的提交是不兼容变更或关闭缺陷，则footer必需，否则可以省略。</li>
</ul>
<h2 data-id="heading-6">实现</h2>
<ul>
<li>
<p>首先我们来安装需要用到的依赖，执行以下命令：</p>
</li>
<li>
<p>执行 <code>yarn add husky -D</code> 安装husky。</p>
</li>
<li>
<p>接着执行 <code>yarn set-script prepare "husky install"</code> 之后，可以在package.json文件的scripts配置项中看到 <code>"prepare": "husky install"</code></p>
</li>
<li>
<p>继续执行 <code>yarn prepare</code>之后，可以在项目的根目录下看到多了如下图所示的目录：</p>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e452c75dcd4453d9f09d48ce4528c61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>husky 准备好之后，我们接着来安装其他的用于规范，检查代码的依赖。</p>
</li>
<li>
<p>执行<code>yarn add lint-staged -D</code></p>
</li>
<li>
<p>执行<code>yarn add eslint prettier -D</code></p>
</li>
<li>
<p>在package.json文件下添加如下代码：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"lint-staged"</span>: &#123;
    <span class="hljs-string">"src/**/*.&#123;js,jsx,ts,tsx,json&#125;"</span>: [
      <span class="hljs-string">"prettier --write"</span>,
      <span class="hljs-string">"eslint"</span>,
      <span class="hljs-string">"git add"</span>
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>执行<code>yarn add @commitlint/cli @commitlint/config-conventional -D</code>安装commitlint相关依赖，用来帮助我们在多人开发时，遵守 git 提交约定。</p>
</li>
<li>
<p>执行<code>echo "module.exports = &#123;extends: ['@commitlint/config-conventional']&#125;" > commitlint.config.js</code>在根目录创建 commitlint.config.js 文件（当然也可以手动创建此文件），其内容如下所示：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">"@commitlint/config-conventional"</span>
  ],
  <span class="hljs-comment">// 以下时我们自定义的规则</span>
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'type-enum'</span>: [
      <span class="hljs-number">2</span>,
      <span class="hljs-string">'always'</span>,
      [
        <span class="hljs-string">'bug'</span>, <span class="hljs-comment">// 此项特别针对bug号，用于向测试反馈bug列表的bug修改情况</span>
        <span class="hljs-string">'feat'</span>, <span class="hljs-comment">// 新功能（feature）</span>
        <span class="hljs-string">'fix'</span>, <span class="hljs-comment">// 修补bug</span>
        <span class="hljs-string">'docs'</span>, <span class="hljs-comment">// 文档（documentation）</span>
        <span class="hljs-string">'style'</span>, <span class="hljs-comment">// 格式（不影响代码运行的变动）</span>
        <span class="hljs-string">'refactor'</span>, <span class="hljs-comment">// 重构（即不是新增功能，也不是修改bug的代码变动）</span>
        <span class="hljs-string">'test'</span>, <span class="hljs-comment">// 增加测试</span>
        <span class="hljs-string">'chore'</span>, <span class="hljs-comment">// 构建过程或辅助工具的变动</span>
        <span class="hljs-string">'revert'</span>, <span class="hljs-comment">// feat(pencil): add ‘graphiteWidth’ option (撤销之前的commit)</span>
        <span class="hljs-string">'merge'</span> <span class="hljs-comment">// 合并分支， 例如： merge（前端页面）： feature-xxxx修改线程地址</span>
      ]
    ]
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>如果还需要别的代码优化依赖包，可以接着进行安装</p>
</li>
<li>
<p>至此，准备好我们需要的依赖包之后，我们开始添加钩子</p>
</li>
<li>
<p>执行<code>yarn husky add .husky/commit-msg 'yarn commitlint --edit "$1"'</code>之后，会看到在根目录的<code>.husky</code>文件夹下多了一个 <code>commit-msg</code> 文件，其内容如下：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.sh"</span>

yarn commitlint --edit <span class="hljs-string">"$1"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>紧接着，我们需要将上一步添加的钩子添加到git中去，执行<code>git add .husky/commit-msg</code></p>
</li>
<li>
<p>执行<code>yarn husky add .husky/pre-commit 'yarn lint-staged --allow-empty "$1"'</code>之后，会看到在根目录的<code>.husky</code>文件夹下多了一个 <code>pre-commit</code> 文件，其内容如下：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">#!<span class="hljs-regexp">/bin/</span>sh
. <span class="hljs-string">"$(dirname "</span>$<span class="hljs-number">0</span><span class="hljs-string">")/_/husky.sh"</span>

yarn lint-staged --allow-empty <span class="hljs-string">"$1"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>同样的，我们需要将上一步添加的钩子添加到git中去，执行<code>git add .husky/pre-commit</code></p>
</li>
<li>
<p>接下来，就是检验我么配置的时候了：当我们按照 commit规范正确提交时，可以在控制台看到如下输出</p>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f95bad7174b422cab42b6ef64686bbd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>当我们不按照配置的规范来提交commit时，就会发现如下报错，并阻止你提交代码</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea5260a7b47c4d32b9aa1d526d64b397~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>至此，我们的钩子配置已经完美收官！</li>
</ul>
<h2 data-id="heading-7">写在最后</h2>
<p>写作不易，欢迎点（一）赞（键）收（三）藏（连），若有错误的地方，欢迎评论指正！！！</p>
<p>我是小憨憨，一个持续性学习，不间断写bug的前端工程师。关注我，不迷路。一起学习，一起进步。</p></div>  
</div>
            