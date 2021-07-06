
---
title: 'Ansible 快速入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f9d2802f36a44359cbe8ca4ad4087ae~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 18:33:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f9d2802f36a44359cbe8ca4ad4087ae~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Ansible 是什么？</h2>
<p>Ansible是一个配置管理和配置工具，它使用SSH连接到服务器并运行配置好的任务，服务器上只需要开启ssh，所有工作都交给client端的ansible负责。</p>
<p>当我们有批量部署的需求时，我们可以自己写脚本，但是更推荐使用 Ansible。使用 Ansible 无需编码只需要配置 yaml 文件即可，并且 Ansible 已经内置了幂等性、并发度控制等功能，大大减少了批量部署时的工作量。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f9d2802f36a44359cbe8ca4ad4087ae~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Ansible 原理示意图如上，我们需要关注以下 3 点就能掌握 Ansible 的大致原理。第一，hosts 配置文件的作用是告诉 Ansible 你的程序要部署到哪些机器；第二，yaml 文件的作用是告诉 Ansible 在目标机器上执行哪些操作。第三，Ansible 不需要在目标机器上安装客户端，它通过 SSH 把指令和要部署的程序发送到目标机器上。</p>
<p><strong>安装 Ansile</strong></p>
<p>安装命令：</p>
<pre><code class="copyable">python3 -m pip install --user ansible==2.5.4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证安装是否正确：</p>
<pre><code class="copyable">ansible --version
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置 Ansible</strong></p>
<ul>
<li><strong>配置 .ansible.cfg 文件</strong></li>
</ul>
<p>.ansible.cfg 的路径：~/.ansible.cfg</p>
<p>将以下内容写入 .ansible.cfg 文件：</p>
<pre><code class="copyable">[defaults]
# inventory 是声明 hosts 配置文件
inventory=~/.ansible/hosts
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>SSH 使用密钥登录服务器</strong></li>
</ul>
<p>设置 SSH 通过密钥登录。使用 ssh-keygen 命令生成密钥对，把 id_rsa.pub 写入目标服务器的 authorized_keys 文件中。</p>
<ul>
<li><strong>编辑 hosts 文件</strong></li>
</ul>
<p>hosts 配置文件的格式是 ini。示例如下</p>
<pre><code class="copyable"># serviceA 是集群名称
[serviceA]
# 枚举 serviceA 集群的 ip 地址
192.168.33.10
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>编辑 YAML 文件</strong></p>
<p>告诉 Ansible 在目标机器上执行哪些操作的 YAML 文件，Ansible 把这类文件称为 “playbook”。</p>
<p>下面我们一起编写一个为名 hello.yml 的 playbook。这个 playbook 的作用是把 helloworld 文件发送到 serviceA 集群。</p>
<pre><code class="copyable"># hosts 是要部署服务的集群
- hosts: serviceA
# remote_user 是以 root 用户登录远程机器
  remote_user: root
# vars 是定义一些变量。这些变量可以在接下来的 tasks 中使用。
  vars:
     src: /Users/yutou/mywork/ansible-playbook
# tasks 是在远程机器上具体的执行动作。
  tasks:
      # name 是该动作的名称
      - name: upload helloworld
        # copy 是要具体执行的动作。copy 是 Ansible 模块，它的作用是把本地文件上传到目标机器上去。
        # &#123;&#123; src &#125;&#125; 是 Jinja2 模板语法，Jinja2 模板语法不懂的话可自行百度。
        copy: src=&#123;&#123; src &#125;&#125;/helloworld dest=/home
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>发布</strong></p>
<pre><code class="copyable">
ansible-playbook hello.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">Ansible playbook 常用模块</h2>
<p>ansible 很多模块都可以做到 “见其名，知其意”，很多模块都是对 Linux 命令的模仿或者封装，更多模块可参见官方文档。下面我们先挑几个模块简单介绍一下：</p>
<ul>
<li>
<p>synchronize，copy，unarchive 都可以上传文件。</p>
</li>
<li>
<p>ping：检查指定节点机器是否还能连通。主机如果在线，则回复pong。</p>
</li>
<li>
<p>yum, apt：这两个模块都是在远程系统上安装包的。</p>
</li>
<li>
<p>pip：远程机器上 python 安装包。</p>
</li>
<li>
<p>user，group：用户管理的。</p>
</li>
<li>
<p>service：管理服务的，类似于 centos7 上的 service。</p>
</li>
</ul>
<p>template 模块和在远程机器上执行 Linux 命令的模块是非常重点的模块，所以接下来重点介绍一下。</p>
<p><strong>Ansible playbook 常用模块</strong></p>
<p>配置文件的一个特点是每个机器上的文件都不一样，都需要一些个性化配置，比如 A 机器配置 “hello world”，B 机器配置 “hello Liming”。这种需求就需要 template 模块实现。</p>
<p>template 模块使用 Jinja2 语法对模板文件进行渲染，然后把渲染后的文件上传到目标机器。渲染时用到的变量可以从 3 个地方读取到：</p>
<ul>
<li>
<p>ansible 内置变量；</p>
</li>
<li>
<p>hosts 文件中定义的变量，如上所示；</p>
</li>
<li>
<p>在 playbook 中 vars 定义的变量。</p>
</li>
</ul>
<p>举例，模板文件 hello_x，内容如下：</p>
<pre><code class="copyable">hello &#123;&#123; name &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hosts 文件配置如下：</p>
<pre><code class="copyable">
[serviceA]
192.168.33.10 name=world
192.168.33.11 name=Liming
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 playbook hello_x.yml 中配置如下：</p>
<pre><code class="copyable">
  tasks:
      - name: upload helloworld
        template: src=&#123;&#123; src &#125;&#125;/hello_x dest=/home
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 ansible-playbook hello_x.yml 后，192.168.33.10 上 /home/hello_x 文件的内容就是 hello world, 192.168.33.11 上则是 hello Liming</p>
<p><strong>在远程机器上执行 Linux 命令</strong></p>
<p>raw, command，shell 这三个模块都以用来在远程机器上执行 Linux 命令。三种区别大致区别如下：</p>
<ul>
<li>
<p>一般情况下使用 command</p>
</li>
<li>
<p>命令中有特殊字符使用 shell</p>
</li>
<li>
<p>raw 是直接执行原始命令，没有经过模块封装，不建议用。</p>
</li>
</ul>
<p>注意命令的内容一般使用 "" 引起来，否则模板渲染的时候可能报错：</p>
<pre><code class="copyable">
    - name: start datanode
      command: "/hadoop-2.7.5/sbin/hadoop-daemon.sh start datanode"
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">推荐阅读</h4>
<p><a href="https://www.upyun.com/tech/article/638/Redis%20%E5%AD%98%E5%82%A8%E5%AF%B9%E8%B1%A1%E4%BF%A1%E6%81%AF%E6%98%AF%E7%94%A8%20Hash%20%E8%BF%98%E6%98%AF%20String.html" target="_blank" rel="nofollow noopener noreferrer">Redis 存储对象信息是用 Hash 还是 String</a></p>
<p><a href="https://www.upyun.com/tech/article/640/%E5%AE%9E%E6%93%8D%E7%AC%94%E8%AE%B0%EF%BC%9A%E4%B8%BA%20NSQ%20%E9%85%8D%E7%BD%AE%E7%9B%91%E6%8E%A7%E6%9C%8D%E5%8A%A1%E7%9A%84%E5%BF%83%E8%B7%AF%E5%8E%86%E7%A8%8B.html" target="_blank" rel="nofollow noopener noreferrer">实操笔记：为 NSQ 配置监控服务的心路历程</a></p></div>  
</div>
            