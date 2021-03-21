
---
title: 玩转cocoapods-plugins开发
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Sat, 20 Feb 2021 01:18:39 GMT
thumbnail: 
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><h4 data-id="heading-0">安装 cocoapods-plugins 组件</h4>
<pre><code class="hljs language-bash copyable" lang="bash">sudo gem install cocoapods-plugins 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">创建 Cocoapods Plugins 模版工程</h4>
<pre><code class="hljs language-bash copyable" lang="bash">pod plugins create hd
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>文件结构</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">├── Gemfile                      插件工程本身是用Bundler来管理项目依赖
├── LICENSE.txt                        
├── README.md
├── Rakefile                     rake默认执行spec目录下的spec文件执行用例自测
├── cocoapods-hd-<span class="hljs-number">0.0</span>.<span class="hljs-number">1</span>.gem
├── cocoapods-hd.gemspec         发布gem包需要的描述文件
├── lib
│   ├── cocoapods-hd
│   │   ├── command
│   │   │   └── hd.rb            插件实现文件
│   │   ├── command.rb
│   │   └── gem_version.rb
│   ├── cocoapods-hd.rb
│   └── cocoapods_plugin.rb
└── spec
    ├── command
    │   └── hd_spec.rb           默认帮你实现插件注册，可以在里面写用例测试插件
    └── spec_helper.rb
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>开发</p>
<pre><code class="hljs language-ruby copyable" lang="ruby"><span class="hljs-class"><span class="hljs-keyword">module</span> <span class="hljs-title">Pod</span></span>
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Command</span></span>
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Hd</span> < Command</span>
      <span class="hljs-keyword">self</span>.summary = <span class="hljs-string">'cocoapods-hd 功能简介'</span>

      <span class="hljs-keyword">self</span>.description = <span class="hljs-string"><<-DESC
        hd 插件测试功能描述
      DESC</span>

      <span class="hljs-comment"># self.arguments = 'NAME'</span>

      <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">initialize</span><span class="hljs-params">(argv)</span></span>
        <span class="hljs-variable">@name</span> = argv.shift_argument
        <span class="hljs-keyword">super</span>
      <span class="hljs-keyword">end</span>

      <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">validate!</span></span>
        <span class="hljs-keyword">super</span>
        help! <span class="hljs-string">'A Pod name is required.'</span> <span class="hljs-keyword">unless</span> <span class="hljs-variable">@name</span>
      <span class="hljs-keyword">end</span>

      <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">run</span></span>
        UI.puts <span class="hljs-string">"Add your implementation for the cocoapods-hd plugin in <span class="hljs-subst">#{<span class="hljs-keyword">__FILE__</span>}</span>"</span>
      <span class="hljs-keyword">end</span>
    <span class="hljs-keyword">end</span>
  <span class="hljs-keyword">end</span>
<span class="hljs-keyword">end</span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-2">编译插件</h4>
<pre><code class="hljs language-bash copyable" lang="bash">sudo gem build cocoapods-hd.gemspec
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">安装插件</h4>
<pre><code class="hljs language-bash copyable" lang="bash">sudo gem install cocoapods-hd-0.0.1.gem
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">查看是否安装成功</h4>
<pre><code class="hljs language-ruby copyable" lang="ruby">pod plugins installed
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">更新</h4>
<pre><code class="hljs language-bash copyable" lang="bash">sudo gem uninstall cocoapods-hd-0.0.1.gem && sudo gem build cocoapods-hd.gemspec  && sudo gem install cocoapods-hd-0.0.1.gem
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">使用VSCode/RubyMine调试</h2>
<ul>
<li>
<p>下载cocoapods源码</p>
</li>
<li>
<p>创建一个空目录debug-hd，然后添加Gemfile</p>
<blockquote>
<p>Gemfile文件、CocoaPods、cocoapods-hd、ios工程等都要放在debug-hd目录下</p>
</blockquote>
<pre><code class="hljs language-ruby copyable" lang="ruby">source <span class="hljs-string">'https://rubygems.org'</span>
gem <span class="hljs-string">'cocoapods'</span>, <span class="hljs-symbol">path:</span> <span class="hljs-string">'./CocoaPods'</span>
gem <span class="hljs-string">'cocoapods-hd'</span>, <span class="hljs-symbol">path:</span> <span class="hljs-string">'./cocoapods-hd'</span>
group <span class="hljs-symbol">:debug</span> <span class="hljs-keyword">do</span>
    gem <span class="hljs-string">'ruby-debug-ide'</span>
    gem <span class="hljs-string">'debase'</span>
 <span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在.vscode文件下，创建launch.json</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">{
    <span class="hljs-string">"version"</span>: <span class="hljs-string">"0.2.0"</span>,
    <span class="hljs-string">"configurations"</span>: [
        {
            <span class="hljs-string">"name"</span>: <span class="hljs-string">"install"</span>,
            <span class="hljs-string">"showDebuggerOutput"</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-string">"type"</span>: <span class="hljs-string">"Ruby"</span>,
            <span class="hljs-string">"request"</span>: <span class="hljs-string">"launch"</span>,
            <span class="hljs-string">"useBundler"</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-string">"cwd"</span>: <span class="hljs-string">"${workspaceRoot}/HDPodTest"</span>,<span class="hljs-regexp">//cwd</span>代表运行的目录，必须和gemfile一个目录。<span class="hljs-variable">${</span>workspaceRoot}指的是VSCode工程的目录
            <span class="hljs-string">"program"</span>: <span class="hljs-string">"~/Work/CocoaPods/bin/pod"</span>,<span class="hljs-regexp">//</span>这里指明的是cocoapods源码里面的bin目录下的pod
            <span class="hljs-string">"args"</span>: [
                <span class="hljs-string">"install"</span>, <span class="hljs-regexp">//</span>这里指明是pod程序的参数 install
                <span class="hljs-string">"verbose"</span> /<span class="hljs-regexp">/ 其他参数
            ],
            "stopOnEntry": false
        }
    ]
}
</span><span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>执行sudo bundle install</p>
</li>
<li>
<p>在plugin里面添加断点，然后按F5运行，就可以看到进入到plugin源码了</p>
</li>
<li>
<p>完整目录</p>
<pre><code class="copyable">├── Gemfile
├── Gemfile.lock
├── CocoaPods        官方源码
├── cocoapods-hd     插件代码
├── HDPodTest        ios工程，包含podfile
│── .vscode
│   ├── launch.json
└── bin
 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-7">其他</h2>
<h3 data-id="heading-8">How to install gems from Gemfile?</h3>
<p>sudo gem install bundler先安装bundler，然后执行bundle init 命令安装ruby库</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">source <span class="hljs-string">"https://rubygems.org"</span>  <span class="hljs-comment"># where gems will be downloaded from</span>
ruby <span class="hljs-string">"2.2.3"</span>  <span class="hljs-comment"># ruby version, change for the one you use</span>
gem <span class="hljs-string">'cocoapods'</span>
 
group <span class="hljs-symbol">:development</span> <span class="hljs-keyword">do</span>   <span class="hljs-comment"># you can make groups for test, development, production..</span>
  gem <span class="hljs-string">'mocha'</span>
 
<span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">安装/卸载已经发布的cocoapods插件</h4>
<pre><code class="hljs language-bash copyable" lang="bash">sudo gem install cocoapods-hd
sudo gem uninstall cocoapods-hd
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">安装指定版本bundler</h4>
<pre><code class="hljs language-ruby copyable" lang="ruby">sudo gem uninstall bundler -v=<span class="hljs-number">2.2</span>.<span class="hljs-number">11</span>
sudo gem install bundler -v=<span class="hljs-number">2.2</span>.<span class="hljs-number">11</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">参考</h4>
<p><a href="https://blog.csdn.net/weixin_39615984/article/details/111266779" target="_blank" rel="nofollow noopener noreferrer">vscode断点调试cocoapods plugin</a></p>
<p><a href="https://juejin.cn/post/6904204635309883405" target="_blank">juejin.cn/post/690420…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            