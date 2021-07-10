
---
title: '为网站接入前端异常监控系统 Sentry'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4070018155ac4ae2ada64bfa8ba2a492~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 01:17:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4070018155ac4ae2ada64bfa8ba2a492~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">背景</h4>
<p>众所周知，现在前端异常监控在实际生产环境中越来越重要了。通过给网站接入前端异常监控系统，我们能获得以下几个好处：</p>
<ul>
<li>收集页面的错误信息</li>
<li>辅助定位代码错误位置</li>
<li>在用户报障前发现问题</li>
</ul>
<p>这对于提升线上系统质量，降低线上故障数量，都具有非常重要的意义。相比于等待用户反馈故障，通过接入异常监控系统，能化被动为主动，缩短线上故障处理的流程和时间。</p>

<h4 data-id="heading-1">前端异常监控方案</h4>
<ul>
<li>badjs</li>
<li>fundebug</li>
<li>Sentry</li>
</ul>
<p>目前比较流行的异常监控方案有以上几种，但从易用性、免费与否、以及项目是否开源等方面考虑，个人觉得 Sentry 是个非常不错的选择，服务端部署也非常简单，当然服务端也可以直接使用 Sentry 提供的，网站客户端引入 sentry sdk 并插入初始化 Sentry 的代码就可以实现对页面脚本异常的监控了。</p>
<h4 data-id="heading-2">Sentry 部署</h4>
<h5 data-id="heading-3">安装 Docker</h5>
<pre><code class="copyable">sudo yum remove docker  docker-common docker-selinux docker-engine
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum list docker-ce --showduplicates | sort -r
sudo yum install docker-ce
sudo systemctl start docker
sudo systemctl enable docker

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">Docker 安装 Sentry</h5>
<ol>
<li>拉取 Sentry 仓库</li>
</ol>
<pre><code class="copyable">git clone https://github.com/getsentry/onpremise.git
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>创建 Sentry 服务</li>
</ol>
<pre><code class="copyable">cd onpremise
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建docker本地数据库</p>
<pre><code class="copyable">docker volume create --name=sentry-data && 
docker volume create --name=sentry-postgres &&
docker volume create --name=sentry-redis &&
docker volume create --name=sentry-zookeeper &&
docker volume create --name=sentry-kafka &&
docker volume create --name=sentry-clickhouse &&
docker volume create --name=sentry-symbolicator

<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建env配置文件</p>
<pre><code class="copyable">cp -n .env.example .env
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">COMPOSE_PROJECT_NAME=sentry_onpremise
SENTRY_EVENT_RETENTION_DAYS=90
# You can either use a port number or an IP:PORT combo for SENTRY_BIND
# See https://docs.docker.com/compose/compose-file/#ports for more
SENTRY_BIND=9000
SENTRY_IMAGE=getsentry/sentry:nightly
SNUBA_IMAGE=getsentry/snuba:nightly
RELAY_IMAGE=getsentry/relay:nightly
SYMBOLICATOR_IMAGE=getsentry/symbolicator:nightly
WAL2JSON_VERSION=latest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构建服务</p>
<pre><code class="copyable">docker-compose build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果报错“-bash: docker-compose: command not found”，则需要先安装 docker-compose:</p>
<pre><code class="copyable">yum -y install epel-release
yum -y install python-pip
pip install docker-compose
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成秘钥</p>
<pre><code class="copyable">docker-compose run --rm web config generate-secret-key
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">...
Digest: sha256:de277fb0489fa674e28ce44a790840ece63dbacd696c990b95abdf0135ae5283
Status: Downloaded newer image for getsentry/sentry:nightly
4ghk9%xzwzg#e9yv5(w@rabcq626y&n*fygk=tzah%d!*la!1l
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一行就是生成的秘钥，将生成的秘钥添加到.env 的 SENTRY_SECRET_KEY</p>
<pre><code class="copyable">COMPOSE_PROJECT_NAME=sentry_onpremise
SENTRY_EVENT_RETENTION_DAYS=90
SENTRY_SECRET_KEY="4ghk9%xzwzg#e9yv5(w@rabcq626y&n*fygk=tzah%d!*la!1l"
# You can either use a port number or an IP:PORT combo for SENTRY_BIND
# See https://docs.docker.com/compose/compose-file/#ports for more
SENTRY_BIND=9000
SENTRY_IMAGE=getsentry/sentry:nightly
SNUBA_IMAGE=getsentry/snuba:nightly
RELAY_IMAGE=getsentry/relay:nightly
SYMBOLICATOR_IMAGE=getsentry/symbolicator:nightly
WAL2JSON_VERSION=latest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建数据库，创建超级管理员，作为登入sentry的账号，创建过程按提示一步步来</p>
<pre><code class="copyable">./install.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成后，使用以下命令启动所有服务：</p>
<pre><code class="copyable">docker-compose up -d
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在浏览器打开：<a href="https://link.juejin.cn/?target=http%3A%2F%2F%25E6%259C%258D%25E5%258A%25A1%25E5%2599%25A8ip%3A9000" target="_blank" rel="nofollow noopener noreferrer" title="http://%E6%9C%8D%E5%8A%A1%E5%99%A8ip:9000" ref="nofollow noopener noreferrer">http://服务器ip:9000</a> 就能看到 Sentry 的服务端登录界面了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4070018155ac4ae2ada64bfa8ba2a492~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-5">网站端接入 Sentry</h5>
<pre><code class="copyable"><script src="$&#123;staticDomain&#125;/statics/lib/sentry/bundle.tracing.min.js?v=1.0" crossorigin="anonymous"></script>
<script>
    Sentry.init(&#123;
        dsn: "http://054e5400ae8d407eb8927804f0011e70@192.168.4.60:9000/2",
        // this assumes your build process sets "npm_package_version" in the env
        // release: "my-project-name@" + process.env.npm_package_version,
        integrations: [new Sentry.Integrations.BrowserTracing()],

        // We recommend adjusting this value in production, or using tracesSampler
        // for finer control
        // tracesSampleRate: 1.0,
        release: "0.0.1",
    &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面可以写一行测试异常代码，验证 Sentry 能否接收到错误，正常接收的异常上报是这样的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a40f1d39abbe4d5fb513a163045c82b9~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里虽然能监控到脚本异常错误，但是我们通常发布到生产环境的代码是经过压缩混淆的，如果我们还想要监控到具体是哪一行代码引起的脚本错误，那就还需要上传 sourcemaps 到 Sentry 服务器。</p>
<h5 data-id="heading-6">Sentry 上传 sourcemaps</h5>
<p>Sentry 上传 sourcemaps 的方式有两种，一种是通过 webpack 插件上传，另一种是通过 sentry cli 上传。两种方式配置都不复杂
，取决于你的项目使用的是什么构建工具，如果你的项目是使用webpack打包的自然是使用webpack插件上传会方便一点，如果是使用 gulp 等其他构建工具的，那就是使用 sentry cli 会方便一点。</p>
<ul>
<li>webpack 插件上传 sourcemaps</li>
</ul>
<p>安装 @sentry/webpack-plugin 和 clean-webpack-plugin</p>
<pre><code class="copyable">npm install @sentry/webpack-plugin clean-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取 authToken</p>
<pre><code class="copyable">API keys -> Auth Tokens -> Create New Token
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 webpack.config.js 中添加以下代码：</p>
<pre><code class="copyable">const SentryWebpackPlugin = require("@sentry/webpack-plugin");
const &#123; CleanWebpackPlugin &#125; = require('clean-webpack-plugin');
module.exports = &#123;
  plugins: [
      new SentryWebpackPlugin(&#123;
          url: "http://192.168.4.60:9000/",
          authToken: "9d332444a2804384b38cce5d11664294c9eea7a41aea4e71ae2daaa4c9b5bd7f",
          org: "sentry",
          project: "pc-web",
          // 本地 sourcemap 所在目录
          include: ".",
          // js 访问路径,如果使用了cdn,则需要写上完整域名和路径
          urlPrefix: "http://src.test.com/statics/js/dist"
      &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>sentry cli 上传 sourcemaps</li>
</ul>
<p>安装 sentry cli</p>
<pre><code class="copyable">npm install @sentry/cli@16.7.1 -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果安装失败，报如下错误：</p>
<pre><code class="copyable">Downloading from https://downloads.sentry-cdn.com/sentry-cli/1.67.1/sentry-cli-Windows-x86_64.exe Error: Unable to download sentry-cli binary from https://downloads.sentry-cdn.com/sentry-cli/1.67.1/sentry-cli-Windows-x86_64.exe. Error code: ECONNRESET
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以修改拉取地址为淘宝镜像地址：</p>
<pre><code class="copyable">npm config set sentrycli_cdnurl https://npm.taobao.org/mirrors/sentry-cli/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置代码打包时生成 sourcemaps, 我的项目是基于 gulp 打包的，所以使用 gulp-sourcemaps 插件生成 sourcemaps：</p>
<pre><code class="copyable">var sourcemaps = require('gulp-sourcemaps');
// 省略其他代码
pump([
    gulp.src(path.join(build_path, paths.optimize + '/' + dir + '/' + versiondir + '/*.js')),
    sourcemaps.init(),
    babel(),
    concat(versiondir + '.js'),
    uglify(),
    sourcemaps.write('./'),
    gulp.dest(distPath)
])
// 省略其他代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行构建任务后，就会在 dist 目录同时生成 sourcemap 文件。</p>
<p>上传 Sourcemaps 到 Sentry,先在项目根目录新建一个.sentryclirc文件，代码如下：</p>
<pre><code class="copyable">[defaults]
url = http://192.168.4.60:9000/
org = sentry
project = pc-web
 
[auth]
token = 9d332444a2804384b38cce5d11664294c9eea7a41aea4e71ae2daaa4c9b5bd7f
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在生产打包的脚本增加 上传 sourcemaps 的命令：</p>
<pre><code class="copyable">gulp js --env pro // 生产打包
sentry-cli releases -o sentry -p pc-web new 0.0.1
sentry-cli releases files 0.0.1 upload-sourcemaps statics/js/dist --url-prefix http://src.test.com/statics/js/dist
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有个要注意的地方，就是 sourcemaps 的版本号（前文示例的 0.0.1）一定要与网站初始化 sentry 时的 release 参数一致，否则 Sentry 监控到报错脚本也无法定位到具体的源码的。</p>
<p>下面看看监控脚本报错的效果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/865d2eb9d049454fad8231319c63c2ff~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">结语</h4>
<p>到这里，就完成了网站前端异常监控系统 Sentry 的接入，本文也只是演示了 Sentry 最基本的功能，还有其他比较高级用法计划在后续逐步引入，包括网站 404 页面监控，接口性能监控等等。</p></div>  
</div>
            