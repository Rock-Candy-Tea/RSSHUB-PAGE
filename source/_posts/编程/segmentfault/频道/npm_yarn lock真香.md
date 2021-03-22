
---
title: 'npm_yarn lock真香'
categories: 
    - 编程
    - segmentfault
    - 频道

author: segmentfault
comments: false
date: 2021-03-22 18:15:52
thumbnail: 'https://segmentfault.com/img/bVcQFQS'
---

<div>   
<p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQFQS" alt="npm-yarn-lock" title="npm-yarn-lock" referrerpolicy="no-referrer"></span></p><h2>前言</h2><p>看完本文，你将从整体了解依赖版本锁定原理，<code>package-lock.json</code> 或 <code>yarn.lock</code> 的重要性。首先要从最近接连出现两起有关 <code>npm</code> 安装 <code>package.json</code> 中依赖包，由于依赖包版本更新 <code>bug</code> 造成项目出错问题说起。</p><h3>事件一：新版本依赖包本身 bug</h3><p>项目本地打包正常，但是线上使用 <code>Jenkins</code> 完成 <code>DevOps</code> 交付流水线打包出错问题。报出如下错误：</p><pre><code class="js">**17:15:32**  ERROR in ./node_modules/clipboard/dist/clipboard.js
**17:15:32**  Module build failed (from ./node_modules/babel-loader/lib/index.js):
**17:15:32**  Error: Couldn't find preset "@babel/env" relative to directory "/app/workspace/SIT/node_modules/clipboard"</code></pre><p>显示错误原因是 <code>clipboard</code> 插件没有安装 <code>@babel/env</code> 预设（<code>preset</code>）。明显这个是插件问题了，去官方库 <a href="https://github.com/zenorocha/clipboard.js" rel="nofollow"><code>clipboard</code></a> 查看源码发现该库依赖包很少，大部分是原生实现。再看 <code>issue</code> 别人有没有出现同样的问题，目前来看还没有人提出。以此推断可能是插件本身的 "问题" 了。</p><p>但是我本地项目打包正常，线上的出错，可能由于本地版本和线上版本不一致导致（某个小版本出现的 <code>bug</code>）的。通过查看<code>package.json</code> 配置的 <code>clipboard: "^2.0.4"</code>，线上实际安装版本是 <code>2.0.7</code>，而我本地实际安装版本是 <code>2.0.6</code><br>因此定位到 <code>2.0.7</code> 出现的 “问题”。</p><p>由于是插件本身“问题”，我的临时解决办法是锁定到 <code>2.0.4</code> 版本，也就是 <code>clipboard: "2.0.4"</code>，后面加上 <code>package-lock.json</code>。</p><p><strong>打破沙锅问到底</strong><br>既然“问题”已经定位到了 <code>2.0.7</code> 版本，进一步通过对比此次版本提交文件内容差异，发现 <code>.babelrc</code> 文件用到的 <code>preset</code> 是 <code>env</code>。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQFQ8" alt="clipboard2.0.6" title="clipboard2.0.6" referrerpolicy="no-referrer"></span></p><p><code>2.0.7</code> 版本用的是 <code>@bable/env</code>，将 <code>babel</code> 更新到了 7！</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQFWG" alt="clipboard2.0.7" title="clipboard2.0.7" referrerpolicy="no-referrer"></span></p><p>问题基本定位到了，这里就顺便给作者提了一个 <a href="https://github.com/zenorocha/clipboard.js/issues/745" rel="nofollow"><code>issues</code></a>。</p><h3>事件二：依赖包的新版插件 bug</h3><p>一直正常使用的 <code>braft-editor</code> 优秀的富文本编辑器插件，最近在其他小伙伴电脑或者在我本地电脑重新部署项目，启动后发现 <code>toHtml()</code> 方法获取富文本 <code>html</code> 内容总是空！</p><p>历史版本是正常的，猜测可能又是版本更新造成。同样的，去官方库 <a href="https://github.com/margox/braft-editor" rel="nofollow">braft-editor</a>看看 <code>issues</code> 别人有没有遇到同样的问题。果然这次有，原因是它的依赖包 <a href="https://github.com/facebook/draft-js" rel="nofollow"><code>draft-js</code></a> 更新后的问题，具体的看这个 <a href="https://github.com/margox/braft-editor/issues/847" rel="nofollow"><code>issues</code></a>。</p><p>这个是由于插件的依赖包更新出现的问题，直接去锁定当前插件没有作用，不会对它的依赖包产生约束（依赖包还是会去下载最新版本的包）。我的临时解决办法是尝试将版本回退到后一个版本并锁定。这样做的原因是回退版本的依赖包版本肯定会低于现在的，之前的版本是正常的。</p><h3>经验教训</h3><p>其实这两起事件是同一个诱因导致的：没有锁定当前项目依赖树模块的版本。下面就来探究一下依赖包的版本管理。</p><h2>语义化版本（semver）</h2><p><code>package.json</code> 在前端工程化中主要用来记录依赖包名称、版本、运行指令等信息字段。其中，<code>dependencies</code> 字段指定了项目运行所依赖的模块，<code>devDependencies</code> 指定项目开发所需要的模块。<br>它们都指向一个对象。该对象的各个成员，分别由模块名和对应的版本要求组成，表示依赖的模块及其版本范围。对应的版本可以加上各种限定，主要有以下几种：</p><ul><li>指定版本：比如 <code>1.2.2</code> ，遵循“大版本.次要版本.小版本”的格式规定，安装时只安装指定版本。</li><li>波浪号（<code>tilde</code>）+指定版本：比如 <code>~1.2.2</code> ，表示安装 <code>1.2.x</code> 的最新版本（不低于<code>1.2.2</code>），但是不安装 <code>1.3.x</code>，也就是说安装时不改变大版本号和次要版本号。</li><li>插入号（<code>caret</code>）+指定版本：比如 <code>ˆ1.2.2</code>，表示安装 <code>1.x.x</code> 的最新版本（不低于 <code>1.2.2</code>），但是不安装 <code>2.x.x</code>，也就是说安装时不改变大版本号。需要注意的是，如果大版本号为 0，则插入号的行为与波浪号相同，这是因为此时处于开发阶段，即使是次要版本号变动，也可能带来程序的不兼容。</li><li>latest：安装最新版本。</li></ul><p>当我们使用比如 <code>npm install package -save</code> 安装一个依赖包时，版本是插入号形式。这样每次重新安装依赖包 <code>npm install</code> 时”次要版本“和“小版本”是会拉取最新的。一般的，主版本不变的情况下，不会带来核心功能变动，<code>API</code> 应该兼容旧版，但是这在开源的世界里很难控制，尤其在复杂项目的众多依赖包中难免会引入一些意想不到的 <code>bug</code>。</p><h2>npm-shrinkwrap && package-lock</h2><h3>npm-shrinkwrap</h3><p>正是存在这每次重新安装，依赖树模块版本存在的不确定性，才有了相应的锁定版本机制。</p><p><code>npm5</code> 之前可以通过 <code>npmshrinkwrap</code> 实现。通过运行 <code>npm shrinkwrap</code>，会在当前目录下生成一个 <code>npm-shrinkwrap.json</code> 文件，它是 <code>package.json</code> 中列出的每个依赖项的大型列表，应安装的特定版本，模块的位置（<code>URI</code>），验证模块完整性的哈希，它需要的包列表，以及依赖项列表。运行 <code>npm install</code> 的时候会优先使用 <code>npm-shrinkwrap.json</code> 进行安装，没有则使用 <code>package.json</code> 进行安装。</p><h3>package-lock</h3><p>在 <code>npm5</code> 版本后，当我们运行 <code>npm intall</code> 发现会生成一个新文件 <code>package-lock.json</code>，内容跟上面提到的 <code>npm-shrinkwrap.json</code> 基本一样。</p><pre><code class="js">"vue-loader": &#123;
  "version": "14.2.4",
  "resolved": "https://registry.npmjs.org/vue-loader/-/vue-loader-14.2.4.tgz",
  "integrity": "sha512-bub2/rcTMJ3etEbbeehdH2Em3G2F5vZIjMK7ZUePj5UtgmZSTtOX1xVVawDpDsy021s3vQpO6VpWJ3z3nO8dDw==",
  "dev": true,
  "requires": &#123;
    "consolidate": "^0.14.0",
    "hash-sum": "^1.0.2",
    "loader-utils": "^1.1.0",
    "lru-cache": "^4.1.1",
    "postcss": "^6.0.8",
    "postcss-load-config": "^1.1.0",
    "postcss-selector-parser": "^2.0.0",
    "prettier": "^1.16.0",
    "resolve": "^1.4.0",
    "source-map": "^0.6.1",
    "vue-hot-reload-api": "^2.2.0",
    "vue-style-loader": "^4.0.1",
    "vue-template-es2015-compiler": "^1.6.0"
  &#125;,
  "dependencies": &#123;
    "postcss-load-config": &#123;
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/postcss-load-config/-/postcss-load-config-1.2.0.tgz",
      "integrity": "sha1-U56a/J3chiASHr+djDZz4M5Q0oo=",
      "dev": true,
      "requires": &#123;
        "cosmiconfig": "^2.1.0",
        "object-assign": "^4.1.0",
        "postcss-load-options": "^1.2.0",
        "postcss-load-plugins": "^2.3.0"
      &#125;
    &#125;,
  &#125;
&#125;,</code></pre><p>当项目中已有 <code>package-lock.json</code> 文件，在安装项目依赖时，将以该文件为主进行解析安装指定版本依赖包，而不是使用 <code>package.json</code> 来解析和安装模块。因为 <code>package-lock</code> 为每个模块及其每个依赖项指定了版本，位置和完整性哈希，所以它每次创建的安装都是相同的。 无论你使用什么设备，或者将来安装它都无关紧要，每次都应该给你相同的结果。</p><h3><code>npm5</code> 版本下 <code>install</code> 规则</h3><p><code>npm</code> 并不是一开始就是按照现有这种规则制定的。</p><p><strong><code>5.0.x</code> 版本</strong>：</p><p>不管 <code>package.json</code> 中依赖是否有更新，<code>npm install</code> 都会根据 <code>package-lock.json</code> 下载。针对这种安装策略，有人提出了这个 <a href="https://github.com/npm/npm/issues/16866" rel="nofollow">issue</a> ，然后就演变成了 <code>5.1.0</code> 版本后的规则。</p><p><strong><code>5.1.0</code> 版本后</strong>：</p><p>当 <code>package.json</code> 中的依赖项有新版本时，<code>npm install</code> 会无视 <code>package-lock.json</code> 去下载新版本的依赖项并且更新 p<code>ackage-lock.json</code>。针对这种安装策略，又有人提出了一个 <a href="https://github.com/npm/npm/issues/17979" rel="nofollow">issue</a> 参考 <code>npm</code> 贡献者 <code>iarna</code> 的评论，得出 <code>5.4.2</code> 版本后的规则。</p><p><strong><code>5.4.2</code> 版本后</strong>：</p><p>如果只有一个 <code>package.json</code> 文件，运行 <code>npm install</code> 会根据它生成一个 <code>package-lock.json</code> 文件，这个文件相当于本次 <code>install</code> 的一个快照，它不仅记录了 <code>package.json</code> 指明的直接依赖的版本，也记录了间接依赖的版本。</p><p>如果 <code>package.json</code> 的 <code>semver-range version</code> 和 <code>package-lock.json</code> 中版本兼容(<code>package-lock.json</code> 版本在 <code>package.json</code> 指定的版本范围内)，即使此时 <code>package.json</code> 中有新的版本，执行 <code>npm install</code> 也还是会根据 <code>package-lock.json</code> 下载。</p><p>如果手动修改了 <code>package.json</code> 的 <code>version ranges</code>，且和 <code>package-lock.json</code> 中版本不兼容，那么执行 <code>npm install</code> 时 <code>package-lock.json</code> 将会更新到兼容 <code>package.json</code> 的版本。</p><h2>yarn</h2><p><code>yarn</code> 的出现主要目标是解决上面描述的由于语义版本控制而导致的 <code>npm</code> 安装的不确定性问题。虽然可以使用 <code>npm shrinkwrap</code> 来实现可预测的依赖关系树，但它并不是默认选项，而是取决于所有的开发人员知道并且启用这个选项。<br><code>yarn</code> 采取了不同的做法。每个 <code>yarn</code> 安装都会生成一个类似于<code>npm-shrinkwrap.json</code> 的 <code>yarn.lock</code> 文件，而且它是默认创建的。除了常规信息之外，<code>yarn.lock</code> 文件还包含要安装的内容的校验和，以确保使用的库的版本相同。</p><h3>yarn 的主要优化</h3><p><code>yarn</code> 的出现主要做了如下优化：</p><ul><li><strong>并行安装</strong>：无论 <code>npm</code> 还是 <code>yarn</code> 在执行包的安装时，都会执行一系列任务。<code>npm</code> 是按照队列执行每个 <code>package</code>，也就是说必须要等到当前 <code>package</code> 安装完成之后，才能继续后面的安装。而 <code>yarn</code> 是同步执行所有任务，提高了性能。</li><li><strong>离线模式</strong>：如果之前已经安装过一个软件包，用 <code>yarn</code> 再次安装时之间从缓存中获取，就不用像 <code>npm</code> 那样再从网络下载了。</li><li><strong>安装版本统一</strong>：为了防止拉取到不同的版本，<code>yarn</code> 有一个锁定文件 (<code>lock file</code>) 记录了被确切安装上的模块的版本号。每次只要新增了一个模块，<code>yarn</code> 就会创建（或更新）<code>yarn.lock</code> 这个文件。这么做就保证了，每一次拉取同一个项目依赖时，使用的都是一样的模块版本。</li><li><strong>更好的语义化</strong>： <code>yarn</code> 改变了一些 <code>npm</code> 命令的名称，比如 <code>yarn add/remove</code>，比 <code>npm</code> 原本的 <code>install/uninstall</code> 要更清晰。</li></ul><h2>安装依赖树流程</h2><ol><li>执行工程自身 <code>preinstall</code>。<br>当前 <code>npm</code> 工程如果定义了 <code>preinstall</code> 钩子此时会被执行。</li><li>确定首层依赖。<br>模块首先需要做的是确定工程中的首层依赖，也就是 <code>dependencies</code> 和 <code>devDependencies</code> 属性中直接指定的模块（假设此时没有添加 <code>npm install</code> 参数）。工程本身是整棵依赖树的根节点，每个首层依赖模块都是根节点下面的一棵子树，<code>npm</code> 会开启多进程从每个首层依赖模块开始逐步寻找更深层级的节点。</li><li><p>获取模块。<br>获取模块是一个递归的过程，分为以下几步：</p><ul><li>获取模块信息。在下载一个模块之前，首先要确定其版本，这是因为 <code>package.json</code> 中往往是 <code>semantic version</code>（<code>semver</code>，语义化版本）。此时如果版本描述文件（<code>npm-shrinkwrap.json</code> 或 <code>package-lock.json</code>）中有该模块信息直接拿即可，如果没有则从仓库获取。如 <code>package.json</code> 中某个包的版本是 <code>^1.1.0</code>，<code>npm</code> 就会去仓库中获取符合 <code>1.x.x</code> 形式的最新版本。</li><li>获取模块实体。上一步会获取到模块的压缩包地址（<code>resolved</code> 字段），<code>npm</code> 会用此地址检查本地缓存，缓存中有就直接拿，如果没有则从仓库下载。</li><li>查找该模块依赖，如果有依赖则回到第 <code>1</code> 步，如果没有则停止。</li></ul></li><li>模块扁平化（<code>dedupe</code>）。<br>上一步获取到的是一棵完整的依赖树，其中可能包含大量重复模块。比如 <code>A</code> 模块依赖于 <code>loadsh</code>，<code>B</code> 模块同样依赖于 <code>lodash</code>。在 <code>npm3</code> 以前会严格按照依赖树的结构进行安装，因此会造成模块冗余。<code>yarn</code> 和从 <code>npm5</code> 开始默认加入了一个 <code>dedupe</code> 的过程。它会遍历所有节点，逐个将模块放在根节点下面，也就是 <code>node-modules</code> 的第一层。当发现有重复模块时，则将其丢弃。这里需要对重复模块进行一个定义，它指的是模块名相同且 <code>semver</code> 兼容。每个 <code>semver</code> 都对应一段版本允许范围，如果两个模块的版本允许范围存在交集，那么就可以得到一个兼容版本，而不必版本号完全一致，这可以使更多冗余模块在 <code>dedupe</code> 过程中被去掉。</li><li>安装模块。<br>这一步将会更新工程中的 <code>node_modules</code>，并执行模块中的生命周期函数（按照 <code>preinstall</code>、<code>install</code>、<code>postinstall</code> 的顺序）。</li><li>执行工程自身生命周期。<br>当前 <code>npm</code> 工程如果定义了钩子此时会被执行（按照 <code>install</code>、<code>postinstall</code>、<code>prepublish</code>、<code>prepare</code> 的顺序）。</li></ol><h2>举例说明</h2><p>插件 <code>htmlparser2@^3.10.1</code> 和 <code>dom-serializer@^0.2.2</code> 都有使用了 <code>entities</code> 依赖包，不过使用的版本不同，同时我们自己安装一个版本的 <code>entities</code> 包。具体如下：</p><pre><code class="js">--htmlparser2@^3.10.1
  |--entities@^1.1.1

--dom-serializer@^0.2.2
  |--entities@^2.0.0

--entities@^2.1.0</code></pre><p>通过 <code>npm install</code> 安装后，生成的 <code>package-lock.json</code> 文件内容和它的 <code>node_modules</code> 目录结构：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQFTa" alt="npm-version" title="npm-version" referrerpolicy="no-referrer"></span></p><p>可以发现：</p><ol><li><code>dom-serializer@^0.2.2</code> 的依赖包 <code>entities@^2.0.0</code> 和我们自己安装的 <code>entities@^2.1.0</code> 被实际安装成 <code>entities@^2.2.0</code>，并放在 <code>node_modules</code> 的第一层。因为这两个版本的<code>semver</code> 范围相同，又先被遍历，所有会被合并安装在第一层；</li><li><code>htmlparser2@^3.10.1</code> 的依赖包 <code>entities@^1.1.1</code> 被实际安放在 <code>dom-serializer</code> 包的 <code>node_modules</code> 中，并且和 <code>package-lock.json</code> 描述结构保持一致。</li></ol><p>通过 <code>yarn</code> 安装后，生成的 <code>yarn.lock</code> 文件内容和它的 <code>node_modules</code> 目录结构：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQFTb" alt="yarn-version" title="yarn-version" referrerpolicy="no-referrer"></span></p><p>可以发现与 <code>npm install</code> 不同的是：</p><ol><li><code>yarn.lock</code> 中所有依赖描述都是扁平化的，即没有依赖描述的嵌套关系；</li><li>在 <code>yarn.lock</code> 中， 相同名称版本号不同的依赖包，如果 <code>semver</code> 范围相同会被合并，否则，会存在多个版本描述。</li></ol><h3>注意 cnpm 不支持 package-lock</h3><p>使用 <code>cnpm install</code> 时候，并不会生成 <code>package-lock.json</code> 文件。<code>cnpm install</code> 的时候，就算你项目中有 <code>package-lock.json</code> 文件，<code>cnpm</code> 也不会识别，仍会根据 <code>package.json</code> 来安装。所以这就是为什么之前你用 <code>npm</code> 安装产生了 <code>package-lock.json</code>，后面的人用 <code>cnpm</code> 来安装，可能会跟你安装的依赖包不一致。</p><p>因此，尽量不要直接使用 <code>cnpm install</code> 安装项目依赖包。但是为了解决直接使用 <code>npm install</code> 速度慢的问题，可以设置 <code>npm</code> 代理解决。</p><pre><code class="js">// 设置淘宝镜像代理
npm config set registry https://registry.npm.taobao.org

// 查看已设置代理
npm config get registry</code></pre><p>当然，也可以通过 <a href="https://www.npmjs.com/package/nrm" rel="nofollow"><code>nrm</code></a> 工具，快捷操作设置代理。</p><p>全局安装</p><pre><code class="js">$ npm install -g nrm</code></pre><p>查看已安装代理列表</p><pre><code class="js">$ nrm ls

* npm -----  https://registry.npmjs.org/
  yarn ----- https://registry.yarnpkg.com
  cnpm ----  http://r.cnpmjs.org/
  taobao --  https://registry.npm.taobao.org/
  nj ------  https://registry.nodejitsu.com/
  skimdb -- https://skimdb.npmjs.com/registry</code></pre><p>切换代理</p><pre><code class="js">$ nrm use cnpm  //switch registry to cnpm

* Registry has been set to: http://r.cnpmjs.org/</code></pre><p>测速</p><pre><code class="js">nrm test cnpm

* cnpm --- 618ms</code></pre><h2>总结</h2><p>项目在以后重新构建，由于依赖树中有版本更新，造成意外事故是不可避免的，究其原因是整个依赖树版本没有锁死。解决方案分为如下四种：</p><ul><li><code>package.json</code> 中固定版本。注意：仅能锁定当前依赖包版本，不能控制整棵依赖树版本。</li><li><code>npm+npm-shrinkwrap.json</code>。</li><li><code>npm+package-lock.json</code>。</li><li><code>yarn+yarn-lock.json</code>。</li></ul><p>根据自身情况选择。<br>见识有限，欢迎指正，谢谢点赞，完～</p>  
</div>
            