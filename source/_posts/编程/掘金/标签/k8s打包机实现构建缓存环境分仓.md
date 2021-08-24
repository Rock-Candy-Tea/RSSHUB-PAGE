
---
title: 'k8s打包机实现构建缓存环境分仓'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=1119'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 19:26:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=1119'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在k8s环境下我们正常打包使用docker镜像进行打包。最好得方案是，每次打包都去拉取所需得jar包，这样就每个每个工程互不影响，但是这样未免也太豪了，并且每个分支包在nexus上还可能产生覆盖冲突等问题。例如，我们有四个环境，如果开发包都用snapshot的话，就可能出现A\B两人使用不同的分支同时打包，并且他们共同依赖了一个公共包，那么这个公共包就有可能A使用了B的包导致出现问题，这就是所谓的串包。那么我们的方案如下，</p>
<ul>
<li>按环境本地分仓,解决不同环境串包问题</li>
<li>开发环境按分支分版本使用version:set -DnewVersion=$&#123;CI_COMMIT_REF_NAME&#125;-SNAPSHOT，解决开发环境串包（未实施）</li>
</ul>
<p>脚本如下，按分支分版本未完善自己行修改，部分变量说明</p>
<ul>
<li>GITLAB_AT：gitlab-Access_token</li>
<li>CI_COMMIT_REF_NAME：git默认环境变量，分支名</li>
<li>DEPENDENCY_LIST自定义需要依赖的构建项目，A依赖B，先构建B,再构建A</li>
<li>BUILD_SUPPORT 自定义的业务框架项目构建开关</li>
<li>BUILD_ARCH 自定义的基础架构项目构建开关</li>
</ul>
<p>以上变量都定义在gitlab ci variables中。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/usr/bin/env bash</span>
<span class="hljs-built_in">set</span> -e
CUR_DIR=$(<span class="hljs-built_in">cd</span> $(dirname <span class="hljs-variable">$0</span>);<span class="hljs-built_in">pwd</span>)
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">build</span></span>()&#123;
    GIT_URL=<span class="hljs-string">"http://<span class="hljs-variable">$&#123;GITLAB_USER:-username&#125;</span>:<span class="hljs-variable">$&#123;GITLAB_AT&#125;</span>@gitlab.xxx.cn/reponame/<span class="hljs-variable">$1</span>.git"</span>
    <span class="hljs-keyword">if</span> [ -d <span class="hljs-variable">$1</span> ];<span class="hljs-keyword">then</span>
        rm -rf <span class="hljs-variable">$&#123;CUR_DIR&#125;</span>/<span class="hljs-variable">$1</span>
    <span class="hljs-keyword">fi</span>;
    git <span class="hljs-built_in">clone</span> <span class="hljs-variable">$GIT_URL</span>
    <span class="hljs-built_in">cd</span> <span class="hljs-variable">$&#123;CUR_DIR&#125;</span>/<span class="hljs-variable">$1</span>
    count=$(git branch -a|grep <span class="hljs-variable">$&#123;CI_COMMIT_REF_NAME&#125;</span>|wc -l)
    <span class="hljs-keyword">if</span> [ <span class="hljs-variable">$count</span> != 0 ];<span class="hljs-keyword">then</span>
      git checkout <span class="hljs-variable">$&#123;CI_COMMIT_REF_NAME&#125;</span>
      env_name=$(get_env)
      mvn clean install -Dmaven.test.failure.ignore=<span class="hljs-literal">true</span> -DskipTests=<span class="hljs-literal">true</span> -Dmaven.repo.local=/root/.m2/repository-<span class="hljs-variable">$env_name</span> -U
    <span class="hljs-keyword">fi</span>
    <span class="hljs-built_in">cd</span> <span class="hljs-variable">$&#123;CUR_DIR&#125;</span>
    rm -rf <span class="hljs-variable">$&#123;CUR_DIR&#125;</span>/<span class="hljs-variable">$1</span>
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">build_dependency</span></span>()&#123;
    <span class="hljs-keyword">for</span> PRO <span class="hljs-keyword">in</span> <span class="hljs-variable">$DEPENDENCY_LIST</span> ;<span class="hljs-keyword">do</span>
        build <span class="hljs-variable">$PRO</span>
    <span class="hljs-keyword">done</span>
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">get_env</span></span>()&#123;
    <span class="hljs-keyword">if</span> [[ <span class="hljs-string">"<span class="hljs-variable">$&#123;CI_COMMIT_REF_NAME&#125;</span>"</span> =~ dev[0-9]* ]]; <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"dev"</span>
    <span class="hljs-keyword">elif</span> [[ <span class="hljs-string">"<span class="hljs-variable">$&#123;CI_COMMIT_REF_NAME&#125;</span>"</span> =~ sit[0-9]* ]] || [[ <span class="hljs-string">"<span class="hljs-variable">$&#123;CI_COMMIT_REF_NAME&#125;</span>"</span> =~ sit[0-9]* ]]; <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"sit"</span>
    <span class="hljs-keyword">elif</span> [[ <span class="hljs-string">"<span class="hljs-variable">$&#123;CI_COMMIT_REF_NAME&#125;</span>"</span>==<span class="hljs-string">"master"</span> ]] || [[ <span class="hljs-string">"<span class="hljs-variable">$&#123;CI_COMMIT_REF_NAME&#125;</span>"</span>==<span class="hljs-string">"release-"</span>* ]] || [[ <span class="hljs-string">"<span class="hljs-variable">$&#123;CI_COMMIT_REF_NAME&#125;</span>"</span>==<span class="hljs-string">"hotfix-"</span>* ]];<span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"prod"</span>
    <span class="hljs-keyword">else</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"dev"</span>
    <span class="hljs-keyword">fi</span>
&#125;
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">main</span></span>()&#123;
    <span class="hljs-keyword">if</span> [[ -n <span class="hljs-variable">$&#123;BUILD_ARCH&#125;</span> ]] &&  [[ <span class="hljs-variable">$&#123;BUILD_ARCH&#125;</span> == <span class="hljs-literal">true</span> ]];<span class="hljs-keyword">then</span>
      build framework-all
    <span class="hljs-keyword">fi</span>
    <span class="hljs-keyword">if</span> [[ -n <span class="hljs-variable">$&#123;BUILD_SUPPORT&#125;</span> ]] && [[ <span class="hljs-variable">$&#123;BUILD_SUPPORT&#125;</span> == <span class="hljs-literal">true</span> ]];<span class="hljs-keyword">then</span>
      build support
    <span class="hljs-keyword">fi</span>
    <span class="hljs-keyword">if</span> [[ -n <span class="hljs-variable">$&#123;DEPENDENCY_LIST&#125;</span> ]];<span class="hljs-keyword">then</span>
      build_dependency
    <span class="hljs-keyword">fi</span>
    env_name=$(get_env)
    mvn clean package -Dmaven.test.failure.ignore=<span class="hljs-literal">true</span> -DskipTests=<span class="hljs-literal">true</span> -Dmaven.repo.local=/root/.m2/repository-<span class="hljs-variable">$env_name</span> -U
&#125;
main $*
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用也相当简单，首先把脚本放在gitlab中，通过curl拉取，然后配置stage即可</p>
<pre><code class="hljs language-yaml copyable" lang="yaml">
<span class="hljs-attr">mvn-package:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">mvn-package</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">bash</span> <span class="hljs-string">build.sh</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">cp</span> <span class="hljs-string">target/app.war</span> <span class="hljs-string">$&#123;CACHE_PIPELINE&#125;/app.war</span>
  <span class="hljs-attr">only:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">sit</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">/^dev\d+$/</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">/^feature-.*$/</span>
   
<span class="hljs-string">.auto_devops:</span> <span class="hljs-string">&auto_devops</span> <span class="hljs-string">|
  echo "GITLAB_AT=$GITLAB_AT;GITLAB_USER=$GITLAB_USER;BUILD_ARCH=$BUILD_ARCH;BUILD_SUPPORT=$BUILD_SUPPORT;DEPENDENCY_LIST=$DEPENDENCY_LIST"
  build_status=`curl -O -s -m 10 --connect-timeout 10 -w %&#123;http_code&#125; --header "PRIVATE-TOKEN:$&#123;GITLAB_AT&#125;"  http://gitlab.xxx.cn/package/bash/raw/master/build.sh`
  if [ $build_status != 200 ];then
    echo '请设置GITLAB_AT'
    exit 1
  fi
</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            