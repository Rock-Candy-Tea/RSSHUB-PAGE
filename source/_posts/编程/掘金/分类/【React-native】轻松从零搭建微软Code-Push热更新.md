
---
title: '【React-native】轻松从零搭建微软Code-Push热更新'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6995046360080728095'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 21:53:39 GMT
thumbnail: 'https://juejin.cn/post/6995046360080728095'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">总体步骤：</h2>
<blockquote>
<ol>
<li>前提：需要 mac 电脑（iOS需要，仅安卓Win亦可），RN iOS/android 环境搭建好，服务器一台（最好linux），mysql 数据库以及 git 和 npm 环境。</li>
<li>搭建服务器，下载code-push项目，npm install安装，配置数据库，生成数据库表。</li>
<li>打开阿里云3000端口，运行测试。</li>
<li>本地安装code-push-cli，获取token，推送应用。</li>
<li>安装code-push，npm install react-native-code-push，react-native link react-native-code-push，输入app token即可。</li>
<li>iOS配置Release与Debug版本token，android配置URL。</li>
<li>运行推送测试。</li>
</ol>
</blockquote>
<hr>
<p>那么，既然是全解，肯定是要一步一步搭建。  </p>
<p>第一步，安装 mysql 可以搜索 Linux 下 yum 安装 mysql，这教程很多，我这里就不说了（什么，你说的一步一步来啊？?）</p>
<hr>
<h3 data-id="heading-1">二，搭建服务器 </h3>
<p>首先，要下载热更新的包到服务器上，这里使用git的方式下载，进入服务器，创建一个文件夹：</p>
<pre><code class="copyable">// 创建热更新文件夹
mkdir code-push
// 进入
cd code-push
// 创建热更新存储文件夹
mkdir code-push-file
// 进入
cd code-push-file
// 创建热更新存储文件夹，后续会用到
mkdir storage
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2369c6ae69eb48b2a699fbca8622ec0c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后使用如下命令，下载热更新代码：</p>
<pre><code class="copyable">git clone https://github.com/lisong/code-push-server.git
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f22b8142d1a499489a687a8d246156d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着，进入 code-push-server 然后安装依赖，命令如下：</p>
<pre><code class="copyable">cd code-push-server && npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 运行结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7633cfb406a549648df32b561245e18d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装完毕后，需要修改配置文件，链接到数据库创建表，这里修改config/config.js文件如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  db: &#123;
    <span class="hljs-attr">username</span>: process.env.RDS_USERNAME || <span class="hljs-string">"用户名"</span>,
    <span class="hljs-attr">password</span>: process.env.RDS_PASSWORD || <span class="hljs-string">"密码"</span>,
    <span class="hljs-attr">database</span>: process.env.DATA_BASE || <span class="hljs-string">"codepush"</span>,
    <span class="hljs-attr">host</span>: process.env.RDS_HOST || <span class="hljs-string">"数据库域名"</span>,
    <span class="hljs-attr">port</span>: process.env.RDS_PORT || <span class="hljs-number">3306</span>,
    <span class="hljs-attr">dialect</span>: <span class="hljs-string">"mysql"</span>,
    <span class="hljs-attr">logging</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">operatorsAliases</span>: <span class="hljs-literal">false</span>,
  &#125;
  <span class="hljs-attr">local</span>: &#123;
    <span class="hljs-comment">// 如下存储路径修改为自己的存储路径，第二部中创建的路径 pwd 后 copy 过来</span>
    <span class="hljs-attr">storageDir</span>: process.env.STORAGE_DIR || <span class="hljs-string">"/root/app/code-push/code-push-file/storage"</span>,
    <span class="hljs-comment">// Binary files download host address which Code Push Server listen to. the files storage in storageDir.</span>
    <span class="hljs-attr">downloadUrl</span>: process.env.LOCAL_DOWNLOAD_URL || <span class="hljs-string">"http://服务器域名:3000/download"</span>,
    <span class="hljs-comment">// public static download spacename.</span>
    <span class="hljs-attr">public</span>: <span class="hljs-string">'/download'</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>配置完毕后，执行以下命令创建数据库的表：</p>
<pre><code class="copyable">// 执行脚本创建数据库
./bin/db init --dbhost localhost --dbuser 用户名 --dbpassword 密码

eg..
./bin/db init --dbhost 127.0.0.1 --dbuser root --dbpassword  root
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 至此，如果没有报错的话，服务器搭建就完毕了，比较傻瓜式。</p>
<hr>
<h3 data-id="heading-2">三，打开阿里云3000端口且运行测试 </h3>
<p>如下图，进入ECS实例后，依次点击 <strong>【更多】</strong> -> <strong>【网络和安全组】</strong> -> <strong>【安全组配置】</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e75db3acfa6244a892244cc04c48ebc3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 如下图，点击 <strong>【配置规则】</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1083e37e4c99475e8676d1c32a9a8ab4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 随便点击一个克隆，然后改为3000即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baf0b80520694f8db931a1a90902986d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如下图，修改为3000即可。 </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb504878eb5d43e191bb7ee877f62e61~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>输入网址进行测试：</p>
<p>如下图，点击 <strong>【登录】</strong> 后，输入账户：admin，密码：123456进行登录。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1442a3815b5246d0a9859dd29113fa02~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 登录成功后，可以点击获取 token 来获得 token 秘钥，用于后面的认证以及修改当前登录账户密码等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43370838106146828d4258427d2545b9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 至此，热更新后端搭建完毕~~~</p>
<hr>
<h3 data-id="heading-3">四，本地搭建code-push-cli环境创建推送应用</h3>
<ul>
<li>安装 code-push-cli 工具</li>
</ul>
<pre><code class="copyable">npm install -g code-push-cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>查看当前登录用户</li>
</ul>
<pre><code class="copyable">code-push whoami
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果显示邮箱则已登录，否则，使用如下命令进行登录 ：</p>
<pre><code class="copyable">// localhost改为热更新服务器域名
code-push login http://localhost:3000
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 此步会跳转到浏览器，登录后获取 token，放入【<strong>终端】</strong> 窗口即可</p>
<ul>
<li>创建应用</li>
</ul>
<p>如下图，创建了一个名为 test-android 的 android 系统应用，对应平台为 RN</p>
<pre><code class="copyable">// code-push app add 应用名 版本 平台
code-push app add test-android android react-native
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>查看当前已创建 app 应用列表 </li>
</ul>
<pre><code class="copyable">code-push app list
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里创建了四个应用，对应的 <strong>【Prodcutin】</strong> 和 <strong>【Staging】</strong> 分别为 <strong>【生产】</strong> 与 <strong>【测试】</strong> 版本 </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda69c956c0a45f1b1ecb8533a6e72df~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>查看已应用对应的 key 值 </li>
</ul>
<pre><code class="copyable">code-push deployment ls 《应用名》 -k
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a1af8cf57c64104bb6e029fcec92998~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>更多命令，可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsupervons%2FcommonProject%2Ftree%2Fmaster%2FcommonPage%2FComponents%2FCodePush" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/supervons/commonProject/tree/master/commonPage/Components/CodePush" ref="nofollow noopener noreferrer">【我的github】</a>，至此，本地环境搭建完毕，已经可以创建 app 应用，那么，喝口水，接着往下走 。</p>
<hr>
<h3 data-id="heading-4">五，项目内安装 code-push </h3>
<p>进入项目中，输入：</p>
<pre><code class="copyable">// 安装热更新服务
npm install react-native-code-push --save
// 关联项目
react-native link react-native-code-push
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在link时，会提示输入相对应的key，也就是第四步 <strong>【查看已应用对应的 key 值 】</strong> 中获取到的 key。</p>
<p>接下来，还需要改一些设置。</p>
<ul>
<li>android：</li>
</ul>
<p>版本号改为三位</p>
<pre><code class="copyable">    defaultConfig &#123;
        versionName "1.0.0"
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <strong>MainApplication.java</strong> 中 getPackages 方法中</p>
<pre><code class="copyable">new CodePush(getResources().getString(R.string.reactNativeCodePush_androidDeploymentKey), getApplicationContext(), BuildConfig.DEBUG, "http://你的域名:3000/"),
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>iOS</li>
</ul>
<p>点击新增自定义设置</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64402e17d0294e6fb2a8b63f4c991fcc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新增如下： </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e94fade7d714788a50454647cf09f62~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 在 info.plist中增加：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59efcacde48645c6996eae785839e1cb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，项目配置到这里，就结束了，接下来，让我们在 RN 中添加热更新的代码。 </p>
<ul>
<li>配置更新代码： </li>
</ul>
<p>在入口（通常是 APP.js）文件中导入codepush库</p>
<pre><code class="copyable">import CodePush from "react-native-code-push";
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加监听 ，这里弹出提示框，默认是英文的，修改了 updateDialog 中的参数后，可以改成想要的文字。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 热更新检测</span>
        CodePush.sync(
            &#123;
                <span class="hljs-attr">updateDialog</span>: &#123;
                    <span class="hljs-attr">optionalIgnoreButtonLabel</span>: <span class="hljs-string">'下次再说'</span>,
                    <span class="hljs-attr">optionalInstallButtonLabel</span>: <span class="hljs-string">'马上体验'</span>,
                    <span class="hljs-attr">optionalUpdateMessage</span>: <span class="hljs-string">'新版本来袭，是否更新'</span>,
                    <span class="hljs-attr">title</span>: <span class="hljs-string">'更新提示'</span>,
                    <span class="hljs-attr">mandatoryUpdateMessage</span>: <span class="hljs-string">'噢，版本中有一些大改动，不得不更新'</span>,
                    <span class="hljs-attr">mandatoryContinueButtonLabel</span>: <span class="hljs-string">'立即更新'</span>
                &#125;,
                <span class="hljs-attr">installMode</span>: CodePush.InstallMode.IMMEDIATE
            &#125;,
            <span class="hljs-built_in">this</span>.codePushStatusDidChange.bind(<span class="hljs-built_in">this</span>),
            <span class="hljs-built_in">this</span>.codePushDownloadDidProgress.bind(<span class="hljs-built_in">this</span>)
        );
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如下为对不同状态的监听，可以用于后续增加用户点击更新后的进度条</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">codePushStatusDidChange</span>(<span class="hljs-params">syncStatus</span>)</span> &#123;
        <span class="hljs-keyword">switch</span> (syncStatus) &#123;
            <span class="hljs-keyword">case</span> CodePush.SyncStatus.CHECKING_FOR_UPDATE:
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">syncMessage</span>: <span class="hljs-string">"Checking for update."</span>&#125;);
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> CodePush.SyncStatus.DOWNLOADING_PACKAGE:
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">syncMessage</span>: <span class="hljs-string">"Downloading package."</span>&#125;);
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> CodePush.SyncStatus.AWAITING_USER_ACTION:
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">syncMessage</span>: <span class="hljs-string">"Awaiting user action."</span>&#125;);
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> CodePush.SyncStatus.INSTALLING_UPDATE:
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">syncMessage</span>: <span class="hljs-string">"Installing update."</span>&#125;);
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> CodePush.SyncStatus.UP_TO_DATE:
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">syncMessage</span>: <span class="hljs-string">"App up to date."</span>, <span class="hljs-attr">progress</span>: <span class="hljs-literal">false</span>&#125;);
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> CodePush.SyncStatus.UPDATE_IGNORED:
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">syncMessage</span>: <span class="hljs-string">"Update cancelled by user."</span>, <span class="hljs-attr">progress</span>: <span class="hljs-literal">false</span>&#125;);
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> CodePush.SyncStatus.UPDATE_INSTALLED:
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">syncMessage</span>: <span class="hljs-string">"Update installed and will be applied on restart."</span>, <span class="hljs-attr">progress</span>: <span class="hljs-literal">false</span>&#125;);
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> CodePush.SyncStatus.UNKNOWN_ERROR:
                <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">syncMessage</span>: <span class="hljs-string">"An unknown error occurred."</span>, <span class="hljs-attr">progress</span>: <span class="hljs-literal">false</span>&#125;);
                <span class="hljs-keyword">break</span>;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">codePushDownloadDidProgress</span>(<span class="hljs-params">progress</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;progress&#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-5"><strong>六，推送及更新测试</strong> </h3>
<ul>
<li>Android </li>
</ul>
<pre><code class="copyable">code-push release-react 《应用名》 android -t "1.0.0" --des "测试热更新" -d Staging
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>android 可以打包后，进行测试，是否是正式环境按配置的 key 来判断 </p>
<ul>
<li> iOS</li>
</ul>
<pre><code class="copyable">code-push release-react 《应用名》 ios -t "1.0.0" --des "测试热更新" -d Staging
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>iOS 如果是用虚拟机的话，则推送到 Staging 环境即可，因虚拟机有 node 服务，看不出来，故可以进行如下设置，以Release 启动，所以上面的 Staging 改成 Production 即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6f6709bac3d4b61aca1c7e5005b6858~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>检测到更新如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7619bfaeb1344fc1804a14a22ecb177d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果需要清空app的更新，用如下命令 </p>
<pre><code class="copyable">code-push deployment clear <appName> Production or Staging
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995046360080728095" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr></div>  
</div>
            