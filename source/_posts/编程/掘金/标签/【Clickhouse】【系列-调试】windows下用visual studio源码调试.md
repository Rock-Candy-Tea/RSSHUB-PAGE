
---
title: '【Clickhouse】【系列-调试】windows下用visual studio源码调试'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6463e35e5fd34f6281de0ad68afe0f7e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 17:24:12 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6463e35e5fd34f6281de0ad68afe0f7e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">克隆源码</h2>
<p><code>git clone --recursive https://github.com/yandex/ClickHouse.git</code></p>
<h2 data-id="heading-1">安装VS 2019</h2>
<p>略</p>
<h2 data-id="heading-2">执行camke</h2>
<p>进入到<code>Clickhouse</code>目录，创建<code>build</code>文件夹。进入<code>build</code>目录，执行<code>cmake .. -DCMAKE_BUILD_TYPE=Debug</code>。这个命令虽简单，但是在<code>Windows</code>下，可能会出现很多问题。我们接下来一一解决。</p>
<h2 data-id="heading-3">提示<code>Cannot enable LDAP support</code></h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6463e35e5fd34f6281de0ad68afe0f7e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>原因是未安装<code>OpenLdap</code>，在下地址：
<a href="https://www.maxcrc.de/wp-content/uploads/2020/04/OpenLDAPforWindows_x64.zip" target="_blank" rel="nofollow noopener noreferrer">www.maxcrc.de/wp-content/…</a>
安装后直接下一步、下一步完成，然后手动执行命令启动:</p>
<pre><code class="copyable">cd OpenLdap安装目录
slapd -d 1 -f slapd.conf
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等待出现下图即可重新<code>cmake</code>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/300ae1da54324935b8513194287df1cc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">提示找不到<code>zlib</code>模块</h2>
<p>按照以下命令执行，克隆<code>zlib</code>源码，并执行<code>submodule</code>更新命令</p>
<pre><code class="copyable">git clone https://github.com/madler/zlib.git
git submodule update --init --recursive
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">执行到<code>CMakeLists.txt</code>的第<code>122</code>行报错：</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f66b537c4454a98a56e73abb0a3f834~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>该错误原因是未安装<code>nasm</code>。下载地址：<a href="https://www.nasm.us/pub/nasm/releasebuilds/2.14.02/win64/nasm-2.14.02-installer-x64.exe" target="_blank" rel="nofollow noopener noreferrer">www.nasm.us/pub/nasm/re…</a>
下载后直接安装即可。安装后再次<code>cmake</code>。</p>
<h2 data-id="heading-6">提示找不到<code>Python</code></h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0884c062d9d84e948aebd6056d79d4e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>该错误原因是没有安装<code>Python</code>，下载地址：
<a href="https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe" target="_blank" rel="nofollow noopener noreferrer">www.python.org/ftp/python/…</a>
下载后直接安装，安装完成后再次<code>cmake</code></p>
<h2 data-id="heading-7">提示不支持<code>Windows</code></h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80d68d6deaa049d59d2c2f36f02c9e39~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们打开<code>contrib/libhdfs3-cmake/CMakeLists.txt</code>文件，然后注释第<code>33</code>行后再次<code>cmake</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c43731d5bc894234b3dcfa3afad0d25a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">提示找不到<code>OpenSSL</code></h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9941e06b03d94718aa7fac9e5d0942f2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里请使用<code>vcpkg</code>工具安装<code>OpenSSL</code>，安装<code>vcpkg</code>的操作如下，<code>vcpkg</code>使用说明请自行Google。</p>
<pre><code class="copyable">git clone https://github.com/microsoft/vcpkg
cd vcpkg
双击执行 bootstrap-vcpkg.bat # 执行完成后会在同级目录生成vcpkg.exe文件，将其加入到Path中
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行命令<code>vcpkg install openssl:x64-windows</code>安装<code>OpenSSL</code>，执行过程中如果报错：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/136817e4ef604168bc41d93231dd37fb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>则需要在<code>Visual Studio</code>上安装英文的语言包。找到VS的安装目录<code>installer</code>，执行<code>vs_installer.exe</code>，选择安装的版本后的修改，再选择语言包，勾选上英文，确认修改。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cec1b2affa04b6f8a9974540650fe9e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/776a376313e3435baa525b716588e15a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>详细安装步骤参考：<a href="https://blog.csdn.net/tutucoo/article/details/85064786" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/tutucoo/art…</a></p>
<p>VS的英文语言包安装完成后，再次执行<code>vcpkg install openssl:x64-windows</code>，出现以下信息即可：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/876b1f50085b4bff90ec69ec85deafea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后将安装的<code>OpenSSL</code>的<code>bin</code>目录（在<code>vcpkg</code>安装目录下）<code>vcpkg\installed\x64-windows\bin</code>加入到系统环境变量中，最后再次<code>cmake</code></p>
<h2 data-id="heading-9"><code>cmake</code>成功</h2>
<p>看到以下信息就表示我们编译成功了~~~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e316b07633540e4a63e357089e2679f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">执行<code>ninja</code>命令报错</h2>
<blockquote>
<p><code>cmake ..</code>执行成功后，接着我们需要执行<code>ninja clickhouse</code>。<code>Windows</code>下该命令会遇到一系列问题。</p>
</blockquote>
<p>在<code>Windows</code>下没有<code>ThIRDPART_HOME</code>目录，因此，在<code>contrib/rocksdb/thirdparty.inc</code>编译时会提示多个包不存在：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83d5242c67dd433593e0574ba37cf59d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/390a0640f190486faf24cc771dc1b970~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99fe30ea19534d18b41e411065545c30~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>出现以上类似的xx.lib找不到的错误，需要执行以下全部命令安装<code>c++</code>库：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">vcpkg install gflags:x64-windows
vcpkg install snappy:x64-windows
vcpkg install zlib:x64-windows
vcpkg install zstd:x64-windows
vcpkg install jemalloc:x64-windows
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成后，进入<code>contrib/rocksdb/thirdparty.inc</code>文件，修改多个库的地址：</p>
<pre><code class="copyable"># 示范：找到下面的定义位置，路径改为vcpkg安装的库的.lib文件路径
set(GFLAGS_LIB_DEBUG xxx/vcpkg/packages/gflags_x64-windows/lib/gflags.lib)
set(GFLAGS_LIB_RELEASE xxx/vcpkg/packages/gflags_x64-windows/lib/gflags.lib)

// 其他几个包类似，可以搜索_LIB_来修改

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果出现下方的错误，提示<code>result_of</code>不是<code>std</code>的成员：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33460f7b6ac64cdb8fd5ff067b8e8127~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是因为在c++2017以后，已经没有<code>result_of</code>函数了，改成了<code>invoke_result_t</code>，所以我们需要进入源码修改，文件为<code>contrib/abseil-cpp/absl/meta/type_traits.h</code>，修改<code>620</code>行为:</p>
<pre><code class="copyable">using result_of_t = typename std::invoke_result_t<T>::type; // 替换原来的result_of
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果出现下列错误，则是因为没有安装<code>cygwin</code>，下载地址：<a href="https://www.cygwin.com/" target="_blank" rel="nofollow noopener noreferrer">www.cygwin.com/</a> ：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d424d68e27ad4db0b19f9ad040494773~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然而。。。安装了<code>cygwin</code>后，问题更艰难了。。。</p>
<p>。。。</p>
<h2 data-id="heading-11">过程很凄惨、结局很光明</h2>
<p>好吧，最后我放弃了。在Windows上调试<code>Clickhouse</code>恐怕难度不小。我转Linux了。安装了<code>VirtualBox</code>虚拟机，并启动了一个<code>Ubuntu</code>系统，然后按照官网教程，很快就在跑<code>ninja clickhouse</code>命令了，而且基本没有出现什么问题。就是这个命令执行时间有点长，已经跑了1个多小时了。。。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4f93d42e32241b991c6ca70ac7eb16f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            