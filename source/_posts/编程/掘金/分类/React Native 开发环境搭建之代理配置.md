
---
title: 'React Native 开发环境搭建之代理配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8474'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 19:42:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=8474'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>此文记录基于mac搭建开发环境中遇到代理问题，希望能帮到遇到相似问题的人。</p>
<p>最近学习React Native开发，在按照<a href="https://reactnative.cn/docs/environment-setup" target="_blank" rel="nofollow noopener noreferrer">官网</a>指导下，安装环境配置顺利进行，直到创建新项目这一步，CocoaPods 的依赖安装步骤卡很久，故不得不配置<a href="https://3600.ml/auth/register?code=k38B" target="_blank" rel="nofollow noopener noreferrer">代理</a>，以便能继续下去。</p>
<blockquote>
<p>1.已知inter处理器的mac电脑安装代理时无需更新（客户端以及配置文件），切记！！！<br>
2.代理开启‘设置为系统代理’之后，可以接管桌面应用，终端是例外，需要如下自行配置（永久使用代理）。<br>
3.菜单栏，点击代理应用图标，选择‘复制终端代理命令’，以备后用。</p>
</blockquote>
<ol>
<li>查看、编辑配置文件（进入当前用户的home目录(默认就是)）</li>
</ol>
<pre><code class="copyable">配置.bash_profile
 （1）终端输入 open -e .bash_profile 
   （文件存在则自动打开，尚未创建请参考  4.创建文件）
   （如果只是查看，直接使用open .bash_profile）

 （2）编辑
     新起一行，将终端代理命令粘贴进来。

 （3）关闭即可保存修改

 （4）更新刚配置的环境变量
     source ~/.bash_profile
 
 
配置.zshrc
 （1）终端输入 open -e .zshrc 
   （文件存在则自动打开，尚未创建请参考  4.创建文件）
   （如果只是查看，直接使用open .zshrc）

 （2）编辑
     新起一行，将终端代理命令粘贴进来。

 （3）关闭即可保存修改

 （4）更新刚配置的环境变量
     source ~/.zshrc
 
 

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>查看当前代理参数配置</li>
</ol>
<pre><code class="copyable">echo $http_proxy;
echo $https_proxy;
echo $all_proxy;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>测试代理是否成功（不能通过ping检测，ping不会走代理;curl系统一般内置）</li>
</ol>
<pre><code class="copyable">curl -I https://twitter.com
代理成功输出内容包含
    HTTP/1.1 200 Connection established
    
    HTTP/2 200 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>创建文件</li>
</ol>
<pre><code class="copyable"> （1） 启动终端


 （2） 进入当前用户的home目录(默认就是)： 
        cd ~   或 cd /Users/YourMacUserName  

 （3）输入touch 文件名，如 touch .bash_profile
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            