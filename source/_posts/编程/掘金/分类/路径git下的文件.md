
---
title: '路径.git下的文件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2853200e033491ebf154019e0c97e34~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 06:48:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2853200e033491ebf154019e0c97e34~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>用了这么久的<code>git</code>, 可以毫不谦虚地说对<code>git</code>是一无所知. 每天用来用去的就是<code>commit</code>, <code>add</code>, <code>merge</code> 等几个有限的命令, 这不符合我这刨根问底的性格啊. 不行, 得研究研究, 从哪里下手呢? 别的咱先不说, 所有 git 项目都有这么一个文件夹<code>.git</code>, 不如就从它入手 ? 那咱就看看这个文件夹下都有些什么妖魔鬼怪.</p>
<p>先来想一想, <code>.git</code>文件夹下保存了<code>git</code>仓库的所有信息, 那么就包括:</p>
<ul>
<li>提交历史</li>
<li>暂存内容</li>
<li>当前分支</li>
<li>远程分支路径</li>
<li>等等</li>
</ul>
<p>好, 来看一看都有些什么:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2853200e033491ebf154019e0c97e34~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210522220738773" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6e7bab623d9426da2e25130592899bc~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210523124534487" loading="lazy" referrerpolicy="no-referrer"></p>
<p>内容都在这了, 好, 那就对这些文件依次看一下吧.</p>
<p>先来说一下我目前对这个测试项目的操作.</p>
<pre><code class="hljs language-bash copyable" lang="bash">; 创建文件提交
touch readme.md
git add readme.md
git commit -m <span class="hljs-string">'add readme'</span>
; 修改文件提交
<span class="hljs-built_in">echo</span> <span class="hljs-built_in">test</span> > readme.md
git add readme.md
git commit -m <span class="hljs-string">'change readme'</span>
; 创建分支
git checkout -b master_test
<span class="copy-code-btn">复制代码</span></code></pre>
<p>仅做了两次提交操作, 这是为了保持<code>.git</code>文件夹最初的状态, 好方便查看.</p>
<h4 data-id="heading-0">COMMIT_EDITMSG</h4>
<p>此文件保存了最后一次<code>commit</code>的信息. 没搞懂存这玩意有啥用, 我直接 <code>git log</code>看不就行了么.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e2a377fef7b4ad4b19eae000ed49851~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210522223207116" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">HEAD</h4>
<p>保存当前使用的分支.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8db626e6c8284b25a3096da3de474c79~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210522223417114" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外, 直接修改这个文件, 就可以达到<code>git checkout</code>命令的目的. (可以切换分支, 但是不能创建分支哦)</p>
<p>再另外, 从这个文件内容中, 可以推断出, <code>refs</code>文件夹是用来保存分支信息的, 不过这个先记到小本本上, 接着往后看.</p>
<h4 data-id="heading-2">config</h4>
<p>不用说, 看名字也知道, 是用来保存配置信息的.</p>
<p>我们加一条本地配置信息看一下: <code>git config --local user.name 'git_test'</code></p>
<p>如果不出所料, 远程地址也保存在这里, 加一下: <code>git remote add origin http://test.com/aa/bb</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7357f803f9b44dba4472e5cf5e56d79~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210523143935008" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">description</h4>
<p>不多说了, 上图, 看文件描述是用来填写项目的描述信息的.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c051668b45074bd191b125d9af54e517~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210522224441090" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">hooks</h4>
<p>存放项目的各个钩子函数, 就是在各种操作的前后添加自己的执行逻辑. 这个之前倒是一直没有用过. 文件夹下有样例文件, 直接将<code>.sample</code>后缀删除即可使用. (下面只列举了常用的几个, 并不是全部)</p>
<ul>
<li>pre-commit: commit 之前触发. 可用来对代码进行检查</li>
<li>prepare-commit-msg: commit 之前, 添加 message 之后.</li>
<li>commit-msg: commit 时调用, 可修改 message, 也可以取消本次提交</li>
<li>post-commit: commit 之后调用</li>
<li>post-update: push之后触发</li>
<li>pre-receive: push 时, 实际推送之前调用</li>
<li>pre-push: push 之前触发</li>
<li>pre-merge-commit: merge之前触发</li>
<li>pre-rebase: rebase 之前触发</li>
</ul>
<p>等等, 具体信息可到<a href="https://git-scm.com/book/zh/v2/%E8%87%AA%E5%AE%9A%E4%B9%89-Git-Git-%E9%92%A9%E5%AD%90" target="_blank" rel="nofollow noopener noreferrer">官网文档</a>查看</p>
<p>可以看到, 此文件夹用来对工作流程进行自动化管理的.</p>
<h4 data-id="heading-5">index</h4>
<p>用来保存本地暂存区中的内容. 二进制文件, 不可直接查看. 可通过命令: <code>git ls-files --stage</code>来查看当前暂存区内容.</p>
<h4 data-id="heading-6">info</h4>
<p>路径下目前只有一个文件: <code>exclude</code>. 此文件用来在<code>git</code>中忽略某些文件. 与<code>.gitignore</code>不同的是, 此文件不会进行提交. 也就是用来忽略一些仅你本地使用的文件.</p>
<h4 data-id="heading-7">logs</h4>
<p>用来记录所有的操作记录. 看一下我本地这几个文件的内容.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e2830d436ea4118bac692d0627264ce~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210523141224344" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>HEAD</code>文件记录的是所有的操作, 而对应<code>refs</code>文件夹下, 则记录的时候各个分支中的操作.</p>
<p>同时, 可以通过<code>git reflog</code>命令来进行查看, 当出现误操作的时候, 通过<code>git reset --hard &#123;id&#125;</code>来后悔.</p>
<h4 data-id="heading-8">objects</h4>
<p>这个文件保存的就是所有 git 历史变动了, 具体文件的保存结构就留待日后研究. 这里先不深究.</p>
<p>可通过<code>git gc</code>来减少文件体积.</p>
<h4 data-id="heading-9">refs</h4>
<p>保存本地的分支和标签. 文件内容也很简单, 就是一个 commit id.</p>
<p>另外, <code>gc</code>之后, 会多出来一个: <code>.git/packed-refs</code>文件. 此文件包含<code>refs</code>下的所有信息, 同时<code>refs</code>下的文件会被清空.</p>
<h4 data-id="heading-10">其他文件</h4>
<h5 data-id="heading-11">FATCH_HEAD</h5>
<p>用来保存远程分支信息</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8251ce29a50c4223845d17852a7bb303~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210523145221640" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-12">ORIG_HEAD</h5>
<p>在执行如<code>merge</code>, <code>reset</code>, <code>rebase</code>等操作时, 对 "HEAD"文件内容进行备份.</p>
<h5 data-id="heading-13">sourcetreeconfig</h5>
<p>当使用<code>sourcetree</code>对项目进行管理时, 用来保存<code>sourcetree</code>中的配置信息.</p>
<hr>
<p>将<code>.git</code>文件夹下的内容过了一遍, 基本保存的位置都找到了, 剩下保存内容的二进制文件了还整不明白.</p>
<p>过下来之后, 倒也发现了一些能够帮到我的内容, 比如本地的 ignore, 之前的处理是在路径下添加<code>.gitignore</code>同时将<code>.gitignore</code>文件本身也忽略. 后面可以直接修改<code>.git/info/exclude</code>这个文件.</p></div>  
</div>
            