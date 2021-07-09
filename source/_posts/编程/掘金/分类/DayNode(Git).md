
---
title: 'DayNode(Git)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aef1f6b213284e32adfc0cd7a3fff42f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 18:37:31 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aef1f6b213284e32adfc0cd7a3fff42f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. git基础概念</h1>
<blockquote>
<p><code>Git</code> 是一个<strong>开源的分布式版本控制系统</strong></p>
<p>特点：项目越大越复杂，协同开发者越多，越能体现出 Git 的<strong>高性能</strong>和<strong>高可用性</strong>！</p>
</blockquote>
<h2 data-id="heading-1">1.1 git安装</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2Fdownloads" target="_blank" rel="nofollow noopener noreferrer" title="https://git-scm.com/downloads" ref="nofollow noopener noreferrer">git安装</a>
配置用户信息</p>
<pre><code class="hljs language-js copyable" lang="js">git config --<span class="hljs-built_in">global</span> user.name <span class="hljs-string">"itheima"</span>
git config --<span class="hljs-built_in">global</span> user.email <span class="hljs-string">"itheima@itcast.cn"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检查配置信息</p>
<pre><code class="hljs language-js copyable" lang="js"># 查看所有的全局配置项
git config --list --<span class="hljs-built_in">global</span>
# 查看指定的全局配置项
git config user.name
git config user.email
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">1.2 git特性</h2>
<p>① 直接记录快照（完整备份），而非差异比较</p>
<ul>
<li><strong>Git 快照</strong>是在原有文件版本的基础上重新生成一份新的文件，<strong>类似于备份</strong>。为了效率，如果文件没有修改，Git 不再重新存储该文件，而是只保留一个链接指向之前存储的文件。
<ul>
<li><strong>缺点：</strong> 占用磁盘空间较大</li>
<li><strong>优点：</strong> 版本切换时非常快</li>
<li><strong>特点：</strong>  <strong>空间换时间</strong></li>
</ul>
</li>
</ul>
<p>② 近乎所有操作都是本地执行</p>
<ul>
<li>
<p>断网后依旧可以在本地对项目进行版本管理</p>
</li>
<li>
<p>联网后，把本地修改的记录同步到云端服务器即可</p>
</li>
</ul>
<h2 data-id="heading-3">1.3 git区域｜状态</h2>
<p><strong>git三个区域：</strong> 工作区、暂存区、<code>Git</code> 仓库
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aef1f6b213284e32adfc0cd7a3fff42f~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-07 下午3.18.32.png" loading="lazy" referrerpolicy="no-referrer">
<strong>git三种状态：</strong></p>
<ul>
<li>
<p><strong>已修改 <code>modified</code></strong></p>
<ul>
<li>表示修改了文件，但还没将修改的结果放到<strong>暂存区</strong></li>
</ul>
</li>
<li>
<p><strong>已暂存 <code>staged</code></strong></p>
<ul>
<li>表示对已修改文件的当前版本做了标记，使之包含在<strong>下次提交的列表中</strong></li>
</ul>
</li>
<li>
<p><strong>已提交 <code>committed</code></strong></p>
<ul>
<li>表示文件已经安全地保存在本地的 <strong>Git 仓库中</strong></li>
</ul>
</li>
</ul>
<p><code>注意：</code></p>
<ul>
<li>文件只要被放到暂存区过了，就处于【被跟踪状态】</li>
<li>工作区有【被跟踪】和【未被跟踪】的两种状态</li>
<li>只要文件修改过，就在工作区了，需要重新提交到暂存区</li>
<li>只有【被跟踪】的文件，才能通过<code>git commit -a -m'备注'</code>绕过<code>暂存区</code>，将<code>工作区</code>的文件提交到<code>仓库</code></li>
</ul>
<h1 data-id="heading-4">2. git基本操作</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eca4fa939734fd0b04a6fbc70061d03~tplv-k3u1fbpfcp-watermark.image" alt="常见git命令.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">2.1 系统操作</h2>
<p><strong>安装权限</strong></p>
<pre><code class="hljs language-js copyable" lang="js">sudo
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>命令快捷键</strong></p>
<pre><code class="hljs language-js copyable" lang="js">上箭头--上个命令
下箭头--下个命令
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>切换路径</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 切换到下一级</span>
cd 文件名

<span class="hljs-comment">// 切换到上一级文件夹</span>
cd ../文件名
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>显示隐藏的文件</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 快捷键</span>
shift+command+. 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2.2 git操作</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01a1d05cc093467abe95355d4abadf5d~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-07 下午2.41.58.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">初始化仓库</h3>
<pre><code class="hljs language-js copyable" lang="js">git init
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">查看当前项目的状态</h3>
<pre><code class="hljs language-js copyable" lang="js">git status

<span class="hljs-comment">// 以精简的方式显示文件状态 -s是--short的简写</span>
git status -s

红色【??】--未跟踪的文件
红色【M】--已修改，但还没放到暂存区中
绿色【M】--已修改，且已放到暂存区中
绿色【A】--新增文件，已放到暂存区
【D】--删除标记
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">将文件添加到本地仓库的<code>暂存区</code>中</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 添加单个文件</span>
git add 文件名（包含后缀）
<span class="hljs-comment">// 添加所有文件</span>
git add .
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">将<code>暂存区</code>的文件生成一个版本放到<code>仓库</code>里</h3>
<pre><code class="hljs language-js copyable" lang="js">git commit -m<span class="hljs-string">'备注'</span>

<span class="hljs-comment">// 将`工作区`的文件直接提交到`仓库`（绕过暂存区）</span>
git commit -a -m<span class="hljs-string">'备注'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">撤销对文件的修改（撤销后文件在工作区）</h3>
<pre><code class="hljs language-js copyable" lang="js">#注意：撤销了之后，文件无法恢复
git checkout -- index.html
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">取消暂存的文件</h3>
<pre><code class="hljs language-js copyable" lang="js">git reset HEAD 文件名
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">移除文件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> 从git仓库和工作区中 同时移除文件
<span class="hljs-comment">// 将工作区的文件删除，且在暂存区中 标记该文件为 删除【绿D】（在仓库里还没有真正被删除）</span>
git rm -f <span class="hljs-number">01</span>.js
<span class="hljs-comment">// 生成新的版本，并将暂存区 标记为 删除【绿D】的文件删除后，从此该文件真正被删除</span>
git commit -m<span class="hljs-string">'删除了01.js文件'</span>


<span class="hljs-number">2.</span> 只从git中移除 在工作区中保留文件
git rm --cached <span class="hljs-number">02</span>.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">.gitignore忽略文件</h3>
<blockquote>
<p>有些文件无需纳入 <code>Git</code> 的管理，也不希望它们总出现在未跟踪文件列表。</p>
</blockquote>
<p>① 以 <strong># 开头</strong>的是注释</p>
<p>② 以 <strong>/ 结尾</strong>的是目录</p>
<p>③ 以 <strong>/ 开头</strong>防止递归</p>
<p>④ 以 <strong>! 开头</strong>表示取反</p>
<p>⑤ 可以使用 <strong>glob 模式</strong>进行文件和文件夹的匹配（glob 指简化了的正则表达式）</p>
<ul>
<li><strong>星号 *</strong> 匹配<strong>零个或多个任意字符</strong></li>
<li><strong><code>[abc]</code></strong> 匹配<strong>任何一个列在方括号中的字符</strong> （此案例匹配一个 a 或匹配一个 b 或匹配一个 c）</li>
<li><strong>问号 ?</strong> 只匹配<strong>一个任意字符</strong></li>
<li><strong>两个星号 *</strong>* 表示匹配<strong>任意中间目录</strong>（比如 a/**/z 可以匹配 a/z 、 a/b/z 或 a/b/c/z 等）</li>
<li>在方括号中使用<strong>短划线</strong>分隔两个字符， 表示所有在这两个字符范围内的都可以匹配（比如 [0-9] 表示匹配所有 0 到 9 的数字）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b786709378c84c7aa0295324515fc64c~tplv-k3u1fbpfcp-watermark.image" alt="忽略清单.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">查看提交历史</h3>
<pre><code class="hljs language-js copyable" lang="js"># 按时间先后顺序列出所有的提交历史，最近的提交在最上面
git log

# 只展示最新的两条提交历史，数字可以按需进行填写
git log -<span class="hljs-number">2</span>

# 在一行上展示最近两条提交历史的信息
git log -<span class="hljs-number">2</span> --pretty=oneline

# 在一行上展示最近两条提交历史信息，并自定义输出的格式
# &h 提交的简写哈希值  %an 作者名字  %ar 作者修订日志  %s 提交说明
git log -<span class="hljs-number">2</span> --pretty=format:<span class="hljs-string">"%h | %an | %ar | %s"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">回退到指定的版本</h3>
<pre><code class="hljs language-js copyable" lang="js"># 【查看当前和之前的版本】在一行上展示所有的提交历史
git log --pretty=oneline

# 使用 git reset --hard 命令，根据指定的提交 ID 回退到指定版本
git reset --hard <CommitID>

# 【查看所有版本】在旧版本中使用 git reflog --pretty=oneline 命令，查看命令操作的历史
git reflog --pretty=oneline

# 再次根据最新的提交 ID，跳转到最新的版本
git reset --hard <CommitID>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">3. 开源</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c58694b57b34674ab9273b3e03e776c~tplv-k3u1fbpfcp-watermark.image" alt="开源和闭源.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><strong>开源</strong>是指不仅提供程序还提供程序的源代码</p>
</li>
<li>
<p><strong>闭源</strong>是只提供程序，不提供源代码</p>
</li>
</ul>
<h2 data-id="heading-18">3.1 开源许可协议</h2>
<blockquote>
<p>Open Source License,为了<strong>限制使用者的使用范围</strong>和<strong>保护作者的权利</strong></p>
</blockquote>
<ul>
<li><code>BSD</code>（Berkeley Software Distribution）</li>
<li><code>Apache Licence 2.0</code></li>
<li><strong><code>GPL</code></strong>（GNU General Public License） (⭐⭐⭐)
<ul>
<li>具有传染性的一种开源协议，不允许修改后和衍生的代码做为闭源的商业软件发布和销售</li>
<li>使用 <code>GPL</code> 的最著名的软件项目是：Linux</li>
</ul>
</li>
<li><code>LGPL</code>（GNU Lesser General Public License）</li>
<li><strong><code>MIT</code></strong>（Massachusetts Institute of Technology, MIT）  (⭐⭐⭐)
<ul>
<li>是目前限制最少的协议，唯一的条件：在修改后的代码或者发行包中，必须包含原作者的许可信息</li>
<li>使用 MIT 的软件项目有：<code>jquery</code>、<code>Node.js</code></li>
</ul>
</li>
</ul>
<h1 data-id="heading-19">4. gitee</h1>
<p>查看远程仓库的提交历史：项目->统计->提交</p>
<h2 data-id="heading-20">4.1 将本地仓库提交到远程仓库</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce251d9b1b6840888594f686b6338b44~tplv-k3u1fbpfcp-watermark.image" alt="00管理本地仓库中的远程地址.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/009317f70e9f419c8c9d644633d3eae2~tplv-k3u1fbpfcp-watermark.image" alt="00远程分支操作.png" loading="lazy" referrerpolicy="no-referrer">
<code>注意：</code></p>
<ul>
<li>如果文件没有修改，生成新的版本，就不能推到远程仓库中</li>
<li>如果工作区更改了，要先提交到本地仓库，才能提交到远程仓库</li>
</ul>
<h3 data-id="heading-21">4.1.1 基于<code>HTTPS</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> 关联远程仓库
git remote add 别名 远程仓库地址

git remote add origin HTTPS信息

git remote add originSSH SSH信息

- 查看origin
git remote

- 查看HTTPS信息
git remote get-url origin master

- 查看SSH信息
git remote get-url originSSH master

<span class="hljs-number">2.</span> 首次提交到远程仓库
git push -u origin master

非首次提交
git push

如果都存在，默认是通过https提交，如果要通过ssh提交
git push -u originSSH master

<span class="hljs-number">3.</span> 删除已经建立的联系
git remote remove origin 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">4.1.2 基于<code>SSH key</code>（推荐）</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b3bdc65db72497cb1f25f2823819330~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-08 下午2.44.08.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d85cd559d78a4811b7458b55166326b7~tplv-k3u1fbpfcp-watermark.image" alt="00远程仓库的两种验证方式.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55d99159daf64857ac45e4a05777d234~tplv-k3u1fbpfcp-watermark.image" alt="03使用公钥私钥验证整份的原理.png" loading="lazy" referrerpolicy="no-referrer">
<code>SSH key</code> 的<strong>作用</strong>：实现本地仓库和 <code>Github</code> 之间免登录的加密数据传输。</p>
<p><code>SSH key</code> 的<strong>好处</strong>：免登录身份认证、数据加密传输。</p>
<p><code>SSH key</code> 由<strong>两部分组成</strong>，分别是：</p>
<p>① <code>id_rsa</code>（私钥文件，存放于客户端的电脑中即可）</p>
<p>② <code>id_rsa.pub</code>（公钥文件，需要配置到 <code>Github</code> 中）
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fhelp%2Farticles%2F4181%23article-header0" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/help/articles/4181#article-header0" ref="nofollow noopener noreferrer">生成公钥</a></p>
<h4 data-id="heading-23">找到ssh文件夹下的id_rsa.pub文件</h4>
<pre><code class="hljs language-js copyable" lang="js">$open ~/.ssh
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">生成 sshkey</h4>
<pre><code class="hljs language-js copyable" lang="js">ssh-keygen -t rsa -C <span class="hljs-string">"xxxxx@xxxxx.com"</span>  
<span class="hljs-comment">// 注意：这里的 xxxxx@xxxxx.com 只是生成的 sshkey 的名称，并不约束或要求具体命名为某个邮箱。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">查看 <code>~/.ssh/id_rsa.pub </code>文件内容，</h4>
<pre><code class="hljs language-js copyable" lang="js">cat ~<span class="hljs-regexp">/.ssh/i</span>d_rsa.pub
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">将公钥复制添加到远程仓库中（gitee/github）</h4>
<h2 data-id="heading-27">4.2 将远程仓库克隆到本地</h2>
<p><code>作用</code></p>
<ol>
<li>创建项目文件夹，并‘解压’当前下载的版本，放到项目文件夹中</li>
<li>创建本地仓库会克隆远程仓库的<code>所有版本</code>历史</li>
<li>为本地仓库添加了远程仓库<code>地址origin</code>-当前下载使用的额地址</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">git clone 远程仓库的地址
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92f5de49f95449689a1a8de4d9379821~tplv-k3u1fbpfcp-watermark.image" alt="03.4【非常重要】使用ssh方式与远程仓库交流整体逻辑图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-28">5. GIT本地分支</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58a1c090367b40638a44f8854e7ab465~tplv-k3u1fbpfcp-watermark.image" alt="01【重要】分支图解.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">5.1 master 主分支</h2>
<blockquote>
<p>作用：<strong>用来保存和记录整个项目已完成的功能代码</strong>。</p>
<p>因此，<strong>不允许程序员直接在 <code>master</code> 分支上修改代码</strong>，容易导致整个项目崩溃。</p>
</blockquote>
<h2 data-id="heading-30">5.2 功能分支</h2>
<blockquote>
<p>专门用来开发新功能的分支，它是临时从 <code>master</code> 主分支上分叉出来的，当新功能开发且测试完毕后，最终需要合并到 <code>master</code> 主分支上</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dd4867b2cf8424ba0aeaba75fc89795~tplv-k3u1fbpfcp-watermark.image" alt="功能分支.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-31">5.3 分支命令操作</h2>
<p><code>注意：</code>只要文件修改了，就需要提交到缓存区于仓库</p>
<h3 data-id="heading-32">查看分支列表</h3>
<p>分支名字前面的 * 号表示当前所处的分支。</p>
<pre><code class="hljs language-js copyable" lang="js">git branch
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">创建新分支</h3>
<p><strong>基于当前分支</strong>，创建一个新的分支，<code>不会切换分支</code>，此时，新分支中的代码和当前分支完全一样</p>
<pre><code class="hljs language-js copyable" lang="js">git branch 分支名称
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">切换分支</h3>
<p><code>注意：</code>切换分支时，会切换工作区代码</p>
<pre><code class="hljs language-js copyable" lang="js">git checkout 分支名称
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">创建并切换分支</h3>
<pre><code class="hljs language-js copyable" lang="js"># -b 表示创建一个新分支
# checkout 表示切换到刚才新建的分支上
git checkout -b 分支名称
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">合并分支</h3>
<p><code>注意：</code>要先切换分支，再合并</p>
<pre><code class="hljs language-js copyable" lang="js"># <span class="hljs-number">1.</span> 切换到 master 分支
git checkout master
# <span class="hljs-number">2.</span> 在master 分支上运行 git merge 命令，将 login 分支的代码合班到 master 分支
git merge login
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">删除本地仓库的分支</h3>
<p>需要在<code>主分支</code>上删除</p>
<pre><code class="hljs language-js copyable" lang="js">git branch -d 分支名称
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">解决分支合并时的冲突问题</h3>
<p>如果<strong>在两个不同的分支中</strong>，对<strong>同一个文件</strong>进行了<strong>不同的修改</strong>，Git 就没法干净的合并它们。 需要打开这些包含冲突的文件然后<strong>手动解决冲突</strong>。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F04af5a5204ff" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/04af5a5204ff" ref="nofollow noopener noreferrer">解决冲突参考</a></p>
<pre><code class="hljs language-js copyable" lang="js"># 假设：在把 login 分支合并到 master 分支期间
git checkout master
git merge login

# 打开包含冲突的文件，手动解决冲突之后，再执行如下命令
git add .
git commit -m <span class="hljs-string">"解决了分支合并冲突的问题"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-39">5.4 远程仓库分支操作</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0341d9039f6c4b5d8efd1d9830e99003~tplv-k3u1fbpfcp-watermark.image" alt="05三种与远程仓库交互的方式.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-40">将本地分支推送到远程仓库</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34ff0fa38d904c7382315ed6e01aeaf8~tplv-k3u1fbpfcp-watermark.image" alt="04远程仓库提交.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> -u 表示把本地分支和远程分支进行关联，只在第一次推送的时候需要带 -u 参数</span>
git push -u 远程仓库的别名 本地分支名称:远程分支名称
<span class="hljs-meta">

#</span><span class="bash"> 实际案例</span>
git push -u origin payment:pay
git push -u origin login// 本地分支名字与远程分支名字一样
<span class="hljs-meta">
#</span><span class="bash"> 如果希望远程分支的名称和本地分支名称保持一致，可以对命令进行简化</span>
git push -u origin payment
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**注意：**第一次推送分支需要带 <strong>-u 参数</strong>，此后可以直接使用 <code>git push</code> 推送代码到远程分支。</p>
<h3 data-id="heading-41">查看远程仓库中所有的分支列表</h3>
<pre><code class="hljs language-shell copyable" lang="shell">git remote show 远程仓库名称
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">跟踪分支(⭐⭐⭐)</h3>
<p>从远程仓库中，把远程分支下载到本地仓库中。</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 示例</span>
git checkout pay
<span class="hljs-meta">
#</span><span class="bash"> 从远程仓库中，把对应的远程分支下载到本地仓库，并把下载的本地分支进行重命名</span>
git checkout -b 本地分支名称 远程仓库名称/远程分支名称
<span class="hljs-meta">
#</span><span class="bash"> 示例</span>
git checkout -b payment origin/pay
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">拉取远程分支的最新的代码</h3>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 从远程仓库，拉取当前分支最新的代码，保持当前分支的代码和远程分支代码一致</span>
git pull
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">删除远程仓库的分支</h3>
<pre><code class="hljs language-js copyable" lang="js"># 删除远程仓库中，制定名称的远程分支
git push 远程仓库名称 --<span class="hljs-keyword">delete</span> 远程分支名称

# 示例
git push origin --<span class="hljs-keyword">delete</span> login
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            