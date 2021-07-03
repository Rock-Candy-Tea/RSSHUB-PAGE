
---
title: 'git 的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=104'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 06:56:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=104'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://www.liaoxuefeng.com/wiki/896043488029600" target="_blank" rel="nofollow noopener noreferrer">git教程</a></p>
<p><a href="https://gitee.com/all-about-git" target="_blank" rel="nofollow noopener noreferrer">git常用命令</a></p>
<ol>
<li>安装git之后首先进行git配置：</li>
</ol>
<pre><code class="copyable">git config --global user.name "屠永涛"
git config --global user.email "***@qq.com" 
// 后续如需针对单个项目进行配置，执行如下
git config user.email "***@qq.com" 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建项目流程如下：</p>
<ol>
<li>创建项目后执行如下命令</li>
</ol>
<pre><code class="copyable">git init // 将当前目录变为git可管理的本地仓库
git add . // 将所有文件从工作区添加到暂存区
git commit -m "首次提交"  // 把暂存区文件提交到本地仓库
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>创建远程仓库（要求远程仓库名与本地仓库名相同）,获取远程仓库地址：例如 <a href="https://gitee.com/tuyongtao/vuepress-blog.git%EF%BC%8C" target="_blank" rel="nofollow noopener noreferrer">gitee.com/tuyongtao/v…</a> 然后执行如下命令</li>
</ol>
<pre><code class="copyable">git remote add https://gitee.com/tuyongtao/vuepress-blog.git // 关联一个远程库
git push -u origin master // 第一次推送，远程库是空的，所以加 -u  
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>当电脑第一次使用Git的clone或者push命令连接GitHub时，会得到一个警告：</li>
</ol>
<pre><code class="copyable">The authenticity of host 'github.com (xx.xx.xx.xx)' can't be established.
RSA key fingerprint is xx.xx.xx.xx.xx.
Are you sure you want to continue connecting (yes/no)?
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是因为Git使用SSH连接，而SSH连接在第一次验证GitHub服务器的Key时，需要你确认GitHub的Key的指纹信息是否真的来自GitHub的服务器，输入yes回车即可。</p>
<p>克隆项目流程如下</p>
<pre><code class="copyable">git clone https://gitee.com/tuyongtao/vuepress-blog.git
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            