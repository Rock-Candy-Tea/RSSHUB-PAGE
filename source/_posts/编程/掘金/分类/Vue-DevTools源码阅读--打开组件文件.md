
---
title: 'Vue-DevTools源码阅读--打开组件文件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8264803da804e4a9b0e43833f393cff~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 09:54:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8264803da804e4a9b0e43833f393cff~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<h3 data-id="heading-0">很感谢若川大佬组织的源码阅读小组活动</h3>
<p>每天下班后逼自己学习学习</p>
<p>以下为若川原文：<a href="https://juejin.cn/post/6959348263547830280#heading-2" target="_blank" title="https://juejin.cn/post/6959348263547830280#heading-2">juejin.cn/post/695934…</a></p>
</blockquote>
<h3 data-id="heading-1">什么是Vue-DevTools？</h3>
<p>作为一个Vue开发者（不是），自然少不了Chrome中的Vue调试插件。</p>
<p>Vue-DevTools是一个可以在Chrome中进行Vue项目调试的工具，可以帮助开发者在使用Vue开发时，更清楚的了解目前页面中的组件、数据情况。</p>
<p>目前该插件有两个版本，支持Vue3的Beta版本，和支持Vue2的版本。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8264803da804e4a9b0e43833f393cff~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">要了解什么？</h3>
<p>这次主要了解在新版本DevTools中支持了一个新特性：在选择对应的组件后，点击<code>open-in-editor</code>的按钮后，即可在编译器中打开对应的组件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4a5274aa01d4bfb89259ee898e752c3~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">实现原理：</h3>
<p>主要通过<code>launch-editor-middleware和launch-editor</code>两个库实现了该功能，这两个库又通过调用node的<code>process、child_process</code>能力，创建一个node的子进程调起编译器打开选中的组件</p>
<h3 data-id="heading-4">阅读前准备：</h3>
<ol>
<li>在Chrome中准备支持Vue3的最新版本插件（目前最新版本号6.0.0 beta 15）</li>
<li><code>vue create</code> 创建一个vue-cli3项目</li>
<li>准备一个编译器</li>
</ol>
<h3 data-id="heading-5">开始调试：</h3>
<blockquote>
<p>Open in editor在Vue3中是一个开箱即用的功能</p>
<p>具体如何配置使用：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevtools.vuejs.org%2Fguide%2Fopen-in-editor.html" target="_blank" rel="nofollow noopener noreferrer" title="https://devtools.vuejs.org/guide/open-in-editor.html" ref="nofollow noopener noreferrer">Open component in editor</a></p>
</blockquote>
<h4 data-id="heading-6">1.寻找入口，进行调试</h4>
<h5 data-id="heading-7">1.1寻找入口</h5>
<p>根据上述文档的项目引入配置，需要在编译器中搜索<code>'/__open-in-editor'</code>，即可在<code>node_modules</code> 中定位到该方法，此时在此处打个点~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1111a85d7f584419a4c25f3208001a51~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再继续进入<code>launchEditorMiddleware</code> 发现这个中间件会调用<code>launch-editor</code>进行后续的打开编译器操作，此时可以在调用launch函数这行打上一个点~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a138154cc357433b8a5934e72a036540~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-8">1.2启动调试</h5>
<p>以Vscode为例：</p>
<p>进入项目的<code>package.json</code>，可以看到在<code>script</code>属性上有一个“调试”或“debug”的按钮，点击后选择<code>serve</code>即可进入调试模式</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d227e2411e854e939247ed183c9169b1~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在这里我踩了一个小坑（也是因为自己不够谨慎）</p>
<p>在npm i完成之后，先npm run serve在8080端口启动了项目，再点击调试</p>
<p>这会造成编译器再开启一个进程在8081端口启动项目，这也许会让你在后续调试时发现无法进入断点处</p>
<p>此时需要注意调试启动的项目端口是否与浏览器端口一致</p>
</blockquote>
<p>接下来就进入到阅读源码部分~</p>
<h3 data-id="heading-9">开始阅读：</h3>
<h4 data-id="heading-10">1.launchEditorMiddleware部分</h4>
<p>在项目开始编译时，就会自动进入该部分代码。</p>
<blockquote>
<p>个人理解在这部分代码中主要做了两件事：</p>
<p>1.函数重载，满足不同开发传参需求</p>
<p>2.通过node.js获取当前进程所在的位置，为后续打开编译器做准备</p>
</blockquote>
<pre><code class="copyable">// serve.js
app.use('/__open-in-editor', launchEditorMiddleware(() => console.log(
  `To specify an editor, specify the EDITOR env variable or ` +
  `add "editor" field to your Vue project config.\n`
)))

//launch-editor-middleware/index.js
module.exports = (specifiedEditor, srcRoot, onErrorCallback) => &#123;
  //这里对传入的第一个参数做一个判断，如果该参数为函数，则将这个参数与错误回调函数的值进行对调
  if (typeof specifiedEditor === 'function') &#123;
      onErrorCallback = specifiedEditor
      specifiedEditor = undefined
    &#125;
    //同样对传入的第二个参数也是做同样的判断
  if (typeof srcRoot === 'function') &#123;
    onErrorCallback = srcRoot
    srcRoot = undefined
  &#125;
    //第二个参数如果传入的是目录，则直接用
  //如果不是则调用node.js中process的能力，获取当前进程所在的位置
  srcRoot = srcRoot || process.cwd()
  return function launchEditorMiddleware (req, res, next) &#123;
    //返回一个中间件
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">2 launch-editor部分</h4>
<h5 data-id="heading-12">2.1执行前路径的判断</h5>
<p>F12打开Vue-DevTools调试面板，选择一个组件，点击<code>open-in-editor</code>即可进入断点处</p>
<p>此时，如果切换到Chrome的Network栏时，会发现此时浏览器发送了一个请求：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3df5da4e5524881b03e08bcab0eb11e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结合编译前的<code>app.use('/__open-in-editor', launchEditorMiddleware(...)</code>不难知道这是一个中间件的写法，当浏览器发送请求时，就会进入到接下来的代码逻辑中</p>
<pre><code class="copyable">module.exports = (specifiedEditor, srcRoot, onErrorCallback) => &#123;
    // ....省略
  return function launchEditorMiddleware (req, res, next) &#123;
    // 首先会读取路径中的file参数
    const &#123; file &#125; = url.parse(req.url, true).query || &#123;&#125;
    if (!file) &#123;
      res.statusCode = 500
      res.end(`launch-editor-middleware: required query param "file" is missing.`)
    &#125; else &#123;
      // 如果存在该路径，则会执行launch-editor逻辑
      launch(path.resolve(srcRoot, file), specifiedEditor, onErrorCallback)
      res.end()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">2.2执行中最重要的一部分</h5>
<p>进入到<code>launchEditor</code>函数后，也是该功能最重要的一部分</p>
<pre><code class="copyable">function launchEditor (file, specifiedEditor, onErrorCallback) &#123;
  //2.2.1通过正则匹配的方式读取文件路径、行号、列号的信息并进行返回
  const parsed = parseFile(file)
  let &#123; fileName &#125; = parsed
  const &#123; lineNumber, columnNumber &#125; = parsed
    // 2.2.2调用node.js的方法，以同步的方式检测该路径是否存在，不存在就return结束
  if (!fs.existsSync(fileName)) &#123;
    return
  &#125;
    // 这里同样是一个函数重载的方法
  if (typeof specifiedEditor === 'function') &#123;
    onErrorCallback = specifiedEditor
    specifiedEditor = undefined
  &#125;
    // 2.2.3这里跟错误回调调用了一个方法，比较有意思
  onErrorCallback = wrapErrorCallback(onErrorCallback)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.2.3部分，采用了装饰器模式（感谢同组的纪年小姐姐的总结），原理是将要执行的逻辑包裹起来，先执行其他的需要处理的代码，再执行<code>onErrorCallback</code>的逻辑。</p>
<p>继续阅读函数~</p>
<pre><code class="copyable">function wrapErrorCallback (cb) &#123;
  return (fileName, errorMessage) => &#123;
    console.log()
    //这里先做了一个错误的输出，同时调用node.js中path的方法，提取出用"/"隔开的path最后一部分内容共
    //并且用了一个chalk库，可以改变控制台输出内容的颜色
    console.log(
      chalk.red('Could not open ' + path.basename(fileName) + ' in the editor.')
    )
    // 此时如果有错误信息时，才会输出错误信息的提示
    if (errorMessage) &#123;
      if (errorMessage[errorMessage.length - 1] !== '.') &#123;
        errorMessage += '.'
      &#125;
      console.log(
        chalk.red('The editor process exited with an error: ' + errorMessage)
      )
    &#125;
    console.log()
    if (cb) cb(fileName, errorMessage)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若此时在这部分没有报错，则会继续进行接下来的流程。</p>
<p>2.2.4 此时会进入一个很“刺激”的猜测环节</p>
<pre><code class="copyable">//launch-editor/index.js
function launchEditor (file, specifiedEditor, onErrorCallback) &#123;
  ...
    // 此时代码进入猜测函数
  const [editor, ...args] = guessEditor(specifiedEditor)
&#125;

// launch-editor/guess.js
module.exports = function guessEditor (specifiedEditor) &#123;
  // 第一步：判断有没有传入对应的shell命令
  if (specifiedEditor) &#123;
    // 如果传入，利用shell-quote库解析shell命令
    return shellQuote.parse(specifiedEditor)
  &#125;
  // We can find out which editor is currently running by:
  // `ps x` on macOS and Linux
  // `Get-Process` on Windows
  
  // 第二步：猜测环节
  // 上面的三行注释也说明了可以判断当前是在哪个系统环境下运行，从而决定用何种方式启动编译器
  try &#123;
    // 通过node.js中process中标识运行node.js进程的操作系统的方法获取当前的操作系统
    // 因为我的系统是MacOs，直接进入第一个猜测中
    if (process.platform === 'darwin') &#123;
      // 此时调用了同步创建子进程的方法,这里会获取到目前的所有进程
      const output = childProcess.execSync('ps x').toString()
      // COMMON_EDITORS_OSX为一个map表，里面维护着MacOs下支持的编译器，以及对应的字段
      // 通过遍历的方式与当前系统中存在的编译器进行匹配
      const processNames = Object.keys(COMMON_EDITORS_OSX)
      for (let i = 0; i < processNames.length; i++) &#123;
        const processName = processNames[i]
        if (output.indexOf(processName) !== -1) &#123;
          return [COMMON_EDITORS_OSX[processName]]
        &#125;
      &#125;
    &#125;
  // ... 不同平台的我就省略了，原理类似
  // 最后还有一个兜底的方案
  // Last resort, use old skool env vars
  if (process.env.VISUAL) &#123;
    return [process.env.VISUAL]
  &#125; else if (process.env.EDITOR) &#123;
    return [process.env.EDITOR]
  &#125;
  return [null]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.2.5 猜测完之后的操作</p>
<pre><code class="copyable">function launchEditor (file, specifiedEditor, onErrorCallback) &#123;
    // ...
  const [editor, ...args] = guessEditor(specifiedEditor)
  // 如果没有找到，就会报错
  if (!editor) &#123;
    onErrorCallback(fileName, null)
    return
  &#125;
    // 核心部分，根据不同的系统状态，打开调起不同的工具打开编译器
  // childProcess.spawn为异步衍生子进程，并且不会阻塞node.js的事件循环
  if (process.platform === 'win32') &#123;
    // On Windows, launch the editor in a shell because spawn can only
    // launch .exe files.
    _childProcess = childProcess.spawn(
      'cmd.exe',
      ['/C', editor].concat(args),
      &#123; stdio: 'inherit' &#125;
    )
  &#125; else &#123;
    // 因为是MacOs，因此调用Vscode，打开args地址（项目地址），并且子进程将使用父进程的标准输入输出。
    // 这块Node文档参考
    // http://nodejs.cn/api/child_process.html#child_process_child_process_spawn_command_args_options
    // 到这里，对应的组件文件就已经在编译器中被打开了
    _childProcess = childProcess.spawn(editor, args, &#123; stdio: 'inherit' &#125;)
  &#125;
    // 这里是对子进程结束后触发做监听，检测进程退出是否存在异常
  _childProcess.on('exit', function (errorCode) &#123;
    _childProcess = null

    if (errorCode) &#123;
      onErrorCallback(fileName, '(code ' + errorCode + ')')
    &#125;
  &#125;)

  _childProcess.on('error', function (error) &#123;
    onErrorCallback(fileName, error.message)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">总结</h3>
<p>首先小小的表扬一下自己，终于克服了不会读不敢读源码的问题</p>
<p>🎉🎉🎉🎉🎉🎉🎉</p>
<p>以前觉得源码都很难懂，框架也很难了解真正的原理。但是通过这次活动，小小的明白了一个工具中一个小模块的实现方法，很有意思。</p>
<p>也很感谢若川大佬组织这次活动，辛苦了。</p>
<p>这次阅读的过程同时也发现了原来Node可以做很多事情，这也是之前没有了解过的知识点。</p>
<h3 data-id="heading-15">相关文档和资料：</h3>
<p>Vue-DevTools：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fdevtools%23open-component-in-editor" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/devtools#open-component-in-editor" ref="nofollow noopener noreferrer">github.com/vuejs/devto…</a></p>
<p>尤大版本launch-editor：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyyx990803%2Flaunch-editor" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yyx990803/launch-editor" ref="nofollow noopener noreferrer">github.com/yyx990803/l…</a></p>
<p>Umijs/launch-editor：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fumijs%2Flaunch-editor" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/umijs/launch-editor" ref="nofollow noopener noreferrer">github.com/umijs/launc…</a></p></div>  
</div>
            