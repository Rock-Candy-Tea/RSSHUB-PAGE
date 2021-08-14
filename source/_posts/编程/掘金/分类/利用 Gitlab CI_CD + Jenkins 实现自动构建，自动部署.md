
---
title: '利用 Gitlab CI_CD + Jenkins 实现自动构建，自动部署'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d48990cc30a46dda053ecfea49f43de~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 06:48:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d48990cc30a46dda053ecfea49f43de~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文是19底年的文章，在公司当时的环境写的了，现在大部分公司都有Devops效能平台采用docker或者oss部署</p>
</blockquote>
<p>本来只是想用 curl 去模拟触发部署静态资源的请求的。后来想到如果把这个操作交给 gitlab 操作岂不是更方便？ 所以这几天折腾了一下 gitlab 的 CI/CD,读了一些 gitlab 的官方文档，进一步完善了.gitlab-ci.yml。记录这个过程如下：</p>
<h2 data-id="heading-0">模拟请求</h2>
<blockquote>
<p>利用 curl 命令行工具去模拟我们点击 <code>开始构建</code> 时那一时刻发起的第一个请求。</p>
</blockquote>
<h3 data-id="heading-1">第一个请求</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d48990cc30a46dda053ecfea49f43de~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
经实践，第一个请求为上面的这个请求，重要参数是 json：xxx 和 Cookie，请求结果是一个 303 重定向。
<a name="user-content-XGAOu" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-2">编写请求脚本</h3>
<p>方便起见，首先用浏览器提供的方式，复制该请求。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0725639742e43caa8ee9cc89e1851fc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">复制了整个请求之后，删除了一些不必要的参数之后，与提取 env， branch 这些变量之后， 得知下面的脚本</p>
<pre><code class="hljs language-shell copyable" lang="shell">env=uat
branch=test

curl 'https://xxxx/job/tao.tao/build?delay=0sec' \
  -H 'Cookie: JSESSIONID=8EF2BD7082FB37279EE93A3B7BB3ED25' \
  --data-raw 'json=&#123;"parameter":[&#123;"name":"PJ","value":"crm-finance-static"&#125;,&#123;"name":"MYENV", "value":"'$env'"&#125;,&#123;"name":"TAG","value":"'$branch'"&#125;]&#125;' \
  --compressed

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的脚本是用 cookie 做用户认证的，既然是 cookie,就存在过期的可能。还好 Jenkins 提供了 token 的方法给用户。
具体看官方文档这两篇文章：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jenkins.io%2Fdoc%2Fbook%2Fsystem-administration%2Fauthenticating-scripted-clients%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/" ref="nofollow noopener noreferrer">www.jenkins.io/doc/book/sy…</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jenkins.io%2Fblog%2F2018%2F07%2F02%2Fnew-api-token-system%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jenkins.io/blog/2018/07/02/new-api-token-system/" ref="nofollow noopener noreferrer">www.jenkins.io/blog/2018/0…</a></p>
<p>配置了 token 之后，修改之后脚本</p>
<pre><code class="hljs language-shell copyable" lang="shell">env=uat
branch=test

curl 'https://xxxx/job/tao.tao/build?delay=0sec' \
  --user tao-tao:1169ee9c0493b27d915632c0577fdd66fd \
  --data-raw 'json=&#123;"parameter":[&#123;"name":"PJ","value":"crm-finance-static"&#125;,&#123;"name":"MYENV", "value":"'$env'"&#125;,&#123;"name":"TAG","value":"'$branch'"&#125;]&#125;' \
  --compressed

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们直接使用了 <code>sh 上面的脚本.sh</code>  执行，打开 jenkins 发布平台就可以看到有任务在执行了</p>
<p><a name="user-content-KZ9kd" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-3">安排到 gitlab 上面</h2>
<blockquote>
<p>注：原来已经有了.gitlab-ci.yml 文件存在了，主要负责： 当我们 push 代码到 gitlab 仓库之后，自动执行 build 命令，并且复制到目标静态资源仓库中，之后再 push 到 gitlab 上</p>
</blockquote>
<blockquote>
<p>不熟悉 gitlab 工作流的话，可以先看，开卷有益</p>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fci%2Fintroduction%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/ee/ci/introduction/" ref="nofollow noopener noreferrer">docs.gitlab.com/ee/ci/intro…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Fce%2Fci%2Fquick_start%2FREADME.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/ce/ci/quick_start/README.html" ref="nofollow noopener noreferrer">docs.gitlab.com/ce/ci/quick…</a></li>
</ol>
</blockquote>
<p>增加如下代码：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">deploy:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">deploy</span>
  <span class="hljs-attr">only:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">/^(test|pre|dev)$/</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">command</span> <span class="hljs-string">-v</span> <span class="hljs-string">curl</span> <span class="hljs-string">>/dev/null</span> <span class="hljs-number">2</span><span class="hljs-string">>&1</span> <span class="hljs-string">||</span> <span class="hljs-string">exit</span> <span class="hljs-number">1</span> <span class="hljs-comment">#判断是否执行curl，否则推荐脚本</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">env="$REF_NAME"</span> <span class="hljs-comment"># 默认env 与 分支名一致， 特殊处理uat --》 test</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">>
      if [ "$REF_NAME" == "test" ]; then
        env="uat"
      fi
</span>    <span class="hljs-bullet">-</span> <span class="hljs-string">sh</span> <span class="hljs-string">./scripts/fetch-jenkins.sh</span> <span class="hljs-string">$env</span> <span class="hljs-string">$REF_NAME</span> <span class="hljs-comment"># 执行脚本， 带上参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最初我是放在 after_script 中执行的，后来发现 after_script 即使脚本执行出错，gitlab 上面的 CI/CD/Pipelines 的 Job 的状态，照样是 passed 状态。
搜索得知 after_script 中是忽略失败的，如果需要支持的话，要另外安装脚本，具体可以看如下解释：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitlab.com%2Fgitlab-org%2Fgitlab-foss%2F-%2Fissues%2F43010" target="_blank" rel="nofollow noopener noreferrer" title="https://gitlab.com/gitlab-org/gitlab-foss/-/issues/43010" ref="nofollow noopener noreferrer">gitlab.com/gitlab-org/…</a>，所以我后面把它放在了 script 中，这样脚本出错的话，Job 的状态也是 failed 的状态（Job 失败的话，gitlab 还给我们发了邮件）</p>
<hr>
<p>另外，curl 只是模拟构建请求，但是我们如何判断请求成功还是失败的？前面我们说构建请求是返回 303 重定向的， 没有 response 内容回来，据此我们就可以判断，请求成功还是失败了，如果有请求结果的话，脚本就 exit 1</p>
<pre><code class="hljs language-shell copyable" lang="shell">if [ "$RES" ]; then &#123; echo 'failed!'; exit 1;  &#125; fi
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.gitlab-ci.yml</code>  与 <code>fetch-jenkins.sh</code>  代码附件:
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fyml%2F365160%2F1593771925625-835c8fda-6f86-4a8e-8270-dd43c182dbc6.yml%3F_lake_card%3D%257B%2522uid%2522%253A%25221593771925609-0%2522%252C%2522src%2522%253A%2522https%253A%252F%252Fwww.yuque.com%252Fattachments%252Fyuque%252F0%252F2020%252Fyml%252F365160%252F1593771925625-835c8fda-6f86-4a8e-8270-dd43c182dbc6.yml%2522%252C%2522name%2522%253A%2522.gitlab-ci.yml%2522%252C%2522size%2522%253A1712%252C%2522type%2522%253A%2522%2522%252C%2522ext%2522%253A%2522yml%2522%252C%2522progress%2522%253A%257B%2522percent%2522%253A99%257D%252C%2522status%2522%253A%2522done%2522%252C%2522percent%2522%253A0%252C%2522id%2522%253A%2522FIJyr%2522%252C%2522card%2522%253A%2522file%2522%257D" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/attachments/yuque/0/2020/yml/365160/1593771925625-835c8fda-6f86-4a8e-8270-dd43c182dbc6.yml?_lake_card=%7B%22uid%22%3A%221593771925609-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fyml%2F365160%2F1593771925625-835c8fda-6f86-4a8e-8270-dd43c182dbc6.yml%22%2C%22name%22%3A%22.gitlab-ci.yml%22%2C%22size%22%3A1712%2C%22type%22%3A%22%22%2C%22ext%22%3A%22yml%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22FIJyr%22%2C%22card%22%3A%22file%22%7D" ref="nofollow noopener noreferrer">.gitlab-ci.yml</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fsh%2F365160%2F1593771950682-e5d84018-6882-4746-b001-082cb57a3565.sh%3F_lake_card%3D%257B%2522uid%2522%253A%25221593771950767-0%2522%252C%2522src%2522%253A%2522https%253A%252F%252Fwww.yuque.com%252Fattachments%252Fyuque%252F0%252F2020%252Fsh%252F365160%252F1593771950682-e5d84018-6882-4746-b001-082cb57a3565.sh%2522%252C%2522name%2522%253A%2522fetch-jenkins.sh%2522%252C%2522size%2522%253A602%252C%2522type%2522%253A%2522text%252Fx-sh%2522%252C%2522ext%2522%253A%2522sh%2522%252C%2522progress%2522%253A%257B%2522percent%2522%253A99%257D%252C%2522status%2522%253A%2522done%2522%252C%2522percent%2522%253A0%252C%2522id%2522%253A%2522GoS0f%2522%252C%2522card%2522%253A%2522file%2522%257D" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/attachments/yuque/0/2020/sh/365160/1593771950682-e5d84018-6882-4746-b001-082cb57a3565.sh?_lake_card=%7B%22uid%22%3A%221593771950767-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fsh%2F365160%2F1593771950682-e5d84018-6882-4746-b001-082cb57a3565.sh%22%2C%22name%22%3A%22fetch-jenkins.sh%22%2C%22size%22%3A602%2C%22type%22%3A%22text%2Fx-sh%22%2C%22ext%22%3A%22sh%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22GoS0f%22%2C%22card%22%3A%22file%22%7D" ref="nofollow noopener noreferrer">fetch-jenkins.sh</a>
<a name="user-content-O7ZU6" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-4">忽略.gitlab-ci.yml 的作用</h2>
<p>如果我们有一个这样的需要,在某一次 push,我不需要 gitlab 执行构建任务,或者我们觉得 gitlab 构建任务 pengding 太久, 或者 running 太慢。 如何解决这个痛点呢？</p>
<p>这样，我们如果控制 push 代码的时候，携带信息通知 gitlab 服务器，达到我们想要的结果。</p>
<p>很幸运，Gitlab CI/CD 是提供这个服务的，只不过有版本限制，
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e00372ca850d47c7938fb1040225f971~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
得知，我们的 gitlab runner 版本是<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7405fd3f1164a70aec92019ea00f274~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">是支持 ci.skip。</p>
<p>携带 <code>-o ci.skip</code> 之后 再 Pipelines 中就可以看到 ,如下图所示:跳过 job<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6e8d1e1964a4e4f8d92ae57b0c0af94~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a name="user-content-bbnOT" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-5">本地执行 CI/CD 脚本</h2>
<blockquote>
<p>如果觉得 gitlab 构建速度太慢,结合我之前写的构建脚本,同样也可以实现自动构建,自动部署。</p>
</blockquote>
<p>大概脚本如下：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash">!/usr/bin/env bash</span>
set -euo pipefail
branch=$1
curPath=`pwd`
targetPath="./build" # 打包静态资源路径配置, 为了统一推荐clone在源码根目录下的build文件夹(.gitignore 已忽略build)
commitID=`git rev-parse --short HEAD` # get last commit SHA
subModule=finance
curBranch=`git symbolic-ref --short -q HEAD` # get current branch
<span class="hljs-meta">
#</span><span class="bash"> 首先判断是否在目标分支build</span>
if [ "$curBranch" != "$branch" ]; then
    echo -------------------------------------
    echo -e "\033[41;37m please checkout $branch before building \033[0m"
    echo -------------------------------------
    exit 1
fi

cd "$targetPath"
<span class="hljs-meta">#</span><span class="bash"> 获取分支名称</span>
targetBranch=`git symbolic-ref --short -q HEAD`
<span class="hljs-meta">#</span><span class="bash">  判断是否在目标分支,不在的话checkout</span>
if [ "$targetBranch" != "$branch" ]; then
    git checkout "$branch"
fi

git pull
rm -rf "$targetPath/$subModule/"
cp -r "$curPath/dist/$subModule/" "./"


message="deploy based on $branch from $commitID"
<span class="hljs-meta">
#</span><span class="bash"> <span class="hljs-built_in">set</span> +e</span>
git add .
git commit -m "$message"
git push -u origin

cd -
<span class="hljs-meta">
#</span><span class="bash"> fetch jenkins interface</span>
case $branch in
  dev  ) env="dev"
      ;;
  test ) env="uat"
      ;;
  pre )  env="pre"
      ;;
  master ) echo -e "\033[41;37m not support master \033[0m" && exit 0
      ;;
  *    ) echo -------------------------------------
         echo -e "\033[41;37m branch($branch) error before fetch jenkins \033[0m"
         echo -------------------------------------
         exit 1
esac

sh ./scripts/fetch-jenkins.sh $env $branch # 执行触发jenkins请求脚本

<span class="copy-code-btn">复制代码</span></code></pre>
<p>附件如下：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fsh%2F365160%2F1594003103252-ceeff864-c94e-4ed9-8c3d-a842a4b7f2f6.sh%3F_lake_card%3D%257B%2522uid%2522%253A%25221594003103166-0%2522%252C%2522src%2522%253A%2522https%253A%252F%252Fwww.yuque.com%252Fattachments%252Fyuque%252F0%252F2020%252Fsh%252F365160%252F1594003103252-ceeff864-c94e-4ed9-8c3d-a842a4b7f2f6.sh%2522%252C%2522name%2522%253A%2522deploy.sh%2522%252C%2522size%2522%253A1518%252C%2522type%2522%253A%2522text%252Fx-sh%2522%252C%2522ext%2522%253A%2522sh%2522%252C%2522progress%2522%253A%257B%2522percent%2522%253A99%257D%252C%2522status%2522%253A%2522done%2522%252C%2522percent%2522%253A0%252C%2522id%2522%253A%2522GujHr%2522%252C%2522card%2522%253A%2522file%2522%257D" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/attachments/yuque/0/2020/sh/365160/1594003103252-ceeff864-c94e-4ed9-8c3d-a842a4b7f2f6.sh?_lake_card=%7B%22uid%22%3A%221594003103166-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fsh%2F365160%2F1594003103252-ceeff864-c94e-4ed9-8c3d-a842a4b7f2f6.sh%22%2C%22name%22%3A%22deploy.sh%22%2C%22size%22%3A1518%2C%22type%22%3A%22text%2Fx-sh%22%2C%22ext%22%3A%22sh%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22GujHr%22%2C%22card%22%3A%22file%22%7D" ref="nofollow noopener noreferrer">deploy.sh</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fsh%2F365160%2F1594003103562-0d3ca043-0f06-4990-9571-dee8a400f3ba.sh%3F_lake_card%3D%257B%2522uid%2522%253A%25221594003103166-1%2522%252C%2522src%2522%253A%2522https%253A%252F%252Fwww.yuque.com%252Fattachments%252Fyuque%252F0%252F2020%252Fsh%252F365160%252F1594003103562-0d3ca043-0f06-4990-9571-dee8a400f3ba.sh%2522%252C%2522name%2522%253A%2522fetch-jenkins.sh%2522%252C%2522size%2522%253A602%252C%2522type%2522%253A%2522text%252Fx-sh%2522%252C%2522ext%2522%253A%2522sh%2522%252C%2522progress%2522%253A%257B%2522percent%2522%253A99%257D%252C%2522status%2522%253A%2522done%2522%252C%2522percent%2522%253A0%252C%2522id%2522%253A%2522Xpjed%2522%252C%2522card%2522%253A%2522file%2522%257D" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/attachments/yuque/0/2020/sh/365160/1594003103562-0d3ca043-0f06-4990-9571-dee8a400f3ba.sh?_lake_card=%7B%22uid%22%3A%221594003103166-1%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fsh%2F365160%2F1594003103562-0d3ca043-0f06-4990-9571-dee8a400f3ba.sh%22%2C%22name%22%3A%22fetch-jenkins.sh%22%2C%22size%22%3A602%2C%22type%22%3A%22text%2Fx-sh%22%2C%22ext%22%3A%22sh%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22Xpjed%22%2C%22card%22%3A%22file%22%7D" ref="nofollow noopener noreferrer">fetch-jenkins.sh</a></li>
</ul>
<p>然后 package.json 在配置如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26ff044b49814594a3782c10649f4bbb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>直接执行 yarn deploy:dev 就帮助我们构建，push 到静态自然仓库，触发 jenkins 请求，部署到了 dev 了</p>
</blockquote>
<p>最后，CI/CD 能有很多方式实现，有待大家挖掘， 这个也算是根据实际的项目情况，打通了 Jenkins，欢迎大家多多交流。</p>
<p>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjackluson%2Flearn-path-recording-and-coding%2Fblob%2Fmaster%2Fdocs%2Fdevelop-flow%2Fgitlab-with-jenkins.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jackluson/learn-path-recording-and-coding/blob/master/docs/develop-flow/gitlab-with-jenkins.md" ref="nofollow noopener noreferrer">github.com/jackluson/l…</a></p></div>  
</div>
            