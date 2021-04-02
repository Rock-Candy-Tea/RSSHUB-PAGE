
---
title: 'iOS模块化管理之CocoaPods实战'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adde5ad917ec49f78f38f45f821e4f5b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 02:09:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adde5ad917ec49f78f38f45f821e4f5b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">环境准备</h1>
<blockquote>
<p>更新gem源，如果系统中没有安装gem，请先安装gem环境</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> sudo gem update --system</span> 
Latest version already installed. Done.
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>CocoaPods依赖ruby环境，在项目开始前先查看一下本地ruby环境，一般Mac电脑都自带了ruby环境。</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> gem sources -l</span>
*** CURRENT SOURCES ***
https://rubygems.org/
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>由于ruby官方源国内被墙，需要修改ruby源。</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> gem sources --remove https://rubygems.org/</span>
<span class="hljs-meta">$</span><span class="bash"> gem sources --add https://gems.ruby-china.com/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>查看ruby镜像是否已经切换</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> gem sources -l</span>                        
*** CURRENT SOURCES ***

https://gems.ruby-china.com/
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>查看本地CocoaPods版本</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> pod --version</span>              
1.10.1
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果没有安装CocoaPods，先安装CocoaPods</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> sudo gem install -n /usr/<span class="hljs-built_in">local</span>/bin cocoapods</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>再次查看CocoaPods版本</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> pod --version</span>              
1.10.1
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">工具准备</h2>
<blockquote>
<p>工欲善其事必先利其器！</p>
</blockquote>
<h3 data-id="heading-2">私有仓库准备</h3>
<blockquote>
<p>创建远程私有仓库。由于示例中仓库名称已经存在，Gitee会有相应的错误提示，但不影响继续往下进行。</p>
</blockquote>
<img alt="image-20210311174013099" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adde5ad917ec49f78f38f45f821e4f5b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<blockquote>
<p>将远程仓库添加至本地pod repo中</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> pod repo add ishadoo-specs https://gitee.com/ishadoo/Specs.git</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>查看本地仓库</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> pod repo list</span>  

ishadoo-specs
- Type: git (master)
- URL:  https://gitee.com/ishadoo/Specs.git
- Path: /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs

master
- Type: git (master)
- URL:  https://github.com/CocoaPods/Specs.git
- Path: /Users/wangchuanhai/.cocoapods/repos/master

trunk
- Type: CDN
- URL:  https://cdn.cocoapods.org/
- Path: /Users/wangchuanhai/.cocoapods/repos/trunk
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">CHModuleConfig工具</h3>
<blockquote>
<p>Gitee仓库地址：<a href="https://gitee.com/ishadoo/CHModuleConfig.git" target="_blank" rel="nofollow noopener noreferrer">gitee.com/ishadoo/CHM…</a></p>
<p>初始化项目，将iOS工程与远程git仓库进行关联。</p>
</blockquote>
<h4 data-id="heading-4">Config脚本：</h4>
<ul>
<li>
<h4 data-id="heading-5">做了3件事：</h4>
<ul>
<li>初始本地iOS项目，添加podspec文件。</li>
<li>将初始化后的项目与远程私有仓库进行关联。</li>
<li>添加私有库上传脚本。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-perl copyable" lang="perl"><span class="hljs-comment">#!/bin/bash</span>

Cyan=<span class="hljs-string">'\033[0;36m'</span>
Default=<span class="hljs-string">'\033[0;m'</span>

projectName=<span class="hljs-string">""</span>
httpsRepo=<span class="hljs-string">""</span>
sshRepo=<span class="hljs-string">""</span>
homePage=<span class="hljs-string">""</span>
confirmed=<span class="hljs-string">"n"</span>

getProjectName() &#123;
    <span class="hljs-keyword">read</span> -p <span class="hljs-string">"Enter Project Name: "</span> projectName
    <span class="hljs-keyword">if</span> test -z <span class="hljs-string">"$projectName"</span>; then
        getProjectName
    fi
&#125;

getHTTPSRepo() &#123;
    <span class="hljs-keyword">read</span> -p <span class="hljs-string">"Enter HTTPS Repo URL: "</span> httpsRepo
    <span class="hljs-keyword">if</span> test -z <span class="hljs-string">"$httpsRepo"</span>; then
        getHTTPSRepo
    fi
&#125;

getSSHRepo() &#123;
    <span class="hljs-keyword">read</span> -p <span class="hljs-string">"Enter SSH Repo URL: "</span> sshRepo
    <span class="hljs-keyword">if</span> test -z <span class="hljs-string">"$sshRepo"</span>; then
        getSSHRepo
    fi
&#125;

getHomePage() &#123;
    <span class="hljs-keyword">read</span> -p <span class="hljs-string">"Enter Home Page URL: "</span> homePage
    <span class="hljs-keyword">if</span> test -z <span class="hljs-string">"$homePage"</span>; then
        getHomePage
    fi
&#125;

getInfomation() &#123;
    getProjectName
    getHTTPSRepo
    getSSHRepo
    getHomePage

    echo -e <span class="hljs-string">"\n<span class="hljs-subst">$&#123;Default&#125;</span>================================================"</span>
    echo -e <span class="hljs-string">"  Project Name  :  <span class="hljs-subst">$&#123;Cyan&#125;</span><span class="hljs-subst">$&#123;projectName&#125;</span><span class="hljs-subst">$&#123;Default&#125;</span>"</span>
    echo -e <span class="hljs-string">"  HTTPS Repo    :  <span class="hljs-subst">$&#123;Cyan&#125;</span><span class="hljs-subst">$&#123;httpsRepo&#125;</span><span class="hljs-subst">$&#123;Default&#125;</span>"</span>
    echo -e <span class="hljs-string">"  SSH Repo      :  <span class="hljs-subst">$&#123;Cyan&#125;</span><span class="hljs-subst">$&#123;sshRepo&#125;</span><span class="hljs-subst">$&#123;Default&#125;</span>"</span>
    echo -e <span class="hljs-string">"  Home Page URL :  <span class="hljs-subst">$&#123;Cyan&#125;</span><span class="hljs-subst">$&#123;homePage&#125;</span><span class="hljs-subst">$&#123;Default&#125;</span>"</span>
    echo -e <span class="hljs-string">"================================================\n"</span>
&#125;

echo -e <span class="hljs-string">"\n"</span>
<span class="hljs-keyword">while</span> [ <span class="hljs-string">"$confirmed"</span> != <span class="hljs-string">"y"</span> -a <span class="hljs-string">"$confirmed"</span> != <span class="hljs-string">"Y"</span> ]
<span class="hljs-keyword">do</span>
    <span class="hljs-keyword">if</span> [ <span class="hljs-string">"$confirmed"</span> == <span class="hljs-string">"n"</span> -o <span class="hljs-string">"$confirmed"</span> == <span class="hljs-string">"N"</span> ]; then
        getInfomation
    fi
    <span class="hljs-keyword">read</span> -p <span class="hljs-string">"confirm? (y/n):"</span> confirmed
done

<span class="hljs-keyword">mkdir</span> -p <span class="hljs-string">"../<span class="hljs-subst">$&#123;projectName&#125;</span>/<span class="hljs-subst">$&#123;projectName&#125;</span>"</span>

licenseFilePath=<span class="hljs-string">"../<span class="hljs-subst">$&#123;projectName&#125;</span>/FILE_LICENSE"</span>
gitignoreFilePath=<span class="hljs-string">"../<span class="hljs-subst">$&#123;projectName&#125;</span>/.gitignore"</span>
specFilePath=<span class="hljs-string">"../<span class="hljs-subst">$&#123;projectName&#125;</span>/<span class="hljs-subst">$&#123;projectName&#125;</span>.podspec"</span>
readmeFilePath=<span class="hljs-string">"../<span class="hljs-subst">$&#123;projectName&#125;</span>/readme.md"</span>
uploadFilePath=<span class="hljs-string">"../<span class="hljs-subst">$&#123;projectName&#125;</span>/upload.sh"</span>
podfilePath=<span class="hljs-string">"../<span class="hljs-subst">$&#123;projectName&#125;</span>/Podfile"</span>

echo <span class="hljs-string">"copy to $licenseFilePath"</span>
cp -f ./templates/FILE_LICENSE <span class="hljs-string">"$licenseFilePath"</span>
echo <span class="hljs-string">"copy to $gitignoreFilePath"</span>
cp -f ./templates/gitignore    <span class="hljs-string">"$gitignoreFilePath"</span>
echo <span class="hljs-string">"copy to $specFilePath"</span>
cp -f ./templates/pod.podspec  <span class="hljs-string">"$specFilePath"</span>
echo <span class="hljs-string">"copy to $readmeFilePath"</span>
cp -f ./templates/readme.md    <span class="hljs-string">"$readmeFilePath"</span>
echo <span class="hljs-string">"copy to $uploadFilePath"</span>
cp -f ./templates/upload.sh    <span class="hljs-string">"$uploadFilePath"</span>
echo <span class="hljs-string">"copy to $podfilePath"</span>
cp -f ./templates/Podfile      <span class="hljs-string">"$podfilePath"</span>

echo <span class="hljs-string">"editing..."</span>
sed -i <span class="hljs-string">""</span> <span class="hljs-string">"s%__ProjectName__%$&#123;projectName&#125;%g"</span> <span class="hljs-string">"$gitignoreFilePath"</span>
sed -i <span class="hljs-string">""</span> <span class="hljs-string">"s%__ProjectName__%$&#123;projectName&#125;%g"</span> <span class="hljs-string">"$readmeFilePath"</span>
sed -i <span class="hljs-string">""</span> <span class="hljs-string">"s%__ProjectName__%$&#123;projectName&#125;%g"</span> <span class="hljs-string">"$uploadFilePath"</span>
sed -i <span class="hljs-string">""</span> <span class="hljs-string">"s%__ProjectName__%$&#123;projectName&#125;%g"</span> <span class="hljs-string">"$podfilePath"</span>

sed -i <span class="hljs-string">""</span> <span class="hljs-string">"s%__ProjectName__%$&#123;projectName&#125;%g"</span> <span class="hljs-string">"$specFilePath"</span>
sed -i <span class="hljs-string">""</span> <span class="hljs-string">"s%__HomePage__%$&#123;homePage&#125;%g"</span>      <span class="hljs-string">"$specFilePath"</span>
sed -i <span class="hljs-string">""</span> <span class="hljs-string">"s%__HTTPSRepo__%$&#123;httpsRepo&#125;%g"</span>    <span class="hljs-string">"$specFilePath"</span>
echo <span class="hljs-string">"edit finished"</span>

echo <span class="hljs-string">"cleaning..."</span>
cd ../$projectName
git init
git remote add origin $httpsRepo  &> <span class="hljs-regexp">/dev/null</span>
git rm -rf --cached ./Pods/     &> <span class="hljs-regexp">/dev/null</span>
git rm --cached Podfile.lock    &> <span class="hljs-regexp">/dev/null</span>
git rm --cached .DS_Store       &> <span class="hljs-regexp">/dev/null</span>
git rm -rf --cached $projectName.xcworkspace/           &> <span class="hljs-regexp">/dev/null</span>
git rm -rf --cached $projectName.xcodeproj/xcuserdata/<span class="hljs-string">`whoami`</span>.xcuserdatad/xcschemes/$projectName.xcscheme &> <span class="hljs-regexp">/dev/null</span>
git rm -rf --cached $projectName.xcodeproj/project.xcworkspace/xcuserdata/ &> <span class="hljs-regexp">/dev/null</span>
git add . &> <span class="hljs-regexp">/dev/null</span>
git commit -m <span class="hljs-string">"first commit"</span> &> <span class="hljs-regexp">/dev/null</span>
git <span class="hljs-keyword">push</span> -u origin master &> <span class="hljs-regexp">/dev/null</span>
echo <span class="hljs-string">"clean finished"</span>
<span class="hljs-keyword">say</span> <span class="hljs-string">"finished"</span>
echo <span class="hljs-string">"finished"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">templates</h4>
<blockquote>
<p>提供初始化上传到CocoaPods仓库模块工程的配置文件模板。</p>
<p>该模板提供了最基础的配置信息。</p>
</blockquote>
<ul>
<li>
<h4 data-id="heading-7">pod.podspec模板</h4>
<blockquote>
<p>初始化私有库模块的podspec文件，为后续模块上传到私有仓库初始化基本配置。</p>
</blockquote>
<pre><code class="hljs language-ruby copyable" lang="ruby">Pod::Spec.new <span class="hljs-keyword">do</span> <span class="hljs-params">|s|</span>

    s.name         = <span class="hljs-string">"__ProjectName__"</span>
    s.version      = <span class="hljs-string">"1.0.0"</span>
    s.summary      = <span class="hljs-string">"__ProjectName__."</span>
    s.description  = <span class="hljs-string"><<-DESC
                      this is __ProjectName__
                     DESC</span>
    s.homepage     = <span class="hljs-string">"__HomePage__"</span>
    s.license      = &#123; <span class="hljs-symbol">:type</span> => <span class="hljs-string">"MIT"</span>, <span class="hljs-symbol">:file</span> => <span class="hljs-string">"FILE_LICENSE"</span> &#125;
    s.author             = &#123; <span class="hljs-string">"王传海"</span> => <span class="hljs-string">"ishadoo@163.com"</span> &#125;
    s.platform     = <span class="hljs-symbol">:ios</span>, <span class="hljs-string">"10.0"</span>
    s.source       = &#123; <span class="hljs-symbol">:git</span> => <span class="hljs-string">"__HTTPSRepo__"</span>, <span class="hljs-symbol">:tag</span> => s.version &#125;
    s.source_files  = <span class="hljs-string">"__ProjectName__/__ProjectName__/**/*.&#123;h,m&#125;"</span>
    s.requires_arc = <span class="hljs-literal">true</span>
  
  <span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-8">Podfile模板</h4>
<blockquote>
<p>初始项目的Podfile文件</p>
</blockquote>
<pre><code class="hljs language-perl copyable" lang="perl"><span class="hljs-comment"># Uncomment this line to define a global platform for your project</span>
platform :ios, <span class="hljs-string">'10.0'</span>

source <span class="hljs-string">'https://gitee.com/ishadoo/Specs.git'</span>
source <span class="hljs-string">'https://github.com/CocoaPods/Specs.git'</span>

target <span class="hljs-string">'__ProjectName__'</span> <span class="hljs-keyword">do</span>

end
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-9">upload脚本模板</h4>
<blockquote>
<p>初始化模块上传脚本，需要根据本地repo修改文件中对应的repo名称和私有仓库地址</p>
</blockquote>
<pre><code class="hljs language-perl copyable" lang="perl">pod repo <span class="hljs-keyword">push</span> ishadoo-specs __ProjectName_<span class="hljs-number">_</span>.podspec --verbose --allow-warnings --<span class="hljs-keyword">use</span>-libraries --sources=<span class="hljs-string">'https://gitee.com/ishadoo/Specs.git,https://github.com/CocoaPods/Specs.git'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-10">项目实战</h2>
<blockquote>
<p>由于公司git仓库的隐私性以及安全性方面的考虑，本教程以gitee仓库为例，手摸手教大家如何从零搭建一个iOS模块化架构。</p>
</blockquote>
<h3 data-id="heading-11">准备ModuleConfig</h3>
<blockquote>
<p>我的项目路径是：~/code/private/CHShare.</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> <span class="hljs-built_in">cd</span> ~/code/private/CHShare</span>
<span class="hljs-meta">$</span><span class="bash"> git <span class="hljs-built_in">clone</span> https://gitee.com/ishadoo/CHModuleConfig.git</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">创建远程项目地址</h3>
<blockquote>
<p>远程仓库根据自己的项目环境去选择，教程中我用的是gitee.</p>
</blockquote>
<img alt="image-20210310111012567" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c467e5eb3ab44d23bcff34c28feb4960~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h3 data-id="heading-13">创建Xcode本地工程</h3>
<blockquote>
<p>工程名要与远端工程名称相同，创建时直接复制远端工程名即可，且路径与ModuleConfig平级</p>
</blockquote>
<img alt="image-20210310113219431" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07e1c4b90e694c69873ce27309ba0db1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<blockquote>
<p>此时项目目录结构中多了我们刚创建的CHShareThird工程</p>
</blockquote>
<img alt="image-20210310113515511" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/972cf83196f94336a0797f84c6a2d5d6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h3 data-id="heading-14">利用CHModuleConfig初始化工程并上传到远程仓库</h3>
<blockquote>
<p>这一步的主要任务是，将本地工程初始化为由CocoaPods管理的工程。</p>
<p>同时将该项目同步到git远程仓库。</p>
<p>终端下cd到CHModuleConfig根目录，执行初始化配置脚本 config.sh。</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell">~ » cd /Users/wangchuanhai/code/private/CHShare/CHModuleConfig  
---------------------------------------------------------------------------------------------------------------------------------
~/code/private/CHShare/CHModuleConfig(master*) » ll  
total 32
-rw-r--r--  1 wangchuanhai  staff   1.0K  3  7 14:24 LICENSE
-rw-r--r--  1 wangchuanhai  staff   839B  3  7 14:24 README.en.md
-rw-r--r--  1 wangchuanhai  staff   928B  3  7 14:24 README.md
-rwxr-xr-x  1 wangchuanhai  staff   3.2K  3  7 14:04 config.sh
drwxr-xr-x  6 wangchuanhai  staff   192B  3  7 14:06 templates
---------------------------------------------------------------------------------------------------------------------------------
~/code/private/CHShare/CHModuleConfig(master*) » ./config.sh 


Enter Project Name: CHShareThird
Enter HTTPS Repo URL: https://gitee.com/ishadoo/CHShareThird.git
Enter SSH Repo URL: git@gitee.com:ishadoo/CHShareThird.git
Enter Home Page URL: https://gitee.com/ishadoo/CHShareThird    

================================================
  Project Name  :  CHShareThird
  HTTPS Repo    :  https://gitee.com/ishadoo/CHShareThird.git
  SSH Repo      :  git@gitee.com:ishadoo/CHShareThird.git
  Home Page URL :  https://gitee.com/ishadoo/CHShareThird
================================================

confirm? (y/n):y
copy to ../CHShareThird/FILE_LICENSE
cp: ./templates/FILE_LICENSE: No such file or directory
copy to ../CHShareThird/.gitignore
cp: ./templates/gitignore: No such file or directory
copy to ../CHShareThird/CHShareThird.podspec
copy to ../CHShareThird/readme.md
cp: ./templates/readme.md: No such file or directory
copy to ../CHShareThird/upload.sh
copy to ../CHShareThird/Podfile
editing...
sed: ../CHShareThird/.gitignore: No such file or directory
sed: ../CHShareThird/readme.md: No such file or directory
edit finished
cleaning...
Initialized empty Git repository in /Users/wangchuanhai/code/private/CHShare/CHShareThird/.git/
clean finished
finished
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>切换到CHShareThird工程，发现多了三个文件</strong></p>
<ul>
<li>
<h5 data-id="heading-15">CHShareThird.podspec</h5>
</li>
<li>
<h5 data-id="heading-16">Podfile</h5>
</li>
<li>
<h5 data-id="heading-17">upload.sh</h5>
</li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">~/code/private/CHShare/CHModuleConfig(master*) » cd .. 
---------------------------------------------------------------------------------------------------------------------------------
~/code/private/CHShare » ll                                                                                       
total 0
drwxr-xr-x   9 wangchuanhai  staff   288B  3  7 14:25 CHModuleConfig
drwxr-xr-x  18 wangchuanhai  staff   576B  3  9 17:36 CHShareDesk
drwxr-xr-x  18 wangchuanhai  staff   576B  3 10 00:39 CHShareHome
drwxr-xr-x  16 wangchuanhai  staff   512B  3  8 00:25 CHShareMaster
drwxr-xr-x  18 wangchuanhai  staff   576B  3  9 15:15 CHShareMine
drwxr-xr-x   8 wangchuanhai  staff   256B  3 10 11:43 CHShareThird
---------------------------------------------------------------------------------------------------------------------------------
~/code/private/CHShare » cd CHShareThird                                                                          
---------------------------------------------------------------------------------------------------------------------------------
~/code/private/CHShare/CHShareThird(master) » ll                                                                  
total 24
drwxr-xr-x  12 wangchuanhai  staff   384B  3 10 11:32 CHShareThird
-rw-r--r--   1 wangchuanhai  staff   643B  3 10 11:43 CHShareThird.podspec
drwxr-xr-x@  5 wangchuanhai  staff   160B  3 10 11:32 CHShareThird.xcodeproj
-rw-r--r--   1 wangchuanhai  staff   213B  3 10 11:43 Podfile
-rw-r--r--   1 wangchuanhai  staff   178B  3 10 11:43 upload.sh
---------------------------------------------------------------------------------------------------------------------------------
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">执行CocoaPods的项目初始化</h3>
<blockquote>
<p>cd 到项目根目录，执行pod install</p>
</blockquote>
<pre><code class="hljs language-sh copyable" lang="sh">$ pod install
<span class="copy-code-btn">复制代码</span></code></pre>
<img alt="image-20210310150153465" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93d5109768d64bd9bc8c419040d38e10~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h3 data-id="heading-19">创建源码SDK</h3>
<blockquote>
<p>模块化工程的源码以SDK的形式提供给宿主工程（也就是模块工程本身）和主App以及其他需要依赖的工程。</p>
<p>选择初始化好的工程，用Xcode打开，File -> New -> Target -> Framework</p>
<p>Product Name: $&#123;projectName&#125; + SDK</p>
</blockquote>
<img alt="image-20210310150722446" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64d4809b34dc43fb9ad9bdc48e3b9767~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h3 data-id="heading-20">创建资源bundle</h3>
<blockquote>
<p>Resource bundle作为单独的Target为SDK提供静态资源等的支持。</p>
<p>File -> New -> Target -> 选择macOS模块下的Bundle。由于Xcode只支持在macOS下创建bundle，故选择macOS模块下的Bundle选项。</p>
<p>Product Name: $&#123;projectName&#125; + Bundle</p>
</blockquote>
<img alt="image-20210310151706958" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/139af3118d6d438f8a69caf649524806~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<blockquote>
<p>在刚创建好的CHShareThirdBundle文件夹下新建Assets.xcassets文件，作为图片等静态资源的容器。</p>
<p>另外，要将CHShareThirdBundle Targets的Base SDK属性修改成iOS支持。</p>
<p>需特别注意的，resource bundle这个SDK中需要将info.plist文件中的Executable file选项移除，不然会出现获取不到文件的情况。</p>
</blockquote>
<img alt="image-20210310152358111" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2ce0695ba1d46749285ccf766dd1bbb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h3 data-id="heading-21">创建framework脚本</h3>
<blockquote>
<p>将编译好的framework文件和bundle文件从模拟器的沙盒目录拷贝至工程的根路径，以方便CocoaPods上传到私有仓库。</p>
<p>File -> New -> Target -> 选择Other下的Aggregate。</p>
</blockquote>
<img alt="image-20210310154437480" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bb3bbee42fc4204bf131c8799171c06~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<blockquote>
<p>添加执行脚本</p>
</blockquote>
<img alt="image-20210310171924524" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c24e7c9b8b745a2859789532a39a5c9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash">!/bin/sh</span>
<span class="hljs-meta">#</span><span class="bash">要build的target名</span>
TARGET_NAME=$&#123;PROJECT_NAME&#125;
if [[ $1 ]]
then
TARGET_NAME=$1
fi
UNIVERSAL_OUTPUT_FOLDER="$&#123;SRCROOT&#125;/$&#123;PROJECT_NAME&#125;Upload/"
<span class="hljs-meta">
#</span><span class="bash">创建输出目录，并删除之前的framework文件</span>
rm -rf "$&#123;UNIVERSAL_OUTPUT_FOLDER&#125;"
mkdir -p "$&#123;UNIVERSAL_OUTPUT_FOLDER&#125;"
<span class="hljs-meta">
#</span><span class="bash">编译模拟器的Framework</span>
xcodebuild -target "$&#123;TARGET_NAME&#125;SDK" ONLY_ACTIVE_ARCH=NO -configuration $&#123;CONFIGURATION&#125; -sdk iphonesimulator BUILD_DIR="$&#123;BUILD_DIR&#125;" BUILD_ROOT="$&#123;BUILD_ROOT&#125;" clean build
<span class="hljs-meta">
#</span><span class="bash">拷贝framework到univer目录</span>
cp -R "$&#123;BUILD_DIR&#125;/$&#123;CONFIGURATION&#125;-iphonesimulator/$&#123;TARGET_NAME&#125;SDK.framework" "$&#123;UNIVERSAL_OUTPUT_FOLDER&#125;"
<span class="hljs-meta">#</span><span class="bash">拷贝bundle到univer目录</span>
cp -R "$&#123;BUILD_DIR&#125;/$&#123;CONFIGURATION&#125;-iphonesimulator/$&#123;TARGET_NAME&#125;Bundle.bundle" "$&#123;UNIVERSAL_OUTPUT_FOLDER&#125;"
<span class="hljs-meta">
#</span><span class="bash">打开合并后的文件夹</span>
open "$&#123;UNIVERSAL_OUTPUT_FOLDER&#125;"

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>到此一个模块的基本配置工作就算完成，接下来需要调整一下资源的依赖关系，从系统层面不难理解，Demo工程（也就是模块项目本身）依赖SDK工程，SDK依赖Bundle资源。</p>
<p>接下来，就可以开开心心地撸代码了。</p>
</blockquote>
<h3 data-id="heading-22">构建Cocoapods版本</h3>
<h4 data-id="heading-23">podspec文件</h4>
<blockquote>
<p>修改version版本号，要与最终提交到git上的代码tag保持一致</p>
<p>增加vendored_frameworks指向工程根目录中script脚本拷贝的framework和bundle资源</p>
<p>添加工程中所依赖的第三方库和系统库等</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell">Pod::Spec.new do |s|

    s.name         = "CHShareThird"
    s.version      = "1.0.20210310"
    s.summary      = "CHShareThird."
    s.description  = <<-DESC
                      this is CHShareThird
                     DESC
    s.homepage     = "https://gitee.com/ishadoo/CHShareThird"
    s.license      = &#123; :type => "MIT", :file => "FILE_LICENSE" &#125;
    s.author             = &#123; "王传海" => "ishadoo@163.com" &#125;
    s.platform     = :ios, "10.0"
    s.source       = &#123; :git => "https://gitee.com/ishadoo/CHShareThird.git", :tag => s.version &#125;

    ## 源码形式集成
    # s.source_files  = "CHShareThird/CHShareThird/**/*.&#123;h,m&#125;"

    ## 是否支持ARC
    s.requires_arc = true

    ## 构建的模块类型
    s.vendored_frameworks = "CHShareThirdUpload/CHShareThirdSDK.framework"
    s.resources = "CHShareThirdUpload/CHShareThirdBundle.bundle"

    ## 依赖的第三方库以及framework资源
    s.dependency "Masonry"
    s.framework = "UIKit"
  
  end
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">upload.sh文件</h4>
<blockquote>
<p>如下图所示，项目中添加一个UIViewController作为NavigationControler根视图，现将该模块封板上传到CocoaPods私有库。</p>
</blockquote>
<img alt="image-20210310164637477" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1857b45e06fb4786b4422ab99a6f46e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<blockquote>
<p>编译通过后，先执行framework 拷贝脚本，然后执行该脚本构建到远端CocoaPods库.</p>
</blockquote>
<h4 data-id="heading-25">执行前</h4>
<img alt="image-20210310165720631" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68c4c9ff6887447ea6335d0950071567~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h4 data-id="heading-26">执行后</h4>
<blockquote>
<p>脚本执行后在项目的根目录多了一个CHShareThirdUpload文件夹，其中包含CHShareThirdSDK.framework和CHShareThirdBundle.bundle这两个文件</p>
</blockquote>
<img alt="image-20210310172434931" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06ff3b334c0b49b2ba5846c8d45cfe5d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<blockquote>
<p>代码封板，将代码上传到远程仓库，同时封版打tag，tag号要与CHShareThird.podspec中的version相一致。</p>
<p>此时准备工作完成。</p>
<p>执行upload.sh</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell">~/code/private/CHShare/CHShareThird(master) » ll   
total 56
drwxr-xr-x  8 wangchuanhai  staff   256B  3 10 16:39 CHShareThird
-rw-r--r--  1 wangchuanhai  staff   979B  3 10 17:13 CHShareThird.podspec
drwxr-xr-x@ 5 wangchuanhai  staff   160B  3 10 16:41 CHShareThird.xcodeproj
drwxr-xr-x@ 5 wangchuanhai  staff   160B  3 10 15:05 CHShareThird.xcworkspace
drwxr-xr-x  4 wangchuanhai  staff   128B  3 10 15:29 CHShareThirdBundle
drwxr-xr-x  6 wangchuanhai  staff   192B  3 10 16:25 CHShareThirdSDK
-rw-r--r--@ 1 wangchuanhai  staff   1.1K  2 24 15:18 FILE_LICENSE
-rw-r--r--@ 1 wangchuanhai  staff   232B  3 10 16:33 Podfile
-rw-r--r--  1 wangchuanhai  staff   270B  3 10 16:34 Podfile.lock
drwxr-xr-x  8 wangchuanhai  staff   256B  3 10 16:34 Pods
-rw-r--r--  1 wangchuanhai  staff   956B  3 10 14:53 README.en.md
-rw-r--r--  1 wangchuanhai  staff   1.3K  3 10 14:53 README.md
-rw-r--r--  1 wangchuanhai  staff   178B  3 10 14:50 upload.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>执行脚本有时会出现执行权限问题，此时需要对upload.sh脚本授权</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell">~/code/private/CHShare/CHShareThird(master) » ./upload.sh         
zsh: permission denied: ./upload.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>授权</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell">~/code/private/CHShare/CHShareThird(master) » chmod +x upload.sh  
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>再次执行脚本</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell">~/code/private/CHShare/CHShareThird(master*) » ./upload.sh 
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>经过漫长的编译，会收到成功上传的信息，部分编译信息如下，</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"> ** BUILD SUCCEEDED **
    
   Testing with `xcodebuild`. 
<span class="hljs-meta"> -></span><span class="bash"> CHShareThird (1.0.2021031001)</span>
    - NOTE  | xcodebuild:  note: Using new build system
    - NOTE  | xcodebuild:  note: Building targets in parallel
    - NOTE  | xcodebuild:  note: Using codesigning identity override: -
    - NOTE  | [iOS] xcodebuild:  note: Planning build
    - NOTE  | [iOS] xcodebuild:  note: Constructing build description
    - NOTE  | [iOS] xcodebuild:  warning: The iOS Simulator deployment target 'IPHONEOS_DEPLOYMENT_TARGET' is set to 6.0, but the range of supported deployment target versions is 9.0 to 14.4.99. (in target 'Masonry' from project 'Pods')
    - NOTE  | [iOS] xcodebuild:  warning: Skipping code signing because the target does not have an Info.plist file and one is not being generated automatically. (in target 'App' from project 'App')
    - NOTE  | [iOS] xcodebuild:  ld: warning: ignoring file CHShareThird/CHShareThirdUpload/CHShareThirdSDK.framework/CHShareThirdSDK, building for iOS Simulator-i386 but attempting to link with file built for iOS Simulator-x86_64
    - NOTE  | [iOS] xcodebuild:  ld: warning: ignoring file CHShareThird/CHShareThirdUpload/CHShareThirdSDK.framework/CHShareThirdSDK, building for iOS Simulator-arm64 but attempting to link with file built for iOS Simulator-x86_64

Updating the `ishadoo-specs' repo
<span class="hljs-meta">
  $</span><span class="bash"> /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs pull</span>
  Already up to date.

Adding the spec to the `ishadoo-specs' repo
<span class="hljs-meta">
  $</span><span class="bash"> /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs status --porcelain</span>
  ?? CHShareThird/
 - [Add] CHShareThird (1.0.2021031001)
<span class="hljs-meta">  $</span><span class="bash"> /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs add CHShareThird</span>
<span class="hljs-meta">  $</span><span class="bash"> /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs commit --no-verify -m [Add] CHShareThird (1.0.2021031001)</span>
  [master 95fe617] [Add] CHShareThird (1.0.2021031001)
   1 file changed, 29 insertions(+)
   create mode 100644 CHShareThird/1.0.2021031001/CHShareThird.podspec

Pushing the `ishadoo-specs' repo
<span class="hljs-meta">
  $</span><span class="bash"> /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs push origin HEAD</span>
  remote: Powered by GITEE.COM [GNK-5.0]        
  To https://gitee.com/ishadoo/Specs.git
     468cfbb..95fe617  HEAD -> master

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>至此，CHShareThird模块的第一个版本就成功上传到Cocoapods私有仓库。</p>
</blockquote>
<h3 data-id="heading-27">查看远程仓库</h3>
<blockquote>
<p>跟踪一下远程仓库，不难发现新建的CHShareThird模块已经成功上传我们的私有仓库。</p>
</blockquote>
<img alt="image-20210310174514089" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6313c709f8e648e8acfb04386825a9b9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="image-20210310174544669" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b4aeb7ca5344435a3b21ec079243cec~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h3 data-id="heading-28">使用CHShareThird模块</h3>
<blockquote>
<p>在该主App的Podflie文件中添加如下依赖   pod 'CHShareThird'</p>
</blockquote>
<pre><code class="hljs language-perl copyable" lang="perl"><span class="hljs-comment"># Uncomment this line to define a global platform for your project</span>
platform :ios, <span class="hljs-string">'10.0'</span>

source <span class="hljs-string">'https://gitee.com/ishadoo/Specs.git'</span>
source <span class="hljs-string">'https://github.com/CocoaPods/Specs.git'</span>
source <span class="hljs-string">'https://gitee.com/ishadoo/CHShareMine.git'</span>

target <span class="hljs-string">'CHShareMaster'</span> <span class="hljs-keyword">do</span>
  pod <span class="hljs-string">'CHShareHome'</span>
  pod <span class="hljs-string">'CHShareMine'</span>, :<span class="hljs-string">git =></span> <span class="hljs-string">'https://gitee.com/ishadoo/CHShareMine.git'</span>, :<span class="hljs-string">branch =></span> <span class="hljs-string">'develop'</span>
  pod <span class="hljs-string">'CHShareDesk'</span>
  pod <span class="hljs-string">'CHShareThird'</span>
end

target <span class="hljs-string">'CHShareSDK'</span> <span class="hljs-keyword">do</span>
  pod <span class="hljs-string">'CHShareHome'</span>
  pod <span class="hljs-string">'CHShareMine'</span>, :<span class="hljs-string">git =></span> <span class="hljs-string">'https://gitee.com/ishadoo/CHShareMine.git'</span>, :<span class="hljs-string">branch =></span> <span class="hljs-string">'develop'</span>
  pod <span class="hljs-string">'CHShareDesk'</span>
  pod <span class="hljs-string">'CHShareThird'</span>
end
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">执行pod update</h3>
<pre><code class="hljs language-perl copyable" lang="perl">~<span class="hljs-regexp">/code/pri</span>vate/CHShare/CHShareMaster(develop*) » pod update
Update all pods
Updating <span class="hljs-keyword">local</span> specs repositories
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs fetch origin --progress
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs rev-parse --abbrev-<span class="hljs-keyword">ref</span> HEAD
  master
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/ishadoo-specs <span class="hljs-keyword">reset</span> --hard origin/master
  HEAD is now at <span class="hljs-number">95</span>fe617 [Add] CHShareThird (<span class="hljs-number">1.0</span>.<span class="hljs-number">2021031001</span>)
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/master fetch origin --progress
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/master rev-parse --abbrev-<span class="hljs-keyword">ref</span> HEAD
  master
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/master <span class="hljs-keyword">reset</span> --hard origin/master
  HEAD is now at <span class="hljs-number">5</span>b4b6eecd2f8 [Add] TCNetwork <span class="hljs-number">0</span>.<span class="hljs-number">2.2</span>
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/gitee-ishadoo-chsharemine fetch origin --progress
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/gitee-ishadoo-chsharemine rev-parse --abbrev-<span class="hljs-keyword">ref</span> HEAD
  master
  $ /usr/bin/git -C /Users/wangchuanhai/.cocoapods/repos/gitee-ishadoo-chsharemine <span class="hljs-keyword">reset</span> --hard origin/master
  HEAD is now at ec3e546 update
Analyzing dependencies
Pre-downloading: <span class="hljs-string">`CHShareMine`</span> from <span class="hljs-string">`https://gitee.com/ishadoo/CHShareMine.git`</span>, branch <span class="hljs-string">`develop`</span>
Downloading dependencies
Installing CHShareMine <span class="hljs-number">1.0</span>.<span class="hljs-number">2021030901</span>
Installing CHShareThird (<span class="hljs-number">1.0</span>.<span class="hljs-number">2021031001</span>)
Generating Pods project
Integrating client project
Pod installation complete! There are <span class="hljs-number">4</span> dependencies from the Podfile <span class="hljs-keyword">and</span> <span class="hljs-number">5</span> total pods installed.
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>此时CHShareThird成功地添加到了主App当中。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            