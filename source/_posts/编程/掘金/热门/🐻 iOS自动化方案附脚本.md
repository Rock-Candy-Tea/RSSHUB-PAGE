
---
title: '🐻 iOS自动化方案附脚本'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=5038'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 18:41:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=5038'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">统一开发环境</h2>
<p>统一开发环境，减少因环境不同导致文件冲突。</p>
<p>具体实现：安装rbenv，管理ruby环境；安装Bundler，管理cocoapods、cocoapods插件、fastlane等。</p>
<h3 data-id="heading-1">环境搭建者需要配置以下内容：</h3>
<p>安装 Homebrew</p>
<pre><code class="copyable">/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 rbenv</p>
<pre><code class="copyable">brew install rbenv ruby-build rbenv-vars
<span class="copy-code-btn">复制代码</span></code></pre>
<p>放到你的 Shell 配置文件里面</p>
<pre><code class="copyable">export PATH="$HOME/.rbenv/bin:$PATH" 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">eval "$(rbenv init -)"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装和设置项目的 Ruby 环境</p>
<pre><code class="copyable">rbenv install 2.7.1
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">rbenv local 2.7.1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rbenv 会帮我们建立 一个叫作.ruby-version 的文件</p>
<h3 data-id="heading-2">其他人员执行以下脚本：</h3>
<pre><code class="copyable"># 在rbenv 下安装特定版本的 Ruby 开发环境

ruby_version=`cat .ruby-version`
if [[ ! -d "$HOME/.rbenv/versions/$ruby_version" ]]; then
  rbenv install $ruby_version;
fi

# 通过 RubyGems 安装 Bunlder

gem install bundler

# 使用 Bundler 安装 CocoaPods 和 fastlane 等依赖包

bundle install

# 安装各个 Pod

bundle exec pod install

<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此统一的环境搭建结束，对于xcode，只要不是差别很大就行，保持在一个大版本中就行，如：XCode12</p>
<p>命名该脚本为：setup.sh</p>
<h2 data-id="heading-3">配置fastlane</h2>
<p>Gemfile 中添加：</p>
<pre><code class="copyable"># frozen_string_literal: true
source "https://rubygems.org"

gem 'cocoapods', '1.10.1'

# 自动部署
gem 'fastlane', '2.179.0'

plugins_path = File.join(File.dirname(__FILE__), 'fastlane', 'Pluginfile')

eval_gemfile(plugins_path) if File.exist?(plugins_path)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行上述脚本 setup.sh</p>
<h2 data-id="heading-4">实用lane</h2>
<p>执行，创建自定义Fastlane文件</p>
<pre><code class="copyable">bundle exec fastlane init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fastlane 执行时，比较困难的是证书配置。</p>
<h3 data-id="heading-5">使用mach来管理证书</h3>
<p>首先，在github或者其他git平台，新建一个私有仓库。</p>
<pre><code class="copyable">  desc "拉取证书" 
  lane :mach_pp do
    # 证书管理
    match(
        git_url: "https://github.com/xxx/xxx.git",
        type: "adhoc" ,
        app_identifier:["com.xxx.xxx","com.xxx.xxx.push"],
        username:"xxx@163.com",
        team_id: "xxx"
        )
    match(
        git_url: "https://github.com/xxx/xxx.git",
        type: "appstore" ,#can be appstore,adhoc, development,enterprise
        app_identifier:["com.xxx.xxx","com.xxx.xxx.push"],
        username:"xxx@163.com",
        team_id: "xxx"
    )
  end 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>填入以上信息：git_url、type、app_identifier、username、team_id</p>
<p>其中：type分为adhoc、appstore</p>
<h3 data-id="heading-6">gym 打包</h3>
<pre><code class="copyable"> desc "发正式包到appstore"
  lane :ipa2apple do
    # gym用来编译ipa
    gym(
        scheme: 'XXX',
        configuration: "Release",
        export_method: "app-store", # 指定打包方式
        xcargs: "-allowProvisioningUpdates",
        archive_path: '../appstore',
        output_directory: './appstore',
        output_name: 'XXX.ipa'
    )
  end

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Pluginfile 管理插件</h3>
<h4 data-id="heading-8">安装fir插件</h4>
<pre><code class="copyable">fastlane add_plugin fir_cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用</p>
<pre><code class="copyable">firim(firim_api_token: "56d42c7266586d43dccad86730555c78")  # token 在fir 上查看。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">上传符号表</h4>
<p>安装firebase插件</p>
<pre><code class="copyable">fastlane add_plugin firebase_app_distribution

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用</p>
<pre><code class="copyable">  # fir 的 release 包 Crash report symbols
  desc 'Upload symbols to Crashlytics for Release app'
  lane :upload_symbols_to_crashlytics_release do
    upload_symbols_to_crashlytics(
      dsym_path: "./fir_release/xxx.app.dSYM.zip",
      gsp_path: "./xxx/GoogleService-Info_Beta.plist",
      api_token: ENV["FIREBASE_API_TOKEN"]
    )
  end
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">其他</h4>
<pre><code class="copyable">desc "准备工作 install"
  lane :ready do

    # 拉代码
    git_pull

    # 全局变量
    time = Time.new

    # build 号
    build_number = time.strftime("%Y%m%d%H%M%S")
    increment_build_number(&#123;
      build_number: build_number
    &#125;)

    git_commit(path:".", message:"[robot][auto build to #&#123;build_number&#125;]")
    sh 'git push origin main'    
  end
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">注意事项</h2>
<ul>
<li>
<p>使用undler工具管理后，以后执行pod 需要在前边加上 bundle exec</p>
</li>
<li>
<p>sync_code_signing命令，其实是match命令的另外一种写法</p>
</li>
<li>
<p>build_app命令其实是gym的别名</p>
</li>
<li>
<p>fastlane 常用的action以及参数 <a href="https://juejin.cn/post/6844903813262901255#heading-7" target="_blank">juejin.cn/post/684490…</a></p>
</li>
<li>
<p>zsh: permission denied问题的解决办法  sudo chmod u+x *.sh</p>
</li>
<li>
<p>sudo操作，如果遇到不明原因的错误，可能是权限问题，使用chmod 777 路径 尝试解决</p>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            