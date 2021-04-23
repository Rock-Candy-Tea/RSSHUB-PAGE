
---
title: '简简单单才是真，初试 Svelte'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca4bd6a8dd6d4f948cb4ece257770e03~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 18:28:37 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca4bd6a8dd6d4f948cb4ece257770e03~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：<a href="https://juejin.cn/post/www.leancloud.cn">LeanCloud weakish</a></p>
<p>最近团队内部需要一个上传文件的 web 小工具，需要写一个简单的前端页面。 像这样的小工具，如果引入 React 和 Vue，似乎太重了，所以想尝试下 Svelte 这个无框架之框架（最终会编译成不带框架的 JS 代码）。</p>
<p>闲话少叙，直接上手。 首先，生成模板项目：</p>
<pre><code class="copyable">npx degit sveltejs/template fileup
<span class="copy-code-btn">复制代码</span></code></pre>
<p>长期以来 Svelte 的一大痛点是不支持 TypeScript，不过去年开始也加入了 <a href="https://svelte.dev/blog/svelte-and-typescript" target="_blank" rel="nofollow noopener noreferrer">TypeScript 支持</a>。 当然，像这样简单的小工具，直接用 JavaScript 写也没什么差别。 不过我还是打算用下 TypeScript。</p>
<p>和其他一些模板生成工具不同，Svelte 官方没有提供单独的 TypeScript 模板项目仓库，也不会在生成模板的过程中让你选择是用 TypeScript 还是 JavaScript，而是在生成模板项目后，运行一个脚本把项目转成 TypeScript 项目：</p>
<pre><code class="copyable">node scripts/setupTypeScript.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转换之后，执行常规的依赖安装步骤，就可以运行了：</p>
<pre><code class="copyable">npm install
npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目使用 npm 管理依赖，使用 <a href="https://rollupjs.org/guide/en/" target="_blank" rel="nofollow noopener noreferrer">rollup</a> 打包，这些都不用操心，对于简单项目而言，只需修改 <code>src/App.svelte</code> 即可，模板、样式、交互逻辑都写在这一个文件中（这和 Vue 有点像）：</p>
<pre><code class="copyable"><script lang="ts">
// TypeScript 代码
</script>

<style>
/* CSS 代码 */
</style>

<!-- Svelte 模板代码 -->
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先来编写上传界面，google 一下，找到一个现成的组件 <a href="https://github.com/thecodejack/svelte-file-dropzone" target="_blank" rel="nofollow noopener noreferrer">svelte-file-dropzone</a></p>
<pre><code class="copyable">npm i svelte-file-dropzone
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将它加入依赖，在 <code>App.svelte</code> 的 <code>script</code> 部分引入，并编写相应的 TypeScript 代码和 Svelet 模板代码：</p>
<pre><code class="copyable"><script lang="ts">
import Dropzone from "svelte-file-dropzone";

let files: File[]
function handleFilesSelect(e) &#123;
    files = e.detail.acceptedFiles
&#125;
</script>

<Dropzone on:drop=&#123;handleFilesSelect&#125;>
  Click to select files, or drag and drop some files here.
</Dropzone>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取选定的文件之后，再上传文件。 文件会上传到 LeanCloud，<a href="https://www.leancloud.cn/" target="_blank" rel="nofollow noopener noreferrer">LeanCloud</a> 是一家 BaaS 云服务商，也提供文件托管服务。 「svelte」的意思是「slender and elegant」，和「lean」也算是近义词，从这个角度说，这两个听起来还挺配的。</p>
<p>同样，我们先把 LeanCloud 的 JavaScript SDK 加入依赖：</p>
<pre><code class="copyable">npm i leancloud-storage
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后初始化 SDK：</p>
<pre><code class="copyable">import LC from "leancloud-storage";

const appId = "your app id";
const appKey = "your app key";
const serverURL = "https://your-custom-domain.example.com";

LC.init(&#123;
    appId,
    appKey,
    serverURL,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>appID</code> 和 <code>appKey</code> 可以从 「LeanCloud 控制台 > 设置 > 应用 Keys」查看，<code>serverURL</code> 是在 LeanCloud 绑定的域名。 当然，这需要<a href="https://leancloud.cn/docs/dashboard_guide.html#hash767751007" target="_blank" rel="nofollow noopener noreferrer">首先在 LeanCloud 注册账号并创建应用</a>。 应有关部门的要求，LeanCloud 国内版需要绑定已备案的域名，如果不想绑域名或者域名没有备案，可以用 <a href="https://leancloud.app/" target="_blank" rel="nofollow noopener noreferrer">LeanCloud 国际版</a>。</p>
<p>国际版初始化时无需传入 <code>serverURL</code>：</p>
<pre><code class="copyable">LC.init(&#123;
    appId,
    appKey
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上传文件非常简单，只需两行代码：</p>
<pre><code class="copyable">async function uploadFile(toUpload): Promise<String> &#123;
    const uploaded = await new LC.File(toUpload.name, toUpload).save();
    return uploaded.get("url");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中，用 <code>new LC.File(文件名, 文件)</code> 构建文件后，调用 <code>save</code> 方法保存到云端，之后就可以通过 <code>url</code> 属性得到可以访问该文件的 URL。</p>
<p>到目前为止，我们已经完成了最核心的功能，选取文件和上传文件，只剩下最后一步，把获取的 URL 显示给用户了。</p>
<pre><code class="copyable">&#123;#if files&#125;
  <h2>Files</h2>
  &#123;#each files as file, i&#125;
    &#123;#await uploadFile(file)&#125;
      <p>Uploading &#123;file.name&#125; (&#123;file.size&#125; bytes) ...</p>
    &#123;:then url&#125;
      <p>Uploaded:
        <code>&#123;url ?? ""&#125;</code>
      </p>
    &#123;:catch error&#125;
      <pre>&#123;error&#125;</pre>
    &#123;/await&#125;
  &#123;/each&#125;
&#123;/if&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里用到了 Svelte 的模板语法。 估计是为了节省写解析器的功夫，Svelte 的模板语法看起来有点别扭（<code>#if</code>、<code>/if</code>、<code>:catch</code>），但是忽略这些视觉上小小的不适，整体上还是清晰易读的。 先用 <code>if</code> 判断是否选取了文件，只有在选取了文件的情况下，才会显示文件列表。 接着用 <code>each</code> 遍历所有选中文件，进行上传操作，并在上传过程中显示文件的名称和大小，上传完成后则显示文件的 URL。 当然，几乎所有程序都少不了错误处理的部分。 因为这是一个内部工具，所以就直接在网页上显示错误信息了，没额外做更多处理。 注意这里用了 <code>await</code> 等待上传文件的异步函数返回结果，获取到结果后将它赋值给 <code>url</code> 变量，然后就可以直接在界面中使用 <code>url</code> 变量了。</p>
<p>好了，大功告成，不到 50 行代码，就完成了这个简单的上传工具。 回头看看代码，非常直截了当。 但仔细想想，还是很神奇的，比如只是通过 <code>files = e.detail.acceptedFiles</code> 这一行赋值操作，界面就能感知到 <code>files</code> 的变化，相应地渲染不同的内容。 这是因为 Svelte 会把 <code>=</code> 编译为类似 React 等框架中的 <a href="https://lihautan.com/compile-svelte-in-your-head-part-1/#updating-data" target="_blank" rel="nofollow noopener noreferrer">setState</a> 方法。 有些人可能觉得这有些太魔法了，但其实大多数编程语言中 <code>=</code> 就挺魔法的，比如会有 <code>x = x + 1</code>; 这样的语句，只是大家都习惯了而已。</p>
<p>最后需要把它部署到一个地方。 因为是个纯静态页面，所以部署到什么地方都行。 既然文件托管已经用了 LeanCloud，那网页也部署到 LeanCloud 吧。</p>
<p>运行以下命令编译、打包项目：</p>
<pre><code class="copyable">npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后运行以下命令即可部署至 LeanCloud：</p>
<pre><code class="copyable">cd public
lean switch --region CN --group web YOUR_APP_ID
lean deploy --prod 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 <code>CN</code> 表示 LeanCloud 华北节点，<code>web</code> 是云引擎分组的名称，如果使用了其他节点或者 LeanCloud 国际版，或者分组名称不同，需要修改相应的值，具体可以查看「LeanCloud 控制台 > 云引擎 > 云引擎分组 > 部署 > 命令行工具」的说明。</p>
<p>如果没有安装 LeanCloud 命令行工具，需要先<a href="https://leancloud.cn/docs/leanengine_cli.html#hash1443149115" target="_blank" rel="nofollow noopener noreferrer">安装</a>并关联账号，关联账号的步骤同样可以上述控制台区域找到。 另外，要访问部署在云引擎上的页面，还需要<a href="https://leancloud.cn/docs/custom-api-domain-guide.html#hash2145569848" target="_blank" rel="nofollow noopener noreferrer">绑定一个云引擎域名</a>，或者申请一个 <code>avosapps.us</code> 下的子域名（仅限国际版）。</p>
<p>下面是部署后的效果图：</p>
<p><img alt="fileup 界面" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca4bd6a8dd6d4f948cb4ece257770e03~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到，为了方便复制 URL，我加了复制到剪贴板的按钮。 使用 <a href="https://www.npmjs.com/package/svelte-copy-to-clipboard" target="_blank" rel="nofollow noopener noreferrer">svelte-copy-to-clipboard</a> 组件：</p>
<pre><code class="copyable">npm i svelte-copy-to-clipboard
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只需添加 10 行代码：</p>
<pre><code class="copyable"><script lang="ts">
import CopyToClipboard from "svelte-copy-to-clipboard";
// 略

function handleSuccessfulCopy(i) &#123;
    copyStatuses[i] = '✅'
&#125;
function handleFailedCopy(i) &#123;
    copyStatuses[i] = '❌'
&#125;
</script>

<!-- 略 -->
&#123;#if files&#125;
  <h2>Files</h2>
    <!-- 略 -->
    &#123;:then url&#125;
      <p>Uploaded:
        <code>&#123;url ?? ""&#125;</code>
        <CopyToClipboard text=&#123;url&#125; on:copy=&#123;() => handleSuccessfulCopy(i)&#125; on:fail=&#123;() => handleFailedCopy(i)&#125; let:copy>
          <button on:click=&#123;copy&#125;>&#123;copyStatuses[i]&#125;</button>
        </CopyToClipboard>
      </p>
  <!-- 略 -->
&#123;/if&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果希望进一步改善用户体验，还可以在上传时显示进度。 这项改进就留给读者作为练习（<a href="https://leancloud.cn/docs/leanstorage_guide-js.html#hash-924104132" target="_blank" rel="nofollow noopener noreferrer">提示</a>）。</p>
<p>不能免俗，用 LightHouse 跑个分：</p>
<p><img alt="配图2.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0492390b5e4a443d9728606d26f933aa~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>之前写页面的时候我并没有考虑性能，但性能评分仍然达到了 100。 SEO 和可访问性方面有些小问题，改起来不麻烦，同样留给读者作为练习。 好吧，你也许已经发现了，我只是在为我自己的懒惰找借口。 不过，如果你真的完成了这些练习，欢迎来提 <a href="https://github.com/leancloud/fileup/pulls" target="_blank" rel="nofollow noopener noreferrer">pr</a>。</p>
<p>写到这里差不多要结束了，总结一下。 就<a href="https://nextfe.com/svelte-for-sites-react-for-apps/" target="_blank" rel="nofollow noopener noreferrer">小工具和交互不多的站点</a>而言，Svelte 写起来更加直截了当，和 React、Vue 相比，编写的代码更加简明扼要， 套路代码（boilerplate code）更少，编译出的代码更加轻量，因此对个人健康（节省键盘敲击次数，避免肌肉劳损）和世界环境（访问者加载和运行的代码更少，显著降低碳排量）都更友好。 Svelte 这样的无框架（frameless）框架和 LeanCloud 这样的无服务器（serverless）云服务，抽象掉了大量无关业务的细节，可以让开发者专注项目的核心功能，提升开发效率，改善开发体验。</p>
<p>题图 <a href="https://unsplash.com/photos/Vs_zkj1sEHc" target="_blank" rel="nofollow noopener noreferrer">Paul Gilmore</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            