
---
title: 'Git 基本原理介绍'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/752bf91426bc38c49e171eb8b1dea511.png'
author: Dockone
comments: false
date: 2021-08-25 15:08:03
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/752bf91426bc38c49e171eb8b1dea511.png'
---

<div>   
<br>简单地说，<code class="prettyprint">Git</code> 究竟是怎样的一个系统呢？ 请注意接下来的内容非常重要，若你理解了 <code class="prettyprint">Git</code> 的思想和基本工作原理，用起来就会知其所以然，游刃有余。 在学习 <code class="prettyprint">Git</code> 时，请尽量理清你对其它版本管理系统已有的认识，如 <code class="prettyprint">CVS</code>、<code class="prettyprint">Subversion</code> 或 <code class="prettyprint">Perforce</code>， 这样能帮助你使用工具时避免发生混淆。尽管 <code class="prettyprint">Git</code> 用起来与其它的版本控制系统非常相似， 但它在对信息的存储和认知方式上却有很大差异，理解这些差异将有助于避免使用中的困惑。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/752bf91426bc38c49e171eb8b1dea511.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/752bf91426bc38c49e171eb8b1dea511.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Git 初始化代码仓库</h3><em>执行完成了 <code class="prettyprint">git init</code> 命令，究竟做了什么呢？</em><br>
<br>执行完成如下命令之后，我们可以得到下图所示的内容，右侧的就是 <code class="prettyprint">Git</code> 为我们创建的代码仓库，其中包含了用于版本管理所需要的内容。<br>
<pre class="prettyprint"># 左边执行<br>
$ mkdir git-demo<br>
$ cd git-demo && git init<br>
$ rm -rf .git/hooks/*.sample<br>
<br>
# 右边执行<br>
$ watch -n 1 -d find .<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/cef77919614b305ae8a8af1ecc711ce8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/cef77919614b305ae8a8af1ecc711ce8.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们这里可以一起看下生成的 <code class="prettyprint">.git</code> 目录的结构如何：<br>
<pre class="prettyprint">➜ tree .git<br>
.git<br>
├── HEAD<br>
├── config<br>
├── description<br>
├── hooks<br>
├── info<br>
│&nbsp;&nbsp; └── exclude<br>
├── objects<br>
│&nbsp;&nbsp; ├── info<br>
│&nbsp;&nbsp; └── pack<br>
└── refs<br>
├── heads<br>
└── tags<br>
</pre><br>
<h4><code class="prettyprint">.git/config</code>  - 当前代码仓库本地的配置文件</h4><ul><li>本地配置文件（<code class="prettyprint">.git/config</code>）和全局配置文件（<code class="prettyprint">~/.gitconfig</code>）</li><li>通过执行如下命令，可以将用户配置记录到本地代码仓库的配置文件中去</li><li><code class="prettyprint">git config user.name &quot;demo&quot;</code></li><li><code class="prettyprint">git config user.email &quot;demo@demo.com&quot;</code></li></ul><br>
<br><pre class="prettyprint">➜ cat .git/config<br>
[core]<br>
repositoryformatversion = 0<br>
filemode = true<br>
bare = false<br>
logallrefupdates = true<br>
ignorecase = true<br>
precomposeunicode = true<br>
<br>
[user]<br>
name = demo<br>
email = demo@demo.com<br>
</pre><br>
<h4><code class="prettyprint">.git/objects</code>  - 当前代码仓库代码的存储位置</h4><ul><li><code class="prettyprint">blob</code> 类型</li><li><code class="prettyprint">commit</code> 类型</li><li><code class="prettyprint">tree</code> 类型</li></ul><br>
<br><pre class="prettyprint"># 均无内容<br>
➜ ll .git/objects<br>
total 0<br>
drwxr-xr-x  2 escape  staff    64B Nov 23 20:39 info<br>
drwxr-xr-x  2 escape  staff    64B Nov 23 20:39 pack<br>
<br>
➜ ll .git/objects/info<br>
➜ ll .git/objects/pack<br>
</pre><br>
<h4><code class="prettyprint">.git/info</code>  - 当前仓库的排除等信息</h4><pre class="prettyprint">➜ cat ./.git/info/exclude<br>
# git ls-files --others --exclude-from=.git/info/exclude<br>
# Lines that start with '#' are comments.<br>
# For a project mostly in C, the following would be a good set of<br>
# exclude patterns (uncomment them if you want to use them):<br>
# *.[oa]<br>
# *~<br>
</pre><br>
<h4><code class="prettyprint">.git/hooks</code>  - 当前代码仓库默认钩子脚本</h4><pre class="prettyprint">./.git/hooks/commit-msg.sample<br>
./.git/hooks/pre-rebase.sample<br>
./.git/hooks/pre-commit.sample<br>
./.git/hooks/applypatch-msg.sample<br>
./.git/hooks/fsmonitor-watchman.sample<br>
./.git/hooks/pre-receive.sample<br>
./.git/hooks/prepare-commit-msg.sample<br>
./.git/hooks/post-update.sample<br>
./.git/hooks/pre-merge-commit.sample<br>
./.git/hooks/pre-applypatch.sample<br>
./.git/hooks/pre-push.sample<br>
./.git/hooks/update.sample<br>
</pre><br>
<h4><code class="prettyprint">.git/HEAD</code>  - 当前代码仓库的分支指针</h4><pre class="prettyprint">➜ cat .git/HEAD<br>
ref: refs/heads/master<br>
</pre><br>
<h4><code class="prettyprint">.git/refs</code>  - 当前代码仓库的头指针</h4><pre class="prettyprint"># 均无内容<br>
➜ ll .git/refs<br>
total 0<br>
drwxr-xr-x  2 escape  staff    64B Nov 23 20:39 heads<br>
drwxr-xr-x  2 escape  staff    64B Nov 23 20:39 tags<br>
<br>
➜ ll .git/refs/heads<br>
➜ ll .git/refs/tags<br>
</pre><br>
<h4><code class="prettyprint">.git/description</code>  - 当前代码仓库的描述信息</h4><pre class="prettyprint">➜ cat .git/description<br>
Unnamed repository; edit this file 'description' to name the repository.<br>
</pre><br>
<h3>add 之后发生了什么</h3><em>执行完成了 <code class="prettyprint">git add</code> 命令，究竟做了什么呢？</em><br>
<br>执行完成如下命令之后，我们可以得到下图所示的内容，我们发现右侧新增了一个文件，但是 <code class="prettyprint">Git</code> 目录里面的内容丝毫没有变化。这是因为，我们现在执行的修改默认是放在工作区的，而工作区里面的修改不归 <code class="prettyprint">Git</code> 目录去管理。<br>
<br>而当我们执行 <code class="prettyprint">git status</code> 命令的时候，<code class="prettyprint">Git</code> 又可以识别出来现在工作区新增了一个文件，这里怎么做到的呢？——  <strong>详见[理解 blob 对象和 SHA1]部分</strong><br>
<br>而当我们执行 <code class="prettyprint">git add</code> 命令让 <code class="prettyprint">Git</code> 帮助我们管理文件的时候，发现右侧新增了一个目录和两个文件，分别是 <code class="prettyprint">8d</code> 目录、<code class="prettyprint">index</code> 和 <code class="prettyprint">0e41..</code> 文件。<br>
<pre class="prettyprint"># 左边执行<br>
$ echo "hello git" > helle.txt<br>
$ git status<br>
$ git add hello.txt<br>
<br>
# 右边执行<br>
$ watch -n 1 -d find .<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/8edf3e09b6875a3d334135ec5cccfe4e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/8edf3e09b6875a3d334135ec5cccfe4e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/64a9fdfaed4a1083fcf01efd0de87829.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/64a9fdfaed4a1083fcf01efd0de87829.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们这里重点看下，生成的 <code class="prettyprint">8d</code> 这个目录以及下面的文件。而其名称的由来是因为 <code class="prettyprint">Git</code> 对其进行了一个叫做 <code class="prettyprint">SHA1</code> 的 <code class="prettyprint">Hash</code> 算法，用于将文件内容或者字符串变成这么一串加密的字符。<br>
<pre class="prettyprint"># 查看 objects 的文件类型<br>
$ git cat-file -t 8d0e41<br>
blob<br>
<br>
# 查看 objects 的文件内容<br>
$ git cat-file -p 8d0e41<br>
hello git<br>
<br>
# 查看 objects 的文件大小<br>
$ git cat-file -s 8d0e41<br>
10<br>
<br>
# 拼装起来<br>
blob 10\0hello git<br>
</pre><br>
现在我们就知道了，执行 <code class="prettyprint">git add</code> 命令将文件从工作区添加到暂存区里面，<code class="prettyprint">Git</code> 会把帮助我们生成一些 <code class="prettyprint">Git</code> 的对象，它存储的是文件的内容和文件类型并不存储文件名称。<br>
<br>为了验证我们上述的说法，我们可以添加同样的内容到另一个文件，然后进行提交，来观察 <code class="prettyprint">.git</code> 目录的变化。我们发现，右侧的 <code class="prettyprint">objects</code> 目录并没有新增目录和文件。这就可以证明，<code class="prettyprint">blob</code> 类型的 <code class="prettyprint">object</code> 只存储的是文件的内容，如果两个文件的内容一致的话，则只需要存储一个 <code class="prettyprint">object</code> 即可。<br>
<br>话说这里 <code class="prettyprint">object</code> 为什么没有存储文件名称呢？这里因为 <code class="prettyprint">SHA1</code> 的 <code class="prettyprint">Hash</code> 算法计算哈希的时候，本身就不包括文件名称，所以取什么名称都是无所谓的。那问题来了，就是文件名的信息都存储到哪里去了呢？——  <strong>详见[理解 blob 对象和 SHA1]部分</strong><br>
<pre class="prettyprint"># 左边执行<br>
$ echo "hello git" > tmp.txt<br>
$ git add tmp.txt<br>
<br>
# 右边执行<br>
$ watch -n 1 -d find .<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/c2e58018d80998aa5326151268b1cb3d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/c2e58018d80998aa5326151268b1cb3d.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>理解 blob 对象和 SHA1</h3><em>了解 Git 的 blob 对象和 SHA1 之前的关系和对应计算！</em><br>
<br><code class="prettyprint">Hash</code> 算法是把任意长度的输入通过散列算法变化成固定长度的输出，根据算法的不同，生成的长度也有所不同。<br>
<br><strong>Hash 算法</strong>：<br>
<ul><li><code class="prettyprint">MD5</code> - <code class="prettyprint">128bit</code> - 不安全 - 文件校验</li><li><code class="prettyprint">SHA1</code> - <code class="prettyprint">160bit(40位)</code> - 不安全 - <code class="prettyprint">Git</code> 存储</li><li><code class="prettyprint">SHA256</code> - <code class="prettyprint">256bit</code>- 安全 - <code class="prettyprint">Docker</code> 镜像</li><li><code class="prettyprint">SHA512</code> - <code class="prettyprint">512bit</code> - 安全</li></ul><br>
<br>但是，当我们使用工具对上述文件内容进行 <code class="prettyprint">SHA1</code> 计算的时候，会发现并没有我们在 <code class="prettyprint">.git</code> 目录里面看到的那样，这是为什么呢？<br>
<pre class="prettyprint">➜ echo "hello git" | shasum<br>
d6a96ae3b442218a91512b9e1c57b9578b487a0b  -<br>
</pre><br>
这里因为 <code class="prettyprint">Git</code> 工具的计算方式，是使用<strong>类型 长度 \0 内容</strong>的方式进行计算的。这里，我们算了下文件内容只有九位，但是这里是十位，这里因为内容里面有换行符的存在导致的。现在我们就可以使用 <code class="prettyprint">git cat-file</code> 命令来拼装 <code class="prettyprint">Git</code> 工具存储的完整内容了。<br>
<pre class="prettyprint">➜ ls -lh hello.txt<br>
-rw-r--r--  1 escape  staff    10B Nov 23 21:12 hello.txt<br>
<br>
➜ echo "blob 10\0hello git" | shasum<br>
8d0e41234f24b6da002d962a26c2495ea16a425f  -<br>
<br>
# 拼装起来<br>
blob 10\0hello git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/1ce29523be0c2a78fad0652c0ad0ae92.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/1ce29523be0c2a78fad0652c0ad0ae92.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当我们使用 <code class="prettyprint">cat</code> 命令来查看 <code class="prettyprint">object</code> 对象里面的内容的时候，发现看着像是一串乱码。其实这是 <code class="prettyprint">Git</code> 工具将文件的原始内容进行一个压缩，然后再存储到 <code class="prettyprint">object</code> 对象里面。奇怪的是，我们发现压缩之后的内容反而比原始内容还大！<br>
<br>这是因为其进行了压缩，存储了一些压缩相关的信息。上例所示的比原始文件大，是因为我们创建的内容实在是太小了。当我们常见一个比较大的文件时，就会看到压缩之后的文件大小远小于原始文件的。<br>
<pre class="prettyprint">➜ cat .git/objects/8d/0e41234f24b6da002d962a26c2495ea16a425f<br>
xKOR04`HWH,6A%<br>
<br>
➜ ls -lh .git/objects/8d/0e41234f24b6da002d962a26c2495ea16a425f<br>
-r--r--r--  1 escape  staff    26B Nov 23 21:36 .git/objects/8d/0e41234f24b6da002d962a26c2495ea16a425f<br>
<br>
➜ file .git/objects/8d/0e41234f24b6da002d962a26c2495ea16a425f<br>
.git/objects/8d/0e41234f24b6da002d962a26c2495ea16a425f: VAX COFF executable not stripped - version 16694<br>
</pre><br>
其实，我们这里也是可以通过 <code class="prettyprint">Python</code> 代码来获取二进制 <code class="prettyprint">object</code> 对象的内容的。<br>
<pre class="prettyprint">import zlib<br>
<br>
contents = open('0e41234f24b6da002d962a26c2495ea16a425f', 'rb').read()<br>
zlib.decompress(contents)<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/f30ae9df519939fd0ef4aeccec86c7a9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/f30ae9df519939fd0ef4aeccec86c7a9.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>聊聊工作区和暂存区</h3><em>聊聊工作区和暂存区，以及文件如何在工作区和缓存区之间同步的问题。</em><br>
<br>之前的章节我们也聊到了，当我们执行 <code class="prettyprint">git status</code> 命令的时候，<code class="prettyprint">Git</code> 工具怎么知道我们有一个文件没有追踪，以及文件名的信息都存储到哪里去了？<br>
<br>这一切的答案，都要从工作区和索引区讲起。<code class="prettyprint">Git</code> 根据其存储的状态不同，将对应状态的“空间”分为<strong>工作区</strong>、<strong>暂存区（也可称为索引区）</strong>和<strong>版本区</strong>三类。具体示例，可以参考下图。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/1a566c7845788bfb6c4e303438b6358d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/1a566c7845788bfb6c4e303438b6358d.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
而更加深层次的理解，就要从执行 <code class="prettyprint">git add</code> 命令后生成相关的 <code class="prettyprint">object</code> 对象，但是其存储的是文件的类容、大小和内容，并不包含文件名称的信息。而文件名称相关的信息就包含在生成的 <code class="prettyprint">index</code> 文件（索引文件）里面。<br>
<br>当我们直接查看 <code class="prettyprint">index</code> 文件里面的内容，发现使我们无法理解的乱码，但是通过基本的输出，我们可以看到其文件名称。要想查看 <code class="prettyprint">index</code> 文件的内容，可以通过 <code class="prettyprint">Git</code> 提供的相关命令进行查看。<br>
<pre class="prettyprint"># 左边执行<br>
$ echo "file1" > file1.txt<br>
$ git add file1.txt<br>
$ cat .git/index<br>
<br>
$ git ls-files     # 列出当前暂存区的文件列表信息<br>
$ git ls-files -s  # 列出当前暂存区文件的详细信息<br>
<br>
# 右边执行<br>
$ watch -n 1 -d tree .git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/db3e5d8d244cb3b12cf2f9dd2109a53b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/db3e5d8d244cb3b12cf2f9dd2109a53b.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当添加文件的时候，文件或目录会从工作区流向暂存区，加之一些其他操作，会导致工作区和暂存区是会有一定差别的。这就会导致，当我们执行 <code class="prettyprint">git status</code> 的结果就是两者的差别。<br>
<br>经过如下操作，会使工作区和暂存区和的内容不一致了，通过命令我们也是可以查看区别的。当我们使用 <code class="prettyprint">add</code> 命令将新文件添加到暂存区的时候，会发现这下就一致了。<br>
<pre class="prettyprint"># 左边执行<br>
$ git status<br>
$ echo "file2" > file2.txt<br>
$ git ls-files -s<br>
$ git status<br>
$ git add file2.txt<br>
$ git ls-files -s<br>
$ git status<br>
<br>
# 右边执行<br>
$ watch -n 1 -d tree .git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/7c8e615763769d72bfeedc473ae0b4c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/7c8e615763769d72bfeedc473ae0b4c4.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果我们这里去修改一个文件的话，很显然这个时候我们的工作区和暂存区又不一致了。当我们使用命令去查看文件状态的时候，发现一个文件被修改了，而 <code class="prettyprint">Git</code> 是怎么知道的呢？咳咳，就是通过查找 <code class="prettyprint">index</code> 文件的内容，找到对应文件名称以及其内部引用的 <code class="prettyprint">object</code> 对象，与工作区的文件内容进行对比而来的。<br>
<pre class="prettyprint"># 左边执行<br>
$ git ls-files -s<br>
$ echo "file.txt" > file1.txt<br>
$ git status<br>
<br>
# 右边执行<br>
$ watch -n 1 -d tree .git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/d8d6bd5eae6844a1ee756267d2566e1e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/d8d6bd5eae6844a1ee756267d2566e1e.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
而这个时候，我们再使用 <code class="prettyprint">git add</code> 命令将其修改内容保存至暂存区的话，会发现对应文件的 <code class="prettyprint">object</code> 的 <code class="prettyprint">blob</code> 对象的引用值发生改变了。这时可以发现，<code class="prettyprint">objects</code> 目录下面有三个对象了，其中 <code class="prettyprint">file1.txt</code> 占了两个，但是文件却只有两个。通过命令查看对应 <code class="prettyprint">blob</code> 对象的内容，发现各有不同。<br>
<pre class="prettyprint"># 左边执行<br>
$ git ls-files -s<br>
$ git add file1.txt<br>
$ git ls-files -s<br>
<br>
# 右边执行<br>
$ watch -n 1 -d tree .git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/88ec62a33467721f2957687a9b3e6412.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/88ec62a33467721f2957687a9b3e6412.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>理解 commit 提交原理</h3><em>执行完成了 <code class="prettyprint">git commit</code> 命令，究竟做了什么呢？</em><br>
<br><code class="prettyprint">Git</code> 仓库中的提交记录保存的是你的目录下所有文件的快照，就像是把整个目录复制，然后再粘贴一样，但比复制粘贴优雅许多！<code class="prettyprint">Git</code> 希望提交记录尽可能地轻量，因此在你每次进行提交时，它并不会盲目地复制整个目录。条件允许的情况下，它会将当前版本与仓库中的上一个版本进行对比，并把所有的差异打包到一起作为一个提交记录。<code class="prettyprint">Git</code> 还保存了提交的历史记录。这也是为什么大多数提交记录的上面都有父节点的原因。<br>
<br>当我们使用 <code class="prettyprint">add</code> 命令将工作区提交到暂存区，而暂存区其实保存的是当前文件的一个状态，其中包括有哪些目录和文件，以及其对应的大小和内容等信息。但是我们最终是需要将其提交到代码仓库（本地）的，而其命令就是 <code class="prettyprint">git commit</code> 了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/8c9d6dd140c8532f3b2c3f63dba5713b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/8c9d6dd140c8532f3b2c3f63dba5713b.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
而当我们执行 <code class="prettyprint">git commit</code> 命令的时候，究竟都发生了什么呢？可以看到当提交之后，<code class="prettyprint">.git</code> 目录中生成了两个信息的 <code class="prettyprint">object</code> 对象，其中 <code class="prettyprint">logs</code> 和 <code class="prettyprint">refs</code> 目录都有新的文件生成。通过如下操作，我们可以查看到其提交的类型和对应内容。<br>
<pre class="prettyprint"># 左边执行<br>
$ git commit -m "1st commit"<br>
<br>
$ git cat-file -t 6e4a700  # 查看 commit 对象的类型<br>
$ git cat-file -p 6e4a700  # 查看 commit 对象的内容<br>
<br>
$ git cat-file -t 64d6ef5  # 查看 tree 对象的类型<br>
$ git cat-file -p 64d6ef5  # 查看 tree 对象的内容<br>
<br>
# 右边执行<br>
$ watch -n 1 -d tree .git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/02a51fa872aa31ef56531cf9c0569387.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/02a51fa872aa31ef56531cf9c0569387.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这样我们就理解了，当我们执行 <code class="prettyprint">git commit</code> 命令之后，会生成一个 <code class="prettyprint">commit</code> 对象和一个 <code class="prettyprint">tree</code> 对象。<code class="prettyprint">commit</code> 对象内容里面包含了一个 <code class="prettyprint">tree</code> 对象和相关提交信息，而 <code class="prettyprint">tree</code> 对象里面则包含了这次我们提交版本里面的文件状态（文件名称和 <code class="prettyprint">blob</code> 对象），这样我们就知道了这次提交的变动了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/3a8cea439c51acd8d6bb5e4cc213415f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/3a8cea439c51acd8d6bb5e4cc213415f.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们这次提交之后，处理 <code class="prettyprint">objects</code> 目录发生变动之外，还有一些其他的变化。比如 <code class="prettyprint">logs</code> 和 <code class="prettyprint">refs</code> 的目录有所变化。我们查看 <code class="prettyprint">refs</code> 目录里面的内容，发现其指向了 <code class="prettyprint">6e4a70</code> 这个 <code class="prettyprint">commit</code> 对象，即当前 <code class="prettyprint">master</code> 分支上面最新的提交就是这个 <code class="prettyprint">6e4a70</code> 了。<br>
<br>而这个 <code class="prettyprint">6e4a70</code> 这个 <code class="prettyprint">commit</code> 对象，有一个 <code class="prettyprint">HEAD</code> 的指向，就是 <code class="prettyprint">.git</code> 目录下的 <code class="prettyprint">HEAD</code> 文件。其实质就是一个指针，其永远指向我们当前工作的分支，即这里我们工作在 <code class="prettyprint">master</code> 分支上。当我们切换分支的时候，这个文件的指向也会随机改变的。<br>
<pre class="prettyprint"># 左边执行<br>
$ cat .git/refs/heads/master<br>
$ cat .git/HEAD<br>
<br>
# 右边执行<br>
$ watch -n 1 -d tree .git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/6abc0b5e35c009ef6b47f1d8f24496e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/6abc0b5e35c009ef6b47f1d8f24496e6.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>加深理解 commit 提交</h3><em>执行完成了 <code class="prettyprint">git commit</code> 命令，究竟做了什么呢？</em><br>
<br>当我们再次对 <code class="prettyprint">file2.txt</code> 文件的内容进行变更、添加以及提交之后，发现在提交的时候，查看的 <code class="prettyprint">commit</code> 对象的内容时，其包含有父节点的 <code class="prettyprint">commit</code> 信息。而对于理解的话，可以看看下面的这个提交流程图。<br>
<pre class="prettyprint"># 左边执行<br>
$ echo "file2.txt" > file2.txt<br>
$ git status<br>
$ git add file2.txt<br>
$ git ls-files -s<br>
$ git cat-file -p 0ac9638<br>
$ git commit -m "2nd commit"<br>
$ git cat-file -p bab53ff<br>
$ git cat-file -p 2f07720<br>
<br>
# 右边执行<br>
$ watch -n 1 -d tree .git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/1f569c8f966c917b840d25a05d725674.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/1f569c8f966c917b840d25a05d725674.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/0cda73388964bb61a5a1bbf33ed41e27.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/0cda73388964bb61a5a1bbf33ed41e27.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在 <code class="prettyprint">Git</code> 中空文件夹是不算在追踪范围内的，而且添加文件夹并不会增加 <code class="prettyprint">object</code> 对象。当我们查看 <code class="prettyprint">index</code> 内容的时候，会发现文件名称是包含相对路径的。<br>
<br>而当我们通过 <code class="prettyprint">commit</code> 命令提交之后，会发现生成了三个 <code class="prettyprint">object</code> 对象，因为 <code class="prettyprint">commit</code> 操作不会生成 <code class="prettyprint">blob</code> 对象，所以分别是一个 <code class="prettyprint">commit</code> 对象和两个 <code class="prettyprint">tree</code> 对象。可以发现，<code class="prettyprint">tree</code> 对象里面有包含了一个目录的 <code class="prettyprint">tree</code>，其里面包含对象文件内容。<br>
<br>下图所示的文件状态，可以体会到 <code class="prettyprint">Git</code> 中版本的概念。即 <code class="prettyprint">commit</code> 对象指向一个该版本中的文件目录树的根（<code class="prettyprint">tree</code>），然后 <code class="prettyprint">tree</code> 在指向 <code class="prettyprint">blob</code> 对象（文件）和 <code class="prettyprint">tree</code> 对象（目录），这样就可以无限的往复下去形成一个完整的版本。<br>
<pre class="prettyprint"># 左边执行<br>
$ mkdir floder1<br>
$ echo "file3" > floder1/file3.txt<br>
$ git add floder1<br>
$ git ls-files -s<br>
$ git commit -m "3rd commit"<br>
$ git cat-file -p 1711e01<br>
$ git cat-file -p 9ab67f8<br>
<br>
# 右边执行<br>
$ watch -n 1 -d tree .git<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/5715afa9738608126b97c87bde258fa6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/5715afa9738608126b97c87bde258fa6.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>文件的生命周期状态</h3><em>总结一下，Git 里面的文件状态和如何切换。</em><br>
<br>现在，我们已经基本理解了文件如何在工作区、暂存区以及代码仓库之间进行状态的跟踪和同步。在 <code class="prettyprint">Git</code> 的操作中，文件的可能状态有哪些，以及如何进行状态切换的，我们这里一起总结一下！<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/6b4a14411e651fb5eb1e8be598e098e0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/6b4a14411e651fb5eb1e8be598e098e0.jpg" class="img-polaroid" title="20.jpg" alt="20.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/ca2361ebabd0156f3c05d0925e9423a6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/ca2361ebabd0156f3c05d0925e9423a6.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Branch 和 HEAD 的意义</h3><em>执行完成了 <code class="prettyprint">git branch</code> 命令，究竟做了什么呢？</em><br>
<br>到底什么是分支？分支切换又是怎么一回事？我们通过查看 <code class="prettyprint">Git</code> 的官方文档，就可以得到，分支就是一个有名字的（<code class="prettyprint">master</code>/<code class="prettyprint">dev</code>）指向 <code class="prettyprint">commit</code> 对象的一个指针。<br>
<br>我们在初始化仓库的时候，提供会默认给我们分配一个叫做 <code class="prettyprint">master</code> 的分支（在最新的版本默认仓库已经变更为 <code class="prettyprint">main</code> 了），而 <code class="prettyprint">master</code> 分支就是指向最新的一次提交。为什么需要给分支起名字呢？就是为了方便我们使用和记忆，可以简单理解为 <code class="prettyprint">alias</code> 命令的意义一致。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/1d110c40f0ce6a23ca68cc3d81503b9f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/1d110c40f0ce6a23ca68cc3d81503b9f.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
有了上述基础，我们就需要考虑下，分支到底是如何实现和工作的。要实现一个分支，我们最基本需要解决两个问题，第一个就是需要存储每一个分支指向的 <code class="prettyprint">commit</code>，第二个问题就是在切换分支的时候帮助我们标识当前分支。<br>
<br>在 <code class="prettyprint">Git</code> 中，它有一个非常特殊的 <code class="prettyprint">HEAD</code> 文件。而 <code class="prettyprint">HEAD</code> 文件是一个指针，其有一个特性就是总会指向当前分支的最新的一个 <code class="prettyprint">commit</code> 对象。而这个 <code class="prettyprint">HEAD</code> 文件正好，解决了我们上面提出的两个问题。<br>
<br>当我们从 <code class="prettyprint">master</code> 切换分支到 <code class="prettyprint">dev</code> 的时候，<code class="prettyprint">HEAD</code> 文件也会随即切换，即指向 <code class="prettyprint">dev</code> 这个指针。设计就是这么美丽，不愧是鬼才，好脑袋。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/7d524d038d272424df48df7359903900.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/7d524d038d272424df48df7359903900.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint"># 左边执行<br>
$ cat .git/HEAD<br>
$ cat .git/refs/heads/master<br>
$ git cat-file -t 1711e01<br>
<br>
# 右边执行<br>
$ glo = git log<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/5042f00a49b43be0fba1d87f173074c3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/5042f00a49b43be0fba1d87f173074c3.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>分支操作的背后逻辑</h3><em>执行完成了 <code class="prettyprint">git branch</code> 命令，究竟做了什么呢？</em><br>
<br>这里我们可以看到分支切换之后，<code class="prettyprint">HEAD</code> 指向发生变动了。<br>
<pre class="prettyprint"># 左边执行<br>
$ git branch<br>
$ git branch dev<br>
$ ll .git/refs/heads<br>
$ cat .git/refs/heads/master<br>
$ cat .git/refs/heads/dev<br>
$ cat .git/HEAD<br>
$ git checkout dev<br>
$ cat .git/HEAD<br>
<br>
# 右边执行<br>
$ glo = git log<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/4888cf8851ea55c53c4e514124fe9700.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/4888cf8851ea55c53c4e514124fe9700.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里需要注意的是，即使我们删除了分支，但是该分支上一些特有的对象并不会被删除的。这些对象其实就是我们俗称的垃圾对象，还有我们多次使用 <code class="prettyprint">add</code> 命令所产生的也有垃圾对象，而这些垃圾对象怎么清除和回收呢？后续，我们会涉及到的。<br>
<pre class="prettyprint"># 左边执行<br>
$ echo "dev" > dev.txt<br>
$ git add dev.txt<br>
$ git commit -m "1st commit from dev branch"<br>
$ git checkout master<br>
$ git branch -d dev<br>
$ git branch -D dev<br>
$ git cat-file -t 861832c<br>
$ git cat-file -p 861832c<br>
$ git cat-file -p 680f6e9<br>
$ git cat-file -p 38f8e88<br>
<br>
# 右边执行<br>
$ glo = git log<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/d185966eaade5045f14bcde828d2cd96.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/d185966eaade5045f14bcde828d2cd96.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>checkout 和 commit 操作</h3><em>我们一起聊一聊，checkout 和 commit 的操作！</em><br>
<br>我们执行 <code class="prettyprint">checkout</code> 命令的时候，其不光可以切换分支，而且可以切换到指定的 <code class="prettyprint">commit</code> 上面，即 <code class="prettyprint">HEAD</code> 文件会指向某个 <code class="prettyprint">commit</code> 对象。在 <code class="prettyprint">Git</code> 里面，将 <code class="prettyprint">HEAD</code> 文件没有指向 <code class="prettyprint">master</code> 的这个现象称之为 <code class="prettyprint">detached HEAD</code>。<br>
<br>这里不管 <code class="prettyprint">HEAD</code> 文件指向的是分支名称也好，是 <code class="prettyprint">commit</code> 对象也罢，其实本质都是一样的，因为分支名称也是指向某个 <code class="prettyprint">commit</code> 对象的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/87a70e24f6018a584f983790d74de5ea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/87a70e24f6018a584f983790d74de5ea.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint"># 左边执行<br>
$ git checkout 6e4a700<br>
$ git log<br>
<br>
# 右边执行<br>
$ glo = git log<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/212615da7d5c8ae8461276de1b520d47.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/212615da7d5c8ae8461276de1b520d47.png" class="img-polaroid" title="28.png" alt="28.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当我们切换到指定的 <code class="prettyprint">commit</code> 的时候，如果需要在对应的 <code class="prettyprint">commit</code> 上继续修改代码提交的话，可以使用上述图片中提及的 <code class="prettyprint">swtich</code> 命令创建新分支，再进行提交。但是，通常我们都不会着玩，都会使用 <code class="prettyprint">checkout</code> 命令来创建新分支的。<br>
<pre class="prettyprint">$ git checkout -b tmp<br>
$ git log<br>
</pre><br>
即使可以这样操作，我们也很少使用。还记得我们上一章节创建的 <code class="prettyprint">dev</code> 分支吗？我们创建了该分支并有了一个新的提交，但是没有合并到 <code class="prettyprint">master</code> 分支就直接删除了。现在再使用 <code class="prettyprint">log</code> 命令查看的话，是看不到了。<br>
<br>实际，真的看不到了吗？大家要记住，在 <code class="prettyprint">Git</code> 里面任何的操作，比如分支的删除。它只是删除了指向某个特定 <code class="prettyprint">commit</code> 的指针引用而已，而那个 <code class="prettyprint">commit</code> 本身并不会被删除，即 <code class="prettyprint">dev</code> 分支的那个 <code class="prettyprint">commit</code> 提交还是在的。<br>
<br>那我们怎么找到这个 <code class="prettyprint">commit</code> 呢？找到之后，我们就可以在上面继续工作，或者找到之前的文件数据等。<br>
<br>第一种方法：<br>
<ul><li>[费劲不太好，下下策]</li><li>在 <code class="prettyprint">objects</code> 目录下面，自己一个一个看，然后切换过去。</li></ul><br>
<br>第二种方法：<br>
<ul><li>[推荐的操作方式]</li><li>使用 <code class="prettyprint">Git</code> 提供的 <code class="prettyprint">git reflog</code> 专用命令来查找。</li><li>该命令的作用就是用于将我们之前的所有操作都记录下来。</li></ul><br>
<br><pre class="prettyprint"># 左边执行<br>
$ git reflog<br>
$ git checkout 9fb7a14<br>
$ git checkout -b dev<br>
<br>
# 右边执行<br>
$ glo = git log<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/bcae669810d76dad266f431df2afc778.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/bcae669810d76dad266f431df2afc778.png" class="img-polaroid" title="29.png" alt="29.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/1398849436ea317abe513c9da6611235.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/1398849436ea317abe513c9da6611235.png" class="img-polaroid" title="30.png" alt="30.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>聊聊 diff 的执行逻辑</h3><em>当我们执行 diff 命令之后，Git 的逻辑它们是怎么对比出来的呢？</em><br>
<br>就在本节中中，我们使用上节的仓库，修改文件内容之后，看看 <code class="prettyprint">diff</code> 命令都输出了哪些内容呢？我们这里一起来看看，研究研究！<br>
<pre class="prettyprint">$ echo "hello" > file1.txt<br>
$ git diff<br>
$ git cat-file -p 42d9955<br>
$ git cat-file -p ce01362<br>
<br>
# 下述命令原理也是一样的<br>
$ git diff --cached<br>
$ git diff HEAD<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/01fe065000e5a5e549c99ac64bd3b58c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/01fe065000e5a5e549c99ac64bd3b58c.png" class="img-polaroid" title="31.png" alt="31.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Git 如何添加远程仓库</h3><em>如何将我们本地的仓库和远程服务器上面的仓库关联起来呢？</em><br>
<h4>初始化仓库</h4><pre class="prettyprint">$ git init<br>
$ git add README.md<br>
$ git commit -m "first commit"<br>
</pre><br>
<h4>关联远程仓库</h4>当我们使用上述命令来关联远程服务器仓库的时候，我们本地 <code class="prettyprint">.git</code> 目录也是会发生改变的。通过命令查看 <code class="prettyprint">.git/config</code> 文件的话，可以看到配置文件中出现了 <code class="prettyprint">[remote]</code> 字段。<br>
<pre class="prettyprint"># 关联远程仓库<br>
$ git remote add origin git@github.com:escapelife/git-demo.git<br>
</pre><br>
<pre class="prettyprint">➜ cat .git/config<br>
[core]<br>
repositoryformatversion = 0<br>
filemode = true<br>
bare = false<br>
logallrefupdates = true<br>
ignorecase = true<br>
precomposeunicode = true<br>
<br>
[remote "origin"]<br>
url = git@github.com:escapelife/git-demo.git<br>
fetch = +refs/heads/*:refs/remotes/origin/*<br>
</pre><br>
<h4>推送本地分支</h4>当我们执行如下命令，将本地 <code class="prettyprint">master</code> 分支推送到远程 <code class="prettyprint">origin</code> 仓库的 <code class="prettyprint">master</code> 分支。之后，我们登陆 <code class="prettyprint">GitHub</code> 就可以看到推送的文件及目录内容了。<br>
<br>推送分支内容的时候，会列举推送的 <code class="prettyprint">objects</code> 数量，并将其内容进行压缩，之后推送到我们远程的 <code class="prettyprint">GitHub</code> 仓库，并且创建了一个远程的 <code class="prettyprint">master</code> 分支（<code class="prettyprint">origin</code> 仓库）。<br>
<pre class="prettyprint"># 推送本地分支<br>
$ git push -u origin master<br>
</pre><br>
推送之后，我们可以发现，本地的 <code class="prettyprint">.git</code> 生成了一些文件和目录，它们都是什么呢？如下所示，会新增四个目录和两个文件，皆为远程仓库的信息。当我们通过命令查看 <code class="prettyprint">master</code> 这个文件的内容时，会发现其也是一个 <code class="prettyprint">commit</code> 对象。此时与我们本地 <code class="prettyprint">master</code> 分支所指向的一致。而其用于表示远程仓库的当前版本，用于和本地进行区别和校对的。<br>
<pre class="prettyprint">➜ tree .git<br>
├── logs<br>
│&nbsp;&nbsp; ├── HEAD<br>
│&nbsp;&nbsp; └── refs<br>
│&nbsp;&nbsp;     ├── heads<br>
│&nbsp;&nbsp;     │   ├── dev<br>
│&nbsp;&nbsp;     │   ├── master<br>
│&nbsp;&nbsp;     │   └── tmp<br>
│       └── remotes     # 新增目录<br>
│&nbsp;&nbsp;         └── origin  # 新增目录<br>
│&nbsp;&nbsp;             └── master  # 新增文件<br>
└── refs<br>
├── heads<br>
│&nbsp;&nbsp; ├── dev<br>
│&nbsp;&nbsp; ├── master<br>
│&nbsp;&nbsp; └── tmp<br>
├── remotes     # 新增目录<br>
│&nbsp;&nbsp; └── origin  # 新增目录<br>
│&nbsp;&nbsp;     └── master  # 新增文件<br>
└── tags<br>
</pre><br>
<h3>远程仓库存储代码</h3><em>使用 GitLab 来了解远程仓库的服务器到底是如何存储，我们的代码的！</em><br>
<br>当我们编写完代码之后，将其提交到对应的远程服务器上面，其存储结构和我们地址是一模一样的。如果我们仔细想想的话，不一样的话才见怪了。<br>
<br><code class="prettyprint">Git</code> 本来就是代码的分发平台，无中心节点，即每个节点都是主节点，所以其存储的目录结构都是一直的。这样，不管哪一个节点的内容发生丢失或缺失的话，我们都可以通过其他节点来找到。而 <code class="prettyprint">Git</code> 服务器就是一个可以帮助我们，实时都可以找到的节点，而已。<br>
<br>原文链接：<a href="https://www.escapelife.site/posts/da89563c.html" rel="nofollow" target="_blank">https://www.escapelife.site/posts/da89563c.html</a>，作者：Escape
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            