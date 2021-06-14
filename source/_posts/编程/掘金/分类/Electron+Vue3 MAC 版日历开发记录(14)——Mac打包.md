
---
title: 'Electron+Vue3 MAC 版日历开发记录(14)——Mac打包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 02:59:00 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第14天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>半个月的努力，终于到了发布一版本的时候了，基于功能逻辑虽然有待不断完善，但根据 MVP 最小量化开发逻辑，给自己定了每两周发一版本的要求。</p>
<p>所以今天的目标就是学习如何打包 Mac 版本。</p>
<p>学习如何在 Github Action 上如何自动化打包 Mac 版本之前，我们需要学习下有关 Github Action 知识。</p>
<h2 data-id="heading-0">Github Actiion</h2>
<p>在使用这个框架模板的前几天，我一直发现，只要我提交代码到 Gtihub 上，总会看到一个红色(❎️)的提示 (当然现在基本都是✅️的提示了)：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/837090b190da42a4999476e201545ec5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击这个提示，发现是跳转到「Actions」界面，如下面报错的截图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0c10870dca446b58327cea3110a3578~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>后来通过了解，原来所有的 Actions 对应的 workflows 是写在了 <code>.github</code> 目录下，具体可看 <a href="https://docs.github.com/en/actions/quickstart" target="_blank" rel="nofollow noopener noreferrer">Github 官网介绍</a>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd680e52f3e84696ac09c35d538b8eb5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面拿 <code>lint.yml</code> 做简单介绍。</p>
<h3 data-id="heading-1">lint.yml</h3>
<p>顾名思义，这个主要是配合代码格式化检测的，其实在代码 commit 到缓存时，也会执行 <code>yarn lint</code> 操作。</p>
<pre><code class="copyable">// package.json
"simple-git-hooks": &#123;
  "pre-commit": "npx lint-staged",
  "pre-push": "npm run typecheck"
&#125;,
"lint-staged": &#123;
  "*.&#123;js,ts,vue&#125;": "eslint --cache --fix"
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即这个等效于：</p>
<pre><code class="copyable">// package.json
"scripts": &#123;
  ...
  
  "lint": "eslint . --ext js,ts,vue",
  
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以在 commit 代码之前，我都会自己执行 <code>yarn lint</code> 让代码没报错。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e93f9b50b4444181bb0e184203b24b84~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>回过头来，我们看看这个 <code>workflow</code> 代码：</p>
<pre><code class="copyable">name: Linters
on:
  push:
    branches:
      - main
    paths:
      - '**.js'
      - '**.ts'
      - '**.vue'
      - 'yarn.lock'
      - '.github/workflows/lint.yml'
  pull_request:
    paths:
      - '**.js'
      - '**.ts'
      - '**.vue'
      - 'yarn.lock'
      - '.github/workflows/lint.yml'


defaults:
  run:
    shell: 'bash'

jobs:
  eslint:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: 15 # Need for npm >=7.7

      - uses: actions/cache@v2
        with:
          path: ~/.npm
          key: $&#123;&#123; runner.os &#125;&#125;-node-$&#123;&#123; hashFiles('**/yarn.lock') &#125;&#125;
          restore-keys: |
            $&#123;&#123; runner.os &#125;&#125;-node-

      # TODO: Install not all dependencies, but only those required for this workflow
      - name: Install dependencies
        run: npm install -g yarn && yarn install --immutable

      - run: yarn lint
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只看最后几行代码基本就知道了，使用了 <code>yarn.lock</code>快速安装所有依赖，然后在全局中安装好 <code>yarn</code>，之后执行 <code>yarn lint</code>，效果一样。</p>
<h3 data-id="heading-2">打包</h3>
<p>看了 <code>lint.yml</code> 的原理，基本也就明白了打包的 <code>release.yml</code> 原理了。</p>
<p>直接看代码：</p>
<pre><code class="copyable">// release.yml
// 其他的舍弃
# Compile app and upload artifacts
  - name: Compile & release Electron app
    uses: samuelmeuli/action-electron-builder@v1
    with:
      build_script_name: build
      args: --config electron-builder.config.js

      # GitHub token, automatically provided to the action
      # (No need to define this secret in the repo settings)
      github_token: $&#123;&#123; secrets.github_token &#125;&#125;
      mac_certs: $&#123;&#123; secrets.mac_certs &#125;&#125;
      mac_certs_password: $&#123;&#123; secrets.mac_certs_password &#125;&#125;

      # If the commit is tagged with a version (e.g. "v1.0.0"),
      # release the app after building
      release: true

      # Sometimes the build may fail due to a connection problem with Apple, GitHub, etc. servers.
      # This option will restart the build as many attempts as possible
      max_attempts: 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要说明的一个就是怎么获取 Mac <code>Code Signing</code>。</p>
<blockquote>
<p>Code Signing</p>
<p>If you are building for macOS, you'll want your code to be signed. GitHub Actions therefore needs access to your code signing certificates:</p>
<p>Open the Keychain Access app or the Apple Developer Portal. Export all certificates related to your app into a single file (e.g. certs.p12) and set a strong password Base64-encode your certificates using the following command: base64 -i certs.p12 -o encoded.txt</p>
</blockquote>
<p>In your project's GitHub repository, go to Settings → Secrets and add the following</p>
<blockquote>
<p>two variables:
mac_certs: Your encoded certificates, i.e. the content of the encoded.txt file you created before
mac_certs_password: The password you set when exporting the certificates</p>
</blockquote>
<pre><code class="copyable">- name: Build/release Electron app
  uses: samuelmeuli/action-electron-builder@v1
  with:
    # ...
    mac_certs: $&#123;&#123; secrets.mac_certs &#125;&#125;
    mac_certs_password: $&#123;&#123; secrets.mac_certs_password &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体在 Mac developer 中心怎么创建一个开发者证书这里就不说了，之后在我们 Mac 本机器上导师证书 p12 格式文件，然后加密输出为字符串：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a76db93b581e43a1a45dcd3e893a204f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3018870632494940a30fa9da5c813bd5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，再将内容填入 <code>Settings/Secrets</code> 中，以供 release action 使用：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a86d7ecfb8a48b09f24d3b62fb71607~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，我们提交代码，看 workflow 运行起来：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/643bd9638eda48e2bd1ff4ece5921334~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此，在 Draft 里可以看到打包的执行包：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36e59eab5bc144458482a8b260e64de9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下载并按照看看能不能跑起来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2f7799af69148fe98953935ca9bfe58~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b88796a70968442a94f3a60d6792096c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">小结</h2>
<p>今天我们粗略了解下如何执行 Github Actions，如何编写 Workflows 和 Mac 证书生成并最后打包成 dmg 格式，以供下载安装使用。</p>
<blockquote>
<p>这里我把之前引入的框架中默认打包为 windows exe 改为 Mac dmg 的；
之前使用 npm，这里改为 yarn；
关于 test 部分我目前删除了，有待于下一步使用时增加自动化测试环节。</p>
</blockquote>
<p>此外，在打包出来执行后，发现有关网络请求和缓存报错了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd2709f43f0b4523baea233a4ce1d9b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这有待于我继续优化了，未完待续！</p>
<blockquote>
<p>这个项目的所有记录基本放进专栏里了，欢迎查看：
<a href="https://juejin.cn/column/6968672386895839269" target="_blank">Electron+Vue3 MAC 版日历开发记录</a>
最近有伙伴问代码链接：代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
<p>最后的最后，每篇文章的开头和结尾不是为了凑数而加上的，我<strong>不为写水文而水</strong>～</p>
</blockquote></div>  
</div>
            